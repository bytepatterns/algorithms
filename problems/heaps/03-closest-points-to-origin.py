"""
Closest Points To Origin (medium) · patterns: max-heap, top-k

Given points on a plane and a number k, return the k points lying closest to
the origin. Distance is the ordinary straight-line distance. Report the
chosen points ordered by distance, and when two points are equally far away
prefer the one with the smaller first coordinate, then the smaller second
one.

Examples:

    Input:  points = [[3, 3], [5, -1], [-2, 4]], k = 2
    Output: [(3, 3), (-2, 4)]
    Why:    their squared distances are 18 and 20, while the middle point sits at 26

    Input:  points = [[1, 0], [0, 1]], k = 1
    Output: [(0, 1)]
    Why:    edge case, an exact tie is broken by the smaller first coordinate

    Input:  points = [[1, 3], [-2, 2]], k = 1
    Output: [(-2, 2)]

Approach:
    Ranking by squared distance avoids the square root entirely without
    changing the order. Holding at most k candidates in a heap whose top is
    the furthest one means each new point costs a logarithm of k rather than
    a full sort, and the eviction rule keeps exactly the best k. Negating
    the key turns the library's min-heap into the max-heap this needs, and
    negating the coordinates makes the eviction prefer to drop the larger
    ones on a tie. Time is O(n log k) and space is O(k).

The lesson behind it: K Closest Points
    https://bytepatterns.com/learn/heaps/k-closest-points
    python heaps/05-k-closest-points.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/heaps/closest-points-to-origin

Run it:  python problems/heaps/03-closest-points-to-origin.py
"""


import heapq
def closest_points(points, k):
    heap = []                        # at most k points, the furthest one on top
    for x, y in points:
        heapq.heappush(heap, (-(x * x + y * y), -x, -y))
        if len(heap) > k:
            heapq.heappop(heap)      # drop the furthest point held so far
    chosen = [(-a, -b) for _, a, b in heap]
    return sorted(chosen, key=lambda p: (p[0] * p[0] + p[1] * p[1], p))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(closest_points([[3, 3], [5, -1], [-2, 4]], 2), [(3, 3), (-2, 4)])
    check(closest_points([[1, 0], [0, 1]], 1), [(0, 1)])
    check(closest_points([[1, 3], [-2, 2]], 1), [(-2, 2)])
