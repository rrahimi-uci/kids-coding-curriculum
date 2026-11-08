"""Checks for Homework 9 - Stamp Studio (keys are pressed with screen.press)."""


def test_next_index_goes_round_the_list(load_target):
    studio = load_target()
    assert studio.next_index(0, 4) == 1, "In a list of 4, the next position after 0 is 1."
    assert studio.next_index(2, 4) == 3, "In a list of 4, the next position after 2 is 3."
    nxt = studio.next_index(3, 4)
    assert nxt == 0, f"In a list of 4, after the last position (3) we go back to 0, not {nxt}."


def test_arrows_and_s_make_a_stamp(run_target):
    result = run_target()
    stamper = result.namespace["stamper"]
    result.screen.press("Right")
    result.screen.press("s")
    assert len(stamper.stamps) == 1, "Pressing s should stamp once."
    (x, y), _colour, _shape = stamper.stamps[0]
    assert x > 0, "After pressing Right, the stamp should be to the right of the middle."


def test_p_and_n_change_the_shape_and_colour(run_target):
    result = run_target()
    screen, stamper = result.screen, result.namespace["stamper"]
    screen.press("s")
    screen.press("p")
    screen.press("n")
    screen.press("s")
    (_p1, colour1, shape1), (_p2, colour2, shape2) = stamper.stamps[:2]
    assert shape2 != shape1, "After pressing p, the next stamp should have a different shape."
    assert colour2 != colour1, "After pressing n, the next stamp should have a different colour."
