# Exercise 9.1 - Etch-a-Sketch

**Goal:** draw with the arrow keys, like the classic drawing toy.

1. Open `starter.py` and press **Run**. Click the turtle window once, then
   press the Up arrow. Nothing happens!
2. **TODO 1** add `screen.listen()` so the window hears the keys. Run, click
   the window, press Up: the turtle draws a line.
3. **TODO 2** write `go_down()`, `go_left()` and `go_right()`, like `go_up()`.
4. **TODO 3** connect the keys with `screen.onkey(...)`. Careful: write
   `screen.onkey(go_down, "Down")` with **no** `()` after `go_down`.
5. **TODO 4** make `c` shake the drawing clean with `pen.clear()`.
6. Draw your nickname, a house or a maze!

**Keys:** arrows draw, `space` lifts or lowers the pen (the turtle turns into
an arrow when the pen is up), `n` picks the next colour, `c` clears.

**Done looks like:** every key does what the help text at the top says.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add `w` and `s` to make the pen thicker and thinner, or a key that
writes your nickname at the turtle's position.
