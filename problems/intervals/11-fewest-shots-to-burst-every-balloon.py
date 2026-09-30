"""
Fewest Shots to Burst Every Balloon (medium) · patterns: intervals, greedy, sort-by-end

Balloons are taped to a wall, and each one spans the horizontal range
[start, end]. A vertical shot fired at position x bursts every balloon with
start less than or equal to x and x less than or equal to end. Return the
fewest shots that burst every balloon.

Examples:

    Input:  balloons = [[10, 16], [2, 8], [1, 6], [7, 12]]
    Output: 2
    Why:    a shot at 6 bursts [2, 8] and [1, 6], and a shot at 12 bursts [7, 12] and [10, 16]

    Input:  balloons = [[1, 2], [3, 4], [5, 6], [7, 8]]
    Output: 4
    Why:    no two balloons overlap

    Input:  balloons = [[1, 2], [2, 3], [3, 4], [4, 5]]
    Output: 2
    Why:    edge case, balloons that only touch at an end can share a shot, at 2 and at 4

Approach:
    This is interval scheduling seen from the other side: the fewest shots
    equal the most balloons that are pairwise apart, and both come from
    sorting by end. The balloon that ends first needs some shot, and firing
    at its end is never worse than firing earlier, since every balloon still
    standing ends at or after that point and the shot bursts all of those
    that have already started. Balloons that start at or before the last
    shot are burst by it, and the first one that starts after it forces a
    new shot at its own end. Sorting costs O(n log n), the walk is O(n), and
    space is O(n) for the sorted copy.

The lesson behind it: Interval Scheduling
    https://bytepatterns.com/learn/greedy/interval-scheduling
    python greedy/02-interval-scheduling.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/intervals/fewest-shots-to-burst-every-balloon

Run it:  python problems/intervals/11-fewest-shots-to-burst-every-balloon.py
"""


def fewest_shots(balloons):
    shots, last = 0, None
    for start, end in sorted(balloons, key=lambda b: b[1]):   # earliest end first
        if last is None or start > last:     # the last shot misses this balloon
            shots += 1
            last = end                       # fire as late as this balloon allows
    return shots


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(fewest_shots([[10, 16], [2, 8], [1, 6], [7, 12]]), 2)
    check(fewest_shots([[1, 2], [3, 4], [5, 6], [7, 8]]), 4)
    check(fewest_shots([[1, 2], [2, 3], [3, 4], [4, 5]]), 2)
