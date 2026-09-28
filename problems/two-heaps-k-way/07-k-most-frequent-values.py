"""
K Most Frequent Values (medium) · patterns: top-k, min-heap, hash-map

Given a list of whole numbers and a count k, return the k values that appear
most often. Order the result from most to least frequent, and when two
values appear equally often, put the smaller value first. You may assume k
is at least 1 and no larger than the number of distinct values.

Examples:

    Input:  values = [4, 1, 4, 2, 1, 4, 3], k = 2
    Output: [4, 1]
    Why:    4 appears three times and 1 twice

    Input:  values = [7, 8, 9, 8, 9], k = 1
    Output: [8]
    Why:    8 and 9 tie at two each, and 8 is smaller

    Input:  values = [5], k = 1
    Output: [5]
    Why:    edge case, a single value

Approach:
    A dictionary counts each value in one pass. A min-heap capped at k then
    holds the best candidates so far, with the weakest at the root, so each
    new value costs one push and at most one pop. Storing the pair (count,
    -value) makes the heap treat fewer appearances as weaker and, on equal
    counts, a larger value as weaker, which matches the required tie rule.
    Sorting the k survivors in reverse gives the final order. Time is O(n +
    d log k) for d distinct values, and space is O(d).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/two-heaps-k-way/k-most-frequent-values

Run it:  python problems/two-heaps-k-way/07-k-most-frequent-values.py
"""


import heapq
from collections import Counter
def most_frequent(values, k):
    keep = []                                   # min-heap of the k strongest (count, -value)
    for v, c in Counter(values).items():
        heapq.heappush(keep, (c, -v))
        if len(keep) > k:
            heapq.heappop(keep)                 # the weakest keeper leaves
    return [-nv for c, nv in sorted(keep, reverse=True)]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(most_frequent([4, 1, 4, 2, 1, 4, 3], 2), [4, 1])
    check(most_frequent([7, 8, 9, 8, 9], 1), [8])
    check(most_frequent([5], 1), [5])
