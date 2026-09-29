"""
Squares of a Sorted List (easy) · patterns: two-pointers, merge-from-back

A list of integers is sorted in non-decreasing order and may contain
negative values. Return a new list holding the square of every value, also
in non-decreasing order. Squaring and then sorting takes O(n log n) time;
the goal is O(n) by using the order the input already has.

Examples:

    Input:  nums = [-5, -2, 1, 3, 4]
    Output: [1, 4, 9, 16, 25]
    Why:    -5 is the smallest value but gives the largest square

    Input:  nums = [-7, -3, -2]
    Output: [4, 9, 49]
    Why:    all negative, so the squares come out in reverse order

    Input:  nums = []
    Output: []
    Why:    edge case, nothing to square

Approach:
    The largest absolute value is always at one end of the sorted input, so
    the largest square still unwritten is always one of the two end squares.
    Two pointers start at the ends and the output is filled from its last
    slot backwards, the same back-to-front idea used to merge two sorted
    arrays. Each step writes one square and moves one pointer, so the loop
    runs exactly n times. Time is O(n) and space is O(n) for the output.

The lesson behind it: Merge Sorted Arrays
    https://bytepatterns.com/learn/arrays/merge-sorted-arrays
    python arrays/10-merge-sorted-arrays.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/squares-of-a-sorted-list

Run it:  python problems/arrays/13-squares-of-a-sorted-list.py
"""


def sorted_squares(nums):
    out = [0] * len(nums)
    lo, hi = 0, len(nums) - 1
    for write in range(len(nums) - 1, -1, -1):   # fill from the back
        if abs(nums[lo]) > abs(nums[hi]):        # the bigger end gives the bigger square
            out[write] = nums[lo] * nums[lo]
            lo += 1
        else:
            out[write] = nums[hi] * nums[hi]
            hi -= 1
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(sorted_squares([-5, -2, 1, 3, 4]), [1, 4, 9, 16, 25])
    check(sorted_squares([-7, -3, -2]), [4, 9, 49])
    check(sorted_squares([]), [])
