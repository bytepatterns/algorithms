"""
Binary and Bitwise Ops: Every integer is a row of switches you can address.

Bitwise operators work lane by lane, with no carries between lanes. & keeps
a 1 only where both sides have one, | where either does, ^ where they
differ.

~ flips every lane. Shifts slide the whole row: << doubles, >> halves.

Lesson 1 of Bit Manipulation, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/bit-manipulation/binary-and-bitwise-ops

Run it:  python bit-manipulation/01-binary-and-bitwise-ops.py
"""


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
    a, b = 12, 10           # 0b1100 and 0b1010
    check_printed(bin(a), bin(b), expect="0b1100 0b1010")
    check(a & b, 8)  # 1 only where both are 1
    check(a | b, 14)  # 1 where either is 1
    check(a ^ b, 6)  # 1 only where they differ
    check(~a, -13)  # flips every bit, sign included
    check(a << 1, 24)  # shifting left doubles
    check(a >> 2, 3)  # shifting right halves, twice
