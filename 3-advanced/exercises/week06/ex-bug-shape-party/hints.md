## Hint 1: Where to look
Run it. The window opens but nothing is drawn, and there is no error. Look at the function that loops over the shapes and asks each one to draw. How do you normally tell Python to run a method?

## Hint 2: Try this
After the first fix, a crash appears. Read the last line of the red error. It names a missing attribute. Ask which `__init__` should have set it, and what a child class can do to also run its parent's `__init__`.

## Hint 3: Almost there
For the last bug, compare the method names in `Diamond` and `Shape` letter by letter. A child class replaces a parent method only when the names match exactly. For the silent bug, step into `draw_party` and watch whether Thonny ever goes inside a `draw` method.
