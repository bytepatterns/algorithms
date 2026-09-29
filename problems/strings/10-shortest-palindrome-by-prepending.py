"""
Shortest Palindrome by Prepending (hard) · patterns: kmp, palindrome

Given a string s of lowercase letters, you may only add characters to its
front. Return the shortest palindrome you can build this way. The empty
string is already a palindrome, and the answer should take O(n) time.

Examples:

    Input:  s = "abacd"
    Output: "dcabacd"
    Why:    "aba" is already a palindrome at the front, so only "dc" is added

    Input:  s = "race"
    Output: "ecarace"
    Why:    only "r" works as a palindromic front, so "eca" is added

    Input:  s = ""
    Output: ""
    Why:    edge case, nothing to mirror

Approach:
    The shortest answer keeps the longest palindromic prefix of s in the
    middle and adds the reverse of everything after it to the front. A
    prefix of s is a palindrome exactly when it also appears as a suffix of
    s reversed, so the longest one is the longest border of s joined to its
    reverse. The separator stops a border from running across the join,
    which would otherwise allow a match longer than s. The border table is
    built in linear time with the usual fall-back to shorter borders on a
    mismatch. Time is O(n) and space is O(n).

The lesson behind it: Build the KMP Table
    https://bytepatterns.com/learn/strings/kmp-failure-table
    python strings/08-kmp-failure-table.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/shortest-palindrome-by-prepending

Run it:  python problems/strings/10-shortest-palindrome-by-prepending.py
"""


def shortest_palindrome(s):
    t = s + "#" + s[::-1]            # '#' never matches a letter
    border = [0] * len(t)
    for i in range(1, len(t)):
        k = border[i - 1]
        while k and t[i] != t[k]:
            k = border[k - 1]        # fall back to the border of the border
        if t[i] == t[k]:
            k += 1
        border[i] = k
    keep = border[-1]                # longest palindromic prefix of s
    return s[keep:][::-1] + s


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
    check_printed(shortest_palindrome("abacd"), expect="dcabacd")
    check_printed(shortest_palindrome("race"), expect="ecarace")
    check(shortest_palindrome(""), "")
