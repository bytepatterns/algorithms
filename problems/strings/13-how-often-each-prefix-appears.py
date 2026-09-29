"""
How Often Each Prefix Appears (hard) · patterns: z-algorithm, suffix-sums

Given a string s of length n, return a list of n counts where the entry at
index i - 1 says how many times the prefix of s with length i appears inside
s. Overlapping appearances count separately, and the prefix itself counts as
one. The answer should take O(n) time, so searching for each prefix
separately is too slow.

Examples:

    Input:  s = "abacaba"
    Output: [4, 2, 2, 1, 1, 1, 1]
    Why:    "a" appears 4 times, "ab" and "aba" twice each, longer prefixes once

    Input:  s = "aaa"
    Output: [3, 2, 1]
    Why:    the two appearances of "aa" overlap and both count

    Input:  s = ""
    Output: []
    Why:    edge case, there are no prefixes to count

Approach:
    The prefix of length L appears at position j exactly when z[j] is at
    least L, so the answer for L is the number of positions whose Z value is
    at least L. The Z-array is built in linear time with the z-box, and
    position 0, which the loop never fills, is set to n because the whole
    string matches itself. A tally of positions per Z value followed by a
    suffix sum turns those values into all n answers in one pass. Time is
    O(n) and space is O(n).

The lesson behind it: Z-Algorithm Intuition
    https://bytepatterns.com/learn/strings/z-algorithm
    python strings/09-z-algorithm.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/how-often-each-prefix-appears

Run it:  python problems/strings/13-how-often-each-prefix-appears.py
"""


def prefix_counts(s):
    n = len(s)
    z, lo, hi = [0] * n, 0, 0
    for i in range(1, n):
        if i < hi:
            z[i] = min(hi - i, z[i - lo])      # reuse the z-box's mirror
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > hi:
            lo, hi = i, i + z[i]
    if n:
        z[0] = n                               # the whole string matches itself
    reach = [0] * (n + 2)
    for v in z:
        reach[v] += 1                          # a match of length v covers lengths 1..v
    for length in range(n - 1, 0, -1):
        reach[length] += reach[length + 1]     # at least this long
    return reach[1:n + 1]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(prefix_counts("abacaba"), [4, 2, 2, 1, 1, 1, 1])
    check(prefix_counts("aaa"), [3, 2, 1])
    check(prefix_counts(""), [])
