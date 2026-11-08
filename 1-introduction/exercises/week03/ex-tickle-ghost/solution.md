# Teacher reference: Exercise 3.2 - Tickle the Ghost
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1 (Introduction), Week 3  **Kind:** Scratch (offline app)  **Time:** about 8 minutes
**Big idea:** An if-else asks a yes/no question and picks one of two paths, and forever makes the sprite keep asking.

## The finished project
Sprite: Ghost (any sprite works; the cat is deleted)
- when green flag clicked
- forever
  - if <touching [mouse-pointer]?> then
    - set size to (150) %
    - say [Boo! That tickles!]
  - else
    - set size to (100) %
    - say [] (empty box)

Setup: delete the cat (right-click it in the sprite pane, then delete), then Choose a Sprite and pick Ghost. "if ... then ... else" and "forever" are in Control, "touching" is in Sensing, "set size to" and "say" are in Looks. In the last say block the child deletes the text so the box is empty. Save as `tickle-ghost`.

## What you should see
- After the flag, when the mouse pointer touches the ghost it grows to 150 % and says "Boo! That tickles!".
- When the mouse moves away it shrinks back to 100 % and the speech bubble disappears.
- This keeps working until the red stop sign is clicked.
- Without forever: nothing happens when the mouse touches the ghost. The question is asked only once, right after the flag, when the pointer is not on the ghost, and then the script ends.

## Talking points
- "The goalkeeper who looks at the ball once and then reads a book misses every goal. A good goalkeeper keeps checking. That is forever with an if inside."
- "An if-else runs exactly one of its two mouths, like 'if wearing socks, wave, else clap'."
- "Predict first: what will happen if we take away the forever?"

## Common mistakes and quick fixes
- Nothing happens when the mouse touches the ghost: the if-else is not inside forever. Wrap it in forever.
- The "Boo!" bubble never goes away: the else part has no empty say block.
- The touching block will not fit: only pointy (six-sided) blocks fit the if slot. Drop it into the hexagon slot.
- The touching dropdown says something other than mouse-pointer: click the little triangle and choose mouse-pointer.
- The ghost does not shrink back: the else part is missing "set size to 100 %".
- Nothing happens at all: the code is on the wrong sprite, or blocks are not snapped to the hat block.

## Check-off list
- [ ] Ghost grows and talks when the mouse touches it: move the mouse over it.
- [ ] It shrinks back and goes quiet when the mouse leaves.
- [ ] The **if-else** is inside **forever**: the if-else sits in the mouth of the forever block.
- [ ] Can explain what happens without forever: it checks only once, so it never reacts.
- [ ] Saved as `tickle-ghost`.
