"""
Typeahead Top Three (medium) · patterns: trie, prefix-match

A shop has a list of distinct lowercase product names. A customer types a
search word one character at a time. After each character, suggest up to
three product names that start with everything typed so far, choosing the
alphabetically smallest ones. Return one list of suggestions per typed
character.

Examples:

    Input:  products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"], word = "mouse"
    Output: [["mobile", "moneypot", "monitor"],
             ["mobile", "moneypot", "monitor"],
             ["mouse", "mousepad"],
             ["mouse", "mousepad"],
             ["mouse", "mousepad"]]

    Input:  products = ["bag", "bags", "banner", "box"], word = "bax"
    Output: [["bag", "bags", "banner"], ["bag", "bags", "banner"], []]
    Why:    once no product matches, it stays that way for longer prefixes

    Input:  products = ["bag"], word = "cat"
    Output: [[], [], []]
    Why:    edge case, not even the first character matches

Approach:
    Inserting the products in sorted order means the first three words to
    pass through any node are the three smallest with that prefix, so each
    node can keep a short suggestion list filled during insertion and never
    touched again. Answering is then one step down the tree per typed
    character, reading the list stored there. Once a character has no child,
    no longer prefix can match either, so the walk records empty lists from
    then on. Sorting costs O(n log n) comparisons, building costs O(total
    characters), and each keystroke is O(1) plus copying at most three
    names.

The lesson behind it: Prefix Search
    https://bytepatterns.com/learn/tries/prefix-search-and-autocomplete
    python tries/02-prefix-search-and-autocomplete.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/tries/typeahead-top-three

Run it:  python problems/tries/05-typeahead-top-three.py
"""


def suggestions(products, word):
    root = {}
    for p in sorted(products):             # sorted, so the first three are the smallest
        node = root
        for ch in p:
            node = node.setdefault(ch, {"#": []})
            if len(node["#"]) < 3:
                node["#"].append(p)        # each node remembers its top three
    out, node = [], root
    for ch in word:
        node = node.get(ch) if node else None   # once off the tree, stay off
        out.append(node["#"] if node else [])
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(suggestions(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse")[2], ['mouse', 'mousepad'])
    check(suggestions(["bag", "bags", "banner", "box"], "bax"), [['bag', 'bags', 'banner'], ['bag', 'bags', 'banner'], []])
    check(suggestions(["bag"], "cat"), [[], [], []])
