"""
Next Generation of Cells (medium) · patterns: eight-neighbours, in-place-encoding

A simulation keeps a grid of cells, each 1 for alive or 0 for dead. Every
cell looks at its eight neighbours (sideways and diagonal) and all cells
change at the same moment: a live cell with two or three live neighbours
stays alive, a dead cell with exactly three live neighbours comes alive, and
every other cell is dead in the next step. Update the grid in place to the
next step and return it. The grid has between 1 and 25 rows and columns, and
the update should use O(1) extra memory beyond the grid itself.

Examples:

    Input:  board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Output: [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    Input:  board = [[1, 1], [1, 0]]
    Output: [[1, 1], [1, 1]]
    Why:    the dead corner has exactly three live neighbours, and each live cell has two

    Input:  board = [[1]]
    Output: [[0]]
    Why:    edge case, a lone live cell has no neighbours and dies

Approach:
    All cells must change at once, so while the grid is being scanned every
    neighbour count has to see the old states. Instead of copying the grid,
    each cell stores two bits: bit 0 is the state now and bit 1 is the state
    in the next step. The first pass counts live neighbours by reading only
    bit 0 and sets bit 1 when the cell survives or is born, which never
    disturbs anything a later cell reads. A second pass shifts every value
    right by one, dropping the old state and keeping the new one. Time is
    O(rows × cols), with eight neighbour checks per cell, and extra space is
    O(1).

The lesson behind it: Grid Traversal
    https://bytepatterns.com/learn/matrix-grid/grid-traversal-and-neighbours
    python matrix-grid/01-grid-traversal-and-neighbours.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/matrix-grid/next-generation-of-cells

Run it:  python problems/matrix-grid/11-next-generation-of-cells.py
"""


def next_generation(board):
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            live = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc
                    if (dr or dc) and 0 <= nr < rows and 0 <= nc < cols:
                        live += board[nr][nc] & 1       # bit 0 is today's state
            if live == 3 or (live == 2 and board[r][c] & 1):
                board[r][c] |= 2                       # bit 1 is tomorrow's state
    for r in range(rows):
        for c in range(cols):
            board[r][c] >>= 1
    return board


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(next_generation([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]), [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])
    check(next_generation([[1, 1], [1, 0]]), [[1, 1], [1, 1]])
    check(next_generation([[1]]), [[0]])
