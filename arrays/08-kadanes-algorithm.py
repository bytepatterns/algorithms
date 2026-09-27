"""
Kadane's Algorithm: Drop the past the moment it starts costing you.

Walk the array keeping the best sum that ends at the current element. If
carrying the running sum forward hurts more than starting over, throw it
away and restart here. The answer is the largest value that streak ever
reached.

Lesson 8 of Arrays, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/arrays/kadanes-algorithm

Run it:  python arrays/08-kadanes-algorithm.py
"""


def max_subarray(nums):
    best = current = nums[0]
    for x in nums[1:]:
        # extend the current streak, or restart at x
        current = max(x, current + x)
        best = max(best, current)
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
    # the winning stretch is [4, -1, 2, 1]
