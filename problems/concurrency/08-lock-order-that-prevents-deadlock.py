"""
Lock Order That Prevents Deadlock (medium) · patterns: lock-ordering, topological-sort, min-heap

A service has several code paths, and each one takes a list of locks in the
order given, holding every earlier lock while it takes the next. Deadlock is
impossible if there is one global lock order that every path already
follows. Given the paths, return such an order as a list of lock names,
choosing the alphabetically smallest free lock at each position so the
answer is unique. If the paths contradict each other, for example one takes
a before b and another takes b before a, no order exists: return None. There
are up to 10,000 locks.

Examples:

    Input:  [["accounts", "ledger"], ["ledger", "audit"], ["accounts", "audit"]]
    Output: ['accounts', 'ledger', 'audit']
    Why:    ledger must come before audit, so audit waits even though it is alphabetically first

    Input:  [["a", "b"], ["b", "c"], ["c", "a"]]
    Output: None
    Why:    the three paths form a cycle, which is exactly the shape a deadlock needs

    Input:  [["cache"], ["db", "cache"], ["log"]]
    Output: ['db', 'cache', 'log']
    Why:    edge case, a path with one lock adds a lock but no ordering rule

Approach:
    Two paths can deadlock only if they take the same two locks in opposite
    orders, directly or through a chain, so the question is whether the
    before-rules the paths imply are free of cycles. Each consecutive pair
    in a path becomes an edge, with a set to avoid counting the same rule
    twice, and Kahn's algorithm peels off locks that have no remaining
    predecessors. Using a min-heap for the free locks makes the order
    deterministic, which is why audit waits behind ledger in the first
    example even though it sorts first. If a cycle exists, its locks never
    reach zero incoming rules and the output comes up short, which is the
    signal to return None. Time is O(E + L log L) for E rules and L locks,
    and space is O(E + L).

The lesson behind it: Deadlock
    https://bytepatterns.com/learn/concurrency/deadlock
    python concurrency/04-deadlock.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/concurrency/lock-order-that-prevents-deadlock

Run it:  python problems/concurrency/08-lock-order-that-prevents-deadlock.py
"""


import heapq
from collections import defaultdict

def lock_order(paths):
    after = defaultdict(set)               # lock -> locks that must come after it
    indeg = {}
    for locks in paths:
        for lock in locks:
            indeg.setdefault(lock, 0)
        for a, b in zip(locks, locks[1:]):
            if b not in after[a]:
                after[a].add(b)
                indeg[b] += 1
    ready = [lock for lock, d in indeg.items() if d == 0]
    heapq.heapify(ready)                   # smallest free lock first
    order = []
    while ready:
        lock = heapq.heappop(ready)
        order.append(lock)
        for nxt in after[lock]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                heapq.heappush(ready, nxt)
    return order if len(order) == len(indeg) else None   # short means a cycle


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(lock_order([["accounts", "ledger"], ["ledger", "audit"], ["accounts", "audit"]]), ['accounts', 'ledger', 'audit'])
    check(lock_order([["a", "b"], ["b", "c"], ["c", "a"]]), None)
    check(lock_order([["cache"], ["db", "cache"], ["log"]]), ['db', 'cache', 'log'])
