"""
What Is Dynamic Programming?: Solve each overlapping subproblem once, then reuse the answer.

Dynamic programming applies when two things are true: the same subproblem
keeps reappearing, and the best whole answer is built from best sub-answers.
Merge sort splits into fresh halves that never overlap, so caching buys
nothing. Fibonacci's branches collide constantly, so caching buys
everything. You already did this by hand in Memoization — DP is that habit,
made deliberate.

Lesson 1 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/what-is-dp

Run it:  python dynamic-programming/01-what-is-dp.py
"""


from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):                       # the same n is asked for again and again
    return n if n < 2 else fib(n - 1) + fib(n - 2)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(fib(50), 12586269025)  # instant, because nothing repeats
    print(fib.cache_info().hits)      # reads that skipped a whole subtree
