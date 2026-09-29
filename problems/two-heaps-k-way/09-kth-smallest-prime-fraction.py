"""
Kth Smallest Prime Fraction (medium) · patterns: k-way-merge, min-heap

You are given a sorted list that starts with 1 and continues with distinct
primes. Every pair of positions i < j defines the fraction values[i] /
values[j], which is always below 1. Return the k-th smallest of these
fractions as the pair [numerator, denominator]. k is at least 1 and at most
the number of pairs.

Examples:

    Input:  values = [1, 2, 3, 5], k = 3
    Output: [2, 5]
    Why:    in order the fractions are 1/5, 1/3, 2/5, 1/2, 3/5, 2/3

    Input:  values = [1, 3, 7, 11, 13], k = 5
    Output: [3, 11]
    Why:    1/13, 1/11, 1/7, 3/13, then 3/11

    Input:  values = [1, 7], k = 1
    Output: [1, 7]
    Why:    edge case, a single pair gives a single fraction

Approach:
    For a fixed denominator the fractions grow as the numerator moves right,
    so the pairs form one sorted run per denominator, the same shape as the
    rows of a sorted matrix. A k-way merge over those runs finds the k-th
    smallest without listing all of them: the heap holds the smallest unused
    fraction of every run, each pop returns the next fraction in global
    order, and the popped run then offers its next fraction. After k minus 1
    pops the heap's top is the k-th smallest. Floating-point keys are safe
    while the values stay in the tens of thousands, since two different
    fractions then differ by far more than rounding error. Time is O((n plus
    k) log n) and space is O(n).

The lesson behind it: Kth Smallest in a Matrix
    https://bytepatterns.com/learn/searching/kth-smallest-matrix
    python searching/08-kth-smallest-matrix.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/two-heaps-k-way/kth-smallest-prime-fraction

Run it:  python problems/two-heaps-k-way/09-kth-smallest-prime-fraction.py
"""


import heapq

def kth_fraction(values, k):
    heap = [(values[0] / values[j], 0, j) for j in range(1, len(values))]
    heapq.heapify(heap)                        # head of every denominator's run
    for _ in range(k - 1):
        _, i, j = heapq.heappop(heap)
        if i + 1 < j:                          # same run, next numerator
            heapq.heappush(heap, (values[i + 1] / values[j], i + 1, j))
    _, i, j = heap[0]
    return [values[i], values[j]]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(kth_fraction([1, 2, 3, 5], 3), [2, 5])
    check(kth_fraction([1, 3, 7, 11, 13], 5), [3, 11])
    check(kth_fraction([1, 7], 1), [1, 7])
    check(kth_fraction([1, 2, 3, 5], 6), [2, 3])
