# Teacher reference: Exercise 8.2 - Never or Right Away? (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 8 (Start, Win and Lose)  **Kind:** Scratch (offline app), bug hunt  **Time:** about 8 minutes
**Big idea:** An ending must be possible but not true at the start, and the check must keep running. A game that ends at once or never ends has a bug in its ending.

## The finished project
Setup: the child's game from Exercise 8.1, saved as a copy (nickname plus "bugs") so the working game stays safe. The children make each bug on purpose, watch it, and fix it. After both fixes the Bowl's referee script is exactly the one from Exercise 8.1:

Sprite: Bowl, after the fixes
- when green flag clicked
- set score to 0
- set misses to 0
- say Catch 10 apples! for 2 seconds
- forever
  - if misses = 3 then
    - say Game over! for 2 seconds
    - stop all
  - if score = 10 then
    - say You win! for 2 seconds
    - stop all

## What you should see
- Leo's bug (misses = 0): right after "Catch 10 apples!", the Bowl says "Game over!" and everything stops. The game ends right at the start.
- Zoe's bug (win check above the forever): catch 10, 11, 12 apples and nothing happens; the game only ends with 3 misses. The game never ends with a win.
- After both fixes: win at 10, game over at 3 misses.

## Bug-hunt answer
- Leo: "misses = 0" is true at the start, because misses was just set to 0. The ending must be something that only happens later. Fix: 3.
- Zoe: the if above the forever runs once, right after the flag, when the score is 0. It never checks again. Fix: drag it into the forever (the same bug as week 2's if outside the loop).

## Talking points
- Link to the warm-up: passing the ball with no way to win (never ends), and "if you wear socks, you lose" (ends at once).
- Test, look, change one thing: change one block, click the flag, watch. Then change it back.
- Making a bug on purpose in a copy is a great way to learn what each block does.

## Common mistakes and quick fixes
- Working in the real game instead of a copy: if it gets muddled, load the saved game again.
- Dragging an if also drags every block below it. That is why the score check is the lower if: it comes out alone. If a child drags the misses check by mistake, both ifs come out and the game can never end; drag them back into the forever.
- After Zoe's bug, the child loses on purpose and thinks it works: ask them to win, too.
- Typing "0" in the wrong = block (the score one): the game then wins at once. Another good find; fix it the same way.

## Check-off list
- [ ] The child predicted both bugs from the printed scripts.
- [ ] Leo's bug made and seen (game over at once), then fixed.
- [ ] Zoe's bug made and seen (no win at 10), then fixed.
- [ ] The child names the clue: "the 0" and "the if outside the forever".
