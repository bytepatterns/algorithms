"""
Same Value Along Every Diagonal (easy) · patterns: matrix-indexing, diagonals

A test pattern for a display is stored as a grid of numbers. It is valid
only when every diagonal running from top-left to bottom-right holds a
single repeated value. Given the grid, return True if it is valid and False
otherwise. The grid has between 1 and 20 rows and between 1 and 20 columns,
and each value is between 0 and 99.

Examples:

    Input:  grid = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    Output: True
    Why:    the diagonals are [9], [5, 5], [1, 1, 1], [2, 2, 2], [3, 3] and [4]

    Input:  grid = [[1, 2], [2, 2]]
    Output: False
    Why:    the main diagonal holds 1 and then 2

    Input:  grid = [[7]]
    Output: True
    Why:    edge case, a single cell is one diagonal with one value

Approach:
    Moving one step down and one step right keeps row minus column
    unchanged, so each cell's diagonal predecessor is the cell at row - 1,
    column - 1. If every cell equals that predecessor, equality chains from
    the first cell of each diagonal to its last, so the whole diagonal holds
    one value; a single mismatch breaks it. Checking each cell against its
    neighbour needs no extra storage, and the same check works if rows
    arrive one at a time, since each new row only has to match the previous
    row shifted right by one. Time is O(rows × cols) and space is O(1).

The lesson behind it: Rotate In Place
    https://bytepatterns.com/learn/matrix-grid/rotate-in-place
    python matrix-grid/03-rotate-in-place.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/matrix-grid/same-value-along-every-diagonal

Run it:  python problems/matrix-grid/10-same-value-along-every-diagonal.py
"""


def diagonal_constant(grid):
    for r in range(1, len(grid)):
        for c in range(1, len(grid[0])):
            if grid[r][c] != grid[r - 1][c - 1]:   # up-left neighbour differs
                return False
    return True


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(diagonal_constant([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]), True)
    check(diagonal_constant([[1, 2], [2, 2]]), False)
    check(diagonal_constant([[7]]), True)
