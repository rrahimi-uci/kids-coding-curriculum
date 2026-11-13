"""Checks for Exercise 7.1 - Hello, Python!"""


def printed_lines(run_target):
    return [line for line in run_target().output_lines if line.strip()]


def test_prints_at_least_four_lines(run_target):
    lines = printed_lines(run_target)
    assert len(lines) >= 4, (
        f"Your program printed {len(lines)} line(s). Add print(...) lines until there are 4."
    )


def test_every_line_is_different(run_target):
    lines = printed_lines(run_target)
    repeats = sorted({line for line in lines if lines.count(line) > 1})
    assert not repeats, f"These lines are printed twice: {repeats}. Make each message different."


def test_says_bye_at_the_end(run_target):
    lines = printed_lines(run_target)
    assert lines and "bye" in lines[-1].lower(), (
        "The last line should be a goodbye message with the word 'bye' in it."
    )
