# Design decisions

This document explains *why* the curriculum and the repository look the way
they do. The *what* (weeks, goals, concepts) is in [grade-4-6/SYLLABUS.md](../grade-4-6/SYLLABUS.md);
the conventions for writing new material are in [AUTHORING.md](AUTHORING.md);
everything that was unspecified and had to be decided is in
[ASSUMPTIONS.md](ASSUMPTIONS.md).

## 1. Language path

The suggested path is kept unchanged:

| Level | Language & tools | Why |
|---|---|---|
| 1 Introductory | Scratch 3 (weeks 1–6) → Python + `turtle` in Thonny (weeks 7–12) | Block coding removes syntax errors so 9–11-year-olds can focus on sequence, loops, events and variables, and it is excellent for games and art. Six weeks is enough for those ideas to stick; `turtle` then gives an immediate visual payoff for the first text code, and every Scratch concept is re-taught in Python (spiral). |
| 2 Intermediate | Python (Thonny, standard library) | Functions, lists, dicts, files, testing and event-driven turtle games cover the intermediate goals without installing anything else. |
| 3 Advanced | Python projects + local git | OOP, algorithms, grids/recursion, data and simple AI are all teachable with the standard library; git is the industry “save game”. |

Alternatives considered and rejected:

* **pygame / Pygame Zero for games.** More capable, but needs package
  installation on every Mac, behaves differently across versions, and is hard
  to test headlessly. `turtle` with `onkey`/`ontimer` is enough for the
  games in this course and ships with Thonny. Faster learners are pointed at
  Pygame Zero as an extension in Level 3.
* **Online platforms (code.org, Replit, Scratch online, GitHub).** All need
  accounts or personal data, which the brief rules out.
* **JavaScript/p5.js for art.** Great for art, but adding a second text
  language before Python is solid splits attention.

## 2. Session shape

Every one of the 42 sessions uses the same five phases — **Warm-up (≈8 min) →
Concept (≈10) → Guided demo (≈10) → Hands-on build (≈24, with pair swaps
and a few minutes of free-build) → Wrap-up (≈8)**. A parent who is not a
teacher benefits most from predictability: after two weeks the routine runs
itself, and the plan can be skimmed in ten minutes. The children benefit from
knowing that there is always making time and always a show-and-tell.

## 3. Level rhythm, review and buffers

Each level runs **10–12 weeks**, one session a week (holiday weeks without a
session do not count). It has 12 core sessions plus 2 optional buffer sessions:

* weeks 1–5 new content, **week 6 review + checkpoint**, weeks 7–9 new
  content, weeks 10–11 project studio, **week 12 showcase + exit**;
* **12-week plan:** the 12 core sessions in order.
* **10-week plan:** merge two pairs of weeks named in each Teacher Guide
  (Level 1: weeks 3+4 and 8+9; Level 2: weeks 4+5 and 10+11; Level 3: weeks
  4+5 and 7+8). Weeks 6 and 12 are never merged. The same merges are how a
  12-week plan absorbs lost sessions without running past 12 weeks.
* B1 (unplugged-heavy) and B2 (free-build/remix) are complete, ready-to-run
  sessions that are **optional**: use them only when there is room inside
  the 12 weeks (for example a 10-week plan plus one or two buffers).

Three levels take 30–36 weeks of sessions (sample calendars are in each
Teacher Guide).

## 4. Spiral curriculum

Big ideas are introduced, revisited and extended across lessons and levels
(see the spiral map at the end of [grade-4-6/SYLLABUS.md](../grade-4-6/SYLLABUS.md)). Examples:
loops appear as Scratch `repeat` (L1 W2), Python `for` (L1 W8), `while` and
nested loops (L2 W4), game loops (L2 W9), search loops (L3 W4) and recursion
(L3 W7). Custom blocks (L1 W5) → `def` (L1 W10) → `return` (L2 W2) →
methods (L3 W2).

## 5. Teaching threads present in every level

| Thread | How it is guaranteed |
|---|---|
| Unplugged activities | ≥ 6 per level (checked by `make test`) |
| Bug hunts | ≥ 10 per level, plus review-week bug-hunt workshops |
| Pair programming roles | ≥ 10 per level; driver/navigator (+ reviewer/tester at Levels 2–3), with instructions for 1, 2, 3 or 4 students |
| Creative free-build | ≥ 10 per level + buffer B2 |
| Reflection prompts | every lesson + every workbook chapter |
| Digital citizenship & safety | ≥ 5 per level, following the syllabus thread (privacy → credit → accessibility → data/encryption → consent → AI ethics) |
| Formative checks | every lesson has an exit ticket |

## 6. Documents: LaTeX, one class, two editions

* **LaTeX** (LuaLaTeX) gives print-quality, version-controlled documents
  with consistent styling from one class file (`shared/latex/kidscode.cls`).
* **Fonts.** Standard edition: *Atkinson Hyperlegible Next* (designed by
  the Braille Institute for letter distinction) and *Atkinson Hyperlegible
  Mono* for code (clear 0/O, 1/l/I). Dyslexia-friendly edition: *Lexend Deca*
  with larger size, 1.5 line spacing, extra letter and word spacing,
  ragged-right text, no italics and a cream page. Both fonts ship with
  TeX Live, so the build is reproducible.
* **Color.** Only the Okabe–Ito color-blind-safe palette. Every colored
  box also has an icon and a word label, so no meaning relies on color.
* **Single source of truth for code.** PDFs include solutions with
  `\pyfile{…}` directly from the tested `.py` files, so printed code can
  never drift from the code that passes the tests.
* PDFs are build outputs (git-ignored). `make pdf` builds them locally and
  CI uploads them as a downloadable artifact on every PR.

## 7. Exercises and automated checks

* Each Python exercise is a folder with `starter.py`, `solution.py`,
  `test_*.py`, `check_my_work.py` and a README. The same tests run against
  the solution in CI and against the student's starter when a child presses
  **Run** on `check_my_work.py` in Thonny (kid-friendly PASS / TRY AGAIN
  output with hints).
* `testing/kidtest` provides a **fake turtle** that records lines, fills,
  colors, text, key handlers and timers, so drawing programs and games are
  tested headlessly and fast (CI runs on Linux without a display).
* A separate **smoke run** (`make smoke`) opens every turtle program in a
  real Tk window on the Mac, proving the code also works with the real
  `turtle` module.
* Scratch exercises are described (expected behavior + checklist), because
  Scratch projects cannot be meaningfully unit-tested.
* Games keep logic (pure functions/classes) apart from drawing (turtle).
  That is good design to teach and it makes logic unit-testable.
* Python 3.10 is the minimum (Thonny's bundled interpreter); the test
  environment uses 3.10 to catch newer-only syntax.

## 8. Quality gates (`make test`)

`testing/test_repo_structure.py` enforces that every week has a lesson,
workbook chapter, homework set and answers; that lessons contain every
required section and the five phases; that objectives are phrased “The
student can …”; that each level meets the thread minimums; that exercise
folders are complete; and that all Python compiles on 3.10 and is ASCII
(the PDF code font has no emoji). `tools/coverage.py --check` keeps the
coverage tables current.

## 9. Privacy and safety by design

No accounts, no internet requirement, no personal data: programs ask for
nicknames or favorite colors, git uses a nickname and a placeholder email,
data exercises use made-up anonymous data, certificates are filled in by
hand, and showcases happen on screen at home with nothing uploaded.

## 10. Tracks and `curriculum.json`

The repository holds two **tracks**, one per grade band: the **junior track**
(Grades 2–3, three 10-week levels, in `grade-2-3/`, see [grade-2-3/SYLLABUS.md](../grade-2-3/SYLLABUS.md)).  and the main track (Grades 4–6, three 12-week levels:
Introductory, Intermediate and Advanced, in `grade-4-6/`, see
[grade-4-6/SYLLABUS.md](../grade-4-6/SYLLABUS.md)). Both share the
LaTeX class, palette, website pipeline, student copy, privacy checks and video
kit, which is why the junior track lives here rather than in a second
repository.

[`curriculum.json`](../curriculum.json) is the single list of tracks and
levels: each track's band folder (`grade-2-3`, which is also its path on the
website) and syllabus, and each level's key (`1`, `j1`, ...), folder, goal-code prefix (`L1`,
`J1`), number of core weeks and buffers, and status. `tools/curriculum.py`
reads it, and the PDF build, coverage tables, student copy, website build and
quality gate all ask it instead of hard-coding level folders or twelve weeks
(`testing/test_curriculum.py` fails if a hard-coded list comes back).

A level is `planned` (declared, with a README in its folder, skipped by every
build and check) or `active` (fully written and checked like any other
level). Every level folder lives inside its track's band folder (the loader
rejects one that does not), so a band is self-contained: its syllabus, README
and levels. Level keys stay short and unique across bands (`1`, `j1`) because
both bands have a Level 1, 2 and 3; on the website and in download names a
level is always qualified by its band (`grade-4-6/level-1/`).
