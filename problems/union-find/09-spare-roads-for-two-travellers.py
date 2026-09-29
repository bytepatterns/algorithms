"""
Spare Roads for Two Travellers (hard) · patterns: union-find, greedy

A region has n towns numbered 1 to n and a list of roads [kind, u, v]. A
road of kind 1 may be used only by the cyclist, kind 2 only by the driver,
and kind 3 by both. The council wants to close as many roads as possible
while each traveller can still get from every town to every other town using
the roads open to them. Return the largest number of roads that can be
closed, or -1 if even the full network fails one of the travellers.

Examples:

    Input:  n = 4, roads = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
    Output: 2
    Why:    [1, 1, 2] and [1, 1, 3] duplicate links the shared roads already give the cyclist

    Input:  n = 4, roads = [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]
    Output: 0
    Why:    every road is needed by at least one traveller

    Input:  n = 4, roads = [[3, 2, 3], [1, 1, 2], [2, 3, 4]]
    Output: -1
    Why:    edge case, the cyclist can never reach town 4 and the driver never town 1

Approach:
    Each traveller needs their open roads to form one connected group, and
    any road that closes a cycle in a traveller's view is redundant for that
    traveller. A shared road that joins two groups does the work of two
    private roads at the cost of one, and any forest of shared roads can
    later be completed with private ones, so taking every useful shared road
    before any private road is never worse. Because both travellers see the
    same shared roads, a shared road joins two groups for one traveller
    exactly when it does for the other at that stage. Private roads come
    next, each offered only to its own traveller's structure. If either
    structure still has more than one group at the end, the task is
    impossible; otherwise every road that was never kept can be closed. Time
    is O(m times the inverse Ackermann function) for m roads and space is
    O(n).

The lesson behind it: Components & Cycles
    https://bytepatterns.com/learn/union-find/components-and-cycles
    python union-find/04-components-and-cycles.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/union-find/spare-roads-for-two-travellers

Run it:  python problems/union-find/09-spare-roads-for-two-travellers.py
"""


def spare_roads(n, roads):
    def dsu():
        parent = list(range(n + 1))
        def join(a, b):                        # True if a and b were apart
            while parent[a] != a: parent[a] = a = parent[parent[a]]
            while parent[b] != b: parent[b] = b = parent[parent[b]]
            parent[a] = b
            return a != b
        return join
    cyclist, driver = dsu(), dsu()
    kept = joins_c = joins_d = 0
    for kind in (3, 1, 2):                     # shared roads first
        for t, u, v in roads:
            if t != kind: continue
            c = t != 2 and cyclist(u, v)
            d = t != 1 and driver(u, v)
            joins_c += c; joins_d += d; kept += c or d
    if joins_c != n - 1 or joins_d != n - 1:
        return -1                              # someone is left stranded
    return len(roads) - kept


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(spare_roads(4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]), 2)
    check(spare_roads(4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]), 0)
    check(spare_roads(4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]]), -1)
