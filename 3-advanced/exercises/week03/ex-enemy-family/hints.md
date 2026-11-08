## Hint 1: Where to look
Read `Enemy` and `Guard` first. `Guard` is a finished example of a child class that does its own `move`. If Run shows an `AttributeError` about `name`, read the message closely. It points at `Sprinter`.

## Hint 2: Try this
A child class can reuse its parent's code with `super()`. Calling `super().move()` runs the parent's version of `move`. Calling `super().__init__(...)` runs the parent's setup. `move_all` needs a loop that asks each enemy to move.

## Hint 3: Almost there
In `Sprinter.__init__`, call `super().__init__(____, ____, ____)` before saving `speed`. In `Zigzagger.move`, call `super().move()`, then use `if self.steps % 2 == ____:` to choose up or down. In `move_all`, write `for ____ in enemies:` and call `.move()`.
