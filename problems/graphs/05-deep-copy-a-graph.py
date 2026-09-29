"""
Deep Copy A Graph (medium) · patterns: dfs, hash-map

Given a reference to one node of a connected undirected graph, build an
independent copy of the whole graph and return the matching node. Every node
in the copy must be a new object, and the copy must have exactly the same
connections as the original. The graph may contain cycles, and an absent
reference copies to nothing.

Examples:

    Input:  a square: 1 - 2 - 3 - 4 - 1
    Output: a new square with the same four labels and the same four links

    Input:  the same square, comparing the copied node with the original
    Output: they are different objects
    Why:    sharing even one node would make it a shallow copy

    Input:  no node at all
    Output: nothing
    Why:    edge case, there is no graph to copy

Approach:
    A map from original node to its copy makes the traversal idempotent:
    arriving at a node a second time returns the copy already made instead
    of building another. The crucial ordering is that the copy is recorded
    before its neighbours are visited, because otherwise a cycle would come
    back to an unrecorded node and recurse forever. With that in place the
    neighbour lists are filled by the same routine applied to each
    neighbour. Each node and edge is handled once, so time is O(V + E) and
    space is O(V).

The lesson behind it: Depth-First Search
    https://bytepatterns.com/learn/graphs/depth-first-search
    python graphs/04-depth-first-search.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/deep-copy-a-graph

Run it:  python problems/graphs/05-deep-copy-a-graph.py
"""


class G:
    def __init__(self, val): self.val, self.nbrs = val, []

def clone(node, made=None):
    if node is None:
        return None
    made = {} if made is None else made
    if node in made:
        return made[node]            # this node was already copied
    made[node] = copy = G(node.val)  # record BEFORE recursing, so cycles stop
    copy.nbrs = [clone(nb, made) for nb in node.nbrs]
    return copy

def adjacency(node):                 # read a graph back as a plain map
    out, stack, seen = {}, [node], {node}
    while stack:
        cur = stack.pop()
        out[cur.val] = sorted(n.val for n in cur.nbrs)
        for nb in cur.nbrs:
            if nb not in seen: seen.add(nb); stack.append(nb)
    return dict(sorted(out.items()))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    a, b, c, d = G(1), G(2), G(3), G(4)
    for x, y in ((a, b), (b, c), (c, d), (d, a)): x.nbrs.append(y); y.nbrs.append(x)
    check(adjacency(clone(a)), {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]})
    check(clone(a) is a, False)
    check(clone(None), None)
