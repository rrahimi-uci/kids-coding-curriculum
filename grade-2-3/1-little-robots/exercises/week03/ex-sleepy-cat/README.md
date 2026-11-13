# Exercise 3.2 – The Sleepy Cat (bug hunt)

**Goal:** find the step in the wrong place, and fix it.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. Click **Events** (yellow). Drag in **when green flag clicked**.
2. Click **Looks** (purple). Snap on **say Hello! for 2 seconds**. Type `Good morning!`.
3. Click **Motion** (blue). Snap on **move 10 steps**. Change 10 to `50`.
4. Click **Looks** (purple). Snap on **think Hmm... for 2 seconds**. Type `Zzz`.
5. Test: click the green flag. Look: what does the cat do first?
6. The cat should sleep first, then wake up, then walk. Change one thing.
7. Test again.

## The script in words (with the bug)

- when green flag clicked
- say Good morning! for 2 seconds
- move 50 steps
- think Zzz for 2 seconds

## Expected behavior

With the bug, the cat says "Good morning!", walks, and then falls asleep.
After the fix, the cat sleeps, says "Good morning!", and then walks.

## Checklist

- [ ] I tested and saw the bug.
- [ ] I moved one block.
- [ ] Now the cat sleeps, wakes up, then walks.
