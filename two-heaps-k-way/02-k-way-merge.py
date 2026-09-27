"""
K-Way Merge: One heap of k heads turns k sorted lists into one.

Only the front value of a sorted list can be the next smallest overall. So
hold just those k heads in a min-heap.

Pop the winner, append it to the output, and push the value that stepped up
behind it. The heap never grows past k, no matter how long the lists are.

Lesson 2 of Two Heaps & K-Way Merge, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/two-heaps-k-way/k-way-merge

Run it:  python two-heaps-k-way/02-k-way-merge.py
"""


import heapq

def merge_k(lists):
    heap = [(rows[0], i, 0) for i, rows in enumerate(lists) if rows]
    heapq.heapify(heap)                 # k heads, nothing more
    out = []
    while heap:
        value, i, j = heapq.heappop(heap)
        out.append(value)
        if j + 1 < len(lists[i]):       # advance only that list
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
    check(merge_k([[1, 6, 9], [2, 4], [3, 8]]), [1, 2, 3, 4, 6, 8, 9])
    check(merge_k([[], [5]]), [5])
