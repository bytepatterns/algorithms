"""
Look and Say Term (easy) · patterns: recursion, run-length

The look-and-say sequence starts with "1". Each later term is made by
reading the previous term aloud in runs of equal digits: "1" is one 1,
giving "11"; "11" is two 1s, giving "21"; "21" is one 2 then one 1, giving
"1211". Given n of at least 1, return the n-th term as a string.

Examples:

    Input:  n = 4
    Output: "1211"

    Input:  n = 5
    Output: "111221"
    Why:    "1211" reads as one 1, one 2, two 1s

    Input:  n = 1
    Output: "1"
    Why:    edge case, the first term is given, nothing to describe

Approach:
    The definition is already recursive: term 1 is "1", and term n is the
    description of term n minus 1. Describing a string means splitting it
    into runs of equal digits and writing each run as its length followed by
    the digit, which one pass with two indices does. The recursion is n
    levels deep, which is fine for the small n this sequence is used with,
    since the terms grow by roughly a third at every step. Time and space
    are proportional to the total length of the terms produced, dominated by
    the length of the n-th term.

The lesson behind it: Recursion Basics
    https://bytepatterns.com/learn/recursion/recursion-basics
    python recursion/01-recursion-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/recursion/look-and-say-term

Run it:  python problems/recursion/09-look-and-say-term.py
"""


def look_and_say(n):
    if n == 1:
        return "1"                             # base case
    prev, out, i = look_and_say(n - 1), [], 0
    while i < len(prev):
        j = i
        while j < len(prev) and prev[j] == prev[i]:
            j += 1                             # extend the run of prev[i]
        out.append(str(j - i) + prev[i])       # count, then digit
        i = j
    return "".join(out)


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
    check_printed(look_and_say(4), expect="1211")
    check_printed(look_and_say(5), expect="111221")
    check_printed(look_and_say(1), expect="1")
    check_printed(look_and_say(8), expect="1113213211")
