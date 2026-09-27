"""
Smash Heaviest Stones (easy) · patterns: max-heap, simulation

A pile of stones is described by their weights. Repeatedly take the two
heaviest stones and smash them together: equal stones destroy each other
completely, while unequal ones leave a single stone weighing the difference,
which goes back into the pile. Return the weight of the last stone left, or
0 when the pile empties.

Examples:

    Input:  stones = [2, 7, 4, 1, 8, 1]
    Output: 1
    Why:    7 and 8 leave 1, then 2 and 4 leave 2, then 1 and 2 leave 1, then 1 and 1 vanish

    Input:  stones = [1, 1]
    Output: 0
    Why:    two equal stones destroy each other and nothing remains

    Input:  stones = [3]
    Output: 3
    Why:    edge case, a lone stone has nothing to smash against

Approach:
    Only two questions are ever asked of the pile, give me the heaviest and
    take this new stone, which is exactly what a heap answers in logarithmic
    time. Building it once and then smashing repeatedly avoids re-sorting
    after every round. A difference of zero is simply not pushed back, so
    the pile shrinks by two in that case and by one otherwise, and the loop
    ends with either one stone or none. Time is O(n log n), and space is
    O(n) for the heap.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/heaps/smash-heaviest-stones

Run it:  python problems/heaps/02-smash-heaviest-stones.py
"""


import heapq
def last_stone_weight(stones):
    heap = [-w for w in stones]      # negated, because the library heap is a min-heap
    heapq.heapify(heap)
    while len(heap) > 1:
        heaviest = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        if heaviest != second:       # equal stones vanish, so nothing goes back
            heapq.heappush(heap, -(heaviest - second))
    return -heap[0] if heap else 0


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(last_stone_weight([2, 7, 4, 1, 8, 1]), 1)
    check(last_stone_weight([1, 1]), 0)
    check(last_stone_weight([3]), 3)
