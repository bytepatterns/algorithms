"""
Merge K Sorted Runs (easy) · patterns: k-way-merge, min-heap

You are given k lists, each sorted in ascending order, and some of them may
be empty. Combine them into one ascending list holding every value,
duplicates included. Read each list only from the front and keep no more
than one waiting value per list at any time.

Examples:

    Input:  lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    Output: [1, 1, 2, 3, 4, 4, 5, 6]

    Input:  lists = [[], [0], []]
    Output: [0]
    Why:    empty lists simply contribute nothing

    Input:  lists = []
    Output: []
    Why:    edge case, no lists at all

Approach:
    The next output value is always the smallest of the current front
    values, so a min-heap holding exactly one front value per list delivers
    it in O(log k). Each entry carries its list index and position, so after
    a pop the heap is refilled from the list that just gave up a value,
    which keeps the one-per-list rule. Tagging with the list index also
    breaks ties between equal values without ever comparing anything else.
    With n values in total, time is O(n log k) and the heap holds at most k
    entries.

The lesson behind it: K-Way Merge
    https://bytepatterns.com/learn/two-heaps-k-way/k-way-merge
    python two-heaps-k-way/02-k-way-merge.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/two-heaps-k-way/merge-k-sorted-runs

Run it:  python problems/two-heaps-k-way/04-merge-k-sorted-runs.py
"""


import heapq

def merge_runs(lists):
    heap = [(run[0], i, 0) for i, run in enumerate(lists) if run]
    heapq.heapify(heap)                         # one front value per list
    out = []
    while heap:
        value, i, j = heapq.heappop(heap)
        out.append(value)
        if j + 1 < len(lists[i]):               # refill from the list just used
            heapq.heappush(heap, (lists[i][j + 1], i, j + 1))
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(merge_runs([[1, 4, 5], [1, 3, 4], [2, 6]]), [1, 1, 2, 3, 4, 4, 5, 6])
    check(merge_runs([[], [0], []]), [0])
    check(merge_runs([]), [])
