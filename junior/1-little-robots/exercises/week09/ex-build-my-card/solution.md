# Teacher reference: Exercise 9.2 - Build My Card
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 1, Week 9 (Project Studio)  **Kind:** Scratch (offline app), project build  **Time:** about 15 minutes
**Big idea:** Plan on a storyboard, then build and test one box at a time.

## The finished project
Setup (core path, done by the grown-up before the lesson): File > New, Choose a Backdrop (pick a backdrop you like), keep the cat, File > Save to your computer as "card-" plus the child's nickname. Mei's sample card for Grandpa; every child's card will differ.

Sprite: Sprite1 (the cat), boxes 1 and 2
- when green flag clicked
- say Happy birthday! for 2 seconds
- play sound Meow until done
- repeat 4
  - next costume
  - wait 1 seconds

Sprite: Balloon1 (added with Choose a Sprite), box 3
- when this sprite clicked
- play sound Pop until done
- say Surprise! for 2 seconds

## What you should see
- After the green flag: the cat says "Happy birthday!" for 2 seconds, meows, then changes costume four times, one second apart.
- Clicking the balloon: a pop sound, then "Surprise!" in a speech bubble.
- Other valid cards: a key event ("when space key pressed") instead of a click; a backdrop change ("switch backdrop to") instead of a second sprite; a turn dance (turn 15 degrees inside the repeat) instead of costumes.

## Talking points
- Test after every box: a bug in a small box is quick to find.
- Each sprite has its own scripts: click the sprite in the sprite list before building.
- The must-haves map to the boxes: flag and sound in box 1, repeat in box 2, click or key and the second sprite in box 3.

## Common mistakes and quick fixes
- A script with no hat block never starts: add one from Events.
- The click script is under the cat, but the child clicks the balloon: drag the script onto the balloon in the sprite list (this copies it), then delete it from the cat.
- The dance is too fast to see: add "wait 1 seconds" inside the repeat.
- The card starts differently on the second run (a hidden sprite stays hidden): add "show" or "switch backdrop to" at the top of a green flag script.
- A real name on the card: change it to "Grandpa", "my friend" or a nickname.

## Check-off list
- [ ] The green flag starts the card: click the flag and watch.
- [ ] At least one repeat: point to the C-shaped orange block.
- [ ] One click or key event: click the sprite or press the key and see something happen.
- [ ] A sound: listen for it.
- [ ] Two sprites or a backdrop change: look at the sprite list or watch the stage.
- [ ] The card matches the storyboard: compare box by box (milestone M2).
