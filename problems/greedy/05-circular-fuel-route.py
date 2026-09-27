"""
Circular Fuel Route (medium) · patterns: greedy, running-sum

Fuel stations sit on a circular road. Station i lets you take on fuel[i]
units, and driving from station i to the next one burns cost[i] units. You
start at one station with an empty tank and drive all the way round, never
letting the tank drop below zero. Return the index of the first station from
which the full loop succeeds, or -1 if none does.

Examples:

    Input:  fuel = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
    Output: 3
    Why:    from station 3 the tank reads 3, 6, 4, 2, 0 after each leg

    Input:  fuel = [2, 3, 4], cost = [3, 4, 3]
    Output: -1
    Why:    9 units of fuel cannot pay for 10 units of driving

    Input:  fuel = [5], cost = [4]
    Output: 0
    Why:    edge case, a single station only has to pay for its own loop

Approach:
    If the fuel on the whole road is less than the driving it has to pay
    for, no start can work. Otherwise a single sweep suffices: a trip from s
    that fails right after station i arrived at every intermediate station
    with a non-negative tank, so starting at one of them only throws that
    surplus away and fails too. The candidate therefore jumps past the
    failure point, and every index it skips is provably bad, which also
    makes the survivor the lowest working index. The total-fuel check
    guarantees the survivor completes the loop. Time is O(n) and space is
    O(1).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/greedy/circular-fuel-route

Run it:  python problems/greedy/05-circular-fuel-route.py
"""


def start_station(fuel, cost):
    if sum(fuel) < sum(cost):
        return -1                        # not enough fuel on the whole road
    start, tank = 0, 0
    for i in range(len(fuel)):
        tank += fuel[i] - cost[i]
        if tank < 0:                     # every start from start..i fails here
            start, tank = i + 1, 0
    return start


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(start_station([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
    check(start_station([2, 3, 4], [3, 4, 3]), -1)
    check(start_station([5], [4]), 0)
