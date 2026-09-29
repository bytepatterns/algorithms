"""
Sentence Segmentation (medium) · patterns: bottom-up-dp, hash-set

Given a string with no spaces and a dictionary of words, decide whether the
string can be cut into a sequence of dictionary words placed end to end.
Words may be reused as often as needed, and every character must belong to
exactly one word. Return true when such a cut exists.

Examples:

    Input:  text = applepen, words = [apple, pen]
    Output: True
    Why:    the cut apple + pen uses every character

    Input:  text = applepin, words = [apple, pen]
    Output: False
    Why:    the tail pin is not a dictionary word

    Input:  text = "", words = [apple]
    Output: True
    Why:    edge case, an empty string is already fully covered by zero words

Approach:
    A flag per position records whether the prefix ending there can be built
    entirely from dictionary words, with position zero true because the
    empty prefix needs nothing. Each position is confirmed by finding an
    earlier confirmed position whose following piece is a word, which reuses
    answers instead of re-exploring cuts. Storing the dictionary in a set
    keeps each piece lookup constant on average. Time is O(L squared) piece
    checks for a string of length L, and space is O(L) plus the dictionary.

The lesson behind it: Word Break
    https://bytepatterns.com/learn/dynamic-programming/word-break-dp
    python dynamic-programming/18-word-break-dp.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/sentence-segmentation

Run it:  python problems/dynamic-programming/03-sentence-segmentation.py
"""


def can_segment(text, words):
    vocab = set(words)
    covered = [False] * (len(text) + 1)
    covered[0] = True                # the empty prefix needs no words at all
    for end in range(1, len(text) + 1):
        for start in range(end):
            # a cut works when the prefix is covered and the piece is a word
            if covered[start] and text[start:end] in vocab:
                covered[end] = True
                break
    return covered[-1]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(can_segment("applepen", ["apple", "pen"]), True)
    check(can_segment("applepin", ["apple", "pen"]), False)
    check(can_segment("", ["apple"]), True)
