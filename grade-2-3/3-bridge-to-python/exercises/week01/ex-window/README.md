# Exercise 1.1 – The Window

**Goal:** draw four squares that make a window, with a repeat inside a repeat.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. Click **Add Extension** (bottom left). Pick **Pen**.
2. Click **Events** (yellow). Drag in **when green flag clicked**.
3. Click **Looks** (purple). Snap on **set size to 100 %**. Change 100 to `40`.
4. Click **Motion** (blue). Snap on **point in direction 90**.
5. Click **Pen** (green). Snap on **erase all**, then **pen down**.
6. Click **Control** (orange). Snap on **repeat 10**. Change 10 to `4`.
7. Drag another **repeat** inside the first one. Change it to `4`.
8. Put **move 60 steps** and **turn ↻ 90 degrees** (blue Motion) in the inside repeat.
9. Put one more **turn ↻ 90 degrees** under the inside repeat, still inside the outside repeat.
10. Snap **pen up** (green Pen) at the bottom.
11. Drag the cat to the middle. Click the green flag.

## The script in words

- when green flag clicked
- set size to 40 %
- point in direction 90
- erase all
- pen down
- repeat 4
  - repeat 4
    - move 60 steps
    - turn ↻ 90 degrees
  - turn ↻ 90 degrees
- pen up

## Expected behavior

Four squares touch in the middle and make a window.

## Checklist

- [ ] One repeat is inside the other.
- [ ] The cat draws four squares.
- [ ] The squares make a window.
