"""
Least Recently Used Cache (medium) · patterns: doubly-linked-list, hash-map, sentinel-nodes

Build a fixed-size cache for an API gateway. LRUCache(capacity) creates it;
get(key) returns the stored value, or -1 if the key is missing; put(key,
value) inserts or updates a key. Both calls count as a use of the key. When
a put would push the cache past its capacity, first evict the key that was
used longest ago. Both operations must run in O(1) time, and the capacity is
between 1 and 3,000. Build the ordering yourself with a doubly linked list
instead of using OrderedDict.

Examples:

    Input:  capacity = 2
            put(1, 1), put(2, 2), get(1), put(3, 3), get(2), put(4, 4), get(1), get(3), get(4)
    Output: [1, -1, -1, 3, 4]
    Why:    put(3, 3) evicts 2 because get(1) just used 1; put(4, 4) then evicts 1

    Input:  capacity = 2
            put(1, 1), put(2, 2), put(1, 10), put(3, 3), get(1), get(2)
    Output: [10, -1]
    Why:    updating key 1 also counts as a use, so key 2 is the one evicted

    Input:  capacity = 1
            put(1, 1), put(2, 2), get(1), get(2)
    Output: [-1, 2]
    Why:    edge case, every new key evicts the only one stored

Approach:
    The cache needs two things in constant time: finding a key, and knowing
    which key is the stalest. A dictionary from key to list node handles the
    first, and a doubly linked list ordered by use handles the second. Every
    get or put moves the key's node to the front, which is O(1) because the
    node knows its own neighbours and can be spliced out without a search.
    Eviction removes the node just before the tail sentinel and deletes its
    key from the dictionary, which is why each node stores its key as well
    as its value. The head and tail sentinels are permanent, so every real
    node always has both neighbours and no pointer update needs a special
    case. Each operation is O(1), and space is O(capacity).

The lesson behind it: Doubly Linked Lists
    https://bytepatterns.com/learn/linked-lists/doubly-linked-lists
    python linked-lists/10-doubly-linked-lists.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/linked-lists/least-recently-used-cache

Run it:  python problems/linked-lists/12-least-recently-used-cache.py
"""


class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val, self.prev, self.next = key, val, None, None

class LRUCache:
    def __init__(self, capacity):
        self.capacity, self.nodes = capacity, {}
        self.head, self.tail = Node(), Node()        # sentinels, never evicted
        self.head.next, self.tail.prev = self.tail, self.head

    def _unlink(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _push_front(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        node = self.nodes.get(key)
        if node is None:
            return -1
        self._unlink(node)
        self._push_front(node)                        # now the most recent
        return node.val

    def put(self, key, val):
        if key in self.nodes:
            node = self.nodes[key]
            node.val = val
            self._unlink(node)
        else:
            if len(self.nodes) == self.capacity:
                stalest = self.tail.prev
                self._unlink(stalest)
                del self.nodes[stalest.key]
            node = self.nodes[key] = Node(key, val)
        self._push_front(node)

def run(capacity, ops):
    cache, out = LRUCache(capacity), []
    for op in ops:
        if op[0] == "put":
            cache.put(op[1], op[2])
        else:
            out.append(cache.get(op[1]))
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    first = [("put", 1, 1), ("put", 2, 2), ("get", 1), ("put", 3, 3), ("get", 2),
             ("put", 4, 4), ("get", 1), ("get", 3), ("get", 4)]
    second = [("put", 1, 1), ("put", 2, 2), ("put", 1, 10), ("put", 3, 3), ("get", 1), ("get", 2)]
    third = [("put", 1, 1), ("put", 2, 2), ("get", 1), ("get", 2)]
    check(run(2, first), [1, -1, -1, 3, 4])
    check(run(2, second), [10, -1])
    check(run(1, third), [-1, 2])
