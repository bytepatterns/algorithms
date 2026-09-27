"""
Tokenization: Models read chunks, not letters or words.

Before a model sees text, the text is split into tokens: subword chunks from
a fixed vocabulary learned from data. Frequent words become one token; rare
names and odd spellings break into several pieces.

Lesson 5 of AI & ML, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/ai-ml/tokenization

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python ai-ml/05-tokenization.py
"""


vocab = ["token", "ization", "un", "believ", "able"]

def tokenize(text):
    out, i = [], 0
    while i < len(text):
        hits = [v for v in vocab if text.startswith(v, i)]
        if not hits:                       # no entry fits: emit one character
            out.append(text[i]); i += 1
            continue
        piece = max(hits, key=len)         # greedy longest match
        out.append(piece); i += len(piece)
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(tokenize("tokenization"), ['token', 'ization'])
    check(tokenize("unbelievable"), ['un', 'believ', 'able'])
