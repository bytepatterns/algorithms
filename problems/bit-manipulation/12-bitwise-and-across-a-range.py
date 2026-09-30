"""
Bitwise AND Across a Range (medium) · patterns: common-prefix, bit-shift

A network tool needs the widest mask shared by a block of consecutive
addresses. Given two integers lo and hi with 0 ≤ lo ≤ hi ≤ 2^31 - 1, return
the bitwise AND of every integer from lo to hi, inclusive. The range can
hold about two billion numbers, so looping over it is far too slow.

Examples:

    Input:  lo = 5, hi = 7
    Output: 4
    Why:    101 & 110 & 111 = 100

    Input:  lo = 12, hi = 15
    Output: 12
    Why:    1100 through 1111 all share the prefix 11, and the low two bits take every value

    Input:  lo = 1, hi = 2147483647
    Output: 0
    Why:    edge case, the range crosses a power of two, so no bit survives

Approach:
    Take the highest bit where lo and hi differ: lo has a 0 there and hi has
    a 1, so the range contains the number with that 1 followed by all zeros,
    and the number just before it with that 0 followed by all ones. Between
    those two, every bit at or below that position is 0 in at least one
    number, so all of them vanish from the AND. Bits above it are the same
    in lo and hi, and since every number in between lies between them, those
    bits are shared by the whole range. The answer is therefore the common
    prefix of lo and hi padded with zeros, found by shifting both right
    until they match. That takes at most 31 shifts, so time and space are
    O(1).

The lesson behind it: Masks and Power of Two
    https://bytepatterns.com/learn/bit-manipulation/masks-and-power-of-two
    python bit-manipulation/04-masks-and-power-of-two.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/bit-manipulation/bitwise-and-across-a-range

Run it:  python problems/bit-manipulation/12-bitwise-and-across-a-range.py
"""


def range_and(lo, hi):
    shift = 0
    while lo != hi:          # strip bits until only the shared prefix is left
        lo >>= 1
        hi >>= 1
        shift += 1
    return lo << shift       # prefix followed by zeros


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(range_and(5, 7), 4)
    check(range_and(12, 15), 12)
    check(range_and(1, 2147483647), 0)
    check(range_and(9, 9), 9)
