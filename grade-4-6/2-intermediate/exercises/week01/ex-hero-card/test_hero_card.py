"""Checks for Exercise 1.1 - Hero Card."""


def card_for(run_target, level="4"):
    return run_target(inputs=["Nova", "ice beams", level]).stdout


def test_card_shows_hero_name_and_power(run_target):
    out = card_for(run_target)
    assert "Nova" in out, "The card should show the hero name the player typed (we typed Nova)."
    assert "ice beams" in out, "The card should show the super power too (we typed ice beams). See TODO 2."


def test_next_level_is_a_number(run_target):
    out = card_for(run_target, level="4")
    lines = [line for line in out.splitlines() if "Next level" in line]
    assert lines, "The card should have a 'Next level' line."
    assert "5" in lines[0], (
        "For level 4 the next level is 5. Did you turn the input into a number with int()? (TODO 1)")


def test_power_points_and_health(run_target):
    out = card_for(run_target, level="4")
    assert "40" in out, "Level 4 should give 40 power points (level * 10). See TODO 3."
    assert "50.0" in out, "Level 4 should give 50.0 health (level * 12.5). See TODO 4."


def test_legend_true_or_false(run_target):
    low = card_for(run_target, level="4")
    high = card_for(run_target, level="12")
    assert "False" in low, "A level 4 hero is not a legend yet: the card should say False. See TODO 5."
    assert "True" in high, "A level 12 hero IS a legend: the card should say True. See TODO 5."
