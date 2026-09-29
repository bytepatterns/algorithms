"""
Sort a Nearly Sorted List (medium) · patterns: min-heap, k-sorted

A sensor log arrives almost in order: every reading is at most k positions
away from the place it would occupy in the fully sorted log. Given the list
and k, return the readings in ascending order. The answer should take O(n
log k) time, which beats a general sort when k is much smaller than n.

Examples:

    Input:  nums = [3, 1, 2, 6, 4, 5], k = 2
    Output: [1, 2, 3, 4, 5, 6]
    Why:    3 sits two places early, 1 and 2 one place late

    Input:  nums = [10, 9, 8, 7], k = 3
    Output: [7, 8, 9, 10]
    Why:    a reversed list of four values is still within 3 places

    Input:  nums = [1, 2, 3], k = 0
    Output: [1, 2, 3]
    Why:    edge case, k = 0 means everything is already in place

Approach:
    The value that belongs in output slot i starts at most k positions away,
    so it is already among the values read once k + 1 of them are waiting.
    Keeping those candidates in a min-heap of size k + 1 means the heap's
    smallest value is always safe to emit, since every unread value belongs
    further right. Heap sort pops a heap holding everything, while this heap
    never holds more than k + 1 values, and that is where the log k comes
    from. Time is O(n log k), and space is O(k) for the heap plus the
    output.

The lesson behind it: Heap Sort
    https://bytepatterns.com/learn/sorting/heap-sort
    python sorting/09-heap-sort.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/heaps/sort-a-nearly-sorted-list

Run it:  python problems/heaps/08-sort-a-nearly-sorted-list.py
"""


import heapq

def sort_nearly(nums, k):
    heap, out = [], []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:            # k + 1 candidates: the smallest is final
            out.append(heapq.heappop(heap))
    while heap:                      # input exhausted, drain in order
        out.append(heapq.heappop(heap))
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(sort_nearly([3, 1, 2, 6, 4, 5], 2), [1, 2, 3, 4, 5, 6])
    check(sort_nearly([10, 9, 8, 7], 3), [7, 8, 9, 10])
    check(sort_nearly([1, 2, 3], 0), [1, 2, 3])
