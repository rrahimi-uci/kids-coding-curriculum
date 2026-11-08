# Exercise 3.3 – Treasure Hunt (bug hunt)

**Goal:** steer an explorer to a spinning star, and fix a sprite that never reacts.
**Tool:** Scratch app (offline). **Work in pairs.**

## Build steps

1. Open your `explorer` project from Exercise 3.1 (**File > Load from your computer**).
2. Click **Choose a Sprite** and add a **Star**. Give the Star the script "Star" below.
3. Click your explorer sprite. Add Sam's script below **exactly**, bug and all.
4. Click the green flag and steer the explorer onto the star with the arrow keys.
   What happens? Why?
5. Fix Sam's script (remember the goalkeeper: keep checking!). Test again.
6. Save as `treasure-hunt`.

## The scripts in words

**Star** sprite:

- when green flag clicked
- go to x: 180 y: 120
- forever:
  - turn right 5 degrees

**Explorer** sprite (Sam's version, with a bug), plus the four arrow-key scripts from 3.1:

- when green flag clicked
- go to x: -180 y: -120
- if touching Star? then
  - say "Treasure found!" for 2 seconds
  - go to x: -180 y: -120

## Expected behavior

After your fix: the star waits in the top-right corner, spinning. You steer
the explorer with the arrow keys. Every time the explorer touches the star,
it says "Treasure found!" for 2 seconds and jumps back to the bottom-left
start, ready to play again.

## Checklist

- [ ] The star spins in the top-right corner.
- [ ] I built Sam's script and saw that it never says "Treasure found!".
- [ ] I can explain why it never reacted.
- [ ] After my fix, the explorer finds the treasure every time.
- [ ] I saved my project.
