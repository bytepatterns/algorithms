"""
Jump Game: Carry one number: the furthest index still in reach.

Each cell says how far you may jump from it, and you want to know whether
the last cell is reachable at all.

You never need the route. Walk left to right carrying the furthest index you
could get to; at each position, stretch that frontier with i + nums[i]. If a
position sits past the frontier it can never be stepped on, so the answer is
no. Reach the end and it is yes.

Lesson 3 of Greedy, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/greedy/jump-game

Run it:  python greedy/03-jump-game.py
"""


def can_finish(nums):
    reach = 0
    for i, jump in enumerate(nums):
        if i > reach:                    # this index was never reachable
            return False
        reach = max(reach, i + jump)     # furthest index now in range
    return True


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(can_finish([2, 3, 1, 1, 4]), True)
    check(can_finish([3, 2, 1, 0, 4]), False)
