# Exercise 3.2 - Shape Family

**Goal:** build a family of shape classes. They all inherit from `Shape`,
but each one overrides `draw()` to make its own picture.

1. Open `starter.py` in Thonny. Read `Shape` and `Square` first.
2. Finish the `TODO`s:
   - `Triangle.draw` - 3 sides, `left(120)`.
   - `Star.draw` - 5 sides, `right(144)`.
   - `Polygon.__init__` - call `super().__init__(x, y, size, color)`.
3. Press **Run**. You should see a 4 x 3 grid of squares, triangles, stars
   and hexagons in 7 colors (each kind also has its own shape, so you can
   tell them apart without color).

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add a `Flower(Shape)` class whose `draw` repeats a small circle
6 times while turning 60 degrees. Add it to `make_pattern`.
