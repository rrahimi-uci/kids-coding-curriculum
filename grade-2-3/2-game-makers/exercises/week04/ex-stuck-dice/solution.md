# Teacher reference: Exercise 4.3 - The Stuck Dice (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 4 (Surprise! Random)  **Kind:** Scratch (offline app), bug hunt  **Time:** about 7 minutes
**Big idea:** pick random rolls the die only when its block runs. A roll above the loop happens once; a roll inside the loop happens every time.

## The finished project
Setup: File > New. Keep the cat. Make one variable, "roll", For all sprites. Build the script as printed (bug included), then fix it.

Sprite: Sprite1 (the cat), after the fix
- when green flag clicked
- forever
  - set roll to (pick random 1 to 10)
  - say (roll) for 1 seconds
  - wait 1 seconds

## What you should see
- With the bug: the cat says one number (for example 7), waits, says 7 again, and so on forever. The roll box on the stage never changes until the flag is clicked again.
- After the fix: a new number from 1 to 10 every 2 seconds, and the roll box changes each time. Repeats such as 4, 4 can happen and are still random.

## Bug-hunt answer
- The "set roll to pick random 1 to 10" block is above the forever loop, so it runs once, when the flag is clicked. The forever loop only repeats the say and the wait.
- Fix (three moves, because dragging a block drags everything under it): drag the forever block away from the set block; drag the set block into the top of the forever's mouth; snap the forever back under the green flag block.
- Also accepted: drag a second "set roll to pick random 1 to 10" into the top of the forever and leave or delete the first one. Right-clicking the old set block and choosing "Delete Block" removes only that block.

## Talking points
- Link to the warm-up: rolling the die once and then moving that same number every turn would not be a dice race.
- "What runs once? What runs again and again?" is the question for every loop bug (it was the same idea for the if in week 2).
- Test, look, change one thing: the children change where one block is, not what is in it.

## Common mistakes and quick fixes
- Dragging the set block drags the forever along: show the three-move fix.
- The set block ends up under the say block inside the forever: it still works, but the first thing the cat says is 0. Move it to the top.
- The child changes 10 to another number: that does not fix it; the number is still rolled once.
- Typing a number into the say block instead of using the roll block: the cat then always says that number.

## Check-off list
- [ ] The child tested the buggy version and saw the same number repeat.
- [ ] The child pointed at the set roll block as the bug.
- [ ] After the fix, the set block is the first block inside the forever.
- [ ] The cat says new numbers.
