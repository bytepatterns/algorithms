"""
K Most Frequent Words (medium) · patterns: top-k, min-heap, hash-map

Given a list of words and an integer k, return the k words that occur most
often, from most to least frequent. Words with the same count are ordered
alphabetically, so the answer is always unique. k is at most the number of
distinct words.

Examples:

    Input:  words = ["red", "blue", "red", "green", "blue", "red"], k = 2
    Output: ["red", "blue"]
    Why:    red appears 3 times, blue 2 and green 1

    Input:  words = ["b", "a", "c", "a", "b", "c"], k = 2
    Output: ["a", "b"]
    Why:    all three words appear twice, so the alphabetical tie-break picks a and b

    Input:  words = ["solo"], k = 1
    Output: ["solo"]
    Why:    edge case, a single word is its own top 1

Approach:
    Counting is one pass with Counter. The two ordering rules fold into the
    single key (-count, word): negating the count makes more frequent words
    smaller, and the word itself breaks ties alphabetically, so "the k best
    words" becomes "the k smallest keys". heapq.nsmallest keeps a heap of
    only k candidates while it scans, evicting the worst one whenever a
    better word arrives, and returns the survivors sorted best first. The
    tie-break is where hand-rolled versions usually go wrong: a plain
    min-heap of (count, word) pairs evicts the alphabetically smaller word
    on a tie, which is the one you wanted to keep. Time is O(n + m log k)
    for n words and m distinct words, and space is O(m) for the counts.

The lesson behind it: Top K in a Stream
    https://bytepatterns.com/learn/two-heaps-k-way/top-k-frequent-stream
    python two-heaps-k-way/03-top-k-frequent-stream.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/two-heaps-k-way/k-most-frequent-words

Run it:  python problems/two-heaps-k-way/12-k-most-frequent-words.py
"""


import heapq
from collections import Counter

def top_k_words(words, k):
    counts = Counter(words)
    # best first: higher count, then alphabetical; only k candidates are kept in the heap
    return heapq.nsmallest(k, counts, key=lambda w: (-counts[w], w))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(top_k_words(["red", "blue", "red", "green", "blue", "red"], 2), ['red', 'blue'])
    check(top_k_words(["b", "a", "c", "a", "b", "c"], 2), ['a', 'b'])
    check(top_k_words(["solo"], 1), ['solo'])
