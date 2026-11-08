## Hint 1: Where to look
There are three `TODO` notes. Start with `name_of`. It is a small helper that `alphabetical` already uses. Look at how `points_of` is written right above it, and copy its idea.

## Hint 2: Try this
For `name_of`, a string has a method that makes all letters lower case. For `top_scores`, `sorted(..., key=..., reverse=True)` puts the best first, and a slice like `[:3]` keeps only the first few. For `rank_lines`, compare points with `previous_points`.

## Hint 3: Almost there
Use `return entry[0].____()` for `name_of`. In `top_scores`, save the sorted list, then `return best_first[:____]`. In `rank_lines`, wrap `place = position` in `if entry[1] ____ previous_points:` so ties keep the old place.
