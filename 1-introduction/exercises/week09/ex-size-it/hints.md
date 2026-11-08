## Hint 1: Where to look
Look at the line where the program makes `size`, and read the `BUG HUNT` note above it. Then read the red error message in the Shell. It hints that something is the wrong kind of thing.

## Hint 2: Try this
When you type in the Shell, `input()` gives back text, even if you type digits. The turtle needs a real number to walk. Python has a command that changes text into a whole number.

## Hint 3: Almost there
The command is `int( )`. Put the name of the thing that holds what you typed inside the parentheses, like `int(____)`. Use it on the line that sets `size`. Then run it and try a few sizes.
