"""
Next Larger Arrangement (medium) · patterns: in-place-reversal, suffix-scan

A test generator walks through every ordering of a list of numbers in
dictionary order. Given a list nums, rearrange it in place into the next
larger ordering in dictionary order. If nums is already the largest
ordering, wrap around to the smallest one, which is ascending order. Use
only O(1) extra space. The list has up to 100 values, and values may repeat.

Examples:

    Input:  nums = [1, 3, 2]
    Output: [2, 1, 3]
    Why:    the orderings after [1, 3, 2] in dictionary order start with [2, 1, 3]

    Input:  nums = [1, 1, 5]
    Output: [1, 5, 1]

    Input:  nums = [3, 2, 1]
    Output: [1, 2, 3]
    Why:    edge case, already the largest ordering, so it wraps to the smallest

Approach:
    The longest descending suffix cannot be made any larger on its own, so
    the next ordering must raise the value just before it, at index i, by as
    little as possible. The smallest value in the suffix that beats nums[i]
    is found by scanning from the right, since the suffix is descending.
    Swapping them keeps the suffix descending, and reversing it in place
    turns it into ascending order, the smallest tail that can follow the new
    prefix. When no such i exists the whole list is descending, and
    reversing it gives the wrap to ascending order. Each step is a single
    pass, so time is O(n), and extra space is O(1).

The lesson behind it: In-Place Reversal
    https://bytepatterns.com/learn/arrays/in-place-reversal
    python arrays/05-in-place-reversal.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/next-larger-arrangement

Run it:  python problems/arrays/19-next-larger-arrangement.py
"""


def next_arrangement(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1                                  # skip the descending suffix
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1                              # smallest value that beats nums[i]
        nums[i], nums[j] = nums[j], nums[i]
    lo, hi = i + 1, len(nums) - 1
    while lo < hi:                              # reverse the suffix in place
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo, hi = lo + 1, hi - 1
    return nums


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(next_arrangement([1, 3, 2]), [2, 1, 3])
    check(next_arrangement([1, 1, 5]), [1, 5, 1])
    check(next_arrangement([3, 2, 1]), [1, 2, 3])
