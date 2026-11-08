## Hint 1: Where to look
Work on TODO 1 first, then TODO 2. Run the program often. The map title and the printed line under it tell you if you are getting closer.

## Hint 2: Try this
A grid is a list of rows, so loop over the rows. Each row is a list, and lists have a `.count()` method that does the counting for you. For `neighbors`, loop over the four steps and add them to `row` and `col`. Only keep a spot if it is inside the map.

## Hint 3: Almost there
Counting: start a `total` at 0, loop over the rows, and add each row's `.count(____)` to the total. Neighbors: for each step, work out `r` and `c`, then use the range test from the TODO before you add the pair `(____, ____)` to `result`.
