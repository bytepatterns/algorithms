"""
Split Candidates Between Two Cities (easy) · patterns: greedy, sort-by-difference

A company is flying an even number of candidates to on-site interviews, and
exactly half must go to office A and half to office B. costs[i] = [a, b]
gives the fare for candidate i to each office. Return the lowest total fare
that sends exactly half of the candidates to each office.

Examples:

    Input:  costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    Output: 110
    Why:    the first two go to A for 10 + 30, the last two to B for 50 + 20

    Input:  costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
    Output: 1859

    Input:  costs = [[5, 5], [7, 7]]
    Output: 12
    Why:    edge case, both offices cost the same, so any even split is optimal

Approach:
    Picture everyone flying to B first; switching candidate i to A then
    changes the total by a minus b, and exactly half of the candidates must
    switch. The cheapest way to choose them is to take the half with the
    smallest values of a minus b, so the list is sorted by that difference
    and split down the middle. An exchange argument confirms it: swapping
    any A candidate for a B candidate with a smaller difference could only
    lower the total. Time is O(n log n) for the sort and space is O(n) for
    the sorted copy.

The lesson behind it: Sorting Basics
    https://bytepatterns.com/learn/sorting/sorting-basics
    python sorting/01-sorting-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/greedy/split-candidates-between-two-cities

Run it:  python problems/greedy/08-split-candidates-between-two-cities.py
"""


def split_cities(costs):
    costs = sorted(costs, key=lambda c: c[0] - c[1])   # most eager for A first
    half = len(costs) // 2
    return sum(a for a, _ in costs[:half]) + sum(b for _, b in costs[half:])


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(split_cities([[10, 20], [30, 200], [400, 50], [30, 20]]), 110)
    check(split_cities([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]), 1859)
    check(split_cities([[5, 5], [7, 7]]), 12)
