"""
Redundant Connection (medium) · patterns: union-find, cycle-detection

A network was built by adding undirected links one at a time. It started as
a tree, so exactly one link too many was added and the network now contains
a single cycle. Given the links in the order they were added, return the one
that closed the cycle. If more than one would qualify, return the one added
last.

Examples:

    Input:  edges = [[1, 2], [1, 3], [2, 3]]
    Output: [2, 3]
    Why:    2 and 3 were already connected through 1 when this link arrived

    Input:  edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    Output: [1, 4]
    Why:    the path 1-2-3-4 already existed, so this link closed the loop

    Input:  edges = [[1, 2], [1, 2]]
    Output: [1, 2]
    Why:    edge case, the same link twice is still a cycle

Approach:
    Process the links in arrival order and merge their endpoints. A link
    between two different sets is part of the tree; a link whose endpoints
    already share a representative is the first — and, since the network
    holds exactly one cycle, the only — link that closes a loop. Returning
    on that first collision also satisfies the "added last" rule, because no
    later link can close another cycle. Time is O(n · α(n)), space O(n).

The lesson behind it: Components & Cycles
    https://bytepatterns.com/learn/union-find/components-and-cycles
    python union-find/04-components-and-cycles.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/union-find/redundant-connection

Run it:  python problems/union-find/02-redundant-connection.py
"""


def redundant(edges):
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]    # path halving
            x = parent[x]
        return x
    for u, v in edges:
        a, b = find(u), find(v)
        if a == b:                           # already reachable: this closes it
            return [u, v]
        parent[a] = b
    return []


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(redundant([[1, 2], [1, 3], [2, 3]]), [2, 3])
    check(redundant([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]), [1, 4])
    check(redundant([[1, 2], [1, 2]]), [1, 2])
