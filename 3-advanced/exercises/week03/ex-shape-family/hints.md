## Hint 1: Where to look
Read `Square` first. It is a finished example. `Triangle` and `Star` look almost the same, but with different sides and turns. Then look at `Polygon.__init__`. It saves `sides` but forgets something.

## Hint 2: Try this
Copy the pattern from `Square.draw`: call `self.start(t)`, fill, and repeat. Use `range(...)` for the number of sides. For `Polygon`, call `super().__init__(...)` so the parent saves `x`, `y`, `size` and `color`. Turtle uses `left` and `right` to turn.

## Hint 3: Almost there
A shape draws like this: `self.start(t)`, `t.begin_fill()`, `for _ in range(____):`, then `t.forward(self.size)` and `t.left(____)` or `t.right(____)`, then `t.end_fill()`. Use the sides and turn from the README. In `Polygon`, write `super().__init__(____, ____, ____, ____)`.
