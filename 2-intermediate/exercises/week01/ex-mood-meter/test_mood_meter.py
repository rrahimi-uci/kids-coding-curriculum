"""Checks for Exercise 1.2 - Mood Meter."""


def test_super_charged_needs_energy_and_snack(load_target):
    m = load_target()
    assert m.mood_for(9, True) == "Super charged", "Energy 9 with a snack should be 'Super charged'."
    assert m.mood_for(9, False) != "Super charged", (
        "Energy 9 WITHOUT a snack should not be 'Super charged'. Use 'and' in TODO 1.")


def test_ready_to_play_uses_or(load_target):
    m = load_target()
    assert m.mood_for(6, False) == "Ready to play", "Energy 6 (no snack) should be 'Ready to play'. See TODO 2."
    assert m.mood_for(2, True) == "Ready to play", (
        "Energy 2 WITH a snack should be 'Ready to play'. Use 'or' in TODO 2.")


def test_recharge_time(load_target):
    m = load_target()
    assert m.mood_for(3, False) == "Recharge time", "Energy 3 and no snack should be 'Recharge time'."


def test_tip_when_no_snack(run_target):
    with_snack = run_target(inputs=["7", "yes"]).stdout
    no_snack = run_target(inputs=["7", "no"]).stdout
    assert len(no_snack.splitlines()) > len(with_snack.splitlines()), (
        "When the answer is 'no', print an extra tip. Use 'if not had_snack:' (TODO 3).")


def test_meter_shows_the_mood_in_words(run_target):
    t = run_target(inputs=["9", "yes"]).turtle
    words = " ".join(text.text for text in t.texts)
    assert "Super charged" in words, "The meter should write the mood in words, not only show a color."
