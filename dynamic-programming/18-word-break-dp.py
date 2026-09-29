"""
Word Break: A prefix is splittable if some earlier cut leaves a real word.

Walk the string left to right and ask one question per position: is this
prefix splittable? It is, if some earlier splittable cut is followed by a
word in the dictionary. The empty prefix is the base case. Greedy fails here
— a long match early on can strand the tail — so every cut point gets tried.

Lesson 18 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/word-break-dp

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python dynamic-programming/18-word-break-dp.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    words = {"code", "camp", "cam"}
    text = "codecamp"

    ok = [False] * (len(text) + 1)
    ok[0] = True                             # the empty prefix always splits
    for i in range(1, len(text) + 1):
        for j in range(i):
            if ok[j] and text[j:i] in words:   # a valid cut, then a real word
                ok[i] = True
                break

    check(ok, [True, False, False, False, True, False, False, True, True])
    check(ok[-1], True)  # "code" + "camp"; the "cam" cut is a dead end
