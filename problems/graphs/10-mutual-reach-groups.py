"""
Mutual Reach Groups (hard) · patterns: strongly-connected-components, dfs

A directed graph has n nodes numbered from 0 and a list of one-way edges (u,
v). Split the nodes into groups so that two nodes share a group exactly when
each can reach the other by following edges. Return the groups, each sorted
ascending, with the list of groups sorted as well. A node that reaches
nobody and is reached by nobody still forms a group of its own.

Examples:

    Input:  n = 5, edges = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4)]
    Output: [[0, 1, 2], [3], [4]]
    Why:    0, 1 and 2 form a loop; 3 and 4 can never get back

    Input:  n = 4, edges = [(0, 1), (1, 0), (2, 3), (3, 2), (1, 2)]
    Output: [[0, 1], [2, 3]]
    Why:    the edge 1 -> 2 runs one way only, so the pairs stay apart

    Input:  n = 1, edges = []
    Output: [[0]]
    Why:    edge case, a lone node is its own group

Approach:
    This is Kosaraju's two-pass method. The first depth-first pass records
    nodes by finishing time, and the node that finishes last always belongs
    to a group that no other group can reach. The second pass runs on the
    reversed graph in reverse finishing order: from such a node the reversed
    edges lead only into its own group, so each search collects one group
    and nothing more. Sorting at the end makes the output order fixed. Time
    is O(n + m) for the passes plus the final sort, and space is O(n + m).

The lesson behind it: Strongly Connected Parts
    https://bytepatterns.com/learn/graphs/strongly-connected-components
    python graphs/16-strongly-connected-components.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/mutual-reach-groups

Run it:  python problems/graphs/10-mutual-reach-groups.py
"""


def reach_groups(n, edges):
    fwd, back = [[] for _ in range(n)], [[] for _ in range(n)]
    for u, v in edges: fwd[u].append(v); back[v].append(u)
    order, seen, owner = [], [False] * n, [None] * n
    def finish(u):                       # pass 1: record nodes as they finish
        seen[u] = True
        for v in fwd[u]:
            if not seen[v]: finish(v)
        order.append(u)
    def claim(u, group):                 # pass 2: reversed edges cannot leave the group
        owner[u] = group; group.append(u)
        for v in back[u]:
            if owner[v] is None: claim(v, group)
    for u in range(n):
        if not seen[u]: finish(u)
    groups = []
    for u in reversed(order):            # latest finisher first
        if owner[u] is None: groups.append([]); claim(u, groups[-1])
    return sorted(sorted(g) for g in groups)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(reach_groups(5, [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4)]), [[0, 1, 2], [3], [4]])
    check(reach_groups(4, [(0, 1), (1, 0), (2, 3), (3, 2), (1, 2)]), [[0, 1], [2, 3]])
    check(reach_groups(1, []), [[0]])
