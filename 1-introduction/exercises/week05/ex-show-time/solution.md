# Teacher reference: Exercise 5.3 - Show Time (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1, Week 5 (Messages and My Blocks)  **Kind:** Scratch (offline app)  **Time:** about 12 minutes
**Big idea:** Sprites talk with broadcast and listen with "when I receive", but only if the message names match exactly.

## The finished project
Setup: new project, keep the cat as the Presenter, add a sprite with several costumes as the Dancer (for example Ballerina). Make two messages in a broadcast dropdown (New message): `start show` and `finale`.

Sprite: Cat (Presenter), script 1
- when green flag clicked
- go to x: -150 y: -50
- say [Welcome to the show!] for (2) seconds
- broadcast (start show)

Sprite: Cat (Presenter), script 2
- when I receive (finale)
- say [Thank you for watching!] for (2) seconds

Sprite: Dancer, script 1
- when green flag clicked
- hide

Sprite: Dancer, script 2
- when I receive (start show)
- go to x: 80 y: -30
- show
- repeat 8
  - next costume
  - wait 0.3 seconds
- broadcast (finale)

Save as `show-time`.

## What you should see
- On the flag the Dancer hides and the Presenter goes to (-150, -50) and says "Welcome to the show!" for 2 seconds.
- Then the Dancer appears at (80, -30) and changes costume 8 times (about 2.4 seconds).
- Then the Presenter says "Thank you for watching!".

## Bug-hunt answers
- Where: the Dancer's hat block "when I receive (show start)" instead of "start show".
- What goes wrong: the Presenter speaks, then nothing happens; the Dancer never appears.
- Why: the Presenter broadcasts `start show`, but the Dancer listens for a different message, `show start`, so no script receives `start show`.
- Fix: in the Dancer's hat block choose `start show` from the dropdown.

## Talking points
- Broadcast is a loudspeaker announcement; "when I receive" is listening for exactly that announcement.
- If you listen for "Snack time!" you stay seated when the loudspeaker says "Lunch time!".
- Always pick the message from the dropdown instead of making a new one with a similar name.

## Common mistakes and quick fixes
- Dancer visible at the start: the "hide" script under the green flag is missing.
- Dancer never dances: the hat block uses a different message name (start show vs show start vs Start Show). Choose from the dropdown.
- Scripts on the wrong sprite: Presenter and Dancer scripts swapped. Check the highlighted sprite.
- Thank-you never appears: the Dancer's last block (broadcast finale) or the Presenter's "when I receive finale" script is missing.
- Dancer shows only one costume: "next costume" is outside the repeat or the sprite has only one costume.

## Check-off list
- [ ] I made the messages `start show` and `finale`: both appear in the broadcast dropdown.
- [ ] The dancer only appears after the presenter has spoken.
- [ ] The presenter says thank you after the dance.
- [ ] I can explain Ada's bug: the message names did not match.
- [ ] I saved my project: file `show-time`.
