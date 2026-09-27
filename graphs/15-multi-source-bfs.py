"""
Multi-Source BFS: Seed the queue with every source and one sweep answers them all.

Running BFS once per source repeats the same work S times. Instead, push
every source into the queue with distance zero and let a single wavefront
expand. Whichever source reaches a node first is its nearest one, which is
exactly the answer. One sweep, one queue, O(V + E) total.

Lesson 15 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/multi-source-bfs

Run it:  python graphs/15-multi-source-bfs.py
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
    grid = [["hot", "cool", "cool"],
            ["cool", "cool", "hot"],
            ["cool", "cool", "cool"]]

    rows, cols = len(grid), len(grid[0])
    dist = [[-1] * cols for _ in range(rows)]
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "hot":          # every source starts at 0
                dist[r][c] = 0
                q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    check(max(max(row) for row in dist), 2)
