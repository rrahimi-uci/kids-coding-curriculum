## Hint 1: Where to look
Run the program and watch both shapes. The blue square and the orange star each have one bug. Look at the two `for` loops in `starter.py` one at a time.

## Hint 2: Try this
For the square, count its sides, then check the number inside `range(...)`. For the star, look at the spaces at the start of each line. A line only belongs to the loop if it is pushed in under the `for` line.

## Hint 3: Almost there
Square: the number in `range(____)` should match the number of sides. Star: the turning line should start with the same number of spaces as `t.forward(150)`. Fix one bug, press Run, then fix the other.
