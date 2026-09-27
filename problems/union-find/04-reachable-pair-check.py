"""
Reachable Pair Check (easy) · patterns: union-find, connectivity

A network has n nodes numbered 0 to n minus 1 and a list of two-way links
between pairs of nodes. Given a source node and a target node, decide
whether some chain of links leads from one to the other. A node always
reaches itself.

Examples:

    Input:  n = 3, links = [[0, 1], [1, 2], [2, 0]], source = 0, target = 2
    Output: True

    Input:  n = 6, links = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source = 0, target = 5
    Output: False
    Why:    the links form two separate groups, {0, 1, 2} and {3, 4, 5}

    Input:  n = 1, links = [], source = 0, target = 0
    Output: True
    Why:    edge case, a node reaches itself without any link

Approach:
    Each link merges the groups of its two ends, so after processing every
    link the disjoint sets are exactly the connected groups, whatever order
    the links came in. Reachability is then one comparison of roots. Path
    halving, which points each visited node at its grandparent during a
    find, keeps the parent chains short without any extra bookkeeping. With
    m links, time is O((n + m) times the inverse Ackermann function),
    effectively linear, and space is O(n).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/union-find/reachable-pair-check

Run it:  python problems/union-find/04-reachable-pair-check.py
"""


def reachable(n, links, source, target):
    parent = list(range(n))                   # every node starts alone
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]     # path halving
            x = parent[x]
        return x
    for u, v in links:
        parent[find(u)] = find(v)             # a link merges two groups
    return find(source) == find(target)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(reachable(3, [[0, 1], [1, 2], [2, 0]], 0, 2), True)
    check(reachable(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5), False)
    check(reachable(1, [], 0, 0), True)
