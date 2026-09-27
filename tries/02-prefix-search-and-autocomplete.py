"""
Prefix Search: Walk to the prefix once, then everything below it is the answer.

Autocomplete asks a different question from "is this a word?". It asks "what
starts with this?".

Walk the prefix once — that costs one hop per typed character. The node you
land on is the root of a subtree holding exactly the words with that prefix,
so gathering the suggestions never touches the rest of the dictionary.

Lesson 2 of Tries, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/tries/prefix-search-and-autocomplete

Run it:  python tries/02-prefix-search-and-autocomplete.py
"""


trie = {"c": {"a": {"r": {"$": 1, "t": {"$": 1}}, "t": {"$": 1}}}}
def walk(prefix):                  # O(len(prefix)) — dictionary size is irrelevant
    node = trie
    for ch in prefix:
        if ch not in node: return {}
        node = node[ch]
    return node

def collect(node, so_far, out):
    if "$" in node: out.append(so_far)
    for ch in node:
        if ch != "$": collect(node[ch], so_far + ch, out)
    return out


if __name__ == "__main__":
    print(collect(walk("ca"), "ca", []))   # every word under the 'ca' branch
