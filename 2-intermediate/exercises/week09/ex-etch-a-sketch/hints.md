## Hint 1: Where to look
Read the comments at the top of `starter.py` about handlers. The program sets up what each key should do, then waits. Right now the window is not paying attention to the keyboard yet.

## Hint 2: Try this
`screen.listen()` makes the window hear keys. `screen.onkey(function, "Key")` links a key to a function. New functions like `go_down()` work just like `go_up()` but use a different heading. `pen.clear()` wipes the drawing.

## Hint 3: Almost there
Shape to fill in: `screen.onkey(____, "Down")`. Put the function name there with no `()`. A new function looks like `def go_down():`, then `pen.setheading(____)`, then `pen.forward(STEP)`. Put `screen.listen()` right before `turtle.done()`.
