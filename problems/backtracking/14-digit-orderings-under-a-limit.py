"""
Digit Orderings Under a Limit (easy) · patterns: backtracking, permutations, pruning

Given a list of distinct digits and a limit, return every number that uses
each digit exactly once, in some order, and is at most the limit, in
increasing order. A number may not start with 0 unless it is the single
digit 0. There are at most 8 digits.

Examples:

    Input:  digits = [3, 1, 2], limit = 300
    Output: [123, 132, 213, 231]
    Why:    312 and 321 are over the limit, and trying digits in increasing order yields the numbers already sorted

    Input:  digits = [0, 2, 1], limit = 999
    Output: [102, 120, 201, 210]
    Why:    orderings that start with 0 are skipped, because 012 is really a two-digit number

    Input:  digits = [5], limit = 4
    Output: []
    Why:    edge case, the only ordering is already over the limit

Approach:
    This is the permutation template with a used array: pick an unused
    digit, recurse, then release it. Sorting the digits first makes the
    search visit prefixes in increasing order, so the results are sorted for
    free. The limit gives a cheap prune: filling the rest with anything at
    all makes the number at least the prefix shifted left by the remaining
    positions, so once that bound passes the limit, this digit and every
    larger one can be skipped with a break. The leading-zero rule is one
    condition on the first position. In the worst case all n! orderings are
    built, so time is O(n × n!) and space is O(n) for the recursion, plus
    the output.

The lesson behind it: Permutations
    https://bytepatterns.com/learn/backtracking/permutations
    python backtracking/03-permutations.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/backtracking/digit-orderings-under-a-limit

Run it:  python problems/backtracking/14-digit-orderings-under-a-limit.py
"""


def orderings_up_to(digits, limit):
    digits = sorted(digits)                # increasing digits give sorted output
    used = [False] * len(digits)
    out = []

    def place(value, length):
        if length == len(digits):
            out.append(value)
            return
        for i, d in enumerate(digits):
            if used[i] or (length == 0 and d == 0 and len(digits) > 1):
                continue                   # used already, or a leading zero
            nxt = value * 10 + d
            if nxt * 10 ** (len(digits) - length - 1) > limit:
                break                      # the smallest completion is too big
            used[i] = True
            place(nxt, length + 1)
            used[i] = False                # back out

    place(0, 0)
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(orderings_up_to([3, 1, 2], 300), [123, 132, 213, 231])
    check(orderings_up_to([0, 2, 1], 999), [102, 120, 201, 210])
    check(orderings_up_to([5], 4), [])
