# Teacher reference: Exercise 3.1 - Pop the Balloon
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 3 (Keep Score)  **Kind:** Scratch (offline app)  **Time:** about 6 minutes
**Big idea:** A variable is a labeled box that remembers a number. "set" puts in a new number; "change" adds to what is there.

## The finished project
Setup: File > New. Add Balloon1 with the "Choose a Sprite" button. Make a variable "score", For all sprites.

Sprite: Balloon1, script 1
- when green flag clicked
- set score to 0
- show variable score

Sprite: Balloon1, script 2
- when this sprite clicked
- change score by 1
- start sound Pop
- next costume

## What you should see
- A small score window at the top left of the stage. After the flag it says 0.
- Each click on the balloon: a pop, the balloon changes color (Balloon1 has three colors), the score goes up by 1.
- Flag again: the score goes back to 0.

## Talking points
- Link to the warm-up boxes: set = empty the box and put in a number; change by 1 = drop in one more counter.
- The score window is how the player sees the variable. The checkbox next to score in the list, or "show variable", turns it on.
- "For all sprites" means every sprite can use the same box: needed when the apple scores and the bowl wants to know.

## Common mistakes and quick fixes
- The menu says "my variable" (Scratch's ready-made one): pick score in each block.
- The variable was made "For this sprite only": delete it (right-click it in the list) and make it again for all sprites.
- Dragging the balloon instead of clicking it: a quick click, without moving the mouse.
- The score keeps going up after the flag: "set score to 0" is missing or in the click script.

## Check-off list
- [ ] Variable "score", For all sprites.
- [ ] "set score to 0" and "show variable score" under the green flag.
- [ ] "change score by 1", a pop and next costume under "when this sprite clicked".
- [ ] Flag gives 0; five clicks give 5; flag gives 0 again.
