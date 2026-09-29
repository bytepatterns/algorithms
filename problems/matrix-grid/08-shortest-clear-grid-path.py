"""
Shortest Clear Grid Path (medium) · patterns: bfs, grid-traversal, shortest-path

A warehouse robot moves on a grid where 0 marks an open cell and 1 marks a
shelf. Each move goes one cell up, down, left or right, and only onto open
cells. Return the fewest moves needed to go from the top-left cell to the
bottom-right cell, or -1 if it cannot be done. The grid has at least one
cell.

Examples:

    Input:  grid = [[0, 0, 0, 0],
                    [1, 1, 0, 1],
                    [0, 0, 0, 0],
                    [0, 1, 1, 0]]
    Output: 6
    Why:    right twice, down twice, right once, down once

    Input:  grid = [[0, 1],
                    [1, 0]]
    Output: -1
    Why:    both neighbours of the start are shelves

    Input:  grid = [[0]]
    Output: 0
    Why:    edge case, the robot already stands on the goal

Approach:
    Treat each open cell as a node joined to its open neighbours, and every
    edge costs one move. Breadth-first search visits nodes in waves of equal
    distance, so the distance recorded when a cell is first reached is the
    shortest. Recording the distance at enqueue time also marks the cell as
    seen, which keeps each cell in the queue at most once. Time is O(rc) for
    r rows and c columns, and space is O(rc).

The lesson behind it: Shortest Path, Unweighted
    https://bytepatterns.com/learn/graphs/shortest-path-unweighted
    python graphs/06-shortest-path-unweighted.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/matrix-grid/shortest-clear-grid-path

Run it:  python problems/matrix-grid/08-shortest-clear-grid-path.py
"""


from collections import deque

def fewest_moves(grid):
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] or grid[rows - 1][cols - 1]:
        return -1                    # a blocked corner can never be used
    dist = {(0, 0): 0}
    queue = deque([(0, 0)])
    while queue:
        r, c = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return dist[r, c]        # first arrival is the shortest
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and not grid[nr][nc] and (nr, nc) not in dist:
                dist[nr, nc] = dist[r, c] + 1
                queue.append((nr, nc))
    return -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(fewest_moves([[0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0]]), 6)
    check(fewest_moves([[0, 1], [1, 0]]), -1)
    check(fewest_moves([[0]]), 0)
