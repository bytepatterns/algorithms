"""
Longest Climbing Path (hard) · patterns: grid-dfs, memoization

A grid holds whole numbers. A climbing path moves one step at a time up,
down, left or right, and every step must land on a strictly larger value
than the cell it leaves. Return the number of cells in the longest climbing
path anywhere in the grid. The grid has at least one cell.

Examples:

    Input:  grid = [[9, 9, 4],
                    [6, 6, 8],
                    [2, 1, 1]]
    Output: 4
    Why:    1, 2, 6, 9 climbs up the left side

    Input:  grid = [[3, 4, 5],
                    [3, 2, 6],
                    [2, 2, 1]]
    Output: 4
    Why:    3, 4, 5, 6 runs along the top and down the right

    Input:  grid = [[7, 7],
                    [7, 7]]
    Output: 1
    Why:    edge case, equal values never climb, so every path is a single cell

Approach:
    Strictly increasing steps mean the cells and their allowed moves form a
    graph with no cycles, so the longest climb from a cell is one plus the
    longest climb from its best larger neighbour, and it never depends on
    the path that led there. That lets each cell's answer be cached the
    first time it is computed, and no visited set is needed because a climb
    can never return to a cell. Every cell is solved once and checks four
    neighbours, so time is O(rows cols); the cache is O(rows cols) and the
    recursion can go as deep as the longest climb.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/matrix-grid/longest-climbing-path

Run it:  python problems/matrix-grid/06-longest-climbing-path.py
"""


from functools import lru_cache

def longest_climb(grid):
    rows, cols = len(grid), len(grid[0])
    @lru_cache(maxsize=None)
    def best(r, c):                             # longest climb starting at (r, c)
        top = 1
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > grid[r][c]:
                top = max(top, 1 + best(nr, nc))   # strictly up, so no cycles
        return top
    return max(best(r, c) for r in range(rows) for c in range(cols))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(longest_climb([[9, 9, 4], [6, 6, 8], [2, 1, 1]]), 4)
    check(longest_climb([[3, 4, 5], [3, 2, 6], [2, 2, 1]]), 4)
    check(longest_climb([[7, 7], [7, 7]]), 1)
