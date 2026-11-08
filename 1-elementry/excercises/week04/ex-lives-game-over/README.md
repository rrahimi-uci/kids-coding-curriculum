# Exercise 4.3 – Lives and Game Over (bonus)

**Goal:** add a second variable, `lives`, and end the game when it reaches 0.
**Tool:** Scratch app (offline). **Start from:** your `apple-catch` project.

## Build steps

1. Open `apple-catch` (**File > Load from your computer**).
2. Make a variable `lives` (**For all sprites**).
3. Click the **Apple**. Under **set score to 0**, add **set lives to 3**.
4. Inside the **if (y position) < -170** block (a missed apple), add
   **change lives by -1** above the **go to** block.
5. At the bottom of the **forever** loop, add the game-over check below.
6. Test: miss three apples on purpose. Then click the flag and play properly.
7. Save as `apple-catch-lives`.

## The script in words (new parts)

Apple sprite, inside the green-flag script:

- set lives to 3 (under set score to 0)
- inside "if (y position) < -170": change lives by -1
- at the bottom of the forever loop:
  - if lives = 0 then
    - say "Game over!" for 2 seconds
    - stop all

## Expected behavior

Each game starts with 0 points and 3 lives. Every missed apple takes away one
life. Catches still add 1 point. When lives reach 0, the apple says
"Game over!" and the whole game stops.

## Checklist

- [ ] `lives` shows 3 at the start of every game.
- [ ] I lose a life only when I miss an apple (not when I catch one).
- [ ] The game says "Game over!" and stops at 0 lives.
- [ ] I saved my project.
