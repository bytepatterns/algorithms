"""
Rate-Limit Tiers for an API Gateway (medium) · patterns: rate-limiting, sliding-window-log

An API gateway limits each key according to its plan. A tier is a list of
(window, limit) rules in seconds, for example free allows 2 requests per
second and 5 per minute. A request at time t is allowed only if, for every
rule of its key's tier, fewer than limit allowed requests from that key fall
in the window (t - window, t]. Rejected requests do not count against later
ones. Given the tiers, a map from key to tier, and the requests as (time,
key) sorted by time, return a dict from each key to [allowed, rejected].
There are up to 1,000,000 requests.

Examples:

    Input:  tiers = {"free": [(1, 2), (60, 5)], "pro": [(1, 5), (60, 100)]},
            3 free and 3 pro requests at 0, 2 free at 1, 2 free at 2, 1 free at 61
    Output: {'k-free': [6, 2], 'k-pro': [3, 0]}
    Why:    free loses 1 request to the per-second rule at 0 and 1 to the per-minute rule at 2

    Input:  tiers = {"free": [(10, 1)]}, requests from "a" at 0, 9, 10, 19, 20
    Output: {'a': [3, 2]}
    Why:    the window is half-open, so a request at 10 no longer sees the one at 0

    Input:  a "pro" key that sends no requests
    Output: {'idle': [0, 0]}
    Why:    edge case, every key appears in the result even when it is silent

Approach:
    Tiers with several windows are the realistic case: a per-second rule
    stops bursts and a per-minute rule caps sustained use, and a request
    must satisfy all of them at once. A sliding window log handles any
    number of windows from one structure, the sorted list of allowed
    timestamps per key, and a binary search turns each window into a count.
    Recording only allowed requests matters: counting rejected ones would
    let a client that keeps retrying lock itself out forever. The half-open
    window in the second example is what makes a 1-per-10-seconds rule allow
    requests exactly 10 seconds apart. Each request costs O(r log n) for r
    rules and n logged requests of its key, and space is O(n); a production
    gateway would trim entries older than the longest window, or switch to
    approximate counters, to bound that memory.

The lesson behind it: Design a Rate Limiter
    https://bytepatterns.com/learn/system-design-cases/design-a-rate-limiter

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/system-design-cases/rate-limit-tiers-for-an-api-gateway

Run it:  python problems/system-design-cases/03-rate-limit-tiers-for-an-api-gateway.py
"""


from bisect import bisect_right
from collections import defaultdict

def gateway(tiers, keys, requests):
    log = defaultdict(list)                # key -> sorted times of allowed requests
    stats = {k: [0, 0] for k in keys}      # key -> [allowed, rejected]
    for t, key in requests:
        times = log[key]
        ok = all(len(times) - bisect_right(times, t - window) < limit    # count in (t - window, t]
                 for window, limit in tiers[keys[key]])
        if ok:
            times.append(t)                # only allowed requests count
        stats[key][0 if ok else 1] += 1
    return stats


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    tiers = {"free": [(1, 2), (60, 5)], "pro": [(1, 5), (60, 100)]}
    reqs = [(0, "k-free")] * 3 + [(0, "k-pro")] * 3 + [(1, "k-free")] * 2 + [(2, "k-free")] * 2 + [(61, "k-free")]
    check(gateway(tiers, {"k-free": "free", "k-pro": "pro"}, reqs), {'k-free': [6, 2], 'k-pro': [3, 0]})
    check(gateway({"free": [(10, 1)]}, {"a": "free"}, [(0, "a"), (9, "a"), (10, "a"), (19, "a"), (20, "a")]), {'a': [3, 2]})
    check(gateway(tiers, {"idle": "pro"}, []), {'idle': [0, 0]})
