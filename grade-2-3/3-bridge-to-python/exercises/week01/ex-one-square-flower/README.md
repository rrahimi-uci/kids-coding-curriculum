# Exercise 1.3 – The One-Square Flower (bug hunt)

**Goal:** find the repeat in the wrong place and fix it.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

Priya wants a flower of six squares. Her cat draws only one square!

## Build steps

1. Click **File**, then **New**. Add the **Pen** extension.
2. Build Priya's script below. Look carefully at where each repeat goes.
3. Drag the cat to the middle. Click the green flag.
4. Count the squares. Which repeat is in the wrong place?
5. Fix it. Test again.

## The script in words (with the bug)

- when green flag clicked (yellow Events)
- erase all (green Pen)
- pen down (green Pen)
- repeat 6 (orange Control)
  - turn ↻ 60 degrees (blue Motion)
- repeat 4 (orange Control)
  - move 60 steps (blue Motion)
  - turn ↻ 90 degrees (blue Motion)

## Expected behavior

With the bug, the cat draws only one square. After the fix, the cat draws
six squares that make a flower.

## Checklist

- [ ] I built Priya's script and saw one square.
- [ ] I found the repeat in the wrong place and moved it.
- [ ] Now I see six squares.
