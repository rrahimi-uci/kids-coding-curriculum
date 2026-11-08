## Hint 1: Where to look
Work on TODO 1 first, then TODO 2. Each one starts with a variable that is set up for you or a list called `result`. Run the program often. The title and the printed line tell you if you are getting closer.

## Hint 2: Try this
A grid is a list of rows, so loop over the rows. Each row is a list, and lists have a `.count()` method that does the counting for you. For `neighbors`, loop over the four steps and add them to `row` and `col`. Only keep a spot if it is inside the map.

## Hint 3: Almost there
Counting: `total = 0`, then `for ____ in grid:` and `total += ____.count(tile)`. Neighbors: `for step in [...]:` then `r = row + step[____]`, `c = col + step[____]`, and `if 0 <= r < ____ and 0 <= c < ____:` before `result.append(____)`.
