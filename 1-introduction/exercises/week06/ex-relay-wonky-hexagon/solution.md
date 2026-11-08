# Teacher reference: Exercise 6.1 - Relay A: Wonky Hexagon (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1, Week 6 (Review Studio and Checkpoint)  **Kind:** Scratch (offline app)  **Time:** about 6 minutes
**Big idea:** Find bugs with the four detective steps and change only one thing at a time.

## The finished project
Setup: new project, Add Extension > Pen, set the cat's Size to 40. Students first build the buggy version exactly as printed (pen up inside the loop, turn right 50).

Sprite: Cat (fixed version)
- when green flag clicked
- erase all
- go to x: 0 y: 0
- point in direction 90
- pen down
- repeat 6
  - move 80 steps
  - turn right 60 degrees
- pen up
- say [Done!] for (2) seconds

## What you should see
- After the fixes: the stage clears, one closed hexagon with 6 equal sides of 80 steps is drawn starting from the middle, then the cat says "Done!".
- Buggy version: only one short line (80 steps to the right) is drawn; the cat then wanders around without drawing and says "Done!".

## Bug-hunt answers
- Bug 1, where: "pen up" is inside the repeat, under "turn right". What goes wrong: after the first side the pen is lifted, so the other five sides are invisible. Fix: drag "pen up" out of the loop and put it after the repeat, before "say Done!".
- Bug 2, where: the turn block says 50 degrees. What goes wrong: once bug 1 is fixed there are six sides but the shape does not close (6 x 50 = 300 degrees, not 360). Why: a full turn is 360 degrees. Fix: turn right 60 (360 / 6).
- Teams often find bug 1 first; that is fine.

## Talking points
- Detective steps: what did I expect, what happened, read the blocks one at a time with a finger, change one thing and test.
- Do not change five things at once: if it works you will not know which change fixed it.
- The turns of any closed shape add up to 360 degrees.

## Common mistakes and quick fixes
- Team fixes the bug while building: insist they build it exactly as printed, click the flag, then hunt.
- Stopped after one bug: compare the stage with "What it should do" again; there are two.
- Hexagon has a gap or overlaps itself: the turn is still not 60.
- Nothing visible at all: the cat is hidden or pen down is missing; check the Pen extension is added.
- Old drawing stays: "erase all" was removed.

## Check-off list
- [ ] I built the project exactly as shown and watched what went wrong: they saw the single line first.
- [ ] I found bug 1 and wrote it on my relay baton: pen up inside the loop.
- [ ] I found bug 2 and wrote it on my relay baton: turn 50 instead of 60.
- [ ] My hexagon closes and the cat says "Done!".
