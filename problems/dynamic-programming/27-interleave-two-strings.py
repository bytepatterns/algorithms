"""
Interleave Two Strings (medium) · patterns: two-string-dp, rolling-row

A log merger combines two event streams into one without reordering either
stream. Given strings a, b and c, return True if c can be formed by
interleaving a and b: every character of a and of b is used exactly once,
and the characters of a appear in c in their original order, as do the
characters of b. a and b have up to 100 characters each, and c up to 200.

Examples:

    Input:  a = "aabcc", b = "dbbca", c = "aadbbcbcac"
    Output: True
    Why:    aa from a, dbbc from b, bc from a, a from b, c from a

    Input:  a = "aabcc", b = "dbbca", c = "aadbbbaccc"
    Output: False

    Input:  a = "", b = "", c = ""
    Output: True
    Why:    edge case, two empty streams merge into an empty one

Approach:
    If the lengths do not add up, the answer is False at once. Otherwise the
    problem is a two-string table in the style of edit distance: cell (i, j)
    records whether the first i characters of a and the first j of b can
    produce the first i + j characters of c. The last character of that
    prefix came either from a, which needs cell (i - 1, j) to be true and
    the characters to match, or from b, which needs cell (i, j - 1). Each
    row only reads the row above and the cell to its left, so a single row
    updated in place is enough. Time is O(len(a) · len(b)), and space is
    O(len(b)).

The lesson behind it: Edit Distance
    https://bytepatterns.com/learn/dynamic-programming/edit-distance
    python dynamic-programming/08-edit-distance.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/interleave-two-strings

Run it:  python problems/dynamic-programming/27-interleave-two-strings.py
"""


def is_interleaving(a, b, c):
    if len(a) + len(b) != len(c):
        return False
    ok = [True] + [False] * len(b)              # row i = 0: only b used so far
    for j in range(1, len(b) + 1):
        ok[j] = ok[j - 1] and b[j - 1] == c[j - 1]
    for i in range(1, len(a) + 1):
        ok[0] = ok[0] and a[i - 1] == c[i - 1]
        for j in range(1, len(b) + 1):
            ch = c[i + j - 1]
            from_a = ok[j] and a[i - 1] == ch       # ok[j] still holds the row above
            from_b = ok[j - 1] and b[j - 1] == ch   # ok[j - 1] is this row already
            ok[j] = from_a or from_b
    return ok[len(b)]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(is_interleaving("aabcc", "dbbca", "aadbbcbcac"), True)
    check(is_interleaving("aabcc", "dbbca", "aadbbbaccc"), False)
    check(is_interleaving("", "", ""), True)
