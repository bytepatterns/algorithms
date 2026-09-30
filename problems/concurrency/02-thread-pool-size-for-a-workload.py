"""
Thread Pool Size for a Workload (easy) · patterns: capacity-math, integer-ceiling

A service handles requests on a fixed thread pool. Each request computes on
the CPU for compute_ms and then waits on the network or a disk for wait_ms,
and while a thread waits its core can run another thread. A common sizing
rule is threads = cores × target utilization × (1 + wait / compute). Given
the core count, the target utilization as a whole percentage, and the two
times in milliseconds, return the pool size rounded up. Use integer
arithmetic so the answer does not depend on floating-point rounding.

Examples:

    Input:  cores = 8, utilization = 100, wait_ms = 90, compute_ms = 10
    Output: 80
    Why:    each core is busy only a tenth of the time, so ten threads share it

    Input:  cores = 4, utilization = 50, wait_ms = 30, compute_ms = 20
    Output: 5
    Why:    4 × 0.5 × 2.5 = 5

    Input:  cores = 16, utilization = 100, wait_ms = 0, compute_ms = 5
    Output: 16
    Why:    edge case, pure CPU work gains nothing from more threads than cores

Approach:
    A thread holds a core only for the compute part of each request, so one
    core can keep (compute + wait) / compute threads busy, and the
    utilization target scales that down to leave headroom. Writing the rule
    as a single fraction keeps every value an integer until the very end,
    and the ceiling is taken with negated floor division, -(-a // b), which
    rounds up exactly. Rounding up rather than down matters: a pool one
    thread short leaves a core idle during every wait. Any positive fraction
    rounds up to at least one thread. Time and space are O(1).

The lesson behind it: Sizing a Thread Pool
    https://bytepatterns.com/learn/concurrency/sizing-a-thread-pool
    python concurrency/13-sizing-a-thread-pool.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/concurrency/thread-pool-size-for-a-workload

Run it:  python problems/concurrency/02-thread-pool-size-for-a-workload.py
"""


def pool_size(cores, utilization_pct, wait_ms, compute_ms):
    # threads = cores * utilization * (1 + wait / compute), rounded up
    num = cores * utilization_pct * (compute_ms + wait_ms)
    den = 100 * compute_ms
    return -(-num // den)                  # integer ceiling


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(pool_size(8, 100, 90, 10), 80)
    check(pool_size(4, 50, 30, 20), 5)
    check(pool_size(16, 100, 0, 5), 16)
    check(pool_size(1, 10, 5, 10), 1)
