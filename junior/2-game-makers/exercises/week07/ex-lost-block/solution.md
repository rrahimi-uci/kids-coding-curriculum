# Teacher reference: Exercise 7.2 - The Lost Block (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 7 (My Own Blocks)  **Kind:** Scratch (offline app), bug hunt  **Time:** about 8 minutes
**Big idea:** Making a My Block is not enough: it runs only where it is used. A block made but never used is a common bug.

## The finished project
Setup: File > New. Keep the cat. Make the variable "score" (For all sprites). Build Sam's buggy version from the workbook first. (Support path: build it yourself before the session.)

Sprite: Sprite1 (the cat), after the fix
- define get ready
- set score to 0
- say Go! for 1 seconds

- when green flag clicked
- get ready
- set rotation style left-right
- forever
  - move 10 steps
  - if on edge, bounce

- when this sprite clicked
- change score by 1

## What you should see
- With the bug: the cat runs and bounces at once. Clicking it adds 1 to the score. A second green flag does not reset the score, and the cat never says "Go!".
- After the fix: every green flag sets the score to 0, the cat says "Go!" for 1 second while standing still, then runs and bounces. Each click on the cat adds 1.

## Bug-hunt answer
- The bug: "define get ready" sits alone. Nothing uses the "get ready" block, so its blocks never run. Fix: drag "get ready" from the My Blocks list under "when green flag clicked", above the forever loop.
- It cannot go under the forever loop (the forever has no notch at the bottom): a block after a forever would never run.

## Talking points
- Link to the warm-up: the WASH HANDS envelope that was made but not in the breakfast plan.
- Test, look, change one thing: click the flag twice and watch the score. That is how you notice the reset is missing.
- "set rotation style left-right" is from week 1: it stops the cat walking upside down after a bounce. "get ready" can go above or below it, as long as it is above the forever.

## Common mistakes and quick fixes
- The child copies "set score to 0" under the flag instead of using the block: it works, but ask them to use their My Block, so the define script is not lost.
- The cat is clicked while dragging, so it moves instead: click quickly.
- The score box does not show on the stage: check the box next to "score" in the Variables list.
- The variable was made "For this sprite only": it still works here, but make it "For all sprites" so later games can share it.

## Check-off list
- [ ] "get ready" is under the green flag hat, above the forever loop.
- [ ] Flag, click the cat a few times, flag again: the score goes back to 0.
- [ ] The cat says "Go!" before it starts running.
- [ ] The child can say why it did not work before ("the block was made but never used").
