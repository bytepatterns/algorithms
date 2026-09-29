"""
Palindrome After One Deletion (easy) · patterns: two-pointers, greedy

A word game accepts a string if it reads the same forwards and backwards,
and it forgives a single typo. Given a string s of lowercase letters, return
True if s is already a palindrome or becomes one after deleting exactly one
character, and False otherwise. The empty string counts as a palindrome.

Examples:

    Input:  s = "racexcar"
    Output: True
    Why:    deleting the x leaves "racecar"

    Input:  s = "abcda"
    Output: False
    Why:    after the outer a's match, b and d disagree, and dropping either one still fails

    Input:  s = ""
    Output: True
    Why:    edge case, nothing to compare, so no deletion is needed

Approach:
    Matching outer characters can never be the problem, so the two pointers
    skip over them without spending the one deletion. At the first mismatch,
    any fix must delete one of those two characters, since every character
    outside them already has its partner. That leaves exactly two candidate
    substrings, each checked with a plain palindrome scan, and no further
    choices appear inside them. Time is O(n) because each character is
    compared at most a few times, and space is O(1).

The lesson behind it: Valid Palindrome
    https://bytepatterns.com/learn/strings/valid-palindrome
    python strings/02-valid-palindrome.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/palindrome-after-one-deletion

Run it:  python problems/strings/08-palindrome-after-one-deletion.py
"""


def almost_palindrome(s):
    def is_pal(i, j):                # plain two-pointer check of s[i..j]
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            # the one deletion must remove s[i] or s[j]
            return is_pal(i + 1, j) or is_pal(i, j - 1)
        i, j = i + 1, j - 1
    return True


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(almost_palindrome("racexcar"), True)
    check(almost_palindrome("abcda"), False)
    check(almost_palindrome(""), True)
