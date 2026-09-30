"""
Group Words by Letter Shift (medium) · patterns: canonical-key, hash-map, grouping

A cipher tool shifts every letter of a word forward by the same amount,
wrapping from z back to a, so "abc" can become "bcd" or "xyz". Given a list
of lowercase words, group together the words that can be shifted into one
another. Return the groups in the order their first word appears in the
input, and keep the words inside each group in input order. There can be up
to 10,000 words of up to 50 letters each.

Examples:

    Input:  words = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    Output: [["abc", "bcd", "xyz"], ["acef"], ["az", "ba"], ["a", "z"]]
    Why:    "az" shifted by one becomes "ba", since z wraps round to a

    Input:  words = ["dog", "eph", "cat"]
    Output: [["dog", "eph"], ["cat"]]

    Input:  words = []
    Output: []
    Why:    edge case, nothing to group

Approach:
    Two words belong together exactly when the gaps between their
    neighbouring letters match, measured modulo 26 so that wrapping from z
    to a counts as a gap of one. That gap sequence is a canonical key,
    playing the role the sorted letters play in Group Anagrams, and a
    dictionary from key to list collects each group in one pass. Python
    dictionaries keep insertion order, which gives the groups in order of
    their first word. Time is O(total letters), and space is O(total
    letters) for the keys and groups.

The lesson behind it: Group Anagrams
    https://bytepatterns.com/learn/hash-tables/group-anagrams
    python hash-tables/04-group-anagrams.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/hash-tables/group-words-by-letter-shift

Run it:  python problems/hash-tables/14-group-words-by-letter-shift.py
"""


def group_by_shift(words):
    groups = {}
    for w in words:
        key = tuple((ord(b) - ord(a)) % 26 for a, b in zip(w, w[1:]))  # wrap-aware gaps
        groups.setdefault(key, []).append(w)
    return list(groups.values())


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(group_by_shift(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]), [['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']])
    check(group_by_shift(["dog", "eph", "cat"]), [['dog', 'eph'], ['cat']])
    check(group_by_shift([]), [])
