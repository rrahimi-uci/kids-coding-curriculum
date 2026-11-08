# Exercise 6.1 – Relay A: Wonky Hexagon (bug hunt)

**Goal:** build a broken project exactly as shown, then find and fix its **two** bugs.
**Tool:** Scratch app (offline) with the Pen extension. **Work as a relay team:**
the driver builds, the navigator reads this card and fills in the relay baton.

## What it should do

Draw one closed hexagon (6 equal sides of 80 steps) in the middle of the
stage, then the cat says "Done!".

## Build steps

1. Start a new project. Click **Add Extension** and choose **Pen**.
2. Set the cat's **Size** to `40`.
3. Build the script below on the cat **exactly** as written, bugs and all.
4. Click the green flag. Compare the stage with "What it should do".
5. Use the four detective steps. Fix one thing at a time and test after each change.
6. Write both bugs and fixes on your relay baton (workbook, Exercise 6.1).

## The script in words (with two bugs)

Cat sprite:

- when green flag clicked
- erase all
- go to x: 0 y: 0
- point in direction 90
- pen down
- repeat 6:
  - move 80 steps
  - turn right 50 degrees
  - pen up
- say "Done!" for 2 seconds

## The four detective steps

1. What did I **expect**?
2. What **happened**?
3. Read the blocks one at a time with your finger.
4. Change **one** thing, then test again.

## Expected behavior

After your fixes: clicking the green flag clears the stage, draws one closed
hexagon with 6 equal sides starting from the middle, and then the cat says
"Done!".

## Checklist

- [ ] I built the project exactly as shown and watched what went wrong.
- [ ] I found bug 1 and wrote it on my relay baton.
- [ ] I found bug 2 and wrote it on my relay baton.
- [ ] My hexagon closes and the cat says "Done!".
