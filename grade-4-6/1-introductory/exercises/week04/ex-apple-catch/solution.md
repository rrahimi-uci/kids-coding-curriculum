# Teacher reference: Exercise 4.2 - Apple Catch
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1, Week 4 (Keeping Score)  **Kind:** Scratch (offline app)  **Time:** about 15 minutes
**Big idea:** A forever loop with if blocks can watch for a catch, add to a score and restart the apple.

## The finished project
Setup: new project, delete the cat, add the sprites Bowl and Apple, pick any backdrop, make a variable `score` (For all sprites). "mouse x" is in Sensing, "y position" in Motion, "<" in Operators.

Sprite: Bowl
- when green flag clicked
- go to x: 0 y: -140
- forever
  - set x to (mouse x)

Sprite: Apple
- when green flag clicked
- set score to 0
- go to x: (pick random -200 to 200) y: 170
- forever
  - change y by -5
  - if touching Bowl? then
    - change score by 1
    - start sound (any; the answer key uses Chomp)
    - go to x: (pick random -200 to 200) y: 170
  - if (y position) < -170 then
    - go to x: (pick random -200 to 200) y: 170

Add a credits comment and save as `apple-catch`.

## What you should see
- Score shows 0 at the start of every game; the bowl sits at the bottom (y = -140) and moves only left and right with the mouse.
- The apple starts at the top (y = 170) at a random x and falls 5 steps per turn.
- A catch adds exactly 1, plays a sound and a new apple starts at the top; a missed apple restarts at the top with no point.

## Bug-hunt answers
- Where: the Apple's "if touching Bowl?" block, with the "go to x: ... y: 170" block taken out (Mei's bug).
- What goes wrong: one catch adds many points (often 15 to 30).
- Why: the apple stays inside the bowl for many turns of the forever loop; each turn asks "touching Bowl?" and gets "yes", so it adds 1 every time.
- Fix: put "go to x: (pick random -200 to 200) y: 170" back right after "change score by 1" so the apple leaves the bowl.

## Talking points
- The forever loop asks the same questions again and again, very fast: "Am I touching the bowl?"
- Moving the apple away after a catch is like putting the ball back on the table so you do not score twice.
- Each sprite has its own job: the Bowl follows the mouse; the Apple falls, counts and restarts.

## Common mistakes and quick fixes
- Both sprites follow the mouse or the bowl never moves: a script is on the wrong sprite. Check which sprite is highlighted.
- Score is stuck at 0 or not shown: variable was made "For this sprite only", or "set score to 0" is inside the loop. Remake it for all sprites; keep the set block once under the flag.
- Score starts with the old number: "set score to 0" is missing.
- Apple never restarts after a miss: the second if (y position < -170) is missing or has the wrong number.
- The "<" block has the wrong order: it must read (y position) < -170.

## Check-off list
- [ ] The bowl follows the mouse and stays at the bottom: it moves left and right only, at y = -140.
- [ ] Apples start from a random place at the top: pick random in the x slot, y is 170.
- [ ] The score starts at 0 every game: "set score to 0" is under the green flag, before the loop.
- [ ] Each catch adds exactly 1: the go-to block is inside the catch if.
- [ ] I can explain Mei's bug (one catch, many points): the apple keeps touching the bowl while the loop keeps checking.
- [ ] I added a credits comment and saved my project: comment present; file `apple-catch`.
