# Teacher reference: Exercise 5.2 - Bug-Hunt Relay (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 3, Week 5 (Play Day: Blocks to Words)  **Kind:** Scratch (offline app), bug hunt relay  **Time:** about 13 minutes (about 4 per leg)
**Big idea:** Test, look, change one thing, then test again: the same detective steps fix a nested repeat, a program in parts and a counter.

## The finished project
Setup (before the lesson, about 8 minutes): build each leg exactly as printed in workbook Exercise 5.2, with the bug, and save it as "relay-1-window", "relay-2-trick" and "relay-3-counter". Leg 1 needs the Pen extension (Add Extension, bottom left). Leg 3: delete the cat, add the Apple sprite with Choose a Sprite, and make the variable "apples" (orange-red Variables, Make a Variable, For all sprites). Drag the cat to the middle of the stage for leg 1.

Leg 1, The Window (after the fix), Sprite1 (the cat)
- when green flag clicked
- erase all
- pen down
- repeat 4
  - repeat 4
    - move 60 steps
    - turn right 90 degrees
  - turn right 90 degrees

Leg 2, The Magic Trick (after the fix), Sprite1 (the cat)
- when green flag clicked
- show
- say Watch this! for 2 seconds
- hide

Leg 3, The Stuck Counter (after the fix), Apple
- when green flag clicked
- set apples to 0

- when this sprite clicked
- change apples by 1

## What you should see
- Leg 1: with the bug, one short line drawn back and forth. After the fix, four squares that touch at one corner (a window).
- Leg 2: with the bug, the cat vanishes at once (or never vanishes): the two green flag scripts race. After the fix, "Watch this!" for 2 seconds, then the cat disappears. The next green flag shows it again.
- Leg 3: with the bug, the apples counter on the stage stays at 1. After the fix, the flag sets it to 0 and each click adds 1.

## Bug-hunt answer
- Leg 1: the second "turn right 90 degrees" is inside the inside repeat (the week 1 bug, inner repeat contents in the wrong place). Fix: drag it out (it is the bottom block, so it comes out alone) and drop it under the inside repeat, still inside the outside repeat.
- Leg 2: two parts that each work alone but not together (the week 2 bug). Fix: one script in order; snap "hide" under the say block and delete the second hat block.
- Leg 3: a counter reset at every click (week 3, collecting data). Fix: "set apples to 0" goes under "when green flag clicked".

## Talking points
- The "should do" line is the plan; a bug is any place where the program does something different.
- Leg 2 links to planning: parts must be joined in the right order, not only built.
- Leg 3 links to data: a tally that starts again at every vote counts nothing.

## Common mistakes and quick fixes
- Leg 1: the child drags the first turn and takes the second with it. Drag the bottom one.
- Leg 2: the child adds a wait to the hide script. It helps, but one script in order is the real fix.
- Leg 3: the child deletes "set apples to 0". Then the count never goes back to 0; put it under the green flag.
- Leg 3: no counter on the stage: tick the box next to "apples" in Variables.

## Check-off list
- [ ] Leg 1 fixed: four squares in a window shape.
- [ ] Leg 2 fixed: words first, then the cat vanishes; it comes back on the next green flag.
- [ ] Leg 3 fixed: three clicks show 3; the green flag shows 0.
- [ ] The child tested before and after each fix.
