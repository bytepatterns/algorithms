"""
Fraction as a Repeating Decimal (medium) · patterns: long-division, hash-map

Given an integer numerator and a non-zero integer denominator, return the
value of the fraction as a decimal string. If the digits after the point
repeat forever, wrap the repeating block in parentheses. Either number may
be negative, and the result carries a minus sign only when the value itself
is negative.

Examples:

    Input:  num = 1, den = 6
    Output: "0.1(6)"
    Why:    1/6 = 0.1666..., the 6 repeats after one digit that does not

    Input:  num = 22, den = 7
    Output: "3.(142857)"

    Input:  num = -50, den = 8
    Output: "-6.25"
    Why:    edge case, a negative value whose digits stop

Approach:
    After the whole part is written, long division is a machine whose entire
    state is the current remainder: multiply by ten, emit the quotient
    digit, keep the new remainder. There are fewer than den possible
    remainders, so either one of them becomes zero and the decimal ends, or
    one of them appears a second time and from then on the same digits come
    out in the same order. A dictionary from remainder to the index of the
    digit it produced tells exactly where the repeating block starts. Time
    and space are O(den) in the worst case, since that bounds the number of
    distinct remainders.

The lesson behind it: Modular Arithmetic
    https://bytepatterns.com/learn/math-number-theory/modular-arithmetic
    python math-number-theory/01-modular-arithmetic.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/math-number-theory/fraction-as-a-repeating-decimal

Run it:  python problems/math-number-theory/08-fraction-as-a-repeating-decimal.py
"""


def to_decimal(num, den):
    if num == 0:
        return "0"
    sign = "-" if (num < 0) != (den < 0) else ""
    num, den = abs(num), abs(den)
    whole, rem = divmod(num, den)
    digits, seen = [], {}
    while rem and rem not in seen:
        seen[rem] = len(digits)                # where this remainder started
        rem *= 10
        digits.append(str(rem // den))
        rem %= den
    frac = "".join(digits)
    if rem:                                    # a remainder came back: cycle
        i = seen[rem]
        frac = frac[:i] + "(" + frac[i:] + ")"
    return sign + str(whole) + ("." + frac if frac else "")


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
    check_printed(to_decimal(1, 6), expect="0.1(6)")
    check_printed(to_decimal(22, 7), expect="3.(142857)")
    check_printed(to_decimal(-50, 8), expect="-6.25")
    check_printed(to_decimal(4, 2), expect="2")
    check_printed(to_decimal(1, 333), expect="0.(003)")
