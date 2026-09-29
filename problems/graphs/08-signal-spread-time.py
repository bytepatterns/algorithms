"""
Signal Spread Time (medium) · patterns: dijkstra, shortest-path, min-heap

A network has n relays numbered from 0 and a list of one-way links (u, v,
t): a signal at relay u reaches relay v after t minutes, where t is 0 or
more. A signal leaves relay source at minute 0 and every relay forwards it
along all of its links the moment it arrives. Return the minute at which the
last relay receives the signal, or -1 if some relay never receives it.

Examples:

    Input:  n = 4, source = 0
            links = [(0, 1, 2), (0, 2, 5), (1, 2, 1), (2, 3, 3)]
    Output: 6
    Why:    relay 2 hears it at minute 3 through relay 1, so relay 3 hears it at 6

    Input:  n = 3, links = [(0, 1, 4)], source = 0
    Output: -1
    Why:    nothing ever links to relay 2

    Input:  n = 1, links = [], source = 0
    Output: 0
    Why:    edge case, the source already has the signal

Approach:
    The arrival time at each relay is its shortest-path distance from the
    source, and with non-negative link times Dijkstra's algorithm finds all
    of them. A min-heap always hands back the earliest unsettled arrival,
    which is final because any other route would pass through a later relay
    first. Stale heap entries for relays already settled are skipped. If
    fewer than n relays get settled the answer is -1, otherwise it is the
    latest arrival. Time is O((n + m) log m) for m links, and space is O(n +
    m).

The lesson behind it: Dijkstra's Algorithm
    https://bytepatterns.com/learn/graphs/dijkstra-intro
    python graphs/07-dijkstra-intro.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/signal-spread-time

Run it:  python problems/graphs/08-signal-spread-time.py
"""


import heapq
def spread_time(n, links, source):
    graph = [[] for _ in range(n)]
    for u, v, t in links: graph[u].append((v, t))
    arrival = {}                          # relay -> final arrival minute
    heap = [(0, source)]
    while heap:
        time, relay = heapq.heappop(heap)
        if relay in arrival: continue     # a quicker route already settled it
        arrival[relay] = time
        for nxt, t in graph[relay]:
            if nxt not in arrival: heapq.heappush(heap, (time + t, nxt))
    return max(arrival.values()) if len(arrival) == n else -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(spread_time(4, [(0, 1, 2), (0, 2, 5), (1, 2, 1), (2, 3, 3)], 0), 6)
    check(spread_time(3, [(0, 1, 4)], 0), -1)
    check(spread_time(1, [], 0), 0)
