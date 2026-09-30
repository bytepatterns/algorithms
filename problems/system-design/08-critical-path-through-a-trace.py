"""
Critical Path Through a Trace (medium) · patterns: distributed-tracing, interval-union, tree-walk

A distributed trace is a tree of spans, each (id, parent, service, start,
end) in milliseconds, with exactly one root whose parent is None. A span's
self time is its duration minus the time covered by at least one of its
children, since children can run in parallel and overlap. Return two things:
the total self time per service, as a dict sorted by service name, and the
critical path, found by starting at the root and repeatedly stepping into
the child that ends last, taking the first listed on a tie, until a span has
no children. There are up to 100,000 spans.

Examples:

    Input:  a gateway 0-100 calls auth 5-20 and orders 20-90;
            orders calls db 25-60, cache 30-40 and db again 55-85
    Output: ({'auth': 15, 'cache': 10, 'db': 65, 'gateway': 15, 'orders': 10}, ['a', 'c', 'f'])
    Why:    the db calls overlap, so orders only covers 25-85 with children; the second db call ends last

    Input:  [("r", None, "api", 0, 50), ("p", "r", "search", 0, 50), ("q", "r", "ads", 10, 30)]
    Output: ({'ads': 20, 'api': 0, 'search': 50}, ['r', 'p'])
    Why:    the api span is fully covered by its children, so all of its time is spent waiting

    Input:  [("x", None, "web", 0, 10)]
    Output: ({'web': 10}, ['x'])
    Why:    edge case, a trace with one span spends all its time in that span

Approach:
    Self time answers where a request actually spent its time, and it has to
    be computed with an interval union: two overlapping children should not
    count their shared milliseconds twice, and a naive
    duration-minus-children would go negative on the orders span. For each
    span the children are sorted by start and swept once, adding only the
    part of each interval that reaches past what is covered so far, clipped
    to the parent's own end. The critical path follows the child that
    finished last at each level, because that child is what the parent was
    waiting on when it finished; speeding up anything off that path does not
    shorten the request. Sorting children dominates, so time is O(n log n)
    for n spans and space is O(n).

The lesson behind it: Tracing a Request
    https://bytepatterns.com/learn/system-design/tracing-a-request

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/system-design/critical-path-through-a-trace

Run it:  python problems/system-design/08-critical-path-through-a-trace.py
"""


from collections import defaultdict

def analyse_trace(spans):
    kids, by_id, root = defaultdict(list), {}, None
    for sid, parent, service, start, end in spans:
        by_id[sid] = (service, start, end)
        if parent is None:
            root = sid
        else:
            kids[parent].append(sid)
    self_time = defaultdict(int)
    for sid, (service, start, end) in by_id.items():
        covered, reached = 0, start
        for s, e in sorted((by_id[c][1], by_id[c][2]) for c in kids[sid]):
            s, e = max(s, reached), min(e, end)   # count only new, in-span time
            if e > s:
                covered += e - s
                reached = e
        self_time[service] += end - start - covered
    path, sid = [root], root
    while kids[sid]:
        sid = max(kids[sid], key=lambda c: by_id[c][2])   # the child that ends last
        path.append(sid)
    return dict(sorted(self_time.items())), path


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    spans = [
        ("a", None, "gateway", 0, 100),
        ("b", "a", "auth", 5, 20),
        ("c", "a", "orders", 20, 90),
        ("d", "c", "db", 25, 60),
        ("e", "c", "cache", 30, 40),
        ("f", "c", "db", 55, 85),
    ]
    check(analyse_trace(spans), ({'auth': 15, 'cache': 10, 'db': 65, 'gateway': 15, 'orders': 10}, ['a', 'c', 'f']))
    check(analyse_trace([("r", None, "api", 0, 50), ("p", "r", "search", 0, 50), ("q", "r", "ads", 10, 30)]), ({'ads': 20, 'api': 0, 'search': 50}, ['r', 'p']))
    check(analyse_trace([("x", None, "web", 0, 10)]), ({'web': 10}, ['x']))
