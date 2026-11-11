# Level 3 Teaching Video Production Plan

> **Status:** Reviewed scripts and an automated regeneration contract for all 12 Level 3 lessons.
> Audience: Children in Grades 4–5 (ages 9–11) who are complete beginners. Every episode is at most 4:55 long (the limit is 5:00).
> This file is generated from `videos/specs/level3.json`; edit the JSON, then run `python -m videos.pipeline.cli plan --level 3`.

## 1. Instructional and creative direction

- **Series:** Nova & Pixel's Code Quest
- **Audience:** Children in Grades 4–5 (ages 9–11) who are complete beginners
- **Frame:** 16:9, 1920×1080, 24 or 30 fps
- **Narration:** Warm, curious, inclusive, and clear at about 140–145 words per minute; friendly without sounding babyish
- **Visual language:** Bright modern 2D motion graphics, real Scratch or Thonny captures, deterministic code overlays, and a recurring mission map
- **Accessibility:** Closed captions (an MP4 caption track plus .srt and .vtt files), Okabe–Ito palette, high contrast, large readable type, no color-only clues, gentle motion, and no rapid flashing

### Recurring story world

Nova is an inventive ten-year-old coder. Pixel is a palm-sized helper robot who takes instructions very literally. Nova writes the code and Pixel runs it exactly as written, so when something goes wrong the two investigate together. Each week, the pair opens a new door in the Code Quest workshop by learning one idea, testing it, and repairing one friendly bug. Learners are invited to predict before the answer appears.

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

The scripts were written from the Level 3 (Advanced: Python projects, git, objects, algorithms, data and AI) syllabus, teacher guide, all 12 lesson plans, workbook and homework chapters, every exercise brief, starter and hint, and the final project materials, then checked line by line by a separate reviewer against the same sources and the answer keys.

Every code example shown or read aloud was run, and its output and error messages match what Python prints. Examples were chosen so that no video gives away the answer to an exercise, homework, exit ticket, checkpoint question or the project reference; the review replaced several examples that were too close.

Each script names the misconception it prevents, uses the level's own debugging routine and citizenship wording, and points learners to the lesson's first hands-on activity.

## 3. Episode scripts and storyboards

## Week 1: Save Points with Git

- **Driving question:** How can git give our code save points that we can go back to?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** git, repository (repo), commit, commit message, commit id, diff, Terminal
- **Misconception to prevent:** git add alone makes a save point, or deleting a committed file later also removes it from the history.
- **Digital citizenship:** History is public-ish: never commit secrets. Commit with a nickname and an @example.com email; never put passwords, real names, addresses, school names or photos of people in a repository. If a secret ever gets committed, tell a grown-up and change that password: deleting the file is not enough.
- **Practice activity:** `3-advanced/exercises/week01/ex-git-quest`

### Instructional objectives

- Explain that a commit is a save point with a message and a commit id.
- Make a commit in Terminal with git add and git commit -m, after setting a nickname with git config.
- Describe what git log, git diff and git restore do: look back, spot a change and undo a mistake.
- Explain why passwords, real names and other secrets never go into a commit history.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Welcome to Level 3! Nova is building a rocket game, and it finally works. ‘Let's add a giant laser!’ says Nova. Pixel runs it, exactly as written… and the whole game crashes. Uh-oh. Nova wants the working game back, but it's gone. In a video game, you'd just load a save point. Can code have save points too? | Workshop. A code panel shows a small rocket game running. Nova types one new line and Pixel presses Run; the panel shakes gently and a red error appears. Nova searches for an undo button. A video-game save icon floats up with a question mark, then freeze on a thinking bubble. **On screen:** MISSION: Give code save points; Pause: When would you want a save? | Three-second prediction pause. Use a soft comic boing for the crash, not a failure buzzer. |
| 0:30–1:25 | **Explain git, commits and the two-move save** | Good news: a program called git can help. Git takes snapshots of a folder. Each snapshot is a save point called a commit. Every commit has a message that says what changed, and a short code name: a commit id. Making a commit takes two moves, like taking a class photo. First, git add calls files into the photo. Then git commit presses the camera button and adds a caption. git log is the photo album. git diff is spot the difference between now and the last photo. And git restore puts a file back the way it was in the last photo. Pause and point: which command is the camera button? | A time arrow with commit dots: a1b ‘Start game’, c3d ‘Add hero’, e5f ‘Add jump’. Then a class-photo scene: file cards step into a frame (git add), a camera flash (git commit), and the photo drops into an album (git log). Finish on three labeled boxes, Your folder → Ready to save → History, with a dashed arrow back labeled git restore. **On screen:** commit = a save point; git add → git commit; log = album • diff = spot the difference; restore = reload the last save | Hold the final diagram for four seconds during the pause. Give each box a label and an icon, not color alone. |
| 1:25–2:30 | **Worked example: a nickname and a first commit** | Let's make Nova's first save point in Terminal. Terminal is a chat window with the computer: you type a command, press Return, and it answers. Nova makes a git-quest folder in Documents and goes inside with cd. Important: git writes your name into every save point, forever. So Nova types git config, dash dash global, user dot name, and a nickname: StarOwl. ‘Never my real name,’ says Nova. The email is pretend too: it ends in example dot com. Nova checks with git config user dot name: StarOwl. Then git init starts the save system. git add rocket dot py calls the file into the photo, and git commit dash m ‘Add rocket drawing’ snaps it. Now git log dash dash oneline shows one line: a commit id and the message. Your id will be different! | A Terminal panel. Commands type in one at a time: cd ~/Documents, mkdir git-quest, cd git-quest, the two git config lines, git config user.name (answer: StarOwl), git init, git add rocket.py, git commit -m "Add rocket drawing", git log --oneline. The answer line 3b8d2f1 (HEAD -> master) Add rocket drawing appears, and a first commit dot pops onto the timeline. Nova gives Pixel a thumbs-up. **On screen:** git config --global user.name "StarOwl"; git add rocket.py; git commit -m "Add rocket drawing"; git log --oneline | Show the email line exactly as git config --global user.email "starowl@example.com". The commit id is illustrative; add a small caption that master may say main. Do not use hero_badge.py or the Git Quest's own commit messages. |
| 2:30–3:35 | **Friendly bug hunt: the wrong file and an unhelpful message** | Bug hunt! Nova adds a smoke trail to the rocket and wants to save. Nova types git add rocket dot py, then git add diary dot txt, and is about to commit with the message ‘things’. Wait! First, let's check git status. Changes to be committed: diary dot txt and rocket dot py. Nova's diary has a real name and an address in it. That's the wrong file! And does ‘things’ say what changed? Let's be detectives: read the clue, find the line, guess, and test one change. Fix one: git restore dash dash staged diary dot txt takes the diary out of the photo before it's taken. Check git status again: only rocket dot py is ready to save. Fix two: a message that says what changed, like ‘Add rocket smoke trail’. Nice catch! | Terminal panel. The two git add lines type in; Nova's hand hovers before a commit, then git status runs instead. Its output appears under ‘Changes to be committed:’ with ‘new file: diary.txt’ then ‘modified: rocket.py’ (git lists them A to Z); a magnifying glass highlights diary.txt and a sticky note shows a blurred name and address. The diary card steps out of the photo frame. The second git status shows only ‘modified: rocket.py’ under ‘Changes to be committed:’, with diary.txt moved down to ‘Untracked files:’. A message card crosses out ‘things’ and writes ‘Add rocket smoke trail’. A check mark appears only after the second git status. **On screen:** Run git status before every commit; git restore --staged diary.txt; Say WHAT changed in the message | Leave four seconds for prediction. Do not show the lesson's messy-history board (asdf, stuff, passwords.txt) or the homework's message makeover examples. The blurred diary text must not show any readable name or address. |
| 3:35–4:30 | **Recap, never commit secrets, and handoff** | Save point unlocked! Let's remember. A commit is a save point with a message and an id. First git add, then git commit. git log is the album, git diff spots the difference, and git restore reloads the last save. And remember: history is public-ish. Git remembers everything, even files you delete later. So commit with a nickname and an example dot com email. Never commit passwords, real names, addresses, school names or photos of people. If a secret ever gets committed, tell a grown-up. Now open The Git Quest. Follow its seven levels, from your first commit to a rescue with git restore. Can you get three commits with helpful messages? | Mission map: the first door opens. Recap icons for add, commit, log, diff and restore. A safe profile card reads ‘StarOwl, starowl@example.com’, beside crossed-out icons for a password, a house, a school and a photo. End card points to The Git Quest folder. **On screen:** add → commit → log; Never commit secrets; NEXT: The Git Quest | End card includes ‘Narration uses an AI-generated voice’ and a five-second clean hold for teachers to pause. |

**Lesson handoff:** Open Exercise 1.1 The Git Quest and follow its 7 levels in Terminal: make Documents/git-quest, set a nickname with git config and check it, git init, commit hero_badge.py, change the badge and look at git diff, break the file on purpose and rescue it with git restore, then make a commit of your own. Done looks like git log --oneline showing 3 or more commits with helpful messages.

**Curriculum evidence:**

- `3-advanced/teaching-material/lessons/week01.tex`
- `3-advanced/teaching-material/workbook/week01.tex`
- `3-advanced/teaching-material/homework/week01.tex`
- `3-advanced/exercises/week01/ex-commit-coach/README.md`
- `3-advanced/exercises/week01/ex-commit-coach/hints.md`
- `3-advanced/exercises/week01/ex-commit-coach/starter.py`
- `3-advanced/exercises/week01/ex-git-quest/README.md`
- `3-advanced/exercises/week01/ex-git-quest/hints.md`
- `3-advanced/exercises/week01/ex-log-reader/README.md`
- `3-advanced/exercises/week01/ex-log-reader/hints.md`
- `3-advanced/exercises/week01/ex-log-reader/starter.py`
- `3-advanced/exercises/week01/hw-inventory-review/README.md`
- `3-advanced/exercises/week01/hw-inventory-review/hints.md`
- `3-advanced/exercises/week01/hw-inventory-review/starter.py`
- `docs/SYLLABUS.md`
- `3-advanced/teaching-material/teacher-guide.tex`

## Week 2: Blueprints and Objects

- **Driving question:** How can one class build many objects that each keep their own data?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** class, object, attribute, method, __init__, self
- **Misconception to prevent:** Changing one object changes every object made from the same class, or the class itself is the object.
- **Digital citizenship:** Designing virtual pets kindly: our pets never get sick, run away or make you feel guilty, and never need money or daily streaks. Good games are fun because you want to play, not because they make you feel guilty. Ask: is this fair and kind to the player? Programmers choose how their games treat people.
- **Practice activity:** `3-advanced/exercises/week02/ex-pet-class`

### Instructional objectives

- Explain that a class is a blueprint and an object is one thing built from it.
- Read a class with __init__, attributes and a method, and make two objects from it.
- Explain what self means and fix a method that forgets it.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Nova wants a garden game with lots and lots of plants. ‘I'll write the code for one plant,’ says Nova, ‘then copy it… and copy it… and copy it.’ Nova starts copying. Fifty copies later, Nova wants plants to grow faster. Uh-oh. That's fifty changes! Can we write the plan once and build as many plants as we like? | Code panel fills with copy after copy of the same plant code while Nova's typing hands blur and Pixel watches. A counter ticks to 50. Nova holds up a pencil to change one line and gasps at the scrolling wall of copies. Freeze on a thinking bubble. **On screen:** MISSION: One plan, many plants; Pause: How could we avoid 50 copies? | Three-second prediction pause. Keep the copy wall readable as a pattern, not tiny text. |
| 0:30–1:25 | **Explain class, object, attribute, method and __init__** | We can! Think of a cookie cutter. One cutter makes lots of cookies, and each cookie can have its own sprinkles and flavor. In Python, the cutter is a class: a blueprint. Each cookie is an object: one thing built from the blueprint. The facts an object remembers are called attributes, like a plant's height. The actions it can do are methods: functions that live inside the class. The setup method has a funny name: dunder init. That's two underscores, init, two underscores. It runs once, every time a new object is made. Pause and point: is the cookie cutter the class or the object? | A star-shaped cookie cutter labeled ‘class’ stamps three cookies labeled ‘object’, each decorated differently. Each cookie flips to show fact cards (attributes). A blueprint card for Plant appears with an attributes section and a methods section, and the __init__ line glows with two underscores on each side. **On screen:** class = blueprint (cookie cutter); object = one thing built from it; attribute = a fact • method = an action; __init__ = setup (dunder init) | Show underscores clearly in a monospaced font. Hold four seconds on the question. |
| 1:25–2:30 | **Worked example: a Plant class and two objects** | Let's build a Plant class. Class Plant, colon. Inside, def dunder init, with self and name. It saves self dot name and sets self dot height to one. Then a method: def water, with self. It says self dot height equals self dot height plus three. So what's self? Self means ‘my.’ Self dot height means ‘my height.’ And Python fills in self for you. Now Nova makes two plants: sunny equals Plant ‘Sunny’, and fern equals Plant ‘Fern’. Pixel runs sunny dot water. Predict! How tall is Sunny now? Four. And Fern? Still one! Nothing happened to Fern. Watering Sunny only changed Sunny. Same blueprint, different objects, and each one keeps its own numbers. | Code panel: class Plant: / def __init__(self, name): / self.name = name / self.height = 1 / def water(self): / self.height = self.height + 3 / sunny = Plant("Sunny") / fern = Plant("Fern") / sunny.water(). A blueprint card produces two object cards, Sunny and Fern, both height 1. When sunny.water() runs, only Sunny's card ticks to 4 and its sprout grows; Fern's card stays at 1. **On screen:** self means “my”; sunny.height → 4; fern.height → 1 | Pause three seconds after ‘Predict!’. Do not use the Pet class, Pip and Bo, or the exit-ticket question. |
| 2:30–3:35 | **Friendly bug hunt: forgot self** | Bug hunt! Nova writes a new version of water, but forgets something. def water, with empty parentheses. Inside: height equals height plus three. Pixel runs sunny dot water, and gets a red error. Let's read it from the bottom up. TypeError: Plant dot water takes zero positional arguments but one was given. Hmm. Python tried to hand the plant to the method, but there was no self to catch it! Guess, and test one change: put self in the parentheses. Run again. A new error: UnboundLocalError. Ask: whose height? Not the plant's! Change one more thing: write self dot height on both sides. Run it. Sunny grows! Every method needs self first. | Code panel shows def water(): with an empty pair of parentheses glowing. A Shell panel shows the red error; a pointer starts at the bottom line. Pixel holds out a plant card to a method that has no hands to catch it. After the first fix, a second red error appears; a speech bubble asks ‘Whose height?’ and both height words gain self. in front. The rerun shows Sunny's sprout growing, then a check mark. **On screen:** def water():   # forgot self!; TypeError: ... 0 positional arguments; Whose height? → self.height; Read → find the line → guess → test | Real wording: ‘TypeError: Plant.water() takes 0 positional arguments but 1 was given’. Do not show Pet.play or happiness (the lesson's bug-hunt station). Allow four seconds for each prediction. |
| 3:35–4:30 | **Recap, kind pet design, and handoff** | Blueprint built! A class is a blueprint. Objects are the things you build from it, and each one keeps its own attributes. Methods are actions, and self means ‘my.’ Now, a design question. Some pet apps say, ‘Your pet is sad. You forgot it!’ How does that make players feel? Our pets never get sick, never run away, and never make you feel guilty. They never need money or daily streaks, either. Programmers choose how their games treat people. Now open Pet Class. Finish play, mood and describe. Then press Run and play with Pip. Does Bo change too? Find out! | Mission map: the second door opens. Recap icons: blueprint, two object cards, an action arrow. A gentle virtual pet waves next to a crossed-out guilt-trip pop-up and a crossed-out coin and calendar streak. End card points to the Pet Class folder. **On screen:** class → many objects; self means “my”; Kind design: fun, not guilt; NEXT: Pet Class | End card includes ‘Narration uses an AI-generated voice’ and a five-second clean hold for teachers to pause. |

**Lesson handoff:** Open Exercise 2.1 Pet Class: __init__ and feed are done. Finish play, mood and describe, then press Run, type p a few times and then f, and watch Pip change while Bo stays the same. Check with check_my_work.py.

**Curriculum evidence:**

- `3-advanced/teaching-material/lessons/week02.tex`
- `3-advanced/teaching-material/workbook/week02.tex`
- `3-advanced/teaching-material/homework/week02.tex`
- `3-advanced/exercises/week02/ex-bubble-art/README.md`
- `3-advanced/exercises/week02/ex-bubble-art/hints.md`
- `3-advanced/exercises/week02/ex-bubble-art/starter.py`
- `3-advanced/exercises/week02/ex-pet-class/README.md`
- `3-advanced/exercises/week02/ex-pet-class/hints.md`
- `3-advanced/exercises/week02/ex-pet-class/starter.py`
- `3-advanced/exercises/week02/hw-coin-purse/README.md`
- `3-advanced/exercises/week02/hw-coin-purse/hints.md`
- `3-advanced/exercises/week02/hw-coin-purse/starter.py`
- `docs/SYLLABUS.md`
- `3-advanced/teaching-material/teacher-guide.tex`

## Week 3: Families of Objects

- **Driving question:** How can classes share code in families, and how can objects be built from other objects?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** inheritance, parent class, child class, override, super(), polymorphism, composition
- **Misconception to prevent:** A child class must copy all of its parent's code, or a misspelled method name still replaces the parent's method.
- **Digital citizenship:** Representation: who gets to be the hero? Designing a character family is a chance to include many kinds of people: different names, skin tones, ages and abilities. Avoid making one group always the villain or always the helper.
- **Practice activity:** `3-advanced/exercises/week03/ex-enemy-family`

### Instructional objectives

- Explain how a child class inherits from a parent and uses super().__init__ to reuse the parent's setup.
- Override a method so different classes react differently to the same call.
- Tell inheritance (is a) from composition (has a) by saying the sentence aloud.
- Find a missing super().__init__ call and a misspelled override.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Nova's robot workshop is growing. There's a plain Robot that rolls one step at a time. Now Nova wants a PaintBot that rolls and paints, and lots more kinds after that. ‘Do I have to copy the whole Robot class every time?’ asks Nova. Pixel holds up a family tree. What if robots could have families? | Workshop floor with one plain robot rolling a step. Nova sketches more robot kinds on a whiteboard, looking worried at a tall stack of copied code. Pixel unrolls a family-tree poster. Freeze on the poster. **On screen:** MISSION: A family of robots; Pause: What do all robots share? | Three-second prediction pause. |
| 0:30–1:25 | **Explain inheritance, overriding, super() and composition** | They can! A child class inherits everything from its parent class: all its attributes and methods. Then it changes only what is different. Think of Grandma's pancake recipe. Your recipe says: make Grandma's pancakes, then add blueberries. You don't copy her whole recipe. You use it and add one thing. Changing a method in the child is called overriding. And super means ‘my parent.’ One more way to build: a Workshop isn't a kind of Robot, but a Workshop has Robots. That's composition. Say the sentence aloud. Is a means inheritance. Has a means composition. | A family tree of classes: a Robot parent card at the top (name, x, move) with is-a arrows from two child cards, PaintBot (adds color) and a blank card with a question mark. A recipe card ‘Grandma's pancakes’ gets a sticky note ‘+ blueberries’. Then a Workshop box opens to show robot cards inside it, labeled has a. **On screen:** class PaintBot(Robot):  → is a; super() = “my parent”; is a → inheritance; has a → composition | Use arrows with an open triangle head for is a and a containing box for has a, so the two ideas differ by shape as well as label. |
| 1:25–2:30 | **Worked example: a PaintBot is a Robot** | Here's the parent: class Robot. Its setup saves a name and an x position, and move adds one to x. Now the child: class PaintBot, with Robot in parentheses. That means a PaintBot is a Robot. PaintBot's setup calls super dot dunder init with name and x. ‘Parent, set up your part!’ says Nova. Then the child adds its extra: a color. PaintBot also overrides move. First, super dot move does the parent's step. Then it adds its own part: a paint message. Nova makes juno equals PaintBot ‘Juno’, with color green. Pixel runs juno dot move. Predict! x becomes one, and it prints: Juno paints a green dot. A plain Robot and a PaintBot both understand move, but each does it its own way. That's polymorphism: many shapes. | Code panel: class Robot: with __init__(self, name, x=0) saving self.name and self.x, and move adding 1 to self.x; class PaintBot(Robot): with __init__(self, name, x=0, color="blue") calling super().__init__(name, x) then self.color = color, and move calling super().move() then print(self.name, "paints a", self.color, "dot"). Below: juno = PaintBot("Juno", color="green") and juno.move(). Shell shows Juno paints a green dot. A plain robot and Juno roll side by side; only Juno leaves a green dot. **On screen:** super().__init__(name, x); super().move(); Shell: Juno paints a green dot; polymorphism = many shapes | Highlight each super line as it is read. Do not show Sprinter, Zigzagger, Hero or Owl code (exercise, workbook and homework). |
| 2:30–3:35 | **Friendly bug hunt: missing super().__init__ and an override typo** | Bug hunt! Nova makes a quick copy of PaintBot, and it has two family bugs. Bug one: the child's setup forgot the super dunder init line. It only saves the color. Pixel runs juno dot move and gets AttributeError: ‘PaintBot’ object has no attribute ‘x’. Read it from the bottom up. No x? The parent's setup never ran! Test one change: put the super line back. Run again. No crash! But wait… Juno rolls and never paints. No error at all. That's a silent bug. Look closely at the method's name: m, o, o, v, e. Moove! That doesn't match, so Python used the parent's move. Fix the spelling and test. Override names must match exactly. | Code panel of the buggy copy: __init__ with only self.color = color, and def moove(self):. A red AttributeError appears in the Shell; a pointer reads it from the bottom. The family tree shows the Robot setup box grayed out. After the fix, Juno rolls without painting; a magnifier spells m-o-o-v-e letter by letter beside the parent's m-o-v-e. After the spelling fix, Juno paints a green dot and a check mark appears. **On screen:** AttributeError: ... no attribute 'x'; def moove(self):   # silent bug!; Override names must match exactly | Real wording: ‘AttributeError: 'PaintBot' object has no attribute 'x'’ (super().move() reads self.x first). Do not use the lesson's Sprinter/mvoe station, Hexagon, or Diamond/drow (Week 6 Bug Hunt 4). Allow four seconds for each prediction. |
| 3:35–4:30 | **Recap, representation, and handoff** | Family reunion! A child class inherits from its parent and changes only what is different. super runs the parent's part. Overriding replaces a method, so the same call can do different things. That's polymorphism. And has a means composition. Now, a question for game makers: who gets to be the hero? When you design a character family, include many kinds of people: different names, skin tones, ages and abilities. Don't make one group always the villain or always the helper. Now open Enemy Family. Finish the Zigzagger, the Sprinter and move all. Then press Run. Does every enemy move its own way? | Mission map: the third door opens. Recap icons: family tree, a super arrow pointing up, a workshop box. A line-up of diverse, friendly game heroes of different ages, skin tones and abilities. End card points to the Enemy Family folder. **On screen:** Child(Parent) • super() • override; Heroes of every kind; NEXT: Enemy Family | End card includes ‘Narration uses an AI-generated voice’ and a five-second clean hold for teachers to pause. |

**Lesson handoff:** Open Exercise 3.1 Enemy Family: read Enemy and Guard first, then finish Zigzagger.move (use super().move()), Sprinter.__init__ (use super().__init__), Sprinter.move and move_all. Run prints 4 turns, and check_my_work.py passes.

**Curriculum evidence:**

- `3-advanced/teaching-material/lessons/week03.tex`
- `3-advanced/teaching-material/workbook/week03.tex`
- `3-advanced/teaching-material/homework/week03.tex`
- `3-advanced/exercises/week03/ex-enemy-family/README.md`
- `3-advanced/exercises/week03/ex-enemy-family/hints.md`
- `3-advanced/exercises/week03/ex-enemy-family/starter.py`
- `3-advanced/exercises/week03/ex-game-roster/README.md`
- `3-advanced/exercises/week03/ex-game-roster/hints.md`
- `3-advanced/exercises/week03/ex-game-roster/starter.py`
- `3-advanced/exercises/week03/ex-shape-family/README.md`
- `3-advanced/exercises/week03/ex-shape-family/hints.md`
- `3-advanced/exercises/week03/ex-shape-family/starter.py`
- `3-advanced/exercises/week03/hw-hero-party/README.md`
- `3-advanced/exercises/week03/hw-hero-party/hints.md`
- `3-advanced/exercises/week03/hw-hero-party/starter.py`
- `docs/SYLLABUS.md`
- `3-advanced/teaching-material/teacher-guide.tex`

## Week 4: Searching: How Fast Is Fast?

- **Driving question:** How can a smart search do less work than checking one by one?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** algorithm, linear search, binary search, sorted, worst case, off-by-one error
- **Misconception to prevent:** Binary search works on any list, or a list ten times bigger needs ten times more binary search steps.
- **Digital citizenship:** Search engines and filter bubbles: a search engine ranks results, putting first what it thinks you want based on what you clicked before, so two people can search the same words and see different answers. To get out of a bubble, use different search words, look at several sources, ask a grown-up or a librarian, and notice when something is an ad.
- **Practice activity:** `3-advanced/exercises/week04/ex-search-race`

### Instructional objectives

- Explain linear search and binary search, and why binary search needs a sorted list.
- Trace a binary search with low, high and mid.
- Count worst-case binary search steps by halving again and again.
- Find and fix an off-by-one bug in a binary search.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Pixel has a row of number cards, face down, sorted from smallest to largest. ‘Find the 40!’ says Nova. Pixel flips the first card. Then the next. Then the next. Flip, flip, flip… seven flips! ‘There has to be a faster way,’ says Nova. Can you find a number with fewer flips? | Seven face-down cards in a row on the workbench. Pixel flips them one at a time from the left while a flip counter ticks up to 7; the last card shows 40. Nova taps a stopwatch. Freeze on a thinking bubble. **On screen:** MISSION: Find it in fewer flips; Pause: Which card would you flip first? | Three-second prediction pause. Card numbers stay hidden until flipped. |
| 0:30–1:25 | **Explain linear search, binary search and the worst case** | Pixel just did a linear search: check the items one by one, from the start. It works on any list, but a long list means a long search. Binary search is smarter. Look at the middle card. If it's too small, the answer must be on the right, so throw away the whole left half. Then check the middle of what's left. Every step cuts the list in half. But there's one rule: the list must be sorted. To compare algorithms, we count the steps in the worst case: the unluckiest search. It's like finding a word in a dictionary. You open it in the middle, not on page one! | Left side: a pointer walks card by card (linear). Right side: a pointer jumps to the middle card, the left half fades to gray, then it jumps to the middle of what is left. A shuffled row appears with a ‘not sorted’ stop sign. A dictionary opens in the middle. **On screen:** Linear: check one by one; Binary: check the middle, halve; Binary search needs a sorted list | Gray thrown-away cards also get a dashed outline so they do not rely on color alone. |
| 1:25–2:30 | **Worked example: trace a binary search** | Let's trace it. Seven cards: 4, 9, 12, 18, 25, 31, 40. Their places are zero to six. We're looking for 40. Low is zero and high is six. The middle place, mid, is three: add low and high, halve it, and round down. Card three is 18. Too small! So low jumps to four. Now mid is five: card 31. Still too small, so low jumps to six. Now low and high are both six, and there's still one card left to check. Mid is six: 40. Found it! Three steps instead of seven. How many steps for fifty cards? Halve again and again: 50, 25, 12, 6, 3, 1. That's six numbers, so six steps at most. | The seven cards face up with places 0 to 6 underneath. Pointer cards labeled low, high and mid slide along. A trace table fills one row per step (low, high, mid, card, so…). Thrown-away cards gray out with a dashed outline. Then a halving ladder of number blocks shrinks: 50, 25, 12, 6, 3, 1, counted with ticks. **On screen:** low 0 • high 6 • mid 3 → 18 too small; mid 5 → 31 too small; mid 6 → 40 found! 3 steps; 50, 25, 12, 6, 3, 1 → 6 steps | Do not use the workbook list [3, 8, 15, 21, 29, 37, 44, 52], the homework list [1, 3, 5, 7, 9, 11, 13], the secret number 73, or the 1000, 10000 and 1,000,000 halvings (exit ticket, exercise and homework predictions). Do not show the binary_search code. |
| 2:30–3:35 | **Friendly bug hunt: an off-by-one that loops forever** | Bug hunt! Nova writes a binary search, but one line is off by one. When the middle card is too small, it says: low equals mid. Pixel searches for 18 in four cards: 4, 9, 12, 18. Mid is one: 9. Too small, so low becomes one. Mid is two: 12. Too small, so low becomes two. Mid is two again: 12. And again. And again! Pixel is stuck in a loop forever. In Thonny, press the red Stop button. Now let's guess. We already checked the middle card, and it was too small, so we should throw it away too. Test one change: low equals mid plus one. Run it. Found 18! An off-by-one bug is a number that's one too big or one too small. | Code panel highlights the single line low = mid. Four cards with places 0 to 3; the mid pointer lands on 12 again and again while Pixel spins in a little circle and a loop counter climbs. A finger presses Thonny's red Stop button. The line changes to low = mid + 1; the rerun lands on 18 with a check mark. **On screen:** low = mid   # bug!; mid 2 → 12… mid 2 → 12… forever!; Throw away mid too: low = mid + 1 | Use this ‘low = mid’ bug only. Do not show while low < high or high = len(items): they are the lesson's bug-hunt station and Week 6 Bug Hunt 3. Allow four seconds for prediction before the fix. |
| 3:35–4:30 | **Recap, filter bubbles, and handoff** | Search solved! Linear search checks one by one. Binary search checks the middle and throws away half, but only on a sorted list. Bigger lists need only a few more binary steps. Search engines are super fast, but they also rank the results, putting first what they think you want, based on what you clicked before. So two people can search the same words and see different answers. That's a filter bubble. To get out, try different search words, look at several sources, and ask a grown-up or a librarian. Now open Search Race. Write binary search, and predict its steps for ten thousand items before you run it! | Mission map: the fourth door opens. Recap icons: a walking pointer and a halving pointer. Two kids type the same search words and get different result cards inside two soap bubbles; the bubbles pop as new sources and a librarian icon appear. End card points to the Search Race folder. **On screen:** Sorted list → check the middle → halve; Pop the filter bubble; NEXT: Search Race | End card includes ‘Narration uses an AI-generated voice’ and a five-second clean hold for teachers to pause. Do not state the step count the program reports for 10000 items. |

**Lesson handoff:** Open Exercise 4.1 Search Race: linear_search is done. Write binary_search so it returns (index, steps), predict the binary steps for 10000 items with a halving ladder, then Run to see the race table and check with check_my_work.py.

**Curriculum evidence:**

- `3-advanced/teaching-material/lessons/week04.tex`
- `3-advanced/teaching-material/workbook/week04.tex`
- `3-advanced/teaching-material/homework/week04.tex`
- `3-advanced/exercises/week04/ex-guess-bot/README.md`
- `3-advanced/exercises/week04/ex-guess-bot/hints.md`
- `3-advanced/exercises/week04/ex-guess-bot/starter.py`
- `3-advanced/exercises/week04/ex-search-race/README.md`
- `3-advanced/exercises/week04/ex-search-race/hints.md`
- `3-advanced/exercises/week04/ex-search-race/starter.py`
- `3-advanced/exercises/week04/hw-growth-table/README.md`
- `3-advanced/exercises/week04/hw-growth-table/hints.md`
- `3-advanced/exercises/week04/hw-growth-table/starter.py`
- `docs/SYLLABUS.md`
- `3-advanced/teaching-material/teacher-guide.tex`

## Week 5: Sorting, Stacks and Queues

- **Driving question:** How do sorts put data in order, and when do we use a stack or a queue?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** sort, swap, key function, stack, queue, deque
- **Misconception to prevent:** Writing a = b and then b = a swaps two values, or two sorts do the same amount of work because they give the same answer.
- **Digital citizenship:** Leaderboards: fair and kind. Show nicknames only, never real names; give ties the same place; show personal bests and most improved, not only the winners; let players choose not to appear. A leaderboard should make people want to play again, not feel bad.
- **Practice activity:** `3-advanced/exercises/week05/ex-sort-race`

### Instructional objectives

- Trace bubble sort and selection sort on four cards and count their swaps.
- Explain a stack as last in, first out and a queue as first in, first out.
- Swap two values without losing one, and spot a sort that loses items.
- Suggest ways to make a leaderboard fair and kind.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Nova's game needs three things: a high-score board in order, an undo button, and a fair way to take turns. Pixel stares at a messy pile of score cards and blinks. ‘Where do I even start?’ beeps Pixel. Today we'll sort cards, stack plates and line up for lunch. Ready? Let's go! | Nova's to-do board shows three sticky notes with icons: a trophy board, an undo arrow, and a line of players. Pixel looks at a messy heap of number cards. A stack of plates and a lunch line slide in at the edges. **On screen:** MISSION: Sort it, undo it, take turns | Keep the hook light and quick; no prediction pause needed. |
| 0:30–1:25 | **Explain two sorts, a stack and a queue** | Sorting means putting things in order, like smallest to largest. Here are two ways. Selection sort finds the smallest card and swaps it to the front. Then it finds the smallest of the rest, and so on. Bubble sort compares two neighbors. If the left one is bigger, they swap. Big cards bubble to the end, like bubbles rising in a drink. Both sorts give the same answer, but they do different amounts of work. Two more helpers. A stack is a pile of plates: last in, first out, just like undo. A queue is a lunch line: first in, first out, so everyone gets a fair turn. | Number cards demonstrate each rule: a spotlight finds the smallest card and it swaps to the front; then two neighbor cards compare and swap as a bubble floats up. A plate is pushed onto a stack and the top one popped off, with an undo arrow. A short lunch line: someone joins at the back and the front person leaves. **On screen:** Selection: smallest to the front; Bubble: neighbors swap; Stack: last in, first out; Queue: first in, first out | Label push, pop, front and back with words and arrows, not color alone. |
| 1:25–2:30 | **Worked example: race two sorts on four cards** | Let's race on four cards: 6, 9, 2, 4. Bubble sort first. Compare 6 and 9: keep. 9 and 2: swap. 9 and 4: swap. After pass one, 9 has bubbled to the end. Pass two: 6 and 2, swap. 6 and 4, swap. Now 6 is in place too. Pass three: 2 and 4, keep. Sorted: 2, 4, 6, 9. That's four swaps. Now selection sort, on the same cards. The smallest is 2, so it swaps with 6. One swap. The next smallest is 4, so it swaps with 9. Then 6 is already in place. That's two swaps in all. Same answer, different amount of work! Pause and point: which sort swapped less? | Bars with numbers on them for 6, 9, 2, 4. Bubble sort: two neighbor bars glow, swap or stay, and a swap counter ticks; bars in their final place get a thick border. Then the same four bars reset for selection sort: a spotlight finds the smallest, swaps it to the front, and a second counter ticks. Both counters sit side by side at the end. **On screen:** Bubble: 6 9 2 4 → 2 4 6 9 (4 swaps); Selection: same cards (2 swaps); Same answer, different work | Do not use the lesson's 5, 2, 4, 1, the workbook's 4, 1, 3, 2, the mid-level checkpoint's 7, 3, 9, 1, or the exercise cards [7, 3, 9, 1, 5, 3, 8, 2] and their swap counts. Do not show the bubble_sort code. |
| 2:30–3:35 | **Friendly bug hunt: the swap that loses an item** | Bug hunt! Nova wants two cards to trade places. Left is 9, and right is 4. Nova writes: left equals right. Then: right equals left. Pixel runs it and prints both: 4 and 4! Where did the 9 go? Let's act it out. The first line puts a 4 where the 9 was, and the 9 is gone. The second line just copies that 4 back. A sort with this swap loses items! Guess, and test one change: Python can swap both at once. left comma right equals right comma left. Run it: 4 and 9. Nothing lost! One more clue: if a high-score board shows the lowest score on top, check the order. For biggest first, sorted needs reverse equals True. | Two card slots labeled left and right holding 9 and 4. Line one: a 4 card drops onto the 9 slot and the 9 card puffs away; line two copies 4 into the right slot. The Shell prints 4 4. Pixel acts it out with two real cards. The fix line slides in and both cards cross paths at the same time; the Shell prints 4 9. Then a small score board flips from lowest-first to biggest-first when reverse=True is added. **On screen:** left = right / right = left → 4 4; left, right = right, left; Biggest first: reverse=True | Code: left = 9 / right = 4 / left = right / right = left / print(left, right) prints 4 4; with left, right = right, left it prints 4 9. Do not show the lesson's [5, 2] station, the result[i] swap, or the Week 6 Lost Scores bugs. Allow four seconds for prediction. |
| 3:35–4:30 | **Recap, fair leaderboards, and handoff** | Cards sorted! Selection sort swaps the smallest to the front. Bubble sort swaps neighbors. A stack is last in, first out, and a queue is first in, first out. Now let's talk about leaderboards. How would you feel if you were always at the bottom of a board everyone can see? A fair, kind board shows nicknames only, never real names. Ties share the same place. It celebrates personal bests and most improved, not only the winners. And players can choose not to appear. Now open Sort Race. Finish the swap inside bubble sort, run it, and write down how many swaps each sort makes. | Mission map: the fifth door opens. Recap icons: sorted bars, a plate stack, a lunch line. A friendly leaderboard with nicknames, two players sharing third place, and a ‘most improved’ star badge. End card points to the Sort Race folder. **On screen:** Sort • Stack • Queue; Nicknames • ties share • most improved; NEXT: Sort Race | End card includes ‘Narration uses an AI-generated voice’ and a five-second clean hold for teachers to pause. Use invented nicknames on the board, not the exercise's Ada, Leo, Mei, Omar and Zoe. |

**Lesson handoff:** Open Exercise 5.1 Sort Race: selection_sort is done. Finish the swap inside bubble_sort and count each swap, then Run it to sort the cards both ways, write down the swaps each sort reports, and check with check_my_work.py.

**Curriculum evidence:**

- `3-advanced/teaching-material/lessons/week05.tex`
- `3-advanced/teaching-material/workbook/week05.tex`
- `3-advanced/teaching-material/homework/week05.tex`
- `3-advanced/exercises/week05/ex-leaderboard/README.md`
- `3-advanced/exercises/week05/ex-leaderboard/hints.md`
- `3-advanced/exercises/week05/ex-leaderboard/starter.py`
- `3-advanced/exercises/week05/ex-sort-race/README.md`
- `3-advanced/exercises/week05/ex-sort-race/hints.md`
- `3-advanced/exercises/week05/ex-sort-race/starter.py`
- `3-advanced/exercises/week05/ex-undo-paint/README.md`
- `3-advanced/exercises/week05/ex-undo-paint/hints.md`
- `3-advanced/exercises/week05/ex-undo-paint/starter.py`
- `3-advanced/exercises/week05/hw-turn-queue/README.md`
- `3-advanced/exercises/week05/hw-turn-queue/hints.md`
- `3-advanced/exercises/week05/hw-turn-queue/starter.py`
- `docs/SYLLABUS.md`
- `3-advanced/teaching-material/teacher-guide.tex`

## Week 6: Slow-Motion Debugging

- **Driving question:** How can the Thonny debugger help us watch our code think, one line at a time?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** debugger, step over, step into, breakpoint, traceback, trace table
- **Misconception to prevent:** Pressing Run shows what happens inside the code, or changing several lines at once is the fastest way to fix a bug.
- **Digital citizenship:** Growth mindset: bugs are how we learn. Every programmer meets bugs every day; celebrate effort and strategy, not speed. Asking for help with a clear description (what I expected, what happened, what I tried) is a skill, not a weakness, and being kind when a partner's code is broken is part of being a good teammate.
- **Practice activity:** `3-advanced/exercises/week06/ex-bug-missing-self`

### Instructional objectives

- Use Debug, Step over, Step into and the Variables view to follow a program one line at a time.
- Follow the bug-hunting loop: read, predict, watch, fix one thing, check.
- Connect the big ideas from weeks 1 to 5: save points, classes, families, searching and sorting.
- Describe a hard bug, what helped, and how to ask for help clearly.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Checkpoint week! Nova and Pixel look back at their quest map: save points, blueprints, families, searching and sorting. But today, Nova's code does something strange, and it happens too fast to see. ‘I wish I could slow it down,’ says Nova. What if you could watch your code think, one line at a time? | The mission map with five opened doors, each with an icon: a commit dot, a blueprint, a family tree, a halving pointer, sorted bars. A sixth door is marked with a magnifying glass. Nova's program flashes past in a blur, and a pause icon appears. **On screen:** MISSION: Watch the code think; Pause: Where could a bug hide? | Three-second prediction pause. |
| 0:30–1:25 | **Explain the Thonny debugger buttons** | You can, with a debugger. A debugger is a slow-motion replay for your code. It's like the replay of a soccer goal: you can pause on every frame and see where every player is. In Thonny, click Debug, the bug icon next to the green Run button. The first line lights up. The highlighted line is the one that runs next. Step over runs that line and stops at the next one. Step into goes inside a function call, so you can watch its lines too. Turn on View, then Variables, to see every variable's value right now. And Stop, the red sign, ends the program. | A soccer replay freezes on a frame with player labels. Then a clean Thonny toolbar: Run, Debug, Step over, Step into, Resume and Stop, each labeled under its icon as it is named. The highlight moves down a short program one line at a time, and the Variables panel opens with View > Variables. **On screen:** Debug = slow motion (bug icon); Step over: run this line, stop at next; Step into: go inside a function; View > Variables | Use an authentic current Thonny capture with labels as overlays outside it. Mention on screen that the toolbar buttons work on every Mac, even when the F-keys need fn. |
| 1:25–2:30 | **Worked example: step into a method** | Let's try it on a tiny Robot class. Its setup gives every robot a battery of fifty, and charge adds some power. At the bottom, Nova makes bolt and calls bolt dot charge twenty-five. Nova clicks Debug, and the first line lights up. Step over, step over… In the Variables view, bolt appears. Click it, and the Object inspector shows its attributes: battery is fifty. Now the highlighted line calls charge, one of our own methods. So Nova clicks Step into. A small window opens. That's normal: it shows the method's own variables, like power, which is twenty-five. Step over once more, and battery becomes seventy-five. Back outside, print shows 75. We watched every step! | Code panel: class Robot: / def __init__(self, name): / self.name = name / self.battery = 50 / def charge(self, power): / self.battery = self.battery + power / bolt = Robot("Bolt") / bolt.charge(25) / print(bolt.battery). A highlight bar walks down the lines. The Variables panel shows bolt; the Object inspector shows battery 50. On Step into, a small method window opens showing power 25; battery ticks to 75. The Shell prints 75. Pixel watches with a tiny replay remote. **On screen:** bolt.battery → 50; Step into: inside charge(25); power 25 → battery 75; Shell: 75 | Turn on View > Variables and View > Object inspector before recording. Do not use ScoreKeeper, undo_last or PiggyBank code (Bug Hunt 1 and Homework 6), or their numbers 10, 5 and 15 and the parameter name amount (the deposit fix). |
| 2:30–3:35 | **Friendly bug hunt: the total that keeps resetting** | Bug-hunt workshop! Nova wants to add up coins: 3, 4 and 5 should make 12. But the program prints 5. There's no red error this time, so let's use the bug-hunting loop. One, read: we expected 12, but got 5. Two, predict: ‘I think the total line is wrong,’ says Nova. Three, watch: click Debug and step over. Total becomes 3, then jumps back to zero, then 4. Then zero again! Aha! The line total equals zero is inside the loop, so it runs every time. Four, fix one thing: move that line above the loop. Five, check: run it. 12! If it's still failing, go around the loop again. Nice catch! | Code panel: for coin in [3, 4, 5]: / total = 0 / total = total + coin / print(total) (print is not indented, so it runs once after the loop). The Shell prints 5 next to an expected card saying 12. A five-step loop diagram (Read, Predict, Watch, Fix ONE thing, Check) lights up one step at a time. In the Variables panel, total flips 0, 3, 0, 4, 0, 5 like a scoreboard. The total = 0 line slides up above the for line; the rerun prints 12 and a check mark appears. **On screen:** 1 Read  2 Predict  3 Watch; 4 Fix ONE thing  5 Check; total = 0 is inside the loop! | Do not show any Week 6 bug-hunt station or Homework 6 bug (missing self, list copy, while condition, duplicates, high = len, low < high, missing call parentheses, super, drow, deposit, withdraw or statement). Allow four seconds for prediction. |
| 3:35–4:30 | **Recap, growth mindset, and handoff** | Checkpoint reached! A debugger is a slow-motion replay. Debug starts it, Step over runs one line, Step into goes inside your method, and the Variables view shows every value. When a bug appears: read, predict, watch, fix one thing, and check. Now, a secret: every programmer meets bugs every day. Bugs are how we learn! If you get stuck, ask for help clearly: what I expected, what happened, what I tried. That's a skill, not a weakness. And be kind when a partner's code is broken. Now open Bug Hunt 1, Score Keeper. Run it, read the last line of the error, and debug one fix at a time. Happy hunting! | Mission map: the sixth door opens. Recap icons for the debugger buttons and the five-step loop. Nova and Pixel high-five; a speech-bubble card reads ‘I expected…, but… happened. I tried…’. End card points to the Bug Hunt 1 folder. **On screen:** Read • Predict • Watch • Fix • Check; Bugs are how we learn; NEXT: Bug Hunt 1: Score Keeper | End card includes ‘Narration uses an AI-generated voice’ and a five-second clean hold for teachers to pause. Do not hint at the Score Keeper fixes. |

**Lesson handoff:** Open Bug Hunt 1: Score Keeper (three bugs, all the same kind). Press Run and read the last line of the red error, then use Debug, Step into and Step over with the Variables view; fix one bug, run again, and repeat until Run prints Comet has 10 points and check_my_work.py passes.

**Curriculum evidence:**

- `3-advanced/teaching-material/lessons/week06.tex`
- `3-advanced/teaching-material/workbook/week06.tex`
- `3-advanced/teaching-material/homework/week06.tex`
- `3-advanced/exercises/week06/ex-bug-binary-search/README.md`
- `3-advanced/exercises/week06/ex-bug-binary-search/hints.md`
- `3-advanced/exercises/week06/ex-bug-binary-search/starter.py`
- `3-advanced/exercises/week06/ex-bug-lost-items/README.md`
- `3-advanced/exercises/week06/ex-bug-lost-items/hints.md`
- `3-advanced/exercises/week06/ex-bug-lost-items/starter.py`
- `3-advanced/exercises/week06/ex-bug-missing-self/README.md`
- `3-advanced/exercises/week06/ex-bug-missing-self/hints.md`
- `3-advanced/exercises/week06/ex-bug-missing-self/starter.py`
- `3-advanced/exercises/week06/ex-bug-shape-party/README.md`
- `3-advanced/exercises/week06/ex-bug-shape-party/hints.md`
- `3-advanced/exercises/week06/ex-bug-shape-party/starter.py`
- `3-advanced/exercises/week06/hw-bug-bank/README.md`
- `3-advanced/exercises/week06/hw-bug-bank/hints.md`
- `3-advanced/exercises/week06/hw-bug-bank/starter.py`
- `docs/SYLLABUS.md`
- `3-advanced/teaching-material/teacher-guide.tex`

## Week 7: Grids, Recursion and Fractal Art

- **Driving question:** How can a function solve a big problem by calling itself on a smaller copy of the same problem?
- **Planned runtime:** 4:45 (285 seconds)
- **Vocabulary:** recursion, base case, recursive case, RecursionError, fractal, grid (2D list), flood fill, negative number
- **Misconception to prevent:** A function that calls itself will somehow know when to stop on its own, or grid[row][col] works like turtle's (x, y) with across first.
- **Digital citizenship:** Credit for generative art and algorithms: the fractal tree and the Koch snowflake (Helge von Koch, 1904) are famous ideas. When you show generative art, say where the idea came from: ‘Fractal tree, based on a classic recursive algorithm; my colors and angles.’ Your code is yours; the idea has a history; giving credit is what real artists and programmers do. Add a comment line # Based on: ... at the top of your fractal file.
- **Practice activity:** `3-advanced/exercises/week07/ex-fractal-tree`

### Instructional objectives

- Explain recursion as solving a smaller copy of the same problem, and point to the base case and the recursive case.
- Read one cell of a grid with grid[row][col]: row first, then column, both counted from 0.
- Describe how a fractal tree is made of smaller copies of itself and how a paint bucket spreads to neighbors.
- Find and fix a missing base case when Python shows a RecursionError.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Welcome back to Code Quest! Today Nova wants two things: a whole forest of trees drawn by code, and a paint bucket that fills a pixel picture with one click. ‘That sounds like thousands of lines,’ beeps Pixel. ‘Not if a function can call itself,’ says Nova. Wait… a function that calls itself? Can it ever stop? | Workshop door 7. Nova sketches a forest and a pixel picture on a whiteboard; Pixel stacks a towering pile of code pages that wobbles. Nova holds up one small recipe card. Freeze on Pixel's puzzled face and a big question mark. **On screen:** MISSION: A forest and a paint bucket; Pause: Can a function call itself? | Three-second prediction pause after the question. Gentle wobble, no crash sound. |
| 0:30–1:25 | **Explain recursion: base case and recursive case** | Picture a set of Russian dolls. Your job is: open the doll. Inside is a smaller doll, so your job is the same again. You keep going until you reach the tiny solid doll. It can't open, so you stop. That's recursion: a function that calls itself on a smaller problem. Every recursive function has two parts. The recursive case does one small step, then calls itself on something smaller. The base case is the tiny problem you can answer straight away, so you stop. Look at countdown. If n is zero or less, print Liftoff and return. That's the base case. Otherwise, print n, then call countdown with n minus one. | Nested dolls open one inside the next; the last solid doll glows with a STOP badge labeled 'base case'. Then the countdown code from the Exercise 7.1 starter appears in a Thonny panel: the if-block is boxed in orange and labeled 'base case', and the countdown(n - 1) line is boxed in sky blue and labeled 'recursive case'. **On screen:** Recursion = same job, smaller problem; Base case = stop here; Recursive case = small step + call again | Show countdown exactly as in the starter (finished code). Never show sum_to or reverse code: they are Exercise 7.1's TODOs. |
| 1:25–2:40 | **Worked example: stacked calls, a fractal tree and a grid** | Let's watch countdown of three run. It prints three, then calls countdown of two, which waits inside it like a smaller doll. Two, one… then countdown of zero reaches the base case: Liftoff! A fractal is a shape made of smaller copies of itself. A tree is a trunk with two smaller trees on top, until the depth reaches zero. Depth one is one line. Depth two, three lines. Depth three, seven. Now grids. A grid is a list of rows, and each row is a list. grid, row one, column three, means go down to row one, then across to column three, both counted from zero. Like a movie ticket: row first, then seat. That cell is H. A paint bucket paints one square, then asks each neighbor, up, down, left and right, to do the same. Where should the paint stop? You'll work that out in Exercise 7.3! | Russian-doll style nested call boxes slide out: countdown(3) → countdown(2) → countdown(1) → countdown(0), each printing its line in a Shell strip, then the boxes close back up. Next, a fractal tree grows branch by branch beside a counter: depth 1 = 1 line, depth 2 = 3 lines, depth 3 = 7 lines. Last, a 3-by-4 grid of letters A–L with row numbers down the side and column numbers across the top; a finger walks down to row 1, then across to column 3, and H lights up. A paint drop lands on one cell and arrows point up, down, left and right, then a big question mark appears. **On screen:** countdown(3): 3, 2, 1, Liftoff!; Depth 1 → 1 line • 2 → 3 • 3 → 7; grid[1][3] → row 1, then column 3; [row][col] is not (x, y) | Use this made-up letter grid, not the workbook's island grid, and stop the line counts at depth 3 (depth 3 = 7 is printed in the workbook picture and the 7.2 README; the workbook table's depth 4 and 5 blanks and the exit ticket's depth 4 are answers). Do not show the fractal tree's five TODO lines or the flood fill's base case and calls. |
| 2:40–3:45 | **Friendly bug hunt: missing base case (RecursionError)** | Bug hunt! Nova writes a function called open_doll. It prints ‘Opening doll’ and the size, then calls open_doll with the size minus one. Pixel runs open_doll of three. Three, two, one, zero, minus one, minus two… the numbers keep falling below zero, and then a red error appears. Let's use our bug-hunting steps. One, read the last line of the error: RecursionError, maximum recursion depth exceeded. Two, predict. ‘I think it never stops,’ says Nova. RecursionError? Look for the base case first! Three, watch: in the debugger, Step into, and the calls pile up like plates. Four, fix one thing. Nova adds a base case: if size is zero, print ‘Solid doll!’ and return. Five, check: run it again. Opening doll three, two, one, Solid doll! | Code panel with the three-line open_doll function and the call open_doll(3). The Shell scrolls: Opening doll 3, 2, 1, 0, -1, -2… as nesting-doll icons shrink to dots, then the red last line. Five step cards light up in turn: Read, Predict, Watch, Fix ONE thing, Check. Thonny's debugger shows boxes stacking. The fix inserts an if-block at the top of the function; the rerun prints four lines and Pixel gives a thumbs-up. **On screen:** RecursionError? Find the base case first; Read • Predict • Watch • Fix one • Check; Each call must get smaller | Four-second prediction pause before the fix appears. Use open_doll only; never show sum_to without a base case (the lesson's bug hunt) or its fix, which is Exercise 7.1's answer. Exact fixed code: if size == 0: print("Solid doll!") then return, above the print line. |
| 3:45–4:45 | **Recap, credit for generative art, and handoff** | Door seven unlocked! Recursion means a function calls itself on a smaller problem. The base case says stop, and the recursive case does one small step and calls itself again. A grid is a list of rows: row first, then column. The fractal tree is a famous idea, and the Koch snowflake was invented by Helge von Koch in 1904. When you show generative art, say where the idea came from, like ‘Fractal tree, based on a classic recursive algorithm; my colors and angles.’ Add a comment that starts with Based on at the top of your file. Now open Exercise 7.2, the Fractal tree, and type along with your teacher. Then finish sum_to and reverse in Exercise 7.1. Where's your base case? Happy coding! | Mission map: door 7 swings open. Three recap icons (nested dolls, a tiny tree, a grid). A code panel shows the comment line '# Based on: classic fractal tree; my colors' above a turtle import. End card points to the Exercise 7.2 folder, then 7.1. **On screen:** Base case • Smaller call • grid[row][col]; # Based on: classic fractal tree; NEXT: 7.2 Fractal tree, then 7.1 | End card includes ‘Narration uses an AI-generated voice’ and a five-second clean hold for teachers to pause. |

**Lesson handoff:** Type along with your teacher in Exercise 7.2 Fractal tree: run starter.py (only the trunks appear), read the base case aloud, add the five TODO lines after the trunk (turn left, smaller tree, turn right twice as far, smaller tree, turn back) and count the lines at depth 1, 2 and 3. Then, in pairs, finish Exercise 7.1 Recursion warm-up (sum_to(n), so sum_to(5) is 15, and reverse(word), so reverse("turtle") is "eltrut", each with a base case and a recursive case; check with check_my_work.py) and build the paint bucket in 7.3.

**Curriculum evidence:**

- `3-advanced/teaching-material/lessons/week07.tex`
- `3-advanced/teaching-material/workbook/week07.tex`
- `3-advanced/teaching-material/homework/week07.tex`
- `3-advanced/exercises/week07/ex-countdown-sum/README.md`
- `3-advanced/exercises/week07/ex-countdown-sum/starter.py`
- `3-advanced/exercises/week07/ex-countdown-sum/hints.md`
- `3-advanced/exercises/week07/ex-fractal-tree/README.md`
- `3-advanced/exercises/week07/ex-fractal-tree/starter.py`
- `3-advanced/exercises/week07/ex-paint-bucket/README.md`
- `3-advanced/exercises/week07/ex-paint-bucket/starter.py`
- `docs/SYLLABUS.md`

## Week 8: Data Detectives: Clean, Count, Chart

- **Driving question:** How do we turn a messy file of survey answers into a true story we can count and chart?
- **Planned runtime:** 4:40 (280 seconds)
- **Vocabulary:** CSV, header, data cleaning, average (mean), sample, consent, anonymize
- **Misconception to prevent:** Numbers read from a CSV file are already numbers, or a blank answer should count as 0 in an average.
- **Digital citizenship:** Consent and anonymizing survey data: our survey asked first, let people pass, and had no names. That is consent and anonymity. Even without names, some answers together can point to one person (the only 13-year-old in the chess club). Before sharing data: keep only the columns you need, replace names with IDs like R1, R2, and never collect addresses, schools, birthdays or photos.
- **Practice activity:** `3-advanced/exercises/week08/ex-survey-cleaner`

### Instructional objectives

- Read a CSV file with csv.DictReader and clean it: strip spaces, skip empty rows, turn text into numbers.
- Count answers with a dictionary tally and work out an average that skips missing answers.
- Describe a bar chart where every bar has its name and its number written on it, not color alone.
- Explain why surveys need consent and how to anonymize answers before sharing.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Nova ran a survey: ‘What's your favorite pet?’ Everyone could choose to answer or pass, and nobody wrote their name. Now the answers are in a file, and Pixel proudly reports: ‘Cat and CAT are two different pets!’ Hmm. That doesn't sound right. How can a data detective find the true story in messy answers? | Nova drops folded sticky notes into a box marked ‘No names. You can pass.’ The notes fly into a text file. Pixel holds up two signs, ‘Cat’ and ‘CAT’, with a proud beep. Nova raises an eyebrow; a detective magnifying glass appears. **On screen:** MISSION: Find the true story; Pause: Are Cat and CAT the same? | Keep the survey anonymous on screen: no faces or names on any note. |
| 0:30–1:25 | **Explain the data pipeline and CSV files** | Data detectives always work in the same order: read, clean, count, calculate, chart. First, read. A CSV file, short for comma-separated values, is a table saved as plain text. One line is one row, and commas split the columns. The first line is the header: the column names. Python's csv dot DictReader turns each row into a dictionary, so row, pet, in square brackets, gives that row's answer. Next, clean. Data is like vegetables from the garden: you wash off the mud before you cook. Strip extra spaces, fix MiXeD capitals, and throw away empty rows. Only then do we count, average and chart. | A five-step pipeline slides in: 1 Read, 2 Clean, 3 Count, 4 Calculate, 5 Chart, each with an icon and a label. A plain-text file morphs into a table: header row highlighted, commas turning into column lines. One row pops out as a dictionary bubble. Muddy carrots get washed as messy values tidy up. **On screen:** Read → Clean → Count → Calculate → Chart; CSV = a table saved as plain text; Header = the column names; Clean before you count! | Name csv.DictReader correctly. Keep the pet file visibly different from favorite_games.csv. |
| 1:25–2:40 | **Worked example: clean, tally, fair-share average, chart** | Here's Nova's little file. Row two says space, cat, space. Row three is empty. Row four, Dog, has no minutes. After cleaning with strip and title, every spelling becomes Cat with a capital C, and the empty row is skipped. Now count with a dictionary, like a tally chart. A new pet starts at zero, then we add one. At the end: Cat, three. Dog, one. Next, the average minutes. The average is a fair share: put everything in one pile, then share it equally. Twenty plus ten plus thirty is sixty. Three people answered, so sixty divided by three is twenty. And the blank? A blank means ‘we don't know,’ not zero, so we skip it. Last, the chart. Cat gets the tallest bar. Dog has one vote and Cat has three, so Dog's bar is one third as tall. Write the name under every bar and the number on top. | A CSV table with columns response, pet, minutes_playing: 1, Cat, 20 / 2, ' cat ', 10 / 3, (empty) / 4, Dog, (blank) / 5, CAT, 30. The empty row is highlighted and slides away; the three cat spellings turn into 'Cat'. A tally chart fills: Cat \|\|\| and Dog \|. Counters for 20, 10 and 30 pile into 60 and split into three equal stacks of 20, while the blank cell shows a '?' tag that steps aside. A turtle bar chart draws two bars, Cat 3 and Dog 1, each with its name below and number on top. **On screen:** Cat 3 • Dog 1; Average = fair share: 60 ÷ 3 = 20; Blank = ‘we don't know’, not 0; Every bar: name below, number on top | Do not show the counts.get line, the average function or bar_height code: they are Exercise 8.2 and 8.3 TODOs. Do not use the exercise's numbers (Block Craft, 3.1 hours, the 2, 4, 6 helper or the exit ticket's 4, 2, 6). |
| 2:40–3:45 | **Friendly bug hunt: numbers read as strings and empty answers** | Bug hunt! Nova's minutes came straight from a file: quote ten, quote nine, quote seven. Pixel finds the biggest with max, and max says quote nine. Nine is bigger than ten? Then sum crashes with a red error. Let's use our steps. Read the last line: TypeError, unsupported operand types for plus, int and str. Predict. ‘I think these numbers are really words,’ says Nova. Watch: each number has quote marks around it. Every CSV value arrives as text, and text is compared letter by letter. Fix one thing: turn text into numbers while cleaning. int of quote ten gives the number ten. But careful! int of an empty answer crashes with a ValueError, so a blank becomes None, and we skip it. Check: run again. The biggest is ten, and the total is twenty-six. | Thonny Shell: minutes = ["10", "9", "7"]. max(minutes) prints '9' with a puzzled Pixel; sum(minutes) prints the red TypeError. The quote marks around each value pulse. The five step cards light up: Read, Predict, Watch, Fix ONE thing, Check. A converter machine turns "10" into 10. An empty answer "" bounces off with a ValueError tag and becomes a None card that steps aside. The rerun shows 10 and 26 with a green check. **On screen:** max(["10", "9", "7"]) → "9"; CSV values arrive as text; int("10") → 10; Blank → None → skip it | Four-second prediction pause before the fix. Use these minutes, not the lesson's hours example. Never show the to_number or is_empty code from Exercise 8.1. |
| 3:45–4:40 | **Recap, consent and anonymizing, and handoff** | Case closed! Read the CSV, clean it, count with a dictionary, take a fair-share average that skips blanks, and label every bar. Now the most important part. Nova's survey asked first, let people pass, and had no names. That's consent and anonymity. Even without names, some answers together can point to one person, like the only thirteen-year-old in the chess club. Before sharing data, keep only the columns you need, replace names with IDs like R1 and R2, and never collect addresses, schools, birthdays or photos. Now open Exercise 8.1, the Survey cleaner, and type along with your teacher. Spot the mess in favorite_games.csv, then clean it until the Shell says Clean answers: seventeen. Happy detecting! | Mission map: door 8 opens. The pipeline icons light up in order. A data table gets anonymized: a column of nickname cards is crossed out and replaced by R1, R2, R3; a 'club' column fades away. A checklist shows: asked first, can pass, no names. End card points to the Exercise 8.1 folder. **On screen:** Clean • Count • Average • Label; Consent • Keep only what you need • R1, R2; NEXT: 8.1 Survey cleaner | Use category words only, never realistic personal data. End card includes ‘Narration uses an AI-generated voice’ and a five-second hold. |

**Lesson handoff:** Type along with your teacher in Exercise 8.1 Survey cleaner: open starter.py and favorite_games.csv, circle the mess (extra spaces, MiXeD capitals, empty rows, a missing number), then finish to_number() and is_empty() and add .title() to the game names, until the Shell says Clean answers: 17 instead of 19. Then, in pairs, count and average in 8.2 and draw the labeled bar chart in 8.3.

**Curriculum evidence:**

- `3-advanced/teaching-material/lessons/week08.tex`
- `3-advanced/teaching-material/workbook/week08.tex`
- `3-advanced/teaching-material/homework/week08.tex`
- `3-advanced/exercises/week08/ex-survey-cleaner/README.md`
- `3-advanced/exercises/week08/ex-survey-cleaner/starter.py`
- `3-advanced/exercises/week08/ex-survey-cleaner/hints.md`
- `3-advanced/exercises/week08/ex-survey-stats/README.md`
- `3-advanced/exercises/week08/ex-survey-stats/starter.py`
- `3-advanced/exercises/week08/ex-bar-chart/README.md`
- `3-advanced/exercises/week08/ex-bar-chart/starter.py`
- `docs/SYLLABUS.md`

## Week 9: How Do Machines Learn?

- **Driving question:** How can a program learn from labeled examples, and why does it copy their mistakes?
- **Planned runtime:** 4:55 (295 seconds)
- **Vocabulary:** feature, label, training data, test data, steps distance, accuracy, classifier, bias, Markov chain, deepfake
- **Misconception to prevent:** An AI understands what it says and is always fair, so when its guesses are wrong the bug must be in the code.
- **Digital citizenship:** AI ethics: AI can be wrong, even when it sounds sure, so check important facts with a trusted source or adult. Never type your real name, address, school, passwords, photos or secrets into a chatbot; what you type may be stored. Deepfakes are fake pictures, voices or videos made by AI: ask ‘Who made this, and why?’ before you believe or share, and never make fakes of real people. Bias: AI is only as fair as its examples. Final project kickoff: Build Something Big starts with your pitch (M1).
- **Practice activity:** `3-advanced/exercises/week09/ex-monster-sorter`

### Instructional objectives

- Explain the difference between a program with hand-written rules and one that learns from labeled examples.
- Use the steps distance (gap plus gap) to find a mystery example's nearest neighbor.
- Show how unbalanced training data leads to bad, unfair predictions.
- Explain how a Markov text generator picks the next word, and why chatbots can sound sure and still be wrong.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Pixel has a new job: sorting dragon eggs into fire eggs and ice eggs. But nobody wrote any rules! ‘Just learn from these examples,’ says Nova, and sets down a basket of labeled eggs. ‘Learn?’ beeps Pixel. ‘I only follow instructions!’ Can a program really learn from examples? And what if the examples are wrong? | A basket of speckled eggs, each with a tag reading FIRE or ICE (a flame or snowflake symbol plus the word). Pixel searches an empty rulebook, then stares at the basket. Freeze on a question mark above Pixel. **On screen:** MISSION: Learn from examples; Pause: Can a program learn? | Every egg label uses a word and a symbol, never color alone. |
| 0:30–1:30 | **Explain rules versus learning, features, labels and testing** | So far, your programs follow rules you typed: if teeth is more than five, say grumpy. A learning program is different. It gets examples with the right answers, called labels, and finds the pattern itself. The things it measures are called features. Our dragon eggs have two features: spots and size, each from zero to ten. Put every example on a chart. To guess a mystery egg, find the closest example and copy its label. That's a nearest-neighbor classifier. To check it, we hide some examples in a test pile, train on the rest, and count the right guesses: its accuracy. Testing on examples it learned from would be like seeing the exam answers first! | Split screen: a 'Rules' card with an if-line versus a 'Learning' card with a stack of labeled examples. Eggs fly onto a feature chart (spots across, size up, 0 to 10), fire eggs as circles marked F, ice eggs as squares marked I. A deck splits into a big Training pile and a small face-down Test pile. **On screen:** Features = what we measure; Label = the right answer; Nearest neighbor: copy the closest label; Train on one pile, test on another | Match the lesson's words: rules, examples, labels, features, training, test, accuracy. |
| 1:30–2:45 | **Worked example: steps distance and a tiny Markov chain** | Here's a mystery egg: seven spots, size three. Which example is closest? Pretend each egg is a game piece on the grid from week seven. It can only step across or up and down, never on a slant. So the steps distance is the gap in spots plus the gap in size. A gap is the bigger number minus the smaller one. To the fire egg at eight, two, the gaps are one and one: two steps. To the ice egg at three, seven, the gaps are four and four: eight steps. The fire egg is closer, so the guess is fire! Machines can learn words, too. A Markov chain learns one thing: after each word, which words came next? From ‘my dog ran, my dog hid,’ it learns that after dog came ran or hid. Then it writes by picking a random next word, again and again. It sounds right, but understands nothing. | Feature chart with four example eggs: fire at (8, 2) and (9, 4), ice at (2, 8) and (3, 7). A white ? egg sits at (7, 3). A dashed grid path walks 1 across and 1 down to (8, 2) with a '2 steps' label; another path walks 4 across and 4 up to (3, 7) with '8 steps'. The nearest egg gets a circle and the guess 'fire'. Then the training text 'my dog ran my dog hid' (shown without commas) becomes a word-chain: 'my' → 'dog'; 'dog' → 'ran' and 'hid'; 'ran' → 'my'. A spinner picks the next word and a silly sentence builds itself. **On screen:** Steps distance = gap + gap; (7, 3) → (8, 2): 1 + 1 = 2 steps; dog → [ran, hid]; Sounds right ≠ understands | Use the dragon-egg cards and the dog sentence only: never the monster cards, the (3, 6) or (5, 5) workbook questions, the exercise's story text, or the distance, nearest or build_chain code. |
| 2:45–3:55 | **Friendly bug hunt: bad training data, bad predictions** | Bug hunt! Someone collected new training eggs but met only one fire egg, a very unusual one at ten spots, size zero, plus lots of ice eggs. Pixel tests it on four eggs it has never seen, and every fire egg gets labeled ice! Is the bug in the code, or in the data? Let's use our steps. Read: there's no red error at all. Predict. ‘The code runs fine. I think the examples are the problem,’ says Nova. Watch one guess on the chart. A real fire egg is six steps from that lonely fire example, but only four steps from an ice egg, so it copies ice. That's bias: unbalanced examples make unfair guesses. When a learning program is wrong, check the examples before the code. Fix one thing: add more fire examples. Check: test again, and the fire eggs are labeled fire. | Training chart: one fire circle far away at (10, 0) and six ice squares at (2, 8), (3, 7), (2, 9), (4, 6), (3, 9) and (5, 5). Four test eggs appear: fire at (7, 3) and (6, 2), ice at (2, 7) and (3, 8). Both fire eggs get an 'ice' guess with a red X, while the ice eggs get green checks. For the fire egg at (7, 3), steps paths compare 3 + 3 = 6 steps (to the lonely fire egg) with 2 + 2 = 4 steps (to the ice egg at (5, 5)). A scale tips heavily toward ice. Three more fire examples join at (8, 2), (9, 4) and (7, 1), and both fire test eggs flip to fire with green checks. **On screen:** Is the bug in the code or the data?; 6 steps vs 4 steps → copies ice; Bias: unbalanced examples, unfair guesses; Check the examples before the code | Four-second prediction pause before Nova's line. Do not say any accuracy percentages from Exercise 9.2 or the exit ticket's 9-out-of-10 answer; do not reuse the lesson's (7, 3, "friendly") label swap. |
| 3:55–4:55 | **Recap, AI ethics, project kickoff and handoff** | Door nine unlocked! A learning program finds patterns in labeled examples. Features are what it measures, the steps distance finds the nearest example, and a test pile checks its accuracy. But AI copies the mistakes in its examples. AI can be wrong, even when it sounds sure: check important facts with a trusted source or adult. Never type your real name, address, school, passwords, photos or secrets into a chatbot; what you type may be stored. Deepfakes are fake pictures, voices or videos: ask, ‘Who made this, and why?’ and never make fakes of real people. AI is only as fair as its examples. Now open Exercise 9.1, the Monster sorter, and type along with your teacher. Then start your Build Something Big pitch card! | Mission map: door 9 opens. Four ethics cards flip over: Can be wrong, Keep it private, Spot deepfakes, Check for bias. A project road map appears with M1 Pitch glowing as the first stop, then M2 to M4 and the Showcase. End card points to the Exercise 9.1 folder. **On screen:** Wrong • Private • Fake • Unfair: be AI-wise; PROJECT: Build Something Big; NEXT: 9.1 Monster sorter, then M1 Pitch | No real chatbot logos or online services. End card includes ‘Narration uses an AI-generated voice’ and a five-second hold. |

**Lesson handoff:** Type along with your teacher in Exercise 9.1 Monster sorter: finish distance(a, b) with the steps distance (the gap in fluff plus the gap in teeth) and nearest(training, mystery), then run it to see each mystery ? joined to its nearest card. Then, in pairs, test fair and biased training in 9.2, build the Markov story machine in 9.3, and start your Build Something Big pitch card (workbook Exercise 9.4, Milestone 1).

**Curriculum evidence:**

- `3-advanced/teaching-material/lessons/week09.tex`
- `3-advanced/teaching-material/workbook/week09.tex`
- `3-advanced/teaching-material/homework/week09.tex`
- `3-advanced/exercises/week09/ex-monster-sorter/README.md`
- `3-advanced/exercises/week09/ex-monster-sorter/starter.py`
- `3-advanced/exercises/week09/ex-monster-sorter/hints.md`
- `3-advanced/exercises/week09/ex-fair-or-biased/README.md`
- `3-advanced/exercises/week09/ex-fair-or-biased/starter.py`
- `3-advanced/exercises/week09/ex-markov-story/README.md`
- `3-advanced/exercises/week09/ex-markov-story/starter.py`
- `docs/SYLLABUS.md`

## Week 10: Project Studio 1: Design First

- **Driving question:** How do we plan a big project with classes, milestones and save points before we build it?
- **Planned runtime:** 4:55 (295 seconds)
- **Vocabulary:** CRC card, class diagram, inheritance, composition, milestone, repository, commit, license
- **Misconception to prevent:** Real programmers start typing right away and save everything in one big commit at the end, or inheritance fits every link between two classes.
- **Digital citizenship:** Licenses: may I use this? Everything in your project must be yours or allowed. The Python standard library is free to use, and your own drawings and sounds are yours. For someone else's picture or sound, look for its license: CC0 means free for anyone; CC BY means free if you give credit; ‘All rights reserved’ or no license means no. Never download anything without your parent, and write every borrowed thing in the Credits section of your README. Easiest choice: draw everything with turtle.
- **Practice activity:** `3-advanced/project/project-brief.tex`

### Instructional objectives

- Design a project with CRC cards and a class diagram that shows ‘is a’ and ‘has a’ links.
- Name the project's must-haves, its milestones and the Core or Full path.
- Start a git repository for the project and make small commits with verb-first messages.
- Check whether a picture, sound or library may be used, and give credit for it.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Studio hook** | Nova's pitch card says: Bee Garden, a grid game where a bee collects pollen and dodges wasps. Nova opens Thonny and starts typing as fast as possible. ‘Wait!’ beeps Pixel. ‘Which parts are there? Who does what?’ Builders draw plans before they pour concrete. Today we design first. What's your plan? | Nova's pitch card fills the screen, then Nova types furiously while code lines tangle into a knot. Pixel holds up a blank index card. A builder's blueprint unrolls behind them. **On screen:** STUDIO MISSION: Design first; Pause: What parts does your project need? | Bee Garden is Nova's own example; it is not the reference project. |
| 0:30–1:35 | **Explain the brief: must-haves, paths and milestones** | Your final project, Build Something Big, can be a grid game, a generative art app, or a data or AI app. It needs two or more classes, one using inheritance or composition. It needs a data structure beyond a flat list, like a dictionary, a queue or a grid. Add one named algorithm, a saved file, five or more pytest tests, eight or more meaningful commits, and a README. It must be fair and safe, too. Most people take the Core path: start from a template, add one class of your own, reuse an algorithm from class, and save one file. The template's tests count toward your five. The Full path is extra challenge: your own design. The milestones are Pitch, Design and core classes, Features with five tests and a playtest, README and polish, and the Showcase. | Three option doors: Grid game, Generative art app, Data/AI app. A must-have checklist ticks in one line at a time, ending with 'README' and 'Fair and safe'. A fork in the road labeled Core path (recommended) and Full path (extra challenge). A project road map lights up five stops: M1 Pitch ✓, M2 Design + core classes, M3 Features + 5 tests + playtest, M4 README + polish, Showcase. **On screen:** 2+ classes • data structure • algorithm; Saved file • 5+ tests • 8+ commits • README; Core path: template + 1 new class; M1 → M2 → M3 → M4 → Showcase | Milestone names and must-haves exactly as in the project brief. Do not show the Core path classes (Game, Tree, Guesser) as code. |
| 1:35–2:50 | **Worked example: CRC cards, class diagram and first commit** | Let's design Bee Garden. A CRC card is an index card for one class: the Class name on top, its Responsibilities on the left, what it knows and does, and its Collaborators on the right, the classes it works with. Bee: knows its row and column, moves unless a wall is in the way, collects pollen. It works with Garden. Garden: holds the grid and says if a square is a wall. Now the class diagram. A hollow arrow means ‘is a’: a Bee is a Critter, and so is a Wasp. A diamond line means ‘has a’: the Game has a Garden and a Bee. Then, in Terminal, inside the project folder: git init, git add, and git commit with a message that starts with a verb, like ‘Add empty Garden and Bee classes.’ Git writes your name into every save point, so use your nickname, never your real name. | Index cards fill in by hand: 'Class: Bee' with responsibilities on the left and 'Garden' as collaborator on the right; then 'Class: Garden'. The cards slide into a class diagram: Bee and Wasp each point to Critter with a hollow-triangle arrow labeled 'is a'; Game connects to Garden and Bee with diamond lines labeled 'has a'. A Terminal panel types: git init, git add bee_garden.py, git commit -m "Add empty Garden and Bee classes", git log --oneline. The commit's author reads a nickname with a placeholder example.com email. **On screen:** CRC: Class, Responsibilities, Collaborators; Hollow arrow = is a • Diamond = has a; git commit -m "Add empty Garden..."; Messages start with a verb | Never show Maze Muncher's CRC cards, class diagram, code or git log; use the Bee Garden example only. Show the author line as a nickname, never a real name. |
| 2:50–3:55 | **Friendly bug hunt: partner code review** | Time for a partner code review! Partners swap seats and read each other's code using three questions. One: does every class match a CRC card? Two: is there a method that does two jobs? Three: is there a name I don't understand? Pixel reviews Nova's code. A Wasp is a Critter, but its init only sets speed. Pixel runs it. Read the last line of the error: AttributeError, Wasp object has no attribute row. Predict. ‘I think Wasp never ran Critter's init,’ says Nova. Fix one thing: add super, dot, init, with row and col, as the first line. Check: run it again. Now the wasp knows where it is! Pixel writes one star, ‘Clear class names,’ and one wish: ‘Add a test for Wasp.’ | Two seats swap. A review card shows the three questions. Code panel: class Critter with __init__(self, row, col) setting self.row and self.col; class Wasp(Critter) whose __init__ only sets self.speed = 1. The Shell shows the red AttributeError. The step cards light up: Read, Predict, Watch, Fix ONE thing, Check. The line super().__init__(row, col) slides in at the top of Wasp's __init__; the rerun prints the row. A star sticky note and a wish sticky note appear. **On screen:** 3 review questions: card? two jobs? name?; AttributeError: no attribute 'row'; super().__init__(row, col); One star + one wish | Model kind, specific feedback about the code, never the person. Four-second pause before the fix. |
| 3:55–4:55 | **Recap, licenses and handoff** | Design done! CRC cards say what each class knows and does. The class diagram shows ‘is a’ and ‘has a.’ Milestones are like LEGO bags, and each commit is a photo after a bag. Now, may you use that picture or sound? Everything in your project must be yours or allowed. Python's standard library is free, and your own drawings are yours. CC0 means free for anyone. CC BY means free if you give credit. All rights reserved, or no license, means no. Never download without a parent, and list borrowed things in your README's Credits. Easiest choice: draw it with turtle! Now grab index cards: one CRC card per class. Play one turn, draw your diagram, then git init and commit your class skeletons. | LEGO bags numbered 1 to 4, each followed by a camera flash labeled 'commit'. Three license badges: CC0 (green check), CC BY (check plus 'give credit'), All rights reserved (stop sign). A README 'Credits' section fills in. End card: index cards, a class diagram and a Terminal with git init. **On screen:** CC0 = free • CC BY = free + credit; No license = do not use; NEXT: CRC cards → diagram → git init | No real logos or brands. End card includes ‘Narration uses an AI-generated voice’ and a five-second hold. |

**Lesson handoff:** Computers closed: write one CRC card per class for your own project (at least two classes; one uses inheritance or composition), play one turn by holding up each card as it does its job, and copy them into workbook Exercise 10.1. Then draw your class diagram (10.2), copy the starter folder into Documents/coding-projects and rename it, check the folder with pwd, run git init, write class skeletons and commit after each class (Milestone 2).

**Curriculum evidence:**

- `3-advanced/teaching-material/lessons/week10.tex`
- `3-advanced/teaching-material/workbook/week10.tex`
- `3-advanced/teaching-material/homework/week10.tex`
- `3-advanced/project/project-brief.tex`
- `3-advanced/project/project-teacher-guide.tex`
- `3-advanced/project/starter/README.md`
- `3-advanced/project/starter/grid_game_template.py`
- `docs/SYLLABUS.md`
- `3-advanced/teaching-material/teacher-guide.tex`

## Week 11: Project Studio 2: Test and Polish

- **Driving question:** How do we prove our project works, learn from playtesters, and explain it to a stranger?
- **Planned runtime:** 4:35 (275 seconds)
- **Vocabulary:** test, edge case, playtest, triage, README, usability, accessibility
- **Misconception to prevent:** If the program works when I play it, it has no bugs, or a test that passes must be checking something.
- **Digital citizenship:** Accessibility and usability review: colors from the Okabe–Ito palette and never color alone (add shapes, letters or text); text large enough to read from a chair; controls written on screen; no fast flashing; usability: a new player knows what to do within 10 seconds. Credits: every borrowed image or sound is listed with its license (or there are none).
- **Practice activity:** `3-advanced/project/project-brief.tex`

### Instructional objectives

- Write pytest tests for your own classes, including an edge case, and check that a test can fail.
- Run a playtest and sort the problems into Must fix, Should fix and Nice to have.
- List what a README needs: what it is, how to run it, how it works, tests and credits.
- Check a project for accessibility and usability and fix at least one problem.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Studio hook** | Bee Garden runs! Nova is ready to show everyone. Then Pixel walks the bee into the corner of the garden… and the whole game crashes. ‘But it worked when I played it!’ says Nova. Other people press keys you'd never think of. How can we catch bugs like this before the showcase? | Bee Garden on a grid: Pixel steers the bee into the bottom-right corner, the window freezes and a red error pops up. Nova's jaw drops. A calendar shows 'Showcase' circled. **On screen:** STUDIO MISSION: Catch bugs early; Pause: How can we find them first? | Comic, not scary: a soft bonk, not a crash siren. |
| 0:30–1:25 | **Explain tests, edge cases, playtests and READMEs** | Today has three jobs. First, tests: tiny programs that check your program. They're like crash-test dummies for cars. You can break things on purpose, safely, as often as you like. Test the logic, like moving and scoring, not the drawing. And test normal cases and edge cases: the corner, the wall, the empty list, the last life. Second, a playtest: someone else uses your project while you watch silently and take notes. Every time they get stuck, you learn something. Third, a README: it tells a stranger what your project is, how to run it, how it works, and who you thank. Future-you is a stranger too! | A crash-test dummy rides a tiny car into a wall and pops back up smiling. Edge cases glow on a grid: a corner square, a wall, an empty list [ ], a single heart. A playtester plays while the owner zips their lips and writes notes. A README page fills in section headings. **On screen:** Tests = crash-test dummies; Edge cases: corner, wall, empty, last life; Playtest: watch silently; README: what • run • how • credits | Keep the words test, edge case, playtest and README as in the lesson. |
| 1:25–2:35 | **Worked example: two tests for a tiny Bee class** | Let's test a tiny Bee class. A new bee has three lives. lose_life takes one away, and if lives drop below zero, it sets them back to zero. Nova writes two tests, and each name says what it checks. Test one: a new bee starts with three lives. Test two is an edge case: lose five lives in a row, and lives should stop at zero. In Thonny's system shell, type python, dash m, pytest, dash q. Two dots: two passing tests! But is test two any good? Break the code on purpose. Nova deletes the two lines that stop at zero, and runs again. An F appears, with the name: lives never go below zero. The test caught it! Put the lines back, green again, and commit: ‘Add tests for Bee lives.’ | Code panel bee_garden.py: class Bee with __init__ setting self.lives = 3, and lose_life doing self.lives -= 1, then if self.lives < 0: self.lives = 0. Second panel test_bee_garden.py: from bee_garden import Bee; def test_bee_starts_with_3_lives(): assert Bee().lives == 3; def test_lives_never_go_below_zero(): bee = Bee(), a for-loop calling bee.lose_life() five times, assert bee.lives == 0. Shell: python -m pytest -q prints '..' and '2 passed'. The two guard lines get deleted; rerun shows '.F' and the failing test name in red. Lines restored; '2 passed' again; git commit -m "Add tests for Bee lives". **On screen:** python -m pytest -q; . = pass • F = fail; Break it on purpose: does it go red?; Test names say what they check | Use this Bee example, not the workbook's tiny Player tests or the template's tests. All code must stay exactly valid as written in the visual. |
| 2:35–3:40 | **Friendly bug hunt: playtest bug triage** | Playtest time! Pixel plays Bee Garden for three minutes, thinking out loud, while Nova stays silent and writes one feedback card per thing: what happened, and what did the player expect? The cards say: the game crashes in the corner. Pollen and wasps look the same. And, ‘I wish there were sound effects.’ Now triage: sort the cards into three piles. Must fix: crashes, can't start, can't win. Should fix: confusing, unfair, hard to read. Nice to have: new ideas for version two. Which pile does the crash go in? Pause and decide. Yes, must fix! For a crash, first write a test that shows the bug, then fix it, so it never comes back. Commit: ‘Fix crash when the bee walks into the corner.’ | Pixel plays with a speech bubble of thoughts; Nova's lips are zipped while three feedback cards fill in under the headings 'What happened?' and 'What did the player expect?'. Three labeled piles appear: 1 Must fix, 2 Should fix, 3 Nice to have. The cards fly to their piles: crash → Must fix, look-alike pollen and wasps → Should fix, sound effects → Nice to have. A new red test appears, then turns green after the fix, then a commit line. **On screen:** Must fix • Should fix • Nice to have; Crash? Write a test first, then fix; git commit -m "Fix crash when..." | Four-second pause before revealing the crash's pile. The owner stays silent during the playtest. |
| 3:40–4:35 | **Recap, accessibility and usability review, and handoff** | Project leveled up! Tests are crash-test dummies, edge cases hide in corners, and triage means fixing the most important thing first. Now the accessibility and usability check. Use colors from the Okabe-Ito palette, and never color alone: add shapes, letters or text. Make text big enough to read from a chair. Write the controls on screen. Nothing flashes fast. A new player should know what to do within ten seconds. And list every borrowed image or sound with its license. Now Milestone 3: write five tests, including an edge case, and commit when they pass. Then the playtest swap and triage. Then Milestone 4: your README and one accessibility fix. | A checklist ticks: Okabe–Ito colors plus shapes and letters (pollen becomes a yellow circle with P, wasps a blue triangle with W), big text, controls on screen, no flashing, a 10-second timer. The road map highlights M3 and M4. End card: a test file, feedback cards and a README. **On screen:** Never color alone: add shapes or letters; Big text • Controls on screen • No flashing; NEXT: M3 tests → playtest → M4 README | Do not show fast flashing even as a bad example. End card includes ‘Narration uses an AI-generated voice’ and a five-second hold. |

**Lesson handoff:** Milestone 3: plan and write at least five tests in test_<your project>.py (at least one edge case; on the Core path the template's passing tests count), run python -m pytest -q in Thonny's system shell and commit when green. Then do the playtest swap with feedback cards and sort them into Must fix, Should fix and Nice to have, and fix one must-fix with a test first. Then Milestone 4: README.md, the accessibility check and one fix.

**Curriculum evidence:**

- `3-advanced/teaching-material/lessons/week11.tex`
- `3-advanced/teaching-material/workbook/week11.tex`
- `3-advanced/teaching-material/homework/week11.tex`
- `3-advanced/project/project-brief.tex`
- `3-advanced/project/project-teacher-guide.tex`
- `3-advanced/project/starter/README.md`
- `3-advanced/project/starter/test_my_project.py`
- `docs/SYLLABUS.md`

## Week 12: Showcase and Graduation

- **Driving question:** How do we share what we built, explain why we built it that way, and keep coding safely?
- **Planned runtime:** 4:40 (280 seconds)
- **Vocabulary:** design decision, showcase, feedback, code of conduct, version 2
- **Misconception to prevent:** A showcase talk should list every feature, and a crash during the demo ruins it.
- **Digital citizenship:** Showcase safety and next steps online: show your nickname, never your real name, on screen; projects stay on our computers and are not uploaded; photos or videos only if everyone agrees. If you share your work later: share with family, or post only with a parent, never with your real name, school, face or location. Choose any coding community together with a parent: look for clear rules, moderators and a code of conduct, and use a nickname. Never move to private chats with strangers, never send photos, and tell an adult if anything feels wrong.
- **Practice activity:** `3-advanced/project/project-brief.tex`

### Instructional objectives

- Plan a two-minute talk that explains one design decision with Problem, Choice, Why and Next time.
- Give kind, specific and useful feedback with one star and one wish.
- Describe how the gallery walk, the talks and the exit assessment work.
- Name safe ways to keep learning and to join coding communities together with a parent.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Showcase hook** | The whole Code Quest workshop has turned into a gallery, and every station runs a project someone built. Nova has two minutes to present Bee Garden. ‘I'll show all forty features!’ says Nova. Pixel's timer beeps. Hmm. In two minutes, what's the most interesting thing you could tell people about your project? | Workshop doors fold back into a gallery of glowing project stations, each with a nickname card. Nova unrolls a very long feature list; Pixel holds up a 2:00 timer. Freeze on a thinking bubble. **On screen:** FINAL MISSION: Tell the why; Pause: What's most interesting? | Keep the timer calm and noncompetitive. Only nicknames on station cards. |
| 0:30–1:25 | **Explain a design-decision talk** | Anyone can say what their program does. A real developer can explain why they built it that way. That's a design decision: a choice about how to build something, with a reason. A museum guide doesn't read every label. They stop at one painting and tell you why the artist painted it that way. So pick one decision and walk through four steps. Problem: what was hard or not working? Choice: what did you decide to do? Why: why that way, and not another? Next time: what would you change? Great decisions to talk about: inheritance or composition, a dictionary or a grid, which algorithm, or what a test caught. | A museum guide stops at one painting while others blur. Four story cards slide in left to right: 1 Problem, 2 Choice, 3 Why, 4 Next time, joined by arrows. Small idea chips float below: is a / has a, dict or grid, algorithm, a test that caught a bug. **On screen:** Design decision = a choice + a reason; Problem → Choice → Why → Next time; Pick ONE decision | Use the four-step wording from the workbook. |
| 1:25–2:35 | **Demo and explain: Nova's model talk** | Let's hear Nova's talk. ‘This is Bee Garden. You collect all the pollen without bumping into a wasp.’ Nova plays for twenty seconds. ‘Problem: my bee and my wasps needed the same position and moving code, and I was copying it twice. Choice: I made a Critter class, and Bee and Wasp are each a Critter. Why: inheritance keeps the shared code in one place, so a fix happens once. Another way was copy and paste, but then every bug needs fixing twice. A test caught a real bug, too: lives dropping below zero. Next time, I'd add a second level loaded from a file.’ Then Nova shows git log, and the save points tell the story, step by step. ‘Any questions?’ | Nova stands beside a running Bee Garden window (bee B, pollen P, wasps W). The four story cards light up one at a time as Nova speaks. A small class diagram shows Bee and Wasp pointing to Critter with 'is a' arrows; a copy-paste icon gets crossed out. A green test row flashes. A Terminal shows git log --oneline with short verb-first messages scrolling up. **On screen:** Problem • Choice • Why • Next time; Choice: Bee and Wasp are Critters; Why: shared code in one place; Show git log: the story of your project | Use Nova's Bee Garden talk, never the Maze Muncher model talk or its git log. Commit messages shown are generic Bee Garden steps that start with a verb. |
| 2:35–3:40 | **Demo and explain: gallery walk, talks and exit assessment** | Now the gallery walk. Visit every station and try each project. On a feedback card, write one star, something specific you liked, and one wish, a specific idea. Good feedback is kind, specific and useful. ‘Cool!’ is kind, but not useful. ‘The score text was big and easy to read’ is all three. Then the talks. One listener is the timekeeper, and another asks one question that starts with ‘Why did you…?’ What if your demo crashes? That's normal! Smile, say, ‘That's a bug for the next version,’ and show your code or your tests instead. Last comes the exit assessment. You work alone and quietly, and it shows what you've learned in Level 3. | Learners walk between stations, leaving feedback cards face down: a star line and a wish line. A vague card 'Cool!' gets an upgrade to the specific sentence. A timekeeper raises a hand at 1:30; a questioner's speech bubble starts 'Why did you…?'. A demo window shows a friendly error and the presenter switches calmly to a test file. A quiet desk with a paper and pencil closes the scene. **On screen:** Star + wish: kind, specific, useful; Ask: ‘Why did you…?’; Demo crashed? Show the code or tests | No phones or cameras pointed at screens. Do not show or describe any exit assessment questions. |
| 3:40–4:40 | **Celebration, safe next steps online, and handoff** | Level 3 complete! You saved your work with git, built classes, searched and sorted, drew fractals, cleaned data, trained a tiny AI, and built something big. Want to keep coding? Your project is yours. If you share it, share with family, or post only with a parent, never with your real name, school, face or location. Choose any coding community with a parent: look for clear rules, moderators and a code of conduct, and use a nickname. Never move to private chats with strangers, never send photos, and tell an adult if anything feels wrong. Now set up your station with your talk card ready: Problem, Choice, Why, Next time. Then join the gallery walk with a star and a wish for every project. Happy coding, graduate! | A Level 3 timeline lights up stop by stop: git save points, classes, search and sort, recursion and grids, data and AI, my big project. A safety shield checks: nickname, parent, rules and moderators, no private chats. A graduation cap lands on Pixel. End card shows a talk card (Problem, Choice, Why, Next time) beside a star-and-wish feedback card. **On screen:** Nickname • Parent • Code of conduct; No private chats • No photos to strangers; NEXT: Gallery walk → 2-minute talk | Warm celebration music with room for applause. The talk card was homework 11; this end card points to the gallery walk. End card includes ‘Narration uses an AI-generated voice’ and a five-second hold. |

**Lesson handoff:** Set up your showcase station: your project and a Terminal showing git log --oneline side by side, with the talk card you filled in for homework 11 (workbook Exercise 12.1: Problem, Choice, Why, Next time) ready. Then join the gallery walk: try every project and leave a feedback card with one star and one wish, face down. Then give your 2-minute talk with a timekeeper and a questioner, and take the exit assessment.

**Curriculum evidence:**

- `3-advanced/teaching-material/lessons/week12.tex`
- `3-advanced/teaching-material/workbook/week12.tex`
- `3-advanced/teaching-material/homework/week12.tex`
- `3-advanced/project/project-brief.tex`
- `3-advanced/project/project-teacher-guide.tex`
- `docs/SYLLABUS.md`

## 4. Automated, adaptable regeneration pipeline

### Architecture

```text
Level 3 sources ──> SHA-256 change detector ──> curriculum analyst agent
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
