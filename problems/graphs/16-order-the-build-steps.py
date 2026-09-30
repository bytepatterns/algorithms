"""
Order the Build Steps (easy) · patterns: topological-sort, indegree

A build has n steps numbered 0 to n - 1, and deps lists pairs [a, b] meaning
step a must finish before step b starts. Return an order that runs every
step after all of its prerequisites. If several orders are valid, any of
them is accepted. If the dependencies loop so that no order exists, return
an empty list.

Examples:

    Input:  n = 4, deps = [[0, 1], [0, 2], [1, 3], [2, 3]]
    Output: [0, 1, 2, 3]
    Why:    0 goes first, 1 and 2 only need 0, and 3 waits for both (running 2 before 1 is valid too)

    Input:  n = 3, deps = [[0, 1], [1, 2], [2, 0]]
    Output: []
    Why:    each step waits on another step in a loop, so none can ever start

    Input:  n = 3, deps = []
    Output: [0, 1, 2]
    Why:    edge case, with no dependencies every order works

Approach:
    This is Kahn's topological sort. A step's in-degree is the number of
    prerequisites it is still waiting for, so the steps with in-degree zero
    are exactly the ones that can run now. Running one removes its outgoing
    edges, which may free more steps, and a queue feeds them into the order
    as they become ready. Steps on a loop never reach in-degree zero, so
    they never enter the order, and a short order is the signal that no
    valid order exists. Every step and dependency is handled once, so time
    is O(n + m) for m dependencies, and space is O(n + m).

The lesson behind it: Topological Sort
    https://bytepatterns.com/learn/graphs/topological-sort
    python graphs/08-topological-sort.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/order-the-build-steps

Run it:  python problems/graphs/16-order-the-build-steps.py
"""


from collections import deque

def build_order(n, deps):
    after = [[] for _ in range(n)]
    waiting = [0] * n                     # in-degree: prerequisites still pending
    for a, b in deps:
        after[a].append(b)
        waiting[b] += 1
    ready = deque(i for i in range(n) if waiting[i] == 0)
    order = []
    while ready:
        step = ready.popleft()
        order.append(step)
        for nxt in after[step]:
            waiting[nxt] -= 1
            if waiting[nxt] == 0:         # its last prerequisite just ran
                ready.append(nxt)
    return order if len(order) == n else []   # short order: a loop blocked the rest


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(build_order(4, [[0, 1], [0, 2], [1, 3], [2, 3]]), [0, 1, 2, 3])
    check(build_order(3, [[0, 1], [1, 2], [2, 0]]), [])
    check(build_order(3, []), [0, 1, 2])
