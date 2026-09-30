"""
Latency Percentiles by Nearest Rank (easy) · patterns: percentiles, sorting

A dashboard reports request latency as percentiles rather than an average.
Given a list of latency samples in milliseconds and a list of percentiles
such as [50, 90, 99], return a dict from each percentile to its value using
the nearest-rank method: sort the samples, and the p-th percentile is the
sample at 1-based rank ceil(p × n / 100), where n is the number of samples.
Use integer arithmetic for the rank. There are up to 1,000,000 samples.

Examples:

    Input:  latencies = [12, 15, 11, 13, 240, 14, 12, 16, 13, 12], ps = [50, 90, 99]
    Output: {50: 13, 90: 16, 99: 240}
    Why:    one slow request out of ten is invisible at p90 and is the whole story at p99

    Input:  latencies = 1 to 100, ps = [50, 90, 99, 100]
    Output: {50: 50, 90: 90, 99: 99, 100: 100}
    Why:    with 100 samples the p-th percentile is simply the p-th smallest

    Input:  latencies = [7], ps = [50, 99]
    Output: {50: 7, 99: 7}
    Why:    edge case, a single sample is every percentile

Approach:
    Averages hide the slow tail that users actually feel, which is why
    dashboards track p50, p90 and p99, and the first example shows it: the
    mean of those ten samples is about 36 ms, a number no request came close
    to. Nearest rank is the simplest percentile definition that always
    returns a real sample: sort, compute the rank ceil(p × n / 100) with
    integer arithmetic, and read that position. Clamping the rank at 1 keeps
    very small percentiles valid on short lists. Sorting dominates, so time
    is O(n log n + q) for q percentiles, and space is O(n) for the sorted
    copy.

The lesson behind it: Observability Basics
    https://bytepatterns.com/learn/system-design/observability-basics

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/system-design/latency-percentiles-by-nearest-rank

Run it:  python problems/system-design/06-latency-percentiles-by-nearest-rank.py
"""


def percentiles(latencies, ps):
    ranked = sorted(latencies)
    n = len(ranked)
    return {p: ranked[max(1, (p * n + 99) // 100) - 1] for p in ps}   # ceil(p * n / 100), 1-based


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(percentiles([12, 15, 11, 13, 240, 14, 12, 16, 13, 12], [50, 90, 99]), {50: 13, 90: 16, 99: 240})
    check(percentiles(list(range(1, 101)), [50, 90, 99, 100]), {50: 50, 90: 90, 99: 99, 100: 100})
    check(percentiles([7], [50, 99]), {50: 7, 99: 7})
