"""
Huffman Intuition: Merge the two rarest symbols, again and again, and the code writes itself.

Frequent symbols deserve short codes, rare ones can afford long codes.
Huffman builds that arrangement from the bottom up.

Put every symbol's count in a min-heap. Pull the two smallest, merge them
under a new parent whose count is their sum, and push it back. Repeat until
one node remains. Each merge pushes everything below it one level deeper,
which is exactly one more bit per character — so the sum of the merges is
the size of the encoded file.

Lesson 5 of Greedy, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/greedy/huffman-intuition

Run it:  python greedy/05-huffman-intuition.py
"""


if __name__ == "__main__":
    import heapq
    freqs = [2, 3, 4, 7]             # counts for d, c, b, a
    heapq.heapify(freqs)
    bits = 0
    while len(freqs) > 1:
        a = heapq.heappop(freqs)     # the two rarest symbols left
        b = heapq.heappop(freqs)
        bits += a + b                # merging adds one bit to everything below
        heapq.heappush(freqs, a + b)
    print(bits)                      # fixed 2-bit codes would cost 32
