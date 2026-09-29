"""
Longest Common Subsequence: Match the two ends, or drop a character from one side.

Compare two sequences from the end inward. If the last characters match, the
answer is the answer for both shorter prefixes plus one. If they differ,
drop the last character of one string or the other and keep whichever gives
more. A grid indexed by prefix lengths stores every one of those sub-answers
exactly once.

Lesson 6 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/longest-common-subsequence

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python dynamic-programming/06-longest-common-subsequence.py
"""


def lcs(a, b):
    grid = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                grid[i][j] = grid[i - 1][j - 1] + 1        # matched: take the diagonal
            else:
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])
    return grid[len(a)][len(b)]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(lcs("ABCBDAB", "BDCABA"), 4)
    check(lcs("night", "eight"), 4)
