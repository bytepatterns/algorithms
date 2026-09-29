"""
Mutual Follow Pairs (easy) · patterns: adjacency-set, directed-graph

A social app stores who follows whom as a list of pairs [a, b], meaning
person a follows person b, with people numbered 0 to n - 1. The list may
contain the same pair more than once, and nobody follows themselves. Return
how many unordered pairs of people follow each other.

Examples:

    Input:  n = 4, follows = [[0, 1], [1, 0], [1, 2], [2, 3], [3, 2], [0, 2]]
    Output: 2
    Why:    0 and 1, and 2 and 3; 1 follows 2 but not the other way round

    Input:  n = 3, follows = [[0, 1], [0, 1], [1, 0]]
    Output: 1
    Why:    the repeated pair still describes one mutual pair

    Input:  n = 2, follows = []
    Output: 0
    Why:    edge case, nobody follows anyone

Approach:
    Storing each person's follows as a set gives an adjacency list that
    doubles as a fast edge test, which is the one question this problem
    keeps asking. The sets also absorb repeated pairs, so a duplicate can
    never be counted twice. Every mutual pair is seen twice, once from each
    side, and the a < b test keeps exactly one of those sightings. Time is
    O(n + m) on average for m follow pairs, and space is O(n + m).

The lesson behind it: List vs Matrix
    https://bytepatterns.com/learn/graphs/adjacency-representations
    python graphs/02-adjacency-representations.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/mutual-follow-pairs

Run it:  python problems/graphs/13-mutual-follow-pairs.py
"""


def mutual_pairs(n, follows):
    adj = [set() for _ in range(n)]       # adjacency sets: fast edge tests
    for a, b in follows:
        adj[a].add(b)
    count = 0
    for a in range(n):
        for b in adj[a]:
            if a < b and a in adj[b]:     # a < b counts each pair once
                count += 1
    return count


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(mutual_pairs(4, [[0, 1], [1, 0], [1, 2], [2, 3], [3, 2], [0, 2]]), 2)
    check(mutual_pairs(3, [[0, 1], [0, 1], [1, 0]]), 1)
    check(mutual_pairs(2, []), 0)
