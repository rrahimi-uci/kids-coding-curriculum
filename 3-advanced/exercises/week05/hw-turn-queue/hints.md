## Hint 1: Where to look
Read the comments at the top of `starter.py` about `append()` and `popleft()`. Then look at the two `TODO` notes in `take_turn` and `leave`. Think of the line at a lunch counter.

## Hint 2: Try this
In `take_turn`, take the player off the front with `popleft()`, then put that same player at the back with `append()`. Do not forget to return the name. In `leave`, check with `in` first, because removing someone who is not there causes an error.

## Hint 3: Almost there
For `take_turn`, store `player = queue.____()`, then `queue.____(player)`, then `return ____`. For `leave`, use `if nickname ____ queue:`, then `queue.____(nickname)` and return `True`. Otherwise the function ends with `False`.
