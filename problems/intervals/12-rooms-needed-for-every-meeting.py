"""
Rooms Needed for Every Meeting (medium) · patterns: min-heap, sweep-line, sorting

Given a list of meetings as (start, end) pairs, return the smallest number
of rooms that lets every meeting take place. A meeting occupies its room
from start up to but not including end, so a meeting that ends at 10 frees
its room for one that starts at 10.

Examples:

    Input:  meetings = [(0, 30), (5, 10), (15, 20)]
    Output: 2
    Why:    the long meeting overlaps both short ones, but the short ones never overlap each other

    Input:  meetings = [(7, 10), (2, 4)]
    Output: 1

    Input:  meetings = [(1, 5), (5, 9), (9, 12)]
    Output: 1
    Why:    edge case, back-to-back meetings share one room because the end time is exclusive

Approach:
    Sorting by start time processes meetings in the order a building manager
    would see them arrive. A min-heap holds one end time per room, so its
    top is the room that frees up first. If that room is free by the time
    the new meeting starts, the meeting takes it, and heapreplace swaps the
    old end time for the new one in a single step; if even that room is
    still busy, every room is, and a new one opens. The heap never shrinks,
    so its final size is the peak number of rooms in use at once. The same
    answer comes from a sweep over sorted starts and sorted ends with two
    pointers. Sorting is O(n log n) and each heap step is O(log n), so time
    is O(n log n) and space is O(n).

The lesson behind it: Meeting Rooms
    https://bytepatterns.com/learn/intervals/meeting-rooms
    python intervals/04-meeting-rooms.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/intervals/rooms-needed-for-every-meeting

Run it:  python problems/intervals/12-rooms-needed-for-every-meeting.py
"""


import heapq

def rooms_needed(meetings):
    ends = []                                  # end time of each room in use, earliest on top
    for start, end in sorted(meetings):
        if ends and ends[0] <= start:          # the room freeing first is already free
            heapq.heapreplace(ends, end)
        else:
            heapq.heappush(ends, end)          # every room is busy: open another
    return len(ends)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(rooms_needed([(0, 30), (5, 10), (15, 20)]), 2)
    check(rooms_needed([(7, 10), (2, 4)]), 1)
    check(rooms_needed([(1, 5), (5, 9), (9, 12)]), 1)
