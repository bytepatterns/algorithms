"""
Back and Forward History (easy) · patterns: doubly-linked-list, design

Simulate the history of a single browser tab that starts on a home page. A
visit opens a new page after the current one and throws away every page you
could previously have gone forward to. A back of k moves up to k pages
towards the start, and a forward of k moves up to k pages towards the newest
one, stopping early when there is nowhere left to go. Given the home page
and a list of operations, return the page you are on after each back or
forward, in order.

Examples:

    Input:  home = "home"
            ops  = [("visit", "a"), ("visit", "b"), ("back", 1),
                    ("visit", "c"), ("forward", 1), ("back", 5)]
    Output: ['a', 'c', 'home']
    Why:    visiting c from a drops b, so forward has nowhere to go

    Input:  home = "x", ops = [("back", 2), ("forward", 3)]
    Output: ['x', 'x']
    Why:    edge case, a fresh tab cannot move either way

Approach:
    Each page is a node with links to the page before and after it, and a
    pointer marks where the tab is. A visit hangs a new node after the
    current one, which silently cuts off the old forward pages, then moves
    onto it. Back and forward follow prev or next links one step at a time
    and stop at the first missing link, so overshooting is harmless. A visit
    is O(1), a move of k steps is O(k), and space is O(number of visits).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/linked-lists/back-forward-history

Run it:  python problems/linked-lists/08-back-forward-history.py
"""


class Page:
    def __init__(self, url, prev=None): self.url, self.prev, self.next = url, prev, None
def run_history(home, ops):
    current, seen = Page(home), []
    for op, arg in ops:
        if op == "visit":
            current.next = Page(arg, current)   # the old forward pages become unreachable
            current = current.next
            continue
        for _ in range(arg):                    # back or forward, at most arg steps
            step = current.prev if op == "back" else current.next
            if step is None:
                break
            current = step
        seen.append(current.url)
    return seen


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run_history("home", [("visit", "a"), ("visit", "b"), ("back", 1), ("visit", "c"), ("forward", 1), ("back", 5)]), ['a', 'c', 'home'])
    check(run_history("x", [("back", 2), ("forward", 3)]), ['x', 'x'])
    check(run_history("x", []), [])
