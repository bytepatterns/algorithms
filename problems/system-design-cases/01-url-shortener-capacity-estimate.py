"""
URL Shortener Capacity Estimate (easy) · patterns: capacity-estimation, back-of-the-envelope

Turn the opening numbers of a URL shortener interview into a capacity
estimate. Given new short links per day, reads per write, bytes stored per
link, years of retention and a peak-to-average factor, return a dict with:
write_qps and read_qps, the average requests per second, rounded up;
peak_read_qps, reads per day times the peak factor per second, rounded up;
storage_tb, all links kept for the retention period in terabytes of 10¹²
bytes, rounded to 1 decimal; and code_length, the shortest code over 62
characters (a-z, A-Z, 0-9) with room for every link. Use 86,400 seconds per
day and 365 days per year, with integer arithmetic for the rounding up.

Examples:

    Input:  new_per_day = 100_000_000, reads_per_write = 100, bytes_per_url = 500, years = 10, peak = 3
    Output: {'write_qps': 1158, 'read_qps': 115741, 'peak_read_qps': 347223, 'storage_tb': 182.5, 'code_length': 7}
    Why:    365 billion links need 7 characters, because 62⁶ is only about 57 billion

    Input:  new_per_day = 1_000_000, reads_per_write = 10, bytes_per_url = 500, years = 5, peak = 2
    Output: {'write_qps': 12, 'read_qps': 116, 'peak_read_qps': 232, 'storage_tb': 0.9, 'code_length': 6}
    Why:    a service 100 times smaller still needs 6 characters, since 62⁵ is under a billion

    Input:  new_per_day = 1, reads_per_write = 1, bytes_per_url = 100, years = 1, peak = 1
    Output: {'write_qps': 1, 'read_qps': 1, 'peak_read_qps': 1, 'storage_tb': 0.0, 'code_length': 2}
    Why:    edge case, rounding up keeps every rate at least 1, and 365 links already overflow 62 one-character codes

Approach:
    A capacity estimate in a design interview is a handful of
    multiplications, and the value is in doing them in a fixed order that
    the interviewer can follow: per day, then per second, then over the
    retention period. Rates are rounded up because a server fleet sized for
    1157.4 writes a second is one write short, and the peak factor is
    applied before dividing so only one rounding step happens. Storage is
    the total link count times the record size, reported in decimal
    terabytes. The code length falls out of the same total: each extra
    base-62 character multiplies the space by 62, so the loop stops at the
    first length that fits, 7 characters for 365 billion links. The loop
    runs O(log total) times and everything else is constant, so time and
    space are O(1) for practical inputs.

The lesson behind it: Design a URL Shortener
    https://bytepatterns.com/learn/system-design-cases/design-a-url-shortener

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/system-design-cases/url-shortener-capacity-estimate

Run it:  python problems/system-design-cases/01-url-shortener-capacity-estimate.py
"""


def url_shortener_capacity(new_per_day, reads_per_write, bytes_per_url, years, peak):
    day = 86_400
    reads_per_day = new_per_day * reads_per_write
    total = new_per_day * 365 * years      # links kept over the retention period
    length = 1
    while 62 ** length < total:            # each character multiplies the space by 62
        length += 1
    return {
        "write_qps": -(-new_per_day // day),              # ceiling division
        "read_qps": -(-reads_per_day // day),
        "peak_read_qps": -(-reads_per_day * peak // day),
        "storage_tb": round(total * bytes_per_url / 10 ** 12, 1),
        "code_length": length,
    }


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(url_shortener_capacity(100_000_000, 100, 500, 10, 3), {'write_qps': 1158, 'read_qps': 115741, 'peak_read_qps': 347223, 'storage_tb': 182.5, 'code_length': 7})
    check(url_shortener_capacity(1_000_000, 10, 500, 5, 2), {'write_qps': 12, 'read_qps': 116, 'peak_read_qps': 232, 'storage_tb': 0.9, 'code_length': 6})
    check(url_shortener_capacity(1, 1, 100, 1, 1), {'write_qps': 1, 'read_qps': 1, 'peak_read_qps': 1, 'storage_tb': 0.0, 'code_length': 2})
