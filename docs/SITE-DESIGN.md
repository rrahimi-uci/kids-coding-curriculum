# Website design

The course website is **generated** from the course sources. Nothing is retyped: the LaTeX and Python
files remain the single source of truth, and rebuilding the site updates the web version. This document
explains the choices and how the pieces fit together. How to run and update the site is in
[the README](../README.md#website).

## Goals

* Make the course easy for children and parents to use on any device.
* Prefer real HTML (searchable, accessible, printable) over PDF links, and offer the PDF alongside.
* Never publish teacher-only material, and prove it automatically on every build.
* Keep JavaScript minimal; no accounts, no analytics, no third-party requests.

## Pipeline

```
course sources (.tex, .py, .md)            site/manifest.yml (public / private, deny by default)
        │                                              │
        ▼                                              ▼
tools/site/build.py ── texconv.py ──► HTML fragments + JSON  ──► Astro (site/) ──► site/dist ──► Pagefind index
        │               figures.py ──► SVG figures
        │               exercises.py ► exercise pages (README + starter + hints)
        │               parents.py ──► research, slides, FAQ (from the parent deck, faq.tex + .bib)
        ├── pdfs.py ───► whole-level and per-week PDFs
        └── videos.py ─► teaching videos from the `videos` release (videos.json, junior-videos.json) ──► site/public/videos/
                                                           checks: private content, content, HTML, links, a11y, Lighthouse
```

`make site` runs the whole thing; `make site-check` runs the browser-based gates. CI does the same
([.github/workflows/site.yml](../.github/workflows/site.yml)) and deploys on every push to `main`.

## Conversion approach per content type

| Content | Approach | Why |
|---|---|---|
| Workbook chapters, homework sets (LaTeX) | Custom preprocessing, then **Pandoc** (LaTeX → HTML5), then HTML post-processing (BeautifulSoup) | Prose, lists, tables and the course's colored boxes convert cleanly. The course's own macros and environments (callouts, `\menu`, `\keys`, vocabulary, self-check lists, fill-in lines) are mapped explicitly, so nothing is silently dropped. LaTeXML and tex4ht were rejected: they struggle with LuaLaTeX, fontspec, tcolorbox, TikZ and the scratch3 package that the course relies on. |
| TikZ diagrams and Scratch scripts | Each figure is compiled with **LuaLaTeX using the course class**, converted to **SVG** with `pdftocairo`, cached by hash | Pixel-faithful to the PDF, scales on phones, sharp in print. Alt text: Scratch scripts get a generated description (block by block, with nesting); every TikZ diagram needs a `%% alt: …` comment in the source (checked). |
| Code listings | `pycode` / `outputcode` blocks → `<pre>`; Python highlighted at build time with **Pygments** (static CSS classes) | No JavaScript needed for highlighting; the copy button is a tiny progressive enhancement. |
| Exercises | **Rendered directly from the source folders**: `README.md`, `starter.py`, `hints.md` | The folders already are the master. Hints are a new public file per exercise (three progressive hints). |
| Parent deck (Beamer) | Embedded PDF viewer + PDF download; **slide images** (WebP, with alt text from the slide text); a research page and FAQ **generated from `main.tex`, `content/faq.tex` and `references.bib`** | Beamer slides are TikZ-heavy and not worth converting frame by frame. The speaker-note paragraphs ("In plain language", questions and answers) and sources are structured in the source, so they become real HTML with linked citations. Questions asked outside the information evening live in `parents/content/faq.tex`, so the slides stay short. |
| Project briefs, cheat sheets, parent notes | The same LaTeX converter, standalone documents: the file's own zero-argument macros are expanded, cheat-sheet code boxes and command tables are mapped (`tools/site/texconv.py`) | They are ordinary student-facing documents; faithful HTML plus the PDF alongside. |
| Glossaries | Parsed structurally (`\gl`, `\term`) into one searchable A to Z page | The three sources use two macro styles; one page is easier to use than three PDFs. |
| Progress trackers | PDF only | They are print-and-tick sheets; HTML adds nothing. |
| Setup and troubleshooting | New short markdown guides in `resources/`; the Mac guide starts with a one-line command and shows the full `resources/install-mac.sh` (published at `downloads/install-mac.sh`, tested by `testing/test_install_script.py`) | The only existing source is the private teacher guide, so the facts were rewritten for children and parents (no self-check script, no answer material). |
| Syllabus tables | Parsed from each band's `SYLLABUS.md` (`grade-2-3/`, `grade-4-6/`) | Level pages, week titles, big ideas and goals stay in sync with the syllabus. |
| Whole-level documents | The PDFs built by `tools/build.py`, standard and dyslexia-friendly editions | Offered as downloads; one PDF per week (chapter + homework) is compiled from a tiny wrapper that inputs the same source files. |

Fallback rule: if something cannot be converted faithfully, the build reports it (a `PROBLEM:` line) and
fails rather than publishing something wrong.

## Static site generator: Astro

* **Content-heavy and static**: pages are generated from JSON and HTML fragments at build time.
* **Zero JavaScript by default.** The only scripts are a small progressive-enhancement file (dark-mode
  toggle, the phone menu, copy buttons) and, on the search page only, Pagefind. The pages are made for
  **reading**: no checkboxes, progress bars, "mark as done" buttons or hints that lock and unlock; the
  self-check lists are ordinary lists and the hints are plain sections in order.
* Dynamic routes (`[band]/[level]/[week]`, `exercises/[slug]`) make the level and week pages come out of the
  data automatically; `base` support makes it work as a GitHub project page.
* **Pagefind** gives offline-capable, no-server site search.
* Jekyll was rejected (Ruby toolchain, weaker component model); Hugo is fast but not installed and templating
  is harder for the component-style design; MkDocs Material is excellent for docs but a playful, card-based
  design would fight the theme.

## Two grade bands

The course has a Grades 2–3 track (`grade-2-3/`: `1-little-robots` to `3-bridge-to-python`) and a Grades 4–6
track (`grade-4-6/`: `1-introductory` to `3-advanced`). `curriculum.json` says which levels exist, their
track and how many weeks each has (10 in Grades 2–3, 12 in Grades 4–6); the manifest lists the published
levels by key (`j1` … `j3`, `1` … `3`) and folder, and the build checks that the two agree. Pages and file
names are named by band, because both bands have a Level 1, 2 and 3 (`grade-2-3/level-1/`,
`grade-4-6-level-1-student-workbook.pdf`). The build is band-aware rather than copied: one level builder, one
set of page templates. What differs:

* **Names and labels.** Each level in `levels.json` carries `track`, `key` (`1`, `j1` …), `band`, `path`
  (`grade-4-6/level-1`) and `id` (`grade-4-6-level-1`); `bands.json` holds each band's title, grades and ages
  for the home, curriculum, band and parent pages. Pages name a level with its band: "Grades 4–6, Level 1".
* **Converter.** The junior LaTeX environments become callouts like the others, each with an icon and a text
  label: `ican` ("I can …", the week's goals, taken out as the objectives like the Grades 4–6 list),
  `grownup` ("For the grown-up") and `playathome` ("Play at home (5–10 minutes, with a grown-up)", the junior
  homework, which has no Core / Challenge / Creative tiers). Figures and week PDFs are compiled with the
  level's class options (`track=junior,level=1`). `showme` (the show-me checklist) is an assessment: it only
  appears in private files, and the converter refuses any file that contains one.
* **Pages.** Grades 2–3 week pages call the homework "Play at home"; Levels 1 and 2 have projects without
  starter files (they start in Scratch), Level 3 offers the Python postcard starter; the Grades 2–3 glossaries
  ("Word Book") are separate sections of the glossary page, linked from each level page.
* **Videos.** Grades 2–3 videos (*Kids Coding Junior with Aiden and Pixi*) are on the same `videos` release but
  listed in their own `junior-videos.json` (same shape as `videos.json`, keys like `j1-2`). Each list is
  read on its own: if one is missing or unreachable, only its videos are left out and the pages are built
  without the player.

## Public vs private (strict)

[`site/manifest.yml`](../site/manifest.yml) is the single place that tags content. **Deny by default:** the
converter opens only files that match the `public` globs (workbook chapters, homework sets, exercise
`README.md` / `starter.py` / `hints.md` and starter data, and an allow-list of PDF stems). Everything else
(answers, lesson plans, teacher guides, reference solutions, tests, the `check_my_work.py` self-check,
assessments) is never read.

[`tools/site/check_private.py`](../tools/site/check_private.py) then scans the finished site and fails the
build when:

1. a published file name or ZIP member contains a private path fragment (`answers/`, `solution`, `test_`, …);
2. a private marker string (`TEACHER ONLY`, `Teacher script`, `Answer key`, …) appears in any text, ZIP member
   or PDF text;
3. a distinctive line of a private source (solution code, answer keys, teacher lessons, assessments,
   certificates) appears anywhere in the output. The check runs over every level in the manifest, so the
   junior folders (Scratch `solution.md` files, the grown-up's answers, show-me checklists) are covered. Lines that also occur in public sources (starter code, workbooks, READMEs, both syllabi) are
   ignored, so shared text is not a false alarm.

`testing/test_site_private.py` proves the check works by injecting leaks into a fake site. Light edits made
for the web (reported, never changing meaning): the self-check script is not published, so sentences and
checklist items that tell the child to run `check_my_work.py` are dropped from the web pages (the PDFs are
unchanged), and the syllabus paragraph that describes the reference solution is removed.

No children's names, photos or personal data are used; the site has no analytics, cookies or accounts.
(The exercises use a few invented first names for characters, such as the child who wrote a buggy script.)

## Site map

* **Home**: value of the course, a choice of grade band, and the three levels of each band at a glance, paths
  for parents and students.
* **For parents** (`/parents/`): weekly commitment, how to help, assessment, safety; **Research**
  (generated from the deck: slide, plain-language explanation, questions, sources, linked references);
  **Slides** (viewer, download, gallery); **FAQ**.
* **Curriculum** (`/curriculum/`): both grade bands in order, each with its timeline (Grades 2–3: weeks 1–10
  with the show-me day, project studio and showcase; Grades 4–6: weeks 1–12 with the checkpoint, project and
  showcase), what is learned, final projects, how progress is measured.
* **Grade bands** (`/grade-2-3/`, `/grade-4-6/`): one page per track with the same timeline and level cards,
  and how the two tracks connect. Every level lives under its band, because both bands have a Level 1, 2 and 3:
  `/grade-2-3/level-1/`, `/grade-4-6/level-1/week-07/`, `/grade-4-6/level-1/exercises/<slug>/`. Download file
  names carry the band too (`grade-4-6-level-1-student-workbook.pdf`).
* **Level pages** and **week pages**: objectives, the week's teaching video (always the first thing in the
  lesson, right below the header, with captions and a transcript), lesson content, exercises, new words, homework tiers
  (Core, Challenge, Creative), downloads (week PDF, starter-file ZIP), previous/next and a self-check list
  (an ordinary list to read, not checkboxes).
* **Exercises**: steps, starter code with copy and download, three hints, in order, from a small nudge to a bigger one. No solutions.
* **Projects** (`/<band>/level-N/project/`): the final-project brief with plan sheet and rubric, and the
  starter files (templates, never the reference solution) to read, copy and download. Levels whose project
  is built in Scratch (Grades 2–3 Levels 1 and 2) have no starter files, so the page shows only the brief.
* **Resources** (`/resources/`): Mac setup guide and troubleshooting (written for the web from the teacher
  setup notes, in `resources/*.md`), cheat sheets per level, a combined A to Z glossary, printable progress
  trackers (PDF) and notes for families per level (`/parents/notes/<band>/level-N/`).
* **Moved pages**: before version 2.0.0 the Grades 4–6 levels were at `/levels/level-N/...` and the Grades 2–3
  levels at `/levels/junior-N/...`; their notes for families were at `/parents/notes/level-N/` and
  `/parents/notes/junior-N/`. Each old address is still generated as a small page that sends the
  browser to the new one (`<meta http-equiv="refresh">`, `noindex`, left out of search), so old links and
  printed QR codes keep working. Old PDF and ZIP download addresses are not redirected.
* **Search** (Pagefind) and **About** (privacy, accessibility, credits, change log).

### Navigation

One menu, in a **left sidebar** on screens 1024px and wider and in a **drawer** opened from a slim top bar on
phones and tablets (without JavaScript the menu is simply shown above the page). It is ordered the way a
family meets the course:

1. **Home** and **Curriculum and timeline** (orientation);
2. **Grades 2–3** and **Grades 4–6**: each band has an *Overview* link and its three levels; each level is a
   disclosure that opens to *Overview*, *Weeks*, *Final project*, *Cheat sheet* and *Notes for families*; the current level is open, the current page is highlighted
   (`aria-current="page"`) and an exercise page highlights its week (`aria-current="location"`);
3. **For parents**: parent guide, research, slides, questions and answers;
4. **Resources**: setup guide, troubleshooting, glossary, all resources, about.

A search box sits above the menu (it submits to `/search/?q=...`). The dark-mode toggle is a single icon
button fixed in the top-right corner, outside the navigation; only the menu below search scrolls. Long pages keep their
**On this page** list: in its own column on the right on wide screens, folded above the text otherwise.
Icons follow the Lucide set (24px grid, 2px stroke) at text size, and every icon is paired with a text label.
* Assessments (placement, checkpoint and exit quizzes) and certificates are not published.

## Visual design

Warm white paper background, generous white space and card-based components; text and headings in
Atkinson Hyperlegible Next (headings bold, body 17px with a 1.7 line height and a 70-character line length,
sentence-case labels rather than capitals); one accent color per level number (blue, green, vermillion, the same in both bands, as in the PDFs) taken from the course's
color-blind-safe Okabe–Ito palette, with darker text shades so every text color passes 4.5:1. The Scratch
and Python material keeps its callout boxes (Tip, Safety, Core, Challenge, Creative, Exercise, Bug hunt,
Self-check, New words, and for Grades 2–3 I can, For the grown-up and Play at home), each with a text label and an icon, so meaning never depends on color. Dark mode
follows the system setting and can be toggled from the top-right corner.
Pages are responsive from phone to desktop and print cleanly. Fonts are subset to WOFF2 (about 10 KB each)
and self-hosted.

## Accessibility (WCAG 2.2 AA)

Skip link, semantic landmarks and heading order, visible focus, keyboard-operable everything (menu,
theme control, copy buttons), accessible names for scrollable tables, alt text for every figure and slide image, video captions on by default
and a transcript for every video, no flashing or autoplay, text resize to 200% without loss, reduced-motion support. Verified by `site/qa/a11y.mjs` (axe-core
with the WCAG 2.0 to 2.2 A and AA rule sets) in light and dark mode and a phone-width overflow check.

## Quality gates (CI)

| Gate | Tool |
|---|---|
| Private content | `tools/site/check_private.py` |
| Every lesson has objectives, every image has alt text, every exercise has hints | `tools/site/check_content.py` |
| HTML validity | html-validate |
| Broken links | linkinator (internal always; external with `LINKS_EXTERNAL=1`) |
| Accessibility | axe-core via Playwright |
| Performance, accessibility, best practices ≥ 90 | Lighthouse |

## Versioning

`VERSION` holds the site version and `CHANGELOG.md` the history; the footer shows the version and the date
of the last commit.
