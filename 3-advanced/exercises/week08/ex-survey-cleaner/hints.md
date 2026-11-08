## Hint 1: Where to look
There are three TODOs, and each one fixes a different kind of mess: extra spaces, empty answers and mixed capitals. Open `favorite_games.csv` and find an example of each. Then run the program and see which mess is still there.

## Hint 2: Try this
Text has helpful methods. `.strip()` removes spaces from both ends, and `.title()` capitalizes each word. Empty text is `""` after stripping. Use `int(...)` to turn text like `"5"` into the number 5. An `if` can return `None` early.

## Hint 3: Almost there
For `to_number`: `text = text.____()`, then `if text == ____: return None`, then `return ____(text)`. For `is_empty`: `return row["favorite_game"].strip() ____ ""`. For TODO 3, add `.____()` after `.strip()` on the game name.
