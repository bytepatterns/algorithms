"""
Kth Number Missing From a List (easy) · patterns: binary-search, counting

Ticket numbers are handed out from 1 upwards, and nums lists the ones that
have been used, strictly increasing and all positive. Return the k-th
smallest positive number that does not appear in nums, where k is at least
1. Aim for a solution faster than walking through the numbers one by one.

Examples:

    Input:  nums = [2, 3, 4, 7, 11], k = 5
    Output: 9
    Why:    the missing numbers are 1, 5, 6, 8, 9, 10, ...

    Input:  nums = [1, 2, 3, 4], k = 2
    Output: 6
    Why:    nothing is missing inside the list, so the answer lies past its end

    Input:  nums = [], k = 4
    Output: 4
    Why:    edge case, with nothing used, the k-th missing number is k itself

Approach:
    At index i the list has used i + 1 numbers, so nums[i] minus (i + 1)
    numbers below nums[i] are missing, and that count never decreases along
    the list. Binary search finds lo, the first index where at least k
    numbers are missing, or the list length if there is none. The answer
    then sits after exactly lo used numbers and is the k-th number not among
    them, which is lo + k. Time is O(log n) and space is O(1).

The lesson behind it: Binary Search
    https://bytepatterns.com/learn/searching/binary-search
    python searching/02-binary-search.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/searching/kth-number-missing-from-a-list

Run it:  python problems/searching/09-kth-number-missing-from-a-list.py
"""


def kth_missing(nums, k):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] - (mid + 1) < k:          # fewer than k missing below nums[mid]
            lo = mid + 1
        else:
            hi = mid
    return lo + k                              # lo used numbers lie below the answer


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(kth_missing([2, 3, 4, 7, 11], 5), 9)
    check(kth_missing([1, 2, 3, 4], 2), 6)
    check(kth_missing([], 4), 4)
    check(kth_missing([5, 6, 7], 3), 3)
