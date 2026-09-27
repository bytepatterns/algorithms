"""
Task Scheduler: Same greedy pick, but now the loser has to sit out a cooldown.

Tasks run one per second, and the same task cannot repeat until the cooldown
has passed. Always run whichever task has the most runs left — the scarce
resource is time, and that task needs the most of it.

A task that has just run goes into a waiting list stamped with the moment it
becomes legal again, then rejoins the heap.

Lesson 7 of Heaps, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/heaps/task-scheduler

Run it:  python heaps/07-task-scheduler.py
"""


import heapq
from collections import Counter

def schedule(tasks, cooldown):
    heap = [-n for n in Counter(tasks).values()]
    heapq.heapify(heap)                            # the busiest task goes first
    time, waiting = 0, []                          # waiting: (ready_at, runs_left)
    while heap or waiting:
        time += 1
        if waiting and waiting[0][0] <= time:
            heapq.heappush(heap, waiting.pop(0)[1])   # its cooldown expired
        if heap:
            left = heapq.heappop(heap) + 1            # run it once
            if left: waiting.append((time + cooldown + 1, left))
    return time                                    # idle seconds are counted too


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(schedule(["a", "a", "a", "b", "b", "c"], 2), 7)
    check(schedule(["a", "b", "c", "d"], 2), 4)  # enough variety, no idling
