## Hint 1: Where to look
Run it and look at the picture. Only the top row shows up, because `draw_grid()` uses `grid[0]` and nothing else. Read `TODO 1` and `TODO 2` in `starter.py`.

## Hint 2: Try this
A nested loop is a loop inside a loop. The outer loop picks one row, and the inner loop walks along that row. In `draw_grid()`, the outer loop also has to move `y` down after each row.

## Hint 3: Almost there
Use this shape: `for ____ in grid:` then, indented below it, `for ____ in ____:`. In `count_pixels()`, add 1 to `count` when `pixel == ____`. In `draw_grid()`, finish each row with `y = y - ____`.
