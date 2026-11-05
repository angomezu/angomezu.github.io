"""Validate the static research portfolio in a checked-out repository."""
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
VOID=set("area base br col embed hr img input link meta param source track wbr".split())

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids=[];self.refs=[];self.errors=[];self.stack=[];self.headings=0;self.jsonparts=[];self.in_json=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if len(a)!=len(attrs):self.errors.append("Duplicate HTML attribute")
        if "id" in a:self.ids.append(a["id"])
        if tag=="h1":self.headings+=1
        if tag=="img":
            for k in ("src","alt","width","height"):
                if k not in a:self.errors.append("Image missing "+k)
        for k in ("src","href","data-animation-source","data-still-source"):
            if k in a:self.refs.append(a[k])
        if tag=="a" and a.get("target")=="_blank" and "noopener" not in a.get("rel","").split():
            self.errors.append("New-tab link missing noopener")
        if tag=="script" and a.get("type")=="application/ld+json":self.in_json=True
        if tag not in VOID:self.stack.append(tag)
    def handle_startendtag(self,tag,attrs):
        self.handle_starttag(tag,attrs)
        if tag not in VOID:self.handle_endtag(tag)
    def handle_endtag(self,tag):
        if tag not in VOID:
            if not self.stack or self.stack[-1]!=tag:self.errors.append("Unexpected closing "+tag)
            else:self.stack.pop()
        if tag=="script":self.in_json=False
    def handle_data(self,data):
        if self.in_json:self.jsonparts.append(data)

def main():
    errors=[]; checked=set(); allpages={}
    for name in ("index.html","resume.html"):
        path=ROOT/name
        if not path.is_file():errors.append("Missing "+name);continue
        content=path.read_text(encoding="utf-8")
        parser=Parser();parser.feed(content);parser.close();allpages[name]=parser
        errors+= [name+": "+e for e in parser.errors]
        if parser.stack:errors.append(name+": unclosed elements "+str(parser.stack))
        if parser.headings!=1:errors.append(name+": expected one H1")
        dup=[v for v,n in Counter(parser.ids).items() if n>1]
        if dup:errors.append(name+": duplicate ids "+str(dup))
        if name=="index.html":
            try:
                if json.loads("".join(parser.jsonparts)).get("@type")!="Person":errors.append("Incorrect Person JSON-LD")
            except ValueError:errors.append("Invalid JSON-LD")
        for ref in parser.refs:
            x=urlsplit(ref)
            if x.scheme or x.netloc or ref.startswith(("mailto:","tel:")):continue
            if x.path:
                target=(ROOT/unquote(x.path)).resolve()
                if not target.is_relative_to(ROOT) or not target.is_file():errors.append(name+": missing local file "+ref)
                else:checked.add(str(target.relative_to(ROOT)))
            if x.fragment:
                dest=allpages.get(x.path or name)
                if x.path in ("","index.html","resume.html"):
                    if not dest and x.path:
                        dest=Parser();dest.feed((ROOT/x.path).read_text(encoding="utf-8"))
                    if dest and x.fragment not in dest.ids:errors.append(name+": broken anchor "+ref)
    for name in (".nojekyll","robots.txt","sitemap.xml","assets/docs/Angel_Barrera_Resume_2026.docx","assets/docs/Angel_Barrera_Academic_CV.pdf"):
        if not (ROOT/name).is_file():errors.append("Missing "+name)
    for name,signature in (("assets/docs/Angel_Barrera_Resume_2026.docx",b"PK"),("assets/docs/Angel_Barrera_Academic_CV.pdf",b"%PDF-")):
        path=ROOT/name
        if path.is_file() and not path.read_bytes().startswith(signature):errors.append("Invalid signature "+name)
    try:
        xml=ET.parse(ROOT/"sitemap.xml")
        urls=[e.text for e in xml.iter() if e.tag.endswith("}loc")]
        expected={"https://angomezu.github.io/","https://angomezu.github.io/resume.html"}
        if set(urls)!=expected:errors.append("Sitemap mismatch")
    except (ET.ParseError,FileNotFoundError) as ex:errors.append("Invalid sitemap: "+str(ex))
    for name in ("assets/style.css","assets/script.js"):
        if not (ROOT/name).is_file():errors.append("Missing "+name)
    print("Validated",len(allpages),"HTML pages and",len(checked),"local assets")
    if errors:
        for error in errors:print("FAIL:",error)
        return 1
    print("PASS: all static site checks")
    return 0
if __name__=="__main__":sys.exit(main())
