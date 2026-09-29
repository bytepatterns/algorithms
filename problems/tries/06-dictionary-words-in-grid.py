"""
Dictionary Words In A Grid (hard) · patterns: trie, backtracking, grid-dfs

You are given a grid of lowercase letters and a list of distinct words. A
word is present if it can be spelled by a path that starts on any cell and
moves up, down, left or right one cell at a time, never using the same cell
twice within that word. Return every present word, each once, in
alphabetical order.

Examples:

    Input:  grid = [["o", "a", "a", "n"],
                    ["e", "t", "a", "e"],
                    ["i", "h", "k", "r"],
                    ["i", "f", "l", "v"]],
            words = ["oath", "pea", "eat", "rain"]
    Output: ["eat", "oath"]

    Input:  grid = [["a", "b"],
                    ["c", "d"]], words = ["abdc", "abcb"]
    Output: ["abdc"]
    Why:    "abcb" would need the b cell twice

    Input:  grid = [["a"]], words = ["a", "aa"]
    Output: ["a"]
    Why:    edge case, a one-cell grid can only spell one-letter words

Approach:
    The trie lets one depth-first walk test every word at once: the walk
    only continues while the letters so far form the start of some word,
    which cuts off almost every branch early. Blanking the current cell
    during the recursion and restoring it afterwards is the backtracking
    step that stops a path from reusing a cell. Popping a word's marker when
    it is found guarantees each word is reported once, and deleting trie
    branches that become empty stops later searches from wandering into
    finished words. In the worst case the time is O(cells times 4 times 3 to
    the L minus 1) for words of length up to L, but the pruning keeps real
    inputs far below that; space is O(total word characters).

The lesson behind it: Word Search With a Trie
    https://bytepatterns.com/learn/tries/word-search-with-a-trie
    python tries/03-word-search-with-a-trie.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/tries/dictionary-words-in-grid

Run it:  python problems/tries/06-dictionary-words-in-grid.py
"""


def find_words(grid, words):
    trie, found = {}, []
    for w in words:
        node = trie
        for ch in w:
            node = node.setdefault(ch, {})
        node["$"] = w                                  # the word that ends here
    def dfs(r, c, parent):
        ch = grid[r][c]
        node = parent[ch]
        if "$" in node:
            found.append(node.pop("$"))                # report each word once
        grid[r][c] = "#"                               # this cell is in use
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] in node:
                dfs(nr, nc, node)
        grid[r][c] = ch                                # un-choose
        if not node:
            parent.pop(ch)                             # prune a finished branch
    for r, c in [(r, c) for r in range(len(grid)) for c in range(len(grid[0]))]:
        if grid[r][c] in trie:
            dfs(r, c, trie)
    return sorted(found)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(find_words([list("oaan"), list("etae"), list("ihkr"), list("iflv")],
                     ["oath", "pea", "eat", "rain"]), ['eat', 'oath'])
    check(find_words([list("ab"), list("cd")], ["abdc", "abcb"]), ['abdc'])
    check(find_words([["a"]], ["a", "aa"]), ['a'])
