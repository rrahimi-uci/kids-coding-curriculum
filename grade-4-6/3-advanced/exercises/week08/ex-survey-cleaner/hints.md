## Hint 1: Where to look
There are three TODOs, and each one fixes a different kind of mess: extra spaces, empty answers and mixed capitals. Open `favorite_games.csv` and find an example of each. Then run the program and see which mess is still there.

## Hint 2: Try this
Text has helpful methods. `.strip()` removes spaces from both ends, and `.title()` capitalizes each word. Empty text is `""` after stripping. Use `int(...)` to turn text like `"5"` into the number 5. An `if` can return `None` early.

## Hint 3: Almost there
For `to_number`: strip the text first. If nothing is left, return `None`. Otherwise turn the text into a number with `____(text)`. For `is_empty`: compare the stripped game name with empty text. For TODO 3, add `.____()` after `.strip()` on the game name.
