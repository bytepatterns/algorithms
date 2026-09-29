"""
Smallest Range K Lists (hard) · patterns: k-way-merge, sliding-window

You are given k lists of numbers, each already sorted in ascending order.
Find the narrowest range [low, high] that contains at least one value from
every list. If two ranges are equally narrow, return the one that starts
earlier.

Examples:

    Input:  lists = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    Output: [20, 24]
    Why:    24 comes from the first list, 20 from the second, 22 from the third

    Input:  lists = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    Output: [1, 1]
    Why:    all three lists share the value 1, so the range collapses to a point

    Input:  lists = [[7], [8], [9]]
    Output: [7, 9]
    Why:    edge case, one option per list and no choice to make

Approach:
    At any moment you hold one candidate per list, so the covering range is
    exactly [min, max] of those candidates. Only replacing the minimum can
    narrow it, which is what the heap gives you in log k. The maximum needs
    no heap at all — it only ever grows, so a single variable tracks it. The
    scan ends the moment any list is exhausted, because no later window can
    still cover that list. Time is O(n log k) across n total values, space
    O(k).

The lesson behind it: K-Way Merge
    https://bytepatterns.com/learn/two-heaps-k-way/k-way-merge
    python two-heaps-k-way/02-k-way-merge.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/two-heaps-k-way/smallest-range-k-lists

Run it:  python problems/two-heaps-k-way/02-smallest-range-k-lists.py
"""


import heapq

def smallest_range(lists):
    heap = [(rows[0], i, 0) for i, rows in enumerate(lists)]
    heapq.heapify(heap)                       # one candidate per list
    high = max(rows[0] for rows in lists)     # the max only ever grows
    best = (heap[0][0], high)
    while True:
        low, i, j = heapq.heappop(heap)
        if high - low < best[1] - best[0]:
            best = (low, high)
        if j + 1 == len(lists[i]):            # that list can no longer be covered
            return list(best)
        nxt = lists[i][j + 1]
        high = max(high, nxt)
        heapq.heappush(heap, (nxt, i, j + 1))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(smallest_range([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]), [20, 24])
    check(smallest_range([[1, 2, 3], [1, 2, 3], [1, 2, 3]]), [1, 1])
    check(smallest_range([[7], [8], [9]]), [7, 9])
