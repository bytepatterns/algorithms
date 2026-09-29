"""
Minimum Window Cover (hard) · patterns: sliding-window, hash-map

Given a text and a set of required characters, find the shortest contiguous
stretch of the text that contains every required character, counting
duplicates. A requirement that lists the same character twice needs two
copies inside the stretch. Return the empty text when no stretch qualifies,
and the earliest one when several tie for shortest.

Examples:

    Input:  text = "ADOBECODEBANC", need = "ABC"
    Output: "BANC"
    Why:    shorter than ADOBEC, which also covers the requirement

    Input:  text = "aa", need = "aa"
    Output: "aa"
    Why:    duplicates in the requirement must each be matched

    Input:  text = "a", need = "aa"
    Output: ""
    Why:    edge case, the text cannot supply a second copy

Approach:
    A window slides forward while a tally holds how many copies of each
    character it still owes; a character in surplus drops below zero, which
    is how the tally distinguishes spares from needs. A single counter of
    outstanding copies makes covered a constant-time test, so the window
    shrinks from the left as soon as it is valid, recording the best stretch
    found. Each character enters and leaves the window once. Time is O(n +
    m), and space is O(k) for the distinct required characters.

The lesson behind it: Sliding Window
    https://bytepatterns.com/learn/arrays/sliding-window
    python arrays/03-sliding-window.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/minimum-window-cover

Run it:  python problems/strings/05-minimum-window-cover.py
"""


from collections import Counter
def minimum_cover(text, need):
    if not need:
        return ""
    owed = Counter(need)             # copies of each character still required
    missing = len(need)              # total outstanding copies
    best = (len(text) + 1, 0, 0)     # width, start, end of the best window
    left = 0
    for right, ch in enumerate(text):
        if owed[ch] > 0:             # this copy was genuinely needed
            missing -= 1
        owed[ch] -= 1
        while missing == 0:          # the window covers the requirement
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right + 1)
            owed[text[left]] += 1    # give the departing character back
            if owed[text[left]] > 0:
                missing += 1
            left += 1
    return text[best[1]:best[2]]


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
    check_printed(minimum_cover("ADOBECODEBANC", "ABC"), expect="BANC")
    check_printed(minimum_cover("aa", "aa"), expect="aa")
    check_printed(minimum_cover("a", "aa"), expect="")
