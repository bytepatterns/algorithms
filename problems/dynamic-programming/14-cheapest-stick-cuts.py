"""
Cheapest Stick Cuts (hard) · patterns: interval-dp, bottom-up-dp

A wooden stick of a given length must be cut at every position in a list of
marks, each strictly between 0 and length and all different. A saw charges
the current length of the piece it cuts, so the order of the cuts changes
the bill. Return the smallest total charge for making all the cuts. With no
marks there is nothing to pay.

Examples:

    Input:  length = 10, marks = [2, 4, 7]
    Output: 20
    Why:    cut at 4 (pays 10), then at 2 (pays 4), then at 7 (pays 6)

    Input:  length = 9, marks = [5, 1, 6, 3]
    Output: 21
    Why:    marks can arrive in any order; only their positions matter

    Input:  length = 6, marks = []
    Output: 0
    Why:    edge case, no cuts

Approach:
    After the first cut inside a piece, the left and right parts are cut
    independently, so the cheapest cost of a piece is its length plus the
    best over every first cut of the two parts' costs. With the marks sorted
    and 0 and length added as ends, every piece is a stretch between two of
    these points, which is interval dynamic programming. Stretches with no
    mark inside cost nothing, and filling by increasing width guarantees the
    smaller stretches are ready. Time is O(m cubed) and space is O(m
    squared) for m marks.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/cheapest-stick-cuts

Run it:  python problems/dynamic-programming/14-cheapest-stick-cuts.py
"""


def min_cut_cost(length, marks):
    ends = [0] + sorted(marks) + [length]
    m = len(ends)
    best = [[0] * m for _ in range(m)]      # best[i][j] = cheapest cuts strictly inside ends i..j
    for width in range(2, m):               # stretches that hold at least one mark
        for i in range(m - width):
            j = i + width
            first = min(best[i][k] + best[k][j] for k in range(i + 1, j))
            best[i][j] = ends[j] - ends[i] + first   # the first cut pays the whole stretch
    return best[0][m - 1]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(min_cut_cost(10, [2, 4, 7]), 20)
    check(min_cut_cost(9, [5, 1, 6, 3]), 21)
    check(min_cut_cost(6, []), 0)
