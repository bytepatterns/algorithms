"""
Earliest Moment All Connected (medium) · patterns: union-find, sort-by-time

A network has n machines numbered 0 to n minus 1. A log lists cable
installations as [time, a, b], meaning machines a and b were linked at that
time, and the log is not in time order. Messages travel over any chain of
cables. Return the earliest time at which every machine can reach every
other machine, or -1 if that never happens.

Examples:

    Input:  n = 5, logs = [[20, 0, 1], [3, 3, 4], [5, 1, 2], [9, 2, 3], [12, 0, 3]]
    Output: 12
    Why:    by time 9 the groups are {0} and {1, 2, 3, 4}; the cable at 12 joins them

    Input:  n = 4, logs = [[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]]
    Output: 3

    Input:  n = 3, logs = [[1, 0, 1]]
    Output: -1
    Why:    edge case, machine 2 is never linked to anything

Approach:
    Connectivity only grows as cables arrive, so replaying the log in time
    order and asking after each cable whether one group remains finds the
    earliest moment. A disjoint-set structure tracks the groups: a cable
    between machines with different roots merges two groups and lowers the
    count by one, while a cable inside a group changes nothing. The first
    cable that brings the count to one gives the answer, and running out of
    cables first means the network never becomes whole. Sorting costs O(m
    log m) for m cables, the merges cost O(m times the inverse Ackermann
    function) with path halving, and space is O(n).

The lesson behind it: Disjoint Sets Basics
    https://bytepatterns.com/learn/union-find/disjoint-sets-basics
    python union-find/01-disjoint-sets-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/union-find/earliest-moment-all-connected

Run it:  python problems/union-find/07-earliest-moment-all-connected.py
"""


def earliest_all_connected(n, logs):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]    # path halving
            x = parent[x]
        return x
    groups = n
    for t, a, b in sorted(logs):             # replay in time order
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            groups -= 1
            if groups == 1:
                return t
    return -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(earliest_all_connected(5, [[20, 0, 1], [3, 3, 4], [5, 1, 2], [9, 2, 3], [12, 0, 3]]), 12)
    check(earliest_all_connected(4, [[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]]), 3)
    check(earliest_all_connected(3, [[1, 0, 1]]), -1)
