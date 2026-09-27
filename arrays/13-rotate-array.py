"""
Rotate an Array: Three reversals move every element home.

Rotating right by k means the last k values jump to the front. Reverse the
whole array and they are at the front already — backwards, and so is
everything else. Now reverse the first k, then reverse the rest, and both
blocks read correctly again. Three linear reversals, no copy of the array,
and k taken modulo the length so a full turn costs nothing.

Lesson 13 of Arrays, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/arrays/rotate-array

Run it:  python arrays/13-rotate-array.py
"""


def rotate(nums, k):
    k %= len(nums)

    def reverse(lo, hi):
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo, hi = lo + 1, hi - 1

    reverse(0, len(nums) - 1)   # flip the whole row
    reverse(0, k - 1)           # put the first block back in order
    reverse(k, len(nums) - 1)   # and the rest
    return nums


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(rotate([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
