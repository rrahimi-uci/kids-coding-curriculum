## Hint 1: Where to look
Run the program and read the last line of the red error message. It tells you the line number to look at. Fix that one first, then run again to find the next one.

## Hint 2: Try this
Inside a class, a method gets the object it belongs to as its first input, and it reaches the object's own data through `self`. Look at how `__init__` and `add` use `self`, and compare them with the other methods.

## Hint 3: Almost there
Check three places. Look at the `def` line of `add` and ask what it is missing. Look inside `undo_last` at `score -= last`. Look at `{nickname}` in `report`. Compare each with `self.score` and `self.nickname` as written in `__init__`.
