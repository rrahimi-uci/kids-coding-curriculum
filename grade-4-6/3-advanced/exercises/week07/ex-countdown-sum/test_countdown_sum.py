"""Checks for Exercise 7.1 - Recursion warm-up."""


def test_countdown_prints_numbers_then_liftoff(load_target, capsys):
    program = load_target()
    program.countdown(3)
    lines = capsys.readouterr().out.split()
    assert lines[:3] == ["3", "2", "1"], f"countdown(3) should print 3, 2, 1 first. It printed: {lines}"
    assert "Liftoff!" in lines[-1], "After the numbers, countdown should print Liftoff!"


def test_sum_to_gives_the_right_answers(load_target):
    program = load_target()
    for n, expected in [(0, 0), (1, 1), (5, 15), (10, 55), (100, 5050)]:
        got = program.sum_to(n)
        assert got == expected, f"sum_to({n}) should be {expected}, but your function gave {got}."


def test_sum_to_calls_itself(load_target):
    program = load_target()
    original = program.sum_to
    calls = []

    def spy(n):
        calls.append(n)
        return original(n)

    program.sum_to = spy  # recursive calls now go through the spy
    original(4)
    assert len(calls) >= 1, ("sum_to should call itself (recursion) with a smaller number, "
                             "like sum_to(n - 1). Yours did not call itself.")


def test_reverse_flips_words(load_target):
    program = load_target()
    for word, expected in [("", ""), ("a", "a"), ("turtle", "eltrut"), ("level", "level")]:
        got = program.reverse(word)
        assert got == expected, f"reverse({word!r}) should be {expected!r}, but your function gave {got!r}."
