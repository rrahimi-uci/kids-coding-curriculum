## Hint 1: Where to look
Look at how `countdown()` is built. It has one part that stops and one part that calls itself. Your two functions need the same two parts. Right now both just return a placeholder.

## Hint 2: Try this
Start with the stopping part. Use an `if` that checks for the tiniest problem and returns its answer right away. Then add a `return` line that does one small step and calls the same function with a smaller input.

## Hint 3: Almost there
For `sum_to`, the shape is `if n <= 0: return ____`, then `return n + sum_to(____)`. For `reverse`, stop when `len(word) <= ____`, then put `word[____]` in front of `reverse(word[:____])`. Fill in each blank by trying tiny inputs by hand.
