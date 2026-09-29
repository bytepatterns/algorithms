"""
Longest Shared Prefix (easy) · patterns: column-scan, string-comparison

Given a collection of words, find the longest opening run of characters that
every word begins with. The run must start at the first character of each
word, so a match that appears later in a word does not count. Return the
empty text when the words share no opening character.

Examples:

    Input:  words = ["flower", "flow", "flight"]
    Output: "fl"
    Why:    the third word breaks the agreement at the third character

    Input:  words = ["dog", "racecar"]
    Output: ""
    Why:    the words disagree immediately

    Input:  words = []
    Output: ""
    Why:    edge case, there are no words to compare

Approach:
    The answer can never exceed the first word, so that word serves as a
    yardstick and the search is over its positions. Scanning column by
    column stops at the first position where any word is too short or
    disagrees, which is exactly where the shared prefix ends. Comparing all
    words at each column, rather than word against word, means the scan
    stops as early as possible. Time is O(total characters) in the worst
    case, and space is O(1) beyond the returned slice.

The lesson behind it: String Basics
    https://bytepatterns.com/learn/strings/string-basics
    python strings/01-string-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/longest-shared-prefix

Run it:  python problems/strings/01-longest-shared-prefix.py
"""


def longest_shared_prefix(words):
    if not words:
        return ""
    for i, ch in enumerate(words[0]):    # walk the yardstick word column by column
        for word in words[1:]:
            if i >= len(word) or word[i] != ch:
                return words[0][:i]      # this column breaks the agreement
    return words[0]                      # every column survived the check


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
    check_printed(longest_shared_prefix(["flower", "flow", "flight"]), expect="fl")
    check_printed(longest_shared_prefix(["dog", "racecar"]), expect="")
    check_printed(longest_shared_prefix([]), expect="")
