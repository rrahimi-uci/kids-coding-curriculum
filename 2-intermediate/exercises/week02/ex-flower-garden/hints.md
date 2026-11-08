## Hint 1: Where to look
Run it and look at the picture. The flowers sit in one spot and all have the same number of petals. Find the places in `draw_flower` and `petal_turn` that use fixed numbers instead of the values you are given.

## Hint 2: Try this
A full turn is 360 degrees, and the petals share it equally. Use division with `/`. The turtle can jump with `t.goto(x, y)`. A `for` loop with `range()` repeats a set number of times, and that number can be a parameter.

## Hint 3: Almost there
Use `return 360 / ____`. In `draw_flower`, replace the fixed numbers with the parameters `x` and `y`: `t.goto(____, ____)`. Change `range(4)` so it reads `range(____)`, using the petal count.
