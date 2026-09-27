"""
Strongly Connected Parts: Groups where every node can reach every other — found in two passes.

In a directed graph, mutual reachability splits the nodes into groups.
Kosaraju finds them twice over: one DFS records the order nodes finish in,
then every edge is reversed and a second DFS starts from the last finisher.
Reversal keeps each group intact but cuts the one-way roads between groups,
so each restart collects exactly one component.

Lesson 16 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/strongly-connected-components

Run it:  python graphs/16-strongly-connected-components.py
"""


g = {"a": ["b"], "b": ["c"], "c": ["a", "d"], "d": ["e"], "e": ["d"]}
order, seen = [], set()

def walk(n):
    seen.add(n)
    for m in g[n]:
        if m not in seen:
            walk(m)
    order.append(n)              # finished last, so it starts the next pass

for n in g:
    if n not in seen:
        walk(n)

rev = {n: [] for n in g}
for n in g:
    for m in g[n]:
        rev[m].append(n)         # every arrow turned around

seen, groups = set(), []
def collect(n, group):
    seen.add(n)
    group.append(n)
    for m in rev[n]:
        if m not in seen:
            collect(m, group)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    for n in reversed(order):
        if n not in seen:
            group = []
            collect(n, group)
            groups.append(sorted(group))

    check(groups, [['a', 'b', 'c'], ['d', 'e']])
