"""TEACHER REFERENCE SOLUTION: Search Race

What the program does: it finds a number in a sorted list in two ways, linear search (look at
every item from the start) and binary search (look in the middle and throw away half), and it
counts the steps each way needs. It prints a table that shows binary search winning more and
more as the list gets bigger.

Key ideas practiced: counting steps to compare two algorithms, the binary search loop with
`low`, `high` and `mid`, and why a list must be sorted for binary search.

Approach: `low` and `high` mark the part of the list that could still hold the target. Each
step looks at the middle item. If it is too small, everything to its left is too small as
well, so `low` jumps past the middle; if it is too big, `high` jumps below it.
"""


def linear_search(items, target):
    """Look at the items one by one, from the start.
    Return (index, steps). index is -1 if the target is not there."""
    steps = 0
    for index in range(len(items)):
        steps = steps + 1
        if items[index] == target:
            return index, steps
    return -1, steps


def binary_search(items, target):
    """items MUST be sorted. Look in the middle and throw away half each time.
    Return (index, steps). index is -1 if the target is not there."""
    low = 0                  # first position that could still hold the target
    high = len(items) - 1    # last position that could still hold the target
    steps = 0
    # Note: keep going while at least one position is left to look at.
    while low <= high:
        steps = steps + 1    # looking at one item is one step
        mid = (low + high) // 2
        if items[mid] == target:
            return mid, steps
        elif items[mid] < target:
            # Sorted list: everything up to mid is smaller, so the target is on the right.
            low = mid + 1
        else:
            # Everything from mid on is bigger, so the target is on the left.
            high = mid - 1
    # low passed high: nothing is left, so the target is not in the list.
    return -1, steps


def race(size, target):
    """Search for target in the sorted list 1..size both ways.
    Return (linear_steps, binary_steps)."""
    items = list(range(1, size + 1))
    # "_" ignores the index; here we only compare the number of steps.
    _, linear_steps = linear_search(items, target)
    _, binary_steps = binary_search(items, target)
    return linear_steps, binary_steps


if __name__ == "__main__":
    print("Searching for the LAST number in a sorted list:")
    print(f"{'items':>8} | {'linear':>7} | {'binary':>7}")
    for size in [10, 100, 1000, 10000]:
        linear_steps, binary_steps = race(size, size)
        print(f"{size:>8} | {linear_steps:>7} | {binary_steps:>7}")


# Common mistakes children make here:
# - Writing `low = mid` or `high = mid` (without + 1 or - 1): the range may stop shrinking
#   and the loop runs forever.
# - Using `while low < high`, which skips the last remaining item, so some numbers (and
#   the missing-item checks) go wrong.
# - Forgetting to count the step, or counting it after the `return`.
# - Trying binary search on an unsorted list: "bigger or smaller" no longer says which half.
#
# Another correct way: Python's bisect module does the halving for you (no step counter):
#     from bisect import bisect_left
#     i = bisect_left(items, target)
#     return i if i < len(items) and items[i] == target else -1
