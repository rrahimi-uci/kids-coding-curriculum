# Teacher reference: Exercise 1.2 - Dance Forever
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 1 (Forever and Bounce)  **Kind:** Scratch (offline app)  **Time:** about 6 minutes
**Big idea:** Repeat does its blocks a number of times and then stops by itself. Forever keeps going until someone presses stop.

## The finished project
Setup: keep working in the Bounce Cat project. Add the Ballerina with the "Choose a Sprite" button.

Sprite: Ballerina, script 1
- when space key pressed
- repeat 4
  - next costume
  - wait 1 seconds

Sprite: Ballerina, script 2
- when green flag clicked
- forever
  - next costume
  - wait 1 seconds

## What you should see
- Space: the Ballerina changes costume 4 times, one each second (she has 4 dance costumes), then stands still.
- Green flag: she changes costume every second without stopping. The cat from 1.1 bounces at the same time. The red stop sign stops both.

## Talking points
- Which one stopped by itself? The repeat. Which one needed us? The forever.
- Both loops hold the same blocks; only the loop is different.
- The flag starts every green-flag script in the project: the cat and the Ballerina at once.

## Common mistakes and quick fixes
- The scripts are in the cat's code: the cat changes costume instead. Click the Ballerina in the sprite list, and drag the scripts onto her picture to copy them.
- Space does nothing: click the stage once so the keyboard goes to the project.
- After space she keeps dancing: the forever script is still running from the flag. Click stop, then press space.
- "wait 1 seconds" outside the loop: she flashes through her costumes too fast to see. Put the wait inside.

## Check-off list
- [ ] Two scripts in the Ballerina's code.
- [ ] repeat 4 under the space key, forever under the green flag.
- [ ] next costume and wait 1 seconds inside each loop.
- [ ] The child can say which loop stops by itself.
