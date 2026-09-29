"""
K Smallest Pair Sums (medium) · patterns: k-way-merge, min-heap

Two lists a and b are sorted in ascending order. A pair takes one value from
a and one from b. Return the k pairs with the smallest sums, smallest sum
first, breaking ties by the position in a and then by the position in b. If
there are fewer than k pairs in total, return all of them.

Examples:

    Input:  a = [1, 7, 11], b = [2, 4, 6], k = 3
    Output: [[1, 2], [1, 4], [1, 6]]
    Why:    the next smallest sum, 7 + 2, is larger than all three

    Input:  a = [1, 1, 2], b = [1, 2, 3], k = 2
    Output: [[1, 1], [1, 1]]
    Why:    equal values at different positions are different pairs

    Input:  a = [1, 2], b = [3], k = 3
    Output: [[1, 3], [2, 3]]
    Why:    edge case, only two pairs exist, so both are returned

Approach:
    For a fixed position i in a, the pairs with every value of b form a row
    that is already sorted by sum, so the answer is the first k values of a
    k-way merge over those rows. A heap holds the front of each live row,
    keyed by sum and then by both positions, which is exactly the required
    tie order. Rows beyond the first k values of a can never make the cut,
    because each of their pairs is preceded by at least k pairs with no
    larger sum and an earlier position. Time is O(k log k) and the heap
    holds at most k entries.

The lesson behind it: K-Way Merge
    https://bytepatterns.com/learn/two-heaps-k-way/k-way-merge
    python two-heaps-k-way/02-k-way-merge.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/two-heaps-k-way/k-smallest-pair-sums

Run it:  python problems/two-heaps-k-way/05-k-smallest-pair-sums.py
"""


import heapq

def smallest_pairs(a, b, k):
    if not a or not b:
        return []
    heap = [(a[i] + b[0], i, 0) for i in range(min(k, len(a)))]   # row fronts
    heapq.heapify(heap)
    out = []
    while heap and len(out) < k:
        _, i, j = heapq.heappop(heap)
        out.append([a[i], b[j]])
        if j + 1 < len(b):                      # advance along row i only
            heapq.heappush(heap, (a[i] + b[j + 1], i, j + 1))
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(smallest_pairs([1, 7, 11], [2, 4, 6], 3), [[1, 2], [1, 4], [1, 6]])
    check(smallest_pairs([1, 1, 2], [1, 2, 3], 2), [[1, 1], [1, 1]])
    check(smallest_pairs([1, 2], [3], 3), [[1, 3], [2, 3]])
