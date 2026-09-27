"""
N-Queens: One queen per row, and a dead row sends you straight back up.

Two queens in the same row always attack, so a solution has exactly one
queen per row. That turns the board into a sequence of decisions: which
column for row 0, then row 1, and so on.

A square is illegal if its column, its down-diagonal row - col or its
up-diagonal row + col is already claimed. Three sets answer that in constant
time. When a row has no legal square, the partial board above it is
hopeless, so the search returns and slides the previous queen along.

Lesson 4 of Backtracking, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/backtracking/n-queens

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python backtracking/04-n-queens.py
"""


def place(n, row, cols, diag, anti):
    if row == n:
        return 1                            # all rows filled: a solution
    found = 0
    for c in range(n):
        if c in cols or row - c in diag or row + c in anti:
            continue                        # square is attacked: prune
        cols.add(c); diag.add(row - c); anti.add(row + c)
        found += place(n, row + 1, cols, diag, anti)
        cols.discard(c); diag.discard(row - c); anti.discard(row + c)
    return found


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(place(4, 0, set(), set(), set()), 2)
    check(place(6, 0, set(), set(), set()), 4)
