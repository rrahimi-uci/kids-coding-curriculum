## Hint 1: Where to look
Read the three rules for the door at the top of the starter file. Right now `door_opens()` only checks the key. Does it ever look at the level?

## Hint 2: Try this
Join two true-or-false checks with `and` when both must be true. Join them with `or` when either one is enough. Brackets `( )` keep a pair of checks together. For the message, an f-string puts a variable inside curly braces.

## Hint 3: Almost there
The `if` line has this shape: `if (____ and level >= ____) or level >= ____:`. For the welcome, start the text with `f` and put the hero name inside braces, like `print(f"... {____} ...")`.
