"""
Rotate A Square Grid (medium) · patterns: in-place, transpose-reverse

Turn an n by n grid a quarter turn clockwise, so the first column read from
the bottom up becomes the first row. Do it in place, rearranging values
inside the grid you were given rather than building a second grid.

Examples:

    Input:  grid = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
    Output: [[7, 4, 1],
             [8, 5, 2],
             [9, 6, 3]]

    Input:  grid = [[1, 2],
                    [3, 4]]
    Output: [[3, 1],
             [4, 2]]

    Input:  grid = [[7]]
    Output: [[7]]
    Why:    edge case, a single cell turns into itself

Approach:
    A clockwise quarter turn sends the cell at row r, column c to row c,
    column n minus 1 minus r. Flipping across the main diagonal sends it to
    row c, column r, and reversing each row then sends that to row c, column
    n minus 1 minus r, which is the same destination. Both steps are made of
    swaps that never need a second grid; the flip only visits cells above
    the diagonal so each pair is swapped once. Every cell is touched a
    constant number of times, so time is O(n squared) and extra space is
    O(1).

The lesson behind it: Rotate In Place
    https://bytepatterns.com/learn/matrix-grid/rotate-in-place
    python matrix-grid/03-rotate-in-place.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/matrix-grid/rotate-square-grid

Run it:  python problems/matrix-grid/05-rotate-square-grid.py
"""


def rotate_clockwise(grid):
    n = len(grid)
    for r in range(n):
        for c in range(r + 1, n):              # above the diagonal only, once per pair
            grid[r][c], grid[c][r] = grid[c][r], grid[r][c]
    for row in grid:
        row.reverse()                          # mirror each row left to right
    return grid


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(rotate_clockwise([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
    check(rotate_clockwise([[1, 2], [3, 4]]), [[3, 1], [4, 2]])
    check(rotate_clockwise([[7]]), [[7]])
