## Hint 1: Where to look
Read the triangle loop at the top of `starter.py`. It already works. The square and the hexagon need a loop that looks just like it, with different numbers.

## Hint 2: Try this
In a `for` loop, `range(...)` says how many sides to draw. Inside the loop, `t.forward(...)` draws a side and `t.left(...)` turns. The turn is always 360 divided by the number of sides.

## Hint 3: Almost there
Under each `# TODO`, write a loop like this: `for i in range(____):`. Push the next two lines in by 4 spaces: `t.forward(____)` and `t.left(____)`. Use the side lengths from the comments. Work out each turn with 360 divided by the sides.
