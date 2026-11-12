# Teacher reference: Exercise 2.2 - Party Time
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 3, Week 2 (Plan It on Paper)  **Kind:** Scratch (offline app)  **Time:** about 15 minutes
**Big idea:** A program built from a plan card, one part at a time. Each part is tested on its own before the next one is built, then all the parts are tested together.

## The finished project
Setup: File > New. Keep the cat. Make the variable "pops" (For all sprites). Add Balloon1 with "Choose a Sprite".

Sprite: Sprite1 (the cat), Part 1
- when green flag clicked
- set pops to 0
- say Party time! for 2 seconds
- broadcast balloons

Sprite: Balloon1, Part 2
- when green flag clicked
- hide

- when I receive balloons
- go to random position
- show

Sprite: Balloon1, Part 3
- when this sprite clicked
- start sound Pop
- change pops by 1
- go to random position

## What you should see
- Green flag: the balloon vanishes, the pops monitor on the stage shows 0, and the cat says "Party time!" for 2 seconds.
- Then the balloon appears in a random place.
- Each click on the balloon: a pop sound, pops goes up by 1, and the balloon jumps somewhere new.
- Part tests: clicking the cat's script runs Part 1. Clicking the "when I receive balloons" script shows the balloon. Clicking the balloon on the stage runs Part 3.

## Talking points
- The plan card is the map. Ask the Helper: "Which part are we on? What is its test?"
- A part can pass its test and still not fit the others: that is next exercise's bug hunt.
- The message is where the cat's part and the balloon's part meet, like the time on the party invitation and the food list.

## Common mistakes and quick fixes
- Balloon scripts built under the cat: the cat hides and jumps when clicked. Drag the scripts onto Balloon1 in the sprite list, then delete them from the cat.
- The variable dropdown shows "my variable": pick "pops" in both the set and change blocks.
- The broadcast still says "message1": choose "New message" and type "balloons", or pick "balloons" if it already exists.
- The balloon is invisible after testing "hide": click the "when I receive balloons" script, or click "show" in the Looks list.
- Pops does not reset: "set pops to 0" is missing from the flag script.

## Check-off list
- [ ] The cat has Part 1; Balloon1 has Parts 2 and 3.
- [ ] "broadcast balloons" and "when I receive balloons" use the same name.
- [ ] Each part was tested on its own and checked off on the plan card.
- [ ] With the green flag, the whole party works: "Party time!", balloon, pops go up.
