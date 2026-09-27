"""
Search A Sorted Grid (medium) · patterns: staircase-walk, grid-search

A grid has every row sorted increasing from left to right, and every column
sorted increasing from top to bottom. Find a target value and report its
position as a row and column pair, or report that it is absent. Scanning
every cell is too slow for a large grid.

Examples:

    Input:  grid = [[1, 4, 7, 11],
                    [2, 5, 8, 12],
                    [3, 6, 9, 16]], target = 5
    Output: (1, 1)

    Input:  same grid, target = 10
    Output: None
    Why:    10 sits between 9 and 11 but appears nowhere

    Input:  grid = [[1]], target = 1
    Output: (0, 0)
    Why:    edge case, a single cell grid

Approach:
    The top-right cell is the largest in its row and the smallest in its
    column, so a single comparison against it always eliminates an entire
    line. Too large means the whole column is too large and the column is
    dropped, too small means the whole row is too small and the row is
    dropped, which is why the walk never has to backtrack. Each step removes
    one row or one column, so the search visits at most rows plus columns
    cells. Time is O(rows + cols), and space is O(1).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/matrix-grid/staircase-grid-search

Run it:  python problems/matrix-grid/03-staircase-grid-search.py
"""


def find_value(g, target):
    r, c = 0, len(g[0]) - 1          # start at the top-right corner
    while r < len(g) and c >= 0:
        v = g[r][c]
        if v == target:
            return (r, c)
        if v > target:
            c -= 1                   # this column is all too large
        else:
            r += 1                   # this row is all too small
    return None


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    grid = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]]
    check(find_value(grid, 5), (1, 1))
    check(find_value(grid, 16), (2, 3))
    check(find_value(grid, 10), None)
    check(find_value([[1]], 1), (0, 0))
