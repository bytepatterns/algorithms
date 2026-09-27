"""
Sliding Window Median: You cannot dig a value out of a heap — so mark it dead instead.

A window median wants the two-heap split again — but each slide evicts a
value that may be buried anywhere inside a heap, and a heap has no way to
reach it.

So do not reach. Record the value as dead in a counter and carry on. Only
when a dead value rises to a root does it actually get popped, because the
root is the one thing you ever read.

Lesson 4 of Two Heaps & K-Way Merge, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/two-heaps-k-way/sliding-window-median

Run it:  python two-heaps-k-way/04-sliding-window-median.py
"""


import heapq

def peek_after_removals(values, removed):
    heap = list(values)
    heapq.heapify(heap)
    dead = {}
    for r in removed:                         # mark, never search
        dead[r] = dead.get(r, 0) + 1
    while heap and dead.get(heap[0], 0):      # clean only at the root
        dead[heap[0]] -= 1
        heapq.heappop(heap)
    return heap[0]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(peek_after_removals([4, 1, 7, 3], [1]), 3)
    check(peek_after_removals([4, 1, 7, 3], [1, 3]), 4)
