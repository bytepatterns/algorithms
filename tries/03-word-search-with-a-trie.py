"""
Word Search With a Trie: One walk over the grid, pruned the moment the path stops being a prefix.

Searching a grid for one word is a depth-first walk. Searching for fifty
words that way is fifty walks.

Put the word list in a trie and the walk carries a trie node with it. Every
step checks one thing: is this letter a child? If not, no word can grow here
and the entire branch dies — that pruning is the whole win.

Lesson 3 of Tries, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/tries/word-search-with-a-trie

Run it:  python tries/03-word-search-with-a-trie.py
"""


grid = [["c", "a", "r"], ["x", "t", "y"]]
trie = {"c": {"a": {"r": {"$": 1}, "t": {"$": 1}}}}
found = set()
def dfs(r, c, node, word):
    ch = grid[r][c]
    if ch not in node: return          # dead prefix — prune this branch
    node, word = node[ch], word + ch
    if "$" in node: found.add(word)
    grid[r][c] = "#"                   # no cell twice inside one word
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if 0 <= r + dr < 2 and 0 <= c + dc < 3:
            dfs(r + dr, c + dc, node, word)
    grid[r][c] = ch                    # put it back for other paths


if __name__ == "__main__":
    for r, c in [(r, c) for r in range(2) for c in range(3)]: dfs(r, c, trie, "")
    print(sorted(found))
