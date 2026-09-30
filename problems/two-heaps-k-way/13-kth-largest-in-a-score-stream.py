"""
Kth Largest in a Score Stream (easy) · patterns: min-heap, top-k, data-stream

A leaderboard shows the kth highest score seen so far. Build a class
KthLargest(k, scores) that starts from a list of scores and has one method,
add(score), which records a new score and returns the current kth largest
score, counting duplicates. Every call to add happens when at least k scores
have been recorded, including the new one.

Examples:

    Input:  k = 3, scores = [4, 5, 8, 2], then add 3, 5, 10, 9, 4
    Output: [4, 5, 5, 8, 8]
    Why:    after adding 3 the scores are 2 3 4 5 8 and the third largest is 4

    Input:  k = 2, scores = [0], then add -1, 1, -2, -4, 3
    Output: [-1, 0, 0, 0, 1]
    Why:    the first add makes two scores, so the second largest is the smaller of them

    Input:  k = 1, scores = [], then add -3, -2, -4, 0, 4
    Output: [-3, -2, -2, 0, 4]
    Why:    edge case, with k = 1 the answer is simply the maximum so far

Approach:
    The kth largest of a growing collection is the smallest member of its
    top k, so a min-heap capped at k holds exactly the information needed.
    Each new score is pushed; if that makes k + 1 scores, the smallest is
    popped, because it now has at least k scores above it and will never be
    the answer again. The top of the heap is then the kth largest. Sorting
    the whole list on every call would cost O(n log n) per score and keep
    every score forever; the heap costs O(log k) per score and O(k) space no
    matter how long the stream runs, which is the point of the top-k pattern
    on a stream.

The lesson behind it: Top K in a Stream
    https://bytepatterns.com/learn/two-heaps-k-way/top-k-frequent-stream
    python two-heaps-k-way/03-top-k-frequent-stream.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/two-heaps-k-way/kth-largest-in-a-score-stream

Run it:  python problems/two-heaps-k-way/13-kth-largest-in-a-score-stream.py
"""


import heapq

class KthLargest:
    def __init__(self, k, scores):
        self.k = k
        self.heap = []                          # the k largest so far, smallest on top
        for s in scores:
            self.add(s)

    def add(self, score):
        heapq.heappush(self.heap, score)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)            # it has k scores above it now
        return self.heap[0]

def run(k, scores, adds):
    board = KthLargest(k, scores)
    return [board.add(s) for s in adds]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run(3, [4, 5, 8, 2], [3, 5, 10, 9, 4]), [4, 5, 5, 8, 8])
    check(run(2, [0], [-1, 1, -2, -4, 3]), [-1, 0, 0, 0, 1])
    check(run(1, [], [-3, -2, -4, 0, 4]), [-3, -2, -2, 0, 4])
