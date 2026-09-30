"""
Deadlock in a Wait-For Graph (easy) · patterns: cycle-detection, graph-colouring, topological-sort

A database tracks n transactions numbered 0 to n - 1. Each pair [a, b] in
waits means transaction a is waiting for a lock that transaction b holds. A
deadlock exists when some group of transactions waits on each other in a
circle. Return True if the wait-for graph contains a deadlock, otherwise
False.

Examples:

    Input:  n = 4, waits = [[0, 1], [1, 2], [2, 0], [3, 0]]
    Output: True
    Why:    0 waits for 1, 1 for 2 and 2 for 0, so none of them can ever proceed

    Input:  n = 4, waits = [[0, 1], [0, 2], [1, 3], [2, 3]]
    Output: False
    Why:    two chains meet at 3, but meeting is not a circle, and 3 waits for nobody

    Input:  n = 2, waits = []
    Output: False
    Why:    edge case, nobody waits, so nobody is stuck

Approach:
    The three-colour depth-first search separates the two cases a visited
    set cannot. White transactions are unexplored, grey ones are on the path
    currently being walked, and black ones are fully explored and proven to
    lead nowhere circular. An edge into a grey transaction closes a loop
    through the current path, which is a deadlock, while an edge into a
    black transaction only joins an already cleared branch. A graph with no
    deadlock is exactly one that has a topological order, so this check also
    tells you whether the transactions could be scheduled one after another.
    Every transaction and wait is visited once, so time is O(n + m) for m
    waits, and space is O(n + m).

The lesson behind it: Cycles in a Directed Graph
    https://bytepatterns.com/learn/graphs/directed-cycle-colours
    python graphs/13-directed-cycle-colours.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/deadlock-in-a-wait-for-graph

Run it:  python problems/graphs/17-deadlock-in-a-wait-for-graph.py
"""


def has_deadlock(n, waits):
    graph = [[] for _ in range(n)]
    for a, b in waits:
        graph[a].append(b)
    WHITE, GREY, BLACK = 0, 1, 2
    colour = [WHITE] * n

    def visit(u):
        colour[u] = GREY                  # on the current path
        for v in graph[u]:
            if colour[v] == GREY:         # walked back into the path: a circle
                return True
            if colour[v] == WHITE and visit(v):
                return True
        colour[u] = BLACK                 # fully explored, no circle through u
        return False

    return any(colour[u] == WHITE and visit(u) for u in range(n))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(has_deadlock(4, [[0, 1], [1, 2], [2, 0], [3, 0]]), True)
    check(has_deadlock(4, [[0, 1], [0, 2], [1, 3], [2, 3]]), False)
    check(has_deadlock(2, []), False)
