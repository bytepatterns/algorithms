"""
Bid-Ask Spread After Each Quote (easy) · patterns: two-heaps, max-heap, min-heap

A quote board receives quotes as ("buy", price) or ("sell", price). Nothing
trades on this board, so every quote stays. After each quote, report the
spread: the lowest sell price minus the highest buy price. When either side
has no quotes yet, report None. Return the list of reports.

Examples:

    Input:  quotes = [("buy", 100), ("sell", 105), ("buy", 102), ("sell", 104), ("buy", 99)]
    Output: [None, 5, 3, 2, 2]
    Why:    the best buy climbs to 102 and the best sell drops to 104, and the low buy at 99 changes nothing

    Input:  quotes = [("sell", 50), ("sell", 40)]
    Output: [None, None]
    Why:    nobody has quoted a buy price yet

    Input:  quotes = [("buy", 12), ("sell", 10)]
    Output: [None, -2]
    Why:    edge case, nothing trades here, so a crossed board simply shows a negative spread

Approach:
    The board is two halves with a boundary between them, which is the shape
    the two-heaps pattern handles: a max-heap for the buy side, so the
    highest buy is on top, and a min-heap for the sell side, so the lowest
    sell is on top. Each quote is one push onto its own side, and the spread
    reads only the two tops. Python's heapq is a min-heap, so buy prices are
    stored negated, which turns the difference into a sum of the two tops.
    Each quote costs O(log n), so time is O(n log n) and space is O(n).

The lesson behind it: Heap Basics
    https://bytepatterns.com/learn/heaps/heap-basics
    python heaps/01-heap-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/two-heaps-k-way/bid-ask-spread-after-each-quote

Run it:  python problems/two-heaps-k-way/11-bid-ask-spread-after-each-quote.py
"""


import heapq

def spreads(quotes):
    bids, asks = [], []                  # bids: max-heap of negated prices, asks: min-heap
    reports = []
    for side, price in quotes:
        if side == "buy":
            heapq.heappush(bids, -price)
        else:
            heapq.heappush(asks, price)
        # lowest sell minus highest buy; bids are stored negated
        reports.append(asks[0] + bids[0] if bids and asks else None)
    return reports


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(spreads([("buy", 100), ("sell", 105), ("buy", 102), ("sell", 104), ("buy", 99)]), [None, 5, 3, 2, 2])
    check(spreads([("sell", 50), ("sell", 40)]), [None, None])
    check(spreads([("buy", 12), ("sell", 10)]), [None, -2])
