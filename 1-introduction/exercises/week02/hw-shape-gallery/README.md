# Homework 2 – Shape Gallery

**Goal:** draw a triangle, a square and a hexagon in a row, with no lines joining them.
**Time:** about 10 minutes. **Tool:** Scratch app (offline) with the Pen extension.

## Build steps

1. Open Scratch. Click **Add Extension** and choose **Pen**. Set the cat's **Size** to `40`.
2. Build the script below. Fill in the two missing hexagon numbers
   (rule: **turn = 360 ÷ sides**).
3. Click the green flag. Save as `shape-gallery`.

## The script in words

- when green flag clicked
- erase all
- point in direction 90
- pen up
- go to x: -200 y: 50
- pen down
- repeat 3: move 80 steps, turn right 120 degrees
- pen up
- go to x: -60 y: 50
- pen down
- repeat 4: move 80 steps, turn right 90 degrees
- pen up
- go to x: 80 y: 50
- pen down
- repeat **?**: move 50 steps, turn right **?** degrees
- pen up

## Expected behavior

When you click the green flag, the stage is cleared and three closed shapes
appear in a row: a triangle on the left, a square in the middle and a hexagon
on the right. There are no lines between the shapes.

## Checklist

- [ ] I used **repeat** for every shape.
- [ ] Every shape closes.
- [ ] There are no lines joining the shapes (I used **pen up** before each **go to**).
- [ ] My hexagon uses repeat 6 and the right turn.
- [ ] I saved my project.
