## Hint 1: Where to look
Look at the `# TODO` comment at the bottom of `starter.py`. It shows a new loop that goes around the square loop. The square loop you already have stays, but it moves inside.

## Hint 2: Try this
Write a `for` loop that goes through every color in `PALETTE`. The first line inside it sets the color. Then the square loop goes inside, pushed in by 4 more spaces. Last, turn a little before the next square starts.

## Hint 3: Almost there
Start with `for color in ____:` and put `t.color(____)` right under it. The old `for side in range(4):` loop comes next, pushed in 4 spaces, with its own lines pushed in 4 more. Finish with `t.left(____)`, lined up with `t.color`.
