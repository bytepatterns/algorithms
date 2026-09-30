"""
Spot Dictionary Words in a Text (easy) · patterns: trie, prefix-pruning

Given a string text and a list of distinct words, return every pair [i, j]
such that the slice of text from index i to index j, both included, is one
of the words. Occurrences may overlap. Return the pairs sorted by i, then by
j.

Examples:

    Input:  text = "bytesofcode", words = ["byte", "bytes", "code", "of", "so"]
    Output: [[0, 3], [0, 4], [4, 5], [5, 6], [7, 10]]
    Why:    byte, bytes, so, of and code, where so and of share the letter o

    Input:  text = "ababa", words = ["aba", "ab"]
    Output: [[0, 1], [0, 2], [2, 3], [2, 4]]

    Input:  text = "abc", words = ["d"]
    Output: []
    Why:    edge case, no word occurs

Approach:
    The trie turns each start position into a walk that stops as soon as the
    text leaves every word, the same pruning that makes a trie-driven grid
    search fast: a set of words can only answer whether a whole slice is a
    word, while a trie also answers whether the slice can still become one.
    Walking from start i in increasing j reports the matches for that start
    in increasing order, and the starts are visited in order, so the output
    needs no sort. For a text of length n and a longest word of length L,
    time is O(n · L) plus O(W) to build the trie from W total letters, and
    space is O(W).

The lesson behind it: Word Search With a Trie
    https://bytepatterns.com/learn/tries/word-search-with-a-trie
    python tries/03-word-search-with-a-trie.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/tries/spot-dictionary-words-in-a-text

Run it:  python problems/tries/11-spot-dictionary-words-in-a-text.py
"""


def word_positions(text, words):
    root = {}
    for w in words:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node["$"] = True                        # a word ends here
    found = []
    for i in range(len(text)):
        node = root
        for j in range(i, len(text)):
            node = node.get(text[j])
            if node is None:                    # no word continues this way
                break
            if "$" in node:
                found.append([i, j])
    return found


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(word_positions("bytesofcode", ["byte", "bytes", "code", "of", "so"]), [[0, 3], [0, 4], [4, 5], [5, 6], [7, 10]])
    check(word_positions("ababa", ["aba", "ab"]), [[0, 1], [0, 2], [2, 3], [2, 4]])
    check(word_positions("abc", ["d"]), [])
