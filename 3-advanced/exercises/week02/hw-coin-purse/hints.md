## Hint 1: Where to look
Look at the three methods with a `TODO`: `add`, `can_afford` and `spend`. Notice that `spend` is built on top of `can_afford`. Fix `can_afford` first. Then compare your output with the README.

## Hint 2: Try this
`self.coins` is the number the purse remembers. Use `if` with a comparison like `>` or `>=` to check a number. In `spend`, call `self.can_afford(price)` rather than doing the math again. A `return` gives back `True` or `False`.

## Hint 3: Almost there
Use these shapes. In `add`, write `if amount > ____:` and then `self.coins = self.coins + ____`. In `can_afford`, write `return self.coins ____ price`. In `spend`, write `if self.can_afford(price):`, change the coins, `return True`, and otherwise `return False`.
