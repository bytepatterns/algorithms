"""
Depth-First Search: Commit to one branch until it dead-ends, then back up.

Depth-first search takes one neighbour and goes as deep as it can before
considering the others. Recursion handles the bookkeeping: the call stack
remembers every junction you still owe a visit. The seen set is what keeps a
cycle from trapping you.

Lesson 4 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/depth-first-search

Run it:  python graphs/04-depth-first-search.py
"""


caves = {"entry": ["hall", "sump"], "hall": ["entry", "gallery"],
         "gallery": ["hall"], "sump": ["entry", "dome"], "dome": ["sump"]}

def dfs(node, seen=None):
    if seen is None:
        seen = []
    seen.append(node)                    # arrive here
    for nb in caves[node]:
        if nb not in seen:
            dfs(nb, seen)                # plunge before siblings
    return seen


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(dfs("entry"), ['entry', 'hall', 'gallery', 'sump', 'dome'])
