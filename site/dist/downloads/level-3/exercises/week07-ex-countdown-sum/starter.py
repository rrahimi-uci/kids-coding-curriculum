# Recursion warm-up
# A recursive function is a function that calls ITSELF on a smaller problem.
# Every recursive function needs two parts:
#   1. a BASE CASE: the tiny problem we can answer straight away (stop!)
#   2. a RECURSIVE CASE: do one small step, then call yourself on the rest
#
# countdown() is finished: read it and run the program to see how it works.
# Then finish sum_to() and reverse().


def countdown(n):
    """Print n, n-1, ... 1 and then Liftoff!"""
    if n <= 0:                # base case: nothing left to count
        print("Liftoff!")
        return
    print(n)                  # one small step...
    countdown(n - 1)          # ...then the same job on a smaller number


def sum_to(n):
    """Return 1 + 2 + ... + n, worked out by recursion."""
    # TODO 1: base case. If n is 0 (or less), return 0.
    # TODO 2: recursive case. Return n + sum_to(n - 1)
    return 0


def reverse(word):
    """Return the word backwards, e.g. 'turtle' -> 'eltrut'."""
    # TODO 3: base case. A word with 0 or 1 letters is its own reverse.
    # TODO 4: recursive case. The last letter is word[-1] and everything
    #         before it is word[:-1]. Put the last letter first, then
    #         the reverse of the rest.
    return word


if __name__ == "__main__":
    countdown(5)
    print("sum_to(10) =", sum_to(10))
    print("reverse('recursion') =", reverse("recursion"))
