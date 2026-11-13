# Exercise 7.2 – The Lost Block

**Goal:** find the block that is never used, and fix Sam's game.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. Start a new project.
2. Click **Variables** (orange-red). Click **Make a Variable**. Type `score`. Choose **For all sprites**.
3. Click **My Blocks** (pink-red). Make a block called `get ready`.
4. Under **define get ready**: **set score to 0** (Variables), then **say Go! for 1 seconds** (Looks, purple).
5. Build **when green flag clicked** (Events, yellow), **set rotation style left-right** (Motion, blue) and a **forever** (Control, orange). Inside: **move 10 steps** and **if on edge, bounce** (Motion).
6. Build **when this sprite clicked** (Events) with **change score by 1** (Variables).
7. Test: flag, click the cat, flag. What is wrong?

## The script in words

- define get ready
- set score to 0
- say Go! for 1 seconds

- when green flag clicked
- set rotation style left-right
- forever
  - move 10 steps
  - if on edge, bounce

- when this sprite clicked
- change score by 1

## Expected behavior

After your fix, the flag sets the score to 0 and the cat says Go!
Then it runs. Each click adds 1.

## Checklist

- [ ] I found the lost block.
- [ ] The flag sets the score to 0.
- [ ] The cat says Go! at the start.
