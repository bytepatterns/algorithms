"""
Rotate In Place: Mirror the diagonal, then flip each row.

A quarter turn clockwise sends row 0 up the right-hand edge. Getting there
directly means juggling four cells at once.

Do it in two easy moves instead. Transpose — swap grid[r][c] with grid[c][r]
— and rows become columns. Then reverse each row, and those columns end up
on the correct side. No second grid, no index gymnastics.

Lesson 3 of Matrix & Grid, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/matrix-grid/rotate-in-place

Run it:  python matrix-grid/03-rotate-in-place.py
"""


def rotate(g):
    n = len(g)
    for r in range(n):
        for c in range(r + 1, n):      # upper triangle only, or you undo it
            g[r][c], g[c][r] = g[c][r], g[r][c]
    for row in g:
        row.reverse()                  # mirror each row left to right
    return g


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(rotate([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
