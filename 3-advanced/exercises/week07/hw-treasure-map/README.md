# Homework 7 - Treasure map

**Goal:** practice grids (lists of lists) with a game map.

```
~ water   ^ mountain   . grass   T treasure   S start
```

1. Open `starter.py` and press **Run**. The map appears and the program
   prints where the start is.
2. TODO 1: finish `count_tiles(grid, tile)`. The words above the map should
   then say "Treasure on this map: 2".
3. TODO 2: finish `neighbors(grid, row, col)`. It gives the cells up, down,
   left and right - but never cells off the edge of the map.

**Math helper:** each step is a pair (row change, column change). `-1` is
read "minus one" and means "one back": `(-1, 0)` is one row up, `(1, 0)` is
one row down, `(0, -1)` is one column left and `(0, 1)` is one column right.
A cell is on the map when `0 <= r < len(grid)`. Read that as: "r is 0 or
more, AND r is less than the number of rows". Do the same check for `c`
with `len(grid[0])`, the number of columns.

**Done looks like:** the Shell shows

```
Start is at (2, 3)
Next to the start: [(1, 3), (3, 3), (2, 2), (2, 4)]
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** draw your own island by changing `MAP_TEXT`. Keep every line the
same length!
