"""
K Weakest Squads (easy) · patterns: top-k, max-heap

A training roster is a grid of 0s and 1s where each row is a squad. In every
row the 1s (trained members) all come before the 0s (recruits). Squad i is
weaker than squad j when it has fewer 1s, or the same number of 1s and a
smaller index. Return the indices of the k weakest squads, weakest first.

Examples:

    Input:  roster = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], k = 3
    Output: [2, 0, 3]
    Why:    the counts are 2, 4, 1, 2 and 5, and the tie between squads 0 and 3 goes to the smaller index

    Input:  roster = [[1, 0], [1, 0], [0, 0]], k = 2
    Output: [2, 0]

    Input:  roster = [[1, 1]], k = 1
    Output: [0]
    Why:    edge case, a single squad is the weakest by default

Approach:
    The k weakest squads are a top-k selection, so a heap of size k is
    enough: it holds the weakest squads seen so far with the strongest of
    them at the root, the one to evict next. Python's heapq is a min-heap,
    so each squad is stored as its negated (count, index) pair, which makes
    the strongest squad the smallest entry. A new squad replaces the root
    only when its pair is smaller than the root's, which is exactly the
    weaker-than rule including the index tie-break. Counting a row takes
    O(n) for n columns, so time is O(m · n + m log k) for m squads, and the
    heap uses O(k) space. Because each row is sorted, the count could also
    come from a binary search for the first 0.

The lesson behind it: Top K Elements
    https://bytepatterns.com/learn/heaps/top-k-elements
    python heaps/04-top-k-elements.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/heaps/k-weakest-squads

Run it:  python problems/heaps/11-k-weakest-squads.py
"""


import heapq

def k_weakest(roster, k):
    heap = []                                # k weakest so far, strongest at the root
    for i, row in enumerate(roster):
        entry = (-sum(row), -i)              # negated: heapq keeps the smallest on top
        if len(heap) < k:
            heapq.heappush(heap, entry)
        elif entry > heap[0]:                # weaker than the strongest kept squad
            heapq.heapreplace(heap, entry)
    return [-i for _, i in sorted(heap, reverse=True)]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(k_weakest([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], 3), [2, 0, 3])
    check(k_weakest([[1, 0], [1, 0], [0, 0]], 2), [2, 0])
    check(k_weakest([[1, 1]], 1), [0])
