## Hint 1: Where to look
Read the red text from the bottom up. The last line says what went wrong, and the line above it points to the function and line number. Which function is it?

## Hint 2: Try this
In Python, `+` can join text to text, or add numbers to numbers. It cannot mix them. `"Level: " + 4` fails because 4 is a number, not text. Your job is to make the line work for any kind of value.

## Hint 3: Almost there
An f-string puts any value into text, like `f"Score: {points}"`. Rewrite the `return` in `card_line()` as an f-string with the `{____}` and `{____}` in curly braces, and put the `: ` between them as plain text.
