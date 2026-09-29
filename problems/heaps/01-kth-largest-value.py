"""
Kth Largest Value (medium) · patterns: min-heap, top-k

Given an unsorted list of numbers and a rank k, return the value that would
sit in position k if the list were arranged from largest to smallest.
Ranking is by value, so repeated values each occupy their own rank. You may
assume k is at least 1 and never exceeds the length of the list.

Examples:

    Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
    Output: 5
    Why:    ordered from the top the values run 6, 5, 4, 3, 2, 1

    Input:  nums = [7, 7, 7], k = 2
    Output: 7
    Why:    duplicates each take a rank of their own

    Input:  nums = [9], k = 1
    Output: 9
    Why:    edge case, the only value is also the largest

Approach:
    A min-heap capped at k entries keeps exactly the k largest values seen
    so far, and its root is the weakest of them, which is the k-th largest
    overall. Each value costs a push and possibly a pop, both logarithmic in
    k rather than in n. This beats full sorting whenever k is much smaller
    than the list. Time is O(n log k) and space is O(k).

The lesson behind it: Top K Elements
    https://bytepatterns.com/learn/heaps/top-k-elements
    python heaps/04-top-k-elements.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/heaps/kth-largest-value

Run it:  python problems/heaps/01-kth-largest-value.py
"""


import heapq
def kth_largest(nums, k):
    heap = []                        # a min-heap holding the k best values
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)      # drop the weakest of the k + 1 candidates
    return heap[0]                   # the smallest survivor is the k-th largest


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
    check(kth_largest([7, 7, 7], 2), 7)
    check(kth_largest([9], 1), 9)
