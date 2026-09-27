"""
Count Queen Placements (hard) · patterns: backtracking, constraint-sets

On an n by n chessboard, place n queens so that no two of them share a row,
a column or a diagonal. Return how many different placements exist. The
board size n is at least 1.

Examples:

    Input:  n = 4
    Output: 2
    Why:    the two placements are mirror images of each other

    Input:  n = 1
    Output: 1
    Why:    a single queen on a single square attacks nothing

    Input:  n = 3
    Output: 0
    Why:    edge case, small boards can have no valid placement at all

Approach:
    Placing one queen per row turns the search into a choice of column per
    row, and three sets make every attack check constant time: one for
    columns, one for the down diagonals keyed by row minus column, and one
    for the up diagonals keyed by row plus column. A column is tried only
    when all three keys are free, which prunes most of the tree long before
    the last row. Marking before the recursive call and unmarking after it
    is the choose-explore-un-choose rhythm. The search is bounded by n
    factorial but pruning keeps it far smaller in practice; the depth is
    O(n) and the sets hold O(n) keys.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/backtracking/count-queen-placements

Run it:  python problems/backtracking/06-count-queen-placements.py
"""


def count_queens(n):
    cols, down, up = set(), set(), set()
    def place(row):
        if row == n:
            return 1                           # every row holds a queen
        total = 0
        for c in range(n):
            if c in cols or row - c in down or row + c in up:
                continue                       # this square is under attack
            cols.add(c); down.add(row - c); up.add(row + c)
            total += place(row + 1)
            cols.remove(c); down.remove(row - c); up.remove(row + c)
        return total
    return place(0)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_queens(4), 2)
    check(count_queens(1), 1)
    check(count_queens(3), 0)
    check(count_queens(8), 92)
