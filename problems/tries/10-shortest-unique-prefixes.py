"""
Shortest Unique Prefixes (medium) · patterns: trie, prefix-count

Given a list of distinct lowercase words where no word is a prefix of
another, return for each word the shortest prefix that no other word in the
list starts with. This is how a command line lets you type just enough
letters to pick one command.

Examples:

    Input:  words = ["zebra", "dog", "duck", "dove"]
    Output: ["z", "dog", "du", "dov"]
    Why:    d is shared by three words and do by two, but dog and dov are unique

    Input:  words = ["bear", "bell", "bid", "bull", "buy"]
    Output: ["bea", "bel", "bi", "bul", "buy"]

    Input:  words = ["solo"]
    Output: ["s"]
    Why:    edge case, a single word is identified by its first letter

Approach:
    A node's pass count is the number of words that start with the prefix
    spelled on the way to it, so the first node on a word's path with a
    count of 1 marks its shortest unique prefix. A counter of sliced
    prefixes would give the same counts, but building every slice costs time
    proportional to its length, which adds up to the square of each word's
    length. The trie reaches every prefix by one step from the previous one
    and stores shared prefixes once. The rule that no word is a prefix of
    another guarantees that every word eventually reaches a count of 1. Time
    is O(L) for L total letters, and space is O(L).

The lesson behind it: Trie vs Hash Set
    https://bytepatterns.com/learn/tries/trie-vs-hash-set
    python tries/04-trie-vs-hash-set.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/tries/shortest-unique-prefixes

Run it:  python problems/tries/10-shortest-unique-prefixes.py
"""


def unique_prefixes(words):
    root = {}
    for w in words:
        node = root
        for ch in w:
            node = node.setdefault(ch, {"#": 0})
            node["#"] += 1                   # one more word passes through here
    result = []
    for w in words:
        node = root
        for i, ch in enumerate(w):
            node = node[ch]
            if node["#"] == 1:               # only this word goes this way
                result.append(w[: i + 1])
                break
    return result


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(unique_prefixes(["zebra", "dog", "duck", "dove"]), ['z', 'dog', 'du', 'dov'])
    check(unique_prefixes(["bear", "bell", "bid", "bull", "buy"]), ['bea', 'bel', 'bi', 'bul', 'buy'])
    check(unique_prefixes(["solo"]), ['s'])
