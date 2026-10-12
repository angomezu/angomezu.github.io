# Angel A. Barrera Gómez: Research Portfolio

Static portfolio for PhD applications in Data & AI Governance, Responsible AI,
Information Systems, and Applied Machine Learning.

## Local preview

From the repository root:

```powershell
python -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000>. Stop the server with Ctrl+C.

## Validation

```powershell
python scripts/validate_site.py
python scripts/validate_site.py --external
node --check assets/script.js
git diff --check
```

The Python check uses only the standard library. External checks require network
access; access restrictions and transient errors are reported separately.
Optional HTML linting: `npx --yes html-validate@11.16.2 index.html`.

## Site files

- `index.html`: introduction, speaking, research experience, six engineering
  projects, education, professional experience, and academic contact links.
- `assets/style.css`, `assets/script.js`: responsive layout and progressively
  enhanced mobile navigation. Content and navigation work without JavaScript.
- `assets/images/`: event photographs, the full-resolution portrait, and an animation still.
- `assets/docs/Angel_Barrera_Academic_CV.pdf`: supplied three-page CV.
- `assets/favicon.svg`, `robots.txt`, `sitemap.xml`: identity and search metadata.
- `.nojekyll`: existing GitHub Pages configuration, preserved unchanged.
- `docs/PORTFOLIO_REVIEW.md`: source audit, validation results, and review items.

Older assets and the prior resume remain at their original URLs to preserve
existing links. Selected project images are reused in the new design. The portrait WebP preserves the original photograph at 1792 x 2084 pixels.
The complete original GIF is lazy-loaded in Research Experience, with a pause
control and a reduced-motion still image.

## GitHub Pages compatibility

The repository root is directly deployable as static files; there is no build
step, package installation, external font, or runtime service dependency. The
production canonical URL is `https://angomezu.github.io/`. Repository history,
branch, and existing `.nojekyll` have been retained.

This implementation remains local on `feat/phd-research-portfolio`. No commit,
push, merge, deployment, or GitHub Pages settings change was performed. Review
the source audit and CV before deciding to publish.
