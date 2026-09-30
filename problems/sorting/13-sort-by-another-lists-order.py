"""
Sort by Another List's Order (easy) · patterns: counting-sort, custom-order

A shop sorts its stock codes by a preferred order from the marketing team.
Given values and a list order of distinct codes, rearrange values so that
codes appearing in order come first, grouped and in the same sequence as
order, followed by every other code in ascending order. Both lists hold at
most 1,000 items, every code in order also appears in values, and each code
is between 0 and 1,000.

Examples:

    Input:  values = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], order = [2, 1, 4, 3, 9, 6]
    Output: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    Why:    7 and 19 are not in order, so they go last in ascending order

    Input:  values = [28, 6, 22, 8, 44, 17], order = [22, 28, 8, 6]
    Output: [22, 28, 8, 6, 17, 44]

    Input:  values = [5, 5], order = []
    Output: [5, 5]
    Why:    edge case, with an empty order the result is a plain ascending sort

Approach:
    Because every code lies between 0 and 1,000, a counting array replaces
    comparisons entirely. One pass over values records how many copies of
    each code exist. Walking order then emits each preferred code the right
    number of times, and zeroing its count ensures it is not emitted again.
    The final sweep over all possible codes from low to high emits the
    leftovers in ascending order, which is exactly the tail the problem asks
    for. With k = 1,001 possible codes, time is O(n + k) and extra space is
    O(k).

The lesson behind it: Counting Sort
    https://bytepatterns.com/learn/sorting/counting-sort
    python sorting/07-counting-sort.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/sort-by-another-lists-order

Run it:  python problems/sorting/13-sort-by-another-lists-order.py
"""


def relative_sort(values, order, top=1000):
    counts = [0] * (top + 1)
    for v in values:
        counts[v] += 1
    out = []
    for code in order:                 # preferred codes first, grouped
        out += [code] * counts[code]
        counts[code] = 0
    for code in range(top + 1):        # the rest, ascending
        out += [code] * counts[code]
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(relative_sort([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]), [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19])
    check(relative_sort([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]), [22, 28, 8, 6, 17, 44])
    check(relative_sort([5, 5], []), [5, 5])
