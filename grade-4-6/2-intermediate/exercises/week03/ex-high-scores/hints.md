## Hint 1: Where to look
Run it and read what prints. The first three scores in the list are not the biggest three. Look at `top_three` first, then at how `print_leaderboard` shows the result.

## Hint 2: Try this
`sorted()` puts a list in order and gives a new list. Add `reverse=True` to put the biggest first. Then `[:3]` keeps the first three. To print, loop with an index so you can pair each place name with its score.

## Hint 3: Almost there
In `top_three`, write `best = sorted(____, reverse=____)`, then `return best[:____]`. In `print_leaderboard`, use `for i in range(len(____)):` and `print(f"{places[____]}: {best[____]}")`.
