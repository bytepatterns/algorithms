"""
Median Of Two Sorted Lists (hard) · patterns: binary-search, partitioning

Two lists are each already sorted in non-decreasing order. Return the median
of all their values taken together, as a decimal number: the middle value
when the combined count is odd, and the average of the two middle values
when it is even. At least one value exists overall, but either list on its
own may be empty. Merging the lists outright is too slow; aim for a
logarithmic number of steps.

Examples:

    Input:  a = [1, 3], b = [2]
    Output: 2.0
    Why:    the combined values are 1, 2, 3 and the middle one is 2

    Input:  a = [1, 2], b = [3, 4]
    Output: 2.5
    Why:    an even count averages the two middle values

    Input:  a = [], b = [1]
    Output: 1.0
    Why:    edge case, one list is empty and the other supplies everything

Approach:
    The median is determined by one cut through the combined values, and
    since the left side must hold a fixed number of values, choosing the cut
    in the first list forces the cut in the second. The cut is correct
    exactly when neither side's last taken value exceeds the other side's
    first remaining value, which is a monotone condition, so a halving
    search finds it. Infinities stand in for the missing neighbours at the
    ends, which removes every boundary case, including an empty list.
    Searching the shorter list gives time O(log of the smaller length), and
    space is O(1).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/searching/median-of-two-sorted-lists

Run it:  python problems/searching/03-median-of-two-sorted-lists.py
"""


def median_of_two(a, b):
    if len(a) > len(b):
        a, b = b, a                  # always cut the shorter list
    total = len(a) + len(b)
    low, high = 0, len(a)
    while low <= high:
        i = (low + high) // 2        # values taken from a
        j = (total + 1) // 2 - i     # values taken from b, forced by i
        a_left = a[i - 1] if i else float("-inf")
        a_right = a[i] if i < len(a) else float("inf")
        b_left = b[j - 1] if j else float("-inf")
        b_right = b[j] if j < len(b) else float("inf")
        if a_left <= b_right and b_left <= a_right:   # the cut is correct
            if total % 2:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        if a_left > b_right:
            high = i - 1             # took too much from a
        else:
            low = i + 1              # took too little from a


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(median_of_two([1, 3], [2]), 2.0)
    check(median_of_two([1, 2], [3, 4]), 2.5)
    check(median_of_two([], [1]), 1.0)
