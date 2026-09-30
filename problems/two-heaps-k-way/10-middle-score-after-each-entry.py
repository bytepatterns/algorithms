"""
Middle Score After Each Entry (easy) · patterns: two-heaps, streaming

Scores arrive one at a time. After each arrival, report the middle score of
everything seen so far. When the number of scores is even, report the lower
of the two middle scores. Return the list of reports, and aim for better
than sorting all the scores again after every arrival.

Examples:

    Input:  scores = [5, 15, 1, 3]
    Output: [5, 5, 5, 3]
    Why:    after all four arrive the sorted scores are 1, 3, 5, 15, and the lower middle is 3

    Input:  scores = [2, 2, 2]
    Output: [2, 2, 2]

    Input:  scores = []
    Output: []
    Why:    edge case, no arrivals means no reports

Approach:
    The two-heaps pattern keeps the sorted order split at the middle without
    ever sorting: a max-heap holds the lower half, so its top is the largest
    of the small scores, and a min-heap holds the upper half. The lower half
    is allowed to be one score bigger, which makes its top the middle for an
    odd count and the lower middle for an even count, exactly the score to
    report. A new score goes to the lower half unless it is larger than the
    lower half's top, and one move across restores the size rule. Python's
    heapq is a min-heap, so the lower half stores negated scores. Each
    arrival costs O(log n), so time is O(n log n) overall and space is O(n).

The lesson behind it: Two Heaps: Running Median
    https://bytepatterns.com/learn/two-heaps-k-way/two-heaps-running-median
    python two-heaps-k-way/01-two-heaps-running-median.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/two-heaps-k-way/middle-score-after-each-entry

Run it:  python problems/two-heaps-k-way/10-middle-score-after-each-entry.py
"""


import heapq

def middle_scores(scores):
    low, high = [], []            # low: max-heap of negated scores, high: min-heap
    reports = []
    for s in scores:
        if low and s > -low[0]:
            heapq.heappush(high, s)
        else:
            heapq.heappush(low, -s)
        if len(low) > len(high) + 1:           # lower half too big
            heapq.heappush(high, -heapq.heappop(low))
        elif len(high) > len(low):             # upper half too big
            heapq.heappush(low, -heapq.heappop(high))
        reports.append(-low[0])                # top of the lower half
    return reports


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(middle_scores([5, 15, 1, 3]), [5, 5, 5, 3])
    check(middle_scores([2, 2, 2]), [2, 2, 2])
    check(middle_scores([]), [])
