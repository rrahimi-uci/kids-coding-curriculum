"""MY TESTS - open this file in Thonny and press the green Run button (F5).

pytest runs every function whose name starts with test_ and tells you
which ones PASSED and which FAILED. A test is a small check:
    assert <something that should be True>, "message if it is not"

1. Change the import below to YOUR program's file name (without .py).
2. Keep the example tests that still fit, delete the others.
3. Write at least 3 tests of YOUR OWN functions (TODO at the bottom).
   Test a normal case AND an edge case (a wall, zero, an empty list...).
"""

import art_studio_template as art
import game_template as game


# ---- Examples for option A (arcade game)

def test_clamp_leaves_a_good_value_alone():
    assert game.clamp(50, -270, 270) == 50


def test_clamp_stops_at_the_wall():
    # Edge case: past the wall on both sides.
    assert game.clamp(500, -270, 270) == 270, "Should stop at the right wall."
    assert game.clamp(-500, -270, 270) == -270, "Should stop at the left wall."


def test_touching_only_when_close():
    assert game.is_touching(0, 0, 10, 10, 25), "These points are close."
    assert not game.is_touching(0, 0, 100, 0, 25), "These points are far apart."


# ---- Example for option B (art studio)

def test_design_to_text_makes_one_line_per_setting():
    text = art.design_to_text({"petals": 6, "color": "#009E73"})
    assert text == "petals=6\ncolor=#009E73\n"


# When you have finished TODO 2 in art_studio_template.py, remove the #
# signs below: this test checks that saving and loading give back the same
# design (a "round trip").
#
# def test_text_to_design_undoes_design_to_text():
#     design = {"petals": 6, "size": 120, "color": "#009E73"}
#     assert art.text_to_design(art.design_to_text(design)) == design


# ---- TODO: YOUR tests. Copy this pattern:
#
# def test_what_should_happen():
#     result = my_function(some, values)
#     assert result == what_i_expect, "a helpful message"


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", __file__])
