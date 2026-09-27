"""
String Basics: Strings never change — every edit builds a brand-new one.

A Python string is a fixed block of characters. Nothing edits it in place:
slicing, .upper() and + each hand back a whole new string.

So s += ch in a loop copies everything built so far, every time. An
innocent-looking loop quietly costs O(n²).

Lesson 1 of Strings, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/strings/string-basics

Run it:  python strings/01-string-basics.py
"""


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
    s = "string"
    # s[0] = "S"  ->  TypeError: strings are immutable

    out = ""
    for ch in s:                  # each += copies the whole result again
        out += ch.upper()         # O(n²) across the loop
    check_printed(out, expect="STRING")

    parts = []
    for ch in s:
        parts.append(ch.upper())  # appends are O(1)
    check_printed("".join(parts), expect="STRING — copied once, O(n)")
