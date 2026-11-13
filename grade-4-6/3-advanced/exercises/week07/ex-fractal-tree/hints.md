## Hint 1: Where to look
Find the five TODO comments inside `branch()`. They sit right after the trunk is drawn. Read them in order and picture the turtle: it turns, draws a small tree, turns again, draws another, then turns back.

## Hint 2: Try this
Each TODO becomes one line of code. Turning uses `t.left(...)` and `t.right(...)`. A smaller tree is a call to `branch` itself, with a shorter `length` and a `depth` that is one less. The file already has a `SHRINK` number for that.

## Hint 3: Almost there
The five lines go in this order: `t.left(____)`, `branch(t, length * ____, depth - ____)`, `t.right(____ * ANGLE)`, the same `branch` call again, then `t.left(____)`. The last turn should undo what is left over, so the turtle faces up again.
