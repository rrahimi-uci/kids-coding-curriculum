# Exercise 5.1 – Shape Machine

**Goal:** make your own block, **polygon**, with two **inputs** (sides and length),
and use it to draw many shapes with one block each.
**Tool:** Scratch app (offline) with the Pen extension. **Work in pairs.**

## Build steps

1. Start a new project (**File > New**). Click **Add Extension** (bottom left) and choose **Pen**.
   Set the cat's **Size** to `40`.
2. Click **My Blocks > Make a Block**. Type `polygon`.
3. Click **Add an input (number or text)** and type `sides`.
   Click it again and type `length`. Click **OK**.
   (Leave "Run without screen refresh" unchecked.)
4. A pink **define polygon (sides) (length)** hat appears. Build the steps under it.
   To use an input, **drag** the little `sides` or `length` oval out of the define hat
   into a slot. The **/** (divide) block is in **Operators**.
5. Build the green-flag script using your new pink **polygon** block four times.
6. Click the green flag.
7. Add a pentagon with one more block: **polygon 5 70**.
8. Save as `shape-machine`.

## The scripts in words

**define polygon (sides) (length)**

- pen down
- repeat (sides):
  - move (length) steps
  - turn right (360 / sides) degrees
- pen up

**when green flag clicked**

- erase all
- go to x: 0 y: 0
- point in direction 90
- polygon 3 120
- polygon 4 100
- polygon 6 60
- polygon 8 40

## Expected behavior

Each click on the green flag clears the stage and draws four shapes that all
start from the middle: a big triangle, a square, a hexagon and a small
octagon. Every shape closes. Adding **polygon 5 70** adds a pentagon.

## Checklist

- [ ] I made a My Block called `polygon` with the inputs `sides` and `length`.
- [ ] I dragged the inputs from the define hat (I did not type them).
- [ ] My turn uses **360 / sides**.
- [ ] My green-flag script uses the polygon block at least 4 times with different numbers.
- [ ] I saved my project.
