"""TEACHER REFERENCE SOLUTION: Sort Race

What the program does: it sorts a list of numbers with two classic methods, selection sort and
bubble sort, and counts how many swaps each one makes. For the sample cards, selection sort
needs 5 swaps and bubble sort needs 16, so the child sees that two correct methods can do
very different amounts of work.

Key ideas practiced: nested loops, comparing neighbors, swapping two items with one line
(a, b = b, a), copying a list so the original is not changed, and counting work.

Approach: bubble sort walks along the list and swaps any neighbors that are in the wrong
order. After the first pass the biggest item has "bubbled" to the end, so each next pass can
stop one place earlier (end shrinks).
"""


def selection_sort(items):
    """Find the smallest item left and swap it to the front. Repeat.
    Return (sorted_list, swaps)."""
    result = list(items)  # a copy: never change the caller's list
    swaps = 0
    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j] < result[smallest]:
                smallest = j
        if smallest != i:
            result[i], result[smallest] = result[smallest], result[i]
            swaps = swaps + 1
    return result, swaps


def bubble_sort(items):
    """Compare neighbors and swap them if they are in the wrong order.
    Big items 'bubble' to the end. Return (sorted_list, swaps)."""
    result = list(items)  # a copy, so the cards the child passed in stay unchanged
    swaps = 0
    # "end" is the last place we still need to look at. Items after it are already in
    # their final spot. range(len - 1, 0, -1) counts down: 7, 6, 5 ... 1 for 8 items.
    for end in range(len(result) - 1, 0, -1):
        for i in range(end):
            # Note: strictly ">" (not ">="): equal neighbors are already fine, and swapping
            # them would waste swaps and be counted for nothing.
            if result[i] > result[i + 1]:
                # Python swaps both items at once, so we do not need a helper variable.
                result[i], result[i + 1] = result[i + 1], result[i]
                swaps = swaps + 1
    return result, swaps


if __name__ == "__main__":
    cards = [7, 3, 9, 1, 5, 3, 8, 2]
    print("Cards:         ", cards)
    sorted_cards, swaps = selection_sort(cards)
    print("Selection sort:", sorted_cards, f"({swaps} swaps)")
    sorted_cards, swaps = bubble_sort(cards)
    print("Bubble sort:   ", sorted_cards, f"({swaps} swaps)")
    print("Cards are unchanged:", cards)


# Common mistakes children make here:
# - Swapping with two lines (result[i] = result[i + 1] then the reverse): the first line
#   overwrites a value, so one card is lost and another is doubled (the test warns that both
#   3s must stay).
# - Using >= so equal neighbors are swapped too, which gives a wrong swap count.
# - Looping range(end + 1), so result[i + 1] goes past the end of the list (IndexError).
# - Forgetting swaps = swaps + 1, or sorting the original list instead of the copy.
#
# Another correct way: stop early when a whole pass makes no swap (the list is sorted):
#     for end in range(len(result) - 1, 0, -1):
#         swapped = False
#         for i in range(end):
#             if result[i] > result[i + 1]:
#                 result[i], result[i + 1] = result[i + 1], result[i]
#                 swaps += 1
#                 swapped = True
#         if not swapped:
#             break
