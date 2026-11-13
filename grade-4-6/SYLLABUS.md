# Grades 4–6 scope and sequence (master syllabus)

> The main track, for Grades 4–6 (ages 9–12). The Grades 2–3 track (Kids Coding Junior)
> has its own syllabus: [grade-2-3/SYLLABUS.md](../grade-2-3/SYLLABUS.md).

This is the single source of truth for **what is taught when**. Every lesson
plan, workbook chapter, homework set, exercise and assessment is written from
this file. If you change a week here, update the four weekly documents and the
coverage table in that level's Teacher Guide.

* 3 levels; **each level runs 10–12 weeks**: 12 core sessions (12-week plan),
  or 10 sessions when two pairs of weeks are merged (10-week plan; the merges
  are listed in each Teacher Guide). Holiday weeks without a session do not
  count. Each level also has 2 optional buffer sessions (B1, B2).
* 1 session = 60 minutes, once a week, at home, up to 4 students (2 pairs).
* Every session has the same shape: **Warm-up → Concept → Guided demo →
  Hands-on build → Wrap-up** (see [AUTHORING.md](../docs/AUTHORING.md)).
* Weekly rhythm inside a level: weeks 1–5 new content, **week 6 review +
  mid-level checkpoint**, weeks 7–9 new content, weeks 10–11 final project,
  **week 12 showcase + exit assessment**. B1/B2 are optional: use them only
  when there is room inside the 12 weeks (for example in a 10-week plan).
* Concept tags: **I** = introduced, **R** = revisited, **E** = extended.
* Goal codes (G1…) are per level; CSTA codes refer to the CSTA K-12 Computer
  Science Standards (revised 2017). See [STANDARDS.md](../docs/STANDARDS.md).

Objective IDs use `L<level>.W<week>.<n>` (e.g. `L1.W07.2`). Every objective is
phrased "The student can …". The objectives themselves are the numbered list at
the top of each lesson plan (with their goal codes); `tools/coverage.py` collects
them into the coverage table of each level's Teacher Guide, so this file lists
only the goals and the concepts per week.

---

## Level 1 — Introductory (Scratch → Python turtle)

**Tools:** Scratch 3 offline app (no account) for weeks 1–6; Thonny with
Python's built-in `turtle` for weeks 7–12.

### Level 1 goals

| Code | Goal: by the end of Level 1 the student can… | CSTA |
|---|---|---|
| L1.G1 | write precise step-by-step instructions (algorithms) and put them in the right order | 1B-AP-08, 1B-AP-10 |
| L1.G2 | use loops to repeat actions and make patterns | 1B-AP-10 |
| L1.G3 | use events and conditionals to make programs react | 1B-AP-10 |
| L1.G4 | use variables (score, size, answers) and random numbers | 1B-AP-09 |
| L1.G5 | break a problem into parts and make reusable blocks/functions | 1B-AP-11, 1B-AP-12 |
| L1.G6 | find and fix bugs using a strategy | 1B-AP-15, 1B-CS-03 |
| L1.G7 | work in a pair (driver/navigator) and explain their code | 1B-AP-16, 1B-AP-17, 1B-IC-20 |
| L1.G8 | stay safe and fair online: privacy, credit, kindness, accessible design | 1B-NI-05, 1B-AP-14, 1B-IC-21, 1B-IC-19 |
| L1.G9 | read and write simple text-based Python programs in Thonny | 1B-AP-10, 1B-AP-12 |

### Level 1 weeks

| Wk | Title | Big idea | Concepts | Unplugged | Bug hunt | Citizenship thread |
|---|---|---|---|---|---|---|
| 1 | Robots Need Instructions | A program is a list of exact steps in order. | sequence (I), algorithm (I), sprite/stage/green flag (I) | “Parent-robot drawing”: kids instruct the parent-robot to draw a simple picture | Steps in the wrong order | Class agreements; Scratch offline app, no accounts; use a nickname, never your real name/address in projects |
| 2 | Loop-de-Loop | Loops repeat steps so we don't have to. | repeat/forever (I), costumes/animation (I), pen extension (I), angles 360/n (I) | “Dance loops”: write a dance with repeat cards and perform it | Wrong turn angle in a shape | Screen-time balance: stretch break, 20-20-20 eyes rule |
| 3 | When This Happens… | Events start code; conditionals choose what happens. | events (I), if / if-else (I), touching/sensing (I), sequence (R), loops (R) | “Simon says IF”: conditional commands game | A sprite that never reacts (missing forever loop) | Kindness when giving feedback: “two stars and a wish” |
| 4 | Keeping Score | Variables are labeled boxes that remember things. | variables (I), random (I), conditionals (R), events (R) | “Label the boxes”: paper boxes for score/lives that change during a game | Score never resets / changes too fast | Credit & remix: whose art/sounds are we using? Use built-in library, give credit |
| 5 | Messages and My Blocks | Break big programs into named parts. | broadcast messages (I), My Blocks/custom blocks with inputs (I), decomposition (I), variables (R) | “Recipe cards”: split a party plan into named sub-recipes | Broadcast sent but nobody receives it | Accessibility: color-blind-safe colors + shapes, readable text size |
| 6 | Review Studio and Checkpoint | Show what you know; get ready for text code. | all Scratch concepts (R), Scratch→Python card sort (I) | “Blocks to words” card sort: match Scratch blocks to Python lines | Bug-hunt relay (3 broken Scratch projects) | Reflection: what makes a project fun and fair for everyone? |
| 7 | Hello, Python! | Text code is blocks written as words — and Python is picky. | Thonny (I), print (I), comments (I), turtle forward/left (I), syntax errors (I), sequence (R) | “Python is picky”: spot spelling/capital/parenthesis differences on cards | Typo hunt: `Print`, missing `)`, `forwad` | Saving files safely: where your work lives, sensible file names |
| 8 | Loops in Python | `for` loops + indentation = Scratch's repeat block. | for/range (I), indentation (I), loops (R), angles (R), nested loop (I, light), lists (I, light: looping over a color `PALETTE`) | “Indent the line-up”: kids stand in/out of a loop to show indentation | Indentation and off-by-one in range | Asking for help well: describe what you expected vs what happened |
| 9 | Variables, Input and Choices | Programs can ask questions, remember answers and decide. | variables (R→text), `input` + `int` (I), `if/elif/else` (R→text), comparison operators (I), color palette (I) | “Choose your path” story: walk an if/elif/else maze drawn on the floor | `input` gives text, not a number | Questions a program should NOT ask (personal info) |
| 10 | Random Art and My Own Commands | `random` makes surprises; `def` makes your own command (like My Blocks). | random (R→text), functions with `def` + parameters (I in Python, R from My Blocks), decomposition (R); final project kickoff (plan) | “Function machine”: input → rule → output cards | Function defined but never called | Being an original artist: remix with credit |
| 11 | Project Studio | Build, test and improve your project in small steps. | iterative development (I), all concepts (R/E) | Paper prototype + playtest feedback | Partner swap bug hunt | Giving and receiving helpful feedback |
| 12 | Showcase and Celebration | Share, explain, reflect. | explaining code (R), reflection | Gallery walk with feedback cards | — (exit assessment) | Showcase safety: share with family only, no personal info on screen |

**Level 1 final project — “My Interactive Art Show”** (Python turtle). The
program greets the viewer, asks 1–2 questions (`input`), and draws a scene or
pattern using at least: a loop, a variable, an `if`, `random`, and at least
one function made with `def`. Reference solution: *Night Sky Postcard* (asks
how many stars and day/night; draws sky, moon/sun, random stars, houses with a
`house(x, y, color)` function). Support path: Scratch version with the same
rubric. Extension path: add key presses (`onkey`).

**Assessments:** interest & comfort survey (week 1, not graded), mid-level
checkpoint (week 6: Scratch + unplugged), exit assessment (week 12: Python
reading/predicting/fixing + short build). Level 1 has no placement quiz (no
prior experience assumed).

**Buffer B1 — Unplugged Games Day:** pixel-art grids (binary/numbers to
pictures), algorithm relay race, debugging detective cards.
**Buffer B2 — Free-Build and Remix Studio:** choose a past exercise and remix
it; gallery share.

---

## Level 2 — Intermediate (Python)

**Tools:** Thonny, Python 3.10+ standard library only (`turtle`, `random`,
`time`, files). `pytest` (installed once via Thonny's package manager) from
week 8.

### Level 2 goals

| Code | Goal: by the end of Level 2 the student can… | CSTA |
|---|---|---|
| L2.G1 | use clearly named variables of different types (int, float, str, bool) and f-strings | 2-AP-11 |
| L2.G2 | combine control structures: while loops, nested loops, compound conditions | 2-AP-12 |
| L2.G3 | write functions with parameters and return values to organize code | 2-AP-14, 2-AP-13 |
| L2.G4 | store and process collections with lists and dictionaries | 2-AP-11, 3A-AP-14 |
| L2.G5 | read and write text files to save and load data | 2-DA-08 |
| L2.G6 | debug systematically (read tracebacks, print-debugging, rubber duck) and write simple tests | 2-AP-17, 2-AP-19 |
| L2.G7 | build event-driven games and generative art with turtle | 2-AP-12, 2-AP-16 |
| L2.G8 | plan with pseudocode/flowcharts, work in a team and act on feedback | 2-AP-10, 2-AP-15, 2-AP-18 |
| L2.G9 | make safe, fair, private choices about data and media | 2-NI-05, 2-NI-06, 2-IC-21, 2-IC-23 |

### Level 2 weeks

| Wk | Title | Big idea | Concepts | Unplugged | Bug hunt | Citizenship thread |
|---|---|---|---|---|---|---|
| 1 | Welcome Back, Python | Values have types; f-strings build messages. Placement quiz (15 min). | data types (I), f-strings (I), `input` (R), `if/elif/else` (R), `and/or/not` (I), starter-file structure: `return` preview and `if __name__ == "__main__":` (I, light) | “Type sorting”: sort value cards into int/float/str/bool bins | `"5" + 5` TypeError | Hero names, not real names: what is personal information? |
| 2 | Functions That Give Back | `return` hands a value back; parameters make functions flexible. | parameters (R), `return` (I), docstrings (I), scope (I, light) | “Function machines” with in/out cards and a mystery rule | Printing instead of returning | Writing comments for future-you and friends |
| 3 | Lists: Collections of Things | A list keeps many values in order. | lists, index, `append`, `len`, `for x in list` (I), `sorted()` and slicing `[:3]` (I, light), `random.choice` (R) | “Human list”: kids hold cards, index from 0 | IndexError / off-by-one | Color-blind-safe palettes: designing for everyone |
| 4 | While Loops and Game Loops | Repeat until something changes; games are loops. | `while` (I), `break` (I), input validation (I), nested loops for grids/pixel art (E) | “Guess my number” with higher/lower | Infinite loop that never ends | Fair play: games that don't trick or pressure players |
| 5 | Dictionaries and Secret Codes | Look things up by name, not number. | dict, keys/values, `.items()` (I), Caesar cipher (I), strings (R), `.lower()` and `.split()` (I, light) | Paper Caesar wheel: encode/decode messages | KeyError and wrong key spelling | Encryption & passwords: why secrets need protecting |
| 6 | Review and Checkpoint | Practice strategies for finding bugs. | debugging strategies (I): tracebacks, print-debugging, rubber duck; all (R) | “Debugging detectives” trace tables on paper | Bug-hunt workshop (5 stations) | Reflection on growth mindset |
| 7 | Files: Saving Your Stuff | Files let programs remember after they close. | `open`, `with`, read/write/append (I), `try/except FileNotFoundError` (I), strings `split` (R) and `strip` (I), lists (R) | “Notebook memory”: what does a program forget? | FileNotFoundError & overwriting with `"w"` | What should (not) be saved: data privacy |
| 8 | Testing: Prove It Works | Tests are automatic checks that catch bugs early. | `assert` (I), pytest (I), normal/edge test cases (I), functions (R) | “Test the toaster”: invent normal/edge tests for a gadget | Fix buggy functions using failing tests | Trust: why apps need testing (real-world bugs) |
| 9 | Event-Driven Games | Keys and timers make things happen; collisions end games. | `onkey`, `ontimer`, game state (I), `distance` collision (I), lists of sprites (E); final project kickoff | “Game loop board game”: each turn = one frame | Handler not called (missing `listen()`, function called with `()`) | Attribution for sounds/images; open licenses |
| 10 | Project Studio 1 | Plan, then build the core. Project milestone M1 = the pitch (week 9 homework) plus the plan (week 10). | pseudocode/flowchart (I), decomposition (R), all (R/E) | Paper prototype | Partner code review | Collaboration: splitting tasks fairly |
| 11 | Project Studio 2 | Test, playtest, polish. | tests for own functions (R), feedback (R) | Playtest feedback cards | Playtest bug list | Accessibility review of own game |
| 12 | Showcase and Celebration | Share, explain, reflect. | explaining design (R) | Gallery walk | — (exit assessment) | Showcase safety |

**Level 2 final project — “Arcade Game or Art Studio”.** Choose: (a) an
arcade game in turtle with keys + timer + score, or (b) a generative art
studio that saves/loads designs. Must use: functions with parameters/returns,
a list, a dictionary, a `while` or game loop/timer, a file (high scores or
saved art), and at least 3 pytest tests of their own functions. Reference
solution: *Star Catcher* (catch falling stars with a basket, dodge meteors;
lists of falling objects; settings dict; high scores saved to a text file;
tested logic module separate from drawing).

**Assessments:** placement quiz (start of week 1; covers Level 1 Python +
concepts), mid-level checkpoint (week 6), exit assessment (week 12).

**Buffer B1 — Cipher & Puzzle Day** (unplugged encryption, logic puzzles).
**Buffer B2 — Generative Art Jam** (free-build with lists/random/functions).

---

## Level 3 — Advanced (Python projects)

**Tools:** Thonny (or any editor), Terminal for `git` (Apple's free Command
Line Tools; no GitHub account), Python standard library only (`turtle`,
`csv`, `random`, `collections`, `json`), pytest.

### Level 3 goals

| Code | Goal: by the end of Level 3 the student can… | CSTA / other |
|---|---|---|
| L3.G1 | design programs with classes, objects, inheritance and composition | 3A-AP-17, 3A-AP-18 |
| L3.G2 | explain and compare searching/sorting algorithms and use recursion | 3A-AP-15, 1B-AP-08 (E), 3A-IC-26 |
| L3.G3 | choose data structures: lists of objects, dicts, stacks, queues, 2D grids | 3A-AP-14, 3A-DA-10 |
| L3.G4 | track their work with git (init, add, commit, log, diff, restore) | 3A-AP-22, 2-AP-19 |
| L3.G5 | plan and build a larger program iteratively, using feedback | 3A-AP-16, 3A-AP-19, 3A-AP-23, 2-AP-18 |
| L3.G6 | collect, clean, analyze and visualize data | 2-DA-08, 3A-DA-11, 3A-DA-12 |
| L3.G7 | explain how simple AI learns from data and where it fails | AI4K12 Big Ideas 1–5, 3A-IC-24 |
| L3.G8 | test and debug larger programs | 2-AP-17, 3A-AP-21 |
| L3.G9 | reason about privacy, bias, ethics and licenses | 3A-IC-24, 3A-IC-25, 3A-IC-29, 3A-AP-20 |

### Level 3 weeks

| Wk | Title | Big idea | Concepts | Unplugged | Bug hunt | Citizenship thread |
|---|---|---|---|---|---|---|
| 1 | Save Points: Git Basics | Git is a save-game system for code. Placement quiz (15 min). | git init/add/commit/log/diff/restore (I) and `git status` (I), Terminal basics (I), tuples (I, light), functions & lists (R) | “Save-point timeline” cards: commits as snapshots | Committed the wrong file / unhelpful message | Commit messages and history are public-ish: never commit secrets |
| 2 | Objects: Blueprints and Things | A class is a blueprint; objects are things built from it. | class, `__init__`, attributes, methods, `self` (I), dicts (R) | “Cookie-cutter classes”: blueprint vs cookies | Forgetting `self` | Designing virtual pets kindly (no manipulative mechanics) |
| 3 | Families of Objects | Share code with inheritance; build with composition. | inheritance, `super()`, overriding (I), polymorphism (I), composition (I) | “Family tree of game characters” | Overriding typo / missing `super().__init__` | Representation: diverse characters in games |
| 4 | Searching and How Fast Is Fast? | Smart algorithms do less work. | linear vs binary search (I), counting steps / growth (I), while loops (R) | Phone-book / guess-the-number halving game | Binary search off-by-one | Search engines and filter bubbles |
| 5 | Sorting, Stacks and Queues | Order data; stacks undo, queues take turns. | selection/bubble sort (I), `sorted(key=…)` (I), stack (I), queue/`deque` (I) | Human sorting race; plate stack; lunch queue | Sort that loses items / wrong comparison | Leaderboards: fairness & kindness |
| 6 | Review and Checkpoint | Connect the pieces. | OOP/algorithms (R), debugging with the Thonny debugger (I) | Algorithm match-up cards | Bug-hunt workshop | Growth mindset reflection |
| 7 | Grids, Recursion and Fractal Art | Functions that call themselves; worlds made of grids. | 2D lists (I), recursion (I), flood fill (I), breadth-first search with a queue (stretch, E), fractal trees (I), turtle (R) | Russian dolls / recursive drawing | Missing base case (RecursionError) | Credit for generative art & algorithms |
| 8 | Data Detectives | Data tells stories when you clean and chart it. | CSV reading (I), counting with dicts (R), averages (I), bar charts with turtle (I) | Class survey on paper (favorite games) → tally → chart | Numbers read as strings; empty rows | Consent & anonymizing survey data |
| 9 | How Do Machines Learn? | AI finds patterns in examples — and copies their mistakes. | training data (I), features (I), nearest-neighbor classifier with a “steps distance” (gap + gap, no Pythagoras) (I), Markov text generator (I), bias (I) | “Train the teacher”: classify mystery cards by features | Bad training data → bad predictions | AI ethics: privacy with chatbots, deepfakes, bias; final project kickoff |
| 10 | Project Studio 1 | Design first: classes, data, milestones. | class diagrams (I), decomposition (R), git workflow (R) | Paper class diagram (CRC cards) | Partner code review | Licenses of assets/libraries |
| 11 | Project Studio 2 | Test, playtest, polish, document. | tests (R), README docs (I), feedback (R) | Playtest feedback | Playtest bug triage | Accessibility & usability review |
| 12 | Showcase and Graduation | Share, explain, reflect, plan next steps. | presenting design decisions (R) | Gallery walk | — (exit assessment) | Showcase safety; next steps online safely |

**Level 3 final project — “Build Something Big”.** Choose: (a) a grid game,
(b) a generative art app, or (c) a data/AI app. Must use: at least 2 classes
(one using inheritance or composition), a data structure beyond a flat list
(dict, stack/queue or grid), one named algorithm (search/sort/recursion/BFS),
a saved file, at least 5 pytest tests, and a git history with 8+ meaningful
commits. Reference solution: *Maze Muncher* (grid maze loaded from text
files; Player, Ghost and Chaser classes; Chaser uses breadth-first search with
a queue; collectables and score; high scores saved; logic module fully tested
and separate from the turtle view). **Core path** for younger or slower
builders (added in the Grade 4–5 review): start from a starter template, add
one class of your own, reuse an algorithm from the weeks, save one file and
write fewer tests (the template's tests count toward the 5); the Full path
above is unchanged and the rubric is the same (6 criteria × 4 = 24).

**Assessments:** placement quiz (start of week 1; covers Level 2), mid-level
checkpoint (week 6), exit assessment (week 12).

**Buffer B1 — Algorithm Olympics** (unplugged sorting networks, maze
solving by hand). **Buffer B2 — Mini Game Jam** (90-second game ideas,
free-build, git commit practice).

---

## Spiral map (how big ideas come back)

| Big idea | Level 1 | Level 2 | Level 3 |
|---|---|---|---|
| Sequence & algorithms | W1 I (unplugged), W7 R (text) | W2 R (functions), W10 E (pseudocode) | W4–5 E (named algorithms, efficiency) |
| Loops | W2 I (Scratch), W8 R (for) | W4 E (while, nested), W9 E (game loop) | W4 R (search loops), W7 E (recursion as repetition) |
| Events & conditionals | W3 I, W9 R (if/elif) | W1 E (and/or), W9 E (onkey/ontimer) | W2–3 R (methods react), project E |
| Variables & data | W4 I, W9 R (input) | W1 E (types), W3 E (lists), W5 E (dicts), W7 E (files) | W2 E (attributes), W5 E (stacks/queues), W7 E (grids), W8 E (CSV data) |
| Abstraction / functions | W5 I (My Blocks), W10 R (def) | W2 E (return), W8 R (testable functions) | W2–3 E (classes), W10 E (modules) |
| Debugging & testing | every week (bug hunt), W6 relay | W6 E (strategies), W8 E (pytest) | W6 E (debugger), project E (5+ tests) |
| Collaboration | pair roles every week | W10 E (task split) | W1 E (git), W10 E (code review) |
| Art & games | W2 pen art, W4 catch game, W10 random art | W3 palettes, W4 pixel art, W9 games | W3 shape families, W7 fractals, project |
| Citizenship & AI ethics | privacy, credit, kindness, accessibility | data privacy, encryption, fair games, attribution | git secrets, consent, bias, AI ethics, licenses |
