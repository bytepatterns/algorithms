"""
Reverse Bit Order (easy) · patterns: bit-shifting, accumulator

Treat a non-negative whole number as a fixed field of 32 binary digits,
padded with zeros on the left. Return the value you get by reversing the
order of those 32 digits, so the lowest digit becomes the highest and vice
versa. The width is always 32, whatever the size of the input.

Examples:

    Input:  value = 1
    Output: 2147483648
    Why:    the single low digit moves all the way to the top of the field

    Input:  value = 3
    Output: 3221225472
    Why:    the two low digits become the two highest ones

    Input:  value = 0
    Output: 0
    Why:    edge case, a field of zeros reads the same in either direction

Approach:
    Reading the input from the bottom up and writing the result from the
    bottom up produces the reversal for free, because the first digit read
    ends up pushed the furthest left by the later shifts. Each round shifts
    the result up to open a slot, copies the input's lowest digit into it
    with a mask and an or, then discards that digit from the input. Running
    exactly 32 rounds is what pads a small number out to the full field
    width instead of stopping early. Time is O(32), which is constant, and
    space is O(1).

The lesson behind it: Binary and Bitwise Ops
    https://bytepatterns.com/learn/bit-manipulation/binary-and-bitwise-ops
    python bit-manipulation/01-binary-and-bitwise-ops.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/bit-manipulation/reverse-bit-order

Run it:  python problems/bit-manipulation/01-reverse-bit-order.py
"""


def reverse_bits(value):
    result = 0
    for _ in range(32):              # a fixed width, whatever the input size
        result = (result << 1) | (value & 1)   # open a slot, copy the low digit
        value >>= 1                  # drop the digit just consumed
    return result


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(reverse_bits(1), 2147483648)
    check(reverse_bits(3), 3221225472)
    check(reverse_bits(0), 0)
