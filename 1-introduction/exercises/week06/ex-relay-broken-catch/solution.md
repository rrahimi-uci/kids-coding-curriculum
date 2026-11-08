# Teacher reference: Exercise 6.2 - Relay B: Apple Catch Can't Count (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1, Week 6 (Review Studio and Checkpoint)  **Kind:** Scratch (offline app)  **Time:** about 6 minutes
**Big idea:** A score needs a reset at the start and must only count once per catch.

## The finished project
Setup: new project, delete the cat, add the sprites Bowl and Apple, make a variable `score` (For all sprites). Students first build the buggy version exactly as printed (no set score block, no go-to after "change score by 1").

Sprite: Bowl
- when green flag clicked
- go to x: 0 y: -140
- forever
  - set x to (mouse x)

Sprite: Apple (fixed version)
- when green flag clicked
- set score to 0
- go to x: (pick random -200 to 200) y: 170
- forever
  - change y by -5
  - if touching Bowl? then
    - change score by 1
    - go to x: (pick random -200 to 200) y: 170
  - if (y position) < -170 then
    - go to x: (pick random -200 to 200) y: 170

## What you should see
- After the fixes: every game starts at 0, the bowl follows the mouse along the bottom, apples fall from random places.
- Each catch adds exactly 1 and a new apple starts at the top; missed apples also restart at the top.
- Buggy version: one catch adds many points (often 15 to 30) and the second game starts with the score from the first.

## Bug-hunt answers
- Bug 1, where: the top of the Apple's green-flag script. What goes wrong: the score is never reset, so game two starts with the old score. Fix: add "set score to 0" under "when green flag clicked", before the forever loop.
- Bug 2, where: inside "if touching Bowl?". What goes wrong: the score changes too fast. Why: the apple is not sent back to the top, so it keeps touching the bowl and the loop adds 1 on every turn. Fix: after "change score by 1" add "go to x: (pick random -200 to 200) y: 170".

## Talking points
- A scoreboard must be reset before each match, like the paper SCORE box in the warm-up.
- The forever loop asks "touching Bowl?" many times a second, so the apple has to leave the bowl after it counts.
- Play two games on purpose: bug 1 only shows up the second time.

## Common mistakes and quick fixes
- Only one game played, so bug 1 is missed: click the flag again and look at the score.
- "set score to 0" placed inside the forever loop: the score stays 0 all the time. Put it once before the loop.
- Go-to block placed after the if (not inside): the apple jumps even without a catch. Keep it inside the touching-Bowl if.
- Changing several things at once: undo and change one thing, then test.
- Team stops after one bug: there are two.

## Check-off list
- [ ] I built the game exactly as shown and played two games: the second game began with the old score.
- [ ] I found bug 1 and wrote it on my relay baton: no reset.
- [ ] I found bug 2 and wrote it on my relay baton: no go-to after scoring.
- [ ] After my fixes, the score starts at 0 and each catch adds exactly 1.
