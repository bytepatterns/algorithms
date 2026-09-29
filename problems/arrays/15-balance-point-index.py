"""
Balance Point Index (easy) · patterns: prefix-sums, running-sum

Given a list of whole numbers, which may be negative, find a position where
the values strictly to its left add up to the same total as the values
strictly to its right. An empty side counts as zero. Return the leftmost
such index, or -1 if there is none.

Examples:

    Input:  values = [2, 7, 1, 5, 4]
    Output: 2
    Why:    2 + 7 = 9 on the left of index 2, and 5 + 4 = 9 on the right

    Input:  values = [1, 2, 3]
    Output: -1
    Why:    no index splits the list into equal sides

    Input:  values = [5]
    Output: 0
    Why:    edge case, both sides of the only value are empty and sum to 0

Approach:
    One pass computes the grand total, and a second pass keeps a running sum
    of everything already passed. At each index the right side is whatever
    is left of the total after removing the left side and the current value,
    so each check is O(1) instead of O(n). The first match is returned,
    which makes it the leftmost. Time is O(n), and extra space is O(1).

The lesson behind it: O(1) and O(n)
    https://bytepatterns.com/learn/big-o/o1-and-on
    python big-o/02-o1-and-on.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/balance-point-index

Run it:  python problems/arrays/15-balance-point-index.py
"""


def balance_point(values):
    total = sum(values)
    left = 0
    for i, v in enumerate(values):
        right = total - left - v        # everything after index i
        if left == right:
            return i
        left += v
    return -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(balance_point([2, 7, 1, 5, 4]), 2)
    check(balance_point([1, 2, 3]), -1)
    check(balance_point([5]), 0)
