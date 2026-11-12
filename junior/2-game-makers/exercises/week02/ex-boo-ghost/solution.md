# Teacher reference: Exercise 2.1 - Boo Ghost
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 2 (If Touching...)  **Kind:** Scratch (offline app)  **Time:** about 5 minutes
**Big idea:** An if asks a question and runs its blocks only when the answer is yes. Inside a forever loop, it asks again and again.

## The finished project
Setup: File > New. Add the Ghost with the "Choose a Sprite" button. The cat can stay or be deleted.

Sprite: Ghost
- when green flag clicked
- forever
  - if touching mouse-pointer? then
    - say Boo! for 1 seconds

## What you should see
- After the flag: nothing, until the mouse-pointer is over the ghost. Then a speech bubble "Boo!" for 1 second.
- Keeping the mouse on the ghost: "Boo!" again every second. Moving it away: no more bubbles after the last one ends.

## Talking points
- The forever keeps asking; the if decides. Link to the lifeguard analogy.
- Pointy blocks are questions: their answer is yes or no. They only fit in pointy holes.
- Sensing (light blue) is new this level: blocks that let a sprite notice things.

## Common mistakes and quick fixes
- The touching block is dropped beside the if, not in the hole: the if then has an empty hole and never runs. Drag it in until the hole lights up.
- The menu says "edge" or another sprite: pick mouse-pointer.
- The script is in the cat's code: the cat says "Boo!" when touched. Click the Ghost in the sprite list and build it there.
- The if is under the green flag with no forever: the ghost checks once and never says anything. That is exactly today's bug hunt (2.3).

## Check-off list
- [ ] The script is in the Ghost's code.
- [ ] The if is inside the forever, and the say block is inside the if.
- [ ] "touching mouse-pointer?" is in the pointy hole.
- [ ] Mouse on the ghost: "Boo!". Mouse away: nothing.
