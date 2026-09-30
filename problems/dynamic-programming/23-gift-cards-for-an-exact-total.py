"""
Gift Cards for an Exact Total (easy) · patterns: 0-1-knapsack, subset-sum

You hold gift cards with the values in cards, and each card can be used at
most once. A card must be used in full. Return True if some of the cards add
up to exactly total, otherwise False.

Examples:

    Input:  cards = [3, 34, 4, 12, 5, 2], total = 9
    Output: True
    Why:    4 + 5 = 9

    Input:  cards = [3, 34, 4, 12, 5, 2], total = 30
    Output: False
    Why:    the small cards add up to only 26, and the 34 card alone is already too much

    Input:  cards = [7], total = 0
    Output: True
    Why:    edge case, using no cards pays exactly zero

Approach:
    This is the 0/1 knapsack with a yes-or-no answer, often called subset
    sum. reachable[t] says whether some of the cards seen so far add up to
    exactly t, and each new card either stays out, leaving the entry as it
    was, or goes in, copying the answer from reachable[t - card]. The inner
    loop runs from high totals to low so that reachable[t - card] still
    describes the cards before this one, which is what keeps each card to a
    single use. Time is O(n · total) and space is O(total).

The lesson behind it: 0/1 Knapsack
    https://bytepatterns.com/learn/dynamic-programming/knapsack-01
    python dynamic-programming/07-knapsack-01.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/gift-cards-for-an-exact-total

Run it:  python problems/dynamic-programming/23-gift-cards-for-an-exact-total.py
"""


def exact_total(cards, total):
    reachable = [False] * (total + 1)
    reachable[0] = True                        # zero is paid with no cards
    for card in cards:
        for t in range(total, card - 1, -1):   # downward: each card used at most once
            if reachable[t - card]:
                reachable[t] = True
    return reachable[total]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(exact_total([3, 34, 4, 12, 5, 2], 9), True)
    check(exact_total([3, 34, 4, 12, 5, 2], 30), False)
    check(exact_total([7], 0), True)
