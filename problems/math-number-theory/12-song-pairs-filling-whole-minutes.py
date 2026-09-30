"""
Song Pairs Filling Whole Minutes (medium) · patterns: modular-arithmetic, remainder-count

You are given the lengths of songs in seconds. Count the pairs of songs, at
positions i < j, whose total length is a whole number of minutes, meaning
the sum of the two lengths is divisible by 60.

Examples:

    Input:  times = [30, 20, 150, 100, 40]
    Output: 3
    Why:    30 + 150, 20 + 100 and 20 + 40 are 180, 120 and 60 seconds

    Input:  times = [60, 60, 60]
    Output: 3
    Why:    every pair of the three songs adds up to 120 seconds

    Input:  times = [10, 20]
    Output: 0
    Why:    edge case, 30 seconds is not a whole minute

Approach:
    Divisibility by 60 depends only on remainders: (x + y) % 60 equals (x %
    60 + y % 60) % 60, so there are just 60 kinds of song. A song with
    remainder r completes a whole minute with any earlier song whose
    remainder is (60 - r) % 60; the outer % 60 makes a remainder of 0 pair
    with 0 rather than with a nonexistent 60, which is also what covers 30
    pairing with 30. Counting partners among the songs already seen, before
    adding the current one, counts each pair exactly once and never pairs a
    song with itself. Time is O(n) and space is O(1), since the table never
    holds more than 60 entries.

The lesson behind it: Modular Arithmetic
    https://bytepatterns.com/learn/math-number-theory/modular-arithmetic
    python math-number-theory/01-modular-arithmetic.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/math-number-theory/song-pairs-filling-whole-minutes

Run it:  python problems/math-number-theory/12-song-pairs-filling-whole-minutes.py
"""


def whole_minute_pairs(times):
    seen = [0] * 60                     # how many earlier songs have each remainder
    pairs = 0
    for t in times:
        r = t % 60
        pairs += seen[(60 - r) % 60]    # earlier songs that complete a minute
        seen[r] += 1
    return pairs


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(whole_minute_pairs([30, 20, 150, 100, 40]), 3)
    check(whole_minute_pairs([60, 60, 60]), 3)
    check(whole_minute_pairs([10, 20]), 0)
