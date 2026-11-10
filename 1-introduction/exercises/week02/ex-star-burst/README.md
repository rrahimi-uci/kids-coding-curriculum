# Exercise 2.3 – Star Burst

**Goal:** make loop art: 36 lines that make a spiky rainbow star.
**Tool:** Scratch app (offline) with the Pen extension. **Work in pairs.**

## Build steps

1. Use your Polygon Party project, or start a new one and add the **Pen** extension.
2. Build the script below. **change pen color by** is in **Pen**.
3. Click the green flag and watch the star grow.
4. Now try your own numbers for repeat, move and turn. Write down your favorite.
5. Save as `star-burst`.

## The script in words

- when green flag clicked
- erase all
- go to x: -75 y: 0
- point in direction 90
- pen down
- repeat 36:
  - move 150 steps
  - turn right 170 degrees
  - change pen color by 5
- pen up

**turn right** means the **Motion** block **turn ↻ (15) degrees**. Its arrow goes
round to the right, the same way as a clock's hands. Change 15 to the number you need.

## Expected behavior

36 long lines criss-cross to make a round, spiky star in the middle of the
stage, about 150 steps wide. The color of the lines changes a little each
time, like a rainbow. The cat ends where it started, at x: -75 y: 0.

**Math corner (optional):** why does the star close? Each turn is 170 degrees,
and there are 36 turns. 36 × 170 = 6,120 degrees. A whole turn is 360 degrees,
and 17 × 360 = 6,120 too. So the cat turns all the way round exactly 17 times
and ends up facing the same way, back at the start.

## Checklist

- [ ] My star has lots of spiky points (36 lines) and is near the middle of the stage.
- [ ] The color changes as it draws.
- [ ] I tried at least one set of my own numbers.
- [ ] I wrote down my favorite numbers in my workbook.
- [ ] I saved my project.
