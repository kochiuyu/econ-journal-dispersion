#!/usr/bin/env python3
"""Freeze editors_theory_decision_title_20261112 on editors_campus_conflict_fix_20261111
(live via Directory PR #64, 004c6cfe). User-approved display-title rename, relayed by
Journal-Editor-Web (formerly Econ-Journal-Web), from
/workspace/collector_journal_title_20261112/theory_decision_rename_20261112.csv
(72 editors_abdc_a_current rows, abdc_journal_id theory_decision_international_journal).

Change only the display field `journal` from the long ABDC form to "Theory and Decision".
Leave journal_name_abdc and every other field unchanged. Sync the long-table `journal`
column for these keys only. Pilots stay byte-identical. No publish. Do not edit
journals/catalog_abdc_a.csv.
"""
from __future__ import annotations
import csv, json, re, sys, glob, shutil, importlib.util
from collections import Counter, defaultdict
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("fr1", HERE / "full_review_fix_20261111.py")
FR = importlib.util.module_from_spec(spec); spec.loader.exec_module(FR)
PR, WI, T, M = FR.PR, FR.WI, FR.T, FR.M
ROOT = M.ROOT; STAMP = "20261112"; METHOD = "theory_decision_title_20261112"
FREEZE_ID = "editors_theory_decision_title_20261112"
BASE_ID = "editors_campus_conflict_fix_20261111"
SRC = ROOT / f"releases/{BASE_ID}"; FREEZE = ROOT / f"releases/{FREEZE_ID}"
for mod in (M, T, WI, PR, FR):
    for a, v in (("SRC_FREEZE", SRC), ("SRC", SRC), ("FREEZE", FREEZE)):
        setattr(mod, a, v)
M.LOGF = ROOT / f"abs_ajg/logs/theory_decision_title_{STAMP}.log"
FR.DIRDIFF_NAME = f"THEORY_DECISION_TITLE_directory_diff_{STAMP}.csv"
log = M.log
LONG, FT, FTR = WI.LONG, WI.FT, WI.FTR
CHANGELOG_NAME = f"THEORY_DECISION_TITLE_changes_{STAMP}.csv"
SKIPS_NAME = f"THEORY_DECISION_TITLE_skipped_{STAMP}.csv"
SRC_CSV = Path("/workspace/collector_journal_title_20261112/theory_decision_rename_20261112.csv")
LONG_TITLE = "Theory and Decision: an international journal for multidisciplinary advances in decision sciences"
SHORT_TITLE = "Theory and Decision"
JID = "theory_decision_international_journal"
UNTOUCHED = (
    "editors_abdc_c_current#15558",
    "editors_abdc_c_current#15559",
    "editors_abdc_a_current#42676",
    "editors_abdc_b_current#16107",
)
HOLD_RX = re.compile(
    r"Henley Business School Africa"
    r"|IMD,?\s*Singapore"
    r"|Middlesex University Dubai"
    r"|Middlesex University Mauritius"
    r"|Nova Business School Africa"
    r"|Peking University HSBC Business School.{0,80}\b(?:UK|United Kingdom|PHBS-UK)"
    r"|Rutgers School of Business.?Camden"
    r"|Rutgers University.?Camden"
    r"|Rutgers-Camden"
    r"|Goldman Sachs\s*&\s*Imperial"
    r"|Consip Spa and University LUISS"
    r"|VIVA Idea"
    r"|Yale School of Management\s*/\s*AQR"
    r"|Public Sector Scorecard Research Centre and Sheffield"
    r"|Leeds University Business School,\s*UK and Carnegie Mellon"
    r"|Nanyang Business School\s*&\s*Renmin"
    r"|Macquarie Business School.{0,80}MIT CISR",
    re.I,
)
PANEL_ALLOWED = {"raw_affiliation", "canonical_name", "ror_id", "ror_name", "ror_country", "continent",
                 "lat", "lon", "ror_notes", "editor_name", "editor_name_raw"}
LONG_ALLOWED = {"raw_aff_part", "ror_id", "ror_name", "ror_country", "is_panel_ror", "ror_match_note", "editor_name"}


def hold_hit(blob):
    m = HOLD_RX.search(blob or "")
    return m.group(0) if m else ""


def main():
    if M.LOGF.exists(): M.LOGF.unlink()
    log(f"start {FREEZE_ID}")
    rows = list(csv.DictReader(open(SRC_CSV, encoding="utf-8")))
    log(f"file rows={len(rows)} keys={len({r['editor_row_key'] for r in rows})} panels={sorted({r['panel'] for r in rows})}")
    catalog, all_rors, name_to_ids = M.build_twin_catalog(SRC)
    dir_ajg1 = glob.glob("/workspace/edj-web/data/editors/*/releases/current/editors_abs_ajg_gap_ajg1_current.csv")[0]
    dir_keys = {r["editor_row_key"] for r in csv.DictReader(open(dir_ajg1, encoding="utf-8-sig"))}
    M.copy_freeze_base()
    data = {f: FR.load(f, FREEZE) for f in M.PANEL_FILES}
    idx = {f: {r["editor_row_key"]: r for r in rows_} for f, (_h, rows_) in data.items()}
    orig = {f: {k: dict(r) for k, r in d.items()} for f, d in idx.items()}
    nav = {r["editor_row_key"] for r in data["editors_abs_ajg_gap_ajg1_current.csv"][1] if r["editor_row_key"] not in dir_keys}
    skips, changed, stats = [], {}, defaultdict(Counter)

    held_keys = []
    for f, d in orig.items():
        if f in M.PILOT_FILES: continue
        for k, r in d.items():
            blob = " ".join((r.get("canonical_name") or "", r.get("raw_affiliation") or ""))
            if hold_hit(blob):
                held_keys.append((f, k, hold_hit(blob)))
    log(f"held rows on base panels: {len(held_keys)}")

    def skip(item, action, name, reason, f="", k=""):
        skips.append(dict(item=item, action=action, institution=PR.red(name), file=f, editor_row_key=k, reason=PR.red(reason)))

    def apply(item, action, name, k, fields, note):
        f = FR.file_of(k)
        if f in M.PILOT_FILES:
            skip(item, action, name, "pilot file stays untouched", f, k); return False
        row = idx.get(f, {}).get(k)
        if row is None:
            skip(item, action, name, "row key not in panel", f, k); return False
        if k in nav:
            skip(item, action, name, "AJG1 nav row untouched", f, k); return False
        fl = dict(fields)
        ch = []
        for fld, val in fl.items():
            if fld not in row:
                skip(item, action, name, f"panel has no {fld} column", f, k); return False
            if row[fld] != val:
                ch.append((fld, row[fld], val)); row[fld] = val
        if not ch: return False
        changed[(f, k)] = dict(item=item, action=action, name=name, ch=ch, note=note, editor_name=row.get("editor_name", ""))
        return True

    for rec in rows:
        k = rec["editor_row_key"]
        f = FR.file_of(k)
        item = rec.get("editor_name") or k
        stats["rows"]["file"] += 1
        if rec.get("field") != "journal" or rec.get("new_value") != SHORT_TITLE or rec.get("old_value") != LONG_TITLE:
            skip(item, "SET_TITLE", SHORT_TITLE, "file row is not the approved journal-display rename", f, k)
            stats["skipped"]["file_mismatch"] += 1; continue
        if rec.get("abdc_journal_id") != JID:
            skip(item, "SET_TITLE", SHORT_TITLE, f"file abdc_journal_id is {rec.get('abdc_journal_id')!r}, not {JID}", f, k)
            stats["skipped"]["file_jid"] += 1; continue
        if f in M.PILOT_FILES or "pilot" in (rec.get("panel") or "") or "pilot" in k:
            skip(item, "SET_TITLE", SHORT_TITLE, "pilot file stays untouched", f, k)
            stats["skipped"]["pilot"] += 1; continue
        row = idx.get(f, {}).get(k)
        if row is None:
            skip(item, "SET_TITLE", SHORT_TITLE, "row key not in panel", f, k); stats["skipped"]["missing"] += 1; continue
        if row.get("abdc_journal_id") != JID:
            skip(item, "SET_TITLE", SHORT_TITLE,
                 f"panel abdc_journal_id is {row.get('abdc_journal_id')!r}, not {JID}; left unchanged", f, k)
            stats["skipped"]["panel_jid"] += 1; continue
        if row.get("journal") != LONG_TITLE:
            if row.get("journal") == SHORT_TITLE:
                stats["already_at_target"]["file"] += 1
                skip(item, "SET_TITLE", SHORT_TITLE, "journal already short title; left unchanged", f, k)
            else:
                skip(item, "SET_TITLE", SHORT_TITLE,
                     f"current journal is {row.get('journal')!r}, not the long title; left unchanged", f, k)
                stats["skipped"]["journal_mismatch"] += 1
            continue
        note = "display journal shortened to 'Theory and Decision'; journal_name_abdc left as the long ABDC listed string"
        if apply(item, "SET_TITLE", SHORT_TITLE, k, {"journal": SHORT_TITLE}, note):
            stats["applied"]["file"] += 1
        else:
            if not any(s["editor_row_key"] == k for s in skips):
                stats["already_at_target"]["file"] += 1

    log(f"stats {json.dumps({k: dict(v) for k, v in stats.items()})} changed={len(changed)} skips={len(skips)}")

    for f, (hdr, rows_) in data.items():
        if f in M.PILOT_FILES: continue
        M.write_csv(FREEZE / f, hdr, rows_, M.detect_lineterminator(SRC / f))

    lh, lrows = FR.load(LONG, FREEZE)
    changelog, long_skip, long_journal_n = [], [], 0
    has_journal = "journal" in (lh or [])
    log(f"long table has journal column={has_journal}")
    ck = {k for (_f, k) in changed}

    def lset(p, fld, val, k, op):
        if fld in p and p[fld] != val:
            changelog.append(dict(file=LONG, editor_row_key=k, editor_name=PR.red(p.get("editor_name", "")),
                                  item=op["item"], action=op["action"], field=fld,
                                  old=PR.red(p[fld]), new=PR.red(val), note="long sync"))
            p[fld] = val
            return True
        return False

    if has_journal:
        for p in lrows:
            k = p["editor_row_key"]
            if k not in ck: continue
            if "pilot" in (p.get("panel_file") or ""):
                long_skip.append((k, "long row is a pilot panel; left untouched")); continue
            op = next(op for (f, kk), op in changed.items() if kk == k)
            if lset(p, "journal", SHORT_TITLE, k, op):
                long_journal_n += 1
    else:
        log("long table has no journal display field; left untouched")

    M.write_csv(FREEZE / LONG, lh, lrows, M.detect_lineterminator(SRC / LONG))
    M.update_working_panels()

    for (f, k), op in sorted(changed.items()):
        for fld, ov, nv in op["ch"]:
            changelog.append(dict(file=f, editor_row_key=k, editor_name=PR.red(op["editor_name"]),
                                  item=op["item"], action=op["action"], field=fld,
                                  old=PR.red(ov), new=PR.red(nv), note=PR.red(op["note"])))
    for c in changelog:
        for kk in ("old", "new", "note", "editor_name", "item"):
            assert not PR.has_contact(c[kk] or ""), "contact in changelog"
        assert c["field"] in {"journal"}, f"unexpected changelog field {c['field']}"
    with open(FREEZE / CHANGELOG_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "editor_row_key", "editor_name", "item", "action", "field", "old", "new", "note"])
        w.writeheader(); w.writerows(changelog)
    with open(FREEZE / SKIPS_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["item", "action", "institution", "file", "editor_row_key", "reason"])
        w.writeheader(); w.writerows(skips)

    v = FR.verify(changed, orig, set(all_rors), nav)
    # This freeze's only intended field is journal, which verify treats as unexpected.
    # Re-scan and allow journal-only diffs on changed keys; any other field remains unexpected.
    v = allow_journal_only(v, changed, orig, nav)
    v["long_skipped"] = long_skip
    v["long_journal_rows_updated"] = long_journal_n
    v["long_has_journal_column"] = has_journal
    file_keys = {r["editor_row_key"] for r in rows}
    broke = []
    for k in UNTOUCHED:
        if k in file_keys: continue
        f = FR.file_of(k)
        b = {r["editor_row_key"]: r for r in FR.load(f, SRC)[1]}
        n = {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]}
        if b.get(k) != n.get(k): broke.append(k)
    held_broke = []
    for f, k, label in held_keys:
        b = orig[f][k]
        n = {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]}.get(k)
        if b != n:
            held_broke.append((k, label))
    v["followup_rows_changed"] = broke
    v["held_rows_changed"] = held_broke
    raw_changed = [k for (f, k), op in changed.items() if any(fld == "raw_affiliation" for fld, _, _ in op["ch"])]
    other_fields = [k for (f, k), op in changed.items() if any(fld != "journal" for fld, _, _ in op["ch"])]
    abdc_changed = []
    for f in M.PANEL_FILES:
        b = {r["editor_row_key"]: r for r in FR.load(f, SRC)[1]}
        n = {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]}
        for k, r in n.items():
            if (r.get("journal_name_abdc", "") or "") != (b[k].get("journal_name_abdc", "") or ""):
                abdc_changed.append(k)
            diffs = [c for c in r if r[c] != b[k][c]]
            if diffs and set(diffs) != {"journal"}:
                other_fields.append(k)
    v["raw_changed_this_freeze"] = raw_changed
    v["journal_name_abdc_changed"] = abdc_changed
    v["non_journal_fields_changed"] = sorted(set(other_fields))
    v["ok"] = (v["row_counts_unchanged"] and v["long_rows"] == 269545 and v["ajg1_file_rows"] == 12326 and v["ajg1_nav"] == 10 and not v["ajg1_nav_touched"]
               and v["ajg2_rows"] == 5462 and v["ft50_rows"] == 10049 and v["ft50_ror_rows"] == 10049 and not v["header_or_eol_changes"]
               and not v["panel_unexpected"] and not v["raw_changed_outside_drop_or_paauwe"] and not raw_changed and not v["long_unexpected"]
               and all(v["pilot_files_byte_identical"].values()) and not v["invented_ror"] and not v["protected_rows_institution_changed"] and not v["contact_n"]
               and v["long_contact_rows"][1] <= v["long_contact_rows"][0] and not v["panel_long_desync_changed_n"] and v["panel_long_desync_full_table"] <= v["base_desync_full_table"]
               and not v["nonlatin_lost"] and not v["near_miss"] and v["keep_11kbw"] and v["unsw"] and v["insead_fr_sg"] and v["working_panels_identical"]
               and not broke and not held_broke and not abdc_changed and not other_fields)
    log(f"verify ok={v['ok']} held_broke={held_broke} followup={broke} long_journal={long_journal_n} abdc_changed={abdc_changed}")
    dirdiff, eb, ea = directory_diff(changed)
    counts = {"before": PR.build("tdt_before", eb), "after": PR.build("tdt_after", ea)}
    pub, ftm = Counter(), Counter()
    for (f, k), op in changed.items():
        (ftm if f == FT else pub)[f"{op['action']}"] += 1
    summ = dict(stats={k: dict(x) for k, x in stats.items()}, rows_publish=dict(pub), rows_ft50_current_mirror=dict(ftm),
                skips=len(skips), changelog_lines=len(changelog), directory_diff_lines=len(dirdiff),
                long_has_journal_column=has_journal, long_journal_rows_updated=long_journal_n,
                journal_name_abdc_changed=abdc_changed, held_rows_on_base=len(held_keys), held_rows_changed=held_broke)
    json.dump(dict(summary=summ, verify=v, counts=counts), open(FREEZE / f"_summary_{STAMP}.json", "w"), indent=1, ensure_ascii=False, default=str)
    shutil.copy2(Path(__file__), FREEZE / Path(__file__).name)
    print(json.dumps(dict(summary=summ, counts=counts, verify_ok=v["ok"],
                          desync=(v["panel_long_desync_full_table"], v["base_desync_full_table"]),
                          unexpected=v["panel_unexpected"][:8], long_unexpected=v["long_unexpected"][:8],
                          invented=v["invented_ror"], followup=broke, held_broke=held_broke,
                          long_skip=long_skip[:8], long_journal=long_journal_n,
                          abdc_changed=abdc_changed),
                     indent=1, ensure_ascii=False, default=str)[:12000])
    log(f"done ok={v['ok']}")


def allow_journal_only(v, changed, orig, nav):
    """Drop journal-only diffs on changed keys from verify unexpected lists; keep any other field."""
    ck = {k for (_f, k) in changed}
    unexpected = []
    for f in M.PANEL_FILES:
        b = list(csv.DictReader(open(SRC / f, encoding="utf-8", newline="")))
        n = list(csv.DictReader(open(FREEZE / f, encoding="utf-8", newline="")))
        for x, y in zip(b, n):
            if x == y: continue
            k = y["editor_row_key"]
            diff = [c for c in x if x[c] != y[c]]
            extra = [c for c in diff if c not in PANEL_ALLOWED]
            if (f, k) not in changed or set(extra) - {"journal"}:
                unexpected.append((f, k, diff))
    lunexp = []
    lb = list(csv.DictReader(open(SRC / LONG, encoding="utf-8", newline="")))
    ln = list(csv.DictReader(open(FREEZE / LONG, encoding="utf-8", newline="")))
    for x, y in zip(lb, ln):
        if x == y: continue
        diffs = [c for c in x if x[c] != y[c]]
        extra = [c for c in diffs if c not in LONG_ALLOWED]
        if (y["editor_row_key"] not in ck or "pilot" in (y.get("panel_file") or "")
                or set(extra) - {"journal"}):
            lunexp.append(y["editor_row_key"])
    v["panel_unexpected"] = unexpected[:15]
    v["panel_unexpected_n"] = len(unexpected)
    v["long_unexpected"] = lunexp[:15]
    v["long_unexpected_n"] = len(lunexp)
    return v


def directory_diff(changed):
    dk = {}
    for f in glob.glob(WI.DIR_GLOB):
        for r in csv.DictReader(open(f, encoding="utf-8-sig", newline="")): dk[(Path(f).name, r["editor_row_key"])] = r
    out, eb, ea = [], defaultdict(lambda: defaultdict(dict)), defaultdict(lambda: defaultdict(dict))
    title_fields = list(FR.FIELDS) + ["journal"]
    for f in M.PUBLISH_FILES:
        b = {r["editor_row_key"]: r for r in FR.load(f, SRC)[1]}
        n = {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]}
        for k, r in n.items():
            d = dk.get((f, k))
            if d is None: continue
            fields = title_fields + (FR.NAME_FIELDS if k in FR.PAAUWE else [])
            for fld in fields:
                if fld not in r: continue
                if d is not None and fld in d:
                    if b[k].get(fld) != d[fld]: eb[f][k][fld] = b[k][fld]
                    if r[fld] != d[fld]:
                        ea[f][k][fld] = r[fld]
                        if (f, k) in changed:
                            out.append(dict(file=f, editor_row_key=k, field=fld, directory_value=PR.red(d[fld]), new_value=PR.red(r[fld])))
                elif (f, k) in changed and b[k].get(fld) != r.get(fld):
                    out.append(dict(file=f, editor_row_key=k, field=fld, directory_value=PR.red(b[k].get(fld, "")), new_value=PR.red(r.get(fld, ""))))
    with open(FREEZE / FR.DIRDIFF_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "editor_row_key", "field", "directory_value", "new_value"])
        w.writeheader(); w.writerows(out)
    return out, eb, ea


if __name__ == "__main__":
    main()
