"""
Roman Numeral to Integer (easy) · patterns: string-scan, lookup-table

A museum catalogue stores years as Roman numerals and needs them as
integers. The symbols are I = 1, V = 5, X = 10, L = 50, C = 100, D = 500 and
M = 1000, written from largest to smallest and added up, except that a
smaller symbol placed right before a larger one is subtracted, as in IV = 4
or CM = 900. Given a valid numeral for a value from 1 to 3999, return its
value.

Examples:

    Input:  s = "LVIII"
    Output: 58
    Why:    L + V + I + I + I = 50 + 5 + 3

    Input:  s = "MCMXCIV"
    Output: 1994
    Why:    M = 1000, CM = 900, XC = 90, IV = 4

    Input:  s = "IV"
    Output: 4
    Why:    edge case, the whole numeral is a single subtractive pair

Approach:
    Every symbol either adds or subtracts its own value, and which one
    depends only on its right-hand neighbour: a smaller symbol before a
    larger one is subtracted, anything else is added. So one left-to-right
    pass with a one-character lookahead is enough, and no special table for
    pairs like CM or XC is needed. The last symbol has no neighbour and is
    always added. Time is O(n) for a numeral of n symbols, and space is
    O(1).

The lesson behind it: String Basics
    https://bytepatterns.com/learn/strings/string-basics
    python strings/01-string-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/roman-numeral-to-integer

Run it:  python problems/strings/16-roman-numeral-to-integer.py
"""


VALUE = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def roman_to_int(s):
    total = 0
    for i, ch in enumerate(s):
        v = VALUE[ch]
        if i + 1 < len(s) and VALUE[s[i + 1]] > v:
            total -= v                  # smaller before larger: subtract
        else:
            total += v
    return total


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(roman_to_int("LVIII"), 58)
    check(roman_to_int("MCMXCIV"), 1994)
    check(roman_to_int("IV"), 4)
