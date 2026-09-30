"""
Scrambled String Check (hard) · patterns: recursion, memoization, divide-and-conquer

A string is scrambled like this: if it has one letter, stop; otherwise cut
it at any point into two non-empty parts, optionally swap the two parts, and
scramble each part the same way. Given two strings s1 and s2 of the same
length, return whether s2 could come out of scrambling s1.

Examples:

    Input:  s1 = "great", s2 = "rgeat"
    Output: True
    Why:    cut into gr and eat, swap g and r inside gr, leave eat unchanged

    Input:  s1 = "abcde", s2 = "caebd"
    Output: False

    Input:  s1 = "a", s2 = "a"
    Output: True
    Why:    edge case, a single letter is its own only scramble

Approach:
    The definition is the recursion. For pieces of length n, try every cut
    k: either the first k letters of the s1 piece become the first k of the
    s2 piece and the rest become the rest, or the parts were swapped, and
    the first k letters of the s1 piece become the last k of the s2 piece.
    Plain recursion explodes because the same pair of pieces is asked about
    along many different paths, so the answer for each (start in s1, start
    in s2, length) triple is cached. The sorted-letters check cuts off most
    branches early, since a swap never changes which letters a piece
    contains. There are O(n³) subproblems and each tries O(n) cuts, so time
    is O(n⁴) in the worst case, and the cache takes O(n³) space.

The lesson behind it: Memoization
    https://bytepatterns.com/learn/recursion/memoization-intro
    python recursion/04-memoization-intro.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/recursion/scrambled-string-check

Run it:  python problems/recursion/12-scrambled-string-check.py
"""


from functools import lru_cache

def is_scramble(s1, s2):
    if len(s1) != len(s2):
        return False

    @lru_cache(maxsize=None)
    def same(i, j, n):                  # can s1[i:i+n] become s2[j:j+n]?
        a, b = s1[i:i + n], s2[j:j + n]
        if a == b:
            return True
        if sorted(a) != sorted(b):      # different letters: no cut can fix that
            return False
        for k in range(1, n):
            if same(i, j, k) and same(i + k, j + k, n - k):        # parts kept in order
                return True
            if same(i, j + n - k, k) and same(i + k, j, n - k):    # parts swapped
                return True
        return False

    return same(0, 0, len(s1))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(is_scramble("great", "rgeat"), True)
    check(is_scramble("abcde", "caebd"), False)
    check(is_scramble("a", "a"), True)
