"""
Fewest Hops to the End (medium) · patterns: greedy, reach-frontier

Each position in a list holds the maximum number of steps you may hop
forward from it. You start at position 0 and the last position is always
reachable. Return the smallest number of hops that gets you there.

Examples:

    Input:  nums = [2, 3, 1, 1, 4]
    Output: 2
    Why:    hop to index 1, then straight to the end

    Input:  nums = [2, 1, 1, 1, 1]
    Output: 3
    Why:    no single hop covers more than two positions here

    Input:  nums = [0]
    Output: 0
    Why:    edge case, you already stand on the last position

Approach:
    Group the positions into layers by how many hops they need; the answer
    is the number of layers crossed. Walking left to right, keep the
    furthest index anything in the current layer can reach. Arriving at the
    current layer's right-hand edge means the layer is exhausted, so one
    more hop is spent and the frontier becomes the new edge. The loop stops
    one position early so standing on the last index never costs a hop. Time
    is O(n) and space is O(1).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/greedy/fewest-hops-to-the-end

Run it:  python problems/greedy/02-fewest-hops-to-the-end.py
"""


def fewest_hops(nums):
    hops, edge, farthest = 0, 0, 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])   # best landing from this layer
        if i == edge:                           # layer exhausted: hop once
            hops += 1
            edge = farthest
    return hops


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(fewest_hops([2, 3, 1, 1, 4]), 2)
    check(fewest_hops([2, 1, 1, 1, 1]), 3)
    check(fewest_hops([0]), 0)
