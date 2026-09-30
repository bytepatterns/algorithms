"""
Cheapest Path Across a Grid (easy) · patterns: grid-dp, 2d-dp

A grid holds a non-negative cost in every cell. You start in the top-left
cell and must reach the bottom-right cell, moving only right or down. Return
the smallest possible sum of the costs of the cells you pass through,
including the first and last cells.

Examples:

    Input:  grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    Output: 7
    Why:    right, right, down, down visits 1, 3, 1, 1, 1 and avoids the 5 in the middle

    Input:  grid = [[2, 1, 4], [3, 1, 1]]
    Output: 5
    Why:    right, down, right visits 2, 1, 1, 1

    Input:  grid = [[7]]
    Output: 7
    Why:    edge case, the start is also the finish

Approach:
    Every path into a cell arrives from above or from the left, so the
    cheapest way to reach it extends the cheaper of those two cheapest ways.
    Filling the table row by row guarantees both neighbours are final before
    a cell needs them. The first row and first column have only one way in,
    which is why they are handled on their own. Time is O(rows · cols) and
    space is O(rows · cols), and because each row only reads the row above
    it, a single row of the table is enough if memory matters.

The lesson behind it: DP on Grids
    https://bytepatterns.com/learn/dynamic-programming/dp-on-grids
    python dynamic-programming/10-dp-on-grids.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/cheapest-path-across-a-grid

Run it:  python problems/dynamic-programming/25-cheapest-path-across-a-grid.py
"""


def cheapest_path(grid):
    rows, cols = len(grid), len(grid[0])
    cost = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                cost[r][c] = grid[r][c]
            elif r == 0:
                cost[r][c] = cost[r][c - 1] + grid[r][c]      # top row: only from the left
            elif c == 0:
                cost[r][c] = cost[r - 1][c] + grid[r][c]      # left column: only from above
            else:
                cost[r][c] = min(cost[r - 1][c], cost[r][c - 1]) + grid[r][c]
    return cost[-1][-1]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(cheapest_path([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
    check(cheapest_path([[2, 1, 4], [3, 1, 1]]), 5)
    check(cheapest_path([[7]]), 7)
