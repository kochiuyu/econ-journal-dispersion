#!/usr/bin/env python3
"""Rebuild held backfill freeze editors_ra_ta_merge_20261106 as editors_ra_ta_merge_rebuild_20261112
on the published backfill editors_backfill_scale_ror_20261031 (web PR #41).
Content = held pack (20 RA/FIX row updates + RED 2021 45 rows + JBES 2018 87 rows), with only mechanical fixes:
  1. line endings restored to the base's CRLF on every file the held pack rewrote as LF;
  2. inventory AER: Insights 2018 cell 'n/a' restored (held pack blanked it by NA-coercion; not part of the merge).
No value changes otherwise. Held folder and base are not modified. Not published."""
import csv, hashlib, json, shutil, sys
from pathlib import Path
from datetime import datetime
REL = Path("/workspace/econ-journal-editors/releases")
BASE = REL / "editors_backfill_scale_ror_20261031"; HELD = REL / "editors_ra_ta_merge_20261106"
OUT = REL / "editors_ra_ta_merge_rebuild_20261112"
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
md5 = lambda p: hashlib.md5(p.read_bytes()).hexdigest()
def eol(p):
    b = p.read_bytes(); return "\r\n" if b"\r\n" in b else "\n"
log = {"files": {}}
for p in sorted(HELD.iterdir()):
    if p.name in ("README.md", "_build.json"): continue
    bp = BASE / p.name
    if p.suffix != ".csv" or not bp.exists():
        shutil.copy2(p, OUT / p.name); log["files"][p.name] = "copied"; continue
    rows = list(csv.reader(open(p, encoding="utf-8", newline="")))
    fixes = 0
    if p.name == "editors_backfill_scale_inventory.csv":
        brows = list(csv.reader(open(bp, encoding="utf-8", newline="")))
        bi = {(r[0], r[2]): r for r in brows[1:]}
        for r in rows[1:]:
            if r[1] == "AER: Insights" and r[2] == "2018":
                b = bi[(r[0], r[2])]
                for j, (x, y) in enumerate(zip(b, r)):
                    if x == "n/a" and y == "": r[j] = "n/a"; fixes += 1
    want = eol(bp)
    with open(OUT / p.name, "w", encoding="utf-8", newline="") as fh:
        csv.writer(fh, lineterminator=want).writerows(rows)
    # value check vs held
    a = list(csv.reader(open(OUT / p.name, encoding="utf-8", newline="")))
    held = list(csv.reader(open(p, encoding="utf-8", newline="")))
    diff = sum(1 for x, y in zip(a, held) if x != y) + abs(len(a) - len(held))
    log["files"][p.name] = dict(eol_base=repr(want), eol_held=repr(eol(p)), rows=len(a) - 1, value_rows_differing_from_held=diff,
                                na_restored=fixes, identical_bytes_to_base=md5(OUT / p.name) == md5(bp),
                                identical_bytes_to_held=md5(OUT / p.name) == md5(p))
json.dump(log, open("/tmp/ra_ta_rebuild_log.json", "w"), indent=1)
print(json.dumps(log, indent=1))
