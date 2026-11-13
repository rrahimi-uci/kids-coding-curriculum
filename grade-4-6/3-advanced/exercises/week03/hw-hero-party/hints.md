## Hint 1: Where to look
Look at `Healer`. It is a finished example, and `Builder` and `Explorer` follow the same pattern. Compare the sentences in the README with the ones in the `TODO` comments. Spell them exactly the same.

## Hint 2: Try this
A child class sets itself up by calling `super().__init__(...)`, which runs the parent's `__init__`. It can also define its own `action` method to replace the parent's. In `take_turn`, use a `for` loop over `self.heroes` and add each result to `actions`.

## Hint 3: Almost there
Each hero class needs two methods. The first looks like `def __init__(self, name):` and then `super().__init__(name, "____")`. The second is `def action(self):` and then `return f"____"`. In `take_turn`, write `for ____ in self.heroes:` and then `actions.append(____)`.
