"""
Capital Project Picks (hard) · patterns: two-heaps, greedy

You start with some capital and may run at most rounds projects, one after
another. Each project is a pair (cost, profit): you can only start it if
your current capital is at least its cost, and finishing it adds its profit
to your capital. Costs are never spent — they are only the bar you must
clear. Return the capital you end with when you choose greedily for the
largest final amount.

Examples:

    Input:  projects = [(0, 1), (1, 2), (2, 3)], capital = 0, rounds = 2
    Output: 3
    Why:    only (0, 1) is affordable, giving 1; then (1, 2) is, giving 3

    Input:  projects = [(1, 3), (1, 4), (2, 9)], capital = 1, rounds = 2
    Output: 14
    Why:    take the profit of 4 first, which unlocks the project paying 9

    Input:  projects = [(2, 5)], capital = 1, rounds = 1
    Output: 1
    Why:    edge case, nothing is affordable and the answer is the starting capital

Approach:
    Two heaps pointing opposite ways. The locked heap is ordered by cost, so
    its root is always the cheapest thing you still cannot buy — one
    comparison tells you whether anything new became affordable. The ready
    heap is ordered by profit, so its root is the best move available right
    now. Each round drains the locked root across while it is affordable,
    then takes one profit. Every project moves between heaps at most once,
    so the total is O(n log n) time and O(n) space.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/two-heaps-k-way/capital-project-picks

Run it:  python problems/two-heaps-k-way/03-capital-project-picks.py
"""


import heapq

def max_capital(projects, capital, rounds):
    locked = [(cost, profit) for cost, profit in projects]
    heapq.heapify(locked)                          # min-heap on cost
    ready, money = [], capital                     # max-heap on profit
    for _ in range(rounds):
        while locked and locked[0][0] <= money:    # newly affordable
            cost, profit = heapq.heappop(locked)
            heapq.heappush(ready, -profit)
        if not ready:                              # nothing can be started
            break
        money -= heapq.heappop(ready)              # a negated pop adds
    return money


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(max_capital([(0, 1), (1, 2), (2, 3)], 0, 2), 3)
    check(max_capital([(1, 3), (1, 4), (2, 9)], 1, 2), 14)
    check(max_capital([(2, 5)], 1, 1), 1)
