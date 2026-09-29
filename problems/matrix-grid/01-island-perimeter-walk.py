"""
Perimeter Of An Island (easy) · patterns: grid-scan, neighbour-check

A grid holds 1 for land and 0 for water, and all the land forms a single
connected island with no lakes inside it. Measure the length of the island's
coastline, counting one unit for each cell side that touches water or the
edge of the grid.

Examples:

    Input:  grid = [[0, 1, 0, 0],
                    [1, 1, 1, 0],
                    [0, 1, 0, 0],
                    [1, 1, 0, 0]]
    Output: 16

    Input:  grid = [[1, 1],
                    [1, 1]]
    Output: 8
    Why:    a solid square of four cells has eight exposed sides

    Input:  grid = [[1]]
    Output: 4
    Why:    edge case, a lone cell is exposed on every side

Approach:
    Each unit of coastline is one side of one land cell, so the perimeter
    can be summed cell by cell rather than traced as a loop. A side counts
    when the neighbour in that direction is water, or when it falls off the
    grid entirely, which is the same check with the bounds test folded in.
    That makes the whole thing a plain sweep with four probes per cell and
    no traversal state. Time is O(rows * cols), and space is O(1).

The lesson behind it: Grid Traversal
    https://bytepatterns.com/learn/matrix-grid/grid-traversal-and-neighbours
    python matrix-grid/01-grid-traversal-and-neighbours.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/matrix-grid/island-perimeter-walk

Run it:  python problems/matrix-grid/01-island-perimeter-walk.py
"""


def perimeter(g):
    rows, cols, total = len(g), len(g[0]), 0
    for r in range(rows):
        for c in range(cols):
            if g[r][c] != 1:
                continue
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                off = not (0 <= nr < rows and 0 <= nc < cols)
                if off or g[nr][nc] == 0:   # that side faces water or the edge
                    total += 1
    return total


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(perimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]), 16)
    check(perimeter([[1, 1], [1, 1]]), 8)
    check(perimeter([[1]]), 4)
