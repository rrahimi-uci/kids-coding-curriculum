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
4. TODO 3: add four recursive calls: up, down, left, right.
5. Run again. Press keys **1-5** to pick a paint, then click to fill.
   Every paint has a letter (O, S, G, Y, P) as well as a color.

**Done looks like:** clicking inside a box fills only that box. Clicking
outside fills the whole background but never the walls.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** draw your own picture by changing the `PICTURE` strings.
