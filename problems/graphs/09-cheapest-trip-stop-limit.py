"""
Cheapest Trip Within a Stop Limit (medium) · patterns: bellman-ford, shortest-path

There are n airports numbered from 0 and a list of one-way flights (u, v,
price) with positive prices. Find the cheapest way to travel from src to dst
when the trip may change planes at most k times, so it uses at most k + 1
flights. Return that price, or -1 if no trip within the limit exists.
Travelling from an airport to itself costs 0.

Examples:

    Input:  n = 4, src = 0, dst = 3, k = 1
            flights = [(0, 1, 100), (1, 2, 100), (2, 3, 100), (0, 3, 500)]
    Output: 500
    Why:    the 300 route needs two stops, one more than allowed

    Input:  n = 4, src = 0, dst = 3, k = 2
            flights = [(0, 1, 100), (1, 2, 100), (2, 3, 100), (0, 3, 500)]
    Output: 300
    Why:    with two stops allowed, 0 -> 1 -> 2 -> 3 is cheapest

    Input:  n = 3, flights = [(0, 1, 5)], src = 0, dst = 2, k = 1
    Output: -1
    Why:    edge case, no flight ever lands at airport 2

Approach:
    This is Bellman-Ford stopped early. After round r the price array holds
    the cheapest trip that uses at most r flights, so k + 1 rounds answer
    the question exactly. The one trap is chaining: relaxing edges in place
    can use a price set earlier in the same round, sneaking in an extra
    flight, so each round reads from the previous round's prices and writes
    to a fresh copy. Time is O(k times m) for m flights, and space is O(n).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/cheapest-trip-stop-limit

Run it:  python problems/graphs/09-cheapest-trip-stop-limit.py
"""


def cheapest_route(n, flights, src, dst, k):
    INF = float("inf")
    price = [INF] * n
    price[src] = 0
    for _ in range(k + 1):               # round r allows trips of up to r flights
        nxt = price[:]                   # read last round only, never this one
        for u, v, p in flights:
            if price[u] + p < nxt[v]:
                nxt[v] = price[u] + p
        price = nxt
    return price[dst] if price[dst] < INF else -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    flights = [(0, 1, 100), (1, 2, 100), (2, 3, 100), (0, 3, 500)]
    check(cheapest_route(4, flights, 0, 3, 1), 500)
    check(cheapest_route(4, flights, 0, 3, 2), 300)
    check(cheapest_route(3, [(0, 1, 5)], 0, 2, 1), -1)
