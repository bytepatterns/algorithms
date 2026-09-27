"""
K Closest Points: Keep the k best by always evicting the current worst.

You want the k nearest points out of n, and n may be huge. Hold exactly k
candidates in a heap ordered so the farthest one sits at the root.

Every new point pushes in; if the heap now holds k+1, evict the root.
Squared distance is enough — the square root would not change any
comparison.

Lesson 5 of Heaps, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/heaps/k-closest-points

Run it:  python heaps/05-k-closest-points.py
"""


import heapq

def k_closest(points, k):
    heap = []                                  # a max-heap, faked by negating
    for x, y in points:
        d = x * x + y * y                      # squared distance orders the same way
        heapq.heappush(heap, (-d, x, y))
        if len(heap) > k: heapq.heappop(heap)  # evict the farthest one held
    return sorted((x, y) for _, x, y in heap)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(k_closest([(1, 3), (-2, 2), (5, 8), (0, 1)], 2), [(-2, 2), (0, 1)])
