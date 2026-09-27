"""
Binary Search on Answer: No sorted array? Binary search the answer range.

Some problems hand you no array to search, but their answers still have
order: if a value works, every larger value works too. Binary search that
range of candidate answers, using a feasibility check in place of a
comparison.

Lesson 5 of Searching, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/searching/binary-search-on-answer

Run it:  python searching/05-binary-search-on-answer.py
"""


def min_capacity(weights, trips):
    def fits(cap):
        used, load = 1, 0
        for w in weights:
            if load + w > cap:      # start a new trip
                used, load = used + 1, 0
            load += w
        return used <= trips
    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if fits(mid): hi = mid      # try something smaller
        else:         lo = mid + 1
    return lo


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(min_capacity([3, 2, 2, 4, 1, 4], 3), 6)
