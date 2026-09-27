"""
Topological Sort: Order the steps so nothing runs before what it depends on.

Some jobs must precede others, and the rest are free to happen in any order.
Model each job as a node and each "must come first" rule as a directed edge.
Kahn's algorithm repeatedly outputs any job whose blockers are all done.
Leftovers at the end mean a cycle.

Lesson 8 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/topological-sort

Run it:  python graphs/08-topological-sort.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    after = {"unpack": ["frame", "legs"], "frame": ["top"], "legs": ["top"],
             "top": ["cushion"], "cushion": []}
    indeg = {n: 0 for n in after}
    for n in after:
        for m in after[n]:
            indeg[m] += 1                    # count each step's blockers
    order, ready = [], [n for n in after if indeg[n] == 0]
    while ready:
        n = ready.pop(0)                     # nothing is waiting on it
        order.append(n)
        for m in after[n]:
            indeg[m] -= 1
            if indeg[m] == 0:                # its last blocker cleared
                ready.append(m)
    check(order, ['unpack', 'frame', 'legs', 'top', 'cushion'])
