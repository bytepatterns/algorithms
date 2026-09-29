"""
Nearest Two Words (easy) · patterns: single-pass, linear-scan

A search tool ranks a document higher when two query words appear close
together. Given a list of words and two different words a and b that each
appear at least once, return the smallest distance between a position
holding a and a position holding b. The distance between positions i and j
is the absolute value of i minus j.

Examples:

    Input:  words = ["cat", "dog", "fox", "cat", "owl", "dog"], a = "cat", b = "dog"
    Output: 1
    Why:    the cat at 0 and the dog at 1 are neighbours

    Input:  words = ["red", "sky", "sky", "sky", "blue"], a = "blue", b = "red"
    Output: 4
    Why:    each word appears once, at opposite ends

    Input:  words = ["up", "down"], a = "up", b = "down"
    Output: 1
    Why:    edge case, the shortest list that can hold both words

Approach:
    For a pair of positions, the later one is met during the scan while the
    earlier one is still stored, as long as no copy of the same word came
    between them. If another copy did come between, that copy is closer to
    the later position, so the skipped pair could never have been the best.
    Checking the distance only when one of the two words is seen keeps the
    pass cheap. Time is O(n) and space is O(1).

The lesson behind it: Linear Search
    https://bytepatterns.com/learn/searching/linear-search
    python searching/01-linear-search.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/searching/nearest-two-words

Run it:  python problems/searching/06-nearest-two-words.py
"""


def nearest_pair(words, a, b):
    last_a = last_b = None           # latest position of each word so far
    best = len(words)
    for i, w in enumerate(words):
        if w == a:
            last_a = i
        elif w == b:
            last_b = i
        else:
            continue                 # other words cannot change the answer
        if last_a is not None and last_b is not None:
            best = min(best, abs(last_a - last_b))
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(nearest_pair(["cat", "dog", "fox", "cat", "owl", "dog"], "cat", "dog"), 1)
    check(nearest_pair(["red", "sky", "sky", "sky", "blue"], "blue", "red"), 4)
    check(nearest_pair(["up", "down"], "up", "down"), 1)
