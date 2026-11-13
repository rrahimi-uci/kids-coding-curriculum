# Grades 4–6: Kids Coding

The main course for children aged 9–12: Scratch first, then Python, Git, data
and a first look at AI, in three levels. Children who finished
[Grades 2–3](../grade-2-3/) (Kids Coding Junior) start at Level 1 and will find
much of it familiar.

> The scope and sequence (weeks, goals, concepts and final projects) is in
> [SYLLABUS.md](SYLLABUS.md). The levels are on the
> [website](https://rrahimi-uci.github.io/kids-coding-curriculum/grade-4-6/).

| Level | Folder | Weeks | You will build | Final project |
|---|---|---|---|---|
| 1 · Introductory | [1-introductory/](1-introductory/) | 12 + 2 buffers | Scratch creations, turtle drawings and interactive art | My Interactive Art Show |
| 2 · Intermediate | [2-intermediate/](2-intermediate/) | 12 + 2 buffers | Games and small data-powered programs | Arcade Game or Art Studio |
| 3 · Advanced | [3-advanced/](3-advanced/) | 12 + 2 buffers | Larger programs that are easier to change | Build Something Big |

One 60-minute session a week, taught at home by a parent on a Mac, for up to
four children. Each level can also run in 10 weeks by merging two pairs of
weeks (see each Teacher Guide).

Every level folder has the same layout:

| Folder | Contents |
|---|---|
| `teaching-material/` | Teacher Guide, Lesson Plans, Student Workbook, Homework, Answer Key, Assessments, and `extras/` (cheat sheet, glossary, progress tracker, notes for families, certificate) |
| `exercises/weekNN/` | One folder per exercise: README, hints, starter, tests and `check_my_work.py` (Python), or a README checklist and a teacher-only `solution.md` (Scratch) |
| `project/` | The final project brief, its teacher guide, starter files and a teacher-only reference |

Build a level's PDFs with `make pdf LEVEL=1` (`2`, `3`) and a solution-free
student copy with `make student-bundle LEVEL=1`. Start with the level's
Teacher Guide (`teaching-material/teacher-guide.tex`).
