# Authoring guide (style, layout and conventions)

Read this before adding or editing any lesson, workbook chapter, homework set,
exercise or document. The automated checks in `testing/test_repo_structure.py`
enforce most of it.

## 1. Repository layout

```
<level>/                         1-introduction | 2-intermediate | 3-advanced
  teaching-material/
    teacher-guide.tex            Teacher Guide (main document)
    lesson-plans.tex             main doc -> \input{lessons/weekNN}, buffer1, buffer2
    student-workbook.tex         main doc -> \input{workbook/weekNN}
    homework.tex                 main doc -> \input{homework/weekNN}
    answer-key.tex               main doc -> \input{answers/weekNN}, answers/assessments
    assessments.tex              placement (L2, L3) / checkpoint / exit papers + rubrics
    lessons/week01.tex … week12.tex, buffer1.tex, buffer2.tex
    workbook/week01.tex … week12.tex
    homework/week01.tex … week12.tex
    answers/week01.tex … week12.tex, assessments.tex
    extras/cheat-sheet.tex, glossary.tex, progress-tracker.tex,
           parent-notes.tex, certificate.tex          (each a main document)
  exercises/
    weekNN/<slug>/               one folder per exercise (in-class "ex-" or homework "hw-")
  project/
    project-brief.tex            student-facing brief, milestones, rubric
    project-teacher-guide.tex    teacher walkthrough, reference solution, showcase plan
    reference/                   complete, tested reference solution (+ test_*.py)
    starter/                     starter template students begin from
shared/latex/kidscode.cls        the document class (all styling lives here)
shared/latex/kidscode-breaks.lua lets long code names and paths wrap after / _ . -
testing/kidtest/                 fake turtle + runners used by every test
```

Names are lowercase kebab-case for folders and documents (`lesson-plans.tex`,
`ex-star-row/`) and snake_case for Python files (`test_star_row.py`), because
Python files must be importable.

Main documents (files with `\documentclass`) are found automatically by
`tools/build.py`. Week files never contain `\documentclass` or
`\begin{document}`.

## 2. LaTeX conventions

* Class: `\documentclass[level=1]{kidscode}`; add `teacher` for teacher-only
  documents (lesson plans, teacher guide, answer key, project teacher guide,
  parent notes are *not* teacher-only — they are for parents).
* Start each main document with `\kctitle{Title}{Subtitle}` then
  `\tableofcontents` (when longer than ~6 pages).
* Start each week file with `\lesson{N}{Title}{Big idea}` (lesson plans),
  `\chapterweek{N}{Title}{Big idea}` (workbook), `\homeworkweek{…}`,
  `\answersweek{…}`. Buffer sessions use `\kcpart{B1}{Title}{Big idea}`.
  Under the banner use `\lessoninfo{Concepts: …}{Tools: …}{CSTA: …}`.
* Write UTF-8. Use real quotes “like this” or `\enquote{…}` — **never
  ``` `` ''```** (the font has no backtick glyph).
* Do not load extra packages in week files; ask for them in the class.
* Avoid italics for body text (harder for dyslexic readers). Use bold sparingly.
* Diagrams: TikZ, using the palette colors below, always with text labels.
* Scratch blocks: use the `scratch3` package environment
  `\begin{scratch} … \end{scratch}` (commands like `\blockinit{when \greenflag clicked}`,
  `\blockmove{move \ovalnum{10} steps}`, `\blockrepeat{repeat \ovalnum{4}}{…}`,
  `\blockinfloop{forever}{…}`, `\blockif{if \boolsensing{touching \ovalsensing*{edge} ?} then}{…}`,
  `\blockifelse{…}{…}{…}`, `\blocklook{say \ovalnum{Hello!} for \ovalnum{2} seconds}`,
  `\blockpen{pen down}`, `\blockvariable{change \selectmenu{score} by \ovalnum{1}}`,
  `\ovalvariable{score}`, `\ovaloperator{pick random \ovalnum{1} to \ovalnum{10}}`,
  `\blockevent{when \selectmenu{space} key pressed}`, `\blockcontrol{wait \ovalnum{1} seconds}`,
  `\blocksensing{ask \ovalnum{What's your name?} and wait}`, `\blockmoreblocks{define \ovalmoreblocks{flower}}`).
* Code shown in PDFs must be **the tested file**: include it with
  `\pyfile{../exercises/week07/ex-square/solution.py}` (path relative to the
  main document's folder, i.e. `teaching-material/`; from `project/` use
  `reference/…`). Short illustrative snippets may use
  `\begin{pycode}[title] … \end{pycode}`. Inline code: `\py{print("hi")}` or
  `\py|x = 5|`. Put `\pyfile` and long `pycode` blocks **outside** other
  boxes (`answer`, `workedexample`, …): a box inside a box cannot break
  across pages and will run into the footer. Terminal: `\begin{shellcode}`. Output: `\begin{outputcode}`.
* Writing space for students: `\answerlines{3}`, `\answerspace{4cm}`,
  `\namedateline`.

### Box environments (all carry an icon + word label, never color alone)

| Environment | Use |
|---|---|
| `objectives` | `\item The student can …` (every item must start exactly like that) |
| `materials` | itemized list of what to prepare |
| `timeplan` + `\timeslot{0--8}{Warm-up}{…}` | minute-by-minute table |
| `teacherscript[Say]` | words the parent can read aloud |
| `analogy[title]` | kid-friendly analogy |
| `workedexample[title]` | step-by-step worked example |
| `commonmistakes` | itemized misconceptions + fixes |
| `differentiation` with `\supportpath …` and `\extensionpath …` | |
| `stretchchallenge[title]` | stretch challenge |
| `formativecheck[title]` | quick check for understanding / exit ticket |
| `unplugged[title]`, `bughunt[title]`, `pairroles[title]`, `freebuild[title]` | the four level threads |
| `reflection[title]` | reflection prompts |
| `safety[title]` | digital citizenship & safety thread |
| `teachernote[title]`, `tip[title]` | side notes |
| `vocab` + `\vocabword{term}{kid-friendly definition}` | vocabulary box |
| `exercise[title]` | numbered in-class exercise (auto “Exercise 7.2”) |
| `scratchspec[title]` | Scratch exercise: expected behavior + checklist |
| `core`, `challenge`, `creative`, `selfcheck` | homework tiers + self-check list |
| `checklist` | ☐ list anywhere |
| `answer[title]`, `rubric[title]` | answer key / rubrics |

## 3. Lesson plan template (every week, every buffer)

Copy `shared/templates/lesson.tex`. Required, in this order:

1. Banner + `\lessoninfo`.
2. `objectives` (3–4 items, “The student can …”, each tagged with the goal
   code, e.g. `(L1.G2)`).
3. `materials` (including what to print and what to open on the Macs; prep
   ≤ 10 minutes).
4. `timeplan` with exactly these phases (names must appear verbatim):
   **Warm-up** (≈ 0–8), **Concept** (≈ 8–18), **Guided demo** (≈ 18–28),
   **Hands-on build** (≈ 28–52, includes pair-programming swaps and a few
   minutes of creative free-build), **Wrap-up** (≈ 52–60: show-and-tell,
   reflection, exit ticket, homework hand-out).
5. Teacher script for each phase (`teacherscript`), with at least one
   `analogy`.
6. `workedexample` (the guided demo, step by step, with the tested code).
7. `unplugged` / `bughunt` / `pairroles` / `freebuild` / `safety` boxes as the
   syllabus specifies for that week (each level needs ≥ 6 unplugged,
   ≥ 10 bug hunts, ≥ 10 pair-roles, ≥ 10 free-builds, ≥ 5 safety boxes).
8. `formativecheck` (what to look for + one exit-ticket question with answer).
9. `commonmistakes`, `differentiation` (support + extension path),
   `stretchchallenge`, `reflection` prompts.
10. “If you are short on time” note (what to cut) in a `teachernote`.

Length: 3–5 pages. A parent with no CS background must be able to teach it
after 10 minutes of reading. Say exactly what to click, type and say.

## 4. Workbook chapter (student-facing, one per week)

Copy `shared/templates/workbook.tex`. Friendly second person (“you”), short
sentences, Grade 5 reading level for Level 1, Grade 6–7 for Levels 2–3.
Required: explanation with at least one diagram (TikZ) or Scratch-block
picture, 2–4 `exercise` boxes (in-class, matching the exercise folders), a
`vocab` box and a `reflection` box. 3–5 pages.

## 5. Homework set (15–20 minutes, one per week)

Copy `shared/templates/homework.tex`. `core` (everyone, ~10 min), `challenge`
(optional, harder), `creative` (open-ended art/game twist) and `selfcheck`
(checklist). Coding homework lives in `exercises/weekNN/hw-<slug>/`. Week 10–12
homework is project work / reflection. Never require internet, accounts or
sharing personal data.

## 6. Answer key (teacher only)

`answers/weekNN.tex`: answers for every workbook exercise and homework task
(include the tested solution via `\pyfile`, plus what “good” looks like for
open-ended tasks), expected Scratch behavior, and scoring notes.
`answers/assessments.tex`: answers + rubrics for placement/checkpoint/exit.

## 7. Exercise code and tests

Each **Python** exercise folder `exercises/weekNN/<slug>/` contains:

| File | Purpose |
|---|---|
| `README.md` | Kid-friendly task, what “done” looks like, how to check (open `check_my_work.py`, press Run) |
| `starter.py` | What the student opens and edits. Has `# TODO` markers, runs without crashing where practical |
| `solution.py` | Complete reference answer (teacher) |
| `test_<slug>.py` | pytest checks with friendly assertion messages |
| `check_my_work.py` | exact copy of `testing/check_my_work_template.py` |
| `smoke_inputs.txt` | (only if the program calls `input()` and uses turtle) one answer per line for the real-window smoke run |

Slugs: `ex-<name>` for in-class, `hw-<name>` for homework, lowercase with
hyphens, e.g. `exercises/week08/ex-polygon-party/`.

Each **Scratch** exercise folder has only `README.md` with the sections
`## Expected behavior` and `## Checklist` (a `- [ ]` list), plus the build
steps and the scripts described in words.

Python code rules:

* Python **3.10** compatible (Thonny's bundled version), **standard library
  only**, **ASCII only** (no emoji: the PDF code font cannot print them).
* Kid-readable: clear names, short functions, comments that explain *why*.
  Level 1 code is top-level script code until functions are taught (week 10).
* Colors: use the color-blind-safe Okabe–Ito palette and never rely on
  color alone in games (use shape/size/text too):

  ```python
  PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
             "#0072B2", "#D55E00", "#CC79A7", "#000000"]
  ```
* Never ask for real names, ages, addresses, schools, photos or passwords.
  Use “nickname”, “hero name”, “favorite color”.
* Turtle programs end with `turtle.done()`. From Level 2, put the main
  program under `if __name__ == "__main__":` and keep logic in functions
  so tests can import them.
* Games: keep **logic** (pure functions / classes, no turtle) separate from
  **drawing** so logic can be unit-tested.
* Files written by programs (high scores, saved art) go next to the program
  and must be created if missing.

Test rules (pytest, see `conftest.py` and `testing/kidtest`):

* Never import `solution` or `starter` by name. Use the fixtures:
  `run_target(inputs=[...], seed=...)` runs the program and returns a
  `RunResult` (`.stdout`, `.turtle`, `.turtles`, `.lines`, `.screen`,
  `.namespace`); `load_target()` imports it as a module (main block not run);
  `inputs([...])` is a context manager that answers `input()` calls.
* `RunResult.turtle` is a `FakeTurtle` with `.lines` (each has `.start`,
  `.end`, `.color`, `.length`), `.dots`, `.fills`, `.texts`, `.stamps`,
  `.total_turn`, `.distance_traveled`, `.colors_used`, `.count("forward")`,
  `.position()`, `.heading()`, `.is_back_at_start()`.
  The screen supports `.press("Left")`, `.click(x, y)`, `.run_timers(n)`,
  `.bg`, `.key_handlers`.
* Test behavior the student can see, not exact code. Accept many correct
  solutions (e.g. any square of side ≥ 50, not exactly 100).
* Assertion messages are for a 10–13-year-old: say what was expected and a
  hint, e.g. `assert n == 4, f"A square needs 4 sides, but your turtle drew {n}."`
* 2–5 tests per exercise. Tests must pass against `solution.py` and should
  fail against the untouched `starter.py` (that is what makes them useful).
* Project tests may load several files with
  `kidtest.load_module(Path(__file__).parent / "file.py")`. Give project
  modules level-unique names (e.g. `starcatcher_logic.py`).

Run before committing:

```bash
make test                     # all pytest checks (fast, headless)
make smoke                    # every turtle program in a real window (Mac)
python3 tools/build.py --level 1 --variant standard   # PDFs for a level
```

## 8. Tone and inclusion

* Address a mixed group of girls and boys; use varied names in examples
  (Ada, Sam, Priya, Leo, Mei, Omar, Zoe, Kai). Never gender a learner role.
* Celebrate mistakes (“bugs are normal”); never “easy”/“just”/“obviously”.
* Every lesson works with 1–4 students: say what to do with 1 student
  (parent is navigator) and with an odd number (rotating trio).
* Color-blind safe: palette below; diagrams also use labels/patterns.
* US English everywhere: color, favorite, center, behavior, math, mom,
  “check off” (not “tick”), “score” (not “mark”). `make test` rejects common
  UK spellings.
* Offline-first: no accounts, no logins, no uploading. Links are optional
  references, never required.

## 9. Palette

| Name | Hex | LaTeX color |
|---|---|---|
| Orange | `#E69F00` | `kcorange` |
| Sky blue | `#56B4E9` | `kcsky` |
| Bluish green | `#009E73` | `kcgreen` |
| Yellow | `#F0E442` | `kcyellow` |
| Blue | `#0072B2` | `kcblue` |
| Vermillion | `#D55E00` | `kcvermillion` |
| Reddish purple | `#CC79A7` | `kcpurple` |
| Black | `#000000` | `kcblack` |


## 10. Website conventions

The website is generated from these sources (see [SITE-DESIGN.md](SITE-DESIGN.md)); a few conventions keep
the web pages correct:

* **Alt text for diagrams.** Put `%% alt: ...` (one line, no percent signs) directly above every
  `\begin{tikzpicture}` in student-facing files. It is a LaTeX comment, so the PDF is unchanged. The build
  fails if a TikZ figure has none. Scratch scripts get their description automatically.
* **Objectives.** Every workbook chapter starts with a `\section{What you will learn}` list (or
  `What you will do today`); the website shows it as the lesson's objectives and fails without it.
* **Hints.** Every exercise folder has a `hints.md` with exactly three hints, written for a Grade 5 reader:

  ```markdown
  ## Hint 1: Where to look
  A nudge: point at the part of the screen or file to focus on. No answer.

  ## Hint 2: Try this
  Name the block or command to use and what it does.

  ## Hint 3: Almost there
  The most specific hint: show the shape with blanks, e.g. `t.left(____)`. Never the finished program.
  ```
* **Public or private.** What may be published is decided by `site/manifest.yml` (deny by default). To publish a
  new kind of file, add it there on purpose. Never put answers into a workbook, homework or exercise
  `README.md`/`starter.py`/`hints.md`: those files are public.
* **The self-check script** (`check_my_work.py`) is not published, so web pages drop the sentences that tell
  children to run it; the PDFs keep them.
