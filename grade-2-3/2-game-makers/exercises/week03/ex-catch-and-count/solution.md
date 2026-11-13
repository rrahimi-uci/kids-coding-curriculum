# Teacher reference: Exercise 3.2 - Catch and Count
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 3 (Keep Score)  **Kind:** Scratch (offline app)  **Time:** about 12 minutes, across both Make it blocks
**Big idea:** A score variable is set once at the start and changed inside the if that decides when a point is earned.

## The finished project
Setup: File > Load from your computer: the child's Catch the Apple game from week 2 ("Game Makers" folder). If it was lost, rebuild it from the Exercise 2.2 teacher reference first. Make a variable "score", For all sprites. Star and Bowl scripts are unchanged from week 2.

Sprite: Apple
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
    - go to Star

## What you should see
- Flag: the score window says 0; the apple falls from the Star's spot.
- Each catch: a pop and the score goes up by exactly 1.
- Each miss: the apple goes back to the top; the score stays the same.
- Flag again: the score is 0.

## Talking points
- Where does a block go? Once at the start: above the forever. Only when something happens: inside that if.
- Fair scoring: say the rule before a friend plays ("1 point for each apple").
- Other places for "set score to 0" also work, for example in the Bowl's green-flag script. One place is enough.

## Common mistakes and quick fixes
- The score shoots up while the apple falls: "change score by 1" is inside the forever but not inside the Bowl if.
- The score goes up on a miss: the change block is in the edge if.
- The score goes up by 2 or 3 for one catch: the "go to Star" is missing from the Bowl if, so the apple touches the bowl for several steps. Put it back after the sound.
- The score never resets: "set score to 0" is missing or says "change". (That is today's bug hunt.)
- The variable was made in last week's file by mistake, or twice: check that every menu says score.

## Check-off list
- [ ] Variable "score", For all sprites, visible on the stage.
- [ ] "set score to 0" above the forever in the Apple's script.
- [ ] "change score by 1" inside "if touching Bowl? then".
- [ ] One catch adds 1; a miss adds nothing; the flag resets to 0.
- [ ] The game is saved again.
