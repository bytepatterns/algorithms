"""
Heap Basics: Not sorted — just guaranteed to know its own winner.

A heap is a complete binary tree where every parent beats its children —
smaller, in a min-heap. That is a much weaker promise than sorting, and much
cheaper to keep.

Only the root is guaranteed. Push and pop cost O(log n); peeking at the
winner costs O(1). The tree lives in a plain array: node i has children at
2i + 1 and 2i + 2.

Lesson 1 of Heaps, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/heaps/heap-basics

Run it:  python heaps/01-heap-basics.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    import heapq

    bids = [7, 3, 9, 1]
    heapq.heapify(bids)            # rearranges in place, O(n)
    check(bids[0], 1)  # the winner, read in O(1)
    heapq.heappush(bids, 2)        # O(log n)
    check(heapq.heappop(bids), 1)  # removes the minimum
    check(heapq.heappop(bids), 2)

    # Python has no max-heap: negate on the way in and out.
    top = []
    for x in [7, 3, 9]:
        heapq.heappush(top, -x)
    check(-top[0], 9)
