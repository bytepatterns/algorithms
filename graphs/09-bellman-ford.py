"""
Bellman-Ford: Relax every edge, V-1 times, and negative weights stop being a problem.

Dijkstra settles the nearest node and never looks back, which a negative
edge can invalidate. Bellman-Ford refuses to settle anything. It just
relaxes every edge, round after round, V-1 times — enough for the longest
possible shortest path. One extra round that still improves something proves
the graph has a negative cycle.

Lesson 9 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/bellman-ford

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python graphs/09-bellman-ford.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    edges = [("a", "b", 4), ("a", "c", 5), ("b", "c", -3), ("c", "d", 3)]
    nodes = ["a", "b", "c", "d"]
    dist = {n: float("inf") for n in nodes}
    dist["a"] = 0

    for _ in range(len(nodes) - 1):        # V-1 rounds is always enough
        for u, v, w in edges:
            if dist[u] + w < dist[v]:      # relax every edge, every round
                dist[v] = dist[u] + w

    negative_cycle = any(dist[u] + w < dist[v] for u, v, w in edges)
    check(dist, {'a': 0, 'b': 4, 'c': 1, 'd': 4})
    check(negative_cycle, False)
