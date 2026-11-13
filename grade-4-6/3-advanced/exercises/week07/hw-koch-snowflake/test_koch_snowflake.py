"""Checks for Homework 7 challenge - Koch snowflake."""


def draw(program, func, depth):
    t = program.turtle.Turtle()
    func(t, 270, depth)
    return t


def test_depth_zero_is_a_straight_line(load_target):
    program = load_target()
    t = draw(program, program.koch, 0)
    assert len(t.lines) == 1, f"koch(t, 270, 0) should draw 1 straight line, not {len(t.lines)}."


def test_each_depth_has_four_times_the_lines(load_target):
    program = load_target()
    for depth in range(0, 4):
        t = draw(program, program.koch, depth)
        expected = 4 ** depth         # 1, 4, 16, 64
        assert len(t.lines) == expected, (f"A Koch line of depth {depth} should have {expected} pieces, "
                                          f"but yours has {len(t.lines)}. Each level swaps every line for 4 smaller ones.")


def test_koch_line_ends_in_a_straight_line_from_the_start(load_target):
    program = load_target()
    t = draw(program, program.koch, 2)
    x, y = t.position()
    assert abs(x - 270) < 0.5 and abs(y) < 0.5, \
        f"A Koch line should end where a straight line of the same length would (270, 0). Yours ended at ({x:.0f}, {y:.0f})."


def test_snowflake_is_closed(load_target):
    program = load_target()
    t = draw(program, program.snowflake, 2)
    assert len(t.lines) == 3 * 16, f"A depth-2 snowflake has 3 x 16 = 48 lines, not {len(t.lines)}."
    assert t.is_back_at_start(), "The snowflake should end where it started (a closed shape)."
