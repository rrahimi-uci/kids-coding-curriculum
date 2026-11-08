## Hint 1: Where to look
Read the three `TODO` comments in `starter.py`. Two of them are inside `play()`, and one is inside `ask_number()`. Fix them one at a time and run after each fix. If the game never stops, press the red Stop button.

## Hint 2: Try this
A `while` loop only stops if something inside it changes, or if you use `break`. To count, make a number bigger each round. To leave the loop early, use `break` inside an `if`.

## Hint 3: Almost there
In `play()`, use `tries = ____ + ____` and then `if result == ____:` with `break` below it. In `ask_number()`, wrap the code in `while True:`. Only `return` when `answer.isdigit()` is True and the number fits between `low` and `high`.
