## Hint 1: Where to look
Start with TODO 1 in `distance`. Each card is a group like `(9, 1, "friendly")`. Only the first two numbers matter here. Then move on to TODO 2, which works like finding the smallest number in a list.

## Hint 2: Try this
For `distance`, find the gap in fluff with `abs()` around the two fluff numbers taken away from each other. Do the same for teeth. Then add the two gaps. For `nearest`, use a `for` loop with an `if` that compares two distances.

## Hint 3: Almost there
Distance: `gap_fluff = abs(a[____] - b[____])`, `gap_teeth = abs(a[____] - b[____])`, then `return ____ + ____`. Nearest: `for card in training:`, then `if distance(card, mystery) ____ distance(best, mystery):` and set `best = ____`.
