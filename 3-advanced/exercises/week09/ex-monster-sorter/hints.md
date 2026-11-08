## Hint 1: Where to look
Start with TODO 1 in `distance`. Each card is a group like `(9, 1, "friendly")`. Only the first two numbers matter here. Then move on to TODO 2, which works like finding the smallest number in a list.

## Hint 2: Try this
For `distance`, subtract one card's fluff from the other's to get `dx`. Do the same with teeth for `dy`. Then use `math.sqrt()` on the squares added together. For `nearest`, use a `for` loop with an `if` that compares two distances.

## Hint 3: Almost there
Distance: `dx = a[____] - b[____]`, `dy = a[____] - b[____]`, then `return math.sqrt(____ * ____ + ____ * ____)`. Nearest: `for card in training:`, then `if distance(card, mystery) ____ distance(best, mystery):` and set `best = ____`.
