# Kids Coding Curriculum

A complete, print-ready programming curriculum for **up to four children
starting in Grade 5**, taught at home by a parent in **one 60-minute session a
week** on Macs. It leans into what the kids enjoy: **making games and visual
art**.

| Level | Weeks | Language | Final project (reference solution) |
|---|---|---|---|
| [1 Introduction](1-introduction/) | 12 + 2 buffer | Scratch, then Python turtle in Thonny | *My Interactive Art Show* (*Night Sky Postcard*) |
| [2 Intermediate](2-intermediate/) | 12 + 2 buffer | Python: functions, lists, dicts, files, testing, games | *Arcade Game or Art Studio* (*Star Catcher*) |
| [3 Advanced](3-advanced/) | 12 + 2 buffer | Python projects: OOP, algorithms, git, data, simple AI | *Build Something Big* (*Maze Muncher*) |

No accounts, no internet needed during lessons, and no personal data.

## Repository layout

```
1-introduction/        Level 1: Scratch, then Python turtle
2-intermediate/        Level 2: Python functions, data, files, testing, games
3-advanced/            Level 3: OOP, algorithms, git, data, simple AI
docs/                  syllabus, design decisions, standards, authoring guide, assumptions
shared/latex/          kidscode.cls (the one document class: fonts, palette, boxes)
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
  lesson-plans           one plan per week + 2 buffer sessions (minute-by-minute,
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

All changes go through pull requests; see
[.github/pull_request_template.md](.github/pull_request_template.md).
