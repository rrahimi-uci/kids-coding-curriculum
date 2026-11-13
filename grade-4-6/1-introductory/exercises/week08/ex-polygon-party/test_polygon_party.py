"""Checks for Exercise 8.2 - Polygon Party."""


def shapes_by_color(run_target):
    """Group the lines by color: one color = one shape."""
    groups = {}
    for line in run_target().turtle.lines:
        groups.setdefault(str(line.color).upper(), []).append(line)
    return groups


def test_three_shapes_in_different_colors(run_target):
    groups = shapes_by_color(run_target)
    assert len(groups) >= 3, (
        f"I found {len(groups)} colored shape(s). Draw a triangle, a square and a hexagon."
    )


def test_triangle_square_and_hexagon(run_target):
    sides = sorted(len(lines) for lines in shapes_by_color(run_target).values())
    for wanted, name in [(3, "triangle"), (4, "square"), (6, "hexagon")]:
        assert wanted in sides, (
            f"I could not find a {name} ({wanted} sides). Shapes found have these side counts: {sides}"
        )


def test_every_shape_is_closed(run_target):
    for color, lines in shapes_by_color(run_target).items():
        gap = abs(lines[0].start[0] - lines[-1].end[0]) + abs(lines[0].start[1] - lines[-1].end[1])
        assert gap < 1, (
            f"The {color} shape is not closed. Check the turn: it should be 360 / number of sides."
        )
