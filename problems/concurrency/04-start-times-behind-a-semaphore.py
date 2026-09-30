"""
Start Times Behind a Semaphore (medium) · patterns: min-heap, event-simulation

A download service lets at most permits jobs run at once, guarded by a
counting semaphore. Jobs arrive as (arrive, duration) pairs, sorted by
arrival time, and the semaphore is fair: blocked jobs acquire a permit in
the order they arrived. A permit released at time t can be used by a job
starting at time t. Return the time at which each job starts running. There
are up to 100,000 jobs.

Examples:

    Input:  permits = 2, jobs = [(0, 5), (1, 3), (2, 4), (3, 1)]
    Output: [0, 1, 4, 5]
    Why:    the third job waits for the permit freed at 4, the fourth for the one freed at 5

    Input:  permits = 1, jobs = [(0, 2), (0, 2), (10, 1)]
    Output: [0, 2, 10]
    Why:    the last job arrives after everything has finished, so it starts at once

    Input:  permits = 3, jobs = [(0, 7), (0, 7)]
    Output: [0, 0]
    Why:    edge case, fewer jobs than permits means nobody ever waits

Approach:
    A counting semaphore is a pool of identical permits, so a waiting job
    does not care which permit it gets, only when the first one comes free.
    A min-heap of release times answers that directly: while there are spare
    permits a job starts on arrival, and otherwise it takes the earliest
    release, or its own arrival if that is later. Fairness comes for free
    because jobs are handled in arrival order and the earliest release only
    ever moves forward, so start times never go backwards. Each job is
    pushed and popped at most once, so time is O(n log p) for n jobs and p
    permits, and space is O(p).

The lesson behind it: Semaphores
    https://bytepatterns.com/learn/concurrency/semaphores
    python concurrency/09-semaphores.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/concurrency/start-times-behind-a-semaphore

Run it:  python problems/concurrency/04-start-times-behind-a-semaphore.py
"""


import heapq

def start_times(permits, jobs):
    busy, starts = [], []                  # min-heap of permit release times
    for arrive, duration in jobs:
        if len(busy) < permits:
            start = arrive                 # a permit is free right away
        else:
            start = max(arrive, heapq.heappop(busy))   # wait for the first release
        heapq.heappush(busy, start + duration)
        starts.append(start)
    return starts


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(start_times(2, [(0, 5), (1, 3), (2, 4), (3, 1)]), [0, 1, 4, 5])
    check(start_times(1, [(0, 2), (0, 2), (10, 1)]), [0, 2, 10])
    check(start_times(3, [(0, 7), (0, 7)]), [0, 0])
