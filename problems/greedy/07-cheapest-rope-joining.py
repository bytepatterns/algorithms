"""
Cheapest Rope Joining (medium) · patterns: greedy, min-heap

A rigger has several ropes with known lengths and must splice them into one.
Splicing two ropes costs the sum of their lengths and produces a rope of
that combined length, which can be spliced again later. Return the smallest
total cost of ending up with a single rope. With one rope or none there is
nothing to splice.

Examples:

    Input:  lengths = [4, 3, 2, 6]
    Output: 29
    Why:    2 + 3 = 5, then 4 + 5 = 9, then 6 + 9 = 15, and 5 + 9 + 15 = 29

    Input:  lengths = [1, 1, 1, 1]
    Output: 8
    Why:    two pairs cost 2 each, then the two halves cost 4

    Input:  lengths = [8]
    Output: 0
    Why:    edge case, already a single rope

Approach:
    Every original rope is paid for once per splice it takes part in, so the
    total cost is each length times its depth in the tree of splices.
    Exactly as in Huffman coding, splicing the two shortest ropes first is
    always safe: they can be placed deepest without making any other choice
    worse. A min-heap hands back the two shortest ropes in O(log n), and the
    spliced rope goes back in as a new candidate. Time is O(n log n) and
    space is O(n).

The lesson behind it: Huffman Intuition
    https://bytepatterns.com/learn/greedy/huffman-intuition
    python greedy/05-huffman-intuition.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/greedy/cheapest-rope-joining

Run it:  python problems/greedy/07-cheapest-rope-joining.py
"""


import heapq
def join_cost(lengths):
    heap = list(lengths)
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        a, b = heapq.heappop(heap), heapq.heappop(heap)   # the two shortest ropes
        total += a + b
        heapq.heappush(heap, a + b)                       # the splice joins the pool
    return total


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(join_cost([4, 3, 2, 6]), 29)
    check(join_cost([1, 1, 1, 1]), 8)
    check(join_cost([8]), 0)
