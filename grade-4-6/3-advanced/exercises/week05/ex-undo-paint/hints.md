## Hint 1: Where to look
Only the `Stack` class needs your help. It has four methods marked `TODO`. Each one works with the list called `self.items`. The end of that list is the top of the stack.

## Hint 2: Try this
A Python list can add to its end with `append`, and remove and return its last item with `pop`. For `pop` and `peek`, check `is_empty()` first so an empty stack gives back `None`. For `size`, use the built-in that counts items.

## Hint 3: Almost there
`push` is `self.items.____(item)`. For `pop` and `peek`, use `if self.is_empty(): return ____`, then return `self.items.____()` or `self.items[____]`. For `size`, write `return ____(self.items)`.
