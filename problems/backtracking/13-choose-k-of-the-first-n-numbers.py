"""
Choose K of the First N Numbers (easy) · patterns: backtracking, combinations, pruning

Given two integers n and k, return every way to choose k different numbers
from 1 to n. Order inside a choice does not matter, so write each choice in
ascending order, and return the choices in ascending lexicographic order.

Examples:

    Input:  n = 4, k = 2
    Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    Why:    4 choose 2 is 6

    Input:  n = 3, k = 3
    Output: [[1, 2, 3]]
    Why:    there is only one way to take everything

    Input:  n = 2, k = 0
    Output: [[]]
    Why:    edge case, choosing nothing is exactly one choice, the empty one

Approach:
    This is the subsets decision tree cut off at depth k. Each level decides
    the next number of the choice, and passing x + 1 as the next start
    guarantees every choice is built in ascending order, so each set of
    numbers is produced exactly once and the output comes out in
    lexicographic order for free. After the recursive call returns, the
    number is popped, which puts the shared pick list back the way the loop
    found it. The upper bound on the loop is the pruning step: a branch that
    cannot possibly collect enough numbers is never entered. There are C(n,
    k) choices and each costs O(k) to copy, so time is O(k × C(n, k)) and
    the recursion depth is k.

The lesson behind it: Subsets
    https://bytepatterns.com/learn/backtracking/subsets
    python backtracking/02-subsets.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/backtracking/choose-k-of-the-first-n-numbers

Run it:  python problems/backtracking/13-choose-k-of-the-first-n-numbers.py
"""


def choose(n, k):
    out, pick = [], []

    def build(start):
        if len(pick) == k:
            out.append(pick[:])                      # record a copy, pick keeps changing
            return
        need = k - len(pick)
        for x in range(start, n - need + 2):         # leave room for the numbers still needed
            pick.append(x)
            build(x + 1)
            pick.pop()                               # undo before trying the next x

    build(1)
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(choose(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
    check(choose(3, 3), [[1, 2, 3]])
    check(choose(2, 0), [[]])
