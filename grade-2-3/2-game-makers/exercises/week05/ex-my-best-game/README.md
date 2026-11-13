# Exercise 5.3 – My Best Game

**Goal:** turn your fixed leg 3 into a real game with a score.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper, swap on the timer.

## Build steps

1. Keep your fixed leg 3 open. Click the **Apple** in the sprite list.
2. Click **Variables** (orange-red). Make a variable called `score`, **For all sprites**.
3. Snap **set score to 0** right under **when green flag clicked**, above the forever.
4. Put **change score by 1** inside the if, at the top.
5. Click the flag. Catch the Apple!
6. Add your own idea: a new sound, a backdrop, or a different sprite to catch.

## The script in words

Apple's code:

- when green flag clicked
- set score to 0
- forever
  - if touching Sprite1? then
    - change score by 1
    - start sound Pop
    - go to random position

The cat's code stays the same: forever, go to mouse-pointer.

## Expected behavior

The score starts at 0. Each time the cat catches the Apple, the score goes
up by 1, the Apple pops and jumps to a surprise place.

## Checklist

- [ ] The score starts at 0 when I click the flag.
- [ ] Each catch adds 1.
- [ ] The Apple jumps to a surprise place.
- [ ] I told my grown-up how my game works.
