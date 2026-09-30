"""
Least-Connections Load Balancer (medium) · patterns: least-connections, min-heap, event-simulation

A load balancer routes each request to the server with the fewest requests
in flight, breaking ties by the order the servers are listed. Requests
arrive as (arrive, duration) pairs sorted by arrival time, and a request
that finishes at time t has already left before one arriving at time t is
routed. Return the server chosen for each request, and the peak number of
requests each server held at once. There are up to 100,000 requests and a
handful of servers.

Examples:

    Input:  servers = ["a", "b"], requests = [(0, 10), (1, 2), (2, 5), (3, 1), (4, 1)]
    Output: (['a', 'b', 'a', 'b', 'b'], {'a': 2, 'b': 1})
    Why:    the long request pins a; b keeps emptying just in time for the next short one

    Input:  servers = ["a", "b", "c"], requests = [(0, 1), (1, 1), (2, 1)]
    Output: (['a', 'a', 'a'], {'a': 1, 'b': 0, 'c': 0})
    Why:    each request is gone before the next arrives, so the tie always goes to a

    Input:  servers = ["x"], requests = [(0, 5), (1, 5), (2, 5)]
    Output: (['x', 'x', 'x'], {'x': 3})
    Why:    edge case, with one server the balancer has no choice

Approach:
    Least-connections routing only needs each server's current in-flight
    count, and the counts only change when a request arrives or finishes.
    Arrivals are processed in order, and before each one a min-heap of end
    times releases every request finished by then, which is what makes the
    "finishes at t leaves before t" rule hold. The pick is a min over the
    servers with the listed order as the tie-breaker, since min returns the
    first of equal keys. Unlike round robin, this adapts to uneven request
    lengths, which the first example shows when one long request keeps
    server a busy. Each request is pushed and popped once and the pick scans
    s servers, so time is O(n (log n + s)) and space is O(n + s).

The lesson behind it: Load Balancing
    https://bytepatterns.com/learn/system-design/load-balancing

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/system-design/least-connections-load-balancer

Run it:  python problems/system-design/05-least-connections-load-balancer.py
"""


import heapq

def least_connections(servers, requests):
    active = {s: 0 for s in servers}
    peak = {s: 0 for s in servers}
    ends, picks = [], []                   # ends: min-heap of (end time, server)
    for arrive, duration in requests:
        while ends and ends[0][0] <= arrive:          # finished requests leave first
            active[heapq.heappop(ends)[1]] -= 1
        best = min(servers, key=lambda s: active[s])  # ties go to the earlier server
        active[best] += 1
        peak[best] = max(peak[best], active[best])
        heapq.heappush(ends, (arrive + duration, best))
        picks.append(best)
    return picks, peak


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(least_connections(["a", "b"], [(0, 10), (1, 2), (2, 5), (3, 1), (4, 1)]), (['a', 'b', 'a', 'b', 'b'], {'a': 2, 'b': 1}))
    check(least_connections(["a", "b", "c"], [(0, 1), (1, 1), (2, 1)]), (['a', 'a', 'a'], {'a': 1, 'b': 0, 'c': 0}))
    check(least_connections(["x"], [(0, 5), (1, 5), (2, 5)]), (['x', 'x', 'x'], {'x': 3}))
