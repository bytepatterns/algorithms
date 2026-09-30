"""
Cheapest Route Between Two Stops (easy) · patterns: dijkstra, min-heap

A delivery map has n stops numbered 0 to n - 1 and one-way roads given as
[u, v, cost], where every cost is zero or more. Return the cheapest total
cost of driving from stop src to stop dst, or -1 if dst cannot be reached.

Examples:

    Input:  n = 5, roads = [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 1], [2, 3, 5], [3, 4, 3]], src = 0, dst = 4
    Output: 7
    Why:    0 to 2 to 1 to 3 to 4 costs 1 + 2 + 1 + 3, cheaper than the direct road to 1 that costs 4 on its own

    Input:  n = 3, roads = [[0, 1, 2]], src = 0, dst = 2
    Output: -1
    Why:    no road leads into stop 2

    Input:  n = 2, roads = [[0, 1, 5]], src = 1, dst = 1
    Output: 0
    Why:    edge case, the route is already at its destination

Approach:
    Dijkstra's algorithm settles stops in order of their cheapest cost.
    Because no road has a negative cost, the stop at the top of the min-heap
    cannot be reached more cheaply later, so the first time dst is popped
    its cost is final and the search can stop. A stop may be pushed several
    times as cheaper routes are found, and the older, more expensive entries
    are skipped when they surface. With m roads, time is O((n + m) log n)
    and space is O(n + m).

The lesson behind it: Dijkstra's Algorithm
    https://bytepatterns.com/learn/graphs/dijkstra-intro
    python graphs/07-dijkstra-intro.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/cheapest-route-between-two-stops

Run it:  python problems/graphs/18-cheapest-route-between-two-stops.py
"""


import heapq

def cheapest_route(n, roads, src, dst):
    graph = [[] for _ in range(n)]
    for u, v, cost in roads:
        graph[u].append((v, cost))
    best = [float("inf")] * n
    best[src] = 0
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if u == dst:
            return d                      # the first pop of dst is final
        if d > best[u]:
            continue                      # an older, more expensive entry
        for v, cost in graph[u]:
            if d + cost < best[v]:
                best[v] = d + cost
                heapq.heappush(heap, (best[v], v))
    return -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(cheapest_route(5, [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 1], [2, 3, 5], [3, 4, 3]], 0, 4), 7)
    check(cheapest_route(3, [[0, 1, 2]], 0, 2), -1)
    check(cheapest_route(2, [[0, 1, 5]], 1, 1), 0)
