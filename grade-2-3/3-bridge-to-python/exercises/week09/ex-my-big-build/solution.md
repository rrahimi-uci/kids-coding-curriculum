# Teacher reference: Exercise 9.2 - Build My Big Build
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 3, Week 9 (Project Studio)  **Kind:** Scratch (offline app) or Python turtle in Thonny, project build  **Time:** about 25 minutes over both Make it phases
**Big idea:** Plan on a plan card, then build and test one part at a time; a partner checks it against the plan.

## The finished project
Setup (core path, done by the grown-up before the lesson): Path A: File > New, add the Pen extension, pick a backdrop you like, keep the cat, make a variable (For all sprites), save as "bigbuild-" plus the nickname. Path B: copy project/starter/postcard.py and rename it, for example postcard_kai.py. Every child's project will differ; these are the two samples from the workbook.

Path A, Leo's Flower Garden, Sprite1 (the cat, made small with "set size to 40 %" if the flowers are too big)
- when green flag clicked
- erase all
- set flowers to 0

- when space key pressed
- go to mouse-pointer
- pen down
- repeat 6
  - repeat 4
    - move 30 steps
    - turn right 90 degrees
  - turn right 60 degrees
- pen up
- change flowers by 1

Path B, Omar's postcard: the starter postcard.py with three changes, each followed by Run:
- t.color("orange") changed to t.color("blue") (the house)
- t.color("purple") changed to t.color("gold") (the roof)
- the three 100s changed to 120 (house sides, the walk up the wall, roof sides)
Extension: a sun under the roof, typed one line at a time: t.color("orange"), then a for i in range(6) loop with t.forward(30) and t.left(60) indented under it. The project folder's reference/postcard_reference.py shows a full postcard with a def flower() (stretch path).

## What you should see
- Path A: the green flag clears the stage and shows flowers 0. Each space press draws a flower of six squares at the mouse-pointer, and the counter goes up by 1.
- Path B: a blue house, sides a little bigger than before, with a gold triangle roof sitting on top.

## Bug-hunt answer
Partner check (Exercise 9.3) finds, in order of how often they appear: a script with no hat block; a counter with no "set to 0" under the green flag; a missing quote mark or bracket in Python (red message in the Shell, with the line number); a line not indented under for, so it runs once; only one of the three 100s changed, so the roof floats or overlaps.

## Talking points
- Test after every part: a bug in a small change is quick to find.
- Point at the code for each part on the plan card; that is next week's showcase sentence.
- Can everyone see it? Thick lines, dark next to light, not color alone.
- Credit: the starter, a friend's idea, a week of the course.

## Common mistakes and quick fixes
- Many changes before one test: undo back to the last working version (Cmd+Z), then one change at a time.
- t.color(blue) without quote marks: put them back.
- The flowers counter does not show on the stage: tick the box next to it in Variables.
- Flowers drawn with a line between them: pen up after the flower, pen down after "go to mouse-pointer".

## Check-off list
- [ ] The plan card is filled in (M1).
- [ ] Path A: a repeat inside a repeat or a My Block, plus a score or counter that works.
- [ ] Path B: a for loop, at least two colors, one shape changed or added; it runs with no red message.
- [ ] Each part was tested before the next one.
- [ ] The partner check is done and one fix was made (M2).
