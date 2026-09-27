"""
Designing a File System: One contract answered by both a leaf and a whole subtree.

Name one contract — an entry that can report its size. A File answers from
its own bytes; a Folder answers by asking everything it holds and adding up.

Nesting then costs nothing: a folder of folders is just a folder whose
children answer the same question.

Lesson 11 of Low-Level Design, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/lld/designing-a-file-system

Run it:  python lld/11-designing-a-file-system.py
"""


class File:
    def __init__(self, name, size): self.name, self._size = name, size
    def size(self): return self._size

class Folder:
    def __init__(self, name): self.name, self.items = name, []
    def add(self, entry): self.items.append(entry); return self
    def size(self): return sum(e.size() for e in self.items)   # ask, do not test


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import re


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
    root = Folder("/").add(File("a.txt", 12)).add(Folder("logs").add(File("x.log", 30)))
    check_printed(root.size(), len(root.items), expect="42 2")
