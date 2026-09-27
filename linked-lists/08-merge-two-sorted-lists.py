"""
Merge Two Sorted Lists: Zip two ordered chains together without allocating a single node.

Both chains are already ordered, so you never compare more than their two
front nodes. Take the smaller, advance that side, repeat.

Nothing is allocated: you are re-pointing next fields on nodes that already
exist. A dummy head means the very first node is not a special case.

Lesson 8 of Linked Lists, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/linked-lists/merge-two-sorted-lists

Run it:  python linked-lists/08-merge-two-sorted-lists.py
"""


class Node:
    def __init__(self, v, nxt=None): self.val, self.next = v, nxt

def merge(a, b):
    dummy = tail = Node(0)                 # fake head: no "first node" special case
    while a and b:
        if a.val <= b.val: tail.next, a = a, a.next
        else:              tail.next, b = b, b.next
        tail = tail.next                   # tail is always the last node taken
    tail.next = a or b                     # one side ran out: append the rest whole
    return dummy.next

def build(vals): return Node(vals[0], build(vals[1:])) if vals else None


if __name__ == "__main__":
    node = merge(build([1, 4, 7]), build([2, 3, 9]))
    while node: print(node.val, end=" "); node = node.next   # 1 2 3 4 7 9
