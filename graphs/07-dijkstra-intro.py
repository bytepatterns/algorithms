"""
Dijkstra's Algorithm: When edges cost different amounts, always settle the nearest first.

With weighted edges, fewest hops stops meaning cheapest. Dijkstra keeps a
tentative distance for every node and repeatedly finalises whichever
unfinished node is currently nearest, relaxing its edges as it goes. A
min-heap supplies that nearest node. Negative weights break the guarantee.

Lesson 7 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/dijkstra-intro

Run it:  python graphs/07-dijkstra-intro.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    import heapq
    g = {"edge": [("hub", 9), ("relay", 2)], "relay": [("hub", 3), ("core", 8)],
         "hub": [("core", 1)], "core": []}
    dist = {n: float("inf") for n in g}
    dist["edge"] = 0
    pq = [(0, "edge")]
    while pq:
        d, n = heapq.heappop(pq)         # nearest unfinished node
        if d > dist[n]:
            continue                     # a stale, superseded entry
        for m, w in g[n]:
            if d + w < dist[m]:          # relax: cheaper route found
                dist[m] = d + w
                heapq.heappush(pq, (dist[m], m))
    check(dist, {'edge': 0, 'relay': 2, 'hub': 5, 'core': 6})
