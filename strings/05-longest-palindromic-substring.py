"""
Longest Palindromic Substring: Stand on every centre and push outwards.

Every palindrome has a centre. So try all of them: each character is an odd
centre, and each gap between neighbours is an even centre.

From a centre, compare outwards while the two sides match. The moment they
differ, that centre is finished — keep the longest stretch you collected.

Lesson 5 of Strings, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/strings/longest-palindromic-substring

Run it:  python strings/05-longest-palindromic-substring.py
"""


def longest_pal(s):
    best = ""
    def grow(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        return s[left + 1:right]          # last stretch that matched
    for i in range(len(s)):
        for cand in (grow(i, i), grow(i, i + 1)):   # odd and even centres
            if len(cand) > len(best):
                best = cand
    return best


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
    check_printed(longest_pal("babad"), expect="bab")
    check_printed(longest_pal("cbbd"), expect="bb")
