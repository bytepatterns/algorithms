"""
Cells Draining to Both Coasts (medium) · patterns: reverse-flood-fill, multi-source-search

A height map of an island is a grid of numbers. The west coast runs along
the top and left edges, and the east coast runs along the bottom and right
edges. Rain on a cell flows to any sideways neighbour whose height is less
than or equal to the cell's own height, and a cell on an edge drains
straight into that coast. Return every cell, as [row, col] in row-major
order, from which rain can reach both coasts. The grid has between 1 and 200
rows and columns, so running a separate search from every cell is too slow.

Examples:

    Input:  heights = [[1, 2, 2, 3, 5],
                       [3, 2, 3, 4, 4],
                       [2, 4, 5, 3, 1],
                       [6, 7, 1, 4, 5],
                       [5, 1, 1, 2, 4]]
    Output: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

    Input:  heights = [[1, 2], [4, 3]]
    Output: [[0, 1], [1, 0], [1, 1]]
    Why:    the corner holding 1 is lower than both of its neighbours, so it only reaches the west coast

    Input:  heights = [[1]]
    Output: [[0, 0]]
    Why:    edge case, a single cell touches both coasts

Approach:
    Water flows from a cell to a neighbour that is no higher, so reversing
    the direction turns the question into a reachability search: starting
    from a coast, climb to any neighbour at least as high as where you
    stand. Every cell that climb reaches has a downhill path back to that
    coast. One flood fill seeded with all west-edge cells and one seeded
    with all east-edge cells each visit every cell at most once, and the
    answer is the intersection of the two visited sets. Time and space are
    both O(rows × cols).

The lesson behind it: Flood Fill
    https://bytepatterns.com/learn/matrix-grid/flood-fill
    python matrix-grid/05-flood-fill.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/matrix-grid/cells-draining-to-both-coasts

Run it:  python problems/matrix-grid/12-cells-draining-to-both-coasts.py
"""


def both_coasts(heights):
    rows, cols = len(heights), len(heights[0])

    def climb(starts):                       # every cell that drains to these edges
        seen, stack = set(starts), list(starts)
        while stack:
            r, c = stack.pop()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen
                        and heights[nr][nc] >= heights[r][c]):   # walk uphill only
                    seen.add((nr, nc))
                    stack.append((nr, nc))
        return seen

    west = climb([(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)])
    east = climb([(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)])
    return sorted([r, c] for r, c in west & east)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(both_coasts([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]), [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])
    check(both_coasts([[1, 2], [4, 3]]), [[0, 1], [1, 0], [1, 1]])
    check(both_coasts([[1]]), [[0, 0]])
