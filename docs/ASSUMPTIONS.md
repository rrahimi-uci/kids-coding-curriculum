# Assumptions

The brief asked for no clarifying questions. Wherever something was not
specified, the choice below was made. Each line says what was assumed and,
where useful, how to change it.

## Students, setting and schedule

1. **Group size and pairing.** Up to 4 students work as 2 pairs. Every lesson
   says what to do with 1 student (the parent is navigator), 2, 3 (rotating
   trio: driver / navigator / tester) or 4.
2. **Computers.** At least one Mac per pair; with one Mac per child, pairs
   still share one Mac for the hands-on build and use their own Mac for
   free-build.
3. **Location and calendar.** The family is in the United States: US Letter
   paper, US school holidays in the sample calendars, CSTA standards.
   For A4, change `letterpaper` to `a4paper` in `shared/latex/kidscode.cls`.
4. **Start date and length.** Each level runs **10–12 weeks** (one session
   a week; holiday weeks without a session do not count). Sample calendars
   start Level 1 in January 2027, Level 2 in May 2027 and Level 3 in
   September 2027.
   Lessons are numbered by week, not date, so any start date works.
5. **Session length.** 60 minutes including setup; Macs are switched on and
   apps opened before the session starts (listed in each lesson's
   materials box).
6. **Reading level.** All student materials (workbooks, homework, exercise
   instructions, hints, assessments, project briefs) target a **Grade 4–5
   reading level** at every level, because the youngest learners are in
   Grade 4 when they take the course (changed from Grade 5 / Grade 6–7 in the
   Grade 4–5 review, November 2026; the track was widened to Grades 4–6 in
   version 2.0.0 without changing the reading level, so it still fits the
   youngest readers). Concepts are not removed for younger
   readers; they get analogies, worked examples and extra practice steps.
   Teacher-facing material (lesson plans, answer keys, guides) stays at an
   adult reading level.
6a. **Math prerequisites.** Code and questions only assume math a Grade 4–5
   student has met (US Common Core): whole-number arithmetic, division with
   remainders, fractions, decimals to hundredths, angles in degrees with a
   full turn of 360°, first-quadrant coordinates. Ideas from Grade 6 and up
   (negative numbers and the four-quadrant plane, mean/average as a formula,
   percent, the `%` operator, halving/doubling growth, distance between
   points) get a short kid-friendly “Math helper” the first time they appear,
   or the task is changed so it does not need them.
7. **Homework.** Optional but encouraged, 15–20 minutes, done at home on a
   Mac with Scratch/Thonny. Core tier for everyone; Challenge and Creative
   are optional. No homework needs internet.
8. **Teacher background.** The parent has no CS teaching background.
   Lessons include teacher scripts, analogies and (Level 3) short “CS
   background for the parent” notes.

## Software and setup

9. **Scratch.** The free offline Scratch 3 app (“Scratch app”) is installed
   on each Mac; no Scratch account is created and nothing is shared online.
10. **Scratch exercise files.** Scratch exercises are specified as build
    steps + expected behavior + checklist (no `.sb3` starter files), because
    generated `.sb3` files cannot be verified without the Scratch app and
    building from scratch is part of the learning.
11. **Thonny.** Thonny 4.x with its bundled Python (3.10+) is installed on
    each Mac. All code targets **Python 3.10** and uses the standard library
    only, so no packages are needed apart from **pytest**, which is installed
    once through Thonny's *Tools → Manage packages* (needs internet once, no
    account). Students who cannot install it can still do every exercise;
    only `check_my_work.py` needs pytest.
12. **Course files on the Macs.** Each child's Mac gets the **student
    copy** made by `make student-bundle` (`tools/student_bundle.py`): every
    exercise folder without `solution.py`/`solution.md`, the project starters,
    `testing/kidtest`, `conftest.py` and `pytest.ini`, plus a `START-HERE.txt`.
    It is copied via USB stick or AirDrop. `check_my_work.py` finds the helpers
    by walking up the folders, so children can self-check alone without having
    the solutions. (Before the Grade 4–5 review the whole repository was
    copied, which put every answer on the child's Mac.)
13. **Git.** Level 3 uses git locally via Apple's free Command Line Tools
    (`xcode-select --install`). No GitHub or other hosting account is used
    by students; `user.name` is a nickname and `user.email` a placeholder.
    This step is a privacy safeguard, not a formality: on macOS, git with no
    `user.name` does not refuse to commit, it silently records the Mac
    account's real name and host name. The Mac setup guide and the git quest
    therefore ask the child to check `git config user.name` before the first
    commit.
14. **Games library.** Games use `turtle` (`onkey`, `ontimer`) rather than
    pygame, so nothing extra is installed (see DESIGN.md §1).
15. **PDF tooling.** The parent (or CI) builds PDFs with TeX Live/MacTeX and
    LuaLaTeX (`make pdf`). PDFs are not committed; CI attaches them to each
    PR as a downloadable artifact.
16. **Fonts.** Atkinson Hyperlegible Next/Mono (standard) and Lexend Deca
    (dyslexia-friendly edition) from TeX Live. OpenDyslexic was not used
    because it is not distributed with TeX Live and the evidence for Lexend
    and Atkinson is at least as good; any OpenType font can be swapped in
    the class file.

## Content and pedagogy

17. **Folder names.** Each track is a grade-band folder: `grade-2-3/`
    (Kids Coding Junior) and `grade-4-6/`. Inside, levels are named after
    their titles: `grade-4-6/1-introductory`, `2-intermediate` and
    `3-advanced`; `grade-2-3/1-little-robots`, `2-game-makers` and
    `3-bridge-to-python`, each with `exercises/`, `project/` and
    `teaching-material/` inside. The first draft kept the owner's original,
    misspelled folder names; they were corrected before the first merge.
    Version 2.0.0 moved the levels from the repository root (and `junior/`)
    into the band folders and renamed Level 1 *Introduction* to
    *Introductory*, matching *Intermediate* and *Advanced*; the website
    redirects the old `/levels/level-N/` addresses.
18. **Level 1 placement.** No placement quiz before Level 1 (the brief says
    no prior experience); an ungraded interest & comfort survey is used
    instead. Placement quizzes are given before Levels 2 and 3 as requested.
19. **Standards.** CSTA K-12 CS Standards (revised 2017) and AI4K12's Five
    Big Ideas. Level 3 deliberately borrows some grades 9–10 (3A) standards
    (see STANDARDS.md). Standard wording is abridged and should be verified
    against the official documents for formal use.
20. **Grading.** Assessments are formative and celebratory, not grades:
    rubrics use four levels (Just starting / Getting there / Got it /
    Expert) and value creativity, working code and the ability to explain
    it equally.
21. **Final projects.** Each level offers a choice of project type with one
    complete, tested reference solution (Level 1 *Night Sky Postcard*, Level
    2 *Star Catcher*, Level 3 *Maze Muncher*). The reference solution is a
    teacher resource and example, not a template students must copy.
22. **Unicode in code.** Python files are ASCII-only (no emoji), because the
    code font used in the PDFs cannot render emoji and older Thonny/Tk builds
    on macOS show them inconsistently.
23. **Data and AI.** All datasets are small, made-up and anonymous; AI is
    taught through transparent, hand-built models (nearest neighbor,
    Markov chains) rather than online AI services, which would need
    accounts and send data off the computer.
24. **Inclusive examples.** Examples use a varied set of first names and
    never assign coding roles by gender.

## Workflow

25. **Version control.** The repository was initialized for this work with an
    empty commit on `main`; all content arrives through a pull request from a
    feature branch, following the owner's PR-only policy, and the PR is left
    open for the owner to review and merge.
26. **Hosting.** The GitHub repository `kids-coding-curriculum` is **public** under the owner’s account
    (the owner’s decision on 2026-11-08; it was first planned as private because it contains teacher-only
    answer keys, see 39).

## Decisions made while writing the levels

27. **Scoring scales.** Level 1: checkpoint /9, exit /14, project rubric
    5–20. Level 2: placement /14 plus a 1-point bonus (0–6 support path,
    7–11 standard, 12–15 extension; the bonus counts toward the bands), checkpoint /18, exit /20, project /16. Level 3: project /24
    (6 criteria × 4). Scores guide support, they are never grades.
28. **Sample calendars** use Saturday sessions and the 12-week plan (12 core
    sessions, no buffers): Level 1 9 Jan–10 Apr 2027 (skipping Presidents' Day
    weekend and spring break); Level 2 8 May–14 Aug 2027 (skipping Memorial
    Day weekend, Juneteenth and July 4 weekend); Level 3 11 Sep–4 Dec 2027
    (skipping Labor Day and Thanksgiving weekends).
29. **Placement and checkpoint timing.** Placement quizzes take the first 15
    minutes of week 1's warm-up; mid-level checkpoints (15 min) sit inside
    week 6's hands-on build.
30. **pytest in Thonny.** Installed once by the parent during Level 1 week 7
    prep (needs internet once). Students run pytest from Thonny's
    *Tools → Open system shell…* (`python -m pytest`), because macOS's own
    Terminal `python3` does not have pytest.
31. **Student-written tests (Level 2 week 8).** The student's test file is
    checked like a tiny mutation test: at least 3 tests, all passing on the
    correct code and each of 3 deliberately broken versions failing at least
    one test.
32. **Starter files never contain syntax errors**, because the quality gate
    compiles every `.py`; syntax-error bug hunts are done on paper or on the
    parent's Mac.
33. **Scratch details.** The Mac App Store listing is “Scratch 3”; library
    sprites used (Balloon1, Bowl, Apple, Ghost, Star, Ballerina) exist in the
    Scratch library; palette colors are given as Scratch color/saturation/
    brightness values (e.g. bluish green = 45/100/62).
34. **Git practice.** Each Level 3 student keeps one `Documents/git-quest`
    repository for the term and builds the final project in
    `~/Documents/coding-projects/<name>`, starting from a copy of
    `project/starter`.
35. **Partial code listings** in Level 3 use `\pyfile[firstline=…,lastline=…]`;
    if a solution file changes, those line ranges must be checked.
36. **Glossaries** contain the level's core vocabulary plus a “More words from
    your workbook” section, so every word in a workbook vocabulary box is in
    the glossary (checked by `make test`).
37. **Lesson length.** Lesson plans run about 5–7 pages rather than the 3–5
    pages first planned: the extra space is teacher script, printable cards
    and setup steps a non-teacher parent needs. Each plan opens with an
    “At a glance” table that fits on one page for quick reading.
37a. **Workbook length after the Grade 4–5 review.** A few workbook
    chapters (Level 3 weeks 7 and 9) now run 6–7 pages instead of 3–5,
    because the scaffolding for Grade 4–5 readers (math helpers, worked
    examples, “try it” practice, “Done looks like” lines) was kept rather
    than cut. Optional stretch sections are marked as such.
38. **US English.** All text and code use US spelling and school vocabulary
    (color, favorite, math, check off, score), matching the US setting
    (#3) and Python's own `color`, so kids never meet two spellings of one word.
    `make test` rejects common UK spellings (`testing/test_consistency.py`).

## Website

39. **Hosting.** GitHub Pages, deployed by GitHub Actions from `main`. The owner chose a public repository.
    Because answer keys, teacher guides, reference solutions and tests live in the same repository, anyone
    can read them in the source (and in the git history) even though the website does not publish them.
    Children should get the student copy (`make student-bundle`, see 12), never the repository folder;
    the student copy, the website and the printed student editions contain no solutions.
40. **What is published.** Student workbooks, homework, exercise instructions, starter code, hints, the parent
    deck and handout. Assessments (placement, checkpoint and exit quizzes) are not published.
41. **Hints and alt text** are new, reviewed content: three hints per exercise (`hints.md`) and a `%% alt:`
    description above each diagram. They are written for a Grade 4–5 reader and checked by the build.
42. **No analytics, cookies or accounts.** Only the display settings (dark mode, easy-read font) are
    stored, in the visitor's own browser (local storage). The pages have no progress tracking.
43. **Invented character names** (such as the children in bug-hunt exercises) appear in a few exercises; they
    are fictional, not real children.
