"""
Smallest Repeating Unit (medium) · patterns: kmp, string-period

Given a non-empty string s, return the shortest string u such that s is u
written a whole number of times in a row. If no shorter unit works, the
answer is s itself. The answer should take O(n) time.

Examples:

    Input:  s = "xyzxyzxyz"
    Output: "xyz"
    Why:    three copies of "xyz"

    Input:  s = "abaab"
    Output: "abaab"
    Why:    a shift of 3 lines "ab" up with itself, but 3 does not divide 5

    Input:  s = "q"
    Output: "q"
    Why:    edge case, a single letter is its own unit

Approach:
    A string is its first p characters repeated exactly when p divides n and
    s lines up with itself after a shift of p, and the shifts that line up
    correspond to borders, prefixes that are also suffixes. The longest
    border b gives the smallest such shift, p = n - b. When p divides n that
    prefix is the unit; when it does not, the periodicity lemma rules out
    every longer shift that divides n as well, so s is its own unit. The
    failure table takes linear time thanks to the fall-back to shorter
    borders on a mismatch. Time is O(n) and space is O(n).

The lesson behind it: String Matching Intuition
    https://bytepatterns.com/learn/strings/string-matching-intuition
    python strings/07-string-matching-intuition.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/smallest-repeating-unit

Run it:  python problems/strings/12-smallest-repeating-unit.py
"""


def smallest_unit(s):
    border = [0] * len(s)
    for i in range(1, len(s)):
        k = border[i - 1]
        while k and s[i] != s[k]:
            k = border[k - 1]          # fall back to a shorter border
        if s[i] == s[k]:
            k += 1
        border[i] = k
    p = len(s) - border[-1]            # the smallest shift that lines s up with itself
    return s[:p] if len(s) % p == 0 else s


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
    check_printed(smallest_unit("xyzxyzxyz"), expect="xyz")
    check_printed(smallest_unit("abaab"), expect="abaab")
    check_printed(smallest_unit("q"), expect="q")
