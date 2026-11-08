# Teacher reference: Exercise 1.1 - Hello, Cat!
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1 (Introduction), Week 1  **Kind:** Scratch (offline app)  **Time:** about 8 minutes
**Big idea:** A program is a list of exact steps, and the computer does them in the order you wrote them.

## The finished project
Sprite: Cat (the default sprite; one script)
- when green flag clicked
- go to x: 0 y: 0
- say [Hi! I am Pixel Panda] for (2) seconds
- move (100) steps
- play sound [Meow] until done
- say [Bye!] for (2) seconds

Setup: no extension and no backdrop needed. In the first say block the child types "Hi! I am" plus their own nickname (Pixel Panda is only the example). In "move (10) steps" the child changes 10 to 100. Save with File > Save to your computer, folder `Scratch Projects`, name `hello-cat`.

## What you should see
- On the green flag the cat jumps to the middle of the stage (0, 0).
- A bubble says "Hi! I am <nickname>" for 2 seconds.
- The cat walks 100 steps to the right (it ends at about x: 100, y: 0).
- The Meow sound plays all the way to the end, then the bubble "Bye!" shows for 2 seconds.
- Clicking the flag again replays the same show, starting from the middle.

## Talking points
- "A program is like a recipe: the steps must be in the right order and nothing can be missing."
- "The cat can only do what the blocks say. It does not guess what you meant."
- "Why do we start with go to x: 0 y: 0?" (So the show always begins in the same place.)
- "We use a nickname, never a real name, in our projects."

## Common mistakes and quick fixes
- Nothing happens when the flag is clicked: blocks are not snapped under the hat block. Drag until the gray shadow appears, then let go.
- Nothing happens (another cause): the wrong sprite is selected. Click the cat in the sprite pane.
- Two separate scripts both start with the flag and things happen at once: join them into one stack.
- The speech bubble has a real name in it: gently remind the child to use the nickname.
- The cat has wandered off the stage on repeated clicks: the go to x: 0 y: 0 block is missing or is below the move block.
- The Meow does not finish before "Bye!": the child used "start sound" instead of "play sound ... until done".

## Check-off list
- [ ] Script starts with **when green flag clicked**: the hat block is on top of the stack.
- [ ] All blocks snapped in one stack: dragging the hat block moves the whole column together.
- [ ] Steps in the right order: go to, say hello, move 100, Meow, say Bye.
- [ ] Nickname used, not real name: read the first speech bubble.
- [ ] Saved in `Scratch Projects`: ask the child to show the file in that folder.
