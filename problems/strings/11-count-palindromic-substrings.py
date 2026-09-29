"""
Count Palindromic Substrings (medium) · patterns: expand-around-center, palindrome

Given a string s, count its substrings that read the same forwards and
backwards. Substrings at different positions count separately even when they
spell the same text, and every single character counts as one. Aim for O(n²)
time and O(1) extra space.

Examples:

    Input:  s = "level"
    Output: 7
    Why:    five single letters, plus "eve" and "level"

    Input:  s = "xyz"
    Output: 3
    Why:    only the single letters

    Input:  s = ""
    Output: 0
    Why:    edge case, an empty string has no substrings to count

Approach:
    Each palindrome is fixed by its centre and its length, and growing
    outward from a centre finds every palindrome around it in order of
    length, until the first mismatch rules out anything longer. The loop
    index c covers all 2n - 1 centres: c // 2 and (c + 1) // 2 name the same
    letter when c is even and two neighbouring letters when c is odd. Each
    step outward counts exactly one palindrome, so the work is the answer
    plus one failed check per centre. Time is O(n²) in the worst case, a
    string of one repeated letter, and space is O(1).

The lesson behind it: Longest Palindromic Substring
    https://bytepatterns.com/learn/strings/longest-palindromic-substring
    python strings/05-longest-palindromic-substring.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/count-palindromic-substrings

Run it:  python problems/strings/11-count-palindromic-substrings.py
"""


def count_palindromes(s):
    total = 0
    for c in range(2 * len(s) - 1):          # n letters and n - 1 gaps
        lo, hi = c // 2, (c + 1) // 2
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            total += 1                       # one more palindrome around this centre
            lo -= 1
            hi += 1
    return total


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_palindromes("level"), 7)
    check(count_palindromes("xyz"), 3)
    check(count_palindromes(""), 0)
