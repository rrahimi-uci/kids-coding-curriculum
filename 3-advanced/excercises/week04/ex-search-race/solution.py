# Search Race - reference solution
# Two ways to find something in a list, and a step counter to compare them.
# A "step" = one time we look at an item and compare it with the target.


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
    low = 0
    high = len(items) - 1
    steps = 0
    while low <= high:
        steps = steps + 1
        mid = (low + high) // 2
        if items[mid] == target:
            return mid, steps
        elif items[mid] < target:
            low = mid + 1    # target is bigger: throw away the left half
        else:
            high = mid - 1   # target is smaller: throw away the right half
    return -1, steps


def race(size, target):
    """Search for target in the sorted list 1..size both ways.
    Return (linear_steps, binary_steps)."""
    items = list(range(1, size + 1))
    _, linear_steps = linear_search(items, target)
    _, binary_steps = binary_search(items, target)
    return linear_steps, binary_steps


if __name__ == "__main__":
    print("Searching for the LAST number in a sorted list:")
    print(f"{'items':>8} | {'linear':>7} | {'binary':>7}")
    for size in [10, 100, 1000, 10000]:
        linear_steps, binary_steps = race(size, size)
        print(f"{size:>8} | {linear_steps:>7} | {binary_steps:>7}")
