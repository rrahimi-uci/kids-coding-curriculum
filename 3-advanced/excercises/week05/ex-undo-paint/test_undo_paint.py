"""Checks for Exercise 5.3 - Undo Paint."""


def test_stack_is_last_in_first_out(load_target):
    paint = load_target()
    stack = paint.Stack()
    for plate in ["red plate", "blue plate", "green plate"]:
        stack.push(plate)
    assert stack.size() == 3, f"After 3 pushes the stack should hold 3 items, not {stack.size()}."
    assert stack.peek() == "green plate", "peek() should show the LAST item pushed (the top)."
    assert stack.size() == 3, "peek() must not take the item off."
    popped = [stack.pop(), stack.pop(), stack.pop()]
    assert popped == ["green plate", "blue plate", "red plate"], f"Items should come off in reverse order. Got {popped}"


def test_pop_on_empty_stack(load_target):
    paint = load_target()
    stack = paint.Stack()
    assert stack.is_empty(), "A new stack should be empty."
    assert stack.pop() is None and stack.peek() is None, "pop() and peek() on an empty stack should return None, not crash."


def test_undo_removes_only_the_last_stroke(load_target):
    paint = load_target()
    pen = paint.turtle.Turtle()
    painter = paint.Painter(pen)
    painter.right()
    painter.up()
    painter.undo()
    assert painter.history.size() == 1, "After 2 strokes and 1 undo, 1 stroke should be left on the stack."
    assert len(pen.lines) == 1, f"After undo the picture should show 1 line, not {len(pen.lines)}."
    assert (painter.x, painter.y) == (paint.STEP, 0), "After undo the painter should be back at the end of the first stroke."


def test_keys_work_in_the_real_program(run_target):
    screen = run_target().screen
    for key in ["Right", "Right", "Up", "u"]:
        screen.press(key)
    lines = screen.all_lines
    assert len(lines) == 2, f"Right, Right, Up, then u (undo) should leave 2 strokes on screen, not {len(lines)}."
