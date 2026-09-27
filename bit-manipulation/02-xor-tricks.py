"""
XOR Tricks: Pairs cancel out, and the loner is left standing.

XOR has two properties that do all the work: x ^ x is 0, and x ^ 0 is x. It
also ignores order.

So XOR a whole list together and every value that appears twice erases
itself. Whatever survives appeared an odd number of times — in O(n) time and
O(1) memory.

Lesson 2 of Bit Manipulation, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/bit-manipulation/xor-tricks

Run it:  python bit-manipulation/02-xor-tricks.py
"""


def single_number(nums):
    acc = 0
    for x in nums:     # x ^ x == 0, and order does not matter
        acc ^= x
    return acc         # every pair cancels; the loner survives


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
    check(single_number([4, 1, 2, 1, 2]), 4)
    check_printed(7 ^ 7, 7 ^ 0, expect="0 7")

    a, b = 3, 9
    a ^= b         # a holds the difference of the two
    b ^= a         # ...so b recovers the old a
    a ^= b         # ...and a recovers the old b
    check_printed(a, b, expect="9 3")
