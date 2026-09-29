"""
Kth Smallest In Matrix (medium) · patterns: k-way-merge, heap

You are given a square grid whose every row is sorted left to right and
whose every column is sorted top to bottom. Return the k-th smallest value
when all the cells are considered as one collection. Duplicates count
separately, so the third smallest of 1, 1, 2 is 2.

Examples:

    Input:  matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], k = 8
    Output: 13
    Why:    in order the cells read 1, 5, 9, 10, 11, 12, 13, 13, 15

    Input:  matrix = [[1, 2], [1, 3]], k = 3
    Output: 2
    Why:    duplicates are counted separately, so the order is 1, 1, 2, 3

    Input:  matrix = [[-5]], k = 1
    Output: -5
    Why:    edge case, a single cell

Approach:
    Treat each row as a sorted stream and merge them with a heap that never
    holds more than one entry per row. Each entry carries its row and
    column, so after a pop you know exactly which row to advance. Popping
    k-1 times leaves the answer at the root. Time is O(k log n) for an n-row
    grid, space is O(n) — far better than O(n² log n) for sorting everything
    when k is small.

The lesson behind it: Kth Smallest in a Matrix
    https://bytepatterns.com/learn/searching/kth-smallest-matrix
    python searching/08-kth-smallest-matrix.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/two-heaps-k-way/kth-smallest-in-sorted-matrix

Run it:  python problems/two-heaps-k-way/01-kth-smallest-in-sorted-matrix.py
"""


import heapq

def kth_smallest(matrix, k):
    heap = [(row[0], r, 0) for r, row in enumerate(matrix) if row]
    heapq.heapify(heap)                      # one head per row, nothing more
    for _ in range(k - 1):
        value, r, c = heapq.heappop(heap)
        if c + 1 < len(matrix[r]):           # advance only that row
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
    return heap[0][0]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8), 13)
    check(kth_smallest([[1, 2], [1, 3]], 3), 2)
    check(kth_smallest([[-5]], 1), -5)
