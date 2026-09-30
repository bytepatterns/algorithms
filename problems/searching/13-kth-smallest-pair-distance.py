"""
Kth Smallest Pair Distance (hard) · patterns: binary-search-on-answer, two-pointers, sorting

The distance of a pair of values is the absolute difference between them.
Given a list of integers nums and an integer k, consider every pair of
positions i < j and return the kth smallest distance among all of those
pairs, counting from 1.

Examples:

    Input:  nums = [1, 3, 1], k = 1
    Output: 0
    Why:    the pair distances are 2, 0 and 2, and the smallest is 0

    Input:  nums = [62, 100, 4], k = 2
    Output: 58
    Why:    the distances sorted are 38, 58 and 96

    Input:  nums = [5, 5, 5], k = 3
    Output: 0
    Why:    edge case, equal values give three pairs at distance 0

Approach:
    Instead of searching the pairs, search the answer. "At least k pairs are
    within distance d" is false for small d and true from some point on, so
    a binary search over d from 0 to the spread of the list finds the first
    d where it becomes true, and that d is the kth smallest distance: at
    least k pairs are within it, and fewer than k are within d - 1. On a
    sorted list the check is a sliding window: for each right end, the
    values within d of it form a contiguous block ending just before it, and
    its left edge only ever moves forward, so counting all pairs takes one
    O(n) pass. Sorting is O(n log n) and the search makes O(log W) checks,
    where W is the spread, so time is O(n log n + n log W) with O(1) extra
    space beyond the sort.

The lesson behind it: Binary Search on Answer
    https://bytepatterns.com/learn/searching/binary-search-on-answer
    python searching/05-binary-search-on-answer.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/searching/kth-smallest-pair-distance

Run it:  python problems/searching/13-kth-smallest-pair-distance.py
"""


def kth_pair_distance(nums, k):
    nums = sorted(nums)

    def pairs_within(d):                        # pairs with distance <= d, one pass
        count, left = 0, 0
        for right, x in enumerate(nums):
            while x - nums[left] > d:
                left += 1
            count += right - left
        return count

    lo, hi = 0, nums[-1] - nums[0]
    while lo < hi:
        mid = (lo + hi) // 2
        if pairs_within(mid) >= k:
            hi = mid                            # mid works, maybe something smaller does too
        else:
            lo = mid + 1
    return lo


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(kth_pair_distance([1, 3, 1], 1), 0)
    check(kth_pair_distance([62, 100, 4], 2), 58)
    check(kth_pair_distance([5, 5, 5], 3), 0)
