<div align="center">

# Kids Coding Curriculum

### A playful, print-ready path from Scratch to Python, Git, data, and simple AI.

One calm, creative session a week for children in Grades 2–6
(ages 7–12), taught at home by a parent on a Mac.

<p>
  <a href="https://rrahimi-uci.github.io/kids-coding-curriculum/">Open the website</a>
  &nbsp;·&nbsp;
  <a href="https://rrahimi-uci.github.io/kids-coding-curriculum/resources/setup-mac/">Set up a Mac</a>
  &nbsp;·&nbsp;
  <a href="#quick-start">Quick start</a>
  &nbsp;·&nbsp;
  <a href="parents/">For parents</a>
</p>

<p>
  <a href="https://github.com/rrahimi-uci/kids-coding-curriculum/actions/workflows/ci.yml"><img src="https://github.com/rrahimi-uci/kids-coding-curriculum/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI status"></a>
  <a href="https://github.com/rrahimi-uci/kids-coding-curriculum/actions/workflows/site.yml"><img src="https://github.com/rrahimi-uci/kids-coding-curriculum/actions/workflows/site.yml/badge.svg?branch=main" alt="Website build status"></a>
</p>

</div>

> **The short version:** children make things they can see and play with; parents get a complete lesson, workbook, homework, answer key, and setup path for every week.

## At a glance

| | Course promise |
|---|---|
| **Audience** | Grades 2–3 (ages 7–9) and Grades 4–6 (ages 9–12) · up to four children |
| **Rhythm** | One session per week (45–60 minutes in Grades 2–3, 60 in Grades 4–6), with optional buffer sessions |
| **Shape** | Two grade bands with three levels each, about 10–12 weeks per level, each ending with a final project |
| **Teaching style** | Make games and visual art, then explain, test, and improve the code |
| **Home setup** | Mac, Scratch, Thonny, Python, and pytest; no student accounts required |
| **Print design** | Standard and dyslexia-friendly editions using the Okabe–Ito color-blind-safe palette |

## Choose your path

The course has two grade bands. Each band has its own folder with its
syllabus and three levels.

### [Grades 2–3](grade-2-3/) · Kids Coding Junior (ages 7–9)

Unplugged robot games and picture-first Scratch, read aloud by a grown-up,
ending with a first look at Python. See the [Grades 2–3 syllabus](grade-2-3/SYLLABUS.md).

| Level | You will build | Main ideas | Capstone |
|---|---|---|---|
| [**1 · Little Robots**](grade-2-3/1-little-robots/) | Robot games on the floor and Scratch animations | Exact steps, repeat loops, events, fixing bugs | **My Animated Greeting Card** |
| [**2 · Game Makers**](grade-2-3/2-game-makers/) | Scratch games with a score, surprises and a way to win | Forever loops, if-touching, variables, random, messages | **My First Arcade Game** |
| [**3 · Bridge to Python**](grade-2-3/3-bridge-to-python/) | Pattern art, data and AI unplugged, first Python turtle | Nested repeats, planning, data, blocks to words | **My Big Build** |

### [Grades 4–6](grade-4-6/) · Kids Coding (ages 9–12)

Scratch first, then Python, Git, data and simple AI. See the
[Grades 4–6 syllabus](grade-4-6/SYLLABUS.md). Children who finish Grades 2–3
continue here at Level 1.

| Level | You will build | Main ideas | Capstone |
|---|---|---|---|
| [**1 · Introductory**](grade-4-6/1-introductory/) | Scratch creations, turtle drawings, and interactive art | Events, loops, decisions, variables, and Python basics | **My Interactive Art Show** · reference: *Night Sky Postcard* |
| [**2 · Intermediate**](grade-4-6/2-intermediate/) | Games and small data-powered programs | Functions, lists, dictionaries, files, testing, and game design | **Arcade Game or Art Studio** · reference: *Star Catcher* |
| [**3 · Advanced**](grade-4-6/3-advanced/) | Larger programs that are easier to change | Classes, algorithms, Git, data, and simple AI | **Build Something Big** · reference: *Maze Muncher* |

<div align="center">

**Create → explain → test → improve → share**

</div>

## Quick start

### If you are teaching a family

1. **[Open the course website](https://rrahimi-uci.github.io/kids-coding-curriculum/)** to browse the curriculum and printable student resources.
2. **[Set up each Mac](https://rrahimi-uci.github.io/kids-coding-curriculum/resources/setup-mac/)** with the current Scratch, Thonny, Python, pytest, and Git instructions.
3. Pick the grade band ([Grades 2–3](https://rrahimi-uci.github.io/kids-coding-curriculum/grade-2-3/) or [Grades 4–6](https://rrahimi-uci.github.io/kids-coding-curriculum/grade-4-6/)), read the level’s **Teacher Guide** and print the Student Workbook and Homework for each child.
4. Start with Level 1, Week 1. Each week has a lesson plan, student practice, homework, and a clear definition of “done.”

For an offline student copy, build a solution-free bundle:

```bash
make student-bundle           # every level of both grade bands
make student-bundle LEVEL=1   # Grades 4–6 Level 1 only
make student-bundle LEVEL=j1  # Grades 2–3 Level 1 only
```

The output is `build/student-bundle/kids-coding/` (with the same `grade-2-3/` and
`grade-4-6/` folders as the repository) and a matching ZIP file. Copy
the folder or unzip it into the child’s Documents folder. It contains the
exercise instructions, hints, starter files, tests, and self-check helpers —
but not solutions, answer keys, or teacher material.

### If you are exploring the repository

```bash
make setup  # create the development environment
make test   # run the headless exercise and repository checks
```

That is enough to confirm the repository is healthy. Maintainers can find the
full build and publishing workflow below.

## What each week includes

Every level is designed as a complete teaching kit rather than a collection of
loose worksheets:

| For the parent | For the child |
|---|---|
| Teacher Guide with setup, pacing, assessment, and troubleshooting | Student Workbook chapter with explanations, diagrams, vocabulary, and reflection |
| Minute-by-minute Lesson Plan with analogies, worked examples, mistakes, and stretch ideas | In-class exercises with hints and a clear “done” checklist |
| Answer Key for workbook, homework, and assessments | Homework in Core, Challenge, and Creative paths, designed for about 15–20 minutes |
| Progress tracker, glossary, cheat sheet, and certificate | Starter files and self-checks that encourage debugging without revealing the solution |

Students check Python work by opening `check_my_work.py` in the exercise folder
and pressing **Run** in Thonny. Scratch and Terminal exercises use their own
expected-behavior and checklist sections.

## Repository map

```text
grade-2-3/             Grades 2–3 (Kids Coding Junior): SYLLABUS.md and three levels
  1-little-robots/       Level 1: robot games and Scratch
  2-game-makers/         Level 2: Scratch games
  3-bridge-to-python/    Level 3: Scratch, then a first look at Python turtle
grade-4-6/             Grades 4–6: SYLLABUS.md and three levels
  1-introductory/        Level 1: Scratch, then Python turtle
  2-intermediate/        Level 2: functions, data, files, testing, and games
  3-advanced/            Level 3: OOP, algorithms, Git, data, and simple AI
curriculum.json        which bands and levels exist, their folders and week counts
docs/                  syllabus, design decisions, standards, and authoring guide
parents/               parent information evening deck, notes, and handout
shared/                LaTeX class, color palette, and document helpers
testing/               fake turtle, test runners, and repository quality checks
tools/                 PDF, coverage, student-bundle, and website build tools
site/                  Astro website, public/private manifest, and browser QA
.github/               CI workflows and the pull-request template
```

An exercise folder normally looks like this:

```text
<band>/<level>/exercises/weekNN/<exercise>/
├── README.md           the kid-friendly task and success checklist
├── starter.py          the file the child changes
├── hints.md            three progressive hints
├── test_*.py           automated checks
└── check_my_work.py    the child-facing self-check
```

Scratch and Terminal exercises use a smaller set of README, hint, and solution
files. Teacher-only material and reference solutions stay in the repository
but are excluded from the public website.

## The website

The [public course website](https://rrahimi-uci.github.io/kids-coding-curriculum/)
is generated from the same source files as the printable curriculum. It follows
the same structure: a page per grade band (`/grade-2-3/`, `/grade-4-6/`) and
every level beneath it (`/grade-4-6/level-1/week-07/`). Addresses from before
version 2.0.0 (`/levels/level-N/...`) redirect to the Grades 4–6 pages. The build
converts workbooks, exercise folders, figures, and selected parent materials;
it does not copy pages by hand. A private-content check prevents answer keys,
solutions, lesson plans, teacher guides, and tests from being published.

Every week page also shows that week's animated teaching video (*Kids Coding
with Rose and Pixi* in Grades 4–6, *Kids Coding Junior with Aiden and Pixi* in
Grades 2–3) in the same place, right below the page header, with captions
and a transcript. The videos are kept on the repository's `videos` release, not
in Git; the build copies them in. See [videos/README.md](videos/README.md#on-the-website)
for how to replace one.

### Build and preview locally

```bash
make site-setup  # one time: Python site environment + npm dependencies
make site        # generate site data, build Astro, and run content checks
make site-serve  # preview site/dist at http://localhost:4321/
make site-check  # HTML, links, accessibility, and Lighthouse checks
```

The site toolchain needs Python 3.12, Node 20+, Pandoc 3.8+, Poppler, and
Google Chrome for browser checks. The full `make site` build also needs the
LuaLaTeX setup listed under [Maintainer commands](#maintainer-commands). On
macOS, the usual additional setup is:

```bash
brew install pandoc poppler
```

### Publish a change

1. Edit the canonical source: a lesson, exercise folder, parent asset, or site content.
2. If you add a diagram, put `%% alt: a short description of the picture` immediately above its `\begin{tikzpicture}`.
3. Run the relevant local checks and inspect the result with `make site-serve`.
4. Commit the source changes on a branch and open a pull request. Do not edit `main` directly.
5. After merge, the **Website** workflow rebuilds and deploys GitHub Pages. Generated site output is intentionally ignored by Git.
6. For a public release, bump `VERSION` and add a dated entry to `CHANGELOG.md`.

## Maintainer commands

Requirements: macOS, [MacTeX/TeX Live](https://tug.org/mactex/) with LuaLaTeX,
and Python 3.10+ (or [uv](https://docs.astral.sh/uv/)).

```bash
make setup          # .venv with Python 3.10 and pytest
make test           # all exercise tests + repository quality gate
make smoke          # open every turtle program in a real Mac window
make pdf            # all PDFs, standard + dyslexia-friendly
make pdf LEVEL=2    # build one level (Grades 4–6 Level 2; j1–j3 are Grades 2–3)
make check          # test + PDF build
make student-bundle # solution-free copy for a child's Mac
```

Useful focused commands:

```bash
python3 tools/coverage.py --check  # verify coverage tables are current
make pdf-standard                  # standard edition only
make pdf-dyslexia                  # dyslexia-friendly edition only
make -C parents                    # parent deck, notes, and handout
```

`make help` prints the complete command list. `LEVEL=1|2|3` (Grades 4–6) or `LEVEL=j1|j2|j3` (Grades 2–3) narrows PDF and
student-bundle commands; omit it to include all levels. Level keys, folders
and week counts come from [`curriculum.json`](curriculum.json); a level marked
`planned` there is skipped by every command until its content exists.

## Documentation guide

* [Grades 2–3 syllabus](grade-2-3/SYLLABUS.md) — the junior track: levels, weeks, goals, and junior rules
* [Grades 4–6 syllabus](grade-4-6/SYLLABUS.md) — scope, sequence, goals, and spiral map
* [Design decisions](docs/DESIGN.md) — the language path and teaching choices
* [Standards alignment](docs/STANDARDS.md) — CSTA and AI4K12 connections
* [Authoring guide](docs/AUTHORING.md) — how to write lessons, exercises, and tests
* [Assumptions](docs/ASSUMPTIONS.md) — the assumptions behind the curriculum
* [Website design](docs/SITE-DESIGN.md) — generation pipeline, privacy rules, and QA
* [Teaching videos](videos/README.md) — scripts, animation, rendering, and publishing to the website
* [Asset licenses](docs/ASSETS.md) — fonts, icons, and figure licenses
* [Parent information deck](parents/README.md) — build and presentation instructions

## Privacy and safety

The curriculum is designed for local, parent-supervised use. Students do not
need accounts, and lessons can run from the local apps and student bundle after
setup. The Mac installer downloads the tools it needs; it does not upload
projects or personal information. The website publishes student-facing content
only, and its private-content check runs before deployment.

## Contributing

All changes go through a pull request. Keep source files and generated outputs
separate, run the checks appropriate to the change, and use the repository’s
[pull-request template](.github/pull_request_template.md) to document the goal,
approach, validation, risks, and deployment implications.

---

<div align="center">

Made for curious kids, patient grown-ups, and the joy of making something work.

</div>
