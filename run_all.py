"""
Run every lesson and problem file and report which ones fail.

    python run_all.py              # everything
    python run_all.py sorting      # only paths containing "sorting"

Each file runs in its own Python process. A file fails if it raises, including
a failed assertion against the output its lesson promises. No dependencies.
"""

import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TIMEOUT = 60

if os.name == "nt":
    os.system("")  # enable ANSI colours in the Windows console

COLOUR = sys.stdout.isatty() and not os.environ.get("NO_COLOR")
RED, GREEN, DIM, RESET = ("\033[31m", "\033[32m", "\033[2m", "\033[0m") if COLOUR else ("", "", "", "")


def files(filters):
    found = sorted(
        p for p in ROOT.rglob("*.py")
        if p.name != "run_all.py" and not any(part.startswith(".") for part in p.relative_to(ROOT).parts)
    )
    rel = [p.relative_to(ROOT).as_posix() for p in found]
    return [r for r in rel if not filters or any(f in r for f in filters)]


def run(rel):
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
    start = time.perf_counter()
    try:
        proc = subprocess.run(
            [sys.executable, rel], cwd=ROOT, env=env, capture_output=True,
            text=True, encoding="utf-8", errors="replace", timeout=TIMEOUT,
        )
        ok, err = proc.returncode == 0, proc.stderr.strip()
    except subprocess.TimeoutExpired:
        ok, err = False, f"timed out after {TIMEOUT}s"
    return rel, ok, err, time.perf_counter() - start


def main():
    targets = files(sys.argv[1:])
    if not targets:
        print("no files match", sys.argv[1:])
        return 1
    failed = []
    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as pool:
        for rel, ok, err, secs in pool.map(run, targets):
            if ok:
                print(f"{GREEN}ok  {RESET} {rel} {DIM}{secs:.2f}s{RESET}")
            else:
                failed.append(rel)
                last = err.splitlines()[-1] if err else "failed"
                print(f"{RED}FAIL{RESET} {rel}\n     {RED}{last}{RESET}")
    passed = len(targets) - len(failed)
    colour = RED if failed else GREEN
    print(f"\n{colour}{passed} passed, {len(failed)} failed{RESET} ({len(targets)} files)")
    for rel in failed:
        print(f"  {RED}{rel}{RESET}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
