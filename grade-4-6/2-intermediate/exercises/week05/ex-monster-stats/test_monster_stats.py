"""Checks for Exercise 5.1 - Monster Stats."""


def test_stat_report_lists_every_key(load_target):
    m = load_target()
    report = m.stat_report({"name": "Zap", "health": 30})
    assert report == ["name: Zap", "health: 30"], f"Expected ['name: Zap', 'health: 30'] but got {report}. (TODO 1)"


def test_level_up(load_target):
    m = load_target()
    monster = m.level_up(m.make_monster("Zap"))
    assert monster["level"] == 2, "After one level up the monster should be level 2."
    assert monster["health"] == 40, f"Health should go from 30 to 40, not {monster['health']}. (TODO 2)"
    assert monster["attack"] == 6, f"Attack should go from 4 to 6, not {monster['attack']}. (TODO 2)"


def test_get_stat_that_exists(load_target):
    m = load_target()
    assert m.get_stat(m.make_monster("Zap"), "speed") == 2, "A new monster has speed 2."


def test_get_stat_that_is_missing(load_target):
    m = load_target()
    try:
        answer = m.get_stat(m.make_monster("Zap"), "magic")
    except KeyError:
        raise AssertionError("get_stat crashed with KeyError for 'magic'. Check 'if stat in monster:' first. (TODO 3)")
    assert answer == 0, f"A missing stat should give 0, not {answer}."
