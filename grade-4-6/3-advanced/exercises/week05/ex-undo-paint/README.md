# Exercise 5.3 - Undo Paint

**Goal:** finish a `Stack` class and use it to give a drawing program an
**undo** button. Every stroke you draw is pushed onto the stack. Pressing
`u` pops the last stroke off and redraws the rest.

1. Open `starter.py` in Thonny.
2. Finish the four `TODO`s in `Stack` (`push`, `pop`, `peek`, `size`).
   The `Painter` class is done: read `move` and `undo` to see how it uses
   the stack.
3. Press **Run**. Click on the turtle window first, then:
   - arrow keys draw,
   - `c` changes color (the color name is written at the top),
   - `u` undoes the last stroke. Press it several times!

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add a REDO: when you undo, push the stroke onto a second stack
called `redo_stack`. Pressing `r` pops from it and draws it again.
