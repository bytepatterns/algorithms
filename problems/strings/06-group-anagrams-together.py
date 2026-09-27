"""
Group Anagrams Together (medium) · patterns: hash-map, canonical-form

Group a list of words so that words using exactly the same letters, in any
order, land in the same group. Return the groups with each group's words
sorted, and the groups themselves sorted.

Examples:

    Input:  words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    Why:    eat, tea and ate all use a, e and t

    Input:  words = ["ab", "ba", "abc"]
    Output: [["ab", "ba"], ["abc"]]
    Why:    length alone separates the second group

    Input:  words = [""]
    Output: [[""]]
    Why:    edge case, the empty word forms its own group

Approach:
    The trick is a canonical form: a value derived from a word that is
    identical for every anagram of it and different for everything else.
    Sorting a word's letters is the simplest such form, and it doubles as a
    hash-map key, so one pass over the words builds all the groups. For n
    words of length up to k, the cost is O(n · k log k) — dominated by
    sorting the letters, not by comparing words to each other. A count-of-26
    tuple replaces the inner sort with O(k) when the alphabet is fixed.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/group-anagrams-together

Run it:  python problems/strings/06-group-anagrams-together.py
"""


def group_anagrams(words):
    groups = {}
    for w in words:
        key = "".join(sorted(w))              # same letters -> same key
        groups.setdefault(key, []).append(w)
    return sorted(sorted(g) for g in groups.values())


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']])
    check(group_anagrams(["ab", "ba", "abc"]), [['ab', 'ba'], ['abc']])
    check(group_anagrams([""]), [['']])
