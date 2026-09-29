"""
Every Way To Bracket (medium) · patterns: divide-and-conquer, memoization

A string holds non-negative integers joined by the operators +, - and *,
with no spaces. Add brackets in every way that fully decides the order in
which the operators are applied, evaluate each version, and return all the
results in sorted order. Two different bracketings that give the same value
both appear.

Examples:

    Input:  expr = "2-1-1"
    Output: [0, 2]
    Why:    (2-1)-1 is 0 and 2-(1-1) is 2

    Input:  expr = "23-45"
    Output: [-34, -14, -10, -10, 10]
    Why:    five bracketings, two of which happen to agree

    Input:  expr = "7"
    Output: [7]
    Why:    edge case, a lone number has exactly one way to be read

Approach:
    Every full bracketing has one operator that is applied last, and
    choosing it splits the expression into a left and a right part that are
    bracketed independently, so the set of results is the union over all
    split points of every left value combined with every right value. The
    recursion bottoms out at a piece with no operator, which is just its
    number. The same substring is reached through many different split
    sequences, so caching by substring stops that work from being repeated.
    The number of results grows like the Catalan numbers, which dominates
    both time and space.

The lesson behind it: Memoization
    https://bytepatterns.com/learn/recursion/memoization-intro
    python recursion/04-memoization-intro.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/recursion/every-way-to-bracket

Run it:  python problems/recursion/06-every-way-to-bracket.py
"""


from functools import lru_cache
import operator

OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul}

def all_results(expr):
    @lru_cache(maxsize=None)
    def solve(s):                               # every value s can take
        out = []
        for i, ch in enumerate(s):
            if ch in OPS:                       # this operator is applied last
                for a in solve(s[:i]):
                    for b in solve(s[i + 1:]):
                        out.append(OPS[ch](a, b))
        return tuple(out) if out else (int(s),)   # no operator: a plain number
    return sorted(solve(expr))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(all_results("2-1-1"), [0, 2])
    check(all_results("2*3-4*5"), [-34, -14, -10, -10, 10])
    check(all_results("7"), [7])
