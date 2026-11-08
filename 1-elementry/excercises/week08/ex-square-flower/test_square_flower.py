"""Checks for Exercise 8.3 - Square Flower."""


def test_draws_at_least_eight_squares(run_target):
    n = len(run_target().turtle.lines)
    assert n >= 32, (
        f"8 squares need 32 lines, but your turtle drew {n}. "
        "Is the square loop inside the colour loop?"
    )


def test_uses_lots_of_colours(run_target):
    colours = run_target().turtle.colors_used
    assert len(colours) >= 4, (
        f"Your flower uses {len(colours)} colour(s). Put t.color(colour) inside the outer loop."
    )


def test_flower_turns_all_the_way_round(run_target):
    t = run_target().turtle
    assert t.is_back_at_start() and round(t.heading()) % 360 == 0, (
        "The turtle should end where it started, facing the same way. "
        "Did you turn a little (t.left(45)) after each square?"
    )
