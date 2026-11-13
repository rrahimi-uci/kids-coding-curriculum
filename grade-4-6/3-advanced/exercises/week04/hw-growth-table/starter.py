# Growth Table - YOUR version
# How many steps does each search need in the WORST case?
#   linear search: it may have to look at every item -> n steps
#   binary search: it halves the list until nothing is left
# Finish the TODOs, then open check_my_work.py and press Run.


def linear_worst(n):
    """Worst case for linear search on n items."""
    # TODO 1: linear search may look at every single item. Return that number.
    return 0


def halving_steps(n):
    """How many times can we halve n (keeping whole numbers) until it is 0?
    That is the worst case for binary search on n items."""
    steps = 0
    # TODO 2: while n is more than 0: n = n // 2 and add 1 to steps
    return steps


def growth_table(sizes):
    """Return a list of rows (n, linear steps, binary steps). (Already done!)"""
    rows = []
    for n in sizes:
        rows.append((n, linear_worst(n), halving_steps(n)))
    return rows


def format_row(n, linear, binary):
    """Line up the numbers in columns, e.g. '    1000 |    1000 |      10'."""
    return f"{n:>8} | {linear:>7} | {binary:>7}"


if __name__ == "__main__":
    print(f"{'items':>8} | {'linear':>7} | {'binary':>7}")
    for n, linear, binary in growth_table([10, 100, 1000, 1000000]):
        print(format_row(n, linear, binary))
