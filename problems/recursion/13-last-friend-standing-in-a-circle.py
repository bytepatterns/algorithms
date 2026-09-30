"""
Last Friend Standing in a Circle (medium) · patterns: recursion, josephus, recurrence

n friends numbered 1 to n sit in a circle. Starting from friend 1, count k
friends clockwise, counting the starting friend as 1; the friend you land on
leaves the circle. The count starts again from the friend just after the one
who left, and this repeats until one friend remains. Return that friend's
number.

Examples:

    Input:  n = 5, k = 2
    Output: 3
    Why:    friends leave in the order 2, 4, 1, 5

    Input:  n = 6, k = 5
    Output: 1
    Why:    friends leave in the order 5, 4, 6, 2, 3

    Input:  n = 1, k = 7
    Output: 1
    Why:    edge case, a circle of one has its winner already

Approach:
    After the first elimination, the remaining n - 1 friends play exactly
    the same game, only relabelled: the friend k seats after the start is
    now seat 0. So if you know where the winner sits in the smaller game,
    shifting that seat by k modulo n gives the winner's seat in the bigger
    game, and the smaller game is solved the same way until one friend is
    left at seat 0. The recursive version mirrors that argument and is easy
    to trust; it also pushes one frame per friend, so n in the thousands
    meets Python's recursion limit. The loop runs the same recurrence from 1
    up to n and needs no stack. Both take O(n) time, with O(n) and O(1)
    space respectively.

The lesson behind it: The Call Stack
    https://bytepatterns.com/learn/recursion/call-stack-visualized
    python recursion/02-call-stack-visualized.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/recursion/last-friend-standing-in-a-circle

Run it:  python problems/recursion/13-last-friend-standing-in-a-circle.py
"""


def last_friend(n, k):
    def seat(m):                          # 0-based winning seat among m friends
        if m == 1:
            return 0
        return (seat(m - 1) + k) % m      # the smaller game, shifted k seats round
    return seat(n) + 1

def last_friend_loop(n, k):
    s = 0
    for m in range(2, n + 1):             # the same recurrence, bottom up
        s = (s + k) % m
    return s + 1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(last_friend(5, 2), 3)
    check(last_friend(6, 5), 1)
    check(last_friend(1, 7), 1)
    check(last_friend_loop(100000, 2), 68929)
