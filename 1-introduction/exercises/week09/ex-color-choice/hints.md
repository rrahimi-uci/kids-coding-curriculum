## Hint 1: Where to look
Look at the `if` and `elif` lines in `starter.py`. Orange and blue each have their own block, but green does not. That is why green gives a red error.

## Hint 2: Try this
Add another `elif` just like the blue one, but for green. Then add an `else:` at the end. The `else:` runs when none of the colors above matched, so it catches silly answers like `pizza`.

## Hint 3: Almost there
An extra choice looks like `elif color_name == "____":`, with the color's code on the next line. The catch-all is `else:`. Under it, print a friendly message and set `color` to black. Check the colon and the 4 spaces!
