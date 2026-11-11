# Level 2 Teaching Video Production Plan

> **Status:** Reviewed scripts and an automated regeneration contract for all 12 Level 2 lessons.
> Audience: Children in Grades 4–5 (ages 9–11) who are complete beginners. Every episode is at most 4:40 long (the limit is 5:00).
> This file is generated from `videos/specs/level2.json`; edit the JSON, then run `python -m videos.pipeline.cli plan --level 2`.

## 1. Instructional and creative direction

- **Series:** Kids Coding with Nova and Pixel
- **Audience:** Children in Grades 4–5 (ages 9–11) who are complete beginners
- **Frame:** 16:9, 1920×1080, 24 or 30 fps
- **Narration:** Warm, curious, inclusive, and clear at about 140–145 words per minute; friendly without sounding babyish
- **Visual language:** Bright modern 2D motion graphics, real Scratch or Thonny captures, deterministic code overlays, and a recurring mission map
- **Accessibility:** Closed captions (an MP4 caption track plus .srt and .vtt files), Okabe–Ito palette, high contrast, large readable type, no color-only clues, gentle motion, and no rapid flashing

### Recurring story world

Nova is an inventive ten-year-old coder. Pixel is a palm-sized helper robot who takes instructions very literally. Nova writes the code and Pixel runs it exactly as written, so when something goes wrong the two investigate together. Each week, the pair opens a new door in the Kids Coding workshop by learning one idea, testing it, and repairing one friendly bug. Learners are invited to predict before the answer appears.

### Five-part learning rhythm

Every episode follows the same reassuring rhythm: a surprising mission, one plain-language idea, a worked example, a friendly bug hunt, and a direct handoff to the lesson activity. The video launches hands-on learning; it does not replace it.

Bug hunts use the course's four detective steps: *What did I expect? What happened? Read one block (or line) at a time with your finger. Change one thing, then test again.*

### Production rules

- Keep the final runtime at or below 5:00, and each scene's narration within its own timing budget.
- Record at roughly 140 words per minute, with pauses after questions.
- Never show the answer to an exercise, homework, relay, exit ticket, card sort or the project reference; teach with a nearby example instead.
- Caption every spoken word. Never use color as the only clue.
- Render code, Scratch blocks, filenames, and UI labels as deterministic overlays—not inside generated artwork.
- Use the Okabe–Ito color palette, high contrast, readable type, gentle motion, and no rapid flashes.
- Show only nicknames and invented data. Never ask a child for a real name, address, school, password, or contact information.
- End with an age-appropriate practice prompt and normalize debugging as part of coding.
- Disclose synthetic narration on the end card, in the file metadata and in the video description.

## 2. Curriculum audit summary

The scripts were written from the Level 2 (Intermediate: Python in Thonny) syllabus, teacher guide, all 12 lesson plans, workbook and homework chapters, every exercise brief, starter and hint, and the final project materials, then checked line by line by a separate reviewer against the same sources and the answer keys.

Every code example shown or read aloud was run, and its output and error messages match what Python prints. Examples were chosen so that no video gives away the answer to an exercise, homework, exit ticket, checkpoint question or the project reference; the review replaced several examples that were too close.

Each script names the misconception it prevents, uses the level's own debugging routine and citizenship wording, and points learners to the lesson's first hands-on activity.

## 3. Episode scripts and storyboards

## Week 1: Every Value Has a Type

- **Driving question:** How do types and f-strings help us build friendly messages without errors?
- **Planned runtime:** 4:40 (280 seconds)
- **Vocabulary:** type, int, float, str (string), bool, f-string, TypeError, personal information
- **Misconception to prevent:** A number typed into input() is already a number, so text like "6" can be added to 5.
- **Digital citizenship:** Hero names, not real names: made-up names, colors and favorites are fine; real names, schools, addresses and birthdays are personal information, which we keep private. All our programs ask for a hero name or nickname instead. If any app or website asks for personal information, check with your teacher first.
- **Practice activity:** `2-intermediate/exercises/week01/ex-hero-card`

### Instructional objectives

- Sort values into the four types int, float, str and bool, and check a guess with type().
- Build a message with an f-string and turn typed text into a number with int().
- Combine conditions with and, or and not.
- Read a TypeError from the bottom line up and explain why text plus a number fails.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Welcome back to Kids Coding! It's Level 2, and Nova has built a Gem Counter for Pixel. ‘Type how many gems you found,’ says Nova. Pixel types 6. The program should add a bonus of 5. Instead… beep! Red text! Pixel did exactly what the code said. So why the crash? The secret: every value has a type! | Workshop with a glowing Level 2 door. Nova at a Thonny-style laptop; Pixel types 6 into a Shell panel. A gem counter shows 6 and a +5 bonus gem flies in, then bounces off. Red text slides up in the Shell; Pixel freezes with a question-mark face. **On screen:** MISSION: Fix the Gem Counter; 6 gems + 5 bonus = ? | Comic boing, not a failure buzzer. Keep the red text blurred here; it is read in scene 4. Do not show the Hero Card program or its crash. |
| 0:30–1:30 | **Explain the four types** | Python sorts every value into a type. The type tells Python what it's allowed to do with that value. Here are the four types we'll use most. An int is a whole number, like 7 or 100. A float is a decimal number, like 3.5. It always has a decimal point, so Python shows 2.0, not 2. A str, short for string, is text inside quotes, like "cat". And a bool is just True or False. Here's the big clue: quotes! 7 is a number, but "7" is text. Think of a number as a LEGO brick. 5 plus 5 clicks together to make 10. Text is a sticker with a 5 printed on it. You can't click a sticker onto a brick. | Four labeled bins slide in: int (whole number), float (decimal number), str (text in quotes), bool (True or False). Value cards 7, 100, 3.5, 2.0, "cat", True drop into the right bins. The card "7" wobbles over the int bin, then lands in str as quote marks glow. Two LEGO bricks labeled 5 click into a 10 brick; a sticker labeled "5" bounces off a brick. **On screen:** int • float • str • bool; Quotes make text: "7" is a str; A float has a decimal point: 2.0 | Each bin has a word label and an icon, never color alone. Use the course's own bin labels. Do not sort the exact unplugged value-card set or the homework Type detective values (42, "42", 4.2, False, "False", -8). |
| 1:30–2:35 | **Worked example in the Shell** | Let's try it in the Thonny Shell, after the three arrows. Predict first! type of 2.5? Python says float. And type of "2.5", in quotes? str! The quotes make it text. Now let's build a message. Nova types robot equals "Pixel", and wheels equals 3. Then an f-string. The f in front means fill in. Python fills each pair of curly braces with the value inside. Out comes: Pixel rolls on 3 wheels. No worries about text plus a number! Last, smarter choices. And is True when both sides are true. Or needs at least one. Not gives the opposite. So: wheels is more than or equal to 2, and robot equals "Pixel". Pause and predict… True! | Shell panel with >>> prompts. Lines type in one at a time with a prediction pause before each answer: type(2.5) → <class 'float'>; type("2.5") → <class 'str'>. Two value boxes appear: robot = "Pixel" and wheels = 3. The f-string's curly braces open like little doors and the values slide in, giving 'Pixel rolls on 3 wheels'. Then a two-sided and-switch lights both sides and shows True. **On screen:** type("2.5")  →  <class 'str'>; f"{robot} rolls on {wheels} wheels"; wheels >= 2 and robot == "Pixel"; and: both • or: one • not: opposite | Real Shell echoes: type(2.5) gives <class 'float'>, type("2.5") gives <class 'str'>, the f-string gives 'Pixel rolls on 3 wheels', and wheels >= 2 and robot == "Pixel" gives True. Do not use the lesson's name/level f-string, the Mood Meter moods, the Dragon Door key-and-level rule, or the checkpoint's "{hero} has {stars * 2} stars" f-string. |
| 2:35–3:40 | **Friendly bug hunt: text plus a number** | Back to the Gem Counter. Here's Nova's code. gems equals input, How many gems? Then print gems plus 5. Pixel typed 6. Let's be detectives. First, read the red error from the bottom line up. The last line says WHAT went wrong: TypeError: can only concatenate str, not int, to str. Concatenate means glue together. Python can glue text to text, but not text to a number. But gems is 6… isn't it? Let's check. Nova adds print, type of gems, just above the crash line. Pixel runs it: class str! Input always gives back text, even when you type digits. So which tool turns text into a whole number? Pause and point. Yes, int! print, int of gems, plus 5. Run again: 11. ‘Bonus collected!’ beeps Pixel. | Code panel shows the two lines; Pixel types 6 in the Shell. The traceback appears and a pointer starts at the last line, which zooms in. A glue bottle tries to stick a text tile "6" to a number brick 5 and fails. A print(type(gems)) line slides in above the crash line; the Shell shows <class 'str'>. int( ) wraps gems, the tile turns into a brick, and the Shell shows 11. **On screen:** gems = input("How many gems? "); print(gems + 5); TypeError: can only concatenate str…; print(int(gems) + 5)  →  11 | Real wording: TypeError: can only concatenate str (not "int") to str. Four-second pause before the reveal. Never show the Hero Card program, its fixes, or the coins exit ticket. |
| 3:40–4:40 | **Recap, hero names, and handoff** | Level 2, door one: open! Let's remember. Every value has a type: int, float, str or bool. Quotes make text. An f-string fills curly braces with values. And input always gives back text, so int turns it into a number. One more thing. In our programs, you always type a made-up hero name or nickname. Your real name, school, address and birthday are personal information. Keep them private. If an app or website asks for them, check with your teacher first. Now open Exercise 1.1, Hero Card. Press Run, type a made-up hero, and read the red error from the bottom up. TODO 1 has two parts, and you need both. Have fun, hero! | Door 1 on the mission map opens. Four type icons line up as a recap. A safe card reads 'Hero name: StarCoder'; cards labeled real name, school, address and birthday get a lock icon. The Hero Card activity card slides in. **On screen:** int • float • str • bool • f"…"; Hero names, not real names; NEXT: Exercise 1.1 Hero Card | Use category labels only, no realistic personal data. Five-second clean hold at the end and the AI-voice disclosure on the end card. |

**Lesson handoff:** Open Exercise 1.1 Hero Card and press Run. Type a made-up hero name, a power and a level, then read the TypeError from the bottom up. Do TODO 1 (both parts: part 1 turns the level into a number with int(), part 2 rewrites the Next level line as an f-string), then TODO 2 to 5: the power, power points, health and Legend? lines with f-strings. Run after each one.

**Curriculum evidence:**

- `2-intermediate/teaching-material/lessons/week01.tex`
- `2-intermediate/teaching-material/workbook/week01.tex`
- `2-intermediate/teaching-material/homework/week01.tex`
- `2-intermediate/exercises/week01/ex-hero-card/README.md`
- `2-intermediate/exercises/week01/ex-hero-card/starter.py`
- `2-intermediate/exercises/week01/ex-hero-card/hints.md`
- `2-intermediate/exercises/week01/ex-mood-meter/README.md`
- `2-intermediate/exercises/week01/ex-mood-meter/starter.py`
- `2-intermediate/exercises/week01/ex-mood-meter/hints.md`
- `docs/SYLLABUS.md`

## Week 2: Functions That Give Back

- **Driving question:** What is the difference between printing an answer and returning it?
- **Planned runtime:** 4:40 (280 seconds)
- **Vocabulary:** parameter, argument, return, None, docstring, scope
- **Misconception to prevent:** If a function prints the right number, it has handed that number back, so the program can store it or do math with it.
- **Digital citizenship:** Comments for future-you and friends: comments explain why, they are always kind (no jokes about people), and they never contain personal information. If an idea came from a friend or a book, a comment can say so: that is giving credit.
- **Practice activity:** `2-intermediate/exercises/week02/ex-game-math`

### Instructional objectives

- Explain the difference between printing an answer and returning it.
- Write a function with parameters that returns an answer, and use the returned value in a new calculation.
- Write a docstring that says what a function gives back.
- Explain why a variable made inside a function is not visible outside it.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Pixel has opened a snack shop! Nova built a function to count the cookies. ‘How many cookies are in 3 boxes?’ asks Nova. The function shouts, ‘18!’ Great. Now Nova adds 2 more cookies… and the program crashes with a strange word: None. The function knew the answer. So why couldn't the program use it? Let's find out! | Pixel behind a snack-shop counter with three cookie boxes. A function-machine box labeled cookies_in shouts a speech bubble '18'. Nova adds two cookies to a tray; a 'None' cloud puffs up and the cookies fall through it. **On screen:** MISSION: Count the cookies; Why does it say None? | Gentle comedic beat. Do not show the Game Math starter or its xp_needed output. |
| 0:30–1:30 | **Explain parameters, arguments and return** | A function is like a machine. Values go in, the machine works on them, and an answer comes back out. The values you hand in are called arguments. Inside the function, they land in parameters, which are like labeled slots. And the word return hands the answer back to whoever called the function. Here's the big idea. Printing is like shouting the answer out of a window. Everyone hears it, but nobody can keep it. Returning is like putting the answer in your friend's hand. Now they can put it in their pocket, a variable, or add it to something else. A function that only prints quietly hands back None. That's Python's word for nothing. | Function machine diagram: IN (arguments) → FUNCTION (labeled parameter slots) → OUT (return). Number cards drop into slots and an answer card slides out of the return chute. Split screen: Nova shouts '8!' out of a window and the number floats away; then Nova places an '8' card in Pixel's hand and Pixel tucks it into a pocket labeled variable. A function that only prints hands Pixel an empty card labeled None. **On screen:** IN → function → OUT; print = shout it; return = hand it over; None = nothing came back | Use the lesson's 'shouting versus handing over' analogy. Do not use the lesson's double_print / double_return demo, damage(), xp_needed() or triple(). |
| 1:30–2:35 | **Worked example: a function that returns** | Pixel collects stickers: 10 on every sheet, plus some loose ones. Nova types def stickers, with two parameters: sheets and loose. Right under the def line goes a docstring, a sentence in triple quotes. It says: Return how many stickers in all. It's a note for future-you and your friends. Then: return sheets times 10, plus loose. Let's call it. album equals stickers of 2 and 3. The 2 goes into sheets and the 3 goes into loose, in the same order. What comes back? 23! Because the answer was returned, we can do math with it. stickers of 2 and 3, plus stickers of 1 and 5. Pause and predict… 38! And remember: a variable made inside a function stays inside it, like bowls in a restaurant kitchen. Diners only see the plate that comes out. | Code panel types the function line by line; the docstring glows as a sticky note. Arguments 2 and 3 slide into parameter slots labeled sheets and loose. Two full sticker sheets of 10 and 3 loose stickers appear, and a value box album shows 23. Next, 1 sheet and 5 loose stickers appear, and the answers 23 and 15 combine into 38. A kitchen cutaway shows bowls staying behind a wall while a plate slides out. **On screen:** def stickers(sheets, loose):; """Return how many stickers in all."""; return sheets * 10 + loose; stickers(2, 3) + stickers(1, 5)  →  38 | Code exactly: def stickers(sheets, loose): / """Return how many stickers in all.""" / return sheets * 10 + loose; album = stickers(2, 3) gives 23; stickers(2, 3) + stickers(1, 5) gives 38. Do not show any Game Math, Flower Garden or Potion Shop function or its answers, and never the checkpoint's area(width, height) function or a multiply-two-parameters example like it. |
| 2:35–3:40 | **Friendly bug hunt: printing instead of returning** | Back to the snack shop. Here's Nova's function: def cookies in, with the parameter boxes. Inside: print boxes times 6. Then total equals cookies in of 3, plus 2. Pixel runs it, exactly as written. First, 18 appears on its own line. Then red text! Read it from the bottom line up: TypeError, unsupported operand types for plus: NoneType and int. NoneType? That's our clue word: None. So ask: which function gave back None? Does it have a return line? Pause and point. Right! cookies in only prints. It shouts 18 out of the window, then hands back nothing. And None plus 2 can't work. The fix: change print to return. Run again. No extra line, and total is 20. ‘20 cookies, in my hand!’ beeps Pixel. | Code panel with the function and the call. The Shell shows 18 alone on a line, then the red traceback; the last line zooms and the word NoneType gets a magnifying glass. A detective card asks: Which function gave back None? Does it have a return line? The print word flips into return, the rerun shows a value box total = 20, and Pixel holds a tray of 20 cookies. **On screen:** print(boxes * 6); 'NoneType' and 'int'; Clue word: None; return boxes * 6 | Real wording: TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'. Pause four seconds before the reveal. Never show xp_needed(), the triple() exit ticket, or the Potion Shop functions. |
| 3:40–4:40 | **Recap, kind comments, and handoff** | Door two is open! Let's remember. Parameters are labeled slots. Arguments fill them, in order. Return hands the answer back, so we can store it or do math with it. If you see None where a number should be, a function probably printed instead of returning. And a docstring tells everyone what a function gives back. Speaking of notes: comments are for future-you and your friends. Good comments explain why. They're always kind, with no jokes about people, and they never hold personal information. If an idea came from a friend or a book, say so. That's giving credit. Now open Exercise 2.1, Game Math. Press Run, find the word None, and track down which function caused it. Happy building! | Door 2 opens on the mission map. Recap cards: slots, return arrow, None warning. A comment bubble reads '# why: shields block some damage' next to a heart icon and a 'credit: idea from Sam' tag. The Game Math activity card slides in. **On screen:** Return it, don't just print it; Comments: why • kind • private; NEXT: Exercise 2.1 Game Math | End card includes the AI-voice disclosure and a five-second hold. |

**Lesson handoff:** Open Exercise 2.1 Game Math and press Run. Find the word None in the output and say which function caused it, then fix it (TODO 1: xp_needed() prints instead of handing its answer back). Then finish damage() so it is never less than 0 and hands result back (TODO 2 and 3), finish is_critical() (TODO 4) and remove the # from the two health lines (TODO 5). Predict each answer before you run.

**Curriculum evidence:**

- `2-intermediate/teaching-material/lessons/week02.tex`
- `2-intermediate/teaching-material/workbook/week02.tex`
- `2-intermediate/teaching-material/homework/week02.tex`
- `2-intermediate/exercises/week02/ex-game-math/README.md`
- `2-intermediate/exercises/week02/ex-game-math/starter.py`
- `2-intermediate/exercises/week02/ex-game-math/hints.md`
- `2-intermediate/exercises/week02/ex-flower-garden/README.md`
- `2-intermediate/exercises/week02/ex-flower-garden/starter.py`
- `2-intermediate/exercises/week02/ex-flower-garden/hints.md`
- `docs/SYLLABUS.md`

## Week 3: Lists: Collections of Things

- **Driving question:** How can one variable keep many values in order, and why is the first one number 0?
- **Planned runtime:** 4:35 (275 seconds)
- **Vocabulary:** list, item, index, append, len, IndexError, off-by-one, accessible
- **Misconception to prevent:** The first item in a list is number 1, so a list of three items has an item at index 3.
- **Digital citizenship:** Color-blind-safe palettes, designing for everyone: use the Okabe-Ito colors and add a label, number, shape or pattern, so color is never the only clue.
- **Practice activity:** `2-intermediate/exercises/week03/ex-palette-stripes`

### Instructional objectives

- Make a list, add to it with append and count it with len.
- Get an item by its index, starting from 0, and explain what an IndexError means.
- Loop over a list with for item in a list and with for i in range(len(...)).
- Choose color-blind-safe colors and add labels so color is never the only clue.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Nova and Pixel are planning a tour of the planets. ‘Mercury, Venus, Earth…’ says Nova. Should each planet get its own variable? planet1, planet2, planet3… and more keep coming! Pixel is juggling boxes. Is there one box that can hold many things, in order? Yes! It's called a list. Let's pack! | Nova points at a star map. Pixel juggles separate variable boxes labeled planet1, planet2, planet3, planet4, which wobble and drop. Then one long row of connected boxes slides in and catches them in order. **On screen:** MISSION: Plan a planet tour; One box for many things? | Playful juggling; no crash sound. Planet names are spelled correctly and capitalized. |
| 0:30–1:25 | **Explain lists, index, append and len** | So far, each variable held one value. A list holds many values in order. We write it inside square brackets, with commas between the items. Think of a row of lockers. Each locker has a number painted on it, called its index. And here's the surprise: the first locker is number 0! So in a list of four lockers, the numbers go 0, 1, 2, 3. To add an item, append puts it at the end. To count the items, len tells you how many. And what if you ask for a locker that doesn't exist? Python stops with an IndexError. That means: list index out of range. | A hallway of four lockers with index numbers 0, 1, 2, 3 painted on the doors. A fifth locker slides onto the end for append. A counter labeled len ticks up to 5. A dashed, empty locker outline appears past the end with an IndexError sign on it. **On screen:** [ ] square brackets, commas between; The first index is 0; append adds to the end; len counts the items | Use the lesson's lockers analogy. Number labels sit on every locker so position never relies on color. Do not use the lesson's backpack list (lantern, rope, map, apple). |
| 1:25–2:30 | **Worked example: build and loop over a list** | Let's plan Pixel's tour in the Thonny Shell. Predict each answer before Pixel runs it! Nova types planets equals, square bracket, "Mercury", "Venus", "Earth". Now: planets dot append "Mars". Mars joins at the end. What's len of planets? Pause and count… four! Now let's visit every item. for planet in planets, colon, print planet. The loop visits each item in order: Mercury, Venus, Earth, Mars. But what if we also want the locker number? Use for i in range of len of planets. len is 4, so i goes 0, 1, 2, 3. Print i and planets of i. The Shell shows 0 Mercury, 1 Venus, 2 Earth, 3 Mars. See? The first one is number 0. | Code panel types each line. A list row of 3 boxes with index numbers 0–2 underneath grows to 4 boxes (index 3: Mars) on append. A len counter shows 4. A spotlight walks along the boxes for the first loop while the Shell prints each name. For the second loop, a value box i changes 0, 1, 2, 3 as the spotlight moves and the Shell prints '0 Mercury' through '3 Mars'. **On screen:** planets.append("Mars"); for planet in planets:; for i in range(len(planets)):;     print(i, planets[i]) | Code is valid Python 3.10: planets = ["Mercury", "Venus", "Earth"]; planets.append("Mars"); len(planets) is 4; the index loop prints 0 Mercury, 1 Venus, 2 Earth, 3 Mars. Do not draw stripes, colors or any Palette Stripes code, and do not show the index -1. |
| 2:30–3:35 | **Friendly bug hunt: off-by-one IndexError** | Bug hunt! Nova starts a new list with just three planets: Mercury, Venus and Earth. ‘Earth is the third planet, so it's number 3,’ says Nova, and types print planets of 3. Pixel runs it, exactly as written. Red text! Read it from the bottom up: IndexError: list index out of range. Let's be detectives. Draw the lockers on paper, with the index numbers underneath. Mercury is 0. Venus is 1. Earth is 2. There's no locker 3! This is called an off-by-one bug: a number that's one too big or one too small. It's one of the most common bugs in all of programming. So which index is Earth? Pause and point. Yes, 2! Nova changes the 3 to a 2. Run again: Earth! | Code panel shows a three-item list and print(planets[3]). The traceback appears; its last line zooms. A pencil sketch draws three boxes with 0, 1, 2 underneath and a dashed empty box at 3 with a question mark. The 3 in the code flips to 2 and the Shell prints Earth. **On screen:** print(planets[3]); IndexError: list index out of range; Draw the boxes: 0 • 1 • 2; Off-by-one: one too big | Four-second prediction pause before the reveal. Never show the Adventure Inventory last_item() line or any fix for it, the exit-ticket pets list, or the High Scores code. |
| 3:35–4:35 | **Recap, colors for everyone, and handoff** | Door three is open! Let's remember. A list keeps many values in order, inside square brackets. Each item has an index, and the first index is 0. Append adds to the end, and len counts the items. Now, a design rule. Some people see colors differently, often red and green. So we use the Okabe-Ito colors, which stay different for almost everyone. And we add a label, number, shape or pattern, so color is never the only clue. Now open Exercise 3.1, Palette Stripes. Press Run: only one stripe! Append two colors, then use a loop to draw a labeled stripe for every color. Notice: the first stripe is number 0. Have fun! | Door 3 opens. Recap icons: brackets, index 0 badge, append arrow, len counter. Eight Okabe-Ito swatches appear, each with its name; a red-versus-green danger sign gains a warning-triangle shape and the word DANGER, a safe sign gains a check shape and the word SAFE. The Palette Stripes card slides in. **On screen:** List • index from 0 • append • len; Color is never the only clue; NEXT: Exercise 3.1 Palette Stripes | Every swatch carries a text label. AI-voice disclosure on the end card and a five-second hold. |

**Lesson handoff:** Open Exercise 3.1 Palette Stripes and press Run: only one stripe appears. Use palette.append(...) to add blue and vermillion (TODO 1), loop with for i in range(len(colors)): to draw one stripe for every color with the label str(i) and move x along (TODO 3), then print the first and last color (TODO 4). Next comes Exercise 3.2 Adventure Inventory, which starts with this week's IndexError bug hunt.

**Curriculum evidence:**

- `2-intermediate/teaching-material/lessons/week03.tex`
- `2-intermediate/teaching-material/workbook/week03.tex`
- `2-intermediate/teaching-material/homework/week03.tex`
- `2-intermediate/exercises/week03/ex-palette-stripes/README.md`
- `2-intermediate/exercises/week03/ex-palette-stripes/starter.py`
- `2-intermediate/exercises/week03/ex-palette-stripes/hints.md`
- `2-intermediate/exercises/week03/ex-inventory/README.md`
- `2-intermediate/exercises/week03/ex-inventory/starter.py`
- `2-intermediate/exercises/week03/ex-inventory/hints.md`
- `2-intermediate/exercises/week03/ex-high-scores/README.md`
- `2-intermediate/exercises/week03/ex-high-scores/starter.py`
- `2-intermediate/exercises/week03/ex-high-scores/hints.md`
- `docs/SYLLABUS.md`

## Week 4: While Loops and Game Loops

- **Driving question:** How can a loop keep going until something changes, and how do we stop one that never ends?
- **Planned runtime:** 4:40 (280 seconds)
- **Vocabulary:** while loop, condition, infinite loop, break, input validation, game loop
- **Misconception to prevent:** A while loop stops by itself after a while, even if nothing inside it changes the condition.
- **Digital citizenship:** Fair play: the rules are honest, the player can stop any time, and nobody is pressured. No timers that pressure you to buy, no untrue 'only 1 left!' messages, no rewards that make you feel you must come back every day, and no nagging to spend money.
- **Practice activity:** `2-intermediate/exercises/week04/ex-guess-number`

### Instructional objectives

- Write a while loop that stops because a variable changes inside it.
- Use while True with break to leave a loop when the job is done.
- Find and fix an infinite loop by asking what is checked and what changes inside the loop.
- Explain what makes a game fair and name one trick a game should not play on its players.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Pixel is playing Guess My Number! Nova thinks of a secret number from 1 to 20. ‘Is it 10?’ asks Pixel. ‘Higher!’ ‘15?’ ‘Lower!’ How many guesses will it take? Three? Seven? Nobody knows! A for loop needs to know how many times to go around. So what kind of loop keeps going until the game is won? | Nova holds a face-down card with a secret number. Pixel's guesses pop up as bubbles with Higher and Lower arrows beside them. A tally counter clicks with each guess and a big question mark spins over the words 'How many times?'. **On screen:** MISSION: Loop until we win; How many guesses? Nobody knows! | Keep the secret number hidden; this mirrors the unplugged warm-up, not the exercise code. |
| 0:30–1:30 | **Explain while loops and infinite loops** | A for loop knows in advance how many times to go around. for i in range 4 is always four times. A while loop is different. It keeps going around while something is true, and it checks again at the top every time. That check is called the condition. Think of a car trip. ‘Are we there yet?’ While we're not there: drive a bit, then ask again. It works because the car moves. But if the car stays parked, you can ask forever, and the answer never changes. That's an infinite loop: a loop that never stops, because nothing changes the condition. If it happens, press Thonny's red Stop button. Every programmer does it! | Flowchart: a diamond 'condition True?' with a yes arrow into a loop body and a back arrow to the check, and a no arrow out of the loop. A car drives along a road, asking 'Are we there yet?' at each signpost until it reaches the finish flag. Then the car sits parked and the same speech bubble repeats forever, until a red Stop button is pressed. **On screen:** for: knows how many times; while: repeats while True; Nothing changes → infinite loop; Stuck? Press the red Stop button | Use the lesson's car-journey analogy. The Stop button should match Thonny's real red stop sign. Do not use the lesson's countdown (n = 3) or the energy exit ticket. |
| 1:30–2:35 | **Worked example: while, then while True with break** | Pixel is jumping up to a cloud that's 10 steps high. Nova writes height equals 0. Then: while height is less than 10, colon. Inside: height equals height plus 3, then print height. That middle line is the change that lets the loop end. Let's trace it. 0 is less than 10, so jump: 3. Check again. Jump: 6. Then 9. Is 9 less than 10? Yes! Jump: 12. Now the check is False, and the loop stops. Here's another pattern. while True goes around forever, on purpose. Then break jumps out of the loop, right away, when we say so. We put break inside an if. Games use this to keep asking until the player types a good answer. That's called input validation. | Code panel types the loop. Pixel hops up a ladder of steps 0 to 12 toward a cloud at 10; a value box labeled height changes 0 → 3 → 6 → 9 → 12, and the Shell prints 3, 6, 9, 12. At each hop the condition 'height < 10' lights True; at 12 it lights False and Pixel lands on the cloud. Then a second panel shows a loop arrow labeled while True with an emergency-exit door labeled break, opened only by an if-key. **On screen:** while height < 10:;     height = height + 3; while True:  …  break; Input validation: ask again | Code exactly: height = 0 / while height < 10: / height = height + 3 / print(height); output 3, 6, 9, 12. Show while True and break only as a diagram, not as an input-checking program: never show any Guess My Number or Slime Battle code or its fixes. |
| 2:35–3:40 | **Friendly bug hunt: the loop that never ends** | Bug hunt! Nova writes a cookie muncher for Pixel. cookies equals 3. While cookies is more than 0, print Munch! Then: cookies equals cookies minus 1. Pixel runs it… Munch! Munch! Munch! Munch! It never stops! Press Stop. Now, two detective questions find almost every infinite loop. One: what is checked? cookies is more than 0. Two: what changes inside the loop, so that check can change? Look closely at the spaces. The minus-one line has no indent! So it's outside the loop. It would only run after the loop ends, and the loop never ends. Indentation decides what's inside. So what's the fix? Pause and point. Push that line in, under print. Run: three munches, then done! | Code panel: the last line sits at the left edge with no indent. The Shell fills with Munch! lines scrolling fast while a cookie counter stays stuck at 3; Pixel's jaw keeps chomping. A red Stop button is pressed. Two detective cards appear: 'What is checked?' and 'What changes inside the loop?'. Indentation guides show the last line outside the loop box. The line slides right four spaces, the counter goes 3 → 2 → 1 → 0, and the Shell shows exactly three Munch! lines. **On screen:** while cookies > 0:; cookies = cookies - 1  ← no indent!; 1 What is checked?; 2 What changes inside the loop? | Gentle motion for the scrolling Shell; no flashing. Never show the Guess My Number game loop, the Slime Battle hits_needed() loop, or the week 6 Rocket Countdown. |
| 3:40–4:40 | **Recap, fair play, and handoff** | Door four is open! Let's remember. A while loop repeats while its condition is True. Something inside must change, or it's an infinite loop. Then press Stop and ask: what is checked, and what changes? while True with break jumps out when we say so. Now, could we make a guessing game cheat? Sure! But would it be fun? Our class rule for games: the rules are honest, the player can stop any time, and nobody is pressured. No fake only-one-left messages, and no nagging to spend money. Now open Exercise 4.1, Guess My Number. Play until you win. Does it stop? If not, press Stop and work out why. Then be the tester: try typing banana! Good luck! | Door 4 opens. Recap icons: loop arrow, condition diamond, Stop button, break door. A fair-play checklist ticks: honest rules, stop any time, no pressure; a fake 'Only 1 left!' banner and a countdown-to-buy timer get crossed out. The Guess My Number card slides in. **On screen:** Something must change inside; Honest • stop any time • no pressure; NEXT: Exercise 4.1 Guess My Number | AI-voice disclosure on the end card and a five-second hold. |

**Lesson handoff:** Open Exercise 4.1 Guess My Number and press Run. Guess until you are right; when it keeps asking, press the red Stop button and say why. Then add 1 to tries every time through the loop (TODO 1), break out of the loop when the result is "Correct" (TODO 3), and make ask_number() keep asking until the answer is a whole number from low to high (TODO 2). Be the tester: try banana, 99, 0 and -3.

**Curriculum evidence:**

- `2-intermediate/teaching-material/lessons/week04.tex`
- `2-intermediate/teaching-material/workbook/week04.tex`
- `2-intermediate/teaching-material/homework/week04.tex`
- `2-intermediate/exercises/week04/ex-guess-number/README.md`
- `2-intermediate/exercises/week04/ex-guess-number/starter.py`
- `2-intermediate/exercises/week04/ex-guess-number/hints.md`
- `2-intermediate/exercises/week04/ex-pixel-art/README.md`
- `2-intermediate/exercises/week04/ex-pixel-art/starter.py`
- `2-intermediate/exercises/week04/ex-pixel-art/hints.md`
- `docs/SYLLABUS.md`

## Week 5: Dictionaries and Secret Codes

- **Driving question:** How can we look things up by name instead of by number, and turn a message into a secret code?
- **Planned runtime:** 4:40 (280 seconds)
- **Vocabulary:** dictionary, key, value, .items(), KeyError, cipher, encode / decode, encryption
- **Misconception to prevent:** A dictionary finds a key even when the spelling or capital letters are a little different, so "Crew" and "crew" are the same key.
- **Digital citizenship:** Encryption and passwords: a real password is only for you and your parent or caregiver, not for friends, games or chat; never type a real password into a program you or a friend wrote, we only use made-up game passwords; long is strong; and if a website or message asks for your password, ask a grown-up first.
- **Practice activity:** `2-intermediate/exercises/week05/ex-monster-stats`

### Instructional objectives

- Make a dictionary, read, change and add keys, and loop over it with .items().
- Encode and decode a message with a Caesar shift.
- Explain what a KeyError means and avoid it by checking with in first.
- Explain why passwords and other secrets need protecting.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Nova slides a sticky note to Pixel. It says: grj. ‘Is that a word?’ beeps Pixel. ‘It's a secret code!’ says Nova. Every letter moved three places along the alphabet. To crack it, Pixel needs a lookup: give it a secret letter, get back the real one. Python has a tool made for lookups. It's called a dictionary. Let's open it! | A sticky note reading 'grj' lands on the workbench. Pixel scans it with a magnifying glass; a paper cipher wheel spins in the background. A big book labeled DICTIONARY opens with a sparkle. **On screen:** MISSION: Crack the code; Secret note: grj | Keep the decoded word hidden until scene 2. Do not use the lesson's sticky-note message, the workbook's 'zhoo grqh!', or the homework's message. |
| 0:30–1:30 | **Explain keys, values and the Caesar cipher** | A list finds things by number, like planets of 0. A dictionary finds things by name. Each name is called a key, and what it gives back is its value. Think of a real dictionary. To find dragon, you don't read every page. You jump straight to the word and read its meaning. The word is the key. The meaning is the value. Python writes a dictionary with curly braces, and a colon between each key and its value. A Caesar cipher is a lookup too! With a shift of 3, a becomes d, b becomes e. At the end, the alphabet wraps around, so z becomes c. To decode, shift the other way. So g, r, j turns back into… dog! | A list row with index numbers fades into dictionary cards: key → value arrows. A paper dictionary flips straight to 'dragon'. Then two alphabet strips line up with a shift of 3: a over d, b over e, and x, y, z wrapping to a, b, c. The letters g, r, j slide back three places to become d, o, g. **On screen:** List: by number • Dictionary: by name; key : value  inside { }; Shift 3: a → d, z → c; Decode: shift the other way | Use the lesson's real-dictionary analogy. Keys and values in different shapes, not only colors. Do not use 'hi' → 'kl', 'hi there!' or 'cat' (exit-ticket bonus). |
| 1:30–2:35 | **Worked example: a spaceship dictionary** | Let's build one in the Shell. Nova types ship equals, curly brace, name colon Comet, fuel colon 20, crew colon 3. Look up by key: ship of "fuel" gives back 20. To change a value, use the same key: ship of "fuel" equals 25. To add a new key, just give it a value: ship of "color" equals "orange". Now let's see everything. for key, value in ship dot items, colon, then print an f-string: key, colon, value. Dot items hands us each key and its value, one pair at a time. The Shell shows: name: Comet, fuel: 25, crew: 3, color: orange. And what if we ask for a key that isn't there, like speed? Pause and predict… KeyError! | Code panel and Shell. Key → value cards appear for name → "Comet", fuel → 20, crew → 3. The fuel card's value flips 20 → 25; a new card color → "orange" snaps onto the end. A loop spotlight visits each pair while the Shell prints four lines. A blank card labeled speed flashes a gentle question mark. **On screen:** ship = {"name": "Comet",;         "fuel": 20, "crew": 3}; for key, value in ship.items():;     print(f"{key}: {value}") | The dictionary is split over two on-screen lines (valid Python inside the braces); show ship["fuel"] = 25 and ship["color"] = "orange" in the code panel. Real output: name: Comet / fuel: 25 / crew: 3 / color: orange. Do not show the Blobby monster, stat_report(), level_up() or get_stat(). |
| 2:35–3:40 | **Friendly bug hunt: KeyError and wrong spelling** | Bug hunt: two kinds today! The loud one first. Nova types ship of "speed". Red text! The last line says KeyError, then the key Python couldn't find, in quotes: speed. There's no such key! To be safe, check first: "speed" in ship gives back False. Now the quiet one. Nova adds a crew member: ship of "Crew", with a capital C, equals 4. No red text! But crew still says 3. Why? Here's a detective trick: print the whole dictionary. Pause and point. Look! There are two crews now. Crew with a capital C is a brand new key. Like a real dictionary, the spelling must be exact. Nova fixes the line to a small c and runs it again. Now crew is 4. | Shell shows ship["speed"] and the KeyError line, with 'speed' circled. A check line "speed" in ship → False appears with a stop-hand icon. Then ship["Crew"] = 4 runs with no error; the printed dictionary shows both 'crew': 3 and 'Crew': 4, and a magnifier highlights the capital C. The line is corrected, the program reruns, and the dictionary shows 'crew': 4 only. **On screen:** KeyError: 'speed'; "speed" in ship  →  False; "Crew" and "crew" are different keys; Print the whole dictionary | Real wording: KeyError: 'speed'. The rerun starts from a fresh program so the stray 'Crew' key is gone. Never show get_stat()'s fix, the Word Counter counting fix, or the Pixel Pet keys. |
| 3:40–4:40 | **Recap, passwords, and handoff** | Door five is open! Let's remember. A dictionary looks things up by name. Each key gives back a value. A KeyError means there's no such key, so check the spelling, or check first with in. A Caesar cipher is fun, but easy to crack: there are only 25 shifts to try! Real apps use much stronger encryption. So: a real password is only for you and your parent or caregiver. Never type a real password into a program you or a friend wrote. Long is strong. And if a message asks for your password, ask a grown-up first. Now open Exercise 5.1, Monster Stats. Loop with dot items, level up the monster, then type magic as the stat. See you in the code! | Door 5 opens. Recap cards: key → value, .items() loop, KeyError magnifier, cipher wheel. A padlock shows four rule icons: you plus a grown-up, no real passwords in our programs, three random words joined together, ask a grown-up. The Monster Stats card slides in. **On screen:** Look up by name: key → value; Real passwords stay private; NEXT: Exercise 5.1 Monster Stats | Show only made-up example passwords (e.g. three random words), never anything resembling a real account. AI-voice disclosure on the end card and a five-second hold. |

**Lesson handoff:** Open Exercise 5.1 Monster Stats and press Run. Loop with for key, value in monster.items(): to build lines like health: 30 (TODO 1) and finish level_up() (TODO 2). Then type magic when it asks for a stat, read the KeyError and do TODO 3: check if stat in monster: first. Next, Exercise 5.2 Caesar Cipher.

**Curriculum evidence:**

- `2-intermediate/teaching-material/lessons/week05.tex`
- `2-intermediate/teaching-material/workbook/week05.tex`
- `2-intermediate/teaching-material/homework/week05.tex`
- `2-intermediate/exercises/week05/ex-monster-stats/README.md`
- `2-intermediate/exercises/week05/ex-monster-stats/starter.py`
- `2-intermediate/exercises/week05/ex-monster-stats/hints.md`
- `2-intermediate/exercises/week05/ex-caesar-cipher/README.md`
- `2-intermediate/exercises/week05/ex-caesar-cipher/starter.py`
- `2-intermediate/exercises/week05/ex-caesar-cipher/hints.md`
- `docs/SYLLABUS.md`

## Week 6: Debug Like a Detective

- **Driving question:** How do programmers find bugs with a strategy instead of luck?
- **Planned runtime:** 4:40 (280 seconds)
- **Vocabulary:** bug, debugging, traceback, print-debugging, rubber duck debugging, trace table, bug report
- **Misconception to prevent:** No red text means no bugs, and changing lots of things at once is the fastest way to fix a program.
- **Digital citizenship:** Growth mindset reflection: finish the sentence "Six weeks ago I could not … and now I can …", and use the word yet: "I can't fix this yet." Being kind to yourself and to others when code breaks is part of being a good digital citizen: we never laugh at someone's bug.
- **Practice activity:** `2-intermediate/exercises/week06/ex-bug-high-scores`

### Instructional objectives

- Read a traceback from the bottom up and name the error type and the line where it happened.
- Use print() lines and a trace table to find where a program's values go wrong.
- Explain code line by line to a partner or a rubber duck to find a bug that does not crash.
- Write a short bug report: what went wrong, where, and what you changed.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Five doors are open, and the Kids Coding workshop is buzzing. But today, Pixel finds a pile of broken programs on the bench. One crashes. One gives a wrong answer. ‘Should I change everything until it works?’ asks Pixel. ‘No way,’ says Nova. ‘Detectives use tools!’ Ready to grab yours? | Mission map with five open doors and a sixth glowing door marked CHECKPOINT. A workbench holds program cards: one with red text, one with a wrong-answer sign. Pixel holds a giant spanner, ready to bash; Nova hands over a detective kit with a magnifying glass, a print stamp, a rubber duck and a pencil. **On screen:** MISSION: Debug like a detective; Tools, not luck | Do not show any workshop station program on the bench cards; use blank code shapes. |
| 0:30–1:30 | **Explain the four detective tools** | Every programmer in the world writes bugs, every day. Good programmers find them with tools. Here are four. One: read the traceback from the bottom up. The last line says what went wrong. The line above says where. Two: print-debugging. Add a print to see what's really inside a variable, then remove it when you're done. Three: the rubber duck. Explain your code, line by line, out loud, to a duck, a toy or a partner. Halfway through, you often hear yourself say the bug. Four: the trace table. Follow the code with a pencil, like a very slow computer, and write down every value. Be a doctor, not a guesser. Change one thing, then run again. | Four tool cards flip over one at a time: an upward arrow over red text, a print() stamp, a rubber duck with a speech bubble, and a pencil over a table grid. Then a doctor's kit maps onto them: ask where it hurts (traceback), take a temperature (print), listen (duck), check step by step (trace table). A sign reads: Change one thing, then run again. **On screen:** 1 Read the traceback bottom-up; 2 Print-debugging; 3 Rubber duck; 4 Trace table | Use the lesson's 'doctor, not a guesser' analogy and its four tool names exactly. Keep the tool cards on screen as a reference strip for scenes 3 and 4. |
| 1:30–2:35 | **Worked example: reading a traceback** | Let's read a real traceback. Nova's program should count spider legs: def spider legs, with the parameter spiders. Then print spider legs of 3. Pixel runs it, and red text appears. Don't panic. Read it from the bottom up. WHAT went wrong? The last line: NameError: name spdiers is not defined. Python even asks: did you mean spiders? A NameError means Python doesn't know that name. It's often a typo, or missing quotes. WHERE? The last File line, just above the code line: line 2, in spider legs. In Thonny, click the blue link to jump right there. HOW did it get there? The lines further up show the main program, on line 4, called spider legs. Now look at line 2. Pause and point. Two letters are swapped! Fix the typo, and run: 24. | Code panel: def spider_legs(spiders): / return spdiers * 8 / blank / print(spider_legs(3)). The red traceback appears in the Shell. A pointer climbs from the bottom: the last line gets a WHAT tag, the 'line 2, in spider_legs' line gets a WHERE tag, and the 'line 4, in <module>' line gets a HOW tag. The typo 'spdiers' wiggles; the letters swap into 'spiders' and the Shell shows 24 next to three cartoon spiders. **On screen:** WHAT: the last line; WHERE: line 2, in spider_legs; HOW: line 4 called it; NameError: name 'spdiers' is not defined… | Real traceback lines (Python 3.10+): File "...", line 4, in <module> / print(spider_legs(3)) / File "...", line 2, in spider_legs / return spdiers * 8 / NameError: name 'spdiers' is not defined. Did you mean: 'spiders'? Python 3.11+ also adds ^ marker lines under each code line. Show the full last line in the Shell; the on-screen card shortens it. Never show the Station 1 card_line() traceback or its fix. |
| 2:35–3:40 | **Friendly bug hunt: a bug with no red text** | Now the sneakiest kind of bug: one with no red text at all. Nova's total apples function should add up the apples Pixel picked on three days: 3, 1 and 2. That's 6. Pixel runs it and says… 2. No crash, just a wrong answer. Time for the rubber duck! Nova explains each line out loud. ‘total starts at 0. For apples in days, total equals apples. Then return total.’ Hmm. Let's check with a trace table. Round one: apples is 3, so total is 3. Round two: apples is 1, so total is 1. Round three: total is 2. The table shows a value we didn't expect! total forgets what it had. What should that line say? Pause and point. total equals total plus apples! Run again: 6. | Code panel: def total_apples(days): / total = 0 / for apples in days: / total = apples / return total, and print(total_apples([3, 1, 2])) with Shell output 2. Pixel holds a rubber duck while Nova talks to it; each line glows as it is explained. A trace table with columns apples and total fills row by row: 3 \| 3, 1 \| 1, 2 \| 2, and the total column flashes softly where it drops. The line becomes total = total + apples; a second table fills 3, 4, 6 and the Shell shows 6. **On screen:** No red text ≠ no bug; total = apples; Trace table: apples \| total; total = total + apples  →  6 | Code is valid: with total = apples the call returns 2; with total = total + apples it returns 6. No rapid flashing. Never show any Loot Shop function, the Station 5 smallest() puzzle, the Pixel Pet mood() rule, the score/lives warm-up table, or the checkpoint's count_stars() question. |
| 3:40–4:40 | **Recap, growth mindset, and handoff** | Detective training complete! Let's remember the four tools. Read the traceback from the bottom up: what, then where. Print-debugging shows what's inside a variable. The rubber duck catches bugs that don't crash. A trace table follows every value. Change one thing, then run again. Now think back. Six weeks ago, I could not… and now I can… How would you finish that? If a bug makes you feel stuck, say: I can't fix this yet. And be kind when code breaks. We never laugh at someone's bug. Workshop time! After Station 1 with your teacher, open Station 2, High Scores. Read the traceback, draw the list with index numbers, and write a bug report for each bug. Happy hunting, detectives! | The CHECKPOINT door opens. The four tool cards line up as badges. A sentence card fills in: 'Six weeks ago I could not … and now I can …' and a sticky note adds the word YET. Nova and Pixel high-five beside a 'We never laugh at someone's bug' sign. A bug-report card (error name, line, what I changed) and the Station 2 card slide in. **On screen:** Traceback • print • duck • trace table; I can't fix this… yet!; NEXT: Station 2 High Scores | Pause three seconds after the sentence starter so learners can answer. AI-voice disclosure on the end card and a five-second hold. Do not show any station's fix. |

**Lesson handoff:** Start the bug-hunt workshop. After Station 1 Hero Card with your teacher, open Station 2 High Scores and press Run: read the traceback bottom-up (which function, which line?), draw the list with its index numbers, fix bug 1, then add print("best is", best) inside podium() to find bug 2. Write a bug report for each bug, remove your print lines, then rotate to stations 3, 4 and 5.

**Curriculum evidence:**

- `2-intermediate/teaching-material/lessons/week06.tex`
- `2-intermediate/teaching-material/workbook/week06.tex`
- `2-intermediate/teaching-material/homework/week06.tex`
- `2-intermediate/exercises/week06/ex-bug-hero-card/README.md`
- `2-intermediate/exercises/week06/ex-bug-hero-card/starter.py`
- `2-intermediate/exercises/week06/ex-bug-hero-card/hints.md`
- `2-intermediate/exercises/week06/ex-bug-high-scores/README.md`
- `2-intermediate/exercises/week06/ex-bug-high-scores/starter.py`
- `2-intermediate/exercises/week06/ex-bug-high-scores/hints.md`
- `2-intermediate/exercises/week06/ex-bug-countdown/README.md`
- `2-intermediate/exercises/week06/ex-bug-countdown/starter.py`
- `2-intermediate/exercises/week06/ex-bug-countdown/hints.md`
- `2-intermediate/exercises/week06/ex-bug-loot-shop/README.md`
- `2-intermediate/exercises/week06/ex-bug-loot-shop/starter.py`
- `2-intermediate/exercises/week06/ex-bug-loot-shop/hints.md`
- `docs/SYLLABUS.md`

## Week 7: Files: Saving Your Stuff

- **Driving question:** How can a program remember things after it closes?
- **Planned runtime:** 4:35 (275 seconds)
- **Vocabulary:** file, open / with, read / write / append, strip(), split(","), FileNotFoundError, data privacy
- **Misconception to prevent:** A program still remembers its variables the next time it runs, or opening a file with "w" adds to it instead of wiping everything that was there.
- **Digital citizenship:** What should (not) be saved? Save only what the program needs, and never personal information: a nickname, a high score and a favorite color are fine; a home address and a password never. A file stays on the computer after the game closes, and anyone who uses this computer, or who gets a copy of the file, can read it. Real apps save data about you too, so ask: what are they saving, and do they really need it?
- **Practice activity:** `2-intermediate/exercises/week07/ex-save-high-scores`

### Instructional objectives

- Save data to a text file with open and with, choosing "a" to add and "w" to replace.
- Read a file line by line and clean each line with strip() and split() into a list.
- Handle a missing file with try/except FileNotFoundError and explain why "w" can wipe data.
- Decide what a game should and should not save, and keep personal information out of files.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Hi, coders! Nova just set a record in a dice game: one hundred and twenty points! ‘Pixel, remember my score!’ says Nova. Pixel closes the game for the night. Next morning, it opens again. ‘Hello! Who are you? The high score is zero.’ Beep boop. Every score is gone! Why did the program forget? And how can we help it remember? | Nova cheers beside a dice game screen showing 120. Pixel presses a big Close button; the screen goes dark and a moon crosses the window. The game reopens with a blank score box reading 0 and Pixel's face shows a question mark. Freeze on a thinking bubble with an empty notebook. **On screen:** MISSION: Make the game remember; Pause: Where could a score be kept? | Keep the 'forgetting' playful: a soft whoosh as the score fades, not a sad or failure sound. Hold three seconds on the question. |
| 0:30–1:25 | **Explain files and the three modes** | Here's the secret. A program keeps its variables in memory, and memory is wiped when the program closes. It's like writing on your hand: handy, but gone after a wash. A file is different. It's like a notebook in a drawer. It stays on the computer's disk, next to your program. To use a file, we open it and choose a mode. r means read. a means append: add to the end, on the next empty line. And w means write a fresh page. Careful! w rips out every page first. We always open files with the word with. When the pushed-in lines end, Python shuts the drawer for us. | Left: a hand with '120' written on it, washed clean by a cartoon tap. Right: a desk drawer opens to reveal a notebook labeled with a file icon. Three mode cards slide in: r (an eye reading), a (a pencil writing on the next empty line), w (every page torn out, then one new line). The drawer closes by itself when an indented code block ends. **On screen:** File = a notebook that stays; "r" read  •  "a" add to the end; "w" wipes, then writes; with closes the file for you | Each mode card needs an icon and a label, not color alone. Show the w rip-out clearly but cheerfully; it sets up the bug hunt. |
| 1:25–2:30 | **Worked example: write, then read a file** | Let's build one together. Nova keeps a sticker file called stickers dot t x t. It already holds one line: unicorn, comma, two. Now Nova adds a line. With open, stickers dot t x t, mode a, as file. Then, pushed in: file dot write, dragon comma three, backslash n. Backslash n means start a new line. Now let's read it back with mode r, one line at a time. Each line hides a new-line at the end. strip removes it. split, with a comma, cuts the line into a list: dragon and three. But that three is still text! Everything from a file is text, just like input. So int turns it into a number. Pause and predict: what will Pixel print? Unicorn two, then dragon three! | A code panel types the two blocks line by line: with open("stickers.txt", "a") as file: / file.write("dragon,3\n"), then with open("stickers.txt", "r") as file: / for line in file: / line = line.strip() / parts = line.split(",") / print(parts[0], int(parts[1])). A file icon beside it gains the new line 'dragon,3' under 'unicorn,2'. A string card 'dragon,3\n' loses its \n (strip), then splits at the comma into a two-box list ['dragon', '3']; the '3' box hops through an int() machine. The Shell panel shows 'unicorn 2' and 'dragon 3'. **On screen:** with open("stickers.txt", "a") as file:; file.write("dragon,3\n"); strip(), then split(","); Text from a file needs int() | Code must match the course style (with open(...) as file:, four-space indents). Do not show Exercise 7.1's save_score or load_scores lines, the hints' fill-in shapes, or the pets.txt exit ticket. The sticker file is a new, nearby example. |
| 2:30–3:40 | **Friendly bug hunt: FileNotFoundError** | Bug hunt time! Nova writes a few lines to read the stickers back. Pixel presses Run, and red text fills the Shell. That's a traceback. We read it from the bottom up. The last line says what went wrong: FileNotFoundError. No such file or directory: stikers dot t x t. The file name is printed in quotes. Detective steps! What did we expect? Our stickers. What happened? Python couldn't find the file. Now compare the name in quotes, letter by letter, with the name in Finder. Pause and point. Yes! The c is missing. Nova fixes the spelling, and it works! Other clues for this error: the program is saved in another folder, or the file isn't made yet. Then try and except FileNotFoundError can do something else instead of crashing. And if saved lines keep vanishing? Look for a sneaky w. | Thonny Shell panel with a red traceback; a magnifying glass slides up from the last line: FileNotFoundError: [Errno 2] No such file or directory: 'stikers.txt'. Split screen: the quoted name above a Finder file icon labeled stickers.txt; letters light up one pair at a time until the missing c flashes. The corrected line runs and the sticker list prints. A small try/except card and a w card with a warning sign appear at the end. **On screen:** Read the traceback bottom-up; Compare the name letter by letter; try / except FileNotFoundError; Lines vanishing? Look for "w" | Give a four-second prediction pause before the missing letter is revealed. Do not use the lesson's high_score.txt bug or the 7.1 file names; keep the try/except card as a concept, not Exercise 7.1's TODO 3 code. |
| 3:40–4:35 | **Recap, data privacy, and handoff** | Mission complete! Let's remember. Programs forget when they close, but files remember. Choose a to add, w to replace, and r to read. strip cleans a line, split cuts it into a list, and int turns text into a number. Now, a privacy question. Should a game save your nickname? Thumbs up! Your high score? Sure. Your address or password? Never! Anyone who uses the computer can open a file. So save only what the program needs. Your turn: open Save High Scores and press Run twice. Does it remember you? Not yet! Finish the three TODOs, play three times, and peek inside high scores dot t x t. Happy coding! | Recap icons: notebook, three mode cards, scissors cutting a line at a comma. Then five index cards flip one by one: nickname, high score, favorite color get a thumbs-up; home address and password get a crossed-out lock. End on the Lucky Dice exercise card with 'Games saved so far: 0' turning into 1, 2, 3. **On screen:** Files remember • a adds • w replaces; Save only what the program needs; Never: address or password; NEXT: Save High Scores | Use category words only, never realistic personal data. End card includes 'Narration uses an AI-generated voice' and a five-second clean hold. |

**Lesson handoff:** Open Exercise 7.1 Save High Scores (Lucky Dice) and press Run twice: it still says Games saved so far: 0. Do TODO 1 (open the file with "a" and write one nickname,score line), TODO 2 (strip, skip empty lines, split at the comma, turn the score into a number with int) and TODO 3 (if the file is missing, make an empty one with "w"). Play three times, open high_scores.txt in Thonny, run check_my_work.py, then choose 7.2 Word Guess or 7.3 Dot Art from a File.

**Curriculum evidence:**

- `2-intermediate/teaching-material/lessons/week07.tex`
- `2-intermediate/teaching-material/workbook/week07.tex`
- `2-intermediate/teaching-material/homework/week07.tex`
- `2-intermediate/exercises/week07/ex-save-high-scores/README.md`
- `2-intermediate/exercises/week07/ex-save-high-scores/starter.py`
- `2-intermediate/exercises/week07/ex-save-high-scores/hints.md`
- `2-intermediate/exercises/week07/ex-word-guess/README.md`
- `2-intermediate/exercises/week07/ex-dot-art-file/README.md`
- `2-intermediate/exercises/week07/hw-idea-notebook/README.md`
- `docs/SYLLABUS.md`
- `2-intermediate/teaching-material/teacher-guide.tex`

## Week 8: Testing: Prove It Works

- **Driving question:** How can a tiny program check our code for us and catch bugs before players find them?
- **Planned runtime:** 4:35 (275 seconds)
- **Vocabulary:** test, assert, pytest, normal case, edge case, expected vs actual
- **Misconception to prevent:** Any test catches any bug, a test with no assert still checks something, or when a test fails you should change the test until it passes.
- **Digital citizenship:** Trust: why apps need testing. In 1999 a spacecraft was lost on its way to Mars because two parts of its software used different units, and no test checked them together. People can only trust apps and games that have been tested. Testing your game is a way of being fair to your players.
- **Practice activity:** `2-intermediate/exercises/week08/ex-test-the-clamp`

### Instructional objectives

- Write a test function with assert that checks what a function returns.
- Run tests with pytest in Thonny and read PASSED, FAILED and the failure message from the bottom up.
- Choose normal and edge test cases, such as an empty list or a value exactly on a limit.
- Use a failing test to find a bug, and decide whether the code or the expected answer is wrong.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Hi, coders! Nova's coin game is ready to share. But this morning, Nova changed one line. Is everything still right? Pixel plays the game. Then again. And again. Fifty times! ‘Checking by hand is slow,’ says Pixel. ‘My battery is at two percent.’ What if a tiny program could check the game for us, in less than a second? | Nova holds a game cartridge labeled 'Coin Game'. Pixel plays on a screen while a tally counter climbs to 50 and Pixel's battery icon drains to 2%. A tiny robot-shaped checklist zooms in with a stopwatch showing 0.1 s. **On screen:** MISSION: Check the game fast; By hand = slow  •  A test = 1 second | Keep the battery joke gentle. Pause two seconds on the question. |
| 0:30–1:25 | **Explain assert, pytest, and edge cases** | That tiny program is called a test. Its magic word is assert. Assert means, ‘I'm sure this is true.’ Try it in the Thonny Shell. Assert two plus two, double equals, four. Nothing happens. Good news! Now: assert two plus two, double equals, five, with the message, math is broken. Python stops and shows AssertionError: math is broken. A test is a function whose name starts with test underscore. pytest is a helper that finds every test, runs it, and says PASSED or FAILED. Try normal cases, what usually happens, and edge cases, the strange corners: empty, zero, first, last, or exactly on a limit. Bugs love to hide at the edges! | Thonny Shell panel. 'assert 2 + 2 == 4' is typed; nothing appears and a small green check pops. 'assert 2 + 2 == 5, "math is broken"' is typed; the red line AssertionError: math is broken appears. A name tag 'test_' sticks onto a function card, and a pytest magnifier robot scans cards, stamping PASSED or FAILED. Crash-test dummies try a normal road, then a cliff edge labeled empty / zero / last / on the limit. **On screen:** assert = "I'm sure this is true"; Test names start with test_; pytest says PASSED or FAILED; Normal case + edge cases | These two Shell lines come from the workbook. Use the crash-test dummy analogy from the lesson; keep the dummies cartoonish and safe. |
| 1:25–2:30 | **Worked example: two tests that pass** | Let's test one. Nova's file, coin tools, has a function called total coins. It adds up the coins in a list of bags. Now Nova makes a test file. First: from coin tools, import total coins. Then a test: def test three bags. Inside: assert total coins of two, five and three, double equals ten, with a message, two plus five plus three is ten. We work out ten on paper first, not by running the code. That's our normal case. Now an edge case: a bag with zero coins in the middle. Assert total coins of four, zero and six, double equals ten. At the bottom, three lines let the Run button start pytest. Pixel presses Run. Two lines say PASSED, and the last line says two passed! | Code panel types test_coins.py: from coin_tools import total_coins / def test_three_bags(): / assert total_coins([2, 5, 3]) == 10, "2 + 5 + 3 is 10" / def test_empty_bag_in_the_middle(): / assert total_coins([4, 0, 6]) == 10, "an empty bag adds 0 coins" / if __name__ == "__main__": / import pytest / pytest.main(["-v", __file__]). Three coin bags (2, 5, 3) pour into a counter showing 10; then bags 4, 0 and 6, where the empty middle bag adds nothing, also show 10. The output panel shows test_coins.py::test_three_bags PASSED, test_coins.py::test_empty_bag_in_the_middle PASSED and '2 passed'. **On screen:** assert total_coins([2, 5, 3]) == 10; assert total_coins([4, 0, 6]) == 10; Work out the answer on paper first; Press Run: 2 passed | total_coins is a new example (a correct loop that adds every bag). The edge case is deliberately a zero bag, not an empty list, so it does not hand over Exercise 8.2's empty-list test. Never show clamp, best_score, encode, can_ride or the Exercise 8.3 helpers, or any expected answer from those exercises. |
| 2:30–3:40 | **Friendly bug hunt: a failing test is a map** | Bug hunt! Nova tidies up total coins and changes one line. Pixel presses Run. Both tests FAILED! Let's read it from the bottom up. The last line is the score: two failed. Now the first failure. The E lines say what happened: assert three, double equals, ten, where three is total coins of two, five and three. The function gave back three, but we expected ten. When a test fails, ask: is the code wrong, or is my expected answer wrong? Two plus five plus three really is ten. So the code is wrong, and the test stays. Pause and point. Inside the loop, Nova wrote total equals coins. That throws away the old total each time. Nova changes it to total equals total plus coins. Run again: two passed! Sneaky fact: a test with just one bag would pass, even with this bug. | Output panel: test_three_bags FAILED, test_empty_bag_in_the_middle FAILED; below the first one E AssertionError: 2 + 5 + 3 is 10, E assert 3 == 10 and E + where 3 = total_coins([2, 5, 3]), then '2 failed'. A magnifier climbs from the last line upward. Expected (10) and actual (3) cards face each other. A paper sum 2 + 5 + 3 = 10 gets a check. The code panel highlights 'total = coins' inside the loop; it changes to 'total = total + coins'; rerun shows '2 passed'. A one-bag test card [7] passes with both versions, with a thought bubble. **On screen:** Read FAILED from the bottom up; Code wrong, or expected answer wrong?; Test is right? Then fix the code; total = total + coins | Leave four seconds before the buggy line is highlighted. This bug is invented for the video; do not use any Exercise 8.3 bug (lives, medal, name tag, average) or the exit-ticket ride example. |
| 3:40–4:35 | **Recap, trust in software, and handoff** | Test complete! Let's remember. assert means, ‘I'm sure this is true.’ A test is a function whose name starts with test underscore, and pytest says PASSED or FAILED. Try normal cases and edge cases. When a test fails, ask: is the code wrong, or the test? In 1999, a spacecraft was lost on its way to Mars. Two parts of its software used different units, and no test checked them together. People can only trust apps that have been tested. Your turn: open Test the Clamp and press Run. Why do the empty tests pass? Then write an assert in each one, and add a test on a limit. Happy testing! | Recap icons: an assert badge, a test_ name tag, PASSED and FAILED stamps. A cartoon spacecraft drifts past two mismatched ruler signs labeled 'pounds' and 'newtons'. Everyday app icons (map, messages, game save) gain a shield. End on the Test the Clamp exercise card with three PASSED lines and two empty test boxes. **On screen:** Normal + edge • Code or test wrong?; Tested apps can be trusted; NEXT: Test the Clamp | Keep the spacecraft story calm; no explosion. Do not reveal any expected value for the clamp tests. End card includes the AI-voice disclosure and a five-second hold. |

**Lesson handoff:** Open Exercise 8.1 Test the Clamp: read clamp_tools.py, then press Run on starter.py (your test file) and explain why the empty tests pass. TODO 1 and TODO 2: write an assert line in each empty test. TODO 3: add a fourth test for a value exactly on a limit. Change one expected answer to something wrong, read the FAILED message, change it back, then run check_my_work.py to catch three broken clamps.

**Curriculum evidence:**

- `2-intermediate/teaching-material/lessons/week08.tex`
- `2-intermediate/teaching-material/workbook/week08.tex`
- `2-intermediate/teaching-material/homework/week08.tex`
- `2-intermediate/exercises/week08/ex-test-the-clamp/README.md`
- `2-intermediate/exercises/week08/ex-test-the-clamp/starter.py`
- `2-intermediate/exercises/week08/ex-test-the-clamp/hints.md`
- `2-intermediate/exercises/week08/ex-test-best-score/README.md`
- `2-intermediate/exercises/week08/ex-fix-the-bugs/README.md`
- `2-intermediate/exercises/week08/hw-test-the-cipher/README.md`
- `docs/SYLLABUS.md`
- `2-intermediate/teaching-material/teacher-guide.tex`

## Week 9: Event-Driven Games

- **Driving question:** How can keys and timers make a game react and move one frame at a time?
- **Planned runtime:** 4:40 (280 seconds)
- **Vocabulary:** event, handler, listen(), game loop, frame, collision, license / attribution
- **Misconception to prevent:** Writing onkey(go_left(), "Left") hands the function to turtle (it really runs it once, right away), or a while True loop is a good way to run a turtle game.
- **Digital citizenship:** Attribution and open licenses: pictures and sounds belong to the person who made them. CC0 means anyone may use it; CC BY means you may use it if you credit the creator; if there is no license, do not use it. Use turtle's own shapes and your own drawings first; if you use something else, a grown-up helps you find it (no accounts, no downloads alone), and you write a credit, for example # Star sound by Mei (CC BY), in your code and on your game's title screen.
- **Practice activity:** `2-intermediate/exercises/week09/ex-etch-a-sketch`

### Instructional objectives

- Connect keys to handler functions with onkey and listen, passing the function without parentheses.
- Build a game loop with ontimer that moves things one frame at a time.
- Detect touching with a distance check and keep the game state in a dictionary.
- Choose a final-project option and explain why borrowed pictures and sounds need a license and credit.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Hi, coders! Pixel presses Run and taps the arrow keys. Left, left, right! Nothing moves. Until now, our programs ran from top to bottom, then stopped. But games are different. Games wait: for a key press, or for a timer to ring. Today, Pixel learns to wait and react. And your own final project begins! | A turtle window with a turtle at the bottom. Pixel taps arrow keys shown as big key caps; the turtle stays still. A straight top-to-bottom arrow beside a code panel bends into a circle with a doorbell and a kitchen timer on it. A sealed envelope labeled 'Final Project' glows in the corner. **On screen:** MISSION: Make the game react; Games wait for keys and timers | Use a soft 'boop' on each key tap with no movement, not an error sound. |
| 0:30–1:25 | **Explain events, handlers, and the game loop** | Something that happens while a program runs, like a key press, is an event. The function that answers it is a handler. Think of a doorbell. You don't stand by the door all day. The bell calls you! screen dot onkey, go right, Right, means: when the Right arrow is pressed, call go right. But the bell only works when switched on. That's screen dot listen. Turtle's kitchen timer is ontimer. It calls a function after some milliseconds. Our game loop does one frame, where everything moves a tiny bit, then sets the timer again. And two things are touching when the distance between them is small, like less than thirty steps. | A doorbell labeled 'Right' wired to a function card go_right; pressing it lights the card. A light switch labeled listen() turns the bell on. A kitchen timer labeled ontimer rings, a flip-book page turns (one frame), and the timer winds itself again. Two circles approach; a ruler between them reads 28 and the word 'touching!' appears under 30. **On screen:** Event → handler; screen.onkey(go_right, "Right"); screen.listen() switches it on; ontimer → the next frame | Keep the doorbell and kitchen-timer analogy from the lesson. Label shapes with words, not color alone. |
| 1:25–2:30 | **Worked example: keys and a timer** | Let's watch a tiny game work. A ball starts at the top, and Nova's turtle waits in the middle. Handler one: go left, which moves x twenty steps left. Handler two: go right, twenty steps right. Then the frame function, called fall. The ball moves down five steps. If it's still above minus two hundred, screen dot ontimer, fall, fifty. That means: run fall again in fifty milliseconds. A thousand milliseconds make one second, and a thousand divided by fifty is twenty. So that's twenty frames every second! Notice: no parentheses after fall or go left. We hand turtle the function, and turtle calls it later. Bigger games also keep their state, like the score, in a dictionary. | Split screen. Left, a code panel types: def go_left(): / player.setx(player.xcor() - 20) / def fall(): / ball.sety(ball.ycor() - 5) / if ball.ycor() > -200: / screen.ontimer(fall, 50) / screen.onkey(go_left, "Left") / screen.listen(). Right, a turtle game frame: the ball drops in small steps while a frame counter ticks 1, 2, 3; the turtle slides 20 steps when a Left key cap is pressed. A math card: 1000 ÷ 50 = 20 frames each second. A dictionary card state = {"score": 0, "running": True} appears at the end. **On screen:** player.setx(player.xcor() - 20); screen.ontimer(fall, 50); 1000 ÷ 50 = 20 frames each second; No () after the function name | Code follows the workbook's try_keys.py style. Do not show Dodge the Meteors' move_player, is_touching or game_loop TODO lines, and do not pose the exit-ticket 'moved once and stopped' question. |
| 2:30–3:40 | **Friendly bug hunt: the handler that never runs** | Bug hunt! Nova wants the turtle to spin when you press r. The code says: def spin, turn left ninety. Then screen dot onkey, spin, open and close parentheses, r. Pixel presses Run. The turtle spins once, right at the start. Then r does nothing, and there's no red error. Detective steps! What did we expect? A spin on every press. What happened? One spin, then nothing. Read one line at a time. Pause and point. Those parentheses call spin right now, only once, and hand onkey its answer, which is nothing. Nova removes them. Run again. Still nothing! Second clue: is the doorbell switched on? There's no screen dot listen. Nova adds it. Third clue: on a Mac, click the turtle window once so it hears the keys. Spin, spin, spin! | Code panel: def spin(): / player.left(90) / screen.onkey(spin(), "r") / turtle.done(). The turtle turns once at launch, then an r key cap is pressed three times with no movement and no red text. A spotlight lands on spin(); the () fly off. Rerun: still nothing; a switched-off doorbell icon appears and screen.listen() slides in above turtle.done(). A cursor clicks inside the turtle window, then each r press spins the turtle 90 degrees. **On screen:** onkey(spin(), "r") runs it once; onkey(spin, "r") calls it later; Add screen.listen(); On a Mac: click the window first | Four-second prediction pause before the parentheses are highlighted. spin and the r key are new; do not reuse the lesson's go_left bug, the exit ticket's jump example, or Etch-a-Sketch's go_up. |
| 3:40–4:40 | **Recap, project kickoff, attribution, and handoff** | You made Pixel react! Let's remember. An event calls a handler. onkey connects them, listen switches on the doorbell, and ontimer runs the next frame. Now your final project begins! Option A is an Arcade Game with keys, a timer and a score. Option B is an Art Studio that saves and loads designs. Want a picture or sound? They belong to the people who made them. CC zero means anyone may use it. CC BY means you may use it if you give credit, in a comment and on your title screen. No license? Don't use it. Your turn: open Etch-a-Sketch. Press Run, click the window, and press Up. Nothing yet! Make the window listen, then add the other arrows. No parentheses! | Recap icons: doorbell, light switch, kitchen timer. Two project cards flip over: Option A, a game frame with a moving player, falling shapes and a score; Option B, a flower design with a 'saved design' note. A credit tag # Star sound by Mei (CC BY) attaches to a sound icon; a picture with no license gets a gentle stop sign. End on the Etch-a-Sketch exercise card. **On screen:** Option A: Arcade Game; Option B: Art Studio; CC0 or CC BY + credit. No license? No.; NEXT: Etch-a-Sketch | Use turtle shapes in the project cards, not borrowed art. Do not show Star Catcher code. End card includes the AI-voice disclosure and a five-second hold. |

**Lesson handoff:** Open Exercise 9.1 Etch-a-Sketch: press Run, click the turtle window once and press the Up arrow (nothing happens yet). TODO 1 make the window listen, TODO 2 write go_down(), go_left() and go_right(), TODO 3 connect the keys with screen.onkey and no () after the function name, TODO 4 make c clear the drawing, then run check_my_work.py. Next, 9.2 Dodge the Meteors. At home, fill in Planning page 1 (My pitch) of the Project Brief for Milestone M1.

**Curriculum evidence:**

- `2-intermediate/teaching-material/lessons/week09.tex`
- `2-intermediate/teaching-material/workbook/week09.tex`
- `2-intermediate/teaching-material/homework/week09.tex`
- `2-intermediate/exercises/week09/ex-etch-a-sketch/README.md`
- `2-intermediate/exercises/week09/ex-etch-a-sketch/starter.py`
- `2-intermediate/exercises/week09/ex-etch-a-sketch/hints.md`
- `2-intermediate/exercises/week09/ex-dodge-meteors/README.md`
- `2-intermediate/exercises/week09/hw-stamp-studio/README.md`
- `docs/SYLLABUS.md`
- `2-intermediate/teaching-material/teacher-guide.tex`

## Week 10: Project Studio 1: Plan and Core

- **Driving question:** How do we turn a project idea into a plan, and the plan into a small core loop that runs?
- **Planned runtime:** 4:35 (275 seconds)
- **Vocabulary:** pseudocode, flowchart, decomposition, core loop, milestone, code review
- **Misconception to prevent:** The best way to start is with the fancy parts (a title screen, colors, many levels), or by typing the whole game before running it, instead of building the smallest version that runs.
- **Digital citizenship:** Collaboration: splitting tasks fairly. Fair teams share the interesting and the boring jobs, swap the keyboard on time and give credit. Each team puts both nicknames in a comment on line 1 (# Made by Comet and Pixel) and a credit comment for any code it remixed. Using someone's idea is fine. Hiding that you used it is not. Real names are not needed anywhere in the code.
- **Practice activity:** `2-intermediate/project/project-brief.tex`

### Instructional objectives

- Turn a project idea into pseudocode or a flowchart that shows a loop, a decision and the data.
- Break the project into named functions and split the tasks fairly on a task board.
- Build a core loop that runs without crashing (Milestone M2).
- Give kind, specific code-review feedback with two stars and a wish.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Studio hook** | Hi, coders! Nova has a giant plan: Comet Catch, with ten levels, boss battles and a rainbow title screen. Nova starts typing everything at once. Pixel waits, and waits. ‘Which part can I run today?’ asks Pixel. Hmm. Nothing yet! Nobody can ride one perfect wheel. So what should Nova build first? | Nova's idea cloud overflows with levels, bosses and a rainbow title. A code panel fills with half-typed lines and a big 'not running yet' sign. Pixel taps a watch. A single shiny car wheel rolls in alone and wobbles over. **On screen:** STUDIO MISSION: Plan, then build; What is the smallest version? | Frame the big plan as exciting, not silly. Pause two seconds on the question. |
| 0:30–1:25 | **Explain the skateboard, pseudocode, and decomposition** | Build a skateboard first. It's tiny, but you can ride it. In a project, the skateboard is the core loop: the smallest version that runs. Before Python, we plan. Pseudocode is your program in plain words, one step per line. A flowchart draws the same steps: ovals for start and end, rectangles for steps, and diamonds for yes-or-no questions. Each line that does one job can become a function. ‘Move the player, but not off the screen’ becomes next x. The position and the direction go in. The new position comes out. That's decomposition: breaking a big problem into small, named parts. Your pitch and plan are Milestone M1. Your core loop is M2. | A skateboard, scooter, bike and car appear in a row; each one rolls. Then a pseudocode card (set up the screen, the player and the keys / repeat every tick: move, check, score) turns into a flowchart with an oval Start, rectangles, a diamond 'Touching the player?' and a 'next tick' arrow. One rectangle pops out as a function card next_x(x, direction) with 'in' and 'out' arrows. A milestone road shows M1, M2, M3, M4 and Showcase. **On screen:** Core loop = the skateboard; Oval start/end • Rectangle step; Diamond = yes/no question; M1 pitch + plan → M2 core loop | Flowchart shapes must also carry text labels. Match milestone names to the Project Brief. |
| 1:25–2:30 | **Worked example: a walking skeleton** | Let's turn a plan into a walking skeleton. Nova saves a new file: mygame dot p y. Never call it turtle dot p y! First, two dictionaries. SETTINGS holds numbers we might change, like a step of twenty. state holds things that change while playing, like the score. Next, the brain: clamp and next x. No turtle at all, just values in and an answer out. Then the key handlers and the game loop. At its end: screen dot ontimer, game loop, fifty. Run me again in fifty milliseconds. The start-up code goes at the bottom, under if name equals main. Press Run, click the window, press the arrows. The square slides and stops at the edges. That's M2! Art Studio teams build a menu loop, or a key that draws a new design. | Code panel types the lesson skeleton in steps, with a Run press after each step: SETTINGS = {"step": 20, "left_edge": -280, "right_edge": 280} / state = {"score": 0, "running": True} / def next_x(x, direction): / def game_loop(): ... screen.ontimer(game_loop, 50) / if __name__ == "__main__":. A brain icon sits beside clamp and next_x. The turtle window shows a square sliding left and right and stopping at both edges. A small Art Studio card shows a menu loop: Draw, Save, Load, Quit. **On screen:** Never name it turtle.py; SETTINGS + state dictionaries; screen.ontimer(game_loop, 50); if __name__ == "__main__": | Show only the lesson's tested skeleton; never the Star Catcher reference code or the answer-key Art Studio loop. Use 'Comet Catch' only as a title. Keep four-space indents. |
| 2:30–3:40 | **Bug hunt: partner code review** | Time for a partner code review. Swap seats. Pixel runs Nova's code and reads it with three questions. One: does it run? If there's red text, which line does the traceback point to? Two: are the names clear? next x tells you its job. A function called thing two doesn't! Three: does each function do one job, and are numbers you might change kept in the settings dictionary? Pixel also hunts last week's classic bugs: parentheses after a handler in onkey, a missing listen, and a game loop that never sets its timer again. Then Pixel writes two stars and a wish. ‘Star: next x says exactly what it does. Star: the square stops at the wall. Wish: could thing two get a name that tells its job?’ Nova says thanks, and decides what to change. | Nova and Pixel swap chairs. A three-item checklist card: Does it run? Clear names? One job each? A traceback arrow points to a line number. Two function cards: next_x gets a check, thing2 gets a question mark. Three bug badges: onkey(go_left()), no listen(), no ontimer. A sticky note fills with two stars and a wish; Nova reads it, smiles and taps a pencil. **On screen:** Does it run? • Clear names? • One job?; Hunt: (), listen(), ontimer; Two stars and a wish; The makers decide | Model asking before touching a partner's keyboard and kind facial expressions. The feedback is about the code, never the person. |
| 3:40–4:35 | **Recap, fair teamwork, and handoff** | Studio day complete! Let's remember. Plan with pseudocode or a flowchart. Break the plan into functions. Build the skateboard, your core loop, before anything fancy. Now, teamwork. Write each function on a sticky note, and take turns choosing, like picking teams fairly. Share the fun jobs and the boring ones, and swap the keyboard on time. Put both nicknames in a comment on line one, and credit any code you remixed. Using someone's idea is fine. Hiding it is not. Your turn: make a paper prototype, finish your plan for M1, fill your task board, and build your core loop for M2. Small and working beats big and broken! | A task board with TO DO, DOING and DONE columns; sticky notes with function names move across as two hands take turns. Line 1 of a code panel reads # Made by Comet and Pixel, and a second comment reads # Movement code remixed from Dodge the Meteors. End on the milestone road with M1 and M2 lit. **On screen:** TO DO → DOING → DONE; # Made by Comet and Pixel; Credit remixed code; NEXT: Plan (M1) → Core loop (M2) | Nicknames only. End card includes the AI-voice disclosure and a five-second hold. |

**Lesson handoff:** Make a paper prototype of your screen and play it for one minute (every clap is one tick). Then finish your plan for Milestone M1: pseudocode or a flowchart with a loop, a yes/no decision, the data (a list, a dictionary and a file) and at least three function names. Put each function on a sticky note on a fair TO DO / DOING / DONE task board, build your core loop for Milestone M2, and swap seats for a partner code review: two stars and a wish.

**Curriculum evidence:**

- `2-intermediate/teaching-material/lessons/week10.tex`
- `2-intermediate/teaching-material/workbook/week10.tex`
- `2-intermediate/teaching-material/homework/week10.tex`
- `2-intermediate/project/project-brief.tex`
- `2-intermediate/project/project-teacher-guide.tex`
- `2-intermediate/project/starter/README.md`
- `2-intermediate/project/starter/game_template.py`
- `2-intermediate/project/starter/art_studio_template.py`
- `docs/SYLLABUS.md`
- `2-intermediate/teaching-material/teacher-guide.tex`

## Week 11: Project Studio 2: Test and Polish

- **Driving question:** How do we prove our project works, learn from playtesters, and make it work for everyone?
- **Planned runtime:** 4:35 (275 seconds)
- **Vocabulary:** playtest, normal case, edge case, accessibility, polish, bug list
- **Misconception to prevent:** pytest can tell whether a game looks nice or is fun, or tests should use the real high-score file (running them would overwrite the real high score).
- **Digital citizenship:** Accessibility review of our own game: colors come from the Okabe-Ito palette; nothing depends on color alone (good and bad things also differ in shape or size, or have a label); text is big enough (font size 16 or larger); the keys are explained on the screen; nothing flashes quickly (more than 3 times a second can hurt some people's eyes); and the game is not too fast to start, with a beginner setting or a slow first level.
- **Practice activity:** `2-intermediate/project/project-brief.tex`

### Instructional objectives

- Write at least three pytest tests, with normal and edge cases, for the team's own functions.
- Add a list, a dictionary and a file that saves and loads to the project (Milestone M3).
- Turn playtest feedback cards into a bug list marked MUST, SHOULD or COULD.
- Check the project for accessibility and make at least one improvement (Milestone M4).

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Studio hook** | Hi, coders! Next week is the Family Arcade, and Comet Catch works! Well, it works when Nova plays it. Pixel tries it for the very first time, presses space twice, and red text appears. ‘Also, I didn't know which keys to press,’ says Pixel. Uh-oh. How can we prove our game works, and make it fun for everyone? | A banner 'Family Arcade: next week'. Nova plays happily; then Pixel sits down, presses a space key cap twice, and a red traceback slides up in the Shell. Pixel looks around for instructions on the game screen; none are there. **On screen:** STUDIO MISSION: Test, playtest, polish; Works for Nova… works for everyone? | Keep the crash comic and low-stakes; Nova reacts with curiosity, not embarrassment. |
| 0:30–1:25 | **Explain test the brain, playtest the fun** | Here's the big idea: test the brain, playtest the fun. Your program has two kinds of functions. Logic functions are the brain. They take values in and give an answer back with return, so pytest can check them. Drawing functions are the paint. A computer can't tell if your comet looks nice, but a person can. Two tricks. One: keep the start-up code under if name equals main, so pytest can borrow your functions without starting the game. Two: give file functions the file name as a parameter. The game uses highscore dot t x t. The tests use test scores dot t x t, so tests never wipe your real score. | Two boxes: 'Logic = the brain' (next_x, touching, load_high_score) with an arrow to a pytest robot stamping PASSED; 'Drawing = the paint' (draw_star, show_score) with an arrow to a playtester holding a feedback card. Then the main guard line glows as a gate the game stays behind. Two file icons: highscore.txt with a game controller, test_scores.txt with a test tube. **On screen:** Logic = brain → pytest; Drawing = paint → playtesters; Start-up code under the main guard; Tests use test_scores.txt | Use the car-factory idea only if time allows in the edit. Keep both file icons clearly labeled with words. |
| 1:25–2:30 | **Worked example: save, load, and four tests** | Watch Nova add a file and tests. First, two recipe functions from the workbook: load high score and save high score. No file yet? Then the high score is zero, not a crash. Next, a new file in the same folder: test mygame dot p y. A normal case: next x of zero and one, double equals twenty. An edge case: next x of two hundred eighty and one, double equals two hundred eighty. The player stays on screen. A round trip: save forty-two in the test file, then load it and expect forty-two. And a missing file gives zero. Press F5. Four PASSED lines! Now Nova breaks next x on purpose, removing the clamp. FAILED: assert three hundred, double equals, two hundred eighty. The test caught it! Undo, run again: all PASSED. | Code panel types test_mygame.py: from mygame import load_high_score, next_x, save_high_score / def test_moves_right_normally(): assert next_x(0, 1) == 20 / def test_stops_at_the_right_edge(): assert next_x(280, 1) == 280 / def test_high_score_round_trip(): save then load 42 / def test_no_file_means_zero(). Output panel: four PASSED lines and '4 passed'. Then mygame.py's last line of next_x changes to 'return new_x'; output shows test_stops_at_the_right_edge FAILED and E assert 300 == 280. Cmd+Z undoes it; all PASSED again. **On screen:** assert next_x(280, 1) == 280; Round trip: save 42, load 42; Break it on purpose → FAILED; Undo → all PASSED | Use only the lesson's tested demo code (mygame.py and test_mygame.py). Never show Star Catcher's logic module, its tests, or the answer-key Art Studio or top-five code. |
| 2:30–3:40 | **Bug hunt: the playtest bug list** | Now the playtest swap. Teams play each other's project for four minutes and fill in feedback cards: I liked. I was confused when. A bug I saw: what I did, what happened, what I expected. One idea. Pixel's cards for Comet Catch say: ‘I pressed space twice and it crashed.’ ‘I didn't know which keys to use.’ ‘Add a rainbow comet!’ Nova turns the cards into a bug list. MUST means it crashes or you can't play. SHOULD means it's confusing. COULD is a nice idea. Pause and point: which gets fixed first? Yes, the crash! Nova reads the traceback and finds the line. If a bug lives in a logic function, write a test that shows it first. It fails. Fix the code. It passes. Now that test guards the bug forever. | A feedback card with four lines fills in. Three cards slide onto a bug-list table with columns What I did / What happened / What I expected / MUST-SHOULD-COULD; the crash row gets a MUST tag, the keys row SHOULD, the rainbow comet COULD. The traceback's last line and line number glow. A mini sequence: a new test card shows FAILED, a code edit, then PASSED with a shield icon. **On screen:** I liked • Confused when • Bug • Idea; What I did / happened / expected; MUST → SHOULD → COULD; Bug in logic? Test first, then fix | Keep feedback specific and kind; no one is laughed at. Do not show the crash's code fix. |
| 3:40–4:35 | **Recap, accessibility review, and handoff** | Great testing! Let's remember. pytest checks the brain, and playtesters check the fun. Test normal cases and edge cases, and give your tests their own file name. Now polish, so everyone can play. Use the color-blind-safe palette. Make good and bad things differ in shape or size, not color alone. Use text size sixteen or bigger, explain the keys on screen, and never flash more than three times a second. Start gently, with a slow first level. Your turn: reach M3. Add your list, dictionary and file, and write three tests until they all say PASSED. Then playtest, fix the top MUST bug on your list, and do the accessibility check for M4. | An accessibility checklist ticks itself: Okabe-Ito swatches with names; a circle comet and a square rock side by side; a size-16 'Score' label; an on-screen line '← → to move'; a crossed-out fast-flash icon; a slow-start speedometer. End on the milestone road with M3 and M4 lit. **On screen:** Shape or size, not color alone; Text 16+ • Keys on screen; No fast flashing • Gentle start; NEXT: M3 data + 3 tests → M4 polish | Do not animate any fast flashing, even as an example. End card includes the AI-voice disclosure and a five-second hold. |

**Lesson handoff:** Milestone M3: add your list, your dictionary and a file that saves and loads (the load_high_score and save_high_score recipe in workbook chapter 11), then write at least 3 tests of your own functions in test_mygame.py (or my_tests.py from the template) and press F5 until they all say PASSED; break your code on purpose once to see FAILED. Then do the playtest swap with feedback cards, turn them into a MUST / SHOULD / COULD bug list, fix the MUST lines first, and do the accessibility review and at least one change for Milestone M4 (someone playtested it, you fixed one thing they found, you did the accessibility check).

**Curriculum evidence:**

- `2-intermediate/teaching-material/lessons/week11.tex`
- `2-intermediate/teaching-material/workbook/week11.tex`
- `2-intermediate/teaching-material/homework/week11.tex`
- `2-intermediate/project/project-brief.tex`
- `2-intermediate/project/project-teacher-guide.tex`
- `2-intermediate/project/starter/README.md`
- `2-intermediate/project/starter/my_tests.py`
- `docs/SYLLABUS.md`
- `2-intermediate/teaching-material/teacher-guide.tex`

## Week 12: Showcase: The Family Arcade

- **Driving question:** How do we share what we built, explain how it works, and see how far we have come?
- **Planned runtime:** 4:35 (275 seconds)
- **Vocabulary:** showcase, pitch, design decision, gallery walk, version
- **Misconception to prevent:** A project must be finished and perfect before it can be shown, or the exit assessment is a test you can fail.
- **Digital citizenship:** Showcase safety: high-score files and saved designs use nicknames only (open highscore.txt and look); no real names, school names, addresses, ages or photos appear in the code, the window or the title. The showcase is for family: if someone wants to take a photo or video, film the screen, not faces, and ask everyone first. Nothing gets uploaded or posted anywhere without a parent deciding together with the student. You can be proud of your work and still keep yourself private.
- **Practice activity:** `2-intermediate/project/project-brief.tex`

### Instructional objectives

- Present the project in about one minute and explain one design decision and one piece of code.
- Give kind, specific feedback with two stars and a wish during the gallery walk.
- Show what you learned about files, tests, events and functions on the exit assessment.
- Explain how to share a project safely: family only, nicknames, no personal information on screen.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Showcase hook** | Hi, coders! Today the classroom becomes the Family Arcade. Every computer is a game or an art studio, and families walk from station to station to play. Nova's heart is thumping. ‘What if I forget what to say?’ Pixel beeps. ‘Do you explain every single line?’ No way! So what makes a great showcase? | Desks turn into glowing arcade stations, each with a folded project card showing a nickname. Cartoon family figures (no realistic faces) walk between stations. Nova paces with a pitch card; Pixel scrolls an endless code printout that piles up on the floor. **On screen:** FINAL MISSION: The Family Arcade; Short, clear, and proud | Warm celebration music, calm pace. Pause two seconds on the question. |
| 0:30–1:25 | **Explain code freeze and the one-minute pitch** | First, code freeze! No new features today. Only fixing a crash is allowed. Save a backup copy, too, just in case. A great pitch is short: about one minute. Answer four questions, in this order. One: what is it? Two: how does one part work? Pick one function, the loop, the list, the dictionary or the file, and say what goes in and what comes out. Three: one design decision. That's a choice you made on purpose, and why. Four: what next? Not finished? That's normal. Show what works, then say what you would add next. | A snowflake 'CODE FREEZE' stamp lands on the code panel; a backup file icon mygame-showcase.py appears beside the original. Four numbered pitch cards fill a one-minute strip: What is it? / How does one part work? / One design decision / What next? **On screen:** CODE FREEZE: save a backup; 1 What is it?  2 How does one part work?; 3 One design decision; 4 What next? | Do not show a strict per-second timer; keep the one-minute target flexible. |
| 1:25–2:30 | **Worked example: Nova's pitch** | Let's watch Nova's pitch. Pixel is the demo driver, playing the game. Nova is the explainer. ‘This is Comet Catch. You catch comets with a rocket.’ That's question one. ‘Our next x function gets the position and the direction, and returns the new position, but never off the screen. We have a test for that.’ That's how one part works: what goes in, and what comes out. ‘The comets are circles and the rocks are squares, so you can tell them apart even without color.’ That's a design decision. ‘Next, we would add a slow mode for beginners.’ Four questions, about a minute. Then the team takes one question. Partners, swap halfway so both of you speak! | Pixel plays a turtle game frame: a rocket at the bottom, circle comets and square rocks falling. As Nova speaks, each pitch card lights up in turn. For card two, a code spotlight shows only the next_x function name with 'in: x, direction' and 'out: new x' arrows, plus a small PASSED badge. For card three, circle and square shapes are shown in grayscale to prove they differ without color. **On screen:** next_x: position in, new position out; Circles vs squares: not color alone; Swap halfway so both speak | This pitch follows the workbook's Comet Catch example. Never show Star Catcher code or any team's full program. |
| 2:30–3:40 | **Demo and explain: exit assessment and gallery walk** | Before the party, one last challenge: the exit assessment. It's not a test you can fail. It's like the stats screen at the end of a video game level. It shows what you've unlocked so far: files, tests, events and functions. It's pencil and paper only, with no computer. Stuck? Skip that question and come back. Then comes the gallery walk. Visit every station and play each project for two or three minutes. Then leave a feedback card: two stars and a wish. That's two specific things that are good, and one kind idea. ‘The score text is big and clear’ helps more than ‘cool.’ Makers don't explain or defend during the walk. They just watch people play. Pause and think: why is watching quietly so useful? It's great playtest data! | A video-game stats screen labels unlocked badges: Files, Tests, Events, Functions. A pencil and paper card with a 'skip and come back' arrow. Then a top-down gallery map: dotted footsteps visit each station; at each one a feedback card fills in two stars and a wish. The maker stands quietly with a small notebook while visitors play. **On screen:** Exit assessment = your stats screen; Stuck? Skip it and come back; Two stars and a wish; Makers watch quietly | Do not show any exit-assessment questions or answers. Use cartoon visitors without realistic faces. |
| 3:40–4:35 | **Showcase safety, celebration, and handoff** | Level 2 complete! You saved data in files, proved your code with tests, built games with keys and timers, and turned a plan into a real project. Before guests play, do the safety check. Open your high-score file and look: nicknames only. No real names, schools, addresses, ages or photos, in the code, the window or the title. Photos? Film the screen, not faces, and ask first. Nothing is uploaded or posted without a parent deciding with you. Your turn: freeze your code, fill in your pitch card, and practice once with your partner. Later, write your reflection. Level 3, here you come! | Concept badges (files, tests, keys and timers, project) form a constellation. A safety checklist ticks: highscore.txt opens to show nickname lines only; a camera icon points at a screen, not a face; an upload arrow is crossed out with 'parent decides' beside it. End on the presentation card and a door labeled Level 3 opening. **On screen:** Nicknames only • Check highscore.txt; Film the screen, not faces; Nothing posted without a parent; NEXT: Pitch card + practice | Use category words, never realistic personal data. Warm music with room for applause. End card includes the AI-voice disclosure and a five-second hold. |

**Lesson handoff:** Code freeze: save a backup copy (File > Save as… mygame-showcase.py), fill in your presentation card in workbook chapter 12 (What is it? How does one part work? One design decision. What next?) and practice your one-minute pitch once with your partner. Then take the exit assessment (your stats screen, not pass or fail; pencil and paper, skip and come back), present at the Family Arcade, do the showcase safety check before guests play, leave two stars and a wish at every station in the gallery walk, and write your Level 2 reflection (homework 12).

**Curriculum evidence:**

- `2-intermediate/teaching-material/lessons/week12.tex`
- `2-intermediate/teaching-material/workbook/week12.tex`
- `2-intermediate/teaching-material/homework/week12.tex`
- `2-intermediate/project/project-brief.tex`
- `2-intermediate/project/project-teacher-guide.tex`
- `2-intermediate/project/starter/README.md`
- `docs/SYLLABUS.md`
- `2-intermediate/teaching-material/teacher-guide.tex`

## 4. Automated, adaptable regeneration pipeline

### Architecture

```text
Level 2 sources ──> SHA-256 change detector ──> curriculum analyst agent
(answers and tests excluded)                        │
                                                    v
tracked plan/spec <── deterministic gates <──> scriptwriter agent
       │                 ^                          │
       │                 └──── reviewer agent ──────┘
       v
scene cards / optional illustrations ──> voice provider ──> FFmpeg + captions
       │
       └──> ignored media output and paid-API cache; tracked manifest records curriculum inputs
```

The Python pipeline uses the OpenAI Agents SDK for a typed, traceable three-agent workflow. A curriculum analyst extracts only source-supported outcomes, vocabulary, examples, and safety points, and notes which examples are answers learners must find. A scriptwriter turns that brief into the video contract. Deterministic checks and a reviewer then score each draft; failures go back to the scriptwriter for at most two bounded revisions. Deterministic validators remain the final authority.

### Change and approval flow

1. `check` fingerprints the syllabus, teacher guide, weekly lesson, workbook, homework, public exercise files and project sources (never answers or tests). It names each changed file, per week.
2. A teacher reads the change. If the script still fits, `accept --week N` records the new fingerprints with no paid calls. Otherwise `generate --week N` sends only that week through the agent workflow and refreshes the spec, this plan and that week's fingerprints.
3. A teacher reviews the script and storyboard in the PR. Paid media generation never begins implicitly.
4. `render --voice-provider macos-say` makes a free offline draft (cards, draft voice, captions) for timing review. `render --approved` makes the production version with paid illustrations or narration. Rendering refuses scripts whose lessons have changed.
5. Generated media and API caches remain ignored. Scripts, evidence paths, configuration, and source hashes remain reviewable in Git.

### Commands

```bash
python3 -m venv .venv-videos
source .venv-videos/bin/activate
python -m pip install -r videos/requirements.txt
python -m videos.pipeline.cli check
python -m videos.pipeline.cli accept --week 7          # script still matches a changed lesson
python -m videos.pipeline.cli generate --week 7        # paid: rewrite the script with agents
python -m videos.pipeline.cli render --week 7 --voice-provider macos-say   # free draft
python -m videos.pipeline.cli render --week 7 --approved                   # paid production
```

`OPENAI_API_KEY` is required for agent, illustration, or OpenAI voice calls. `ffmpeg` and `ffprobe` are required for MP4 rendering. Production narration uses the Realtime API (`openai-realtime`), the documented replacement for the Speech API models that shut down on January 6, 2027; its transcript is compared with the script so a paraphrased read is rejected. The legacy `openai-speech` adapter remains available until that date.

### Automated quality gates

- Exactly one episode for each Level 1 week, in order, with stable slugs and scene ids.
- Runtime from 3:00 through 5:00, and every scene's narration within its 145-wpm budget.
- At least two objectives and 4–7 fully specified scenes per episode.
- Evidence files and the practice activity must be part of that week's fingerprinted material; answers and tests never are.
- At most four on-screen text items per scene, each short enough to read; US spelling.
- Human `--approved` gate before paid media calls; refusal to render stale scripts; no automatic publication.
- Caption track plus `.srt` and `.vtt` files timed to the measured narration, voice disclosure, accessible palette, and deterministic code/UI overlays.

### Maintainability decisions

- The JSON spec is the machine-readable source; this Markdown file is reproducible from it.
- Agent prompts and typed output contracts live in code, separate from curriculum content.
- Per-file fingerprints support incremental regeneration and show exactly what changed.
- Media providers are adapters in one registry. Replacing image or voice technology does not change the educational workflow.
- Paid images and narration are cached by their exact inputs, so re-rendering never pays twice.
- Agent traces carry level, week, and source digest metadata for review and troubleshooting.
- The system proposes updates; deterministic checks and a teacher review decide whether they ship.
