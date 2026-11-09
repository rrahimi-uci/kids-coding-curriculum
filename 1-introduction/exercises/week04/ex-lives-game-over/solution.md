# Teacher reference: Exercise 4.3 - Lives and Game Over (bonus)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1, Week 4 (Keeping Score)  **Kind:** Scratch (offline app)  **Time:** about 10 minutes
**Big idea:** A second variable and one if block can decide when a game ends.

## The finished project
Setup: open `apple-catch`, make a variable `lives` (For all sprites). The Bowl script does not change.

Sprite: Bowl
- when green flag clicked
- go to x: 0 y: -140
- forever
  - set x to (mouse x)

Sprite: Apple
- when green flag clicked
- set score to 0
- set lives to 3
- go to x: (pick random -200 to 200) y: 170
- forever
  - change y by -5
  - if touching Bowl? then
    - change score by 1
    - start sound (any; the answer key uses Chomp)
    - go to x: (pick random -200 to 200) y: 170
  - if (y position) < -170 then
    - change lives by -1
    - go to x: (pick random -200 to 200) y: 170
  - if lives = 0 then
    - say [Game over!] for (2) seconds
    - stop all

Save as `apple-catch-lives`.

## What you should see
- Each game starts with score 0 and lives 3.
- A caught apple adds 1 to the score and never changes lives.
- Each missed apple takes away exactly 1 life.
- At 0 lives the Apple says "Game over!" for 2 seconds, then everything stops (the bowl stops following the mouse).

## Talking points
- "lives" is a second labeled box, just like SCORE and LIVES in the paper ball game.
- A negative number in "change" takes away: change lives by -1.
- The game-over check sits inside the forever loop because the game must keep asking "are lives 0 yet?"

## Common mistakes and quick fixes
- You lose a life when you catch an apple: "change lives by -1" is in the touching-Bowl if. Move it into the y position < -170 if.
- Game over on the second game: "set lives to 3" is missing, so lives is still 0.
- Game never ends: the "if lives = 0" check is outside the forever loop, or the number is wrong (not 0).
- Lives go below 0 or skip 0: the check is missing or uses a different test; keep it as "lives = 0".
- Lives not visible: the checkbox next to `lives` is not checked.

## Check-off list
- [ ] `lives` shows 3 at the start of every game: set lives to 3 sits under the green flag.
- [ ] I lose a life only when I miss an apple (not when I catch one): the change lives block is in the missed-apple if.
- [ ] The game says "Game over!" and stops at 0 lives: say for 2 seconds, then stop all.
- [ ] I saved my project: file `apple-catch-lives`.
