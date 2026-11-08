"""Checks for Exercise 9.1 - Etch-a-Sketch.

The checks press keys for you with screen.press("Up") and look at the pen.
"""


def start(run_target):
    result = run_target()
    return result.screen, result.namespace["pen"]


def test_the_window_listens_for_all_four_arrows(run_target):
    screen, pen = start(run_target)
    assert screen.listening, "The window is not listening for keys. Add screen.listen() (TODO 1)."
    missing = [key for key in ["Up", "Down", "Left", "Right"] if key not in screen.key_handlers]
    assert not missing, f"Nothing happens for these keys yet: {missing}. Connect them with screen.onkey(...)."


def test_each_arrow_moves_the_right_way(run_target):
    screen, pen = start(run_target)
    for key, check in [("Up", lambda x, y: y > 0 and x == 0),
                       ("Right", lambda x, y: x > 0 and y == 0),
                       ("Down", lambda x, y: y < 0 and x == 0),
                       ("Left", lambda x, y: x < 0 and y == 0)]:
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        screen.press(key)
        x, y = pen.position()
        assert check(x, y), f"After pressing {key} from the middle, the pen went to ({x:.0f}, {y:.0f}). Check its heading."


def test_space_lifts_and_lowers_the_pen(run_target):
    screen, pen = start(run_target)
    screen.press("space")
    before = len(pen.lines)
    screen.press("Right")
    assert len(pen.lines) == before, "After pressing space once, moving should NOT draw (the pen is up)."
    screen.press("space")
    screen.press("Right")
    assert len(pen.lines) == before + 1, "After pressing space again, moving should draw again."


def test_c_shakes_the_drawing_clean(run_target):
    screen, pen = start(run_target)
    screen.press("Up")
    screen.press("Right")
    assert pen.lines, "Pressing arrows should draw lines."
    screen.press("c")
    assert not pen.lines, "After pressing c, the drawing should be gone (pen.clear())."


def test_n_changes_the_color(run_target):
    screen, pen = start(run_target)
    first = pen.pencolor()
    screen.press("n")
    assert pen.pencolor() != first, "Pressing n should change the pen color."
