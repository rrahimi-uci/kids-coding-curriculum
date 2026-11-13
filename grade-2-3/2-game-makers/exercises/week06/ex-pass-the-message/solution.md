# Teacher reference: Exercise 6.2 - Pass the Message
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 6 (Messages)  **Kind:** Scratch (offline app)  **Time:** about 7 minutes
**Big idea:** Messages can pass the action along a chain: each sprite waits for its own message, acts, then sends the next one.

## The finished project
Setup: File > New. Keep the cat; add the Ghost and the Ballerina. Spread them out on the stage by dragging.

Sprite: Sprite1 (the cat)
- when green flag clicked
- say Hi, Ghost! for 2 seconds
- broadcast ghost

Sprite: Ghost
- when I receive ghost
- say Boo! for 2 seconds
- broadcast dance

Sprite: Ballerina
- when I receive dance
- repeat 4
  - next costume
  - wait 1 seconds

## What you should see
- Flag: the cat says "Hi, Ghost!" for 2 seconds.
- Then the Ghost says "Boo!" for 2 seconds.
- Then the Ballerina changes costume four times, one each second.
- The order never changes, and nobody had to count how long the others talk.

## Talking points
- Compare with Level 1 week 7, where two sprites took turns with wait blocks: if a line got longer, every wait had to change. With messages, each sprite starts when the one before it is done.
- The broadcast comes after the say block, because "say for 2 seconds" finishes before the next block runs.
- The chain is the note relay from the warm-up, inside the computer.

## Common mistakes and quick fixes
- Everyone talks at once: a sprite starts with "when green flag clicked" instead of "when I receive". Swap the hat block.
- The Ballerina never dances: her hat listens for "ghost" or "message1". Pick dance.
- The broadcast is above the say block: the next sprite talks at the same time. Move the broadcast to the bottom.
- The chain stops in the middle: read every message name out loud, sender then listener, and find the pair that does not match.

## Check-off list
- [ ] The cat broadcasts ghost; the Ghost listens for ghost.
- [ ] The Ghost broadcasts dance; the Ballerina listens for dance.
- [ ] Each broadcast is the last block in its script.
- [ ] The three sprites act in order.
