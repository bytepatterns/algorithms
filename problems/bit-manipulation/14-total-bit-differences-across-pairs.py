"""
Total Bit Differences Across Pairs (medium) · patterns: bit-counting, per-bit-contribution

A network team compares device fingerprints stored as non-negative integers
below 2^30. The difference between two fingerprints is the number of bit
positions where they differ. Given a list of fingerprints, return the sum of
the differences over every unordered pair. The list has up to 10,000 values,
so XOR-ing every pair is too slow.

Examples:

    Input:  nums = [4, 14, 2]
    Output: 6
    Why:    4 vs 14 differ in 2 bits, 4 vs 2 in 2, 14 vs 2 in 2

    Input:  nums = [4, 14, 4]
    Output: 4

    Input:  nums = [7]
    Output: 0
    Why:    edge case, one value makes no pairs

Approach:
    The total over all pairs can be summed one bit position at a time,
    because each pair's difference is just the count of positions where it
    disagrees. At a given position, a pair disagrees exactly when one value
    has a 1 and the other a 0, so with c ones among n values there are c *
    (n - c) disagreeing pairs, and no pair ever needs to be looked at on its
    own. That makes 30 passes of n values each, so time is O(30 · n) = O(n),
    and extra space is O(1).

The lesson behind it: Counting Set Bits
    https://bytepatterns.com/learn/bit-manipulation/counting-set-bits
    python bit-manipulation/03-counting-set-bits.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/bit-manipulation/total-bit-differences-across-pairs

Run it:  python problems/bit-manipulation/14-total-bit-differences-across-pairs.py
"""


def total_bit_differences(nums):
    n, total = len(nums), 0
    for bit in range(30):
        ones = sum((x >> bit) & 1 for x in nums)   # values with this bit on
        total += ones * (n - ones)                 # each on/off pair differs here
    return total


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(total_bit_differences([4, 14, 2]), 6)
    check(total_bit_differences([4, 14, 4]), 4)
    check(total_bit_differences([7]), 0)
