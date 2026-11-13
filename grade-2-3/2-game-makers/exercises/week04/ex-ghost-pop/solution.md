# Teacher reference: Exercise 4.2 - Ghost Pop
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 4 (Surprise! Random)  **Kind:** Scratch (offline app)  **Time:** about 8 minutes
**Big idea:** go to random position puts a sprite in a place nobody can guess. A surprise makes a game fun to play again.

## The finished project
Setup: File > New. Add the Ghost from the library and delete the cat (right-click it in the sprite list, delete). Make one variable, "score", For all sprites.

Sprite: Ghost, script 1
- when green flag clicked
- set score to 0
- forever
  - go to random position
  - wait 1 seconds

Sprite: Ghost, script 2
- when this sprite clicked
- change score by 1
- start sound Pop
- go to random position

## What you should see
- Flag: the score shows 0 and the ghost jumps to a new place every second, anywhere on the stage.
- A quick click on the ghost: a pop, the score goes up by 1, and the ghost jumps away at once (so one catch counts once).
- Flag again: the score goes back to 0.

## Talking points
- "go to random position" is pick random for places: nobody knows where the ghost goes next, not even the person who made the game.
- The wait keeps the game fair: with no wait, the ghost jumps too fast to catch.
- The score works like week 3: set to 0 at the start, change by 1 when something good happens.

## Common mistakes and quick fixes
- The ghost does not move: go to random position is under the forever instead of inside it. Drag it into the forever's mouth.
- The ghost moves too fast to catch: the wait is missing or outside the forever.
- Holding the mouse drags the ghost around: click quickly.
- The score keeps going up from last time: "set score to 0" is missing from the flag script.
- No pop: the computer volume is off, or "start sound" has a different sound picked. Any sound is fine.

## Check-off list
- [ ] set score to 0 is under the green flag, above the forever.
- [ ] go to random position and wait 1 seconds are inside the forever.
- [ ] The click script changes the score by 1 and moves the ghost away.
- [ ] The child can catch the ghost and see the score go up.
