"""
Maximum Gap Buckets (hard) · patterns: bucket-sort, pigeonhole

Given a list of integers, return the largest difference between two values
that would be adjacent if the list were sorted. Return 0 when fewer than two
distinct values exist. Aim for a solution that does not sort the values.

Examples:

    Input:  nums = [3, 6, 9, 1]
    Output: 3
    Why:    sorted the values read 1, 3, 6, 9 and every step is 2 or 3

    Input:  nums = [1, 10000000]
    Output: 9999999
    Why:    two values far apart, so the single gap is the answer

    Input:  nums = [1, 1, 1]
    Output: 0
    Why:    edge case, no two distinct values exist

Approach:
    The pigeonhole principle does the work. With n values spanning hi - lo,
    some adjacent pair must differ by at least (hi - lo) / (n - 1), so
    choosing that as the bucket width guarantees the winning gap straddles a
    bucket boundary. Each bucket then only needs its own minimum and
    maximum, and the answer is the widest jump from one non-empty bucket's
    maximum to the next one's minimum. Time is O(n) plus the cost of
    visiting the buckets in order, space O(n).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/maximum-gap-buckets

Run it:  python problems/sorting/05-maximum-gap-buckets.py
"""


def maximum_gap(nums):
    if len(nums) < 2:
        return 0
    lo, hi = min(nums), max(nums)
    if lo == hi:
        return 0
    size = max(1, (hi - lo) // (len(nums) - 1))   # no gap can be smaller
    buckets = {}
    for n in nums:
        b = (n - lo) // size
        low, high = buckets.get(b, (n, n))
        buckets[b] = (min(low, n), max(high, n))  # only the extremes matter
    best, prev = 0, lo
    for b in sorted(buckets):
        best = max(best, buckets[b][0] - prev)    # across a bucket boundary
        prev = buckets[b][1]
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(maximum_gap([3, 6, 9, 1]), 3)
    check(maximum_gap([1, 10000000]), 9999999)
    check(maximum_gap([1, 1, 1]), 0)
