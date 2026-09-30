"""
In-Memory File System (hard) · patterns: class-design, path-walk, invariants

Design an in-memory file system with absolute, slash-separated paths.
mkdir(path) creates a directory and any missing parents. append(path, text)
creates a file if needed, including missing parent directories, and adds
text to its end. read(path) returns a file's whole content, ls(path) returns
the sorted names inside a directory, or a one-item list with the file's own
name for a file, and size(path) returns the total characters stored at or
below a path. The structure must stay a valid tree: nothing may be created
inside a file, and a directory may never be read or appended to, so those
calls raise NotADirectoryError or IsADirectoryError and change nothing.

Examples:

    Input:  mkdir("/logs/app"), append("/logs/app/today.txt", "boot ok\\n"),
            append("/logs/app/today.txt", "user in\\n"), append("/notes/todo.md", "ship it")
            ls("/"), ls("/logs/app"), ls("/notes/todo.md")
    Output: ['logs', 'notes'] ['today.txt'] ['todo.md']

    Input:  then read("/logs/app/today.txt"), size("/")
    Output: 'boot ok\\nuser in\\n' 23
    Why:    8 + 8 characters in today.txt and 7 in todo.md

    Input:  then mkdir("/notes/todo.md/drafts"), append("/logs", "x")
    Output: NotADirectoryError IsADirectoryError
    Why:    edge case, the tree refuses a folder inside a file and text written to a folder

Approach:
    A directory is a dict from name to child and a file is a list of text
    chunks, so every rule reduces to one isinstance check at the right
    moment. All five operations share one path walk, which either creates
    missing directories or raises when a name is missing, and which refuses
    to descend into a file; that single guard is what keeps the tree valid,
    because no call can ever place a child under a file. append checks the
    parent and the target before creating anything, so a refused call leaves
    no half-built directories behind, and it stores chunks rather than
    joining strings so appends stay cheap until a read joins them once. A
    walk costs O(d) for a path of depth d, and size is O(n) over the n nodes
    below the path.

The lesson behind it: Designing a File System
    https://bytepatterns.com/learn/lld/designing-a-file-system
    python lld/11-designing-a-file-system.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/lld/in-memory-file-system

Run it:  python problems/lld/05-in-memory-file-system.py
"""


class FileSystem:
    def __init__(self):
        self.root = {}                     # a directory is a dict, a file is a list of chunks

    def _walk(self, path, create=False):
        node = self.root
        for name in filter(None, path.split("/")):
            if isinstance(node, list):
                raise NotADirectoryError(path)         # never step inside a file
            if name not in node and not create:
                raise FileNotFoundError(path)
            node = node.setdefault(name, {})
        return node

    def mkdir(self, path):
        if isinstance(self._walk(path, create=True), list):
            raise NotADirectoryError(path)             # the path names a file

    def append(self, path, text):
        parent, name = path.rsplit("/", 1)
        folder = self._walk(parent, create=True)
        if isinstance(folder, list) or isinstance(folder.get(name), dict):
            raise IsADirectoryError(path)
        folder.setdefault(name, []).append(text)

    def read(self, path):
        node = self._walk(path)
        if isinstance(node, dict):
            raise IsADirectoryError(path)
        return "".join(node)

    def ls(self, path):
        node = self._walk(path)
        return [path.rsplit("/", 1)[1]] if isinstance(node, list) else sorted(node)

    def size(self, path):
        node = self._walk(path)
        if isinstance(node, list):
            return sum(len(chunk) for chunk in node)
        return sum(self.size(path.rstrip("/") + "/" + name) for name in node)

def attempt(action, *args):
    try:
        action(*args)
        return "ok"
    except OSError as error:
        return type(error).__name__


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
    fs = FileSystem()
    fs.mkdir("/logs/app")
    fs.append("/logs/app/today.txt", "boot ok\n")
    fs.append("/logs/app/today.txt", "user in\n")
    fs.append("/notes/todo.md", "ship it")
    check_printed(fs.ls("/"), fs.ls("/logs/app"), fs.ls("/notes/todo.md"), expect="['logs', 'notes'] ['today.txt'] ['todo.md']")
    check_printed(repr(fs.read("/logs/app/today.txt")), fs.size("/"), expect="'boot ok\\nuser in\\n' 23")
    check_printed(attempt(fs.mkdir, "/notes/todo.md/drafts"), attempt(fs.append, "/logs", "x"), expect="NotADirectoryError IsADirectoryError")
