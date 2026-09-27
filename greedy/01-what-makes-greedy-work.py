"""
What Makes Greedy Work: Take the best move now — but only when it can never block a better answer.

A greedy algorithm takes the move that looks best right now and never
revisits it. No search tree, no undo — one pass.

That is only correct when a local win can never cost you a better global
answer. The usual proof is an exchange argument: take any optimal answer,
swap the greedy choice into it, and show the result is still optimal. If
that swap always survives, greedy is safe. One counterexample and it is not.

Lesson 1 of Greedy, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/greedy/what-makes-greedy-work

Run it:  python greedy/01-what-makes-greedy-work.py
"""


def greedy_coins(coins, amount):
    used = 0
    for c in sorted(coins, reverse=True):   # biggest coin first
        used += amount // c                 # take as many as still fit
        amount %= c
    return used


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(greedy_coins([25, 10, 5, 1], 30), 2)  # and 2 is optimal
    check(greedy_coins([1, 3, 4], 6), 3)  # but 3 + 3 is only 2
