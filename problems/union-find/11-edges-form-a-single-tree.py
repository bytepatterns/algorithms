"""
Edges Form a Single Tree (easy) · patterns: union-find, cycle-detection

You are given n nodes labelled 0 to n - 1 and a list of undirected edges.
Return whether the edges form exactly one tree: every node is connected to
every other, and there is no cycle.

Examples:

    Input:  n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    Output: True

    Input:  n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    Output: False
    Why:    1, 2 and 3 form a cycle

    Input:  n = 4, edges = [[0, 1], [2, 3]]
    Output: False
    Why:    edge case, no cycle, but the graph is in two pieces

Approach:
    Two facts about trees do all the work. A tree on n nodes has exactly n -
    1 edges, and a graph with n - 1 edges and no cycle is always connected,
    since each edge that joins two different components reduces the
    component count by one, from n down to exactly 1. So after the count
    check the only question is whether some edge closes a cycle, which is
    precisely what a disjoint set answers: an edge whose two ends already
    have the same root connects nodes that were connected before. Path
    halving keeps the trees shallow. Time is O(n · α(n)), effectively
    linear, and space is O(n).

The lesson behind it: Components & Cycles
    https://bytepatterns.com/learn/union-find/components-and-cycles
    python union-find/04-components-and-cycles.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/union-find/edges-form-a-single-tree

Run it:  python problems/union-find/11-edges-form-a-single-tree.py
"""


def is_single_tree(n, edges):
    if len(edges) != n - 1:
        return False
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]    # path halving
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:                         # already connected: this edge closes a cycle
            return False
        parent[ra] = rb
    return True


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(is_single_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True)
    check(is_single_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False)
    check(is_single_tree(4, [[0, 1], [2, 3]]), False)
