"""
Flip Letter Case Variants (easy) · patterns: backtracking, include-exclude

A string mixes letters and digits. Every letter may be written in lowercase
or in uppercase, while digits never change. Return every string you can
produce this way. List them so that, for each letter from left to right, the
lowercase choice comes before the uppercase one.

Examples:

    Input:  s = "a1b"
    Output: ["a1b", "a1B", "A1b", "A1B"]
    Why:    two letters, two choices each, four strings

    Input:  s = "3Z"
    Output: ["3z", "3Z"]
    Why:    the letter's original case does not matter, both forms are listed

    Input:  s = "42"
    Output: ["42"]
    Why:    edge case, with no letters there is exactly one string, the input itself

Approach:
    Each letter is an include-or-exclude style decision with exactly two
    branches, and each digit is a level with a single branch, so the
    recursion depth is the string length and the leaves are the answers. A
    single buffer holds the current string; each branch overwrites its own
    position before going deeper, which is why no explicit undo step is
    needed. Trying the lowercase form first gives the required order. With L
    letters in a string of length n there are 2 to the L results of length
    n, so time is O(n times 2 to the L) and the recursion depth is O(n).

The lesson behind it: Subsets
    https://bytepatterns.com/learn/backtracking/subsets
    python backtracking/02-subsets.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/backtracking/flip-letter-case-variants

Run it:  python problems/backtracking/04-flip-letter-case-variants.py
"""


def case_variants(s):
    out, path = [], list(s)
    def build(i):
        if i == len(s):                   # every position is decided
            out.append("".join(path))
            return
        if s[i].isalpha():
            for ch in (s[i].lower(), s[i].upper()):   # two branches
                path[i] = ch              # overwriting doubles as the undo
                build(i + 1)
        else:
            build(i + 1)                  # a digit has a single branch
    build(0)
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(case_variants("a1b"), ['a1b', 'a1B', 'A1b', 'A1B'])
    check(case_variants("3Z"), ['3z', '3Z'])
    check(case_variants("42"), ['42'])
