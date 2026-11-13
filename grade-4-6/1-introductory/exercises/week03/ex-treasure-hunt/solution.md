# Teacher reference: Exercise 3.3 - Treasure Hunt (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1 (Introductory), Week 3  **Kind:** Scratch (offline app)  **Time:** about 8 minutes
**Big idea:** An if checks only once, so to keep watching for something you put the if inside forever.

## The finished project
Setup: open the `explorer` project from Exercise 3.1 (File > Load from your computer). Choose a Sprite and add a Star. The explorer keeps its four arrow-key scripts from 3.1.

Sprite: Star
- when green flag clicked
- go to x: 180 y: 120
- forever
  - turn right (5) degrees

Sprite: Explorer (the fixed version; the four arrow-key scripts from 3.1 stay on this sprite too)
- when green flag clicked
- go to x: -180 y: -120
- forever
  - if <touching [Star]?> then
    - say [Treasure found!] for (2) seconds
    - go to x: -180 y: -120

Save as `treasure-hunt`.

## What you should see
- The star waits in the top-right corner (180, 120) and spins all the time.
- The child steers the explorer with the arrow keys from the bottom-left start (-180, -120).
- Each time the explorer touches the star it says "Treasure found!" for 2 seconds and then jumps back to the start, ready to play again.

## Bug-hunt answers
- Where: Sam's explorer script, which has no forever. It is: go to start, then if touching Star then say and go to start.
- What goes wrong: steering the explorer onto the star does nothing, and there is no message.
- Why: the if is checked only once, straight after the flag is clicked, when the explorer is far from the star. Then the script ends.
- Fix: put the whole if block (with its two blocks inside) into a forever loop, under "go to x: -180 y: -120".

## Talking points
- "The goalkeeper who checks the ball once and then reads a book misses every goal. A good goalkeeper keeps checking."
- "Ask: when did the if check, and what was true at that moment?"
- "The arrow keys are doorbells (events). The touching question needs a loop to keep asking."

## Common mistakes and quick fixes
- Still no message after the fix: the if is next to the forever, not inside its mouth. Drag it inside.
- Touching dropdown still says mouse-pointer or something else: click the little triangle and choose Star.
- The explorer script is built on the star (or the arrow keys stop working): click the explorer in the sprite pane and check the code area.
- Arrow keys do nothing: click the stage once so Scratch hears the keyboard.
- The star does not spin: the turn block is outside the forever, or the Star has no script.
- The message flashes and the explorer does not return: the second go to block is missing or is outside the if.

## Check-off list
- [ ] The star spins in the top-right corner: check the position and the spin.
- [ ] Built Sam's script and saw it never says "Treasure found!".
- [ ] Can explain why it never reacted: it checks once, then the script ends.
- [ ] After the fix the explorer finds the treasure every time: test at least twice.
- [ ] Saved as `treasure-hunt`.
