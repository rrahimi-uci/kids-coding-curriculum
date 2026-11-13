# Teacher reference: Exercise 8.1 - Win and Lose
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 8 (Start, Win and Lose)  **Kind:** Scratch (offline app)  **Time:** about 12 minutes
**Big idea:** A game needs a start (everything set to 0, the goal told), a play part (a forever loop) and an ending (win or game over, then stop all).

## The finished project
Setup: File > Load from your computer: the child's catch game from weeks 2-3 (Star marker, Bowl with arrow keys, falling Apple with a score). Variables "score" and "misses", both For all sprites. Lives are counted as misses that go up, so no number ever goes below 0.

Sprite: Star (unchanged)
- when green flag clicked
- hide

Sprite: Bowl, the new referee script (the arrow-key scripts from week 2 stay as they are)
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

Sprite: Apple (week 3 script, one block added)
- when green flag clicked
- set score to 0
- set rotation style left-right
- go to Star
- point in direction 180
- forever
  - move 5 steps
  - if touching Bowl? then
    - change score by 1
    - start sound Pop
    - go to Star
  - if touching edge? then
    - change misses by 1
    - go to Star

## What you should see
- Green flag: score 0, misses 0, the Bowl says "Catch 10 apples!" for 2 seconds while the first apple falls.
- Catch 10: "You win!" for 2 seconds, then everything stops (the apple freezes in place).
- Miss 3: "Game over!" for 2 seconds, then everything stops.
- A second green flag starts a fresh game at 0 and 0.

## Talking points
- The referee does not move. It only keeps checking, like a soccer referee.
- "stop all" is the final whistle: every script of every sprite stops.
- A good game maker tests every ending, not only the fun one.
- Is 10 a fair goal? Possible to reach, but not in five seconds. Is 3 misses fair? Let the Player say.

## Common mistakes and quick fixes
- An if outside the forever: it checks once, at the start. Drag it in.
- "stop all" outside the if: the game stops at once. Put it inside the if, under the say.
- "score" typed as a word in the = block: drag the round orange-red score block in instead.
- Game over straight away: misses was not set to 0, or the Star is touching an edge (the apple counts a miss at once). Drag the Star lower and away from the sides.
- Misses never go up: "change misses by 1" is in the Bowl's if instead of the Apple's edge check, or below "go to Star" in a different if.
- The score jumps past 10: the apple is not sent back to the Star straight after a catch.

## Check-off list
- [ ] "misses" exists (For all sprites) and goes up by 1 for each apple that falls past.
- [ ] The Bowl's referee sets score and misses to 0 and says the goal before the forever.
- [ ] Both ifs are inside the forever, each with a say and "stop all".
- [ ] Play to win: "You win!" and the game stops.
- [ ] Play to lose: "Game over!" and the game stops.
