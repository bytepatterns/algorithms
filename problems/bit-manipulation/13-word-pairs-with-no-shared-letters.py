"""
Word Pairs With No Shared Letters (medium) · patterns: bitmask, set-as-integer

A puzzle setter wants two clue words that share no letter at all, and the
longer the pair the better. Given a list of lowercase words, return the
largest value of len(a) * len(b) over two different words a and b that have
no letter in common, or 0 if no such pair exists. There are up to 1,000
words of up to 1,000 letters each, so comparing the letters of every pair
directly is too slow.

Examples:

    Input:  words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    Output: 16
    Why:    "abcw" and "xtfn" share no letter, and 4 * 4 = 16

    Input:  words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    Output: 4
    Why:    "ab" and "cd" is the best disjoint pair

    Input:  words = ["a", "aa", "aaa"]
    Output: 0
    Why:    edge case, every pair shares the letter a

Approach:
    Each word is turned into a 26-bit mask of the letters it uses, which
    costs one pass over its letters. Set intersection is then a bitwise AND,
    so testing a pair is a single operation no matter how long the words
    are. Keeping only the longest word for each distinct mask can shrink the
    list further, since words with the same letter set are interchangeable
    and only the longest matters. Building the masks is O(L) for L total
    letters, and the pair loop is O(n²) constant-time checks; space is O(n).

The lesson behind it: Bitmask as a Set
    https://bytepatterns.com/learn/bit-manipulation/bitmask-as-a-set
    python bit-manipulation/05-bitmask-as-a-set.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/bit-manipulation/word-pairs-with-no-shared-letters

Run it:  python problems/bit-manipulation/13-word-pairs-with-no-shared-letters.py
"""


def best_disjoint_product(words):
    longest = {}                                  # letter mask -> longest word length
    for w in words:
        mask = 0
        for ch in w:
            mask |= 1 << (ord(ch) - ord("a"))     # add the letter to the set
        longest[mask] = max(longest.get(mask, 0), len(w))
    items = list(longest.items())
    best = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][0] & items[j][0] == 0:    # no letter in common
                best = max(best, items[i][1] * items[j][1])
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(best_disjoint_product(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]), 16)
    check(best_disjoint_product(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]), 4)
    check(best_disjoint_product(["a", "aa", "aaa"]), 0)
