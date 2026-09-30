"""
Closest K Values to a Target (easy) · patterns: top-k, max-heap

Given an unsorted list of integers nums, a target and a count k, return the
k values closest to the target. When two values are equally far away, the
smaller value is closer. Return the chosen values in ascending order.

Examples:

    Input:  nums = [9, 2, 14, 5, 7, 11], target = 8, k = 3
    Output: [5, 7, 9]
    Why:    7 and 9 are 1 away, then 5 and 11 tie at 3 and the smaller value wins

    Input:  nums = [1, 10, 4, 4], target = 4, k = 2
    Output: [4, 4]
    Why:    repeated values count separately

    Input:  nums = [3], target = 100, k = 1
    Output: [3]
    Why:    edge case, the only value is the closest one however far it is

Approach:
    This is k closest points on a line: the distance is a single absolute
    difference, and the heap of size k keeps the k best candidates with the
    worst one at the root, ready to be evicted. Negating both the distance
    and the value turns Python's min-heap into that max-heap and folds the
    tie rule into the comparison, since a larger value on a tie is the worse
    candidate. A new value replaces the root only when its entry is greater,
    meaning closer, or equally close and smaller. Time is O(n log k) and the
    heap uses O(k) space, which matters when the list is a long stream and k
    is small.

The lesson behind it: K Closest Points
    https://bytepatterns.com/learn/heaps/k-closest-points
    python heaps/05-k-closest-points.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/heaps/closest-k-values-to-a-target

Run it:  python problems/heaps/12-closest-k-values-to-a-target.py
"""


import heapq

def closest_k(nums, target, k):
    heap = []                              # k closest so far, the worst at the root
    for x in nums:
        entry = (-abs(x - target), -x)     # farther, then larger, is worse
        if len(heap) < k:
            heapq.heappush(heap, entry)
        elif entry > heap[0]:              # closer than the worst kept value
            heapq.heapreplace(heap, entry)
    return sorted(-x for _, x in heap)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(closest_k([9, 2, 14, 5, 7, 11], 8, 3), [5, 7, 9])
    check(closest_k([1, 10, 4, 4], 4, 2), [4, 4])
    check(closest_k([3], 100, 1), [3])
