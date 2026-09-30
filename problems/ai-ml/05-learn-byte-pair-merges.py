"""
Learn Byte Pair Merges (hard) · patterns: byte-pair-encoding, pair-counting

Byte pair encoding builds a tokenizer's vocabulary from a corpus. Start with
every word split into single characters. Then, merges times, count every
pair of adjacent symbols across the corpus, weighting each word by how often
it occurs, pick the most frequent pair, breaking ties by the alphabetically
smallest pair, record it, and join that pair into one symbol everywhere,
left to right. Given the word counts and the number of merges, return the
learned merge rules in order. Then write encode(word, rules), which splits a
new word into tokens by replaying the rules in the order they were learned.

Examples:

    Input:  words = {"low": 5, "lower": 2, "newest": 6, "widest": 3}, merges = 4
    Output: [('e', 's'), ('es', 't'), ('l', 'o'), ('lo', 'w')]
    Why:    e s and s t both occur 9 times, and e s wins the tie alphabetically

    Input:  encode("lowest", the rules above)
    Output: ['low', 'est']
    Why:    a word never seen in training is still built from learned pieces

    Input:  encode("xyz", the rules above)
    Output: ['x', 'y', 'z']
    Why:    edge case, no rule applies, so the word falls back to single characters

Approach:
    Every distinct word is kept once, as a tuple of its current symbols with
    its corpus count, so each round costs one pass over the vocabulary
    rather than over the raw text. A Counter tallies adjacent pairs weighted
    by those counts, and min with the key (-count, pair) picks the most
    frequent pair with a deterministic alphabetical tie-break, which matters
    because different tie-breaks produce different tokenizers from the same
    corpus. One helper joins a pair wherever it occurs, scanning left to
    right so that overlapping matches like a a a are merged the same way
    every time. Encoding replays the rules in learned order, which is
    exactly how a trained tokenizer splits text it has never seen, down to
    single characters when no rule applies. Training costs O(m × L) for m
    merges over L total symbols, and encoding a word costs O(m × w) for a
    word of length w.

The lesson behind it: BPE vs WordPiece
    https://bytepatterns.com/learn/ai-ml/bpe-vs-wordpiece
    python ai-ml/23-bpe-vs-wordpiece.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/ai-ml/learn-byte-pair-merges

Run it:  python problems/ai-ml/05-learn-byte-pair-merges.py
"""


from collections import Counter

def merge(syms, pair):
    out, i = [], 0
    while i < len(syms):
        if syms[i:i + 2] == pair:
            out.append(syms[i] + syms[i + 1])      # join a non-overlapping match
            i += 2
        else:
            out.append(syms[i])
            i += 1
    return tuple(out)

def learn_bpe(word_counts, merges):
    words = {tuple(w): c for w, c in word_counts.items()}   # start from single characters
    rules = []
    for _ in range(merges):
        pairs = Counter()
        for syms, c in words.items():
            for pair in zip(syms, syms[1:]):
                pairs[pair] += c           # weight each pair by how often the word occurs
        if not pairs:
            break
        best = min(pairs, key=lambda p: (-pairs[p], p))    # most frequent, then alphabetical
        rules.append(best)
        words = {merge(syms, best): c for syms, c in words.items()}
    return rules

def encode(word, rules):
    syms = tuple(word)
    for pair in rules:                     # replay merges in the order they were learned
        syms = merge(syms, pair)
    return list(syms)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    rules = learn_bpe({"low": 5, "lower": 2, "newest": 6, "widest": 3}, 4)
    check(rules, [('e', 's'), ('es', 't'), ('l', 'o'), ('lo', 'w')])
    check(encode("lowest", rules), ['low', 'est'])
    check(encode("xyz", rules), ['x', 'y', 'z'])
