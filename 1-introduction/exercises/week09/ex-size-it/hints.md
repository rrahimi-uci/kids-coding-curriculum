## Hint 1: Where to look
Look at the line where the program makes `size`, and read the `BUG HUNT` note above it. Then read the red error message in the Shell. It tells you what kind of thing the turtle got by mistake.

## Hint 2: Try this
When you type in the Shell, `input()` gives back text, even if you type digits. The turtle needs a real number to walk. Python has a command that changes text into a whole number.

## Hint 3: Almost there
The command is `int( )`. Put the thing you want to change inside the parentheses, like `int(____)`. Use it on the line that sets `size`, and put the answer to the question inside. Then run it and try a few sizes.
