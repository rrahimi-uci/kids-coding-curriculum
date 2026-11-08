## Hint 1: Where to look
Run the program and read the very last line of the red error. It names two kinds of data that do not mix. Then look at which line of `print_card` has a `+` in it.

## Hint 2: Try this
`input()` always gives back text, even when you type digits. Python has a built-in, `int()`, that turns text into a whole number. Use it where the level is typed in. For the new lines, copy the shape of the `HERO` line.

## Hint 3: Almost there
Wrap the typed text like this: `level = ____(input("..."))`. Then make each new variable on its own line, such as `health = level * ____`. Show it with `print(f"  Label:  {____}")`. A comparison like `level >= 10` gives True or False.
