"""
Palindrome Check Ignoring Punctuation (easy) · patterns: tail-recursion, two-pointers

Decide whether a string reads the same forwards and backwards once you
ignore case and skip every character that is not a letter or a digit. Write
it first as a recursive function that compares the two ends and recurses on
what lies between them, then turn it into a loop that handles strings of any
length.

Examples:

    Input:  s = "A man, a plan, a canal: Panama"
    Output: True
    Why:    the letters alone read amanaplanacanalpanama both ways

    Input:  s = "race a car"
    Output: False
    Why:    raceacar reversed is racaecar

    Input:  s = ".,!"
    Output: True
    Why:    edge case, nothing is left after skipping punctuation, and an empty string is a palindrome

Approach:
    The recursive version states the definition directly: skip a
    non-alphanumeric end, fail on a mismatched pair, otherwise move both
    ends inwards. Every recursive call is in tail position, since its result
    is returned unchanged with no work left afterwards, so the frame that
    made the call is dead weight. Python does not reuse those frames, so a
    string of a few thousand characters overflows the recursion limit even
    though the logic is fine. The loop is the mechanical translation: the
    parameters i and j become variables, and each tail call becomes an
    update of them followed by another trip round the loop. Both run in O(n)
    time; the recursive one uses O(n) stack and the loop O(1).

The lesson behind it: Tail Calls and Loops
    https://bytepatterns.com/learn/recursion/tail-recursion
    python recursion/07-tail-recursion.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/recursion/palindrome-check-ignoring-punctuation

Run it:  python problems/recursion/14-palindrome-check-ignoring-punctuation.py
"""


def is_palindrome(s, i=0, j=None):
    if j is None:
        j = len(s) - 1
    if i >= j:
        return True
    if not s[i].isalnum():
        return is_palindrome(s, i + 1, j)
    if not s[j].isalnum():
        return is_palindrome(s, i, j - 1)
    if s[i].lower() != s[j].lower():
        return False
    return is_palindrome(s, i + 1, j - 1)       # tail call: nothing happens after it

def is_palindrome_loop(s):
    i, j = 0, len(s) - 1
    while i < j:                                # each tail call becomes one update
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
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
    check(is_palindrome("A man, a plan, a canal: Panama"), True)
    check(is_palindrome("race a car"), False)
    check(is_palindrome(".,!"), True)
    check(is_palindrome_loop("ab" * 50000 + "a"), True)
