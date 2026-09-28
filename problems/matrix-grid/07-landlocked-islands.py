"""
Landlocked Islands (medium) · patterns: flood-fill, grid-traversal

A map is a grid of 1s for land and 0s for water, and an island is a group of
land cells joined up, down, left or right. Count the islands that are
completely surrounded by water inside the map, meaning no cell of the island
lies in the first or last row or column. Islands that touch the edge might
continue off the map, so they do not count. The grid may be empty.

Examples:

    Input:  grid = [[1, 1, 0, 0, 0],
                    [1, 0, 0, 1, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1]]
    Output: 1
    Why:    only the three cells in the middle stay clear of the edge

    Input:  grid = [[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]]
    Output: 1
    Why:    a single inland cell is an island

    Input:  grid = [[1]]
    Output: 0
    Why:    edge case, the only cell lies on the edge

Approach:
    Every island is explored once with a stack-based flood fill that starts
    at its first unvisited cell and marks cells as seen so none is walked
    twice. During that walk a single flag records whether any cell lies on
    the border, which is all that decides if the island counts. An iterative
    stack avoids deep recursion on large islands. Time is O(rows times cols)
    because each cell is visited a constant number of times, and space is
    O(rows times cols) for the seen set.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/matrix-grid/landlocked-islands

Run it:  python problems/matrix-grid/07-landlocked-islands.py
"""


def landlocked_islands(grid):
    rows, cols = len(grid), len(grid[0]) if grid else 0
    seen, count = set(), 0
    for r0 in range(rows):
        for c0 in range(cols):
            if grid[r0][c0] != 1 or (r0, c0) in seen: continue
            seen.add((r0, c0))
            stack, inland = [(r0, c0)], True
            while stack:                                # walk one whole island
                r, c = stack.pop()
                if r in (0, rows - 1) or c in (0, cols - 1): inland = False
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in seen:
                        seen.add((nr, nc)); stack.append((nr, nc))
            count += inland
    return count


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(landlocked_islands([[1, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1]]), 1)
    check(landlocked_islands([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 1)
    check(landlocked_islands([[1]]), 0)
