# Teacher reference: Homework 1 - Walk and Talk
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1 (Introduction), Week 1  **Kind:** Scratch (offline app)  **Time:** about 10 minutes
**Big idea:** A show is a list of steps in the right order, and it should start from the same place every time.

## The finished project
Sprite: Cat (or any sprite)
- when green flag clicked
- go to x: -180 y: -100
- say [Hi! I am Pixel Panda] for (2) seconds
- glide (2) secs to x: (0) y: (-100)
- say [Look at this place!] for (2) seconds
- glide (2) secs to x: (180) y: (-100)
- say [Bye!] for (2) seconds

Setup: pick any backdrop with Choose a Backdrop. The child uses their own nickname in the first bubble. Save to your computer as `walk-and-talk`.

## What you should see
- The sprite appears at the left, at (-180, -100), and says hello for 2 seconds.
- It glides for 2 seconds to the middle (0, -100) and says "Look at this place!" for 2 seconds.
- It glides for 2 seconds to the right (180, -100) and says "Bye!".
- The whole show takes about 10 seconds. It restarts from the left on every flag click.

## Talking points
- "Walk it through with your finger: where is the sprite after each block?"
- "Why does it start on the left every time?" (The go to block is the first step after the hat block.)
- "Is the order right? A recipe only works if the steps are in order."

## Common mistakes and quick fixes
- The sprite starts where it last stopped: the go to x: -180 y: -100 block is missing or sits below a glide. Put it directly under the hat block.
- The sprite jumps instead of walking: the child used "go to" instead of "glide".
- The sprite flies up or down: the glide y number is not -100.
- A real name is in the speech bubble: remind the child to use the nickname.
- Nothing runs: blocks not snapped to the hat block.

## Check-off list
- [ ] Script starts with **when green flag clicked**: hat block on top.
- [ ] Sprite always starts on the left: click the flag twice and watch.
- [ ] Steps happen in the planned order: hello, glide to middle, talk, glide to right, bye.
- [ ] Nickname used, not real name.
- [ ] Project saved as `walk-and-talk`.

## Extension answers
Creative extra: add "switch backdrop to [...]" (Looks) between the glides so the sprite walks into a new place each time. Look for these blocks between the glides, and one near the top so the story always starts on the first backdrop. Any backdrops are fine.
