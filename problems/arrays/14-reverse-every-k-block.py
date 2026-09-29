"""
Reverse Every K Block (easy) · patterns: in-place-reversal, two-pointers

Given a list and a positive integer k, reverse the order of the values
inside every consecutive block of k values: the first k, then the next k,
and so on. If the length is not a multiple of k, the final block is shorter
than k and stays as it is. Work in place with O(1) extra space and return
the same list.

Examples:

    Input:  nums = [1, 2, 3, 4, 5, 6, 7, 8], k = 3
    Output: [3, 2, 1, 6, 5, 4, 7, 8]
    Why:    two full blocks are reversed; 7 and 8 form a short block

    Input:  nums = [1, 2, 3, 4], k = 4
    Output: [4, 3, 2, 1]
    Why:    one block covers the whole list

    Input:  nums = [5, 6], k = 3
    Output: [5, 6]
    Why:    edge case, there is no full block at all

Approach:
    Block starts are 0, k, 2k and so on, and a block is only reversed when
    all k of its values exist, which the range bound len(nums) - k + 1
    enforces. Each block is reversed by two indexes that swap values and
    meet in the middle, so no second list is built. Every value is swapped
    at most once. Time is O(n) and space is O(1).

The lesson behind it: In-Place Reversal
    https://bytepatterns.com/learn/arrays/in-place-reversal
    python arrays/05-in-place-reversal.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/reverse-every-k-block

Run it:  python problems/arrays/14-reverse-every-k-block.py
"""


def reverse_blocks(nums, k):
    for start in range(0, len(nums) - k + 1, k):   # full blocks only
        lo, hi = start, start + k - 1
        while lo < hi:                             # swap the ends, walk inward
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1
    return nums


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(reverse_blocks([1, 2, 3, 4, 5, 6, 7, 8], 3), [3, 2, 1, 6, 5, 4, 7, 8])
    check(reverse_blocks([1, 2, 3, 4], 4), [4, 3, 2, 1])
    check(reverse_blocks([5, 6], 3), [5, 6])
