# Teacher reference: Homework 6 - Remix Studio
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1, Week 6 (Review Studio and Checkpoint) homework  **Kind:** Paper plus Scratch (offline app)  **Time:** about 10 minutes
**Big idea:** Every Scratch block has a matching Python line, and an old project can be improved without losing the old version.

## The finished project
Part 1 (paper), Scratch block and its Python line:
- move 50 steps: t.forward(50)
- turn left 90 degrees: t.left(90)
- say "Hi!": print("Hi!")
- repeat 3: for i in range(3):
- set lives to 3: lives = 3

Part 2 (Scratch): open a project from weeks 1-5, add one improvement (a sound effect, a new backdrop, a score or lives variable, a key that does something, a My Block, or a message between two sprites), and save it with a new name ending in `-v2`.

Example improvement (Apple Catch, on the Apple, at the bottom of the forever loop):

Sprite: Apple
- if score = 10 then
  - say [You win!] for (2) seconds
  - stop all

Save as `apple-catch-v2`.

## What you should see
- Part 1: five Python lines as above. Accept small slips (missing colon, capital letters); next week's lesson is about exactly that.
- Part 2: the `-v2` project still does everything the old one did, plus the one new improvement, every time the green flag is clicked.
- The old version is still saved under the old name.

## Talking points
- The card sort is a dictionary: forward is like move, print is like say, for ... range is like repeat.
- Python has brackets, quotes and a colon at the end of lines that hold other lines.
- Save as a new name so the old version stays safe; that is what a remix does.

## Common mistakes and quick fixes
- Python line missing quotes or brackets: t.forward 50 or print(Hi!). Add the brackets and put text in quotes.
- "=" confusion: lives = 3 means "set lives to 3".
- Improvement breaks the old game: undo the last change and test after each small change.
- Saved over the old file: the name must end in `-v2`; if the old one is lost, rebuild or use the older copy.
- "You win" never shows: the if block is outside the forever loop, or it is on the wrong sprite.

## Check-off list
- [ ] I wrote a Python line for every block in Part 1: five lines matching the list above.
- [ ] I added one improvement to an old project: the student can say what they added.
- [ ] I tested it and it works: click the green flag together.
- [ ] I saved it with `-v2` at the end of the name: for example `apple-catch-v2`.
