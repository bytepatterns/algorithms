"""
Valid Palindrome: Two pointers walk inward and settle it in one pass.

A palindrome reads the same from both ends, so check it from both ends. Put
one pointer at the start, one at the end, and walk them toward each other.

One mismatch is a definite no. Meeting in the middle is a definite yes — no
reversed copy, no extra memory.

Lesson 2 of Strings, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/strings/valid-palindrome

Run it:  python strings/02-valid-palindrome.py
"""


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():      # skip junk from the left
            left += 1
        elif not s[right].isalnum():   # ...and from the right
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False               # one mismatch is enough
        else:
            left, right = left + 1, right - 1
    return True


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(is_palindrome("RaceCar!"), True)
    check(is_palindrome("byte"), False)
