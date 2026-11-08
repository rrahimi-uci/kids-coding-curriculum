## Hint 1: Where to look
Read `feed` first, since it is already done. It adds or subtracts, then stops the number from going too far. `play` works the same way. Each pet keeps its own `hunger` and `happiness`.

## Hint 2: Try this
In `play`, change `self.happiness` with an `if` that caps it at 10, then do the same for `self.hunger`. In `mood`, use `if` statements in the order the comments list. A `return` ends the function straight away. In `describe`, use an f-string.

## Hint 3: Almost there
For the cap, copy the shape of `feed`: `self.happiness = self.happiness + ____`, then `if self.happiness > ____:` and set it back to the limit. For the sentence, use `return f"____"` and put `{self.____}` pieces inside it. Call the method with `self.mood()`.
