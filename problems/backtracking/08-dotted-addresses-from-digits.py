"""
Dotted Addresses From Digits (medium) · patterns: backtracking, pruning

A log file lost the dots from its network addresses, leaving only a string
of digits. An address is four numbers from 0 to 255 joined by dots, and a
number never has a leading zero unless it is exactly 0. Return every address
that could have produced the digit string, keeping the digits in order and
using all of them. Any order of the results is accepted.

Examples:

    Input:  s = "25525511135"
    Output: ["255.255.11.135", "255.255.111.35"]

    Input:  s = "101023"
    Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    Why:    "1.01.0.23" is not listed, since 01 has a leading zero

    Input:  s = "0000"
    Output: ["0.0.0.0"]
    Why:    edge case, each part must be a single 0

Approach:
    The search is a decision tree four levels deep, where each level decides
    whether the next part takes one, two or three digits, so it has at most
    81 leaves however long the input is. A part is invalid when it starts
    with 0 and is longer than one digit or when its value exceeds 255, and
    in both cases every longer part from the same position is invalid as
    well, so the loop can stop instead of continuing. A branch that has cut
    four parts is kept only if it used every digit, and strings shorter than
    4 or longer than 12 digits are rejected up front. The tree has a
    constant size, so time and space are O(1) beyond the output.

The lesson behind it: The Decision Tree
    https://bytepatterns.com/learn/backtracking/the-decision-tree
    python backtracking/01-the-decision-tree.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/backtracking/dotted-addresses-from-digits

Run it:  python problems/backtracking/08-dotted-addresses-from-digits.py
"""


def dotted_addresses(s):
    out = []
    def place(start, parts):
        if len(parts) == 4:
            if start == len(s):                # all digits used
                out.append(".".join(parts))
            return
        for size in (1, 2, 3):
            piece = s[start:start + size]
            if len(piece) < size: break        # ran out of digits
            if (piece[0] == "0" and size > 1) or int(piece) > 255:
                break                          # longer pieces fail too
            place(start + size, parts + [piece])
    if 4 <= len(s) <= 12:
        place(0, [])
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(dotted_addresses("25525511135"), ['255.255.11.135', '255.255.111.35'])
    check(dotted_addresses("101023"), ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3'])
    check(dotted_addresses("0000"), ['0.0.0.0'])
