<div align="center">

# Kids Coding Curriculum

### A playful, print-ready path from Scratch to Python, Git, data, and simple AI.

One calm, creative 60-minute session a week for children in Grades 4–5
(ages 9–11), taught at home by a parent on a Mac.

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
| **Audience** | Grades 4–5 · ages 9–11 · up to four children |
| **Rhythm** | One 60-minute session per week, with optional buffer sessions |
| **Shape** | Three levels, each about 10–12 weeks, plus a final project |
| **Teaching style** | Make games and visual art, then explain, test, and improve the code |
| **Home setup** | Mac, Scratch, Thonny, Python, and pytest; no student accounts required |
| **Print design** | Standard and dyslexia-friendly editions using the Okabe–Ito color-blind-safe palette |

## Choose your path

| Level | You will build | Main ideas | Capstone |
|---|---|---|---|
| [**1 · Introduction**](1-introduction/) | Scratch creations, turtle drawings, and interactive art | Events, loops, decisions, variables, and Python basics | **My Interactive Art Show** · reference: *Night Sky Postcard* |
| [**2 · Intermediate**](2-intermediate/) | Games and small data-powered programs | Functions, lists, dictionaries, files, testing, and game design | **Arcade Game or Art Studio** · reference: *Star Catcher* |
| [**3 · Advanced**](3-advanced/) | Larger programs that are easier to change | Classes, algorithms, Git, data, and simple AI | **Build Something Big** · reference: *Maze Muncher* |

> **Younger children (Grades 2–3, ages 7–9):** a gentler **junior track** of
> three 10-week levels (*Little Robots*, *Game Makers*, *Bridge to Python*) of
> unplugged games and Scratch, ending with a first look at Python and leading
> into Level 1 above. **Junior Level 1 is ready to teach** (`make pdf LEVEL=j1`);
> Levels 2–3 are planned. See [junior/](junior/) and the
> [junior syllabus](docs/JUNIOR-SYLLABUS.md). The junior track is not on the website yet.

<div align="center">

**Create → explain → test → improve → share**

</div>

## Quick start

### If you are teaching a family

1. **[Open the course website](https://rrahimi-uci.github.io/kids-coding-curriculum/)** to browse the curriculum and printable student resources.
2. **[Set up each Mac](https://rrahimi-uci.github.io/kids-coding-curriculum/resources/setup-mac/)** with the current Scratch, Thonny, Python, pytest, and Git instructions.
3. Read the level’s **Teacher Guide** and print the Student Workbook and Homework for each child.
4. Start with Level 1, Week 1. Each week has a lesson plan, student practice, homework, and a clear definition of “done.”

For an offline student copy, build a solution-free bundle:

```bash
make student-bundle          # all three levels
make student-bundle LEVEL=1  # Level 1 only
```

The output is `build/student-bundle/kids-coding/` and a matching ZIP file. Copy
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
1-introduction/        Level 1: Scratch, then Python turtle
2-intermediate/        Level 2: functions, data, files, testing, and games
3-advanced/            Level 3: OOP, algorithms, Git, data, and simple AI
junior/                junior track for Grades 2-3 (Level 1 written; Levels 2-3 planned)
curriculum.json        which tracks and levels exist, their folders and week counts
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
<level>/exercises/weekNN/<exercise>/
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
is generated from the same source files as the printable curriculum. The build
converts workbooks, exercise folders, figures, and selected parent materials;
it does not copy pages by hand. A private-content check prevents answer keys,
solutions, lesson plans, teacher guides, and tests from being published.

Every week page also shows that week's animated teaching video, *Kids Coding
with Rose and Pixi*, in the same place, right below the page header, with captions
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
make pdf LEVEL=2    # build one level
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

`make help` prints the complete command list. `LEVEL=1|2|3|j1` narrows PDF and
student-bundle commands; omit it to include all levels. Level keys, folders
and week counts come from [`curriculum.json`](curriculum.json); a level marked
`planned` there is skipped by every command until its content exists.

## Documentation guide

* [Syllabus](docs/SYLLABUS.md) — scope, sequence, goals, and spiral map
* [Junior syllabus](docs/JUNIOR-SYLLABUS.md) — the planned Grades 2–3 track: levels, weeks, goals, and junior rules
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
