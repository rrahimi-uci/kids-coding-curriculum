"""Checks for Exercise 7.2 - Fractal tree."""


def segments(t):
    """Distinct line segments drawn (drawing back over a line counts once)."""
    return {frozenset([(round(a[0]), round(a[1])), (round(b[0]), round(b[1]))])
            for a, b in ((line.start, line.end) for line in t.lines)}


def fresh_turtle(program):
    t = program.turtle.Turtle()
    t.setheading(90)
    return t


def test_depth_one_is_a_single_trunk(load_target):
    program = load_target()
    t = fresh_turtle(program)
    program.branch(t, 100, 1)
    n = len(segments(t))
    assert n == 1, f"branch(t, 100, 1) should draw just the trunk (1 line), but it drew {n}."


def test_lines_double_with_each_depth(load_target):
    program = load_target()
    for depth in range(1, 7):
        t = fresh_turtle(program)
        program.branch(t, 100, depth)
        expected = 2 ** depth - 1      # 1, 3, 7, 15, 31, 63
        n = len(segments(t))
        assert n == expected, (f"A tree of depth {depth} should have {expected} branches "
                               f"(1 trunk + two smaller trees), but yours drew {n}. "
                               "Did you call branch() twice with depth - 1?")


def test_branches_get_shorter(load_target):
    program = load_target()
    t = fresh_turtle(program)
    program.branch(t, 100, 3)
    lengths = sorted({round(line.length, 1) for line in t.lines}, reverse=True)
    assert len(lengths) >= 3 and lengths[0] > lengths[-1], \
        "Each level of branches should be shorter than the one below it (length * SHRINK)."


def test_turtle_ends_where_it_started(load_target):
    program = load_target()
    t = fresh_turtle(program)
    program.branch(t, 100, 5)
    assert t.is_back_at_start(), "After drawing a tree the turtle should be back at the bottom of the trunk."
    assert round(t.heading()) == 90, "After drawing a tree the turtle should face the same way as at the start."
