"""
Balanced Bracket Strings (medium) · patterns: backtracking, pruning

Given a number of pairs n, return every string of n opening and n closing
round brackets that is balanced: reading left to right, the closers seen so
far never outnumber the openers seen so far. Return the strings in sorted
order, where an opening bracket sorts before a closing one.

Examples:

    Input:  n = 3
    Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

    Input:  n = 1
    Output: ["()"]

    Input:  n = 0
    Output: [""]
    Why:    edge case, zero pairs still form one balanced string, the empty one

Approach:
    The two counters are the whole state: an opener is legal while any
    remain, and a closer is legal only when it has an unmatched opener to
    close. Because an illegal character is never appended, every leaf the
    recursion reaches is a valid answer, so no work is wasted on dead
    prefixes. Branching on the opener before the closer produces the strings
    in sorted order for free. The number of results is the n-th Catalan
    number, roughly 4 to the n divided by n to the 1.5, and each costs O(n)
    to build, which bounds the time; the depth is 2n.

The lesson behind it: Backtracking
    https://bytepatterns.com/learn/recursion/backtracking-intro
    python recursion/05-backtracking-intro.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/backtracking/balanced-bracket-strings

Run it:  python problems/backtracking/05-balanced-bracket-strings.py
"""


def balanced(n):
    out = []
    def build(path, opened, closed):
        if len(path) == 2 * n:                 # every bracket is placed
            out.append("".join(path))
            return
        if opened < n:                         # an opener is still available
            path.append("("); build(path, opened + 1, closed); path.pop()
        if closed < opened:                    # a closer has something to match
            path.append(")"); build(path, opened, closed + 1); path.pop()
    build([], 0, 0)
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(balanced(3), ['((()))', '(()())', '(())()', '()(())', '()()()'])
    check(balanced(1), ['()'])
    check(balanced(0), [''])
    check(len(balanced(5)), 42)
