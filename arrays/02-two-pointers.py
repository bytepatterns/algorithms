"""
Two Pointers: Two indexes closing in beat one loop nesting another.

Keep one index at each end and move them toward each other based on what you
see. Every step rules out a whole group of pairs at once. Brute force checks
every pair in O(n²); two pointers does the same job in O(n).

Lesson 2 of Arrays, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/arrays/two-pointers

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python arrays/02-two-pointers.py
"""


def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return (left, right)
        if total < target:
            left += 1        # need a bigger sum
        else:
            right -= 1       # need a smaller sum
    return None


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(two_sum_sorted([1, 3, 4, 8, 11], 11), (1, 3))
