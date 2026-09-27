"""
Top K Elements: Hold k winners and let the weakest one guard the door.

You rarely need everything ranked — just the best k. Hold a min-heap of
exactly k items, so the root is your weakest keeper.

Each new value is compared against that root alone. Bigger, and it evicts
the weakling; smaller, and it is dropped for good. Cost: O(n log k) time and
O(k) memory, with no need to hold the stream.

Lesson 4 of Heaps, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/heaps/top-k-elements

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python heaps/04-top-k-elements.py
"""


import heapq

def top_k(stream, k):
    keep = []                                  # min-heap of the best k so far
    for x in stream:
        if len(keep) < k:
            heapq.heappush(keep, x)
        elif x > keep[0]:                      # beats the weakest keeper?
            heapq.heapreplace(keep, x)         # pop it, push x: one sift
    return sorted(keep, reverse=True)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(top_k([4, 1, 9, 7, 3, 8], 3), [9, 8, 7])
    print(heapq.nlargest(3, [4, 1, 9, 7, 3, 8]))   # same, batteries included
