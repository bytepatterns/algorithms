"""
O(1) and O(n): One step, or every step? That's the whole difference.

O(1) means the work never changes, no matter how large the input gets. O(n)
means you touch every item once. Telling these two apart in your own code is
the fastest complexity skill to pick up.

Lesson 2 of Big-O, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/big-o/o1-and-on

Run it:  python big-o/02-o1-and-on.py
"""


def first_item(nums):
    # one lookup, same cost for any list size -> O(1)
    return nums[0]

def contains(nums, target):
    # may scan every element -> O(n)
    for x in nums:
        if x == target:
            return True
    return False


if __name__ == "__main__":
    print("Defines first_item, contains. Import this file to use them.")
