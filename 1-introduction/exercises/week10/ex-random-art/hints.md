## Hint 1: Where to look
Look inside the `for` loop in `starter.py`. Every round uses the same four values, so all 30 bubbles land in the same spot. Find the `# TODO` notes next to `x`, `y`, `size` and `color`.

## Hint 2: Try this
The `random` module is already imported at the top. It can pick a random whole number between two limits. It can also pick one item from a list. Use those so each round gets new values.

## Hint 3: Almost there
For a number, use `random.randint(____, ____)` with the smallest and biggest allowed values. For a color, use `random.choice(____)` with the list name inside. Put one of these on each of the four lines inside the loop, in place of the fixed values.
