# Portfolio implementation and review

Reviewed October 10, 2026 (America/Chicago). This report accompanies local,
uncommitted changes on `feat/phd-research-portfolio`.

## Editorial redesign (current)

Reviewed the rendered starting page at desktop and mobile sizes, then inspected
the original `index.html` and `assets/style.css` through Git history. The original
design used a compact, person-focused sidebar and system typography. The current
page's main weaknesses were a keyword-led introduction, an isolated portrait
panel, and similar bordered cards for talks, research, and engineering projects.

Rebuilt the page composition and stylesheet as one design rather than adding
overrides to the prior card layout. Retained the original system font stack,
navy (#10243A), blue (#245A81), white, and slate. Secondary text on light-gray
surfaces uses a darker slate for contrast. No imported fonts, gradients, rounded
cards, decorative animations, frameworks, or new dependencies were introduced.

- Introduction: uses the two owner-supplied paragraphs verbatim, with the full
  name and uncropped 1792 x 2084 portrait integrated into the composition. Current
  role reads Data Governance Lead, CenterPoint Energy, Houston, Texas. CV and
  research actions remain. Removed the research-interest eyebrow and keyword list.
- Speaking: remains first. A large DD Youth photograph leads the section; the
  UEES student photograph and webinar presentation have different proportions.
  The authentic poster, full presentation, and session screenshot remain available.
  Added 2025 to the UEES student presentation using the owner's explicit latest
  instruction, rather than inferring the year from the photograph. DD Youth 2024
  and the October 9, 2026 UEES/Evolium webinar retain their titles and descriptions.
- Research: the completed ETSU/ORNL study leads with problem, team contribution,
  methodology, project-reported results, unpublished-manuscript status, and code.
  Its original animated demonstration is prominent beside the methods, with both
  scanning photographs below. The UEES study remains a prospective proposal with
  intended evaluation and a CV reference; the undergraduate work remains a
  completed monograph catalogued as a thesis. No new publication claim was added.
- Engineering: preserved all six remaining projects and repository URLs. Two
  illustrated features, two visual studies, and two shorter entries replace the
  uniform grid. Existing extraction-output and seller-dashboard images are linked
  as supporting documentation. Evaluation limits and technical details remain.
- Background: separate education and Professional Experience lists with aligned
  dates and descriptions. All six employment/assistantship entries remain, and
  CenterPoint is explicitly identified as a contract assignment.
- Structure: introduction, speaking, research, projects, education/experience,
  contact. Numbering is 01 through 04. Existing navigation anchors are preserved;
  the research agenda remains absent. Titles and metadata now say Research Portfolio.

After the initial implementation, reviewed desktop, tablet, and mobile captures
and performed a second refinement pass. Reduced the tablet portrait column to
remove excess space before the introduction, improved the small role/education
text, removed repeated methodology wording, simplified the engineering section
introduction, and preserved matching document/visual order for the CRM entry on
mobile. Final desktop, tablet, mobile, and 2x-density portrait captures were
reviewed visually. Photographs preserve natural proportions without cropping.

### Validation after the editorial redesign

- `python scripts/validate_site.py --external`: PASS. Checked 60 references,
  20 local files, six anchors, 12 images, and structured/search metadata. Thirteen
  external URLs returned HTTP 200. LinkedIn returned HTTP 999 (manual review).
- `html-validate@11.16.2`: PASS with default recommended rules.
- `stylelint@17.16.0`: PASS with the existing temporary syntax/rules configuration.
- `node --check assets/script.js`: PASS. Existing navigation and animation behavior
  needed no JavaScript changes.
- Chromium responsive measurements: no horizontal overflow or offscreen content
  at actual widths 320, 375, 560, 768, 800, 802, 1024, 1440, and 1920 pixels.
  The requested 801 setting was reported as 802 by the browser environment.
- Axe 4.14.0 WCAG 2.1 A/AA checks at 320, 768, and 1440 pixels: zero violations
  and no incomplete checks. Keyboard checks passed for skip-link/main focus,
  Space menu activation, Tab navigation, Escape close and focus restoration,
  selection/outside-click close, breakpoint reset, and back-to-top. All section
  targets remain below the sticky header. Automated checks do not constitute
  a full screen-reader or cross-browser certification.
- All 12 on-page images decoded successfully. No failed local requests or
  JavaScript page errors. High-resolution portrait visually inspected at 2x density.
- Fresh browser context: GIF not requested during the initial screen load;
  requested on approach to research. Frame screenshots differed during playback
  and after resume, and matched while paused. Space/Enter operate the pause/play
  button. Reduced motion selects the still; changing back restores animation.
  Original GIF retains 900 x 650 dimensions, 400 frames, 12 seconds, and looping.
- JavaScript-disabled mobile context: visible navigation, working research
  anchor, readable content, and no horizontal overflow. Hidden enhancement
  controls do not appear without JavaScript.
- Rendered text contains no prohibited portfolio/CV labels or U+2014 punctuation.
  Source scan passed. Plant research appears exactly once, with three research
  entries and six technical projects confirmed in the DOM.
- All 28 original/supplied assets matched pre-redesign SHA-256 hashes, including
  the CV, original portrait, event photographs, supporting media, and GIF.
  CV SHA-256 remains
  `e515e31e808d3915c8487b4a3ce380cbb6d6f0d150a0ea3d5d8fbd742e3cda57`.
- `.nojekyll`, branch, and HEAD remain unchanged. Static files require no build.
  No commit, push, merge, deployment, or Pages configuration change was made.

Files edited in this pass: `index.html`, `assets/style.css`, and this report.
No site file or media asset was added or deleted during this redesign. Earlier
authorized integration files remain in the working tree for review. Browser
captures and lint packages are kept outside the repository.

Remaining concerns: LinkedIn requires manual checking; the UEES institutional
record is still HTTP-only; the original GIF is approximately 15.3 MB once loaded.
The CV remains unchanged and subject to its separate factual review. Existing
credential/title verification items in the source audit below still apply.

## Typography, media, and research corrections (previous pass)

Restored the original font stack exactly:
`ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif`.
Removed letter spacing and uppercase treatments from small headings, moderated
heading sizes, and improved spacing around methodology. Navy, blue, white, and
slate colors remain. No imported fonts or decorative typefaces are used.

The header/footer now use Research Portfolio. Navigation and buttons use CV,
View CV, and Download CV. Formal degree and research terminology remains intact.
Removed all U+2014 punctuation from website sources, using a title separator,
colon, comma, and "to" in date ranges as appropriate. The webinar description's
meaning is preserved, with its punctuation corrected.

The hero now uses `assets/images/angel-barrera-original.webp`, converted from
the original `assets/prof_pic.png` at its complete 1792 x 2084 resolution using
WebP quality 93. The image is 841,650 bytes versus the original 5,813,538 bytes.
No cropping, enlargement, AI generation, or upscaling was performed. Natural
proportions are preserved by intrinsic dimensions and automatic rendered height.
The original PNG is retained unchanged. Desktop and 2x-density image rendering
were visually inspected for detail and sharpness.

Plant Organ Segmentation appears once, under Research Experience at
`#plant-segmentation`. The entry contains the methodology, project-reported
65.58% mean IoU and approximately 82% stem recall, completion/unpublished-work
status, repository link, animated prediction, and both original supporting
photographs. The scanning photograph caption describes the visible scanning
setup. Removed the duplicate plant project from Technical Projects and combined
the remaining six engineering projects into one grid, numbered 01 through 06.
Main section numbering stays 01 through 04. Speaking remains the first content
section, and the research agenda remains absent.

`assets/prediction.gif` is reused unchanged: 900 x 650, 400 frames, 12 seconds,
continuous looping. It is displayed as a native animated image with lazy
loading. A keyboard-operable pause/play control switches between the GIF and a
lossless first-frame still, `assets/images/plant-segmentation-still.webp` (27,078
bytes). Ordinary browsing plays the animation; reduced-motion preferences
default to the still and allow explicit playback. With JavaScript disabled,
the original native GIF and navigation remain available.

The full GIF is 15,292,824 bytes. Its complete animation is preserved, and it
loads only when the research entry approaches the viewport; no animation
conversion or frame removal was performed. On slow connections, the full
demonstration may take time to load.

The CV PDF, original PNG/GIF, and previously supplied event photographs match
the pre-correction SHA-256 hashes. The PDF's content and original file URL are
unchanged. CV factual review remains separate. Speaking descriptions, event
titles, dates, and images are preserved apart from the required punctuation
change. No missing event date was invented.

Current validation results:

- HTML (`html-validate@11.16.2`), CSS syntax/property/selector checks
  (`stylelint@17.16.0`), JavaScript syntax, and Git whitespace checks: PASS.
- Site checker: 51 references, 18 local files, six navigation targets, eleven
  on-page images, Pages marker, PDF signature, and metadata: PASS. Checks now
  also cover animation/still data attributes, prohibited labels, U+2014 in source
  files, and a single plant-research title.
- Source and rendered body/title/metadata/accessible-label checks: no U+2014
  characters or prohibited portfolio/CV labels.
- Nine viewport settings from 320 to 1920 pixels: no horizontal overflow.
  Desktop/mobile introduction and research media layouts visually inspected.
- Browser animation screenshots separated by 450 ms differ during playback and
  after resuming, and match while paused. Reduced-motion default and keyboard
  Space/Enter activation work. Network observation confirmed the GIF was not
  requested during initial hero rendering, then loaded on approaching research.
- Portrait decoded at 1792 x 2084 and retained the original aspect ratio. All
  WebP files passed integrity checks; the lossless still matches GIF frame zero.
  The original GIF still reports all 400 frames and an infinite loop.
- Axe WCAG 2.1 A/AA at 375, 768, and 1440 pixels: zero violations and zero
  incomplete checks. Skip link, focus restoration, ordered navigation, section
  anchors, back-to-top, animation controls, and JavaScript-disabled navigation:
  PASS. No browser page errors or failed requests during playback checks.
- External links: thirteen HTTP 200 responses. LinkedIn continues to return
  HTTP 999 to automated checking and requires manual review.

This correction modifies `index.html`, `assets/style.css`, `assets/script.js`,
`scripts/validate_site.py`, `README.md`, and this report. Adds the full-resolution
portrait WebP and lossless animation still listed above. Deletes no files.
Static GitHub Pages compatibility, `.nojekyll`, branch, HEAD, and Git index are
preserved. No commit, push, merge, or deployment was performed.

## Previous design and structure refinement

The current design uses deep navy `#10243A`, professional blue `#245A81`,
white `#FFFFFF`, and slate gray `#64748B`, with system sans-serif typography,
consistent spacing, and subtle borders. Removed gradients, glow/shadow effects,
translucent header treatments, decorative illustrations, oversized italic
headlines, hover transforms, and the marketing-style introduction. The hero now
leads with the applicant's name and doctoral research interests.

Removed the entire research-agenda section, its introduction, all three interest
cards, and their unused CSS. Current content order:

1. Introduction
2. `01 / Talks & academic outreach`: Sharing Knowledge in Practice (`#speaking`)
3. `02 / Research experience` (`#research`)
4. `03 / Selected technical work` (`#projects`)
5. `04 / Education & experience` (`#background`)
6. Academic contact (`#contact`)

Navigation follows the same order. The research link now targets actual research
experience. Back-to-top targets the page body, avoiding sticky-header anchor
behavior. The mobile header remains in normal flow when JavaScript is disabled,
so the expanded fallback navigation does not obscure section targets.

All three speaking titles, dates, descriptions, and image tags were compared
against the pre-refinement version and match. The UEES student talk still has no
invented date. The webinar poster is displayed in full rather than cropped.
The CV and six supplied photographs/images remain byte-for-byte unchanged;
their SHA-256 hashes match the pre-refinement baseline. CV factual
review remains separate. All seven technical projects remain.

Corrected existing encoding artifacts in project/experience text and removed
redundant decorative link arrows. Updated the favicon to navy/white.

This refinement modifies `index.html`, `assets/style.css`, `assets/favicon.svg`,
`README.md`, and this report. No files were deleted or newly added in this
refinement. The file inventory below includes the preceding integration too.

Latest validation:

- HTML validation (`html-validate@11.16.2`): zero errors/warnings.
- CSS validation (Stylelint, syntax/property/function/selector checks): PASS.
- JavaScript syntax (`node --check assets/script.js`): PASS; navigation script
  itself was retained unchanged.
- Standard-library site checker: PASS; 45 references, 15 local files, six anchor
  targets, and nine on-page images. Metadata and static Pages sentinel pass.
- External links: 13 HTTP 200 responses; LinkedIn still returns HTTP 999 to the
  automated checker and requires manual review.
- Nine viewport settings between 320 and 1920 pixels: no horizontal overflow.
  Desktop, phone introduction, and speaking-section rendering visually reviewed.
- Axe WCAG 2.1 A/AA checks at 375, 768, and 1440 pixels: zero violations and zero
  incomplete checks.
- Keyboard skip link/main focus, Space menu opening, first navigation focus on
  Speaking, Escape focus restoration, link-selection close, outside-click close,
  breakpoint reset, all section anchors, and back-to-top behavior: PASS.
- JavaScript-disabled phone navigation, section targeting without header
  obstruction, reduced-motion behavior, and CV HTTP loading: PASS.
- All nine on-page images decoded; no browser page errors or failed requests.
- `git diff --check`: PASS. Branch and HEAD retained; nothing staged, committed,
  pushed, merged, or deployed. GitHub Pages still requires no build process.

## Initial implementation

Inspected the complete old HTML/CSS, staged HTML/CSS/JavaScript, both supplied
PDFs, staged photographs, tracked file inventory, branch, and recent history
before changing the site. The initial working tree was clean. Starting HEAD:
`0fa1e8103ceb14a7c0ca031d017cae6d6862a3e5`.

Integrated the staged design, portrait, five outreach/event images, favicon, CV,
and search metadata. The introduction explicitly seeks doctoral opportunities
in Data & AI Governance, Responsible AI, Information Systems, and Applied Machine
Learning. Preserved all seven original technical projects and reused five
existing project images. Added the additional employment and graduate
assistantship from the supplied materials.

Research proposals, completed research, undergraduate thesis work, and
unpublished manuscripts have explicit, distinct labels. Removed an unsupported
claim about having performed internal LLM security tests, reframing it as
research questions motivated by practice. Financial extraction checks disclose
that validation reuses extracted content; the site does not claim independent
source verification. EEG performance retains the subject-wise generalization
limitation. The readmission project is identified as coursework with no clinical
validation claim.

Navigation now works without JavaScript, supports keyboard use and Escape focus
restoration, closes after selection/outside clicks and breakpoint changes, and
respects reduced motion. Fixed low-contrast secondary text, an accessible-name
mismatch, incorrect portrait dimensions, and HTML lint issues.

## Academic and factual source audit

Evidence is distinguished from independent verification. A supplied CV supports
applicant-reported information; it is not an institutional transcript or employer
verification. Public repositories support reported methods and results, without
independently reproducing the experiments.

| Claim | Evidence and finding | Website treatment |
| --- | --- | --- |
| 2025 ETSU/ORNL plant segmentation collaboration, methods, authorship, and results | [Research repository](https://github.com/angomezu/geometric-deep-learning-plant-organ-segmentation), its README, and both supplied PDFs agree on the collaboration, Dynamic EdgeConv, geometric descriptors, and 65.58% mean IoU. README reports approximately 82% stem recall. | Completed applied research with team attribution; results described as project-reported. Replaced staged 82.27% with approximately 82%, supported by the README and supplied CVs. |
| Publication status of ORNL work | Repository describes an ongoing manuscript and provides an `@unpublished` citation. No journal acceptance or peer-review evidence was supplied. | Explicitly unpublished manuscript; no peer-reviewed publication claimed. Completion refers to the 2025 project, not manuscript publication. |
| 2026 UEES governance study | Supplied CV describes a prospective study and proposed instrument. No study dataset, results, ethics approval, funding record, institutional appointment, or publication was supplied or located. | Research proposal and planned study; no empirical findings, funded-project claim, or PI appointment asserted on the page. |
| UEES/FUNPRES graduation research | [Institutional record](http://138.99.0.237/handle/123456789/769) returned HTTP 200. Metadata lists Barrera Gómez and Hernández Escoto as authors, issue date May 2024, and type `Thesis`. Abstract reports operational improvements within the evaluated sample. Repository accession is January 2026, distinct from research date. | Completed 2024 undergraduate graduation monograph, catalogued as thesis. No journal-article claim or general causal-effect claim. |
| M.S. degree, 2024–2025, GPA 3.79/4.00 | Both supplied PDFs and old site agree; no official transcript was supplied. [Webinar organizer archive](https://evoliumsystems.com/es/webinar) also identifies the ETSU master's degree. | Applicant-reported education preserved; no new academic honor or credential added. |
| UEES Computer Systems Engineering, 2019–2024 | Supplied PDFs agree on field and completion, but old resume says B.S.; old site/staged page says B.E.; CV uses the field without a degree abbreviation. GPA scales also differ. | Uses “Computer Systems Engineering” without asserting B.S./B.E. equivalence or a GPA conversion. |
| CenterPoint, AES, Executel, Resultier, ETSU assistantship, The Office Gurus | Supplied resumes and staging establish the roles/responsibilities. Organizer archive identifies CenterPoint role. Internal performance figures and employment terms are not independently verified. | Preserved responsibilities and dates; CenterPoint identified as contract assignment per staging. Executel uses a neutral “Data engineering & operations” heading because exact titles conflict. Resultier internship wording follows the older resume. |
| DD Youth 2024 talk and UEES student outreach | Supplied staged captions and photographs. The owner explicitly supplied 2025 for the UEES student presentation in the editorial redesign task. Photographs support the speaking context but do not independently establish every title/date. | Preserved titles and descriptions. UEES year is owner-supplied, not inferred or independently documented. |
| October 9, 2026 webinar | Staged poster/session screenshots and organizer archive agree on title, date, and presenter. Archive identifies the concluded event. | Past webinar with event archive, poster, and session screenshots; Spanish title marked with `lang="es"`. |
| Technical project descriptions | READMEs from all seven linked public repositories were fetched and checked, including financial extraction limitations, eight CRM dashboards, EEG pooled and subject-wise results, readmission test AUC, ESG prototype, and PDF parser. | Project status/methods retained; no peer-reviewed publication status inferred from code. |
| ORCID and Scholar identity links | URLs match embedded hyperlinks in supplied CV and returned HTTP 200. | Identity links only; no publication count or citation metrics claimed. |

## Items requiring owner attention

1. Verify official undergraduate degree wording against the diploma/transcript
   before using B.E. or B.S. on application materials. Confirm Executel and
   Resultier official job titles; the two supplied resumes differ.
2. The CV was copied unchanged. Its “Principal Investigator” proposal
   title, recognition, internal employer metrics, and exact employment terms
   remain applicant-reported. Confirm the PI wording describes a proposal role
   accurately and that these CV details are appropriate for public distribution.
   The page does not imply a funded study, verified appointment, or completed
   governance findings.
3. Independently confirm DD Youth title/year and the owner-supplied 2025 UEES
   student-talk year if additional dated event documentation becomes available.
   No missing day or month was invented.
4. LinkedIn returned HTTP 999 to the automated checker. The preserved profile URL
   requires a manual browser check; this is not evidence of a broken link.
5. The UEES institutional record works over HTTP. HTTPS at the same IP timed out;
   no working HTTPS replacement was found. The existing official HTTP link is
   retained. Browsers that require HTTPS may need an explicit navigation choice.

No implementation defect currently blocks local review. The limitations above
are evidence and owner-review issues; this report does not certify credentials
from official records that were not supplied.

## Initial integration validation results

- `python scripts/validate_site.py --external`: PASS for 45 references, 15 local
  files, six unique anchors, nine on-page images, PDF signature, `.nojekyll`,
  JSON-LD, robots, and sitemap. Thirteen of fourteen unique external anchor URLs
  returned HTTP 200; LinkedIn returned HTTP 999 (manual review).
- `node --check assets/script.js`: PASS.
- `html-validate@11.16.2 index.html`: PASS, zero errors or warnings using the
  default recommended rules.
- Playwright/Chromium: no horizontal overflow across nine viewport settings
  from 320 to 1920 pixels, including tablet and navigation breakpoint widths.
  Rendered desktop and mobile layouts visually inspected. All nine on-page
  images decoded successfully; all six new WebP files passed image integrity
  checks. No failed local requests or JavaScript page errors.
- Keyboard checks: skip link visibility and main focus, Space menu activation,
  Tab into navigation, Escape close/focus restoration, selection close, outside
  click close, desktop/mobile breakpoint reset, section anchors clear of sticky
  header, and back-to-top navigation: PASS.
- JavaScript-disabled mobile context: content, visible navigation, anchor
  selection, and no horizontal overflow: PASS. Reduced-motion behavior: PASS.
- Axe: zero WCAG 2.1 A/AA violations at 375, 768, and 1440 pixels; full default
  audit also reported zero violations. Gradient-background contrast remained a
  manual-check item; the darkest light hero endpoint and portrait text/background
  combinations were checked separately. Automated accessibility checks do not
  replace assistive-technology testing.
- CV: three pages extracted and rendered; all pages visually inspected
  with no clipping or broken layout. SHA-256
  `e515e31e808d3915c8487b4a3ce380cbb6d6f0d150a0ea3d5d8fbd742e3cda57`.
  Binary equals staged CV; six new images likewise equal staged sources.
- `git diff --check`: PASS. Git may warn about Windows LF/CRLF normalization;
  this does not indicate a whitespace validation failure.

Validation dependencies and screenshots were kept outside the repository. No
pre-existing package manifest or test suite was present. The new standard-library
checker provides repeatable local validation without adding a deployment build.

## Files changed

Modified:

- `index.html`
- `assets/style.css`
- `README.md`

Added:

- `assets/script.js`
- `assets/favicon.svg`
- `assets/docs/Angel_Barrera_Academic_CV.pdf`
- `assets/images/angel-barrera-portrait.webp`
- `assets/images/angel-barrera-original.webp`
- `assets/images/plant-segmentation-still.webp`
- `assets/images/dd-youth-2024.webp`
- `assets/images/uees-student-talk.webp`
- `assets/images/uees-evolium-webinar-poster.webp`
- `assets/images/webinar-presentation.webp`
- `assets/images/webinar-meeting.webp`
- `robots.txt`
- `sitemap.xml`
- `scripts/validate_site.py`
- `docs/PORTFOLIO_REVIEW.md`

Deleted: none. Legacy URLs remain valid, including the old resume and original
project photographs/illustrations. Existing `.nojekyll`, Git history, and
GitHub Pages settings were preserved. No commit, push, merge, or deployment was
performed.
