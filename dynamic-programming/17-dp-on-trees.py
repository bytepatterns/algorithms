"""
DP on Trees: Every node returns two answers: taken, and not taken.

On a tree there is no left-to-right order to sweep, so the recursion carries
the state instead. Each node returns two numbers: the best total if it is
taken, and the best if it is skipped. A parent that takes itself may only
add its children's skip values. The tree is walked once, bottom-up.

Lesson 17 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/dp-on-trees

Run it:  python dynamic-programming/17-dp-on-trees.py
"""


tree = {"a": ["b", "c"], "b": ["d", "e"], "c": [], "d": [], "e": []}
loot = {"a": 3, "b": 4, "c": 5, "d": 1, "e": 1}

def best(node):
    take, skip = loot[node], 0
    for kid in tree[node]:
        kid_take, kid_skip = best(kid)
        take += kid_skip                    # taking here forbids the children
        skip += max(kid_take, kid_skip)     # skipping here frees them
    return take, skip


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(best("b"), (4, 2))
    check(max(best("a")), 9)  # skip a, take b and c
