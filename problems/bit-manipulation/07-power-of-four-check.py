"""
Power of Four Check (easy) · patterns: bitmask, power-of-two

Given a whole number n that fits in a signed 32-bit integer, return True if
n equals 4 raised to some whole power (1, 4, 16, 64 and so on) and False
otherwise. Zero and negative numbers are never powers of four. Try to answer
without a loop, using only bit operations.

Examples:

    Input:  n = 16
    Output: True
    Why:    16 is 4 squared

    Input:  n = 8
    Output: False
    Why:    8 is a power of two, but its single set bit is in the wrong place

    Input:  n = 1
    Output: True
    Why:    edge case, 4 to the power 0 is 1

Approach:
    A power of four is a power of two whose only set bit sits at an even
    position, since each multiplication by four shifts that bit two places
    left. Subtracting one from a power of two flips its single bit and every
    bit below it, so n & (n - 1) is zero exactly for powers of two. The mask
    0x55555555 has a 1 in every even position of a 32-bit word, so it keeps
    the bit of 1, 4, 16 and 64 but drops the bit of 2, 8 and 32. Time and
    space are O(1).

The lesson behind it: Masks and Power of Two
    https://bytepatterns.com/learn/bit-manipulation/masks-and-power-of-two
    python bit-manipulation/04-masks-and-power-of-two.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/bit-manipulation/power-of-four-check

Run it:  python problems/bit-manipulation/07-power-of-four-check.py
"""


def is_power_of_four(n):
    one_bit = n > 0 and (n & (n - 1)) == 0    # a power of two has a single set bit
    return one_bit and (n & 0x55555555) != 0  # ...and for four it sits at an even position


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(is_power_of_four(16), True)
    check(is_power_of_four(8), False)
    check(is_power_of_four(1), True)
    check(is_power_of_four(0), False)
