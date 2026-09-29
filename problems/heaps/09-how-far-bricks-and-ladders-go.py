"""
How Far Bricks and Ladders Go (medium) · patterns: min-heap, greedy

A climber walks along a row of rooftops, heights[0] first. Stepping down or
to an equal height is free. Stepping up by d needs either one ladder,
whatever the height, or d bricks. Given a number of bricks and a number of
ladders, return the index of the furthest rooftop the climber can reach when
the resources are used as well as possible.

Examples:

    Input:  heights = [4, 2, 7, 6, 9, 14, 12], bricks = 5, ladders = 1
    Output: 4
    Why:    bricks for the rise of 5 onto index 2, the ladder for the rise of 3 onto index 4; the rise of 5 after that is too much

    Input:  heights = [4, 12, 2, 7, 3, 18, 20, 3, 19], bricks = 10, ladders = 2
    Output: 7

    Input:  heights = [1, 5], bricks = 0, ladders = 0
    Output: 0
    Why:    edge case, the very first climb cannot be paid for

Approach:
    Among the climbs made so far, the best use of the ladders is always the
    tallest climbs, with bricks covering the rest. A min-heap of the climbs
    that currently hold a ladder makes that choice revisable: each new climb
    takes a ladder, and when there are more climbs than ladders, the
    smallest ladder climb is switched to bricks, which is the cheapest
    possible brick payment. If the bricks run out, the climber is stuck on
    the current rooftop, and no other assignment could have done better
    because the brick total was already the minimum. The heap holds at most
    ladders plus one rises, so time is O(n log L) for L ladders and space is
    O(L).

The lesson behind it: Priority Queue
    https://bytepatterns.com/learn/heaps/priority-queue
    python heaps/03-priority-queue.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/heaps/how-far-bricks-and-ladders-go

Run it:  python problems/heaps/09-how-far-bricks-and-ladders-go.py
"""


import heapq

def furthest(heights, bricks, ladders):
    ladder_climbs = []                         # climbs that currently hold a ladder
    for i in range(len(heights) - 1):
        rise = heights[i + 1] - heights[i]
        if rise <= 0:
            continue                           # going down is free
        heapq.heappush(ladder_climbs, rise)
        if len(ladder_climbs) > ladders:
            bricks -= heapq.heappop(ladder_climbs)   # smallest climb uses bricks
            if bricks < 0:
                return i
    return len(heights) - 1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(furthest([4, 2, 7, 6, 9, 14, 12], 5, 1), 4)
    check(furthest([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2), 7)
    check(furthest([1, 5], 0, 0), 0)
    check(furthest([14, 3, 19, 3], 17, 0), 3)
