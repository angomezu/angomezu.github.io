# Research profile update — November 2026

## Scope
A research-first personal website with an original academic editorial layout, selected research, enterprise engineering highlights, speaking engagements, education, experience, and a dedicated résumé page.

Updated files: `index.html`, `resume.html`, `assets/style.css`, `assets/script.js`, `sitemap.xml`, and `scripts/validate_site.py`. The original images, academic CV, legacy projects and URLs remain in the repository. The current Word résumé is `assets/docs/Angel_Barrera_Resume_2026.docx` and corresponds to the owner's October 30, 2026 master document.

The résumé webpage is print-ready: use **Print / Save PDF**. A separately hosted dated résumé PDF was typeset and inspected during development but is not part of this branch; do not add a dead link or claim one is deployed.

## Editorial approach
Claims about research are qualified by status: completed ETSU/ORNL collaboration, undergraduate thesis, and a prospective UEES governance research proposal. The page does not imply peer-reviewed publications, funded study results, or completed empirical findings where none were documented. The enterprise experience and selected project claims are drawn from the supplied master résumé; no additional privileged access paths or credentials are published.

## Checks executed
- Python static site validator: PASS (both pages, paths, anchors, image references, Word document signature, metadata and sitemap).
- `node --check assets/script.js`: PASS.
- CSS parser (tinycss2): PASS.
- `git diff --cached --check` on a local validation tree: PASS.
- Word source equality: matched the supplied original.
- Separately prepared résumé PDF: two US-letter pages, searchable text; not included in GitHub branch.
- Chromium DOM/rendering QA using in-memory documents and locally available **proxy** image files (direct navigation blocked by the environment): no horizontal overflow at 320, 375, 560, 768, 800, 801, 1024, 1440 and 1920 pixels; responsive navigation, Escape-to-close/focus restoration, animation toggle, image decoding for proxy assets, and résumé page layout passed.
- A real narrow-screen overflow in the research section was found and corrected in CSS in commit `edc070f`.

## Limits
The Chromium session blocks navigation to local, HTTP and data URLs, so the DOM QA used in-memory HTML, inline CSS/JS and proxy images. This does **not** verify the real full-resolution images or external URLs in-browser. Live GitHub Pages checks are required after merge. Static GitHub Pages hosting requires no build step.

## URLs
- Homepage: https://angomezu.github.io/
- Résumé: https://angomezu.github.io/resume.html
- Source: https://github.com/angomezu/angomezu.github.io
