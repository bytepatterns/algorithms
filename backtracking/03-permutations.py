"""
Permutations: Every unused value is a branch; the used set is the pruning.

A permutation places every value exactly once, so at each level the branches
are whichever values are still free.

Carry a used set alongside the path. A value in the set is skipped, which
prunes the branches that would repeat it — without that test the tree grows
n to the n leaves instead of n factorial. When the path is full there is
nothing left to choose, so record a copy and unwind.

Lesson 3 of Backtracking, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/backtracking/permutations

Run it:  python backtracking/03-permutations.py
"""


def permute(nums, used, path, out):
    if len(path) == len(nums):
        out.append(path[:])
        return
    for n in nums:
        if n in used:                     # already placed on this path
            continue
        used.add(n); path.append(n)       # choose
        permute(nums, used, path, out)    # explore
        used.discard(n); path.pop()       # un-choose


if __name__ == "__main__":
    out = []
    permute([1, 2, 3], set(), [], out)
    print(len(out))
    print(out[0], out[-1])
