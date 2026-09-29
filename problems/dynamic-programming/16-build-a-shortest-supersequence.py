"""
Build a Shortest Supersequence (hard) · patterns: string-dp, subsequence-dp

Given two strings a and b, return a shortest string that contains both of
them as subsequences, meaning each can be read from it left to right by
skipping some characters. Several strings may share the shortest length; any
one of them is accepted, and the examples show one. Either input may be
empty.

Examples:

    Input:  a = "tile", b = "style"
    Output: "stiyle"
    Why:    length 6 = 4 + 5 - 3, since "tle" is shared and written once

    Input:  a = "abac", b = "cab"
    Output: "cabac"
    Why:    "ab" is shared, so 4 + 3 - 2 = 5 characters are enough

    Input:  a = "", b = "xyz"
    Output: "xyz"
    Why:    edge case, only b has to fit

Approach:
    A supersequence that shares a common subsequence has length len(a) +
    len(b) minus the shared part, so the shortest one is built around a
    longest common subsequence. Cell i, j of the table holds the longest
    common subsequence length of a from i and b from j, which makes a
    forward walk possible. At each step the walk follows the cell that
    produced the current value: a match is written once, otherwise the
    character on the side that keeps the larger value is written and that
    side advances. Every character is written exactly once except the shared
    ones, which gives the optimal length. Time and space are both O(len(a) ×
    len(b)).

The lesson behind it: Reading the Answer Back
    https://bytepatterns.com/learn/dynamic-programming/reading-the-answer-back
    python dynamic-programming/19-reading-the-answer-back.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/build-a-shortest-supersequence

Run it:  python problems/dynamic-programming/16-build-a-shortest-supersequence.py
"""


def shortest_super(a, b):
    m, n = len(a), len(b)
    L = [[0] * (n + 1) for _ in range(m + 1)]   # LCS of a[i:] and b[j:]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            L[i][j] = L[i + 1][j + 1] + 1 if a[i] == b[j] else max(L[i + 1][j], L[i][j + 1])
    out, i, j = [], 0, 0
    while i < m and j < n:           # read the answer back from the table
        if a[i] == b[j]:
            out.append(a[i]); i += 1; j += 1        # shared: written once
        elif L[i + 1][j] >= L[i][j + 1]:
            out.append(a[i]); i += 1                # a's character goes first
        else:
            out.append(b[j]); j += 1
    return "".join(out) + a[i:] + b[j:]            # one side may have leftovers


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
    check_printed(shortest_super("tile", "style"), expect="stiyle")
    check_printed(shortest_super("abac", "cab"), expect="cabac")
    check_printed(shortest_super("", "xyz"), expect="xyz")
