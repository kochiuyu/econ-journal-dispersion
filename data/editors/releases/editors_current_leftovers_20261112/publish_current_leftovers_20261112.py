#!/usr/bin/env python3
"""Publish editors_current_leftovers_20261112 into /workspace/edj-web (cell-level apply from the changes CSV,
in place by editor_row_key; long table aligned on (editor_row_key, aff_rank))."""
from __future__ import annotations
import csv, gzip, json, shutil, subprocess, sys, re
from collections import Counter, defaultdict
from pathlib import Path

SRC = Path("/workspace/econ-journal-editors/releases/editors_current_leftovers_20261112")
WEB = Path("/workspace/edj-web")
FREEZE = "editors_current_leftovers_20261112"
DEST = WEB / "data/editors/releases" / FREEZE
PREV_GZ = WEB / "data/editors/releases/editors_leftover_fixes_20261112/editor_affiliations.csv.gz"
B13 = "editors_abdc_b_current#13"
DRY = "--dry" in sys.argv
C = WEB / "data/editors"
PANELS = {
    "editors_ft50_current.csv": C / "ft50/releases/current/editors_ft50_current.csv",
    "editors_ft50_current_with_ror.csv": C / "ft50/releases/current/editors_ft50_current_with_ror.csv",
    "editors_abdc_a_star_current.csv": C / "abdc/releases/current/editors_abdc_a_star_current.csv",
    "editors_abdc_a_current.csv": C / "abdc/releases/current/editors_abdc_a_current.csv",
    "editors_abdc_b_current.csv": C / "abdc/releases/current/editors_abdc_b_current.csv",
    "editors_abdc_c_current.csv": C / "abdc/releases/current/editors_abdc_c_current.csv",
    "editors_abs_ajg_gap_prio43_current.csv": C / "abs_ajg_gap/releases/current/editors_abs_ajg_gap_prio43_current.csv",
    "editors_abs_ajg_gap_ajg2_current.csv": C / "abs_ajg_gap/releases/current/editors_abs_ajg_gap_ajg2_current.csv",
    "editors_abs_ajg_gap_ajg1_current.csv": C / "abs_ajg_gap/releases/current/editors_abs_ajg_gap_ajg1_current.csv",
}
UNPUB_OK = {"editors_ft50_current#577", "editors_ft50_current#578",
            "editors_ft50_current_with_ror#577", "editors_ft50_current_with_ror#578"}
UNTOUCHED = ["editors_ft50_current#640", "editors_ft50_current#608", "editors_ft50_current#627",
             "editors_ft50_current_with_ror#640", "editors_ft50_current_with_ror#608", "editors_ft50_current_with_ror#627",
             "editors_abdc_b_current#18374", "editors_abs_ajg_gap_ajg2_current#5448", "editors_abs_ajg_gap_ajg2_current#5449",
             "editors_abs_ajg_gap_ajg2_current#5450", "editors_abs_ajg_gap_ajg2_current#5451",
             "editors_abdc_c_current#15763", "editors_abdc_c_current#15767"]
LONG_FIELDS_OK = {"ror_country", "ror_id", "ror_name", "is_panel_ror", "ror_match_note", "editor_name"}
PANEL_FIELDS_OK = {"ror_notes", "ror_country", "continent", "canonical_name", "ror_id", "ror_name", "lat", "lon",
                   "editor_name", "ror_id_aff_rank", "affiliation_count", "primary_aff_basis"}


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f); return list(r.fieldnames or []), list(r)


def write(path, fields, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
        w.writeheader(); w.writerows(rows)


def die(msg):
    print("FAIL:", msg); sys.exit(1)


def main():
    stats = {"freeze": FREEZE, "panels": {}}
    _, diffs = load(SRC / "CURRENT_LEFTOVERS_directory_diff_20261112.csv")
    _, changes = load(SRC / "CURRENT_LEFTOVERS_changes_20261112.csv")
    _, skipped = load(SRC / "CURRENT_LEFTOVERS_skipped_20261112.csv")
    stats["collector_skipped"] = skipped
    pub = {f: load(p) for f, p in PANELS.items()}
    # round-trip check: rewriting unchanged published panels must be byte-identical
    for f, p in PANELS.items():
        tmp = Path("/tmp/_rt.csv"); write(tmp, *pub[f])
        if tmp.read_bytes() != p.read_bytes(): die("round-trip not byte-identical " + f)
    pub_idx = {f: {r["editor_row_key"]: r for r in rows} for f, (_, rows) in pub.items()}
    snap_untouched = {k: dict(pub_idx[k.split("#")[0] + ".csv"][k]) for k in UNTOUCHED}

    # 1. directory_diff old values vs published
    missing = mism = 0; unpub_in_diff = 0
    for d in diffs:
        r = pub_idx[d["file"]].get(d["editor_row_key"])
        if r is None:
            if d["editor_row_key"] in UNPUB_OK: unpub_in_diff += 1; continue
            missing += 1; print("MISSING", d); continue
        if r.get(d["field"], "") != d["directory_value"]:
            mism += 1; print("OLD MISMATCH", d, repr(r.get(d["field"])))
    print(f"directory_diff {len(diffs)} cells missing={missing} old_mismatch={mism} unpublished_ok={unpub_in_diff}")
    stats["directory_diff"] = {"cells": len(diffs), "missing": missing, "old_mismatch": mism, "unpublished_ok": unpub_in_diff}
    if missing or mism: die("directory_diff vs published")

    # 2. panel changes
    applied = Counter(); skipped_unpub = Counter(); applied_keys = set(); pmism = 0
    item_keys = defaultdict(set); action_keys = defaultdict(set)
    for ch in changes:
        if ch["file"] == "editor_affiliations.csv": continue
        k = ch["editor_row_key"]; r = pub_idx[ch["file"]].get(k)
        if r is None:
            if k not in UNPUB_OK: die("unexpected unpublished change key " + k)
            skipped_unpub[ch["file"]] += 1; continue
        if ch["field"] not in PANEL_FIELDS_OK: die("unexpected panel field " + str(ch))
        if r[ch["field"]] != ch["old"]:
            pmism += 1; print("PANEL OLD MISMATCH", k, ch["field"], repr(r[ch["field"]]), repr(ch["old"])); continue
        r[ch["field"]] = ch["new"]; applied[ch["file"]] += 1; applied_keys.add(k)
        item_keys[ch["item"]].add(k); action_keys[(ch["item"], ch["action"])].add(k)
    if pmism: die("panel old mismatches")
    stats["panel_cells_applied"] = sum(applied.values())
    stats["panel_keys_applied"] = len(applied_keys)
    stats["panel_keys_by_item"] = {k: len(v) for k, v in item_keys.items()}
    stats["panel_keys_by_item_action"] = {f"{a}:{b}": len(v) for (a, b), v in action_keys.items()}
    for d in diffs:
        r = pub_idx[d["file"]].get(d["editor_row_key"])
        if r is not None and r.get(d["field"], "") != d["new_value"]: die("new value " + str(d))
    for fname, (fields, rows) in pub.items():
        cf, crows = load(SRC / fname)
        if cf != fields: die("HEADER DIFF " + fname)
        cidx = {r["editor_row_key"]: r for r in crows}
        pkeys = [r["editor_row_key"] for r in rows]
        pks = set(pkeys); extras = [k for k in cidx if k not in pks]
        if any(k not in cidx for k in pkeys): die("published key missing in collector " + fname)
        tdiv = []
        for r in rows:
            k = r["editor_row_key"]
            if k in applied_keys:
                tdiv += [(k, f) for f in fields if r[f] != cidx[k][f]]
        alldiv = Counter(f for r in rows for f in fields if r[f] != cidx[r["editor_row_key"]][f])
        stats["panels"][fname] = {"rows": len(rows), "collector_rows": len(crows), "extras_not_published": len(extras),
                                  "extras_keys": extras, "cells_applied": applied[fname],
                                  "cells_skipped_unpublished": skipped_unpub[fname],
                                  "touched_key_divergence_vs_collector": tdiv,
                                  "residual_field_divergence_vs_collector": dict(alldiv)}
        print(fname, {k: v for k, v in stats["panels"][fname].items() if k != "extras_keys"}, extras[:12])
        if tdiv: die("touched key diverges from collector " + str(tdiv))
        if applied[fname] and not DRY: write(PANELS[fname], fields, rows)
    if stats["panels"]["editors_ft50_current.csv"]["rows"] != 10047 or stats["panels"]["editors_ft50_current_with_ror.csv"]["rows"] != 10047:
        die("ft50 count")
    for k, snap in snap_untouched.items():
        if pub_idx[k.split("#")[0] + ".csv"][k] != snap: die("untouched changed " + k)
    stats["applied_panel_keys"] = sorted(applied_keys)

    # 3. long table
    with gzip.open(PREV_GZ, "rt", encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f); lf = list(rd.fieldnames or []); plong = list(rd)
    orig = [dict(r) for r in plong]
    col = {}; colrows_by_key = defaultdict(list); ncol = 0
    with open(SRC / "editor_affiliations.csv", newline="", encoding="utf-8") as f:
        rd = csv.DictReader(f)
        if list(rd.fieldnames or []) != lf: die("LONG HEADER DIFF")
        for r in rd:
            ncol += 1; col[(r["editor_row_key"], r["aff_rank"])] = r; colrows_by_key[r["editor_row_key"]].append(r)
    lch = defaultdict(list)
    for ch in changes:
        if ch["file"] == "editor_affiliations.csv": lch[ch["editor_row_key"]].append(ch)
    stats["long_change_rows_in_csv"] = sum(len(v) for v in lch.values())
    stats["long_change_keys_in_csv"] = len(lch)
    pub_keys = {r["editor_row_key"] for r in plong}
    stats["long_change_keys_not_published"] = sorted(k for k in lch if k not in pub_keys)
    lfc = Counter(); lmiss = 0; lmism = 0; lkeys = set()
    for r in plong:
        k = r["editor_row_key"]
        if k not in lch: continue
        c = col.get((k, r["aff_rank"]))
        if c is None: lmiss += 1; continue
        fields = {ch["field"] for ch in lch[k]}
        for fld in fields:
            if r[fld] != c[fld]:
                olds = {ch["old"] for ch in lch[k] if ch["field"] == fld}
                if r[fld] not in olds:
                    lmism += 1; print("LONG OLD MISMATCH", k, r["aff_rank"], fld, repr(r[fld]), olds); continue
                r[fld] = c[fld]; lfc[(lch[k][0]["item"], fld)] += 1; lkeys.add(k)
    if lmiss or lmism: die(f"long missing={lmiss} mism={lmism}")
    raw_changed = sum(1 for r, o in zip(plong, orig) if r["raw_aff_part"] != o["raw_aff_part"])
    other_changed = Counter(f for r, o in zip(plong, orig) for f in lf if r[f] != o[f])
    b13 = any(r["editor_row_key"] == B13 and "web_email_scrub_20261110" in (r.get("ror_match_note") or "") for r in plong)
    uniq = len({r["editor_row_key"] for r in plong})
    changed_parts = sum(1 for r, o in zip(plong, orig) if r != o)
    touched_resid = Counter(f for r in plong if r["editor_row_key"] in lch for f in lf
                            if (c := col.get((r["editor_row_key"], r["aff_rank"]))) is not None and r[f] != c[f])
    resid = Counter(f for r in plong for f in lf if (c := col.get((r["editor_row_key"], r["aff_rank"]))) is not None and r[f] != c[f])
    absent = sum(1 for r in plong if (r["editor_row_key"], r["aff_rank"]) not in col)
    print(f"long pub={len(plong)} uniq={uniq} collector={ncol} changed_parts={changed_parts} keys={len(lkeys)} "
          f"fields={dict(lfc)} raw_changed={raw_changed} other={dict(other_changed)} b13={b13} touched_resid={dict(touched_resid)} resid={dict(resid)} absent={absent}")
    if len(plong) != 181449 or uniq != 180025 or raw_changed or not b13: die("long guards")
    if set(other_changed) - LONG_FIELDS_OK: die("unexpected long field")
    if touched_resid: die("touched long diverges from collector")
    stats.update(long_n=len(plong), long_unique_keys=uniq, collector_long_n=ncol, long_changed_parts=changed_parts,
                 long_changed_keys=len(lkeys), long_field_changes={f"{a}:{b}": n for (a, b), n in lfc.items()},
                 long_other_changed=dict(other_changed),
                 long_raw_changed=raw_changed, long_raw_unchanged=len(plong) - raw_changed, b13_ok=b13,
                 long_residual_vs_collector=dict(resid), long_parts_absent_in_collector=absent)
    # panel keys changed without long rows
    stats["panel_keys_changed_without_long"] = sorted(k for k in applied_keys if k not in pub_keys)
    # panel-long sync on intended fields for changed keys (primary long row = ror_id_aff_rank or aff_rank 1)
    long_by_key = defaultdict(list)
    for r in plong: long_by_key[r["editor_row_key"]].append(r)
    desync = []
    for f, (_, rows) in pub.items():
        for r in rows:
            k = r["editor_row_key"]
            if k not in applied_keys or k not in long_by_key: continue
            rank = r.get("ror_id_aff_rank") or "1"
            lr = next((x for x in long_by_key[k] if x["aff_rank"] == rank), long_by_key[k][0])
            for pf, lfld in (("ror_id", "ror_id"), ("ror_country", "ror_country"), ("editor_name", "editor_name")):
                if lfld in lr and pf in r and r[pf] != lr[lfld]: desync.append((k, pf, r[pf], lr[lfld]))
    stats["panel_long_desync_changed_keys"] = desync
    print("panel-long desync on changed keys:", len(desync), desync[:10])
    email = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
    em = sum(1 for f, (_, rows) in pub.items() for r in rows if r["editor_row_key"] in applied_keys for v in r.values() if v and email.search(v))
    stats["emails_on_touched_rows"] = em
    if em: die("email")
    if DRY:
        print("DRY OK"); return
    DEST.mkdir(parents=True, exist_ok=True)
    tmp = Path("/tmp/editor_affiliations_current_leftovers.csv"); write(tmp, lf, plong)
    gz = DEST / "editor_affiliations.csv.gz"
    with open(gz, "wb") as out: subprocess.check_call(["gzip", "-9", "-n", "-c", str(tmp)], stdout=out)
    stats["gz_md5"] = subprocess.check_output(["md5sum", str(gz)], text=True).split()[0]
    stats["gz_size"] = gz.stat().st_size
    for n in ["CURRENT_LEFTOVERS_changes_20261112.csv", "CURRENT_LEFTOVERS_directory_diff_20261112.csv",
              "CURRENT_LEFTOVERS_skipped_20261112.csv", "HANDOFF.md", "README.md", "current_leftovers_20261112.py"]:
        shutil.copy2(SRC / n, DEST / n)
    shutil.copy2(SRC / "RELEASE_NOTES.md", DEST / "COLLECTOR_RELEASE_NOTES.md")
    shutil.copy2(__file__, DEST / "publish_current_leftovers_20261112.py")
    Path("/tmp/current_leftovers_publish_stats.json").write_text(json.dumps(stats, indent=2, ensure_ascii=False) + "\n")
    print("OK", stats["gz_size"], stats["gz_md5"])


if __name__ == "__main__":
    main()
