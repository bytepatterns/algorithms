"""
Spiral Grid Walk (medium) · patterns: matrix-traversal, boundary-shrinking

Read every cell of a rectangular grid in a single inward spiral: across the
top row, down the right column, back along the bottom row, up the left
column, then repeat on whatever rectangle is left. Return the values in the
order they are visited. The grid may have any width and height, including a
single row or a single column.

Examples:

    Input:  [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    Input:  [[1, 2],
             [3, 4],
             [5, 6]]
    Output: [1, 2, 4, 6, 5, 3]
    Why:    a tall grid spirals just the same

    Input:  [[7]]
    Output: [7]
    Why:    edge case, a single cell is a complete spiral on its own

Approach:
    The unread region is always a rectangle, so four boundaries describe it
    completely and each finished side moves one boundary inward. Walking
    top, right, bottom and left in that order while shrinking after each
    side reproduces the spiral without any visited marks. The two guards
    before the bottom row and the left column matter only at the very end,
    when the rectangle has collapsed to a single row or column that would
    otherwise be read twice. Time is O(rows times cols) since each cell is
    read once, and space is O(1) beyond the output.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/spiral-grid-walk

Run it:  python problems/arrays/08-spiral-grid-walk.py
"""


def spiral_walk(grid):
    if not grid or not grid[0]:
        return []
    top, bottom, left, right = 0, len(grid) - 1, 0, len(grid[0]) - 1
    out = []
    while top <= bottom and left <= right:
        for c in range(left, right + 1): out.append(grid[top][c])
        top += 1
        for r in range(top, bottom + 1): out.append(grid[r][right])
        right -= 1
        if top <= bottom:            # a flat leftover row must not repeat
            for c in range(right, left - 1, -1): out.append(grid[bottom][c])
            bottom -= 1
        if left <= right:            # a thin leftover column must not repeat
            for r in range(bottom, top - 1, -1): out.append(grid[r][left])
            left += 1
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(spiral_walk([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])
    check(spiral_walk([[1, 2], [3, 4], [5, 6]]), [1, 2, 4, 6, 5, 3])
    check(spiral_walk([[7]]), [7])
