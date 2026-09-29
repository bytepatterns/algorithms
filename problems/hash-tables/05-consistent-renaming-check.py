"""
Consistent Renaming Check (easy) · patterns: hash-map, bijection

Two pieces of text have the same shape if one can be turned into the other
by renaming characters. A renaming must be consistent in both directions:
every occurrence of a character maps to the same replacement, and no two
different characters may share a replacement. Decide whether such a renaming
exists.

Examples:

    Input:  a = "egg", b = "add"
    Output: True
    Why:    e becomes a and g becomes d, consistently

    Input:  a = "foo", b = "bar"
    Output: False
    Why:    o would have to become both a and r

    Input:  a = "ab", b = "aa"
    Output: False
    Why:    edge case, two characters may not collapse onto the same replacement

Approach:
    Walking both texts together pairs up the characters position by
    position, and a valid renaming means no pair ever contradicts an earlier
    one. Two maps are needed rather than one: the forward map catches a
    character being renamed two different ways, and the backward map catches
    two characters collapsing onto the same replacement. Recording on first
    sight and comparing thereafter does both checks in one pass. Time is
    O(n) on average, and space is O(k) for the distinct characters.

The lesson behind it: Hash Table Basics
    https://bytepatterns.com/learn/hash-tables/hash-table-basics
    python hash-tables/01-hash-table-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/hash-tables/consistent-renaming-check

Run it:  python problems/hash-tables/05-consistent-renaming-check.py
"""


def has_consistent_renaming(a, b):
    if len(a) != len(b):
        return False
    forward, backward = {}, {}       # a -> b and b -> a pairings seen so far
    for x, y in zip(a, b):
        # setdefault records a new pairing and returns the one already stored
        if forward.setdefault(x, y) != y or backward.setdefault(y, x) != x:
            return False
    return True


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(has_consistent_renaming("egg", "add"), True)
    check(has_consistent_renaming("foo", "bar"), False)
    check(has_consistent_renaming("ab", "aa"), False)
