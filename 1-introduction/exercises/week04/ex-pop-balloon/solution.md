# Teacher reference: Exercise 4.1 - Pop the Balloon
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1, Week 4 (Keeping Score)  **Kind:** Scratch (offline app)  **Time:** about 10 minutes
**Big idea:** A variable is a labeled box that remembers a number; we set it once at the start and change it during the game.

## The finished project
Setup: File > New, delete the cat, add the sprite Balloon1, make a variable `pops` (For all sprites, shown on the stage).

Sprite: Balloon1, script 1
- when green flag clicked
- set pops to 0
- go to x: 0 y: 0

Sprite: Balloon1, script 2
- when this sprite clicked
- change pops by 1
- start sound Pop
- go to x: (pick random -200 to 200) y: (pick random -140 to 140)

Also add a comment: "Credits: Balloon sprite and Pop sound from the Scratch library." Save as `pop-balloon`.

## What you should see
- After the green flag: `pops` shows 0 and the balloon sits in the middle of the stage (0, 0).
- Each click on the balloon: `pops` goes up by exactly 1, a pop sound plays, the balloon jumps to a random place.
- Clicking the flag again resets `pops` to 0.
- Without "set pops to 0", a new game starts with the old number (for example 7) and keeps counting from there.

## Talking points
- A variable is like a scoreboard: it has a name, shows one number, and someone must reset it before the next match.
- "set" throws away the old number and puts in a new one; "change" adds to what is already there.
- "pick random" is a dice roll: you cannot know where the balloon will land next.

## Common mistakes and quick fixes
- Score never resets: "set pops to 0" is missing. Add it under the green flag.
- Score stays at 0 all the time: "set pops to 0" was put inside the click script. Move it to the green-flag script.
- Variable name is typed in or cannot be seen by the sprite: choose it from the dropdown; make it "For all sprites".
- Balloon always jumps to the same spot: the numbers were typed instead of using "pick random" blocks in both x and y slots.
- Balloon jumps off the stage edge: random ranges are too big. Use -200 to 200 for x and -140 to 140 for y.

## Check-off list
- [ ] I made a variable called `pops` and I can see it on the stage: a `pops` box is visible (checkbox ticked).
- [ ] `pops` starts at 0 every time I click the green flag: click the flag after a few pops and it shows 0.
- [ ] Each click adds exactly 1: three clicks give 3.
- [ ] The balloon jumps to a different place each time: pick random sits in both the x and y slots.
- [ ] I added a credits comment and saved my project: a comment is in the code area; the file `pop-balloon` exists.
