"""
Rotate Right By K (medium) · patterns: in-place, reversal

Shift every element of a list k positions to the right, so values pushed off
the end reappear at the front. The rearrangement must happen inside the same
list rather than in a freshly allocated one. The shift amount k is zero or
positive and may be larger than the list itself.

Examples:

    Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    Output: [5, 6, 7, 1, 2, 3, 4]
    Why:    the last three values wrap around to the front

    Input:  nums = [1, 2], k = 5
    Output: [2, 1]
    Why:    five shifts over two slots is the same as one shift

    Input:  nums = [], k = 3
    Output: []
    Why:    edge case, an empty list has nothing to wrap

Approach:
    A rotation swaps two blocks: the last k elements move ahead of the first
    n-k. Reversing the entire list puts both blocks on the right side but
    internally backwards, so reversing each block separately restores its
    order. Reducing k modulo the length first makes over-large shifts free,
    and the early return covers the empty list. Time is O(n) across three
    reversals, and space is O(1).

The lesson behind it: Rotate an Array
    https://bytepatterns.com/learn/arrays/rotate-array
    python arrays/13-rotate-array.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/rotate-right-by-k

Run it:  python problems/arrays/07-rotate-right-by-k.py
"""


def rotate_right(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    k %= n                           # a whole turn changes nothing
    def flip(i, j):                  # reverse the stretch nums[i..j] in place
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    flip(0, n - 1)                   # both blocks land on the correct side
    flip(0, k - 1)                   # repair the block now at the front
    flip(k, n - 1)                   # repair the block now at the back
    return nums


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(rotate_right([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4])
    check(rotate_right([1, 2], 5), [2, 1])
    check(rotate_right([], 3), [])
