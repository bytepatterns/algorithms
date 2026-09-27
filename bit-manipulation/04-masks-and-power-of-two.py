"""
Masks and Power of Two: One shifted bit is a key to any position you like.

A mask is a number whose 1s mark the lanes you care about. 1 << i builds the
mask for a single position.

From there: OR sets a bit, AND with the inverted mask clears it, XOR flips
it, and shifting right then ANDing 1 reads it. n & (n - 1) == 0 says n has
at most one bit set.

Lesson 4 of Bit Manipulation, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/bit-manipulation/masks-and-power-of-two

Run it:  python bit-manipulation/04-masks-and-power-of-two.py
"""


def get_bit(x, i):   return (x >> i) & 1
def set_bit(x, i):   return x | (1 << i)
def clear_bit(x, i): return x & ~(1 << i)
def flip_bit(x, i):  return x ^ (1 << i)

x = 0b1011                   # 11
print(get_bit(x, 2))         # 0
print(bin(set_bit(x, 2)))    # 0b1111
print(bin(clear_bit(x, 0)))  # 0b1010
print(bin(flip_bit(x, 3)))   # 0b11

def is_power_of_two(n):
    return n > 0 and n & (n - 1) == 0   # exactly one bit set


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
    check_printed(is_power_of_two(16), is_power_of_two(12), expect="True False")
