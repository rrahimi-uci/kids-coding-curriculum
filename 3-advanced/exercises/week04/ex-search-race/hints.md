## Hint 1: Where to look
Read `linear_search` first. It counts steps and returns two things. `binary_search` must return the same two things. Look at the `TODO` steps and picture a loop that keeps going while there is still something left to search.

## Hint 2: Try this
Use a `while` loop with `low` and `high`. Each time around, count one step, find the middle with `//`, and compare. A match returns right away. Otherwise move `low` or `high` so half of the list is thrown away.

## Hint 3: Almost there
The shape is `while low <= high:`, then add 1 to `steps`, then `mid = (____ + ____) // 2`. Use `if`, `elif` and `else` on `items[mid]`. If it is too small, set `low = ____`. If it is too big, set `high = ____`.
