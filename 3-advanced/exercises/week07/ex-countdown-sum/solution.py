# Recursion warm-up - reference solution
# A recursive function is a function that calls ITSELF on a smaller problem.
# Every recursive function needs two parts:
#   1. a BASE CASE: the tiny problem we can answer straight away (stop!)
#   2. a RECURSIVE CASE: do one small step, then call yourself on the rest


def countdown(n):
    """Print n, n-1, ... 1 and then Liftoff!"""
    if n <= 0:                # base case: nothing left to count
        print("Liftoff!")
        return
    print(n)                  # one small step...
    countdown(n - 1)          # ...then the same job on a smaller number


def sum_to(n):
    """Return 1 + 2 + ... + n, worked out by recursion."""
    if n <= 0:                # base case: the sum of no numbers is 0
        return 0
    return n + sum_to(n - 1)  # n plus "the sum of everything below n"


def reverse(word):
    """Return the word backwards, e.g. 'turtle' -> 'eltrut'."""
    if len(word) <= 1:        # base case: 0 or 1 letters read the same backwards
        return word
    # last letter first, then the reverse of everything before it
    return word[-1] + reverse(word[:-1])


if __name__ == "__main__":
    countdown(5)
    print("sum_to(10) =", sum_to(10))
    print("reverse('recursion') =", reverse("recursion"))
