# Teacher reference: Exercise 7.1 - Hello, Ballerina!
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 1, Week 7 (Two Sprites Talk)  **Kind:** Scratch (offline app)  **Time:** about 8 minutes
**Big idea:** Each sprite has its own scripts. The green flag starts all of them at once, so the second speaker waits for its turn.

## The finished project
Setup: File > New. Keep the cat. Add the Ballerina ("Choose a Sprite") and any backdrop ("Choose a Backdrop"). Drag the sprites apart on the stage.

Sprite: Sprite1 (the cat)
- when green flag clicked
- say Hi, Ballerina! for 2 seconds

Sprite: Ballerina
- when green flag clicked
- wait 2 seconds
- say Hi, Cat! for 2 seconds

## What you should see
- The chosen backdrop, with the cat and the Ballerina in their own spots.
- After the green flag: "Hi, Ballerina!" over the cat for 2 seconds, then "Hi, Cat!" over the Ballerina for 2 seconds.

## Talking points
- Link to the warm-up: the WAIT 2 card on top of the Ballerina's SAY card.
- Why 2? The cat talks for 2 seconds, so the Ballerina waits 2 seconds. Try wait 1: the bubbles overlap.
- Who made the cat, the Ballerina and the backdrop? The Scratch team. Say it at the start of the show.

## Common mistakes and quick fixes
- Both scripts built in the cat's code: the cat says both lines. Drag the second script onto the Ballerina in the sprite list, then delete the cat's copy.
- The wait is in the cat's script: the Ballerina talks first. Move the wait to her script.
- The wait is under the say block, not above it: she talks at once, then waits. Drag it up under the green flag block.
- The Ballerina sits on top of the cat: drag her to her own spot.

## Check-off list
- [ ] Each sprite has its own green-flag script: click each one in the sprite list to check.
- [ ] The Ballerina's script starts with wait 2 seconds.
- [ ] A backdrop is chosen.
- [ ] After the flag the sprites talk one after the other: watch one run.
