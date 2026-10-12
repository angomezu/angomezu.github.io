"""Check the static portfolio without a build step or third-party dependencies."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
VOID = set("area base br col embed hr img input link meta param source track wbr".split())


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.refs = []
        self.external = set()
        self.errors = []
        self.stack = []
        self.images = 0
        self.h1s = 0
        self.structured = []
        self.in_json = False

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        line = self.getpos()[0]
        if tag not in VOID:
            self.stack.append(tag)
        if len(data) != len(attrs):
            self.errors.append(f"Line {line}: duplicate attributes")
        if "id" in data:
            self.ids.append(data["id"])
        if tag == "html" and not data.get("lang"):
            self.errors.append("Missing document language")
        if tag == "h1":
            self.h1s += 1
        if tag == "img":
            self.images += 1
            for required in ("src", "alt", "width", "height"):
                if required not in data:
                    self.errors.append(f"Line {line}: image missing {required}")
        for attr in ("href", "src", "data-animation-source", "data-still-source"):
            if attr in data:
                self.refs.append((data[attr], line))
        if tag == "a":
            href = data.get("href", "")
            if href.startswith(("http://", "https://")):
                self.external.add(href)
            if data.get("target") == "_blank" and "noopener" not in data.get("rel", "").split():
                self.errors.append(f"Line {line}: new-tab link missing noopener")
        if tag == "script" and data.get("type") == "application/ld+json":
            self.in_json = True

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag not in VOID:
            if not self.stack or self.stack[-1] != tag:
                self.errors.append(f"Line {self.getpos()[0]}: unexpected closing {tag}")
            else:
                self.stack.pop()
        if tag == "script":
            self.in_json = False

    def handle_data(self, data):
        if self.in_json:
            self.structured.append(data)


def check_remote(url):
    request = Request(url, headers={"User-Agent": "Mozilla/5.0 (portfolio-link-check)"})
    try:
        with urlopen(request, timeout=20) as response:
            return "PASS", url, str(response.status)
    except HTTPError as error:
        kind = "REVIEW" if error.code in (401, 403, 429, 999) else "FAIL"
        return kind, url, f"HTTP {error.code}"
    except (URLError, TimeoutError, OSError) as error:
        return "REVIEW", url, str(error)


def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("--external", action="store_true", help="Check public anchor links")
    options = args.parse_args()
    parser = SiteParser()
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    parser.feed(html)
    parser.close()
    errors = parser.errors
    if re.search(r"\bacademic (?:portfolio|CV)\b", html, re.IGNORECASE):
        errors.append("Use Research Portfolio and CV labels")
    source_types = {".html", ".css", ".js", ".svg", ".xml", ".txt", ".md", ".py"}
    for source in ROOT.rglob("*"):
        if any(part in {".git", "node_modules", ".playwright-mcp"} for part in source.parts):
            continue
        if source.is_file() and source.suffix in source_types:
            if "\u2014" in source.read_text(encoding="utf-8-sig"):
                errors.append(f"U+2014 punctuation remains in {source.relative_to(ROOT)}")
    study_title = "Plant Organ Segmentation from 3D LiDAR Point Clouds"
    if html.count(study_title) != 1:
        errors.append("Present the plant segmentation research once")
    if parser.stack:
        errors.append(f"Unclosed elements: {parser.stack}")
    duplicates = [name for name, count in Counter(parser.ids).items() if count > 1]
    if duplicates:
        errors.append(f"Duplicate IDs: {duplicates}")
    if parser.h1s != 1:
        errors.append(f"Expected one main heading; found {parser.h1s}")
    local = set()
    fragments = set()

    def check_ref(ref, base, line):
        parts = urlsplit(ref)
        if parts.scheme or parts.netloc:
            return
        if parts.path:
            path = (base / unquote(parts.path)).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file():
                errors.append(f"Line {line}: missing or invalid local file {ref}")
            else:
                local.add(path)
        if parts.fragment and (not parts.path or parts.path == "index.html"):
            fragments.add(parts.fragment)
            if parts.fragment not in parser.ids:
                errors.append(f"Line {line}: missing anchor #{parts.fragment}")

    for ref, line in parser.refs:
        check_ref(ref, ROOT, line)
    for ref in re.findall(r"url\(\s*['\"]?([^)'\"]+)", (ROOT / "assets/style.css").read_text()):
        check_ref(ref, ROOT / "assets", "CSS")
    try:
        person = json.loads("".join(parser.structured))
        if person.get("@type") != "Person":
            errors.append("Expected Person structured data")
        sitemap = ET.parse(ROOT / "sitemap.xml")
        locations = [element.text for element in sitemap.iter() if element.tag.endswith("}loc")]
        if locations != ["https://angomezu.github.io/"]:
            errors.append(f"Unexpected sitemap locations: {locations}")
    except (ValueError, ET.ParseError) as error:
        errors.append(f"Invalid structured metadata: {error}")
    if not (ROOT / ".nojekyll").is_file():
        errors.append("Missing .nojekyll")
    if "Sitemap: https://angomezu.github.io/sitemap.xml" not in (ROOT / "robots.txt").read_text():
        errors.append("robots.txt sitemap mismatch")
    cv = ROOT / "assets/docs/Angel_Barrera_Academic_CV.pdf"
    if not cv.is_file() or not cv.read_bytes().startswith(b"%PDF-"):
        errors.append("Missing or invalid academic CV PDF")
    print(f"Checked {len(parser.refs)} references, {len(local)} local files, "
          f"{len(fragments)} anchors, {parser.images} images, and metadata.")
    for error in errors:
        print(f"FAIL: {error}")
    if not errors:
        print("PASS: all local site checks")
    if options.external:
        with ThreadPoolExecutor(max_workers=8) as pool:
            for kind, url, status in pool.map(check_remote, sorted(parser.external)):
                print(f"{kind}: {url} ({status})")
                if kind == "FAIL":
                    errors.append(f"Broken external link: {url}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
