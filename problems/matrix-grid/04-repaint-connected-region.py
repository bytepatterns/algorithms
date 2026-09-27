"""
Repaint A Connected Region (easy) · patterns: flood-fill, dfs

A grid of numbers represents the colours of an image. Given a starting cell
and a new colour, repaint the starting cell and every cell reachable from it
by steps up, down, left or right that pass only through cells of the
starting cell's original colour. Return the grid.

Examples:

    Input:  grid = [[1, 1, 1],
                    [1, 1, 0],
                    [1, 0, 1]], row = 1, col = 1, colour = 2
    Output: [[2, 2, 2],
             [2, 2, 0],
             [2, 0, 1]]
    Why:    the bottom-right 1 only touches the region diagonally, so it stays

    Input:  grid = [[5]], row = 0, col = 0, colour = 3
    Output: [[3]]

    Input:  grid = [[0, 0],
                    [0, 0]], row = 0, col = 0, colour = 0
    Output: [[0, 0],
             [0, 0]]
    Why:    edge case, repainting with the same colour changes nothing

Approach:
    This is a plain depth-first flood outward from the start, where the
    paint itself serves as the visited marker: once a cell holds the new
    colour it no longer matches the original and will not be expanded again.
    That trick only works when the two colours differ, which is why equal
    colours return early; without that check the same cells would be pushed
    forever. An explicit stack keeps deep regions from exhausting the call
    stack. Every cell in the region is painted once and pushes four
    neighbours, so time is O(rows cols) and the stack is O(rows cols) in the
    worst case.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/matrix-grid/repaint-connected-region

Run it:  python problems/matrix-grid/04-repaint-connected-region.py
"""


def repaint(grid, row, col, colour):
    old = grid[row][col]
    if old == colour:
        return grid                         # nothing to do, and no endless loop
    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == old:
            grid[r][c] = colour             # painting doubles as the visited mark
            stack += [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    return grid


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(repaint([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2), [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
    check(repaint([[5]], 0, 0, 3), [[3]])
    check(repaint([[0, 0], [0, 0]], 0, 0, 0), [[0, 0], [0, 0]])
