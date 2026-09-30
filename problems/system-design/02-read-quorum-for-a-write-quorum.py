"""
Read Quorum for a Write Quorum (easy) · patterns: quorum, pigeonhole

A replicated key-value store keeps every key on n replicas. A write succeeds
once w replicas acknowledge it, and a read asks r replicas and keeps the
newest version it sees. A read is guaranteed to see the latest successful
write only if every possible read set shares at least one replica with every
possible write set. Given n and w, return the smallest such r, together with
how many replicas can be down while both reads and writes can still succeed.

Examples:

    Input:  n = 3, w = 2
    Output: (2, 1)
    Why:    any 2 of 3 overlap any other 2 of 3, and 1 replica can be lost

    Input:  n = 5, w = 3
    Output: (3, 2)

    Input:  n = 3, w = 3
    Output: (1, 0)
    Why:    edge case, every write reaches everyone, so one replica is enough to read, but none may fail

Approach:
    There are n - w replicas that a given write never reached, so a read of
    that many replicas can miss the write entirely, while one more forces an
    overlap by the pigeonhole principle. That makes the smallest safe read
    quorum n - w + 1, the familiar r + w > n rule. Availability then follows
    from counting: a write needs w live replicas and a read needs r, so the
    system keeps serving both as long as no more than n - max(r, w) replicas
    are down. Raising w buys cheaper reads at the cost of fewer tolerated
    failures, which is the trade-off the examples show. Time and space are
    O(1).

The lesson behind it: Consistency and CAP
    https://bytepatterns.com/learn/system-design/consistency-and-cap

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/system-design/read-quorum-for-a-write-quorum

Run it:  python problems/system-design/02-read-quorum-for-a-write-quorum.py
"""


def quorum_plan(n, w):
    r = n - w + 1                          # smallest read set that must meet every write set
    tolerate = n - max(r, w)               # replicas that can be down with both still working
    return r, tolerate


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(quorum_plan(3, 2), (2, 1))
    check(quorum_plan(5, 3), (3, 2))
    check(quorum_plan(3, 3), (1, 0))
