"""
Counting Set Bits: Clear the lowest 1 and count how often you can.

Subtracting 1 from a number flips its lowest 1 to 0 and turns every 0 below
it into 1. AND the two values together and that tail is wiped out — one set
bit gone, the rest untouched.

Repeat until nothing is left. The loop runs once per 1, not once per bit.

Lesson 3 of Bit Manipulation, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/bit-manipulation/counting-set-bits

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python bit-manipulation/03-counting-set-bits.py
"""


def popcount(x):
    count = 0
    while x:
        x &= x - 1          # wipes the lowest set bit, nothing else
        count += 1
    return count            # one pass per 1, not per bit


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
    check(popcount(44), 3)  # 0b101100 has three 1s
    check(popcount(255), 8)
    check_printed(bin(44), bin(43), expect="0b101100 0b101011 -> the tail flipped")
    check_printed(bin(44 & 43), expect="0b101000 -> lowest 1 cleared")
