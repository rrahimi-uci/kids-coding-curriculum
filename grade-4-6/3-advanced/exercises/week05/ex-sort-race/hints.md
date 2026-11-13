## Hint 1: Where to look
Find the `TODO` inside `bubble_sort`. The two loops are already there. Your job is what happens each time the loop looks at one item `result[i]` and its neighbor, `result[i + 1]`.

## Hint 2: Try this
Use an `if` to ask whether the left item is bigger than the right one. If it is, swap them with a Python two-in-one assignment, and count that swap by adding to `swaps`. If it is not bigger, do nothing.

## Hint 3: Almost there
The shape is `if result[i] ____ result[i + 1]:`. Inside it, write `result[i], result[i + 1] = ____, ____`, with the two values in the opposite order. Then write `swaps = swaps + ____`. Compare with how `selection_sort` counts.
