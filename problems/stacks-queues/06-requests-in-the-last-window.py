"""
Requests in the Last Window (easy) · patterns: queue, sliding-window

A service logs the arrival time of every request in milliseconds, and the
times come in non-decreasing order. For each request, report how many
requests, itself included, arrived during the last w milliseconds, that is,
at a time strictly greater than its own time minus w. Return one count per
request.

Examples:

    Input:  times = [0, 400, 900, 1000, 1400], w = 1000
    Output: [1, 2, 3, 3, 3]
    Why:    at 1000 the request from time 0 is exactly w old and no longer counts

    Input:  times = [5, 5, 5], w = 1
    Output: [1, 2, 3]
    Why:    equal times all fall inside the same window

    Input:  times = [], w = 50
    Output: []
    Why:    edge case, no requests

Approach:
    Because times never decrease, requests expire in the same order they
    arrived, so the requests still inside the window always form a run at
    the front of a queue. Each arrival joins at the back, and expired times
    leave from the front until the oldest remaining one is recent enough.
    Every time is added once and removed at most once, so the total work is
    linear even when a single arrival removes many. Time is O(n) and space
    is O(n), reached when every request falls inside one window.

The lesson behind it: Queue Basics
    https://bytepatterns.com/learn/stacks-queues/queue-basics
    python stacks-queues/03-queue-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/requests-in-the-last-window

Run it:  python problems/stacks-queues/06-requests-in-the-last-window.py
"""


from collections import deque

def recent_counts(times, w):
    window, out = deque(), []
    for t in times:
        window.append(t)
        while window[0] <= t - w:     # too old now, and for every later arrival
            window.popleft()
        out.append(len(window))
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(recent_counts([0, 400, 900, 1000, 1400], 1000), [1, 2, 3, 3, 3])
    check(recent_counts([5, 5, 5], 1), [1, 2, 3])
    check(recent_counts([], 50), [])
