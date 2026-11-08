# Kids Coding Curriculum

A complete, print-ready programming curriculum for **up to four children
starting in Grade 5**, taught at home by a parent in **one 60-minute session a
week** on Macs. It leans into what the kids enjoy: **making games and visual
art**.

| Level | Length | Language | Final project (reference solution) |
|---|---|---|---|
| [1 Introduction](1-introduction/) | 10–12 weeks | Scratch, then Python turtle in Thonny | *My Interactive Art Show* (*Night Sky Postcard*) |
| [2 Intermediate](2-intermediate/) | 10–12 weeks | Python: functions, lists, dicts, files, testing, games | *Arcade Game or Art Studio* (*Star Catcher*) |
| [3 Advanced](3-advanced/) | 10–12 weeks | Python projects: OOP, algorithms, git, data, simple AI | *Build Something Big* (*Maze Muncher*) |

No accounts, no internet needed during lessons, and no personal data.

## Repository layout

```
1-introduction/        Level 1: Scratch, then Python turtle
2-intermediate/        Level 2: Python functions, data, files, testing, games
3-advanced/            Level 3: OOP, algorithms, git, data, simple AI
docs/                  syllabus, design decisions, standards, authoring guide, assumptions
site/                  Astro project (theme, pages) + manifest.yml (public/private rules) + qa/ checks
parents/               parent information evening: research-based slide deck,
                       speaker notes and one-page handout (see parents/README.md)
shared/latex/          kidscode.cls (the one document class: fonts, boxes),
                       kidscode-colors.sty (the shared Okabe-Ito palette)
                       and kidscode-breaks.lua (lets long code names wrap)
shared/templates/      blank lesson / workbook / homework / answer files to copy
testing/               fake turtle + test runners, repository quality checks
tools/                 build.py (PDFs) and coverage.py (objective coverage tables)
.github/               CI workflow and pull request template
```

## What is in each level

```
<level>/teaching-material/
  teacher-guide          goals, roadmap, setup, session template, assessment plan,
                         troubleshooting, pacing + holiday plan, coverage tables
  lesson-plans           one plan per week + 2 optional buffer sessions (minute-by-minute,
                         teacher script, analogies, worked example, mistakes,
                         differentiation, stretch challenge)        [teacher]
  student-workbook       one chapter per week: explanations, diagrams,
                         in-class exercises, vocabulary box, reflection
  homework               one 15–20 min set per week: Core / Challenge / Creative
                         + self-check list
  answer-key             workbook, homework and assessment answers [teacher]
  assessments            placement quiz (Levels 2–3), mid-level checkpoint,
                         exit assessment, each with a rubric
  extras/                cheat sheet, glossary, progress tracker, parent notes,
                         certificate
<level>/exercises/weekNN/<exercise>/
  README.md  starter.py  solution.py  test_*.py  check_my_work.py
<level>/project/
  project-brief          student brief, milestones, rubric
  project-teacher-guide  teacher walkthrough, reference solution, showcase plan
  reference/             complete tested reference solution
  starter/               starter templates
```

Every document is built in two editions: **standard** (Atkinson Hyperlegible)
and **dyslexia-friendly** (Lexend, larger and wider spacing, cream page).
All colors come from the color-blind-safe Okabe–Ito palette.

## Quick start for the parent

1. **Get the PDFs.** Download the `curriculum-pdfs` artifact from the latest
   CI run, or build them yourself (below). For Level 1, print: the Student
   Workbook and Homework (one per child), and keep the Teacher Guide, Lesson
   Plans and Answer Key for yourself.
2. **Read the Teacher Guide** (setup checklist, how a session runs).
3. **Set up each Mac** (Teacher Guide → Setup): Scratch app, Thonny, and a
   copy of this folder.
4. Each week: read that week's lesson plan (≈10 minutes), print the workbook
   chapter and homework, and teach.

Students check their own Python work by opening `check_my_work.py` in an
exercise folder and pressing **Run** in Thonny.

**Recruiting families?** [parents/](parents/) has a 25-minute information
evening deck on why coding matters and what the research shows, with speaker
notes and a one-page handout (`make -C parents`).

## Website

The course also runs as a website (GitHub Pages) that is **generated from these same files**: the LaTeX
workbooks and homework, the exercise folders and the parent deck. Nothing is copied by hand, so the web
pages and the PDFs always match. Answer keys, lesson plans, teacher guides, solutions and tests are never
read or published; the build checks the finished site and fails if any of them would be.
Design and decisions: [docs/SITE-DESIGN.md](docs/SITE-DESIGN.md).

```bash
make site-setup     # once: .venv-site (Python 3.12) + site/ npm packages
make site           # convert sources -> site/dist, run the private-content and content checks
make site-serve     # preview at http://localhost:4321/
make site-check     # HTML validation, broken links, accessibility (axe), Lighthouse >= 90
```

Needs the TeX Live setup above plus [Pandoc](https://pandoc.org) 3.8 or newer (`brew install pandoc`),
poppler (`brew install poppler`), Node 20+ and Google Chrome for the browser checks.

**How to update a lesson and republish**

1. Edit the source, for example `1-introduction/teaching-material/workbook/week07.tex`, or an exercise folder
   such as `1-introduction/exercises/week07/ex-first-square/` (`README.md`, `starter.py`, `hints.md`).
2. New diagram? Put a line `%% alt: a short description of the picture` right above its
   `\begin{tikzpicture}`. Scratch scripts are described automatically.
3. `make site` and look at the result with `make site-serve`.
4. Commit and open a pull request. CI runs every gate; after you merge into `main`, the workflow
   *Website* deploys to GitHub Pages (one-time setup: Settings, Pages, Source: *GitHub Actions*).
5. For a release, bump `VERSION` and add an entry to `CHANGELOG.md`. The footer shows both.

## For maintainers

Requirements: macOS, [MacTeX/TeX Live](https://tug.org/mactex/) with
LuaLaTeX, Python 3.10+ (or [uv](https://docs.astral.sh/uv/)).

```bash
make setup          # .venv with Python 3.10 (like Thonny) + pytest
make test           # every exercise test + repository quality gate (headless)
make smoke          # open every turtle program in a real window (Mac)
make pdf            # all PDFs, both editions -> build/pdf/
make pdf LEVEL=2    # one level
python3 tools/coverage.py   # regenerate objective coverage tables
```

Documentation:

* [docs/SYLLABUS.md](docs/SYLLABUS.md) — scope and sequence, goals, spiral map
* [docs/DESIGN.md](docs/DESIGN.md) — design decisions and language path
* [docs/STANDARDS.md](docs/STANDARDS.md) — CSTA / AI4K12 alignment
* [docs/AUTHORING.md](docs/AUTHORING.md) — how to write lessons, exercises, tests
* [docs/ASSUMPTIONS.md](docs/ASSUMPTIONS.md) — every assumption made
* [docs/SITE-DESIGN.md](docs/SITE-DESIGN.md) — the website: pipeline, public/private rules, design, checks
* [docs/ASSETS.md](docs/ASSETS.md) — licenses of fonts, icons and figures

All changes go through pull requests; see
[.github/pull_request_template.md](.github/pull_request_template.md).
