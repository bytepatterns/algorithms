"""
Serialize a Tree: Write the gaps down and the shape survives the trip.

A tree has to survive being written to a file or sent over a socket.
Preorder gives the values in a usable order, and a marker for every absent
child records the shape.

Rebuilding is the same walk in reverse: take the next token, then build the
left subtree, then the right. The stream is read once, strictly forwards.

Lesson 12 of Trees & BST, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/trees/serialize-and-deserialize

Run it:  python trees/12-serialize-and-deserialize.py
"""


class Node:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

def dump(n):                                   # preorder, with a mark for every gap
    if not n: return ["#"]
    return [str(n.val)] + dump(n.left) + dump(n.right)

def load(tokens):
    t = tokens.pop(0)                          # the stream is read strictly in order
    if t == "#": return None
    return Node(int(t), load(tokens), load(tokens))   # left first, exactly as written


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import re

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


def _same(printed, expected):
    """Printed text vs the lesson's comment, which may add a note after it."""
    printed, expected = printed.strip(), expected.strip()
    wants = [expected] + [expected.rsplit(s, 1)[1].strip() for s in (" -> ", " = ") if s in expected]
    for want in wants + [w[1:] for w in wants if w.startswith("~")]:
        rest = want[len(printed):] if want.startswith(printed) else None
        if rest == "" or (rest and re.match(r"[\s,;:]+([A-Za-z]|\u2014|\u2013|-(?!\d)|\u2192|<-|\([A-Za-z]|#)", rest)):
            return True
    return False


def check_printed(*values, expect, sep=" ", end="\n"):
    """print(*values), then assert the line reads the way the lesson's comment says."""
    print(*values, sep=sep, end=end)
    forms = [sep.join(map(str, values))]
    if len(values) == 1 and isinstance(values[0], str):
        forms += [repr(values[0]), '"%s"' % values[0]] + (["(empty string)"] if not values[0] else [])
    if len(values) > 1 and isinstance(values[0], str):  # a leading label
        forms.append(sep.join(map(str, values[1:])))
    assert any(_same(f, expect) for f in forms), f"expected {expect!r}, got {forms[0]!r}"


if __name__ == "__main__":
    root = Node(1, Node(2), Node(3, Node(4), Node(5)))
    text = ",".join(dump(root))
    check_printed(text, expect="1,2,#,#,3,4,#,#,5,#,#")
    check(dump(load(text.split(","))) == dump(root), True)
