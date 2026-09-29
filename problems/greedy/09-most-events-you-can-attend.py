"""
Most Events You Can Attend (medium) · patterns: greedy, min-heap, earliest-deadline

A conference lists events as [startDay, endDay], inclusive. You can attend
an event on any single day within its range, and you can attend at most one
event per day. Return the largest number of events you can attend.

Examples:

    Input:  events = [[1, 2], [2, 3], [3, 4], [1, 2]]
    Output: 4
    Why:    days 1 and 2 go to the two [1, 2] events, then [2, 3] on day 3 and [3, 4] on day 4

    Input:  events = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]
    Output: 4

    Input:  events = [[1, 1], [1, 1], [1, 1]]
    Output: 1
    Why:    edge case, three events compete for the same single day

Approach:
    On each day, the right event to attend is the open one with the earliest
    end: if an optimal plan attended something else today, swapping in the
    earliest-ending event keeps the plan valid, because that event could
    only have been attended on days that the other one also covers. A
    min-heap of end days holds the events that have started, so the earliest
    end is always on top, and expired events are discarded as they surface.
    Sorting by start day lets the walk add events as their first day arrives
    and skip idle stretches of days entirely. Each event is pushed and
    popped once, so time is O(n log n) and space is O(n).

The lesson behind it: Interval Scheduling
    https://bytepatterns.com/learn/greedy/interval-scheduling
    python greedy/02-interval-scheduling.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/greedy/most-events-you-can-attend

Run it:  python problems/greedy/09-most-events-you-can-attend.py
"""


import heapq

def most_events(events):
    events = sorted(events)
    ends, i, n, day, attended = [], 0, len(events), 0, 0
    while i < n or ends:
        if not ends:
            day = max(day, events[i][0])       # skip idle days
        while i < n and events[i][0] <= day:
            heapq.heappush(ends, events[i][1]); i += 1
        while ends and ends[0] < day:          # already over
            heapq.heappop(ends)
        if ends:
            heapq.heappop(ends)                # attend the one ending soonest
            attended += 1; day += 1
    return attended


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(most_events([[1, 2], [2, 3], [3, 4], [1, 2]]), 4)
    check(most_events([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]), 4)
    check(most_events([[1, 1], [1, 1], [1, 1]]), 1)
