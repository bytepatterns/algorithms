"""
Shortest Paths With Rebate Roads (easy) · patterns: bellman-ford, negative-edges

A region has n towns numbered 0 to n - 1 and one-way roads given as [u, v,
cost]. Some roads pay a rebate, so their cost is negative, but no loop of
roads has a negative total. Return the cheapest cost from town src to every
town, using None for towns that cannot be reached.

Examples:

    Input:  n = 4, roads = [[0, 1, 4], [0, 2, 5], [2, 1, -3], [1, 3, 2]], src = 0
    Output: [0, 2, 5, 4]
    Why:    going 0 to 2 to 1 costs 5 - 3 = 2, cheaper than the direct road to 1 that costs 4

    Input:  n = 3, roads = [[0, 1, -2]], src = 0
    Output: [0, -2, None]
    Why:    town 2 has no road leading into it

    Input:  n = 1, roads = [], src = 0
    Output: [0]
    Why:    edge case, the start town costs nothing to reach

Approach:
    Bellman-Ford does not trust any cost until enough passes have run. After
    pass k, every town whose cheapest path uses at most k roads has its
    final cost, because that path's last road was relaxed after its
    second-to-last town was already correct. A cheapest path never repeats a
    town when no loop has a negative total, so n - 1 passes are enough, and
    a pass with no change means every cost is final already. Cheapest-first
    search fails here because a rebate road found later can undercut a town
    it already settled. Time is O(n · m) for m roads, and space is O(n).

The lesson behind it: Bellman-Ford
    https://bytepatterns.com/learn/graphs/bellman-ford
    python graphs/09-bellman-ford.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/shortest-paths-with-rebate-roads

Run it:  python problems/graphs/19-shortest-paths-with-rebate-roads.py
"""


def cheapest_from(n, roads, src):
    INF = float("inf")
    cost = [INF] * n
    cost[src] = 0
    for _ in range(n - 1):                # a cheapest path uses at most n - 1 roads
        changed = False
        for u, v, c in roads:
            if cost[u] != INF and cost[u] + c < cost[v]:
                cost[v] = cost[u] + c     # relax the road
                changed = True
        if not changed:                   # nothing moved: every cost is final
            break
    return [x if x != INF else None for x in cost]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(cheapest_from(4, [[0, 1, 4], [0, 2, 5], [2, 1, -3], [1, 3, 2]], 0), [0, 2, 5, 4])
    check(cheapest_from(3, [[0, 1, -2]], 0), [0, -2, None])
    check(cheapest_from(1, [], 0), [0])
