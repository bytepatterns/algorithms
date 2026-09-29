"""
Indexes: A second, sorted copy of one column that ends the full scan.

An index is a separate structure that keeps one or more columns in sorted
order, each entry pointing back at its row. It turns "read everything and
check" into "jump straight there". The price is paid on writes: every insert
and update must maintain the index too.

Lesson 7 of SQL, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sql/indexes

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python sql/07-indexes.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import re


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
      CREATE TABLE photo (id INTEGER, shot_by TEXT, box INTEGER);
      INSERT INTO photo VALUES (1, 'Okonjo', 4), (2, 'Weiss', 9), (3, 'Okonjo', 2);
    """)
    q = "SELECT box FROM photo WHERE shot_by = 'Okonjo'"
    check_printed(db.execute("EXPLAIN QUERY PLAN " + q).fetchone()[3], expect="SCAN photo")
    db.execute("CREATE INDEX photo_by ON photo(shot_by)")
    check_printed(db.execute("EXPLAIN QUERY PLAN " + q).fetchone()[3], expect="SEARCH photo USING INDEX photo_by (shot_by=?)")
