"""
Subarrays Summing To K (medium) · patterns: prefix-sums, hash-map

Given a list of integers and a target k, count how many contiguous stretches
of the list add up to exactly k. Stretches that start or end at different
positions count separately even when they hold the same values. Negative
numbers are allowed, so sums do not grow steadily as the stretch widens.

Examples:

    Input:  nums = [1, 2, 3, 1], k = 3
    Output: 2
    Why:    the stretches 1,2 and 3 both total 3

    Input:  nums = [2, -1, 2, -1], k = 1
    Output: 3
    Why:    negatives let several different stretches land on the same total

    Input:  nums = [0, 0], k = 0
    Output: 3
    Why:    edge case, each single zero counts and so does the pair

Approach:
    The sum of a stretch equals the running total at its end minus the
    running total just before its start, so a stretch hits k exactly when an
    earlier prefix total equals the current total minus k. A map from prefix
    total to occurrence count answers that in constant time, and it must
    start with one occurrence of zero so stretches beginning at index zero
    are counted. Because negatives are allowed, sliding-window shrinking
    would be unsound, which is why the counting approach is used instead.
    Time is O(n) on average, and space is O(n) for the map.

The lesson behind it: Subarray Sums With a Map
    https://bytepatterns.com/learn/hash-tables/subarray-sum-map
    python hash-tables/06-subarray-sum-map.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/hash-tables/subarrays-summing-to-k

Run it:  python problems/hash-tables/02-subarrays-summing-to-k.py
"""


def count_subarrays_with_sum(nums, k):
    counts = {0: 1}                  # prefix total -> how often it occurred
    running = 0
    total = 0
    for x in nums:
        running += x
        # any earlier prefix equal to running - k closes a valid stretch here
        total += counts.get(running - k, 0)
        counts[running] = counts.get(running, 0) + 1
    return total


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_subarrays_with_sum([1, 2, 3, 1], 3), 2)
    check(count_subarrays_with_sum([2, -1, 2, -1], 1), 3)
    check(count_subarrays_with_sum([0, 0], 0), 3)
