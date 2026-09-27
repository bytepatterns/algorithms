"""
Union by Rank or Size: Hang the smaller tree under the bigger one and depth barely grows.

union has a choice: which root goes under which. Choose badly every time and
the structure degrades into a chain.

Keep a size per root and always hang the smaller tree under the bigger one.
Only the smaller side gets deeper, so depth can only grow when two equal
trees meet — which takes doubling to reach.

Lesson 3 of Union-Find, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/union-find/union-by-size

Run it:  python union-find/03-union-by-size.py
"""


parent, size = list(range(5)), [1] * 5
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]         # halve the path on the way up
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb: return
    if size[ra] > size[rb]: ra, rb = rb, ra   # smaller root goes underneath
    parent[ra] = rb
    size[rb] += size[ra]


if __name__ == "__main__":
    union(0, 1); union(2, 3); union(1, 3)
    print(find(0) == find(2), size[find(0)])
