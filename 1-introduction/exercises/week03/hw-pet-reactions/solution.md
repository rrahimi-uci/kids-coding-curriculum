# Teacher reference: Homework 3 - Pet Reactions
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1 (Introduction), Week 3  **Kind:** Scratch (offline app)  **Time:** about 10 minutes
**Big idea:** Different events (click, key, mouse touching) start different scripts, and an if inside forever keeps watching.

## The finished project
Sprite: Pet (the cat, or any animal). Three scripts.

Script 1
- when this sprite clicked
- start sound [any sound from the dropdown]
- change [color] effect by (25)

Script 2
- when [space] key pressed
- next costume

Script 3
- when green flag clicked
- forever
  - if <touching [mouse-pointer]?> then
    - say [Pet me more!]
  - else
    - say [] (empty box)

Setup: no extension. "when this sprite clicked" is in Events, "start sound" in Sound, "change color effect by" in Looks. Any animal and any sound are fine. Save as `pet-reactions`.

## What you should see
- Clicking the pet plays a sound and changes its color (a new color on every click).
- Pressing space switches to the next costume (a sprite with only one costume will not visibly change).
- After the green flag, the pet says "Pet me more!" whenever the mouse is over it, and the bubble disappears when the mouse moves away.

## Talking points
- "Which block is the doorbell in each script?" (when this sprite clicked, when space key pressed, when green flag clicked.)
- "Script 3 is the goalkeeper: forever keeps checking whether the mouse is touching."
- "A sprite has one speech bubble. The newest say block wins, so two scripts that both say can overwrite each other. That is why the click script changes color instead of talking."

## Common mistakes and quick fixes
- "Pet me more!" never appears: the if-else is not inside forever (the if runs once, right after the flag, when the mouse is not touching the pet).
- "Pet me more!" stays forever: the else has no empty say block.
- Space does nothing: the hat block dropdown is not set to space, or the stage was not clicked yet.
- No change on space: the pet has only one costume, so pick an animal with several.
- Click does nothing: the child used "when green flag clicked" instead of "when this sprite clicked", or the code is on another sprite.
- Child adds a say block to the click script and its words never show: the pet is under the mouse when clicked, so script 3 replaces the bubble with "Pet me more!" at once. Explain the one-bubble rule; use a color, size or sound reaction for the click instead.
- The pet keeps its new color after the flag: optional extra, add "clear graphic effects" (Looks) under the green flag.

## Check-off list
- [ ] Pet reacts to a click, a key press and the mouse: test all three.
- [ ] The **if-else** is inside **forever**: it sits in the mouth of the forever block.
- [ ] Can say which block is the event in each script: the hat block on top of each.
- [ ] Asked someone at home for two stars and a wish: look for two specific things they liked and one kind idea to improve it. Specific is better than "it's good".
- [ ] Saved as `pet-reactions`.
