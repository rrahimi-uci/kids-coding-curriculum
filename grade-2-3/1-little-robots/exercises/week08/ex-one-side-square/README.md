# Exercise 8.2 – The One-Side Square (bug hunt)

**Goal:** find the block in the wrong place, and fix it.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. Build Omar's script below. Put the turn under the repeat, not inside it.
2. Drag the cat to the left side of the stage. Click the green flag.
3. What did the cat draw? How many times did it turn?
4. Find the block in the wrong place.
5. Drag it inside the repeat, under the move. Click the flag again.

## The script in words (with the bug)

- when green flag clicked
- erase all
- pen down
- repeat 4: move 100 steps
- (under the repeat) turn ↻ 90 degrees

## Expected behavior

With the bug, the cat draws one long line and turns only once, at the end.
After the fix, the cat draws a square with four sides.

## Checklist

- [ ] I found the block in the wrong place.
- [ ] I moved the turn inside the repeat.
- [ ] Now the cat draws a square.
