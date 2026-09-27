"""
Race Conditions: Two readers, one write survives.

A race condition is when the answer depends on who got there first. Two
threads read the same value, both add one to their own copy, and both write
back. One increment silently disappears — no error, no crash, just a number
that is quietly wrong.

Lesson 2 of Concurrency, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/concurrency/race-conditions

Run it:  python concurrency/02-race-conditions.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    # one shared counter, two workers, a fixed interleaving
    shared = {"count": 0}
    steps = [("A", "read"), ("B", "read"), ("A", "write"), ("B", "write")]
    local = {}

    for who, action in steps:
        if action == "read":
            local[who] = shared["count"]      # both workers see 0
        else:
            local[who] += 1
            shared["count"] = local[who]      # the later write erases the earlier

    check(shared["count"], 1)  # two increments, one survivor
