# Exercise 1.2 – Mixed-Up Jump (bug hunt)

**Goal:** find and fix a bug where two steps are in the wrong order.
**Tool:** Scratch app (offline). **Work in pairs.**

The cat **should**: say "Watch me jump!", jump **up**, come back down to the
ground, and say "Ta-da!". But this script has a bug.

## Build steps

1. Start a new project: **File > New**.
2. Build the script below **exactly** as written, bug and all.
   **change y by** is in **Motion** (y means up and down). **wait** is in **Control**.
3. Click the green flag. Watch carefully. What did the cat do?
4. Find the two blocks that are in the wrong order. Drag them to fix the order.
5. Test again. Save as `mixed-up-jump`.

## The script in words (with the bug)

The middle of the stage is x: 0 y: 0. A number with a minus sign, like -100,
means "the other way": y: -100 is 100 steps **below** the middle, so the cat
starts near the bottom, on the "ground". A bigger y is higher up.

Cat sprite, one script:

- when green flag clicked
- go to x: 0 y: -100
- say "Watch me jump!" for 2 seconds
- change y by -50
- wait 0.5 seconds
- change y by 50
- say "Ta-da!" for 2 seconds

## Debugging steps

1. What did I **expect**?
2. What **happened**?
3. Read the blocks one at a time with your finger and act them out.
4. Change **one** thing, then test again.

## Expected behavior

After your fix: the cat says "Watch me jump!", moves **up**, waits half a
second, comes back **down** to where it started, then says "Ta-da!".

## Checklist

- [ ] I built the buggy script first and saw what went wrong.
- [ ] I can say which two blocks were in the wrong order.
- [ ] After my fix, the cat jumps **up** and lands back on the ground.
- [ ] I tested it more than once.
