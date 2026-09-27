"""
Equal Split: Can any subset hit exactly half the total? Track reachable sums.

Splitting a set into two equal halves sounds like a search over subsets. It
is really 0/1 knapsack with the values thrown away: mark sum zero as
reachable, then let each number extend every sum already marked. If half the
total lights up, the split exists. Backwards iteration keeps each number
single-use.

Lesson 13 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/partition-equal-subset

Run it:  python dynamic-programming/13-partition-equal-subset.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    nums = [3, 3, 4, 2]
    total = sum(nums)
    half = total // 2

    can = [False] * (half + 1)
    can[0] = True                        # the empty subset reaches zero
    for n in nums:
        for s in range(half, n - 1, -1):   # backwards: each number used once
            can[s] = can[s] or can[s - n]

    check(can, [True, False, True, True, True, True, True])
    check(total % 2 == 0 and can[half], True)  # 3 + 3 against 4 + 2
