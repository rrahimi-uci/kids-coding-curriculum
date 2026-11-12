# Junior track scope and sequence (Grades 2–3)

> **Status:** Levels 1 and 3 are written (`active` in [`curriculum.json`](../curriculum.json)).
> Level 2 is planned: it will arrive in its own pull request and switch from
> `planned` to `active` when it is complete.

This is the single source of truth for **what the junior track teaches when**,
in the same way that [SYLLABUS.md](SYLLABUS.md) is for the main
(Grades 4–5) track. Every junior lesson, workbook page, exercise and
show-me checklist is written from this file.

## Who it is for and how it fits

* **Children:** Grades 2–3 (ages 7–9), up to four children, taught at home
  by a parent on a Mac. No prior experience is needed.
* **Shape:** 3 levels × **10 core weeks**, plus 2 optional buffer sessions
  per level. That is 30–36 sessions: about one school year at one session a
  week.
* **Pathway:** Junior Level 1 → Junior Level 2 → Junior Level 3 → main-track
  Level 1 (see [Next steps after the junior track](#next-steps-after-the-junior-track)).
* **Pacing options:**
  * *One school year:* all three levels, using buffers for holidays and
    "we need another week" moments.
  * *Two school years* (recommended when a child starts in early Grade 2):
    Grade 2 = Junior Levels 1 and 2 with both buffers; Grade 3 = Junior
    Level 3, then main-track Level 1.

### Why the junior track differs from the main track

The main track assumes Grade 4–5 reading, typing and math. A Grade 2–3 child is
still learning to read fluently, types slowly, and has not met angles in
degrees (US Grade 4), coordinates (Grade 5) or negative numbers (Grade 6).
The junior track therefore follows the rules below. They apply to every
junior document and are enforced by checks as the levels are written.

| Area | Junior rule |
|---|---|
| Session | **45 minutes** in Level 1, 45–60 in Levels 2–3. Five phases: **Warm-up** (video or unplugged, ≈10) → **Show me** (parent demo, ≈8) → **Make it** (build, ≈20, Driver/Helper swap every 5–7 minutes with a sand timer) → **Wiggle break** (≈2) → **Share** (≈5). Change activity at least every 10 minutes. |
| Reading | Student pages are **picture-first and read aloud by the parent**. About 250 words of student text per week; one short sentence per step; every Scratch step shows the block. Goals are "I can …" statements with an icon. Teacher pages stay at an adult reading level. |
| Math | Whole numbers to 100 (Levels 1–2) and to 1,000 (Level 3). Turns are named, not computed: **quarter turn = 90**, **half turn = 180**; other shapes use a turn card (triangle 120, hexagon 60) rather than 360 ÷ sides. **No typed x/y positions and no negative numbers**: sprites are dragged into place or use "go to random position" / "go to *sprite*". Graphs are picture and bar graphs (Grade 2–3 math). |
| Typing | Levels 1–2: only short words in "say" blocks and nicknames. Level 3 Python weeks: change numbers and color names in a program that already runs, and type at most one short new line per step. |
| Tools | Scratch 3 offline app (no account) with a **mouse**, not a trackpad. Thonny only in Level 3 weeks 6–9. An iPad with ScratchJr is a nice extra for Level 1 at home, never a requirement. No pytest, no `check_my_work.py`: Python work is checked by **matching a picture** of the expected result. |
| Homework | Optional **"Play at home" card**, 5–10 minutes, mostly unplugged, done with a grown-up. |
| Assessment | No quizzes or placement tests. **Show-me checklists** in weeks 5 and 10: the parent watches and ticks *Not yet / Getting there / Got it*. Level 1 week 1 has an ungraded "what do you like to make?" chat. |
| Pairs | **Driver** (mouse) and **Helper** (points and reads). With one child, the parent is the Helper. Siblings of different ages swap roles on the timer, not by age. |
| Videos | Rose & Pixi episodes of 2–3 minutes with one idea each, used as the warm-up. They carry most of the explaining, so a child does not have to read it. |

All other main-track principles stay: no accounts, offline, nicknames only,
color-blind-safe palette with icons and words, dyslexia-friendly edition,
unplugged activity and bug hunt every week, citizenship thread every week,
and a solution-free student copy.

### Conventions

* Concept tags: **I** = introduced, **R** = revisited, **E** = extended.
* Goal codes are `J<level>.G<n>` (for example `J2.G3`). Lesson objectives
  are phrased "The student can …" and end with their goal code, so
  `tools/coverage.py` can build the coverage tables as it does for the
  main track.
* CSTA codes refer to the CSTA K–12 Computer Science Standards (revised
  2017): band **1A** is grades K–2 and band **1B** is grades 3–5. AI ideas
  follow AI4K12's Five Big Ideas. The wording is abridged; verify against
  the official documents before formal use.
* Weekly rhythm in every level: weeks 1–4 new ideas, **week 5 play day +
  show-me checklist**, weeks 6–8 new ideas, **week 9 project studio**,
  **week 10 showcase + certificate**. B1 (unplugged) and B2 (free build and
  remix) are optional and can go anywhere after week 5.

---

## Level 1 — Little Robots (unplugged + Scratch)

**Tools:** Unplugged cards and a floor grid (masking tape on the floor);
Scratch 3 offline app with only the Motion, Looks, Sound, Events, Control
and Pen blocks. Optional: ScratchJr on an iPad for extra play at home.

### Level 1 goals

| Code | Goal: by the end of Level 1 the student can… | CSTA |
|---|---|---|
| J1.G1 | give and follow exact step-by-step instructions in the right order | 1A-AP-08, 1A-AP-11 |
| J1.G2 | build Scratch programs with sequences and repeat loops | 1A-AP-10 |
| J1.G3 | start code with simple events: green flag, click and key press | 1A-AP-10, 1B-AP-10 |
| J1.G4 | find and fix bugs in the order of steps and in loops | 1A-AP-14, 1A-CS-03 |
| J1.G5 | plan a short animated story on a storyboard and build it | 1A-AP-12 |
| J1.G6 | take turns as Driver and Helper and say what their code does | 1A-AP-15, 1B-AP-16 |
| J1.G7 | use a computer safely, kindly and fairly: nicknames, ask a grown-up, give credit, take breaks | 1A-IC-17, 1A-IC-18, 1A-NI-04, 1A-AP-13 |

### Level 1 weeks

| Wk | Title | Big idea | Concepts | Unplugged | Bug hunt | Citizenship thread |
|---|---|---|---|---|---|---|
| 1 | Robots Need Instructions | A program is a list of exact steps, in order. | sequence (I), algorithm (I) | “Parent robot”: guide the parent across a floor grid with arrow cards | An arrow card in the wrong place | Our rules: nicknames only, ask a grown-up when an app asks for anything |
| 2 | Meet Scratch | Blocks snap together to make a sprite act. | sprite, stage, green flag (I), say / move / sound blocks (I), sequence (R) | “Puppet show”: one child is the sprite, one reads out the script | Blocks that are not snapped together | Looking after the Mac and our bodies: sit up, mouse care, screen breaks |
| 3 | Bugs Are Clues | A bug is a clue: test, look, change one thing. | bug and debugging (I), test-and-change (I), wait (I), sequence (R) | “Spot the difference”: a robot routine that goes wrong | Steps in the wrong order; too fast to see (no wait) | Kind words when a friend finds a bug |
| 4 | Repeat It! | A repeat loop does the same steps again, so we don't have to. | repeat (I), costumes and animation (I), sequence (R) | “Dance loops”: perform a dance written with repeat cards | Too many or too few repeats | Sharing the mouse fairly: swap when the timer runs out |
| 5 | Play Day and Show Me | Practice everything, then show a grown-up what you can do. | sequence, repeat, debugging (R); show-me checklist | “Arrow maze” challenge cards | Bug-hunt relay: three broken projects | What makes a project fun for everyone? |
| 6 | When I Click… | Events start code: the flag, a click or a key. | when this sprite clicked (I), when key pressed (I), events (R), repeat (R) | “When I clap, you jump” game | Script under the wrong sprite; wrong key | Projects show nicknames, never real names or photos |
| 7 | Two Sprites Talk | Each sprite has its own script; wait makes them take turns. | several sprites (I), backdrops (I), wait and timing (R) | Act out a two-person conversation with timing cards | Both sprites talk at the same time | Giving credit: who made this picture or sound? |
| 8 | Draw With the Pen | The cat can draw: a square is repeat 4 of move and a quarter turn. | pen down / pen up (I), quarter turn = 90 (I), stamp (I), repeat (R) | Walk a square on the floor: steps, then a quarter turn | Turn outside the repeat, so only one side is drawn | Passwords are secret, like a toothbrush: never share them |
| 9 | Project Studio | Plan on a storyboard, then build one box at a time. | storyboard planning (I), all concepts (R) | Draw a three-box storyboard | Partner checks the project against the storyboard | Ask before you show someone else's work |
| 10 | Showcase and Certificate | Show, explain and celebrate. | explaining my code (R); show-me checklist | Gallery walk with sticker feedback | — (show-me checklist) | Showcase safety: family only, nicknames on screen |

**Level 1 final project — “My Animated Greeting Card”.** A Scratch card for
someone special, planned on a three-box storyboard. Must use: the green flag
to start, at least one repeat (an animation or dance), one click or key
event, a sound, and two sprites or a backdrop change. Core path: start from a
card with the backdrop and first sprite already in place. Stretch path: add a
pen-drawn border or pattern.

**Assessments:** week 1 “what do you like to make?” chat (ungraded); show-me
checklists in week 5 and week 10 (observed, never graded).

**Buffer B1 — Unplugged Games Day:** arrow mazes, color-by-number pixel grids
(numbers stand for colors, 1A-AP-09) and a debugging detective card game.
**Buffer B2 — Remix Studio:** pick a past project, change it and share it.

---

## Level 2 — Game Makers (Scratch)

**Tools:** Scratch 3 offline app with a mouse. All block categories are now
allowed except typed x/y positions; sprites are placed by dragging or with
“go to random position”.

### Level 2 goals

| Code | Goal: by the end of Level 2 the student can… | CSTA |
|---|---|---|
| J2.G1 | use forever and repeat loops to keep a game running | 1B-AP-10 |
| J2.G2 | use if-then with touching and key checks to make sprites react | 1B-AP-10 |
| J2.G3 | use a variable for score or lives, and random numbers for surprises | 1B-AP-09 |
| J2.G4 | split a game into parts with messages and My Blocks | 1B-AP-11, 1B-AP-12 |
| J2.G5 | test a game and find and fix bugs with a strategy | 1B-AP-15, 1B-CS-03 |
| J2.G6 | plan a game with a partner and improve it with players' feedback | 1B-AP-13, 1B-AP-16, 1B-AP-17, 1B-IC-20 |
| J2.G7 | make games that are fair, kind and easy for everyone to play, and give credit | 1B-AP-14, 1B-IC-19, 1B-IC-21 |

### Level 2 weeks

| Wk | Title | Big idea | Concepts | Unplugged | Bug hunt | Citizenship thread |
|---|---|---|---|---|---|---|
| 1 | Forever and Bounce | A forever loop keeps going until you press stop. | forever (I), if on edge, bounce (I), repeat (R), events (R) | “Forever freeze dance”: keep moving until the music stops | Blocks placed under a forever loop never run | Screen-time balance: stop when the timer says so |
| 2 | If Touching… | If-then lets a sprite check something and choose. | if-then (I), touching (I), forever (R) | “Simon says IF”: “If you have a sock on, jump!” | An if outside the forever loop only checks once | Kind feedback: two stars and a wish |
| 3 | Keep Score | A variable is a labeled box that remembers a number. | variables (I), set and change by 1 (I), show variable (I) | Paper boxes labeled Score and Lives that change during a game | Score does not go back to 0 when the flag is clicked | Fair scoring: everyone knows the rules |
| 4 | Surprise! Random | Random picks a number nobody can guess. | pick random 1 to 10 (I), go to random position (I), variables (R) | Dice race: roll and move | Random picked once before the loop, so it never changes | Being a good sport when you win or lose |
| 5 | Play Day and Show Me | Practice everything, then show a grown-up what you can do. | all concepts (R); show-me checklist | “Be the computer”: act out a script with if and score | Bug-hunt relay: three broken games | What did I get better at? |
| 6 | Messages | One sprite can tell the others when to start. | broadcast and when I receive (I), events (R) | Pass-the-note relay | Message sent but nobody is listening; wrong message name | Credit for sprites and sounds we did not make |
| 7 | My Own Blocks | Give a group of blocks a name and use it again. | My Blocks (I), decomposition (I), one number input (I, stretch) | Recipe cards: “make toast” as one named step | Block made but never used | Games for everyone: big text, colors plus shapes |
| 8 | Start, Win and Lose | A game needs a start, a goal and an ending. | game start / play / game over (I), lives (R), stop all (I) | Board-game rules: how do you win? how do you lose? | Game never ends, or ends right at the start | Games that do not trick players into “just one more” |
| 9 | Project Studio | Plan on a game card, build the core, then playtest. | game plan card (I), playtesting (I), all concepts (R) | Paper prototype played by a partner | Playtest bug list | Ask before you share a game |
| 10 | Arcade Showcase | Show, explain and celebrate. | explaining design choices (R); show-me checklist | Arcade gallery with sticker feedback | — (show-me checklist) | Showcase safety: family only |

**Level 2 final project — “My First Arcade Game”.** A catch game or a maze
game in Scratch, planned on a game plan card and playtested by someone else.
Must use: a forever loop, an if-touching check, a score or lives variable,
random, and a win or game-over ending. Core path: start from a template where
the player already moves with the arrow keys. Stretch path: a My Block or a
second level.

**Assessments:** short “show me” warm-up in week 1 to see what carried over
from Level 1 (ungraded); show-me checklists in week 5 and week 10.

**Buffer B1 — Secret Codes Day** (unplugged): picture codes, a letter-shift
wheel and logic puzzles. **Buffer B2 — Mini Game Jam:** a 90-second idea,
then free build.

---

## Level 3 — Bridge to Python (Scratch, then Python turtle)

**Tools:** Scratch 3 offline app (weeks 1–5); Thonny in simple mode with
Python's built-in `turtle` (weeks 6–9). Every Python starter already runs and
draws something; children change it.

### Level 3 goals

| Code | Goal: by the end of Level 3 the student can… | CSTA / other |
|---|---|---|
| J3.G1 | use a repeat inside a repeat and My Blocks to make patterns and art | 1B-AP-10, 1B-AP-11 |
| J3.G2 | plan a program on paper as parts and steps before building it | 1B-AP-11, 1B-AP-13 |
| J3.G3 | collect data, show it in a bar graph and say what it shows | 1B-DA-06, 1B-DA-07 |
| J3.G4 | explain that computers learn from examples and can learn unfair mistakes | AI4K12 Big Ideas 3 and 5 |
| J3.G5 | read and change short Python turtle programs: numbers, colors and repeat loops | 1B-AP-10, 1B-AP-12 |
| J3.G6 | test and debug in blocks and in text, including typos | 1B-AP-15 |
| J3.G7 | keep personal information private and give credit for others' work | 1B-NI-05, 1B-AP-14 |

### Level 3 weeks

| Wk | Title | Big idea | Concepts | Unplugged | Bug hunt | Citizenship thread |
|---|---|---|---|---|---|---|
| 1 | Patterns in Patterns | A repeat inside a repeat makes amazing art. | nested repeat (I), pen (R), My Blocks (R) | Clap patterns: repeat 3 of (clap, clap, stomp) | Inner repeat in the wrong place | My own pattern, not a copy |
| 2 | Plan It on Paper | Big programs are small parts, planned first. | decomposition (R), step list (I), test each part (I) | Plan a party in named parts | A part that works alone but not with the others | Teamwork: everyone gets a job |
| 3 | Data Detectives | Data is information we collect; a graph tells its story. | data (I), tally (I), bar graph (I), ask and answer (I) | Family survey: favorite fruit, tally marks and a paper bar graph | “Apple” and “apple” counted as different answers | Only ask what you need; never ask for personal information |
| 4 | How Do Computers Learn? | Computers learn patterns from examples, and copy our mistakes. | training examples (I), features (I), predictions (I), bias (I) | “Teach the robot”: a partner learns to sort animal cards from examples | Too few or one-sided examples lead to wrong guesses | AI can be wrong; never tell a chatbot personal information |
| 5 | Play Day: Blocks to Words | Every Scratch block has a word twin in Python. | all concepts (R), blocks-to-words card sort (I); show-me checklist | Match Scratch blocks to Python lines | Bug-hunt relay | What am I proud of so far? |
| 6 | Hello, Python! | Python uses words instead of blocks, and it is picky about spelling. | Thonny (I), Run (I), turtle forward and left (I), typos and error messages (I) | “Python is picky”: spot the difference cards | Typo hunt: `forwad`, missing `)` | Saving files with clear names |
| 7 | Repeat in Python | `for` plus an indent is Scratch's repeat block. | `for` with `range` (I), indentation (I), nested repeat (R) | “Indent the line-up”: stand inside or outside the loop | A line that is not indented runs only once | Asking for help well: what I expected, what happened |
| 8 | Colors and My Own Pattern | Change the numbers and colors to make it yours. | color names (I), pen size (I), changing a working program (R), `def` as a My Block (I, stretch) | Color-by-code cards | A color name spelled wrong | Credit: whose idea did I remix? |
| 9 | Project Studio | Choose a Scratch game or a Python picture; plan, build, test. | all concepts (R) | Plan card | Partner check against the plan | Can everyone see it? Colors and sizes for all |
| 10 | Graduation Showcase | Show, explain, celebrate and choose what is next. | explaining my code (R); show-me checklist | Gallery walk with sticker feedback | — (show-me checklist) | Next steps safely: what to do if a site asks for your name |

**Level 3 final project — “My Big Build”.** Choose: (a) a Scratch game or art
app that uses a nested repeat or a My Block plus a score or a counter, or (b) a
Python turtle postcard that starts from a working starter, uses a `for` loop,
at least two colors and one shape the student changed or added. Both are
planned on a plan card and checked by a partner. Core path: start from a
template. Stretch path: use `def` for a repeated shape.

**Assessments:** short “show me” warm-up in week 1 (ungraded); show-me
checklists in week 5 and week 10; a junior graduation certificate.

**Buffer B1 — Robot Olympics** (unplugged): sorting races and maze solving by
hand. **Buffer B2 — Free Build:** Scratch or Python, child's choice.

---

## Spiral map (how big ideas come back)

| Big idea | Level 1 | Level 2 | Level 3 | Main track |
|---|---|---|---|---|
| Sequence & algorithms | W1 I (unplugged), W2 R | W8 R (game states) | W2 E (planning in parts) | L1 W1, L2 W10 |
| Loops | W4 I (repeat), W8 R (pen) | W1 E (forever) | W1 E (nested), W7 R (`for`) | L1 W2, L1 W8 |
| Events | W2 I (green flag), W6 E (click, key) | W6 E (messages) | W6–8 R (Run) | L1 W3 |
| Conditionals | — | W2 I (if touching), W8 R | W4 R (sorting rules) | L1 W3, L1 W9 |
| Variables & data | B1 (numbers stand for colors) | W3 I (score), W4 I (random) | W3 E (survey data) | L1 W4, L2 W3 |
| Abstraction | W9 storyboard | W7 I (My Blocks) | W1 R, W8 `def` (stretch) | L1 W5, L1 W10 |
| Debugging | every week, W3 I | W5 relay, playtesting | W6 E (typos in text) | every week |
| AI | — | — | W4 I (unplugged) | L3 W9 |
| Citizenship | nicknames, breaks, credit, passwords | fairness, kindness, credit, accessibility | privacy, data, AI safety, credit | every week |

## Next steps after the junior track

A child who finishes Junior Level 3 is ready for main-track Level 1. Because
Scratch, events, loops, variables and a first look at Python are already
familiar, use main-track Level 1 weeks 1–5 as a quick review (two weeks per
session, or as homework) and teach weeks 6–12 in full. Main-track reading and
math assume Grade 4–5, so a child still in Grade 3 may need the parent to read
aloud and help with angles (the “Math helper” boxes) when they get there.

## How the levels will be built

Each level arrives in its own pull request, in this order:

1. Junior Level 1: lessons, workbook, play-at-home cards, show-me checklists,
   exercise folders, teacher guide and project. Switch `j1` to `active`.
2. Junior Level 2, then Level 3, in the same way.
3. Website: add the junior track to `site/manifest.yml` and the level pages.
4. Videos: 2–3 minute Rose & Pixi episodes for each junior week.
5. Junior quality checks: reading length, no typed x/y or negative numbers,
   no 360 ÷ sides, and the junior session phases.
