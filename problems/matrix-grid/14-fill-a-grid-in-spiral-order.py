"""
Fill a Grid in Spiral Order (easy) · patterns: matrix-traversal, direction-turning

Given a number of rows and columns, build a grid of that size filled with
the numbers 1 to rows × cols in an inward clockwise spiral: along the top
row to the right, down the right column, back along the bottom row, up the
left column, and around again until every cell is filled. Return the grid as
a list of rows.

Examples:

    Input:  rows = 3, cols = 3
    Output: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    Why:    the spiral ends in the centre cell

    Input:  rows = 3, cols = 4
    Output: [[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]]
    Why:    a wide grid ends on a short middle row instead of a single cell

    Input:  rows = 1, cols = 1
    Output: [[1]]
    Why:    edge case, the spiral is a single step

Approach:
    Filling a spiral is the reading version run backwards, and the simplest
    way to write it is to walk: keep a position and a direction, write the
    next number, and turn clockwise whenever the next step would leave the
    grid or hit a filled cell. The filled cells act as the shrinking
    boundary, so there are no four separate edge loops and no special cases
    for a single row or column. Each cell is written exactly once and each
    step does constant work, so time is O(rows × cols) and the only space is
    the grid itself.

The lesson behind it: Spiral Order
    https://bytepatterns.com/learn/matrix-grid/spiral-order
    python matrix-grid/02-spiral-order.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/matrix-grid/fill-a-grid-in-spiral-order

Run it:  python problems/matrix-grid/14-fill-a-grid-in-spiral-order.py
"""


def spiral_fill(rows, cols):
    grid = [[0] * cols for _ in range(rows)]      # 0 = not filled yet
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]    # right, down, left, up
    r = c = d = 0
    for value in range(1, rows * cols + 1):
        grid[r][c] = value
        nr, nc = r + moves[d][0], c + moves[d][1]
        if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc]:
            d = (d + 1) % 4                       # blocked: turn clockwise
            nr, nc = r + moves[d][0], c + moves[d][1]
        r, c = nr, nc
    return grid


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(spiral_fill(3, 3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
    check(spiral_fill(3, 4), [[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]])
    check(spiral_fill(1, 1), [[1]])
