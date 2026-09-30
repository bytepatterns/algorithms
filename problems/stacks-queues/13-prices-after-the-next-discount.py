"""
Prices After the Next Discount (easy) · patterns: monotonic-stack, next-smaller

A shop lists item prices in shelf order. Buying item i earns a discount
equal to the price of the first item to its right whose price is less than
or equal to prices[i]. If no such item exists, there is no discount. Return
the price actually paid for every item.

Examples:

    Input:  prices = [8, 4, 6, 2, 3]
    Output: [4, 2, 4, 2, 3]
    Why:    8 is discounted by 4, 4 and 6 are both discounted by 2, and 2 and 3 have no cheaper item after them

    Input:  prices = [10, 1, 1, 6]
    Output: [9, 0, 1, 6]
    Why:    an equal price counts, so the first 1 is discounted by the second 1

    Input:  prices = [1, 2, 3, 4, 5]
    Output: [1, 2, 3, 4, 5]
    Why:    edge case, rising prices never meet a cheaper item to the right

Approach:
    This is the next smaller element scan, the same one Largest Rectangle
    runs to find where each bar stops. Indices wait on a stack with rising
    prices, and the first price at or below an item's own pops it and fixes
    its discount. An item that is never popped had no cheaper item to its
    right, so it keeps its price, which is why the result starts as a copy
    of the input. Every index is pushed and popped at most once, so time is
    O(n) and space is O(n).

The lesson behind it: Largest Rectangle
    https://bytepatterns.com/learn/stacks-queues/largest-rectangle
    python stacks-queues/09-largest-rectangle.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/prices-after-the-next-discount

Run it:  python problems/stacks-queues/13-prices-after-the-next-discount.py
"""


def final_prices(prices):
    paid = prices[:]                             # no discount unless one is found
    stack = []                                   # waiting indices, prices rising upward
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] >= p:  # p is the first price at or below theirs
            j = stack.pop()
            paid[j] = prices[j] - p
        stack.append(i)
    return paid


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(final_prices([8, 4, 6, 2, 3]), [4, 2, 4, 2, 3])
    check(final_prices([10, 1, 1, 6]), [9, 0, 1, 6])
    check(final_prices([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
