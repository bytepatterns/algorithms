"""
Pancake Flips to Sort (medium) · patterns: selection-sort, prefix-reversal

A robot arm can only do one move on a stack of numbered plates: slide a
spatula under the top k plates and flip them over, which reverses the first
k values of the list. Given a list arr that is a permutation of 1 to n,
return a list of flip sizes k that leaves arr in ascending order. Any answer
with at most 2n flips is accepted; the examples show the answer from placing
the largest unplaced value first. The list has up to 100 values.

Examples:

    Input:  arr = [3, 2, 4, 1]
    Output: [3, 4, 2, 3, 2]
    Why:    flip 3 brings 4 to the front, flip 4 sends it to the end, and so on

    Input:  arr = [2, 1]
    Output: [2]

    Input:  arr = [1, 2, 3]
    Output: []
    Why:    edge case, already sorted, so no flip is needed

Approach:
    This is selection sort with a restricted move. Each round finds the
    largest value that is not yet in place; one flip brings it to the top of
    the stack and a second flip of the whole unsorted part sends it to the
    bottom, where it stays because later flips never reach that far. Flips
    that would change nothing are skipped: a value already in place needs
    none, and a value already on top needs only the second. That is at most
    2 flips for each of n - 1 rounds. Finding the value and flipping are
    O(n) each round, so time is O(n²) and extra space is O(n) for the
    answer.

The lesson behind it: Selection Sort
    https://bytepatterns.com/learn/sorting/selection-sort
    python sorting/03-selection-sort.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/pancake-flips-to-sort

Run it:  python problems/sorting/14-pancake-flips-to-sort.py
"""


def pancake_sort(arr):
    arr, flips = arr[:], []
    for size in range(len(arr), 1, -1):
        i = arr.index(size)                  # largest value not yet in place
        if i == size - 1:
            continue                         # already where it belongs
        if i > 0:
            arr[:i + 1] = arr[:i + 1][::-1]  # bring it to the front
            flips.append(i + 1)
        arr[:size] = arr[:size][::-1]        # drop it into slot size - 1
        flips.append(size)
    return flips


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(pancake_sort([3, 2, 4, 1]), [3, 4, 2, 3, 2])
    check(pancake_sort([2, 1]), [2])
    check(pancake_sort([1, 2, 3]), [])
