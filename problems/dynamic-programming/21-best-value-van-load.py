"""
Best Value Van Load (medium) · patterns: unbounded-knapsack, bottom-up-dp

A van can carry at most W kilograms. There are several crate types, each
with a whole-number weight of at least 1 and a positive value, and the
warehouse has as many crates of every type as you want. Return the largest
total value you can load without going over W.

Examples:

    Input:  W = 10, crates (weight, value) = [(3, 5), (4, 7), (6, 11)]
    Output: 18
    Why:    one 4 kg crate and one 6 kg crate; three 3 kg crates only reach 15

    Input:  W = 7, crates = [(2, 3), (5, 9)]
    Output: 12
    Why:    5 kg plus 2 kg beats three 2 kg crates, which are worth 9

    Input:  W = 2, crates = [(3, 5)]
    Output: 0
    Why:    edge case, the only crate is too heavy, so the van leaves empty

Approach:
    Take away any one crate from a best load for capacity c and the rest
    must be a best load for c minus that crate's weight, so the answers for
    small capacities build the answers for larger ones. Filling capacities
    from small to large lets a crate type be used again, because best[c -
    weight] may already contain crates of the same type. Leaving room unused
    is covered because the table starts at zero and never goes down. Time is
    O(W times the number of crate types), and space is O(W).

The lesson behind it: Unbounded Knapsack
    https://bytepatterns.com/learn/dynamic-programming/unbounded-knapsack
    python dynamic-programming/11-unbounded-knapsack.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/best-value-van-load

Run it:  python problems/dynamic-programming/21-best-value-van-load.py
"""


def best_load(W, crates):
    best = [0] * (W + 1)                       # best[c]: most value within c kg
    for c in range(1, W + 1):
        for weight, value in crates:
            if weight <= c:
                best[c] = max(best[c], best[c - weight] + value)   # reuse is allowed
    return best[W]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(best_load(10, [(3, 5), (4, 7), (6, 11)]), 18)
    check(best_load(7, [(2, 3), (5, 9)]), 12)
    check(best_load(2, [(3, 5)]), 0)
