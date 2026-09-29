"""
Three Way Flag Sort (medium) · patterns: dutch-national-flag, in-place

A list holds only the values 0, 1 and 2. Arrange it so all the zeros come
first, then all the ones, then all the twos. Do it inside the same list with
a single pass over the values, without counting how many of each value there
are first.

Examples:

    Input:  values = [2, 0, 2, 1, 1, 0]
    Output: [0, 0, 1, 1, 2, 2]

    Input:  values = [2, 0, 1]
    Output: [0, 1, 2]
    Why:    every value is a different one, so each has to move

    Input:  values = []
    Output: []
    Why:    edge case, there is nothing to arrange

Approach:
    Three boundaries carve the list into finished zeros, finished ones,
    unexamined values, and finished twos. Each step inspects one unexamined
    value and places it in constant time: zeros swap down to the low
    boundary, twos swap up to the high boundary, and ones are already where
    they belong. The asymmetry matters — after swapping a two into place the
    inspection point must not advance, because the value it received from
    the far end has never been looked at. Time is O(n) in a single pass, and
    space is O(1).

The lesson behind it: Dutch National Flag
    https://bytepatterns.com/learn/arrays/dutch-national-flag
    python arrays/11-dutch-national-flag.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/three-way-flag-sort

Run it:  python problems/sorting/02-three-way-flag-sort.py
"""


def flag_sort(values):
    low, mid, high = 0, 0, len(values) - 1
    while mid <= high:
        if values[mid] == 0:
            values[low], values[mid] = values[mid], values[low]
            low, mid = low + 1, mid + 1
        elif values[mid] == 2:
            values[mid], values[high] = values[high], values[mid]
            high -= 1                # the value swapped in is still unexamined
        else:
            mid += 1                 # a one is already in the middle region
    return values


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(flag_sort([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2])
    check(flag_sort([2, 0, 1]), [0, 1, 2])
    check(flag_sort([]), [])
