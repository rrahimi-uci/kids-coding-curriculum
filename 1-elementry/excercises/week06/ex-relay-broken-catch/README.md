# Exercise 6.2 – Relay B: Apple Catch Can't Count (bug hunt)

**Goal:** build a broken catch game exactly as shown, then find and fix its **two** bugs.
**Tool:** Scratch app (offline). **Work as a relay team.**

## What it should do

- Every game starts with a score of 0.
- Apples fall from surprise places at the top.
- Every apple caught in the bowl adds **exactly 1** to the score.
- Missed apples go back to the top.

## Build steps

1. Start a new project. Delete the cat. Add the **Bowl** and **Apple** sprites.
2. Make a variable `score` (**For all sprites**).
3. Build the two scripts below **exactly** as written, bugs and all.
4. Play **two** games (click the green flag, play, then click the green flag again).
   Compare with "What it should do".
5. Use the four detective steps. Fix one thing at a time and test after each change.
6. Write both bugs and fixes on your relay baton (workbook, Exercise 6.2).

## The scripts in words (with two bugs)

**Bowl**:

- when green flag clicked
- go to x: 0 y: -140
- forever:
  - set x to (mouse x)

**Apple**:

- when green flag clicked
- go to x: (pick random -200 to 200) y: 170
- forever:
  - change y by -5
  - if touching Bowl? then
    - change score by 1
  - if (y position) < -170 then
    - go to x: (pick random -200 to 200) y: 170

## Expected behavior

After your fixes: every game starts with the score at 0. The bowl follows the
mouse along the bottom. Apples fall from random places; each one you catch
adds exactly 1 and a new apple starts at the top; missed apples also start
again at the top.

## Checklist

- [ ] I built the game exactly as shown and played two games.
- [ ] I found bug 1 and wrote it on my relay baton.
- [ ] I found bug 2 and wrote it on my relay baton.
- [ ] After my fixes, the score starts at 0 and each catch adds exactly 1.
