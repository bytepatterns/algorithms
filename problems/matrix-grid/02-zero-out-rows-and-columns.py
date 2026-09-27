"""
Zero Out Rows And Columns (medium) · patterns: grid-marking, in-place

Given a grid of whole numbers, every cell holding a zero must clear its
entire row and its entire column. Rewrite the grid in place, using the
values as they were before any clearing began.

Examples:

    Input:  grid = [[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]]
    Output: [[1, 0, 1],
             [0, 0, 0],
             [1, 0, 1]]

    Input:  grid = [[0, 1, 2, 0],
                    [3, 4, 5, 2],
                    [1, 3, 1, 5]]
    Output: [[0, 0, 0, 0],
             [0, 4, 5, 0],
             [0, 3, 1, 0]]

    Input:  grid = [[1, 2],
                    [3, 4]]
    Output: [[1, 2],
             [3, 4]]
    Why:    edge case, no zeros means nothing changes

Approach:
    The only real difficulty is that writing a zero creates evidence
    indistinguishable from the original input, so the algorithm splits into
    a read phase and a write phase. The first pass collects the doomed row
    indexes and column indexes, and the second pass clears any cell that
    matches either set. Both passes touch each cell once, so time is O(rows
    * cols), and the two sets cost O(rows + cols) extra space. Trading that
    for the marker-row trick would bring space down to O(1) at the cost of a
    much fussier implementation.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/matrix-grid/zero-out-rows-and-columns

Run it:  python problems/matrix-grid/02-zero-out-rows-and-columns.py
"""


def zero_out(g):
    rows_to_clear = {r for r, row in enumerate(g) if 0 in row}
    cols_to_clear = {c for row in g for c, v in enumerate(row) if v == 0}
    for r, row in enumerate(g):            # nothing is written until now
        for c in range(len(row)):
            if r in rows_to_clear or c in cols_to_clear:
                row[c] = 0
    return g


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(zero_out([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
    check(zero_out([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]), [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
    check(zero_out([[1, 2], [3, 4]]), [[1, 2], [3, 4]])
