# Exercise 4.1 – Pop the Balloon

**Goal:** use a **variable** to count pops and **pick random** to move the balloon.
**Tool:** Scratch app (offline). **Work in pairs.**

## Build steps

1. Start a new project: **File > New**. Delete the cat (right-click > **delete**).
2. Click **Choose a Sprite** and pick **Balloon1**.
3. Click **Variables > Make a Variable**. Type `pops`, keep **For all sprites**, click **OK**.
   A `pops` box appears on the stage.
4. Build the two scripts below. **pick random** is in **Operators**: drop one into the
   x slot and one into the y slot of **go to x: y:**.
5. Click the green flag and pop the balloon a few times.
6. Click the green flag again. Does `pops` start at 0?
7. Experiment: take away **set pops to 0** and click the flag. What happens? Put it back.
8. Add a credits comment: right-click the code area > **Add Comment** >
   "Credits: Balloon sprite and Pop sound from the Scratch library."
9. Save as `pop-balloon`.

## The scripts in words

Balloon sprite, two scripts:

1. when green flag clicked
   - set pops to 0
   - go to x: 0 y: 0
2. when this sprite clicked
   - change pops by 1
   - start sound Pop
   - go to x: (pick random -200 to 200) y: (pick random -140 to 140)

## Expected behavior

When you click the green flag, `pops` shows 0 and the balloon is in the
middle. Every time you click the balloon, `pops` goes up by 1, you hear a pop,
and the balloon jumps to a surprise place. Without **set pops to 0**, a new
game starts with the old score.

## Checklist

- [ ] I made a variable called `pops` and I can see it on the stage.
- [ ] `pops` starts at 0 every time I click the green flag.
- [ ] Each click adds exactly 1.
- [ ] The balloon jumps to a different place each time.
- [ ] I added a credits comment and saved my project.
