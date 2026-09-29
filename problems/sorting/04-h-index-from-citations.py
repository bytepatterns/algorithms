"""
H Index From Citations (medium) · patterns: sorting, counting

A researcher's h-index is the largest number h such that at least h of their
papers have h or more citations each. Given the citation count of every
paper, return the h-index.

Examples:

    Input:  citations = [3, 0, 6, 1, 5]
    Output: 3
    Why:    three papers have at least 3 citations; four papers with 4 or more do not exist

    Input:  citations = [1, 1]
    Output: 1
    Why:    one paper has at least 1 citation, but two papers with 2 or more do not

    Input:  citations = [0]
    Output: 0
    Why:    edge case, an uncited paper gives an h-index of zero

Approach:
    Sorting descending turns the definition into a single comparison per
    paper: at zero-based position i there are i + 1 papers with at least
    this citation count, so the h-index is the last position where the count
    still reaches i + 1. Because the sorted counts only fall while the
    required bar only rises, the test fails once and never recovers — so the
    scan can stop at the first failure. Time is O(n log n) for the sort,
    space O(1) beyond it.

The lesson behind it: Sorting Basics
    https://bytepatterns.com/learn/sorting/sorting-basics
    python sorting/01-sorting-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/h-index-from-citations

Run it:  python problems/sorting/04-h-index-from-citations.py
"""


def h_index(citations):
    citations.sort(reverse=True)         # most cited first
    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:                   # i+1 papers have at least c citations
            h = i + 1
        else:
            break                        # counts fall, the bar rises: no recovery
    return h


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(h_index([3, 0, 6, 1, 5]), 3)
    check(h_index([1, 1]), 1)
    check(h_index([0]), 0)
