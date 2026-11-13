## Hint 1: Where to look
Look at `next_shape()`. It already uses `next_index()` to move through the list of shapes. Your job is to finish `next_index()` and then write a twin function for colors.

## Hint 2: Try this
The `%` operator gives the remainder after dividing. That makes a number wrap back to 0 when it reaches the length of the list. For `next_color()`, copy the shape function and swap in the color names. Then link keys with `screen.onkey(...)`.

## Hint 3: Almost there
Shapes to fill in: `return (index + ____) % ____`. A twin function looks like `studio[____] = next_index(studio[____], len(____))`, then `stamper.color(____[____])`. Connect it with `screen.onkey(next_color, "____")`, with no `()`.
