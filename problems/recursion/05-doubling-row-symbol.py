"""
Symbol In A Doubling Row (medium) · patterns: recursion, halving

Row 1 is the single symbol 0. Each later row is made from the one above by
replacing every 0 with 01 and every 1 with 10, so row n has 2 to the n minus
1 symbols. Given a row number n and a position k counted from 1, return the
symbol at that position. Row 30 has over half a billion symbols, so building
rows is not an option.

Examples:

    Input:  n = 4, k = 5
    Output: 1
    Why:    the rows are 0, 01, 0110, 01101001

    Input:  n = 2, k = 2
    Output: 1

    Input:  n = 1, k = 1
    Output: 0
    Why:    edge case, the seed row itself

Approach:
    Each symbol in row n is one of the two children of a symbol in row n
    minus 1: position k comes from position (k + 1) // 2, and an odd k is
    the left child, which copies its parent, while an even k is the right
    child, which flips it. So the question for row n reduces to the same
    question one row up with the position halved, until row 1 answers 0.
    Only one call is made per row, so time and stack depth are both O(n),
    and nothing close to the full row is ever built.

The lesson behind it: Recursion Basics
    https://bytepatterns.com/learn/recursion/recursion-basics
    python recursion/01-recursion-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/recursion/doubling-row-symbol

Run it:  python problems/recursion/05-doubling-row-symbol.py
"""


def symbol(n, k):
    if n == 1:
        return 0                              # the seed row is a single 0
    parent = symbol(n - 1, (k + 1) // 2)      # the symbol that produced position k
    return parent if k % 2 == 1 else 1 - parent   # left child copies, right flips


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(symbol(4, 5), 1)
    check(symbol(2, 2), 1)
    check(symbol(1, 1), 0)
    check(symbol(30, 2 ** 29), 1)
