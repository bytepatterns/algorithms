"""
Out Of Place Count (easy) · patterns: sorting, pairwise-comparison

Students stand in a line, each described by a height. They were supposed to
be lined up from shortest to tallest. Count the positions holding a student
whose height differs from the height that should be standing there. Equal
heights are interchangeable, so a position holding the right height is never
counted.

Examples:

    Input:  heights = [1, 1, 4, 2, 1, 3]
    Output: 3
    Why:    the correct line is 1 1 1 2 3 4, and three positions disagree

    Input:  heights = [5, 4, 3, 2, 1]
    Output: 4
    Why:    only the middle student happens to already stand correctly

    Input:  heights = [1, 2, 3]
    Output: 0
    Why:    edge case, an already correct line has nothing out of place

Approach:
    The target line is just the input sorted, so the whole task is producing
    that copy and comparing position by position. Sorting a copy rather than
    the input itself matters: sorting in place would overwrite the line
    being judged and the count would always come out as zero. Comparing
    heights rather than students is enough, because two students of equal
    height are interchangeable and a position holding the right height is
    correct whoever is standing there. Time is O(n log n) for the sort, and
    space is O(n) for the copy.

The lesson behind it: Sorting Basics
    https://bytepatterns.com/learn/sorting/sorting-basics
    python sorting/01-sorting-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/out-of-place-count

Run it:  python problems/sorting/01-out-of-place-count.py
"""


def count_out_of_place(heights):
    target = sorted(heights)         # a COPY, so the original line survives
    mismatches = 0
    for standing, expected in zip(heights, target):
        if standing != expected:     # this position holds the wrong height
            mismatches += 1
    return mismatches


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_out_of_place([1, 1, 4, 2, 1, 3]), 3)
    check(count_out_of_place([5, 4, 3, 2, 1]), 4)
    check(count_out_of_place([1, 2, 3]), 0)
