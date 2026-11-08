## Hint 1: Where to look
Run it and look at the picture. The flowers sit in one spot and all have the same number of petals. Find the places in `draw_flower` and `petal_turn` that use fixed numbers instead of the values you are given.

## Hint 2: Try this
A full turn is 360 degrees, and the petals share it equally. Use division with `/`. The turtle can jump with `t.goto(x, y)`. A `for` loop with `range()` repeats a set number of times, and that number can be a parameter.

## Hint 3: Almost there
Use `return 360 / ____`. In `draw_flower`, `t.goto(____, ____)` needs the parameters `x` and `y`. You need it before the stem, and the second `goto` should use it too. Change `range(4)` so it reads `range(____)`, using the petal count.
