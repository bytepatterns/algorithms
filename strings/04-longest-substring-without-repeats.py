"""
Longest Unique Substring: Grow a window, shrink it the moment a letter repeats.

Keep a window that holds only distinct characters, plus a set of what is
inside it. The right edge always advances.

When the incoming character is already in the set, pull the left edge in —
dropping characters — until the duplicate is gone. The longest width you
ever saw is the answer.

Lesson 4 of Strings, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/strings/longest-substring-without-repeats

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python strings/04-longest-substring-without-repeats.py
"""


def longest_unique(s):
    seen = set()
    left = best = 0
    for right, ch in enumerate(s):
        while ch in seen:           # shrink until ch is free again
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        best = max(best, right - left + 1)
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(longest_unique("abcabcbb"), 3)  # "abc"
    check(longest_unique("bbbbb"), 1)
