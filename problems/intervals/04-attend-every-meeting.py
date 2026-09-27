"""
Attend Every Meeting (easy) · patterns: intervals, sorting

A calendar lists meetings as [start, end] pairs in no particular order.
Decide whether one person can sit through every meeting from start to
finish. A meeting that ends exactly when another begins is fine, because the
person can walk straight from one to the next.

Examples:

    Input:  meetings = [[0, 30], [5, 10], [15, 20]]
    Output: False
    Why:    the long meeting swallows both of the others

    Input:  meetings = [[7, 10], [2, 4], [4, 7]]
    Output: True
    Why:    in time order the meetings only touch at their ends

    Input:  meetings = []
    Output: True
    Why:    edge case, an empty calendar has nothing to clash

Approach:
    Once the meetings are sorted by start time, the only way two of them can
    overlap is for some meeting to begin before its immediate predecessor
    ends: if neighbours in that order never overlap, their end times are
    also in order, so nothing further back can reach forward past them. That
    turns a pairwise question into one comparison per adjacent pair, with a
    strict less-than so that touching meetings pass. Time is O(n log n) for
    the sort, and space is O(n) for the sorted copy.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/intervals/attend-every-meeting

Run it:  python problems/intervals/04-attend-every-meeting.py
"""


def can_attend_all(meetings):
    ordered = sorted(meetings)                  # by start time
    for prev, cur in zip(ordered, ordered[1:]):
        if cur[0] < prev[1]:                    # starts before the last one ends
            return False
    return True


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(can_attend_all([[0, 30], [5, 10], [15, 20]]), False)
    check(can_attend_all([[7, 10], [2, 4], [4, 7]]), True)
    check(can_attend_all([]), True)
