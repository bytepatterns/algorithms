"""
Shortest Encoding of a Word List (medium) · patterns: trie, suffix-sharing

A list of lowercase words is stored as one reference string in which every
word ends with a #, and each word is read by starting at some index and
stopping at the next #. A word that is a suffix of another word therefore
needs no space of its own: me can be read inside time#. Return the length of
the shortest reference string that can encode all the words.

Examples:

    Input:  words = ["time", "me", "bell"]
    Output: 10
    Why:    time#bell# holds all three, with me read from index 2

    Input:  words = ["atom", "tom", "m", "bat"]
    Output: 9
    Why:    atom#bat#, since tom and m are both suffixes of atom

    Input:  words = ["me", "me"]
    Output: 3
    Why:    edge case, a repeated word is encoded once

Approach:
    Reversing the words turns shared suffixes into shared prefixes, which is
    what a trie stores for free. After inserting each distinct reversed
    word, a word whose final node has children is the reversed prefix of a
    longer word, so it is a suffix of that word and rides inside its
    encoding. A word whose final node is a leaf must be written out with its
    #. Two different words cannot end at the same node, since the path
    spells the word, so counting leaves never double counts. The hash set
    version gives the same answer with less code but slices out every suffix
    of every word, which costs O(L²) per word; the trie touches each letter
    once. Time and space are O(W) for W total letters.

The lesson behind it: Trie vs Hash Set
    https://bytepatterns.com/learn/tries/trie-vs-hash-set
    python tries/04-trie-vs-hash-set.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/tries/shortest-encoding-of-a-word-list

Run it:  python problems/tries/12-shortest-encoding-of-a-word-list.py
"""


def encoding_length(words):
    root, ends = {}, []
    for w in set(words):                    # a repeated word is encoded once
        node = root
        for ch in reversed(w):              # shared suffixes become shared prefixes
            node = node.setdefault(ch, {})
        ends.append((node, len(w)))
    return sum(n + 1 for node, n in ends if not node)   # only leaves need their own #


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(encoding_length(["time", "me", "bell"]), 10)
    check(encoding_length(["atom", "tom", "m", "bat"]), 9)
    check(encoding_length(["me", "me"]), 3)
