"""Checks for Exercise 3.2 - Shape Family."""


def draw_one(art, shape):
    t = art.turtle.Turtle()
    shape.draw(t)
    return t


def equal_sides(t):
    return len({round(line.length) for line in t.lines}) == 1


def test_triangle_draws_three_equal_sides(load_target):
    art = load_target()
    t = draw_one(art, art.Triangle(0, 0, 80, "#E69F00"))
    assert len(t.lines) == 3, f"A Triangle should draw 3 lines, but drew {len(t.lines)}. Did you override draw()?"
    assert equal_sides(t) and t.is_back_at_start(), "The triangle should have 3 equal sides and be closed (left 120)."


def test_star_draws_five_points(load_target):
    art = load_target()
    t = draw_one(art, art.Star(0, 0, 90, "#56B4E9"))
    assert len(t.lines) == 5, f"A Star should draw 5 lines, but drew {len(t.lines)}."
    assert equal_sides(t) and t.is_back_at_start(), "The star's 5 lines should be equal and end where they started (right 144)."


def test_polygon_uses_super_init(load_target):
    art = load_target()
    hexagon = art.Polygon(10, 20, 40, "#009E73", 6)
    assert getattr(hexagon, "colour", None) == "#009E73", (
        "Polygon has no colour. Call super().__init__(x, y, size, colour) in Polygon's __init__."
    )
    t = draw_one(art, hexagon)
    assert len(t.lines) == 6, f"A 6-sided Polygon should draw 6 lines, not {len(t.lines)}."


def test_same_method_different_drawings(load_target):
    art = load_target()
    shapes = [art.Square(0, 0, 50, "#E69F00"), art.Triangle(0, 0, 50, "#E69F00"), art.Star(0, 0, 50, "#E69F00")]
    counts = [len(draw_one(art, s).lines) for s in shapes]
    assert counts == [4, 3, 5], f"Square, Triangle and Star should draw 4, 3 and 5 lines. Yours drew {counts}."
