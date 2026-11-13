"""Checks for Exercise 7.1 - Repeat 4."""


def test_uses_a_for_loop(target_path):
    code = target_path.read_text(encoding="utf-8")
    assert "for " in code and "range(" in code, "Keep the repeat line: for i in range(4):"


def test_draws_enough_equal_sides(run_target):
    lines = run_target().turtle.lines
    lengths = {round(line.length) for line in lines}
    assert len(lines) >= 3 and len(lengths) == 1, (
        f"The turtle drew {len(lines)} side(s). A square needs 4 equal sides. "
        "Change the 2 in range(2) to 4."
    )


def test_shape_is_closed(run_target):
    assert run_target().turtle.is_back_at_start(), (
        "The shape is not closed: the turtle did not get back to the start. "
        "How many times does the repeat go round?"
    )
