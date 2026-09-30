"""
Largest Product Subarray (medium) · patterns: kadane, running-min-max

A growth model stores daily multipliers as integers, some negative and some
zero. Given a non-empty list nums, return the largest product of any
non-empty contiguous run of values. The list has up to 20,000 values between
-10 and 10, and the answer fits in a normal integer. Checking every run is
too slow.

Examples:

    Input:  nums = [2, 3, -2, 4]
    Output: 6
    Why:    the run [2, 3]; adding -2 flips the sign

    Input:  nums = [-2, 3, -4]
    Output: 24
    Why:    two negatives cancel, so the whole list wins

    Input:  nums = [-2, 0, -1]
    Output: 0
    Why:    edge case, a zero beats every run that holds a single negative

Approach:
    This is Kadane's algorithm with one extra number. For sums, the best run
    ending here either extends the previous best or starts fresh. For
    products a very negative run can become the best as soon as another
    negative arrives, so both the largest and the smallest product of a run
    ending at the current value are carried forward. Each new value picks
    its new extremes from three candidates: itself alone, times the old
    largest, or times the old smallest. A zero resets both to zero, and the
    next value starts a fresh run through the itself-alone candidate. Time
    is O(n), and extra space is O(1).

The lesson behind it: Kadane's Algorithm
    https://bytepatterns.com/learn/arrays/kadanes-algorithm
    python arrays/08-kadanes-algorithm.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/largest-product-subarray

Run it:  python problems/arrays/20-largest-product-subarray.py
"""


def largest_product(nums):
    hi = lo = best = nums[0]
    for x in nums[1:]:
        candidates = (x, x * hi, x * lo)      # start fresh, or extend either extreme
        hi, lo = max(candidates), min(candidates)
        best = max(best, hi)
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(largest_product([2, 3, -2, 4]), 6)
    check(largest_product([-2, 3, -4]), 24)
    check(largest_product([-2, 0, -1]), 0)
