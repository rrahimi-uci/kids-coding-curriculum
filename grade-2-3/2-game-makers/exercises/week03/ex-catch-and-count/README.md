# Exercise 3.2 – Catch and Count

**Goal:** add a score to your catch game.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. File > Load from your computer. Open your catch game from last week.
2. Click **Variables** (orange-red). Make a variable called `score`, for all sprites.
3. Click the **Apple** in the sprite list.
4. Snap **set score to 0** (orange-red Variables) right under **when green flag clicked**.
5. Put **change score by 1** (orange-red Variables) inside **if touching Bowl? then**, at the top.
6. Click the flag. Play! Watch the score.
7. Save with the same name.

## The script in words

Apple (new blocks marked NEW):
- when green flag clicked
- set score to 0 (NEW)
- set rotation style left-right
- go to Star
- point in direction 180
- forever
  - move 5 steps
  - if touching Bowl? then
    - change score by 1 (NEW)
    - start sound Pop
    - go to Star
  - if touching edge? then
    - go to Star

## Expected behavior

The score starts at 0. Each apple you catch adds 1. A missed apple adds nothing.
A new game starts at 0 again.

## Checklist

- [ ] The score starts at 0.
- [ ] Each catch adds 1.
- [ ] A miss does not add a point.
- [ ] I saved my game.
