"""
Number of Islands: Count a blob once, then erase it so it cannot count twice.

Sweep the grid row by row. The first land cell you meet belongs to an island
nobody has counted, so add one to the total.

Then flood it: visit every connected land cell and mark it, with a queue or
plain recursion. When the flood finishes the island is gone from the board,
and the sweep carries on past cells it can safely ignore.

Lesson 4 of Matrix & Grid, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/matrix-grid/number-of-islands

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python matrix-grid/04-number-of-islands.py
"""


def count_islands(g):
    rows, cols, total = len(g), len(g[0]), 0
    def sink(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or g[r][c] != 1:
            return                                   # off-grid or water
        g[r][c] = 0                                  # erase as you go
        for n in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            sink(*n)
    for r in range(rows):
        for c in range(cols):
            if g[r][c] == 1:
                total += 1                           # a blob nobody has seen
                sink(r, c)
    return total


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_islands([[1, 1, 0, 0, 1],
                         [1, 0, 0, 1, 1],
                         [0, 0, 1, 0, 0],
                         [0, 0, 1, 0, 0]]), 3)
