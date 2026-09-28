"""
Every Subset by Bitmask (easy) · patterns: bitmask, subsets

Given a list of distinct items, return every subset of it. Order the subsets
by counting: read a subset as a binary number in which bit i is 1 when
items[i] is included, and list the subsets from that number 0 up to the
largest. Inside each subset keep the items in their original order. The list
holds at most 15 items, and the empty list still has one subset.

Examples:

    Input:  items = ["a", "b"]
    Output: [[], ['a'], ['b'], ['a', 'b']]
    Why:    the numbers 0, 1, 2 and 3 in binary are 00, 01, 10 and 11

    Input:  items = [1, 2, 3]
    Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    Why:    items[2] joins from number 4 onwards, when bit 2 turns on

    Input:  items = []
    Output: [[]]
    Why:    edge case, the empty set is the only subset

Approach:
    A subset of n items is a yes-or-no choice per item, which is exactly an
    n-bit number, so counting from 0 to 2 to the power n minus 1 walks every
    subset once. For each number, bit i is tested with mask >> i & 1, and
    the items whose bits are on form the subset. Because bit i always means
    items[i], the members stay in their original order. Time is O(n times 2
    to the n) and space is the same for the output.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/bit-manipulation/every-subset-by-bitmask

Run it:  python problems/bit-manipulation/08-every-subset-by-bitmask.py
"""


def all_subsets(items):
    n, subsets = len(items), []
    for mask in range(1 << n):                # every n-bit pattern is one subset
        subsets.append([items[i] for i in range(n) if mask >> i & 1])
    return subsets


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(all_subsets(["a", "b"]), [[], ['a'], ['b'], ['a', 'b']])
    check(all_subsets([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    check(all_subsets([]), [[]])
