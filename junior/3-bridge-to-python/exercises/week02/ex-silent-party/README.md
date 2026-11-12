# Exercise 2.3 – The Silent Party (bug hunt)

**Goal:** find why parts that work alone do not work together, and fix it.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

Leo built Party Time from the same plan. Each part passes its test. But with
the green flag, the balloon never comes!

## Build steps

1. Open your Party Time project. Click the cat.
2. In its **broadcast** block, pick **New message**: `party`. Now it is Leo's version.
3. Test each part on its own: click each script.
4. Click the green flag. Does the balloon come?
5. Find the bug. Fix it. Test again.

## The script in words (with the bug)

Cat:

- when green flag clicked (yellow Events)
- set pops to 0 (orange-red Variables)
- say Party time! for 2 seconds (purple Looks)
- broadcast party (yellow Events)

Balloon1 (no change):

- when I receive balloons (yellow Events)
- go to random position (blue Motion)
- show (purple Looks)

## Expected behavior

With the bug, the balloon never comes. After the fix, it comes after
"Party time!".

## Checklist

- [ ] I tested each part on its own.
- [ ] I found the part where the two scripts do not match.
- [ ] The flag starts the whole party again.
