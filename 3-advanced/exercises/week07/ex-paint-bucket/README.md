# Exercise 7.3 - Paint bucket (flood fill)

**Goal:** make the paint-bucket tool from drawing apps, using a grid and
recursion.

The picture is a **grid**: a list of rows, and each row is a list of cells.
`grid[row][col]` is one cell (row 0 is the top). Click a cell and the paint
spreads to every touching cell of the same color - but not through walls.

**Steps**

1. Open `starter.py` and press **Run**. Click inside a shape: nothing
   happens yet. Close the window.
2. TODO 1: finish `count_tiles(grid, symbol)` with two nested loops.
3. TODO 2: add the second base case: stop if the cell is not the `old`
   color.
4. TODO 3: add four recursive calls: up (`row - 1`), down (`row + 1`),
   left (`col - 1`) and right (`col + 1`). Row 0 is the top, so "up" means
   a smaller row number.
5. Run again. Press keys **1-5** to pick a paint, then click to fill.
   Every paint has a letter (O, S, G, Y, P) as well as a color.

**Done looks like:** clicking inside a box fills only that box. Clicking
inside the big box at the top paints its 8 inside squares. Clicking the tiny
box on the right paints only 1 square. Clicking outside the boxes fills the
whole white background, but never the black walls.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** draw your own picture by changing the `PICTURE` strings.

**Stretch (optional): fill with a queue (BFS).** Recursion dives down one
path first. *Breadth-first search* (BFS) fills in **rings**, nearest squares
first, like ripples in a pond. It uses a queue (first in, first out) that
holds the squares waiting to be visited. Write a second function under
`paint`, called `flood_fill_queue(grid, row, col, old, new)`, that paints
exactly the same cells as `flood_fill`:

1. `from collections import deque`, then `queue = deque([(row, col)])` and
   paint that first cell right away (`grid[row][col] = new`).
2. `while queue:` take the front square: `r, c = queue.popleft()`.
3. For each of its four neighbors that is on the grid and still `old`:
   paint it (so it is never added twice), then `queue.append((nr, nc))`.
4. Change `paint` to call `flood_fill_queue`. The game should look the same.

Hint: if your fill never ends, check that you paint a square *when you add
it* to the queue, not when you take it out. Bonus: BFS never gives a
`RecursionError`, and if you count the rings you get the distance from
the click to every square.

`check_my_work.py` only checks the stretch if you wrote it.
