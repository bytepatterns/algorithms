"""
Strategy Pattern: Put the part that varies in its own object and swap it at runtime.

Find the one step that keeps changing, lift it into its own object with a
fixed method name, and have the surrounding workflow call it. The workflow
stops caring which variant is loaded, and adding a sixth variant never
reopens it.

Lesson 6 of Low-Level Design, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/lld/strategy-pattern

Run it:  python lld/06-strategy-pattern.py
"""


def slicks(base): return base * 1.0      # dry: full grip
def wets(base):   return base * 0.8      # safe in rain, slower
def gravel(base): return base * 0.6

class Stage:
    def __init__(self, tyres): self.tyres = tyres   # the swappable step
    def time(self, base): return round(120 / self.tyres(base), 2)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    s = Stage(slicks)
    check(s.time(1), 120.0)
    s.tyres = wets                           # swapped between runs; Stage untouched
    check(s.time(1), 150.0)
    check(Stage(gravel).time(1), 200.0)
