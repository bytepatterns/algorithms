"""
Disjoint Sets Basics: Every group is named by one root, and find walks up to it.

Keep one array: parent[x] is who x points at. Follow the pointers and you
stop at an element that points at itself — the root, which is the group's
name.

find walks up to that root. union finds both roots and hangs one under the
other, merging two groups with a single write.

Lesson 1 of Union-Find, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/union-find/disjoint-sets-basics

Run it:  python union-find/01-disjoint-sets-basics.py
"""


parent = list(range(6))          # everyone starts alone: parent[i] == i
def find(x):
    while parent[x] != x:        # walk up to the root
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb: return False    # already one group
    parent[ra] = rb              # hang one root under the other
    return True


if __name__ == "__main__":
    union(0, 1); union(1, 2)
    print(find(0) == find(2), find(0) == find(3))
