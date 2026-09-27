"""
Encapsulation and Invariants: Hide the state so the object can never be caught in a bad one.

An invariant is a promise about an object that holds before and after every
public call. Encapsulation is how you keep it: fields stay private, and the
only way in is a method that validates first. A rejected call changes
nothing at all.

Lesson 2 of Low-Level Design, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/lld/encapsulation-and-invariants

Run it:  python lld/02-encapsulation-and-invariants.py
"""


class Thermostat:
    def __init__(self, target): self._target = 5; self.set(target)
    def set(self, c):
        if not 5 <= c <= 30:                  # the invariant, checked at the door
            raise ValueError("outside safe range")
        self._target = c
    @property
    def target(self): return self._target     # read-only from outside


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    t = Thermostat(21)
    t.set(24)
    check(t.target, 24)
    try: t.set(80)
    except ValueError as e: print("refused:", e)  # refused: outside safe range
    check(t.target, 24)  # still a legal state
