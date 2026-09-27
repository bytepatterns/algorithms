"""
Grid Traversal: Row first, column second, and always check the edge.

A grid is a list of rows, so grid[r][c] reads row r, column c. Row first,
always.

Neighbours are offsets added to that pair: four for edge-sharing, eight if
diagonals count. Each one needs the same guard, 0 <= r < rows and 0 <= c <
cols, because Python answers a negative index with the far side of the grid
instead of an error.

Lesson 1 of Matrix & Grid, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/matrix-grid/grid-traversal-and-neighbours

Run it:  python matrix-grid/01-grid-traversal-and-neighbours.py
"""


grid = [[0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11]]
rows, cols = len(grid), len(grid[0])
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # up, down, left, right

def neighbours(r, c):
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:   # the guard, every time
            yield grid[nr][nc]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(list(neighbours(1, 1)), [1, 9, 4, 6])
    check(list(neighbours(0, 0)), [4, 1])  # two offsets fell off the grid
