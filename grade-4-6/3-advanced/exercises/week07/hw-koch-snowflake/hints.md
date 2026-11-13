## Hint 1: Where to look
Look at the TODO inside `koch()`. The straight `t.forward(length)` at the bottom draws only one plain line. That is why you see triangles. The TODO lists the pieces that should replace it.

## Hint 2: Try this
Delete the straight line and write out the list from the TODO, one line at a time. Drawing a smaller Koch line means calling `koch` again with a shorter length and a depth one smaller. Turning uses `t.left(...)` and `t.right(...)`.

## Hint 3: Almost there
You need four smaller Koch lines, each a fraction of the length and one level shallower. Put a turn between each pair of lines. Read the TODO to see which way to turn and by how many degrees. Keep the early `return` in the base case so the drawing stops.
