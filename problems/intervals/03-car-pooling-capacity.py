"""
Car Pooling Capacity (medium) · patterns: intervals, sweep-line

A car drives east along a straight road and can never turn back. Each trip
is (riders, start, end): that many people board at start and leave at end.
Given a seat capacity, decide whether every trip can be served without ever
exceeding it. Passengers leaving at a point free their seats before anyone
boarding at that same point sits down.

Examples:

    Input:  trips = [(2, 1, 5), (3, 3, 7)], capacity = 4
    Output: False
    Why:    between 3 and 5 both groups are aboard, needing 5 seats

    Input:  trips = [(2, 1, 5), (3, 5, 7)], capacity = 3
    Output: True
    Why:    the first group leaves at 5 exactly as the second boards

    Input:  trips = [], capacity = 0
    Output: True
    Why:    edge case, no trips can never overflow

Approach:
    This is a sweep line over positions rather than a comparison of
    intervals. Each trip becomes a +riders event at its start and a -riders
    event at its end; the running sum after each event is the exact
    occupancy on that stretch of road. Sorting the pairs directly puts a
    negative delta before a positive one at the same position, which is
    precisely the "leave before board" rule. Time is O(n log n) for the
    sort, space O(n) for the events.

The lesson behind it: Meeting Rooms
    https://bytepatterns.com/learn/intervals/meeting-rooms
    python intervals/04-meeting-rooms.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/intervals/car-pooling-capacity

Run it:  python problems/intervals/03-car-pooling-capacity.py
"""


def can_carry(trips, capacity):
    events = []
    for riders, start, end in trips:
        events.append((start, riders))     # board
        events.append((end, -riders))      # alight; negative sorts first on ties
    events.sort()
    onboard = 0
    for _, delta in events:
        onboard += delta
        if onboard > capacity:
            return False
    return True


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(can_carry([(2, 1, 5), (3, 3, 7)], 4), False)
    check(can_carry([(2, 1, 5), (3, 5, 7)], 3), True)
    check(can_carry([], 0), True)
