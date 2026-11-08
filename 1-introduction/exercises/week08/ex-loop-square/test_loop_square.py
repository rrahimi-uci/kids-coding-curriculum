"""Checks for Exercise 8.1 - Loop Square."""


def test_uses_a_for_loop(target_path):
    code = target_path.read_text(encoding="utf-8")
    assert "for " in code and "range(" in code, (
        "Use a loop like:  for i in range(4):"
    )


def test_draws_four_equal_sides(run_target):
    t = run_target().turtle
    lengths = sorted({round(line.length) for line in t.lines})
    assert len(t.lines) == 4 and len(lengths) == 1, (
        f"A square has 4 equal sides. Your turtle drew {len(t.lines)} line(s)."
    )


def test_square_is_closed(run_target):
    t = run_target().turtle
    assert t.is_back_at_start(), (
        "The turtle did not get back to the start. Is t.left(90) INSIDE the loop (pushed in 4 spaces)?"
    )
