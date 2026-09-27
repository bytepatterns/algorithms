"""
In-Place Reversal: Flip an array with one temp variable, not a copy.

Swap the first and last elements, then step both indexes inward and repeat.
After n/2 swaps the whole array is reversed. Time is O(n) and extra space is
O(1).

Lesson 5 of Arrays, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/arrays/in-place-reversal

Run it:  python arrays/05-in-place-reversal.py
"""


def reverse(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        # swap the two ends, then step inward
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(reverse([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
    # n // 2 swaps, no second array -> O(n) time, O(1) space
