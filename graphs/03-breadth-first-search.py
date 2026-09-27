"""
Breadth-First Search: Sweep outward one ring at a time, using a queue.

Breadth-first search visits everything one hop away, then everything two
hops away, and so on. A queue enforces that order: you always take the
oldest waiting node. Mark a node the moment you enqueue it, or a shared
neighbour gets queued twice.

Lesson 3 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/breadth-first-search

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python graphs/03-breadth-first-search.py
"""


from collections import deque
grid = {"sub": ["a", "b"], "a": ["sub", "c"], "b": ["sub", "c"], "c": ["a", "b", "d"], "d": ["c"]}

def bfs(start):
    seen, order = {start}, [start]
    q = deque([start])
    while q:
        for nb in grid[q.popleft()]:     # oldest node first
            if nb not in seen:
                seen.add(nb)             # mark on enqueue
                order.append(nb)
                q.append(nb)
    return order


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(bfs("sub"), ['sub', 'a', 'b', 'c', 'd'])
