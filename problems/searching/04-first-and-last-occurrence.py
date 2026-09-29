"""
First And Last Occurrence (medium) · patterns: binary-search, boundary-search

A sorted list may hold a target value many times over. Report the first and
last positions it occupies, as a pair, or a pair of -1 values when it is
absent. The run of equal values can be long, so walking outwards from a hit
is too slow.

Examples:

    Input:  nums = [5, 7, 7, 8, 8, 10], target = 8
    Output: (3, 4)

    Input:  nums = [5, 7, 7, 8, 8, 10], target = 6
    Output: (-1, -1)
    Why:    the value is absent, even though it sits inside the range

    Input:  nums = [], target = 1
    Output: (-1, -1)
    Why:    edge case, an empty list has no positions at all

Approach:
    Binary search is really a border finder: given a test that is false for
    a prefix and true for the rest, it returns the first true position.
    Asking for the first value at least the target lands on the start of the
    run, and asking for the first value strictly greater lands one past its
    end. One guard is still needed, because both answers exist even when the
    target does not, so the value at the start position has to be checked.
    Each search is O(log n) and they run one after the other, so time is
    O(log n) and space is O(1).

The lesson behind it: Binary Search Variants
    https://bytepatterns.com/learn/searching/binary-search-variants
    python searching/03-binary-search-variants.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/searching/first-and-last-occurrence

Run it:  python problems/searching/04-first-and-last-occurrence.py
"""


def bounds(nums, target):
    def first(pred):                     # leftmost index where pred is true
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if pred(nums[mid]):
                hi = mid                 # mid may itself be the border
            else:
                lo = mid + 1
        return lo
    start = first(lambda v: v >= target)
    if start == len(nums) or nums[start] != target:
        return (-1, -1)                  # the border exists, the value does not
    return (start, first(lambda v: v > target) - 1)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(bounds([5, 7, 7, 8, 8, 10], 8), (3, 4))
    check(bounds([5, 7, 7, 8, 8, 10], 6), (-1, -1))
    check(bounds([], 1), (-1, -1))
    check(bounds([2, 2], 2), (0, 1))
