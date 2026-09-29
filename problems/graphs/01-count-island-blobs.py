"""
Count Island Blobs (medium) · patterns: dfs, flood-fill, grid-traversal

A rectangular grid holds 1 for land and 0 for water. An island is a group of
land cells connected to each other through shared edges, so cells touching
only at a corner belong to different islands. Count how many separate
islands the grid contains.

Examples:

    Input:  [[1, 1, 0],
             [0, 1, 0],
             [0, 0, 1]]
    Output: 2
    Why:    the corner-touching cell at the bottom right is its own island

    Input:  [[0, 0],
             [0, 0]]
    Output: 0
    Why:    edge case, a grid of pure water has no islands

    Input:  [[1]]
    Output: 1
    Why:    edge case, a single land cell is a complete island

Approach:
    Each land cell is a node and edge-sharing land cells are connected, so
    counting islands is counting connected components. The outer scan starts
    a flood only at unvisited land, and the flood marks the entire component
    so the scan never counts it again. An explicit stack drives the flood,
    which avoids deep recursion on large grids. Time is O(rows times cols)
    since each cell is examined a constant number of times, and space is
    O(rows times cols) in the worst case.

The lesson behind it: Connected Components
    https://bytepatterns.com/learn/graphs/connected-components
    python graphs/05-connected-components.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/count-island-blobs

Run it:  python problems/graphs/01-count-island-blobs.py
"""


def count_islands(grid):
    if not grid: return 0
    rows, cols, seen = len(grid), len(grid[0]), set()
    def sink(r, c):                  # flood the whole blob from one cell
        stack = [(r, c)]
        while stack:
            i, j = stack.pop()
            for a, b in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= a < rows and 0 <= b < cols and grid[a][b] == 1 and (a, b) not in seen:
                    seen.add((a, b)); stack.append((a, b))
    total = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in seen:
                seen.add((r, c)); sink(r, c); total += 1   # a brand new island
    return total


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_islands([[1, 1, 0], [0, 1, 0], [0, 0, 1]]), 2)
    check(count_islands([[0, 0], [0, 0]]), 0)
    check(count_islands([[1]]), 1)
