"""
First Unique Character (easy) · patterns: hash-map, two-pass

Given a piece of text, find the position of the first character that appears
exactly once in the whole text. Positions are counted from zero. Return -1
when every character shows up more than once.

Examples:

    Input:  text = "reference"
    Output: 2
    Why:    r and e both repeat later, so f is the first character that stands alone

    Input:  text = "aabb"
    Output: -1
    Why:    every character has a twin

    Input:  text = ""
    Output: -1
    Why:    edge case, there is no character to report

Approach:
    Uniqueness cannot be decided during a single forward pass, because a
    character seen once may still repeat later. Two passes solve it cleanly:
    the first builds a tally of every character, and the second walks the
    text in order and stops at the first character whose tally is one.
    Walking the text rather than the tally is what makes the answer the
    first position rather than an arbitrary one. Time is O(n) and space is
    O(k) for the distinct characters.

The lesson behind it: Frequency Counting
    https://bytepatterns.com/learn/hash-tables/frequency-counting
    python hash-tables/03-frequency-counting.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/first-unique-character

Run it:  python problems/strings/02-first-unique-character.py
"""


from collections import Counter
def first_unique_index(text):
    counts = Counter(text)           # one pass to tally every character
    for i, ch in enumerate(text):
        if counts[ch] == 1:          # the earliest character with a tally of one
            return i
    return -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(first_unique_index("reference"), 2)
    check(first_unique_index("aabb"), -1)
    check(first_unique_index(""), -1)
