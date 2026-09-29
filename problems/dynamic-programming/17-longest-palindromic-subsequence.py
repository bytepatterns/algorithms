"""
Longest Palindromic Subsequence (medium) · patterns: lcs, 2d-dp

Given a string s, return the length of its longest palindromic subsequence:
the longest palindrome you can get by deleting any characters from s while
keeping the rest in their original order. The kept letters do not need to be
next to each other in s.

Examples:

    Input:  s = "character"
    Output: 5
    Why:    "carac" keeps c, a, r, a, c in order and reads the same both ways

    Input:  s = "abcd"
    Output: 1
    Why:    no letter repeats, so a single letter is the best

    Input:  s = ""
    Output: 0
    Why:    edge case, nothing to keep

Approach:
    Every palindromic subsequence of s is also a subsequence of its reverse,
    so it is common to both strings; in the other direction, a longest
    common subsequence of s and its reverse can always be chosen to be a
    palindrome, so the two lengths are equal. The standard recurrence fills
    a table whose cell (i, j) holds the answer for the first i letters of s
    and the first j letters of the reverse. Each row only reads the row
    above it, so two rows of length n + 1 are enough. Time is O(n²) and
    space is O(n).

The lesson behind it: Longest Common Subsequence
    https://bytepatterns.com/learn/dynamic-programming/longest-common-subsequence
    python dynamic-programming/06-longest-common-subsequence.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/longest-palindromic-subsequence

Run it:  python problems/dynamic-programming/17-longest-palindromic-subsequence.py
"""


def longest_pal_subseq(s):
    rev = s[::-1]
    prev = [0] * (len(s) + 1)                # the row for zero letters of s
    for a in s:
        cur = [0]
        for j, b in enumerate(rev):
            # a match extends the diagonal; otherwise keep the better neighbour
            cur.append(prev[j] + 1 if a == b else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(longest_pal_subseq("character"), 5)
    check(longest_pal_subseq("abcd"), 1)
    check(longest_pal_subseq(""), 0)
