# Exercise 8.1 – Draw a Square

**Goal:** make the cat draw a square with the pen.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. Click **Add Extension** at the bottom-left. Choose **Pen**.
2. Click **Events** (yellow). Drag in **when green flag clicked**.
3. Click **Looks** (purple). Snap on **set size to 100 %**. Change 100 to `40`.
4. Click **Pen** (green). Snap on **erase all**, then **pen down**.
5. Click **Control** (orange). Snap on **repeat 10**. Change 10 to `4`.
6. Click **Motion** (blue). Put **move 10 steps** inside the repeat. Change 10 to `100`.
7. Put **turn ↻ 15 degrees** inside the repeat, under the move. Change 15 to `90`.
8. Click **Pen** (green). Snap **pen up** under the repeat.
9. Drag the cat to a place with room. Click the green flag.

## The script in words

- when green flag clicked
- set size to 40 %
- erase all
- pen down
- repeat 4: move 100 steps, then turn ↻ 90 degrees
- pen up

## Expected behavior

The cat gets small. It draws a square: move, quarter turn, four times.
It ends where it started.

## Checklist

- [ ] I added the Pen extension.
- [ ] Move and turn are both inside the repeat.
- [ ] My cat drew a square with four sides.
