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
        └── pdfs.py ───► whole-level and per-week PDFs
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
| Syllabus tables | Parsed from `docs/SYLLABUS.md` | Level pages, week titles, big ideas and goals stay in sync with the master syllabus. |
| Whole-level documents | The PDFs built by `tools/build.py`, standard and dyslexia-friendly editions | Offered as downloads; one PDF per week (chapter + homework) is compiled from a tiny wrapper that inputs the same source files. |

Fallback rule: if something cannot be converted faithfully, the build reports it (a `PROBLEM:` line) and
fails rather than publishing something wrong.

## Static site generator: Astro

* **Content-heavy and static**: pages are generated from JSON and HTML fragments at build time.
* **Zero JavaScript by default.** The only scripts are a small progressive-enhancement file (display
  toggles, the phone menu, copy buttons) and, on the search page only, Pagefind. The pages are made for
  **reading**: no checkboxes, progress bars, "mark as done" buttons or hints that lock and unlock; the
  self-check lists are ordinary lists and the hints are plain sections in order.
* Dynamic routes (`levels/[level]/[week]`, `exercises/[slug]`) make the level and week pages come out of the
  data automatically; `base` support makes it work as a GitHub project page.
* **Pagefind** gives offline-capable, no-server site search.
* Jekyll was rejected (Ruby toolchain, weaker component model); Hugo is fast but not installed and templating
  is harder for the component-style design; MkDocs Material is excellent for docs but a playful, card-based
  design would fight the theme.

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
3. a distinctive line of a private source (solution code, answer keys, teacher lessons, assessments) appears
   anywhere in the output. Lines that also occur in public sources (starter code, workbooks, READMEs) are
   ignored, so shared text is not a false alarm.

`testing/test_site_private.py` proves the check works by injecting leaks into a fake site. Light edits made
for the web (reported, never changing meaning): the self-check script is not published, so sentences and
checklist items that tell the child to run `check_my_work.py` are dropped from the web pages (the PDFs are
unchanged), and the syllabus paragraph that describes the reference solution is removed.

No children's names, photos or personal data are used; the site has no analytics, cookies or accounts.
(The exercises use a few invented first names for characters, such as the child who wrote a buggy script.)

## Site map

* **Home**: value of the course, three levels at a glance, paths for parents and students.
* **For parents** (`/parents/`): weekly commitment, how to help, assessment, safety; **Research**
  (generated from the deck: slide, plain-language explanation, questions, sources, linked references);
  **Slides** (viewer, download, gallery); **FAQ**.
* **Curriculum** (`/curriculum/`): three-level timeline (weeks 1–12 with the checkpoint, project and
  showcase), what is learned, final projects, how progress is measured.
* **Level pages** and **week pages**: objectives, lesson content, exercises, new words, homework tiers
  (Core, Challenge, Creative), downloads (week PDF, starter-file ZIP), previous/next and a self-check list
  (an ordinary list to read, not checkboxes).
* **Exercises**: steps, starter code with copy and download, three hints, in order, from a small nudge to a bigger one. No solutions.
* **Projects** (`/levels/level-N/project/`): the final-project brief with plan sheet and rubric, and the
  starter files (templates, never the reference solution) to read, copy and download.
* **Resources** (`/resources/`): Mac setup guide and troubleshooting (written for the web from the teacher
  setup notes, in `resources/*.md`), cheat sheets per level, a combined A to Z glossary, printable progress
  trackers (PDF) and notes for families per level (`/parents/notes/level-N/`).
* **Search** (Pagefind) and **About** (privacy, accessibility, credits, change log).

### Navigation

One menu, in a **left sidebar** on screens 1024px and wider and in a **drawer** opened from a slim top bar on
phones and tablets (without JavaScript the menu is simply shown above the page). It is ordered the way a
family meets the course:

1. **Home** and **Curriculum and timeline** (orientation);
2. **Levels**: each level is a disclosure that opens to *Overview*, *Weeks 1 to 12*, *Final project*, *Cheat
   sheet* and *Notes for families*; the current level is open, the current page is highlighted
   (`aria-current="page"`) and an exercise page highlights its week (`aria-current="location"`);
3. **For parents**: parent guide, research, slides, questions and answers;
4. **Resources**: setup guide, troubleshooting, glossary, all resources, about.

A search box sits above the menu (it submits to `/search/?q=...`), and **Display** (Dark mode, Easy-read font,
both switches with `aria-pressed`) sits below it; only the menu between them scrolls. Long pages keep their
**On this page** list: in its own column on the right on wide screens, folded above the text otherwise.
Icons follow the Lucide set (24px grid, 2px stroke) at text size, and every icon is paired with a text label.
* Assessments (placement, checkpoint and exit quizzes) and certificates are not published.

## Visual design

Warm white paper background, generous white space and card-based components; text and headings in
Atkinson Hyperlegible Next (headings bold, body 17px with a 1.7 line height and a 70-character line length,
sentence-case labels rather than capitals); one accent color per level (blue, green, vermillion) taken from the course's
color-blind-safe Okabe–Ito palette, with darker text shades so every text color passes 4.5:1. The Scratch
and Python material keeps its callout boxes (Tip, Safety, Core, Challenge, Creative, Exercise, Bug hunt,
Self-check, New words), each with a text label and an icon, so meaning never depends on color. Dark mode
follows the system setting and can be toggled; an **Easy-read font** switch loads Lexend with wider spacing.
Pages are responsive from phone to desktop and print cleanly. Fonts are subset to WOFF2 (about 10 KB each)
and self-hosted.

## Accessibility (WCAG 2.2 AA)

Skip link, semantic landmarks and heading order, visible focus, keyboard-operable everything (menu,
toggles, copy buttons), accessible names for scrollable tables, alt text for every figure and slide image, no flashing or
autoplay, text resize to 200% without loss, reduced-motion support. Verified by `site/qa/a11y.mjs` (axe-core
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
