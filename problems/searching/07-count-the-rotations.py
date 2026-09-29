"""
Count the Rotations (medium) · patterns: binary-search, boundary-search

A list of distinct numbers was sorted in increasing order and then rotated
to the right r times, where one rotation moves the last element to the front
and r is smaller than the list length. Given the rotated list, return r. The
list has at least one element, and the answer should take O(log n) time.

Examples:

    Input:  nums = [15, 18, 2, 3, 6, 12]
    Output: 2
    Why:    the smallest value, 2, was carried two places to the right

    Input:  nums = [1, 2, 3, 4]
    Output: 0
    Why:    the list was never rotated

    Input:  nums = [9]
    Output: 0
    Why:    edge case, one element cannot move

Approach:
    After rotation the list is two increasing runs, and the first element of
    the second run is the minimum, whose index equals the number of
    rotations. Comparing the middle with the right end of the window reveals
    which run the middle belongs to: a larger middle belongs to the first
    run, so the minimum is to its right. A smaller middle belongs to the
    second run, so the minimum is at the middle or before it, which is why
    hi moves to mid and not past it. Time is O(log n), and space is O(1).

The lesson behind it: Search in Rotated Array
    https://bytepatterns.com/learn/searching/search-in-rotated-array
    python searching/04-search-in-rotated-array.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/searching/count-the-rotations

Run it:  python problems/searching/07-count-the-rotations.py
"""


def rotations(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1             # the drop lies right of mid
        else:
            hi = mid                 # mid..hi is sorted, the minimum is at mid or left
    return lo                        # index of the minimum = rotations


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(rotations([15, 18, 2, 3, 6, 12]), 2)
    check(rotations([1, 2, 3, 4]), 0)
    check(rotations([9]), 0)
