# Research profile refresh — November 2026

This change presents Angel A. Barrera Gómez's professional and research profile through a research-led homepage, selected engineering work, talks, background, and a separate printable résumé page.

The wording is based on the latest supplied professional résumé (October 30, 2026). Research is classified as a proposal, completed applied team research, or an undergraduate thesis; no peer-reviewed publication or grant is implied. The legacy academic CV remains unchanged and clearly labeled.

Updated: `index.html`, `assets/style.css`, `assets/script.js`, `sitemap.xml`, and `scripts/validate_site.py`.
Added: `resume.html`, `assets/docs/Angel_Barrera_Resume_2026.docx`.

The new résumé page is printable from the browser. A separately typeset PDF exists in the design package but is **not** included in this GitHub commit; do not publish a broken PDF URL. This text-first distribution preserves the exact Word source while the static site and print view are reviewed.

Validation:
```sh
python scripts/validate_site.py
node --check assets/script.js
git diff --check
```
Browser validation for desktop, mobile, keyboard navigation, contrast, and résumé print layout is required before merging.

All pre-existing images, original PDF assets, .nojekyll and legacy URLs must remain intact.
