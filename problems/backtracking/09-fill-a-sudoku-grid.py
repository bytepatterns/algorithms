"""
Fill a Sudoku Grid (hard) · patterns: backtracking, constraint-sets

A 9 by 9 puzzle grid holds digits as the characters "1" to "9" and "." for
empty cells. Fill the empty cells in place so that every row, every column
and every 3 by 3 box contains each digit exactly once, and return True. If
the givens already clash or no filling exists, return False.

Examples:

    Input:  grid = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1",
                    "7...2...6", ".6....28.", "...419..5", "....8..79"]
    Output: True, grid becomes ["534678912", "672195348", "198342567", ...]

    Input:  the first row is "11......." and the rest are empty
    Output: False
    Why:    edge case, the givens already break the row rule, so no search is needed

Approach:
    This is the same place-check-undo pattern as placing queens row by row,
    with three constraint families instead of columns and diagonals. Sets of
    used digits for each row, column and box make a legality check three
    lookups, and the givens are loaded into them once, which is also where a
    clash among the givens shows up. The search fills the empty cells in
    order, trying only digits that the three sets allow, and undoes a
    placement in the grid and the sets as soon as the branch below it fails.
    The worst case is exponential in the number of empty cells, at most 9
    choices each, but the constraints prune real puzzles to a small fraction
    of that; the extra space is O(1) for a fixed 9 by 9 grid.

The lesson behind it: N-Queens
    https://bytepatterns.com/learn/backtracking/n-queens
    python backtracking/04-n-queens.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/backtracking/fill-a-sudoku-grid

Run it:  python problems/backtracking/09-fill-a-sudoku-grid.py
"""


def solve_sudoku(grid):
    rows, cols, boxes = ([set() for _ in range(9)] for _ in range(3))
    empty = []
    for r in range(9):
        for c in range(9):
            d, b = grid[r][c], r // 3 * 3 + c // 3
            if d == ".": empty.append((r, c)); continue
            if d in rows[r] or d in cols[c] or d in boxes[b]: return False
            rows[r].add(d); cols[c].add(d); boxes[b].add(d)
    def fill(i):
        if i == len(empty): return True
        r, c = empty[i]; b = r // 3 * 3 + c // 3
        for d in "123456789":
            if d in rows[r] or d in cols[c] or d in boxes[b]: continue
            grid[r][c] = d; rows[r].add(d); cols[c].add(d); boxes[b].add(d)
            if fill(i + 1): return True
            grid[r][c] = "."; rows[r].remove(d); cols[c].remove(d); boxes[b].remove(d)
        return False                           # nothing fits: undo above
    return fill(0)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import re

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


def _same(printed, expected):
    """Printed text vs the lesson's comment, which may add a note after it."""
    printed, expected = printed.strip(), expected.strip()
    wants = [expected] + [expected.rsplit(s, 1)[1].strip() for s in (" -> ", " = ") if s in expected]
    for want in wants + [w[1:] for w in wants if w.startswith("~")]:
        rest = want[len(printed):] if want.startswith(printed) else None
        if rest == "" or (rest and re.match(r"[\s,;:]+([A-Za-z]|\u2014|\u2013|-(?!\d)|\u2192|<-|\([A-Za-z]|#)", rest)):
            return True
    return False


def check_printed(*values, expect, sep=" ", end="\n"):
    """print(*values), then assert the line reads the way the lesson's comment says."""
    print(*values, sep=sep, end=end)
    forms = [sep.join(map(str, values))]
    if len(values) == 1 and isinstance(values[0], str):
        forms += [repr(values[0]), '"%s"' % values[0]] + (["(empty string)"] if not values[0] else [])
    if len(values) > 1 and isinstance(values[0], str):  # a leading label
        forms.append(sep.join(map(str, values[1:])))
    assert any(_same(f, expect) for f in forms), f"expected {expect!r}, got {forms[0]!r}"


if __name__ == "__main__":
    g = [list(r) for r in ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1",
                           "7...2...6", ".6....28.", "...419..5", "....8..79"]]
    check_printed(solve_sudoku(g), "".join(g[0]), "".join(g[8]), expect="True 534678912 345286179")
    bad = [list("11......."), *[list(".........") for _ in range(8)]]
    check(solve_sudoku(bad), False)
