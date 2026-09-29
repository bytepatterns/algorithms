"""
Running Median Stream (hard) · patterns: two-heaps, streaming

Numbers arrive one at a time. After each arrival, report the median of
everything received so far: the middle value when the count is odd, and the
average of the two middle values when it is even. Return the list of
medians, one per arrival, as decimal numbers. The values do not arrive in
any particular order.

Examples:

    Input:  stream = [5, 15, 1, 3]
    Output: [5.0, 10.0, 5.0, 4.0]
    Why:    after three arrivals the values are 1, 5, 15 and the middle one is 5

    Input:  stream = [1, 2]
    Output: [1.0, 1.5]
    Why:    an even count averages the two middle values

    Input:  stream = [7]
    Output: [7.0]
    Why:    edge case, a single value is its own median

Approach:
    Two heaps face each other across the middle: the lower half exposes its
    largest value and the upper half its smallest, so the median is always
    one or two values away. Pushing every arrival into the lower half and
    immediately handing its largest to the upper half guarantees the value
    lands on the correct side regardless of where it belongs, and one
    rebalancing move keeps the lower half never smaller than the upper. Each
    arrival costs a logarithm. Time is O(n log n) overall, and space is
    O(n).

The lesson behind it: Priority Queue
    https://bytepatterns.com/learn/heaps/priority-queue
    python heaps/03-priority-queue.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/heaps/running-median-stream

Run it:  python problems/heaps/04-running-median-stream.py
"""


import heapq
def running_medians(stream):
    low, high = [], []               # low is a max-heap (negated), high is a min-heap
    out = []
    for x in stream:
        heapq.heappush(low, -x)                    # everything enters through low
        heapq.heappush(high, -heapq.heappop(low))  # hand low's largest to high
        if len(high) > len(low):                   # keep low the bigger half
            heapq.heappush(low, -heapq.heappop(high))
        if len(low) > len(high):
            out.append(float(-low[0]))
        else:
            out.append((-low[0] + high[0]) / 2)
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(running_medians([5, 15, 1, 3]), [5.0, 10.0, 5.0, 4.0])
    check(running_medians([1, 2]), [1.0, 1.5])
    check(running_medians([7]), [7.0])
