## Hint 1: Where to look
Find the two `TODO` notes in `starter.py`. Right now `check` always says "correct" and `next_guess` always picks the lowest number. Fix `check` first, then the bot's guessing.

## Hint 2: Try this
In `check`, compare `guess` with `secret` using `<` and `>` inside `if` and `elif`. In `next_guess`, the middle of two numbers comes from adding them and dividing. Use `//` so the result stays a whole number.

## Hint 3: Almost there
For `check`, the shape is `if guess ____ secret: return "____"`, then an `elif` for the other direction, then a final `return`. For `next_guess`, write `return (____ + ____) // 2` using the two numbers the function receives.
