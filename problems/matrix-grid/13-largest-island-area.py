"""
Largest Island Area (easy) · patterns: flood-fill, dfs, grid-traversal

A map is a grid of 0s (water) and 1s (land). An island is a group of land
cells connected up, down, left or right; diagonal neighbours do not connect.
The area of an island is its number of cells. Return the area of the largest
island, or 0 if there is no land.

Examples:

    Input:  grid = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 0]]
    Output: 4
    Why:    the top-left island has 3 cells and the one on the right has 4

    Input:  grid = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    Output: 1
    Why:    diagonal cells do not join, so there are five islands of one cell

    Input:  grid = [[0, 0], [0, 0]]
    Output: 0
    Why:    edge case, no land at all

Approach:
    Every land cell belongs to exactly one island, and a flood fill from any
    of its cells visits the whole island and nothing else. The outer scan
    starts a fill only on land that has not been visited yet, and the fill
    counts cells as it pops them. Sinking a cell (setting it to 0) as soon
    as it is pushed is the visited mark, so no cell is pushed twice. An
    explicit stack keeps a large island from hitting Python's recursion
    limit. Each cell is scanned once and pushed at most once, so time is
    O(rows × cols); the stack can hold O(rows × cols) cells in the worst
    case. The function works on a copy so the caller's grid is left alone.

The lesson behind it: Number of Islands
    https://bytepatterns.com/learn/matrix-grid/number-of-islands
    python matrix-grid/04-number-of-islands.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/matrix-grid/largest-island-area

Run it:  python problems/matrix-grid/13-largest-island-area.py
"""


def largest_island(grid):
    grid = [row[:] for row in grid]               # sink cells in a copy
    rows, cols = len(grid), len(grid[0])
    best = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 1:
                continue
            grid[r][c] = 0
            stack, area = [(r, c)], 0
            while stack:
                y, x = stack.pop()
                area += 1
                for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == 1:
                        grid[ny][nx] = 0          # visited the moment it is pushed
                        stack.append((ny, nx))
            best = max(best, area)
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(largest_island([[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 0]]), 4)
    check(largest_island([[1, 0, 1], [0, 1, 0], [1, 0, 1]]), 1)
    check(largest_island([[0, 0], [0, 0]]), 0)
