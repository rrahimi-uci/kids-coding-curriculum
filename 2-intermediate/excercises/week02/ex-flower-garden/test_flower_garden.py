"""Checks for Exercise 2.2 - Flower Garden."""


def test_petal_turn_returns_the_angle(load_target):
    m = load_target()
    assert m.petal_turn(6) == 60, f"6 petals need a turn of 360 / 6 = 60 degrees, not {m.petal_turn(6)}."
    assert m.petal_turn(5) == 72, "5 petals need a turn of 360 / 5 = 72 degrees."


def test_flower_has_the_right_number_of_petals(load_target):
    m = load_target()
    t = m.turtle.Turtle()
    m.draw_flower(t, 0, 0, 7, m.PURPLE)
    assert len(t.fills) == 7, f"draw_flower(..., 7, ...) should draw 7 petals, but drew {len(t.fills)}."


def test_flower_is_drawn_at_x_y(load_target):
    m = load_target()
    t = m.turtle.Turtle()
    m.draw_flower(t, 100, -50, 5, m.SKY)
    starts = {(round(f.points[0][0]), round(f.points[0][1])) for f in t.fills}
    assert starts == {(100, -50)}, (
        "The petals of draw_flower(t, 100, -50, ...) should start at (100, -50). "
        f"Yours started at {sorted(starts)}. Use goto(x, y).")


def test_garden_has_three_flowers(run_target):
    t = run_target().turtle
    assert len(t.dots) >= 3, "The garden should have at least 3 flowers (each has a dot in the middle)."
    assert len({f.color for f in t.fills}) >= 2, "Use at least 2 different petal colours."
