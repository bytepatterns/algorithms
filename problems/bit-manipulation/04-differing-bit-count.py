"""
Differing Bit Count (easy) · patterns: xor, bit-counting

Write two non-negative whole numbers in binary, one above the other and
aligned on the right. Count the positions where their binary digits
disagree. Missing digits on the left of the shorter number count as zeros.

Examples:

    Input:  a = 1, b = 4
    Output: 2
    Why:    001 against 100 disagrees in the first and last positions

    Input:  a = 7, b = 10
    Output: 3
    Why:    0111 against 1010 disagrees everywhere except the second position from the right

    Input:  a = 5, b = 5
    Output: 0
    Why:    edge case, a number never disagrees with itself

Approach:
    XOR sets a bit exactly where its inputs disagree, so the answer is
    simply the number of ones in a XOR b. Counting them with the
    clear-the-lowest-one trick costs one loop round per one rather than per
    digit, because subtracting one flips the lowest one and everything below
    it, and the AND then wipes that one out. The loop therefore runs as many
    times as the answer. Time is O(number of differing bits), at most O(log
    of the larger input), and space is O(1).

The lesson behind it: Counting Set Bits
    https://bytepatterns.com/learn/bit-manipulation/counting-set-bits
    python bit-manipulation/03-counting-set-bits.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/bit-manipulation/differing-bit-count

Run it:  python problems/bit-manipulation/04-differing-bit-count.py
"""


def differing_bits(a, b):
    x = a ^ b                  # a 1 wherever the two numbers disagree
    count = 0
    while x:
        x &= x - 1             # clear the lowest remaining 1
        count += 1
    return count


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(differing_bits(1, 4), 2)
    check(differing_bits(7, 10), 3)
    check(differing_bits(5, 5), 0)
