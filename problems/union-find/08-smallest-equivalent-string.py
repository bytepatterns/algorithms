"""
Smallest Equivalent String (medium) · patterns: union-find, strings

Two strings a and b of equal length declare letter equivalences: a[i] is
equivalent to b[i] for every i. Equivalence is reflexive, symmetric and
transitive, so it groups the lowercase letters into classes. Given a third
string text, replace each of its letters with the smallest letter of its
class and return the alphabetically smallest string this produces.

Examples:

    Input:  a = "parker", b = "morris", text = "parser"
    Output: "makkek"
    Why:    the classes include {m, p}, {a, o}, {k, r, s} and {e, i}

    Input:  a = "hello", b = "world", text = "hold"
    Output: "hdld"
    Why:    o shares a class with e and d, so it becomes d; h, l and d already lead theirs

    Input:  a = "", b = "", text = "abc"
    Output: "abc"
    Why:    edge case, with no equivalences every letter stands alone

Approach:
    Every pair merges two classes of letters, and transitivity is exactly
    what a disjoint-set structure provides for free. The twist is choosing
    the representative: if every merge hangs the root with the larger letter
    under the root with the smaller letter, each root is always the smallest
    letter of its class. Replacing each letter of text by its root therefore
    gives the smallest letter at every position independently, which is the
    smallest possible string overall. Path halving keeps the finds short.
    With an alphabet of 26 letters, time is O(n plus m) for the pair and
    text lengths, and space is O(1).

The lesson behind it: Path Compression
    https://bytepatterns.com/learn/union-find/path-compression
    python union-find/02-path-compression.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/union-find/smallest-equivalent-string

Run it:  python problems/union-find/08-smallest-equivalent-string.py
"""


def smallest_equivalent(a, b, text):
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]    # path halving
            x = parent[x]
        return x
    for x, y in zip(a, b):
        rx, ry = sorted((find(x), find(y)))
        parent[ry] = rx                      # the smaller letter stays root
    return "".join(find(ch) for ch in text)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import re


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
    check_printed(smallest_equivalent("parker", "morris", "parser"), expect="makkek")
    check_printed(smallest_equivalent("hello", "world", "hold"), expect="hdld")
    check_printed(smallest_equivalent("", "", "abc"), expect="abc")
    check_printed(smallest_equivalent("leetcode", "programs", "sourcecode"), expect="aauaaaaada")
