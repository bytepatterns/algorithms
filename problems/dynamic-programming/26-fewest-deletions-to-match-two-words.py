"""
Fewest Deletions to Match Two Words (easy) · patterns: lcs, string-dp

Given two words a and b, one step deletes a single character from either
word. Return the fewest steps needed to make the two words identical.

Examples:

    Input:  a = "sea", b = "eat"
    Output: 2
    Why:    delete the s from sea and the t from eat, leaving ea in both

    Input:  a = "abcde", b = "ace"
    Output: 2
    Why:    ace already appears inside abcde in order, so only b and d go

    Input:  a = "abc", b = ""
    Output: 3
    Why:    edge case, everything in the first word must be deleted

Approach:
    Deleting until the words match leaves a string that is a subsequence of
    both, so the fewest deletions come from keeping the longest common
    subsequence and removing everything else from each word. The table entry
    for the first i characters of a and the first j of b extends the
    diagonal entry by one when the last characters match, and otherwise
    takes the better of dropping the last character of either word. Every
    character outside the common subsequence is deleted once, which gives
    len(a) + len(b) - 2 * lcs. Time is O(m · n) and space is O(m · n) for
    words of lengths m and n.

The lesson behind it: Longest Common Subsequence
    https://bytepatterns.com/learn/dynamic-programming/longest-common-subsequence
    python dynamic-programming/06-longest-common-subsequence.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/fewest-deletions-to-match-two-words

Run it:  python problems/dynamic-programming/26-fewest-deletions-to-match-two-words.py
"""


def min_deletions(a, b):
    m, n = len(a), len(b)
    lcs = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1          # keep the matching pair
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    return m + n - 2 * lcs[m][n]                           # delete everything not kept


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(min_deletions("sea", "eat"), 2)
    check(min_deletions("abcde", "ace"), 2)
    check(min_deletions("abc", ""), 3)
