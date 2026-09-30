"""
Ransom Note From a Magazine (easy) · patterns: frequency-count, hash-map

A sign maker cuts letters out of a spare banner to spell a new message.
Given two lowercase strings note and banner, return True if note can be
spelled using letters from banner, where each letter of banner can be used
at most once. Both strings have up to 100,000 letters, so avoid searching
the banner again for every letter of the note.

Examples:

    Input:  note = "aab", banner = "baa"
    Output: True
    Why:    the banner has two a's and one b, exactly what the note needs

    Input:  note = "aa", banner = "ab"
    Output: False
    Why:    the note needs two a's, the banner only has one

    Input:  note = "", banner = "xyz"
    Output: True
    Why:    edge case, an empty note needs no letters at all

Approach:
    Only the number of copies of each letter matters, so the banner is
    reduced to a table of letter counts in one pass. Each letter of the note
    then spends one copy from that table, and the first letter whose count
    is already zero proves the note cannot be made. Every letter of both
    strings is touched once, so time is O(n + m), and the table holds at
    most 26 entries, so extra space is O(1).

The lesson behind it: Frequency Counting
    https://bytepatterns.com/learn/hash-tables/frequency-counting
    python hash-tables/03-frequency-counting.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/hash-tables/ransom-note-from-a-magazine

Run it:  python problems/hash-tables/13-ransom-note-from-a-magazine.py
"""


from collections import Counter

def can_spell(note, banner):
    stock = Counter(banner)             # letter -> copies left
    for ch in note:
        if stock[ch] == 0:
            return False                # this letter has run out
        stock[ch] -= 1
    return True


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(can_spell("aab", "baa"), True)
    check(can_spell("aa", "ab"), False)
    check(can_spell("", "xyz"), True)
