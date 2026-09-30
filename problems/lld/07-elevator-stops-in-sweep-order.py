"""
Elevator Stops in Sweep Order (medium) · patterns: elevator-sweep, event-simulation

An elevator starts at floor start, heading up, and receives floor requests
as (time, floor) pairs. It moves one floor per time unit and stops take no
time. At every tick it first learns the requests that have arrived by now,
then serves the current floor if it was requested, then decides where to go:
it keeps its direction while any request lies ahead, reverses when all
remaining requests are behind it, and stays put when there are none. Return
the stops as (time, floor) pairs in the order they happen. There are up to
1,000 requests.

Examples:

    Input:  start = 3, requests = [(0, 5), (0, 1), (1, 4), (6, 2)]
    Output: [(1, 4), (2, 5), (6, 1), (7, 2)]
    Why:    it finishes the upward sweep first, and passes floor 2 one tick before it is requested

    Input:  start = 0, requests = [(0, 3), (2, 1), (10, 6)]
    Output: [(3, 3), (5, 1), (15, 6)]
    Why:    floor 1 is requested behind the car, so it waits for the reversal; then the car idles until 10

    Input:  start = 4, requests = [(0, 4)]
    Output: [(0, 4)]
    Why:    edge case, a request for the floor the car is on is served at once

Approach:
    This is the sweep rule most elevator controllers use: keep going while
    there is work ahead and only turn around when there is none, which
    avoids the back and forth a nearest-request rule causes. The controller
    keeps the floor, the direction and a set of pending floors, and every
    tick runs the same three steps in a fixed order: learn new requests,
    serve the current floor, then choose the direction and move. That order
    is what makes the first example pass floor 2 at time 5 and come back for
    it at time 7. When nothing is pending, the clock jumps to the next
    arrival instead of ticking through idle time. With F floors travelled
    over the run and p pending floors, time is O(F × p + r log r) for r
    requests, and space is O(r).

The lesson behind it: Elevator Controller
    https://bytepatterns.com/learn/lld/elevator-controller
    python lld/12-elevator-controller.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/lld/elevator-stops-in-sweep-order

Run it:  python problems/lld/07-elevator-stops-in-sweep-order.py
"""


def elevator_stops(start, requests):
    requests = sorted(requests)
    floor, direction, t, i = start, 1, 0, 0     # direction: 1 up, -1 down
    pending, stops = set(), []
    while i < len(requests) or pending:
        while i < len(requests) and requests[i][0] <= t:
            pending.add(requests[i][1])         # learn what has arrived by now
            i += 1
        if not pending:
            t = requests[i][0]                  # idle: jump to the next request
            continue
        if floor in pending:
            pending.discard(floor)
            stops.append((t, floor))
            if not pending:
                continue
        if not any((f - floor) * direction > 0 for f in pending):
            direction = -direction              # nothing ahead: turn around
        floor += direction
        t += 1
    return stops


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(elevator_stops(3, [(0, 5), (0, 1), (1, 4), (6, 2)]), [(1, 4), (2, 5), (6, 1), (7, 2)])
    check(elevator_stops(0, [(0, 3), (2, 1), (10, 6)]), [(3, 3), (5, 1), (15, 6)])
    check(elevator_stops(4, [(0, 4)]), [(0, 4)])
