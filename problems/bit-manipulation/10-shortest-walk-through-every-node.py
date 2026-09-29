"""
Shortest Walk Through Every Node (hard) · patterns: bitmask, bfs

A connected undirected graph has n nodes, numbered 0 to n - 1, where n is at
most 12, given as adjacency lists. Return the fewest edges in a walk that
visits every node at least once. The walk may start and end at any nodes,
and it may repeat both nodes and edges.

Examples:

    Input:  adj = [[1, 3, 4], [0, 2], [1, 3, 5], [2, 0], [0], [2]]
    Output: 6
    Why:    a square 0-1-2-3 with a leaf on 0 and a leaf on 2;
            4-0-1-2-3-2-5 has to step back through 2 once

    Input:  adj = [[1, 2], [0, 2, 5], [0, 1, 3], [2, 4], [3], [1]]
    Output: 5
    Why:    5-1-0-2-3-4 touches all six nodes without repeating one

    Input:  adj = [[]]
    Output: 0
    Why:    edge case, a single node is visited before any step is taken

Approach:
    A state is the current node together with the bitmask of visited nodes,
    and moving along any edge costs 1, so breadth-first search over states
    finds the fewest steps. Starting from every node with distance 0 lets
    the walk begin anywhere, and the first state whose mask is full gives
    the answer, wherever it ends. Revisiting nodes is allowed because the
    same node with a different mask is a different state, while the same
    node with the same mask is never queued twice. Time is O(2ⁿ times the
    number of edges), and space is O(n 2ⁿ) for the visited states.

The lesson behind it: Bitmask as a Set
    https://bytepatterns.com/learn/bit-manipulation/bitmask-as-a-set
    python bit-manipulation/05-bitmask-as-a-set.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/bit-manipulation/shortest-walk-through-every-node

Run it:  python problems/bit-manipulation/10-shortest-walk-through-every-node.py
"""


from collections import deque
def shortest_full_walk(adj):
    n = len(adj)
    full = (1 << n) - 1
    starts = [(v, 1 << v) for v in range(n)]
    seen = set(starts)
    queue = deque((v, mask, 0) for v, mask in starts)   # every node is a start
    while queue:
        v, mask, steps = queue.popleft()
        if mask == full:
            return steps
        for u in adj[v]:
            state = (u, mask | 1 << u)                   # stepping to u marks it visited
            if state not in seen:
                seen.add(state)
                queue.append((u, state[1], steps + 1))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(shortest_full_walk([[1, 3, 4], [0, 2], [1, 3, 5], [2, 0], [0], [2]]), 6)
    check(shortest_full_walk([[1, 2], [0, 2, 5], [0, 1, 3], [2, 4], [3], [1]]), 5)
    check(shortest_full_walk([[]]), 0)
