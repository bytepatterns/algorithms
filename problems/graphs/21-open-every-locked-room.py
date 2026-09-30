"""
Open Every Locked Room (easy) · patterns: dfs, reachability

An escape room has n rooms numbered 0 to n - 1. Room 0 is open and every
other room starts locked. Inside room i lies a list of keys, rooms[i], and a
key with number j opens room j. Keys can be used any number of times and in
any order. Return True if you can get into every room. There are up to 1,000
rooms and up to 3,000 keys in total.

Examples:

    Input:  rooms = [[1], [2], [3], []]
    Output: True
    Why:    room 0 holds key 1, room 1 holds key 2, room 2 holds key 3

    Input:  rooms = [[1, 3], [3, 0, 1], [2], [0]]
    Output: False
    Why:    the only key to room 2 is locked inside room 2 itself

    Input:  rooms = [[]]
    Output: True
    Why:    edge case, the only room is already open

Approach:
    The rooms and keys form a directed graph, with an edge from room i to
    every room whose key lies in room i, and a room can be entered exactly
    when it is reachable from room 0. A depth-first search from room 0 marks
    every reachable room; an explicit stack avoids deep recursion on a long
    chain of rooms. Every room is pushed at most once and every key is
    looked at once, so time is O(n + k) for n rooms and k keys, and space is
    O(n).

The lesson behind it: Depth-First Search
    https://bytepatterns.com/learn/graphs/depth-first-search
    python graphs/04-depth-first-search.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/open-every-locked-room

Run it:  python problems/graphs/21-open-every-locked-room.py
"""


def can_open_all(rooms):
    seen = {0}
    stack = [0]
    while stack:
        room = stack.pop()
        for key in rooms[room]:
            if key not in seen:          # a room we have not entered yet
                seen.add(key)
                stack.append(key)
    return len(seen) == len(rooms)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(can_open_all([[1], [2], [3], []]), True)
    check(can_open_all([[1, 3], [3, 0, 1], [2], [0]]), False)
    check(can_open_all([[]]), True)
