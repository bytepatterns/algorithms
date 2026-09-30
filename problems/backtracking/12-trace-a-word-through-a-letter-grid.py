"""
Trace a Word Through a Letter Grid (medium) · patterns: backtracking, grid-dfs, pruning

Given a grid of letters as a list of equal-length strings and a word, decide
whether the word can be traced through the grid. A trace starts on any cell,
moves one step up, down, left or right for each next letter, and never uses
the same cell twice. Return True if some trace spells the whole word,
otherwise False.

Examples:

    Input:  board = ["ABCE", "SFCS", "ADEE"], word = "ABCCED"
    Output: True
    Why:    A B C across the top row, down to the second C, then E and D along the bottom

    Input:  board = ["ABCE", "SFCS", "ADEE"], word = "ABCB"
    Output: False
    Why:    the only B next to that C is the one already used

    Input:  board = ["A"], word = "AA"
    Output: False
    Why:    edge case, the word needs more cells than the grid has

Approach:
    Each start cell launches a depth-first search that matches one letter
    per step. A cell is overwritten with # while it is on the current path,
    so it cannot be reused, and restored when the search returns from it,
    which is the undo step that makes this backtracking rather than a plain
    flood fill: a cell that failed on one path may still be needed on
    another. The letter-count check up front rejects hopeless words without
    a single step, and the search itself stops on the first mismatch. With L
    letters in the word and R × C cells, the worst case is O(R × C × 3^L),
    since after the first step each cell has at most three unvisited
    neighbours, and the recursion uses O(L) stack.

The lesson behind it: Word Search & Pruning
    https://bytepatterns.com/learn/backtracking/word-search-and-pruning
    python backtracking/05-word-search-and-pruning.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/backtracking/trace-a-word-through-a-letter-grid

Run it:  python problems/backtracking/12-trace-a-word-through-a-letter-grid.py
"""


from collections import Counter

def can_trace(board, word):
    grid = [list(row) for row in board]
    rows, cols = len(grid), len(grid[0])
    have = Counter(ch for row in grid for ch in row)
    if any(have[ch] < n for ch, n in Counter(word).items()):
        return False                                # not enough of some letter

    def walk(r, c, i):
        if i == len(word):
            return True
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != word[i]:
            return False
        grid[r][c] = "#"                            # on the current path
        found = (walk(r + 1, c, i + 1) or walk(r - 1, c, i + 1)
                 or walk(r, c + 1, i + 1) or walk(r, c - 1, i + 1))
        grid[r][c] = word[i]                        # undo on the way back
        return found

    return any(walk(r, c, 0) for r in range(rows) for c in range(cols))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(can_trace(["ABCE", "SFCS", "ADEE"], "ABCCED"), True)
    check(can_trace(["ABCE", "SFCS", "ADEE"], "ABCB"), False)
    check(can_trace(["A"], "AA"), False)
