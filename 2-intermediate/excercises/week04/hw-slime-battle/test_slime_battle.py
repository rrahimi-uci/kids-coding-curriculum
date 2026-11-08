"""Checks for Homework 4 - Slime Battle."""


def test_hits_needed_exact(load_target):
    m = load_target()
    assert m.hits_needed(30, 10) == 3, "30 health and 10 damage per hit: 3 hits."
    assert m.hits_needed(30, 5) == 6, "30 health and 5 damage per hit: 6 hits."


def test_hits_needed_with_leftover(load_target):
    m = load_target()
    answer = m.hits_needed(30, 7)
    assert answer == 5, f"30 health and 7 damage: 30, 23, 16, 9, 2, then below 0. That is 5 hits, not {answer}."


def test_ask_yes_no_keeps_asking(load_target, inputs):
    m = load_target()
    with inputs(["maybe", "YES"]) as prompts:
        answer = m.ask_yes_no("Again? ")
    assert answer == "yes", f"After 'maybe' then 'YES', the answer should be 'yes', not {answer!r}."
    assert len(prompts) == 2, "'maybe' is not yes or no, so the question should be asked again."
