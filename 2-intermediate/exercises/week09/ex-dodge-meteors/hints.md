## Hint 1: Where to look
Do the TODOs in order. Start with `move_player()` and `is_touching()` at the top. They are small functions that only return a value. The turtle keys and the game loop come after that.

## Hint 2: Try this
`clamp()` is already in the file, so use it to keep `x` between `-limit` and `limit`. `math.dist()` gives the distance between two points. Compare that distance to `how_close` with `<`. Arrow keys need `screen.onkey(...)` and then `screen.listen()`. `screen.ontimer(...)` plans the next frame.

## Hint 3: Almost there
Shapes to fill in: `return clamp(____, -limit, limit)`, `return math.dist(____, ____) ____ how_close`, `screen.onkey(____, "Left")`, and `screen.ontimer(____, ____)`. Leave off the `()` after function names.
