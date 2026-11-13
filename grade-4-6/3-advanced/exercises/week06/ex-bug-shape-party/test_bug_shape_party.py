"""Checks for Bug Hunt 4 - Shape Party."""


def test_hexagon_has_its_parent_attributes(load_target):
    art = load_target()
    hexagon = art.Hexagon(10, 20, 40, "#009E73")
    assert getattr(hexagon, "color", None) == "#009E73", (
        "A Hexagon has no color. Its __init__ must call super().__init__(x, y, size, color)."
    )
    assert hexagon.label == "hex", "The Hexagon should still keep its own label."


def test_diamond_draws_four_sides(load_target):
    art = load_target()
    t = art.turtle.Turtle()
    art.Diamond(0, 0, 50, "#E69F00").draw(t)
    assert len(t.lines) == 4, (
        f"A Diamond should draw 4 lines, but drew {len(t.lines)}. Is its draw method spelled exactly 'draw'?"
    )


def test_draw_party_draws_every_shape(load_target):
    art = load_target()
    t = art.turtle.Turtle()
    shapes = [art.Diamond(0, 0, 50, "#E69F00"), art.Diamond(100, 0, 50, "#56B4E9")]
    art.draw_party(shapes, t)
    assert len(t.fills) == 2, f"draw_party should draw 2 filled shapes, but drew {len(t.fills)}. Calling a method needs ()."


def test_whole_program_draws_seven_shapes(run_target):
    t = run_target().turtle
    assert len(t.fills) == 7, f"The party should show 7 filled shapes, but there were {len(t.fills)}."
