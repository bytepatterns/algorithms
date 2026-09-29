"""
Reverse the Word Order (easy) · patterns: two-pointers, word-split

A sentence holds words separated by one or more spaces, and it may also
start or end with spaces. Return a new string with the words in reverse
order, joined by exactly one space and with no spaces at either end. A word
is any run of characters that are not spaces, and the letters inside a word
keep their order.

Examples:

    Input:  s = "  the sky   is blue "
    Output: "blue is sky the"
    Why:    extra spaces disappear and the words swap places

    Input:  s = "one"
    Output: "one"
    Why:    a single word has nothing to swap with

    Input:  s = "    "
    Output: ""
    Why:    edge case, only spaces means no words at all

Approach:
    Scanning from the right meets the last word first, so collecting words
    in the order they are found already produces the reversed sentence.
    Skipping runs of spaces before each word discards the extra spacing,
    including spaces at both ends. The letters of each word are sliced out
    as a block, so they never change order. In everyday Python, joining the
    reversed result of split gives the same answer in one line. Time is O(n)
    and space is O(n) for the output.

The lesson behind it: Reverse Words
    https://bytepatterns.com/learn/strings/reverse-words
    python strings/03-reverse-words.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/reverse-the-word-order

Run it:  python problems/strings/09-reverse-the-word-order.py
"""


def reverse_words(s):
    words, i = [], len(s) - 1
    while i >= 0:
        while i >= 0 and s[i] == " ":
            i -= 1                   # skip the gap before the next word
        end = i
        while i >= 0 and s[i] != " ":
            i -= 1                   # walk to the start of that word
        if end > i:
            words.append(s[i + 1:end + 1])
    return " ".join(words)


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
    check_printed(reverse_words("  the sky   is blue "), expect="blue is sky the")
    check_printed(reverse_words("one"), expect="one")
    check(reverse_words("    "), "")
