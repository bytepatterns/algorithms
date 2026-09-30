"""
Event Bus With Topic Wildcards (medium) · patterns: observer, topic-matching

Design an in-process event bus. subscribe(pattern, handler) registers a
handler and returns a token, and unsubscribe(token) removes it again. Topics
are dot-separated, such as order.paid, and in a pattern a ` matches exactly
one segment, so order. matches order.paid but neither order nor
order.paid.late. publish(topic, payload) calls every matching handler in the
order they subscribed and returns how many were called. A handler that
raises must not stop the handlers after it; the bus counts the failure in
failures` and carries on.

Examples:

    Input:  subscribe("order.*", audit), subscribe("order.paid", broken), subscribe("order.paid", ship)
            publish("order.paid", "o7")
    Output: 3, log = ['audit o7', 'ship o7'], failures = 1
    Why:    broken raised, but ship still ran after it

    Input:  then unsubscribe(the audit token), publish("order.created", "o8")
    Output: 0
    Why:    the only handler for order.* is gone, and order.paid does not match

    Input:  then publish("order.paid.late", "o9")
    Output: 0
    Why:    edge case, a * never stretches over two segments

Approach:
    A dict from token to (pattern, handler) gives both requirements at once:
    Python dicts keep insertion order, so handlers run in subscription
    order, and a token removes one subscription in O(1) without disturbing
    the others. Patterns are split into segments when they are registered,
    so matching a topic is a same-length check plus one comparison per
    segment, and a * can only ever stand for one segment. Each handler runs
    inside its own try/except, which isolates a failing observer from the
    rest, the main promise of an event bus. publish iterates over a copy of
    the subscriptions so a handler that unsubscribes during delivery cannot
    break the loop. A publish costs O(s × d) for s subscriptions and d
    segments.

The lesson behind it: Observer Pattern
    https://bytepatterns.com/learn/lld/observer-pattern
    python lld/07-observer-pattern.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/lld/event-bus-with-topic-wildcards

Run it:  python problems/lld/04-event-bus-with-topic-wildcards.py
"""


class EventBus:
    def __init__(self):
        self.subs, self.next_id, self.failures = {}, 0, 0

    def subscribe(self, pattern, handler):
        self.next_id += 1
        self.subs[self.next_id] = (pattern.split("."), handler)
        return self.next_id                # the token to unsubscribe with

    def unsubscribe(self, token):
        self.subs.pop(token, None)

    def publish(self, topic, payload):
        called, parts = 0, topic.split(".")
        for pattern, handler in list(self.subs.values()):     # subscription order
            if len(pattern) == len(parts) and all(p in ("*", t) for p, t in zip(pattern, parts)):
                called += 1
                try:
                    handler(payload)
                except Exception:
                    self.failures += 1     # one bad handler never silences the rest
        return called


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import re

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


def _same(printed, expected):
    """Printed text vs the lesson's comment, which may add a note after it."""
    printed, expected = printed.strip(), expected.strip()
    wants = [expected] + [expected.rsplit(s, 1)[1].strip() for s in (" -> ", " = ") if s in expected]
    for want in wants + [w[1:] for w in wants if w.startswith("~")]:
        rest = want[len(printed):] if want.startswith(printed) else None
        if rest == "" or (rest and re.match(r"[\s,;:]+([A-Za-z]|\u2014|\u2013|-(?!\d)|\u2192|<-|\([A-Za-z]|#)", rest)):
            return True
    return False


def check_printed(*values, expect, sep=" ", end="\n"):
    """print(*values), then assert the line reads the way the lesson's comment says."""
    print(*values, sep=sep, end=end)
    forms = [sep.join(map(str, values))]
    if len(values) == 1 and isinstance(values[0], str):
        forms += [repr(values[0]), '"%s"' % values[0]] + (["(empty string)"] if not values[0] else [])
    if len(values) > 1 and isinstance(values[0], str):  # a leading label
        forms.append(sep.join(map(str, values[1:])))
    assert any(_same(f, expect) for f in forms), f"expected {expect!r}, got {forms[0]!r}"


if __name__ == "__main__":
    log = []
    bus = EventBus()
    audit = bus.subscribe("order.*", lambda p: log.append("audit " + p))
    bus.subscribe("order.paid", lambda p: 1 / 0)
    bus.subscribe("order.paid", lambda p: log.append("ship " + p))
    check_printed(bus.publish("order.paid", "o7"), log, bus.failures, expect="3 ['audit o7', 'ship o7'] 1")
    bus.unsubscribe(audit)
    check(bus.publish("order.created", "o8"), 0)
    check(bus.publish("order.paid.late", "o9"), 0)
