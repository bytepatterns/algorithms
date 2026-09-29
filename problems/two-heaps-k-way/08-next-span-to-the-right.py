"""
Next Span to the Right (medium) · patterns: two-heaps, max-heap

A build system has a list of jobs, each a time span [start, end], and no two
jobs share a start time. For every job, find the job that could run next on
the same machine: the one with the smallest start that is at least this
job's end. Return, for each job in input order, the index of that job, or -1
if there is none. A job whose start equals its own end may follow itself.

Examples:

    Input:  spans = [[3, 4], [2, 3], [1, 2]]
    Output: [-1, 0, 1]
    Why:    nothing starts at 4 or later; [3, 4] follows [2, 3], and [2, 3] follows [1, 2]

    Input:  spans = [[1, 4], [2, 3], [3, 4]]
    Output: [-1, 2, -1]

    Input:  spans = [[1, 2]]
    Output: [-1]
    Why:    edge case, a single job has no successor

Approach:
    One max-heap orders the jobs by end and the other orders them by start.
    Jobs are answered from the largest end down, and for each one the start
    heap is popped while its top is still at least the current end; the last
    start popped is the smallest qualifying start. Starts popped earlier are
    larger than that one, so no later job, whose end is even smaller, would
    ever prefer them, which is why they can be discarded. The best one is
    pushed back for the jobs still to come. Each start is discarded at most
    once and each job pushes back at most once, so time is O(n log n) and
    space is O(n).

The lesson behind it: Two Heaps: Running Median
    https://bytepatterns.com/learn/two-heaps-k-way/two-heaps-running-median
    python two-heaps-k-way/01-two-heaps-running-median.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/two-heaps-k-way/next-span-to-the-right

Run it:  python problems/two-heaps-k-way/08-next-span-to-the-right.py
"""


import heapq

def next_to_the_right(spans):
    ends = [(-e, i) for i, (s, e) in enumerate(spans)]
    starts = [(-s, i) for i, (s, e) in enumerate(spans)]
    heapq.heapify(ends); heapq.heapify(starts)   # both act as max-heaps
    answer = [-1] * len(spans)
    while ends:
        neg_end, i = heapq.heappop(ends)         # largest end still waiting
        best = None
        while starts and -starts[0][0] >= -neg_end:
            best = heapq.heappop(starts)         # a smaller start that still fits
        if best:
            answer[i] = best[1]
            heapq.heappush(starts, best)         # smaller ends may use it too
    return answer


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(next_to_the_right([[3, 4], [2, 3], [1, 2]]), [-1, 0, 1])
    check(next_to_the_right([[1, 4], [2, 3], [3, 4]]), [-1, 2, -1])
    check(next_to_the_right([[1, 2]]), [-1])
    check(next_to_the_right([[1, 1], [3, 4], [2, 3]]), [0, -1, 1])
