"""
Simplify a Unix Path (medium) · patterns: stack, string-parsing

Given an absolute Unix-style path, return its simplest equivalent form. In
the input, . means the current directory, .. means the parent directory (the
parent of the root is the root), and several slashes in a row count as one.
Any other name, including ..., is an ordinary directory. The result must
start with a single slash, separate names with single slashes and not end
with a slash unless it is the root itself.

Examples:

    Input:  path = "/a/./b/../../c/"
    Output: "/c"
    Why:    enter a, stay, enter b, leave b, leave a, enter c

    Input:  path = "/home//user/.../docs/"
    Output: "/home/user/.../docs"
    Why:    the double slash collapses, and three dots is just a directory name

    Input:  path = "/../"
    Output: "/"
    Why:    edge case, going up from the root stays at the root

Approach:
    The directories you are inside form a stack: entering a directory pushes
    its name and .. pops the last one entered. Splitting on / turns runs of
    slashes and a trailing slash into empty pieces, which are skipped along
    with ., so the only real cases left are a name and ... Popping only when
    the stack is not empty is the rule that the root's parent is the root.
    Whatever remains on the stack, bottom to top, is the path from the root,
    and joining it with a leading slash gives the canonical form, including
    / for an empty stack. Time and space are O(n) in the length of the path.

The lesson behind it: Stack Basics
    https://bytepatterns.com/learn/stacks-queues/stack-basics
    python stacks-queues/01-stack-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/simplify-a-unix-path

Run it:  python problems/stacks-queues/14-simplify-a-unix-path.py
"""


def simplify_path(path):
    stack = []                                 # directories entered, deepest on top
    for part in path.split("/"):
        if part == "..":
            if stack:                          # the parent of the root is the root
                stack.pop()
        elif part and part != ".":             # skip empty pieces and "."
            stack.append(part)
    return "/" + "/".join(stack)


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
    check_printed(simplify_path("/a/./b/../../c/"), expect="/c")
    check_printed(simplify_path("/home//user/.../docs/"), expect="/home/user/.../docs")
    check_printed(simplify_path("/../"), expect="/")
