"""
Grid Paths With Blocks (medium) · patterns: grid-dp, bottom-up-dp

A robot starts in the top-left cell of a grid and wants to reach the
bottom-right cell, moving only right or down. Cells marked 1 are blocked and
cannot be entered, while cells marked 0 are free. Count the distinct paths
the robot can take, which is 0 when the start, the finish, or every route
between them is blocked.

Examples:

    Input:  [[0, 0, 0],
             [0, 1, 0],
             [0, 0, 0]]
    Output: 2
    Why:    the blocked centre leaves one route along each edge

    Input:  [[0, 1],
             [1, 0]]
    Output: 0
    Why:    both routes out of the start are blocked

    Input:  [[0]]
    Output: 1
    Why:    edge case, the robot already stands on the finish

Approach:
    Paths into a cell equal paths into the cell above plus paths into the
    cell to the left, and a blocked cell simply has zero. Sweeping row by
    row means a single row of counters can be reused: before a slot is
    overwritten it still holds the count from the row above, and the
    neighbour to the left has already been updated for the current row. The
    start is seeded with one way, and a blocked start short-circuits to
    zero. Time is O(rows times cols), and space is O(cols).

The lesson behind it: DP on Grids
    https://bytepatterns.com/learn/dynamic-programming/dp-on-grids
    python dynamic-programming/10-dp-on-grids.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/grid-paths-with-blocks

Run it:  python problems/dynamic-programming/02-grid-paths-with-blocks.py
"""


def paths_with_blocks(grid):
    if not grid or grid[0][0] == 1: return 0     # a blocked entrance ends it
    rows, cols = len(grid), len(grid[0])
    ways = [0] * cols                # one row of counters, reused downward
    ways[0] = 1                      # a single way to stand on the start
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                ways[c] = 0          # nothing can pass through a blocked cell
            elif c > 0:
                # the slot still holds the row above, add the cell to the left
                ways[c] += ways[c - 1]
    return ways[-1]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(paths_with_blocks([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)
    check(paths_with_blocks([[0, 1], [1, 0]]), 0)
    check(paths_with_blocks([[0]]), 1)
