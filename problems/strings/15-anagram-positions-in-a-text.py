"""
Anagram Positions in a Text (medium) · patterns: fixed-sliding-window, frequency-count

A plagiarism checker looks for scrambled copies of a short key inside a long
text. Given lowercase strings text and key, return every start index i where
the len(key) letters of text starting at i form an anagram of key, meaning
they use exactly the same letters the same number of times. List the indices
in ascending order. Both strings have up to 30,000 letters, so re-counting
every window from scratch is too slow.

Examples:

    Input:  text = "cbaebabacd", key = "abc"
    Output: [0, 6]
    Why:    "cba" starts at 0 and "bac" starts at 6

    Input:  text = "abab", key = "ab"
    Output: [0, 1, 2]
    Why:    windows may overlap: "ab", "ba", "ab"

    Input:  text = "a", key = "ab"
    Output: []
    Why:    edge case, the key is longer than the text

Approach:
    The window has a fixed width, so each slide adds one letter on the right
    and drops one on the left, and only those two letters' counts change.
    Rather than comparing two full tables each time, the code keeps need[c]
    as the key's count minus the window's count, plus a tally of how many
    letters have need[c] ≠ 0. Changing one count can only move that letter
    in or out of the tally, so the check stays O(1) per slide, and a tally
    of zero means the window matches the key. Time is O(len(text) +
    len(key)), and space is O(1) for 26 letters.

The lesson behind it: Sliding Window
    https://bytepatterns.com/learn/arrays/sliding-window
    python arrays/03-sliding-window.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/anagram-positions-in-a-text

Run it:  python problems/strings/15-anagram-positions-in-a-text.py
"""


from collections import Counter

def anagram_starts(text, key):
    k = len(key)
    need = Counter(key)                 # key count minus window count
    off = len(need)                     # letters whose need is not zero
    out = []

    def change(ch, delta):
        nonlocal off
        before = need[ch]
        need[ch] = before + delta
        if before == 0:
            off += 1                    # was balanced, now is not
        elif need[ch] == 0:
            off -= 1                    # just became balanced

    for i, ch in enumerate(text):
        change(ch, -1)                  # letter enters the window
        if i >= k:
            change(text[i - k], +1)     # letter leaves the window
        if i >= k - 1 and off == 0:
            out.append(i - k + 1)
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(anagram_starts("cbaebabacd", "abc"), [0, 6])
    check(anagram_starts("abab", "ab"), [0, 1, 2])
    check(anagram_starts("a", "ab"), [])
