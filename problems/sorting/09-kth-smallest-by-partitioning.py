"""
Kth Smallest by Partitioning (medium) · patterns: quickselect, three-way-partition

Given an unsorted list of integers and a number k, return the k-th smallest
value, counting from 1 and counting repeated values separately. Sorting
takes O(n log n) time; aim for O(n) expected time by reusing the partition
step from quicksort. Leave the caller's list unchanged.

Examples:

    Input:  nums = [7, 2, 9, 4, 4, 1], k = 3
    Output: 4
    Why:    in sorted order the list reads 1, 2, 4, 4, 7, 9

    Input:  nums = [3, 3, 3, 3], k = 2
    Output: 3
    Why:    every value equals the pivot, which must not slow the search down

    Input:  nums = [5], k = 1
    Output: 5
    Why:    edge case, a single value

Approach:
    Quickselect is quicksort that continues into one side only. A three-way
    partition gathers every copy of the pivot into a middle band, so the
    pivot is the answer whenever index k - 1 lands in that band, and a list
    full of repeated values cannot push the search into quadratic time. A
    random pivot shrinks the range by a constant fraction on average, so the
    work adds up to a geometric series and is O(n) expected; the unlikely
    worst case is O(n²). Space is O(n) for the copy that keeps the caller's
    list unchanged.

The lesson behind it: Quick Sort
    https://bytepatterns.com/learn/sorting/quick-sort
    python sorting/06-quick-sort.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/kth-smallest-by-partitioning

Run it:  python problems/sorting/09-kth-smallest-by-partitioning.py
"""


import random

def kth_smallest(nums, k):
    a, lo, hi, want = list(nums), 0, len(nums) - 1, k - 1   # want is an index
    while True:
        pivot = a[random.randint(lo, hi)]
        lt, i, gt = lo, lo, hi               # a[lo:lt] < pivot, a[gt+1:hi+1] > pivot
        while i <= gt:
            if a[i] < pivot:
                a[lt], a[i] = a[i], a[lt]
                lt, i = lt + 1, i + 1
            elif a[i] > pivot:
                a[gt], a[i] = a[i], a[gt]
                gt -= 1
            else:
                i += 1
        if want < lt:
            hi = lt - 1                      # the answer is among the smaller values
        elif want > gt:
            lo = gt + 1                      # the answer is among the larger values
        else:
            return pivot


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(kth_smallest([7, 2, 9, 4, 4, 1], 3), 4)
    check(kth_smallest([3, 3, 3, 3], 2), 3)
    check(kth_smallest([5], 1), 5)
