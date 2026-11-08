"""Checks for Exercise 7.3 - Typo Hunt."""

def run_without_errors(run_target):
    try:
        return run_target()
    except (NameError, AttributeError) as err:
        raise AssertionError(
            f"Python stopped with an error: {err}. "
            "Check capital letters and spelling on the line Thonny shows in red."
        ) from None


def test_runs_without_any_red_errors(run_target):
    run_without_errors(run_target)


def test_prints_the_message(run_target):
    result = run_without_errors(run_target)
    assert "Typo hunt: fixed!" in result.stdout, "The Shell should say: Typo hunt: fixed!"


def test_draws_the_pole_and_flag(run_target):
    result = run_without_errors(run_target)
    n = len(result.turtle.lines)
    assert n == 4, f"The pole and flag need 4 lines, but your turtle drew {n}."
