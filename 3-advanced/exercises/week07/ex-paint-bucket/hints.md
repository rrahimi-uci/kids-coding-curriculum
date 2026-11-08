## Hint 1: Where to look
There are three TODOs. Start with TODO 1 in `count_tiles` and ignore the drawing code. Then look at `flood_fill`, which already has one reason to stop: walking off the edge of the grid.

## Hint 2: Try this
For TODO 1, a `for` loop inside another `for` loop visits every cell, and a variable can keep a running total. For TODO 2, add a second `if ...: return` that stops when the cell is not the color being replaced. For TODO 3, call the function itself on each neighbor.

## Hint 3: Almost there
Counting looks like `for ____ in grid:` then `for ____ in ____:` then `if ____ == symbol:`. The second stop is `if grid[row][col] ____ old: return`. The spreading calls look like `flood_fill(grid, row ____ 1, col, old, new)`. Make one call for each of the four directions.
