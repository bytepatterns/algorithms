"""
Shortest Path, Unweighted: BFS already found it — store parents to read it back.

Every edge costs the same, so the first time BFS touches a node it has
arrived by the fewest possible hops. The distance is free. To recover the
route itself, record which node discovered each one, then follow those
parent links back from the goal and reverse.

Lesson 6 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/shortest-path-unweighted

Run it:  python graphs/06-shortest-path-unweighted.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    from collections import deque
    g = {"a1": ["b3", "c2"], "b3": ["a1", "d4"], "c2": ["a1", "d4"],
         "d4": ["b3", "c6"], "c6": ["d4"]}
    parent, q = {"a1": None}, deque(["a1"])
    while q:
        n = q.popleft()
        for m in g[n]:
            if m not in parent:
                parent[m] = n                # who reached m first
                q.append(m)
    node, path = "c6", []
    while node:                              # walk the trail backwards
        path.append(node)
        node = parent[node]
    check(path[::-1], ['a1', 'b3', 'd4', 'c6'])
