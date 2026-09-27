"""
Cycles in a Directed Graph: Grey means still on the path — meet grey again and you have looped.

One visited set cannot distinguish two very different situations: a node you
finished long ago, and a node still sitting open on the path beneath you.
Three colours can. White is untouched, grey is on the current path, black is
finished. An edge into grey is a back edge, and a back edge is a cycle.

Lesson 13 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/directed-cycle-colours

Run it:  python graphs/13-directed-cycle-colours.py
"""


g = {"build": ["test"], "test": ["deploy"], "deploy": ["build"], "docs": []}
colour = {n: "white" for n in g}

def visit(n):
    colour[n] = "grey"                   # on the current path
    for m in g[n]:
        if colour[m] == "grey":          # back edge: the path bites itself
            return True
        if colour[m] == "white" and visit(m):
            return True
    colour[n] = "black"                  # finished, never on a path again
    return False


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(any(visit(n) for n in g if colour[n] == "white"), True)
