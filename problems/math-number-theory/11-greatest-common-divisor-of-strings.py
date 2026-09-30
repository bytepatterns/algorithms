"""
Greatest Common Divisor of Strings (easy) · patterns: gcd, string-period

A string t divides a string s when s is t written one or more times in a
row. Given two strings a and b, return the longest string that divides both
of them, or an empty string when no string does.

Examples:

    Input:  a = "ABCABC", b = "ABC"
    Output: "ABC"

    Input:  a = "ABABAB", b = "ABAB"
    Output: "AB"
    Why:    AB divides both, while ABAB does not divide ABABAB

    Input:  a = "LOOP", b = "POOL"
    Output: ""
    Why:    edge case, the strings share no repeating unit at all

Approach:
    If both strings are copies of some unit t, then a + b and b + a are the
    same number of copies of t, so they are equal; if the strings are not
    built from a common unit, the two concatenations differ somewhere, and
    that one comparison rules the case out. When they do share a unit, every
    common divisor has a length that divides both lengths, and the longest
    possible length, the greatest common divisor of the two lengths, also
    works, since a prefix of that length tiles both strings. Euclid's
    algorithm computes it in O(log n) steps, so the whole solution costs O(n
    + m) time for the concatenation check and O(n + m) space.

The lesson behind it: GCD and Euclid
    https://bytepatterns.com/learn/math-number-theory/gcd-and-euclid
    python math-number-theory/02-gcd-and-euclid.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/math-number-theory/greatest-common-divisor-of-strings

Run it:  python problems/math-number-theory/11-greatest-common-divisor-of-strings.py
"""


from math import gcd

def gcd_of_strings(a, b):
    if a + b != b + a:                 # no common building block exists
        return ""
    return a[:gcd(len(a), len(b))]    # the longest block that tiles both


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
    check_printed(gcd_of_strings("ABCABC", "ABC"), expect="ABC")
    check_printed(gcd_of_strings("ABABAB", "ABAB"), expect="AB")
    check_printed(gcd_of_strings("LOOP", "POOL"), expect="(empty string)")
