"""
Fewest Roads to Link Every Town (hard) · patterns: strongly-connected-components, directed-graph

There are n towns, numbered 0 to n - 1, joined by one-way roads given as
pairs (from, to). You may build new one-way roads between any two towns.
Return the fewest new roads needed so that every town can reach every other
town.

Examples:

    Input:  n = 5, roads = [(0, 1), (1, 2), (2, 0), (3, 2), (3, 4)]
    Output: 2
    Why:    0, 1, 2 already form a loop; 3 has no way in, and both the loop
            and 4 have no way out, so two roads are needed, e.g. 2 -> 3 and 4 -> 3

    Input:  n = 3, roads = [(0, 1), (1, 2), (2, 0)]
    Output: 0
    Why:    the three roads already form one loop through every town

    Input:  n = 3, roads = []
    Output: 3
    Why:    edge case, no roads at all: a loop of three new roads is the cheapest fix

Approach:
    Collapsing each strongly connected component to one point leaves a graph
    with no cycles. A group with no incoming road can only be reached
    through a new road that ends in it, and a group with no outgoing road
    needs a new road that starts in it, so the answer is at least the larger
    of those two counts. That many roads is also enough when they are laid
    out to chain the dead ends back into the starts, a known result for
    acyclic graphs, and with a single component nothing is needed. The
    components come from Kosaraju's two passes, written with explicit stacks
    so a long chain of towns cannot overflow Python's recursion. Time is O(n
    + r) for r roads, and space is O(n + r).

The lesson behind it: Strongly Connected Parts
    https://bytepatterns.com/learn/graphs/strongly-connected-components
    python graphs/16-strongly-connected-components.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/fewest-roads-to-link-every-town

Run it:  python problems/graphs/15-fewest-roads-to-link-every-town.py
"""


def roads_to_add(n, roads):
    out, back = [[] for _ in range(n)], [[] for _ in range(n)]
    for u, v in roads: out[u].append(v); back[v].append(u)
    order, seen = [], [False] * n
    for s in range(n):                        # pass 1: record finish order
        if seen[s]: continue
        seen[s], stack = True, [(s, iter(out[s]))]
        while stack:
            v, it = stack[-1]
            nxt = next((u for u in it if not seen[u]), None)
            if nxt is None: order.append(v); stack.pop()
            else: seen[nxt] = True; stack.append((nxt, iter(out[nxt])))
    comp, c = [-1] * n, 0
    for s in reversed(order):                 # pass 2: reversed roads, latest finish first
        if comp[s] != -1: continue
        comp[s], stack = c, [s]
        while stack:
            for u in back[stack.pop()]:
                if comp[u] == -1: comp[u] = c; stack.append(u)
        c += 1
    if c == 1: return 0
    has_in, has_out = [False] * c, [False] * c
    for u, v in roads:
        if comp[u] != comp[v]: has_out[comp[u]] = has_in[comp[v]] = True
    return max(has_in.count(False), has_out.count(False))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(roads_to_add(5, [(0, 1), (1, 2), (2, 0), (3, 2), (3, 4)]), 2)
    check(roads_to_add(3, [(0, 1), (1, 2), (2, 0)]), 0)
    check(roads_to_add(3, []), 3)
