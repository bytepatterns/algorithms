"""
Token Bucket Rate Limiter (easy) · patterns: token-bucket, integer-math

An API gateway limits each client with a token bucket. The bucket holds at
most capacity tokens and starts full at time 0. Tokens drip back in
continuously at per_second tokens per second, never beyond the capacity, and
every request spends one whole token or is rejected. Given the request times
in milliseconds, in order, return for each one whether it is allowed.
Refills are fractional, so a quarter of a second at 4 tokens per second is
exactly one token; avoid floating point so a request exactly on the boundary
is never rejected by a rounding error.

Examples:

    Input:  capacity = 2, per_second = 1, times_ms = [0, 0, 0, 500, 1000, 3000]
    Output: [True, True, False, False, True, True]
    Why:    the burst of three gets two; half a token at 500 is not enough; the bucket refills after

    Input:  capacity = 1, per_second = 4, times_ms = [0, 100, 250, 260]
    Output: [True, False, True, False]
    Why:    exactly one token is back at 250 ms

    Input:  capacity = 3, per_second = 1, times_ms = []
    Output: []
    Why:    edge case, no traffic

Approach:
    A token bucket needs no background refill job: the level can be
    recomputed when a request arrives from how long it has been since the
    previous one, which is the same answer a ticking timer would give.
    Counting in thousandths of a token makes every refill an integer,
    because one millisecond at per_second tokens per second is exactly
    per_second thousandths, so a request landing precisely when a token
    completes is always allowed. The cap models the bucket's size, which is
    what bounds a burst after a quiet period. Each request is O(1), so the
    whole run is O(n), with O(1) state per client.

The lesson behind it: Rate Limiting
    https://bytepatterns.com/learn/system-design/rate-limiting

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/system-design/token-bucket-rate-limiter

Run it:  python problems/system-design/01-token-bucket-rate-limiter.py
"""


def token_bucket(capacity, per_second, times_ms):
    # count in thousandths of a token so every refill is exact integer maths
    full, tokens, last, out = capacity * 1000, capacity * 1000, 0, []
    for t in times_ms:
        tokens = min(full, tokens + (t - last) * per_second)   # refill since last
        last = t
        if tokens >= 1000:
            tokens -= 1000                 # spend one whole token
            out.append(True)
        else:
            out.append(False)
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(token_bucket(2, 1, [0, 0, 0, 500, 1000, 3000]), [True, True, False, False, True, True])
    check(token_bucket(1, 4, [0, 100, 250, 260]), [True, False, True, False])
    check(token_bucket(3, 1, []), [])
