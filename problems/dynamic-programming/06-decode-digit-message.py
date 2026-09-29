"""
Decode Digit Message (medium) · patterns: bottom-up-dp, rolling-variables

Letters were turned into numbers, A to Z becoming 1 to 26, and the numbers
were then written down with no separators. Count how many different letter
sequences could have produced a given digit text. A group of digits is only
a letter when it reads as 1 through 26, so no group may start with a zero.

Examples:

    Input:  digits = "226"
    Output: 3
    Why:    the cuts 2 26, 22 6 and 2 2 6 are all legal

    Input:  digits = "11106"
    Output: 2
    Why:    the zero must join the digit before it, which rules out most cuts

    Input:  digits = "0"
    Output: 0
    Why:    edge case, nothing decodes a leading zero

Approach:
    The last letter of any decoding consumes either one digit or two, so the
    number of decodings of a prefix is the sum of the counts for the
    prefixes one and two digits shorter, each guarded by whether that final
    group is legal. A zero can never stand alone, and a pair only counts
    when it lands between 10 and 26, which is what rules out both leading
    zeros and oversized pairs. Only the last two counts are ever needed, so
    two variables replace the table. Time is O(n) and space is O(1).

The lesson behind it: Top-Down vs Bottom-Up
    https://bytepatterns.com/learn/dynamic-programming/top-down-vs-bottom-up
    python dynamic-programming/02-top-down-vs-bottom-up.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/decode-digit-message

Run it:  python problems/dynamic-programming/06-decode-digit-message.py
"""


def count_decodings(digits):
    if not digits:
        return 0
    prev, cur = 1, (0 if digits[0] == "0" else 1)   # empty prefix, then one digit
    for i in range(1, len(digits)):
        total = 0
        if digits[i] != "0":                        # this digit stands on its own
            total += cur
        if 10 <= int(digits[i - 1:i + 1]) <= 26:    # the pair reads as one letter
            total += prev
        prev, cur = cur, total
    return cur


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_decodings("226"), 3)
    check(count_decodings("11106"), 2)
    check(count_decodings("0"), 0)
