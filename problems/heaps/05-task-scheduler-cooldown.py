"""
Task Scheduler Cooldown (medium) · patterns: heap, greedy

A processor runs one task per time slot. Two runs of the same task must be
separated by at least gap slots, during which the processor may run a
different task or sit idle. Given the list of tasks to run in any order,
return the smallest number of slots — busy and idle together — needed to
finish them all.

Examples:

    Input:  tasks = ["a", "a", "a", "b", "b", "b"], gap = 2
    Output: 8
    Why:    a b _ a b _ a b fills six tasks into eight slots

    Input:  tasks = ["a", "a", "a"], gap = 2
    Output: 7
    Why:    a _ _ a _ _ a — nothing else exists to fill the waits

    Input:  tasks = ["a", "b", "c"], gap = 0
    Output: 3
    Why:    edge case, no cooldown means no idling

Approach:
    Greedily scheduling the most frequent remaining task first is what keeps
    the busiest task from bunching up at the end, and a max-heap on
    remaining counts makes that choice cheap. One round is exactly gap + 1
    slots, which is the shortest window in which a task may repeat, so
    filling a round with distinct tasks is always legal. A round that runs
    out of distinct tasks pays idle slots, except on the final round where
    the schedule simply ends. Time is O(n log d) for d distinct tasks, space
    O(d).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/heaps/task-scheduler-cooldown

Run it:  python problems/heaps/05-task-scheduler-cooldown.py
"""


import heapq
from collections import Counter

def total_slots(tasks, gap):
    heap = [-n for n in Counter(tasks).values()]
    heapq.heapify(heap)                        # max-heap on remaining runs
    time = 0
    while heap:
        held = []
        for _ in range(gap + 1):               # one cooldown-length round
            if heap:
                held.append(heapq.heappop(heap) + 1)
            time += 1
            if not heap and not any(held):     # last round: stop, do not idle
                break
        for n in held:
            if n:
                heapq.heappush(heap, n)
    return time


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(total_slots(["a", "a", "a", "b", "b", "b"], 2), 8)
    check(total_slots(["a", "a", "a"], 2), 7)
    check(total_slots(["a", "b", "c"], 0), 3)
