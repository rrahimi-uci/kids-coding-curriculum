"""TEACHER REFERENCE SOLUTION: Growth Table

What the program does: it prints a table of the WORST-case number of steps for linear search
and for binary search on lists of 10, 100, 1000 and 1000000 items. The child sees that linear
search grows as fast as the list, but binary search barely grows at all (20 steps for a
million items).

Key ideas practiced: how an algorithm's work grows with the size of the problem, a `while`
loop that halves a number, and building a table from a list of rows.

Approach: in the worst case linear search looks at every item, so the answer is `n`. For
binary search we count how many times a number can be halved (using whole-number division)
before it reaches 0. That count is the number of steps binary search needs at most.
"""


def linear_worst(n):
    """Worst case for linear search on n items."""
    # Step 1: if the item is last (or missing), we looked at all n items.
    return n


def halving_steps(n):
    """How many times can we halve n (keeping whole numbers) until it is 0?
    That is the worst case for binary search on n items."""
    steps = 0
    # Step 2: "n // 2" halves and drops the fraction (10 -> 5 -> 2 -> 1 -> 0 is 4 halvings).
    # This n is our own copy, so changing it does not change the caller's number.
    while n > 0:
        n = n // 2
        steps = steps + 1
    return steps


def growth_table(sizes):
    """Return a list of rows (n, linear steps, binary steps)."""
    rows = []
    for n in sizes:
        rows.append((n, linear_worst(n), halving_steps(n)))
    return rows


def format_row(n, linear, binary):
    """Line up the numbers in columns, e.g. '    1000 |    1000 |      10'."""
    # ">8" means "right-aligned in 8 characters", so the columns line up under each other.
    return f"{n:>8} | {linear:>7} | {binary:>7}"


if __name__ == "__main__":
    print(f"{'items':>8} | {'linear':>7} | {'binary':>7}")
    for n, linear, binary in growth_table([10, 100, 1000, 1000000]):
        print(format_row(n, linear, binary))


# Common mistakes children make here:
# - Writing `while n > 1` or `while n >= 1` instead of `while n > 0`: the count is off by one
#   (10 should give 4, 1 should give 1).
# - Forgetting `steps = steps + 1` inside the loop, or putting `return steps` inside it.
# - Using `/` instead of `//`, which never reaches 0 (the numbers just get smaller forever).
# - Thinking the answer for linear search is 1 because "it might be the first item".
#
# Another correct way for halving_steps (bit_length counts the binary digits of n):
#     return n.bit_length()
