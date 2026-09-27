"""
Course Order Feasibility (medium) · patterns: topological-sort, cycle-detection

A programme has n courses numbered from 0, plus a list of pairs where the
pair course, before means that course cannot be taken until before is
finished. Decide whether an order exists that lets a student finish all n
courses. Return true when such an order exists and false when the
requirements contradict each other.

Examples:

    Input:  n = 3, pairs = [[1, 0], [2, 1]]
    Output: True
    Why:    the order 0, 1, 2 satisfies both requirements

    Input:  n = 2, pairs = [[1, 0], [0, 1]]
    Output: False
    Why:    each course waits for the other, so neither can start

    Input:  n = 1, pairs = []
    Output: True
    Why:    edge case, a course with no requirements can always be taken

Approach:
    The requirements form a directed graph, and a valid order exists
    precisely when that graph has no cycle. Peeling off courses whose
    outstanding requirement count has reached zero simulates taking them,
    and releases their dependants one at a time. Any course stuck in a cycle
    never reaches zero, so a shortfall in the finished count proves the
    requirements contradict each other. Time is O(n + p) for n courses and p
    pairs, and space is O(n + p).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/course-order-feasibility

Run it:  python problems/graphs/02-course-order-feasibility.py
"""


from collections import deque
def can_finish(n, pairs):
    graph = [[] for _ in range(n)]   # course -> courses unlocked by it
    waiting = [0] * n                # how many requirements are still open
    for course, before in pairs:
        graph[before].append(course)
        waiting[course] += 1
    ready = deque(c for c in range(n) if waiting[c] == 0)
    done = 0
    while ready:                     # take a course with nothing left to wait for
        c = ready.popleft()
        done += 1
        for nxt in graph[c]:
            waiting[nxt] -= 1
            if waiting[nxt] == 0: ready.append(nxt)
    return done == n                 # leftovers mean a cycle blocked them


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(can_finish(3, [[1, 0], [2, 1]]), True)
    check(can_finish(2, [[1, 0], [0, 1]]), False)
    check(can_finish(1, []), True)
