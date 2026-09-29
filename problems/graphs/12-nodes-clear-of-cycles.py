"""
Nodes Clear of Cycles (medium) · patterns: dfs, graph-colouring, cycle-detection

A build system has n steps numbered 0 to n - 1, and graph[i] lists the steps
that step i hands off to, as a directed graph. A step is safe when every
chain of hand-offs starting from it eventually stops, which means no chain
from it can reach a cycle. Return the safe steps in increasing order. A step
that hands off to itself forms a cycle.

Examples:

    Input:  graph = [[1, 2], [2], [3], [], [5], [4], [3, 4]]
    Output: [0, 1, 2, 3]
    Why:    4 and 5 hand off to each other forever, and 6 can reach them

    Input:  graph = [[], [0], [1]]
    Output: [0, 1, 2]
    Why:    every chain ends at step 0, which hands off to nobody

    Input:  graph = [[0]]
    Output: []
    Why:    edge case, the only step loops back to itself

Approach:
    This is the three-colour cycle search with its colours reused as a memo.
    A step turns black only after every step it can reach has turned black,
    so black means no cycle is reachable. A search that meets a grey step
    has found a back edge, and every step on the current path can reach that
    cycle, so those steps are left grey for good and later searches treat
    grey as unsafe. Every step and edge is handled once, so time is O(n + e)
    for e hand-offs, and space is O(n) for the colours and the recursion.

The lesson behind it: Cycles in a Directed Graph
    https://bytepatterns.com/learn/graphs/directed-cycle-colours
    python graphs/13-directed-cycle-colours.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/nodes-clear-of-cycles

Run it:  python problems/graphs/12-nodes-clear-of-cycles.py
"""


def safe_steps(graph):
    WHITE, GREY, BLACK = 0, 1, 2
    colour = [WHITE] * len(graph)
    def safe(u):
        if colour[u] != WHITE:
            return colour[u] == BLACK    # grey: on the path now, or proven unsafe
        colour[u] = GREY
        for v in graph[u]:
            if not safe(v):
                return False             # u stays grey: it reaches a cycle
        colour[u] = BLACK
        return True
    return [u for u in range(len(graph)) if safe(u)]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(safe_steps([[1, 2], [2], [3], [], [5], [4], [3, 4]]), [0, 1, 2, 3])
    check(safe_steps([[], [0], [1]]), [0, 1, 2])
    check(safe_steps([[0]]), [])
