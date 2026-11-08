# Sort Race - YOUR version
# Two classic sorting algorithms, each with a swap counter.
# Both return a NEW sorted list, so the original list is never changed.
# Finish the TODOs, then open check_my_work.py and press Run.


def selection_sort(items):
    """Find the smallest item left and swap it to the front. Repeat.
    Return (sorted_list, swaps). (Already done - read it first!)"""
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
    """Compare neighbours and swap them if they are in the wrong order.
    Big items 'bubble' to the end. Return (sorted_list, swaps)."""
    result = list(items)
    swaps = 0
    for end in range(len(result) - 1, 0, -1):
        for i in range(end):
            # TODO: if result[i] is bigger than result[i + 1]:
            #           swap them:  result[i], result[i + 1] = result[i + 1], result[i]
            #           add 1 to swaps
            pass
    return result, swaps


if __name__ == "__main__":
    cards = [7, 3, 9, 1, 5, 3, 8, 2]
    print("Cards:         ", cards)
    sorted_cards, swaps = selection_sort(cards)
    print("Selection sort:", sorted_cards, f"({swaps} swaps)")
    sorted_cards, swaps = bubble_sort(cards)
    print("Bubble sort:   ", sorted_cards, f"({swaps} swaps)")
    print("Cards are unchanged:", cards)
