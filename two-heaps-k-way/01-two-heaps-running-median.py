"""
Two Heaps: Running Median: Two heaps face each other, and the middle sits between their roots.

Keep the small half in a max-heap and the large half in a min-heap. The two
roots sit either side of the middle, so the median is always one glance away
— never a re-sort.

Every arrival enters the low side, then low's largest is handed across to
high. One size check keeps the halves level.

Lesson 1 of Two Heaps & K-Way Merge, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/two-heaps-k-way/two-heaps-running-median

Run it:  python two-heaps-k-way/01-two-heaps-running-median.py
"""


import heapq

def medians(stream):
    low, high = [], []                             # low: max-heap (negated)
    out = []
    for x in stream:
        heapq.heappush(low, -x)                    # everything enters low
        heapq.heappush(high, -heapq.heappop(low))  # hand low's largest across
        if len(high) > len(low):                   # keep low the bigger half
            heapq.heappush(low, -heapq.heappop(high))
        out.append(-low[0] if len(low) > len(high)
                   else (-low[0] + high[0]) / 2)
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(medians([5, 15, 1, 3]), [5, 10.0, 5, 4.0])
