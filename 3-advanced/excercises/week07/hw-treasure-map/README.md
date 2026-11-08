# Homework 7 - Treasure map

**Goal:** practise grids (lists of lists) with a game map.

```
~ water   ^ mountain   . grass   T treasure   S start
```

1. Open `starter.py` and press **Run**. The map appears and the program
   prints where the start is.
2. TODO 1: finish `count_tiles(grid, tile)`. The title should then say
   "Treasure on this map: 2".
3. TODO 2: finish `neighbours(grid, row, col)`. It gives the cells up, down,
   left and right - but never cells off the edge of the map.

**Done looks like:** the program prints
`Next to the start: [(1, 3), (3, 3), (2, 2), (2, 4)]`.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** draw your own island by changing `MAP_TEXT`. Keep every line the
same length!
