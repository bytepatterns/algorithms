"""
Reading a Query Plan: Stop guessing why it is slow — ask the engine what it did.

A query plan is the engine's own account of what it will do: which table it
reads first, whether it scans or searches, which index it uses, and whether
it has to sort afterwards. Two words carry most of the meaning — SCAN reads
everything, SEARCH jumps in.

Lesson 15 of SQL, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sql/reading-a-query-plan

Run it:  python sql/15-reading-a-query-plan.py
"""


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
    printed = printed.replace("SCAN TABLE ", "SCAN ").replace("SEARCH TABLE ", "SEARCH ")
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
    import sqlite3
    db = sqlite3.connect(":memory:")
    db.executescript("""
      CREATE TABLE kiln (id INT PRIMARY KEY, glaze TEXT);
      CREATE TABLE firing (kiln_id INT, cone INT);
      INSERT INTO kiln VALUES (1,'tenmoku'),(2,'celadon');
      INSERT INTO firing VALUES (1,10),(1,8),(2,6);""")
    q = """SELECT k.glaze, f.cone FROM firing f
           JOIN kiln k ON k.id = f.kiln_id WHERE f.cone > 7"""
    check([r[3] for r in db.execute("EXPLAIN QUERY PLAN " + q)], ['SCAN f', 'SEARCH k USING INDEX sqlite_autoindex_kiln_1 (id=?)'])
    db.execute("CREATE INDEX i_cone ON firing(cone)")
    check_printed([r[3] for r in db.execute("EXPLAIN QUERY PLAN " + q)][0], expect="SEARCH f USING INDEX i_cone (cone>?)")
