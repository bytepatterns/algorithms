"""
Four List Zero Tuples (medium) · patterns: hash-map, meet-in-the-middle

Four lists of equal length are given. Count the ways to pick exactly one
value from each list so the four values add up to zero. Two picks count
separately whenever they come from different positions, even if the values
happen to be equal.

Examples:

    Input:  a = [1, 2], b = [-2, -1], c = [-1, 2], d = [0, 2]
    Output: 2
    Why:    1 + (-2) + (-1) + 2 and 2 + (-1) + (-1) + 0 both reach zero

    Input:  a = [0], b = [0], c = [0], d = [0]
    Output: 1
    Why:    there is only one pick to make and it works

    Input:  a = [1], b = [1], c = [1], d = [1]
    Output: 0
    Why:    edge case, no combination can reach zero

Approach:
    Splitting the four lists into two halves turns a fourth-power search
    into two squared ones. Every pair from the first half is tallied by its
    sum, so a pair from the second half only has to look up the count of its
    exact opposite. Counting rather than storing the pairs themselves is
    what keeps the lookup constant time, and separate positions with equal
    values are naturally counted separately. Time is O(n squared) on
    average, and space is O(n squared) for the tally.

The lesson behind it: Two Sum
    https://bytepatterns.com/learn/hash-tables/two-sum
    python hash-tables/02-two-sum.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/hash-tables/four-list-zero-tuples

Run it:  python problems/hash-tables/06-four-list-zero-tuples.py
"""


from collections import Counter
def count_zero_tuples(a, b, c, d):
    # every sum reachable from the first half, with how many pairs make it
    pair_sums = Counter(x + y for x in a for y in b)
    total = 0
    for x in c:
        for y in d:
            total += pair_sums.get(-(x + y), 0)   # the exact opposite sum
    return total


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_zero_tuples([1, 2], [-2, -1], [-1, 2], [0, 2]), 2)
    check(count_zero_tuples([0], [0], [0], [0]), 1)
    check(count_zero_tuples([1], [1], [1], [1]), 0)
