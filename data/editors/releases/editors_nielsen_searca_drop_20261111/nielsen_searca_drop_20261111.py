#!/usr/bin/env python3
"""Freeze editors_nielsen_searca_drop_20261111 on editors_open_items_followup_20261111
(live via PR #57, af8f5451). User-approved Marks-style DROP of exactly two rows, relayed by Econ-Journal-Web:
  editors_abdc_a_current#42676  Consultant (former Chief Research Officer, Nielsen), USA
  editors_abdc_c_current#15559  Independent consultant (formerly SEARCA Knowledge Management Department Head)
Keep country/continent where they exist (United States / North America on Nielsen; SEARCA already blank).
Do not touch abdc_c#15558 or Diamond Leadership Institute (abdc_b#16107). Pilots stay byte-identical.
No publish."""
from __future__ import annotations
import csv, json, re, sys, glob, importlib.util
from collections import Counter, defaultdict
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("fr1", HERE / "full_review_fix_20261111.py")
FR = importlib.util.module_from_spec(spec); spec.loader.exec_module(FR)
PR, WI, T, M = FR.PR, FR.WI, FR.T, FR.M
ROOT = M.ROOT; STAMP = "20261111"; METHOD = "nielsen_searca_drop_20261111"
FREEZE_ID = "editors_nielsen_searca_drop_20261111"; BASE_ID = "editors_open_items_followup_20261111"
SRC = ROOT / f"releases/{BASE_ID}"; FREEZE = ROOT / f"releases/{FREEZE_ID}"
for mod in (M, T, WI, PR, FR):
    for a, v in (("SRC_FREEZE", SRC), ("SRC", SRC), ("FREEZE", FREEZE)):
        setattr(mod, a, v)
M.LOGF = ROOT / f"abs_ajg/logs/nielsen_searca_drop_{STAMP}.log"
FR.DIRDIFF_NAME = f"NIELSEN_SEARCA_DROP_directory_diff_{STAMP}.csv"
log = M.log
LONG = WI.LONG
CHANGELOG_NAME = f"NIELSEN_SEARCA_DROP_changes_{STAMP}.csv"
SKIPS_NAME = f"NIELSEN_SEARCA_DROP_skipped_{STAMP}.csv"
TARGETS = [
    dict(item="Nielsen", key="editors_abdc_a_current#42676",
         expected_raw="Consultant (former Chief Research Officer, Nielsen), USA",
         keep_country="United States"),
    dict(item="SEARCA", key="editors_abdc_c_current#15559",
         expected_raw="Independent consultant (formerly SEARCA Knowledge Management Department Head)",
         keep_country=""),
]
UNTOUCHED = ("editors_abdc_c_current#15558", "editors_abdc_b_current#16107")


def main():
    if M.LOGF.exists(): M.LOGF.unlink()
    log(f"start {FREEZE_ID}")
    catalog, all_rors, name_to_ids = M.build_twin_catalog(SRC)
    dir_ajg1 = glob.glob("/workspace/edj-web/data/editors/*/releases/current/editors_abs_ajg_gap_ajg1_current.csv")[0]
    dir_keys = {r["editor_row_key"] for r in csv.DictReader(open(dir_ajg1, encoding="utf-8-sig"))}
    M.copy_freeze_base()
    data = {f: FR.load(f, FREEZE) for f in M.PANEL_FILES}
    idx = {f: {r["editor_row_key"]: r for r in rows} for f, (_h, rows) in data.items()}
    orig = {f: {k: dict(r) for k, r in d.items()} for f, d in idx.items()}
    nav = {r["editor_row_key"] for r in data["editors_abs_ajg_gap_ajg1_current.csv"][1] if r["editor_row_key"] not in dir_keys}
    skips, changed, stats = [], {}, defaultdict(Counter)

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
        blob = " ".join((row.get(c) or "") for c in ("canonical_name", "raw_affiliation", "ror_name"))
        if M.PROTECT_RX.search(blob) or re.search(r"1\s*decembrie\s*1918", blob, re.I):
            skip(item, action, name, "protected organisation on row (11KBW/UNSW/INSEAD/1 Decembrie 1918)", f, k); return False
        ch = []
        for fld, val in fields.items():
            if fld in row and row[fld] != val:
                ch.append((fld, row[fld], val)); row[fld] = val
        if not ch: return False
        changed[(f, k)] = dict(item=item, action=action, name=name, ch=ch, note=note, editor_name=row.get("editor_name", ""))
        return True

    # log the Nielsen pilot twin so it is clearly skipped, not silently left
    for f in M.PILOT_FILES:
        for r in data[f][1]:
            if (r.get("raw_affiliation") or "") == TARGETS[0]["expected_raw"] or r["editor_row_key"].endswith("#42152"):
                if "Nielsen" in (r.get("raw_affiliation") or "") or (r.get("editor_name") or "") == "Pete Doe":
                    skip("Nielsen", "DROP", r.get("raw_affiliation") or "",
                         "pilot row left byte-identical (approved drop applies only to editors_abdc_a_current#42676)",
                         f, r["editor_row_key"])
                    stats["Nielsen"]["pilot_skipped"] += 1

    for t in TARGETS:
        k, item = t["key"], t["item"]
        f = FR.file_of(k)
        row = idx.get(f, {}).get(k)
        if row is None:
            skip(item, "DROP", t["expected_raw"], "row key not in panel", f, k); stats[item]["skipped"] += 1; continue
        raw = row.get("raw_affiliation") or ""
        stats[item]["before"] = {
            "canonical_name": row.get("canonical_name", ""), "raw_affiliation": raw,
            "ror_id": row.get("ror_id", ""), "ror_country": row.get("ror_country", ""),
            "continent": row.get("continent", ""), "ror_notes": (row.get("ror_notes") or "")[:180],
        }
        if raw != t["expected_raw"]:
            skip(item, "DROP", raw, f"printed raw does not match the approved text; not dropped", f, k)
            stats[item]["skipped"] += 1; continue
        if row.get("ror_id"):
            skip(item, "DROP", raw, f"row still carries ROR {row['ror_id']}; not dropped (ROR should already have been blanked)", f, k)
            stats[item]["skipped"] += 1; continue
        extra_w = set(w.casefold() for w in PR.ORGWORD.findall(raw)) - set(w.casefold() for w in PR.ORGWORD.findall(t["expected_raw"]))
        if extra_w:
            skip(item, "DROP", raw, f"printed raw names an organisation ({', '.join(sorted(extra_w))}); not dropped", f, k)
            stats[item]["skipped"] += 1; continue
        # keep existing country/continent (Nielsen: United States / North America; SEARCA: already blank)
        if t["keep_country"] and not FR.same_country(row.get("ror_country", ""), t["keep_country"]):
            skip(item, "DROP", raw, f"expected to keep country {t['keep_country']}, found {row.get('ror_country')}", f, k)
            stats[item]["skipped"] += 1; continue
        fl = dict(canonical_name="", raw_affiliation="", ror_id="", ror_name="", lat="", lon="")
        if "ror_notes" in row:
            tr = f"{METHOD}: user-approved DROP (Marks); printed text: {PR.red(raw)}"
            fl["ror_notes"] = f"{row['ror_notes']}; {tr}" if row.get("ror_notes") else tr
        ok = apply(item, "DROP", raw, k, fl, "Marks-style DROP; country and continent left as they were")
        stats[item]["applied"] = int(ok)

    log(f"stats {json.dumps({k: dict(v) for k, v in stats.items()}, default=str)} changed={len(changed)}")
    for f, (hdr, rows) in data.items():
        if f in M.PILOT_FILES: continue
        M.write_csv(FREEZE / f, hdr, rows, M.detect_lineterminator(SRC / f))

    lh, lrows = FR.load(LONG, FREEZE)
    by = defaultdict(list)
    for p in lrows: by[p["editor_row_key"]].append(p)
    changelog, long_skip = [], []

    def lset(p, fld, val, k, op):
        if fld in p and p[fld] != val:
            changelog.append(dict(file=LONG, editor_row_key=k, editor_name=PR.red(p.get("editor_name", "")),
                                  item=op["item"], action=op["action"], field=fld,
                                  old=PR.red(p[fld]), new=PR.red(val), note="long sync"))
            p[fld] = val

    for (f, k), op in changed.items():
        r, o = idx[f][k], orig[f][k]; ps = by.get(k)
        if not ps: long_skip.append((k, "no long rows")); continue
        # Marks DROP: blank raw_aff_part that matched the old printed text; trace in ror_match_note;
        # blank institution/ROR fields so the long table stays in sync. Keep ror_country.
        old_raw = o.get("raw_affiliation", "")
        tgt = ps if len(ps) == 1 else [p for p in ps if p.get("raw_aff_part") == old_raw] or ps
        if op["action"] == "DROP":
            tr = f"{METHOD}: user-approved DROP (Marks); printed text: {PR.red(old_raw)}"
            for p in tgt:
                note = f"{p['ror_match_note']}; {tr}" if p.get("ror_match_note") else tr
                lset(p, "ror_match_note", note, k, op)
                lset(p, "raw_aff_part", "", k, op)
                lset(p, "ror_id", "", k, op)
                lset(p, "ror_name", "", k, op)
                lset(p, "is_panel_ror", "0", k, op)
                # country stays as on the panel (US on Nielsen, blank on SEARCA)
                lset(p, "ror_country", r.get("ror_country", ""), k, op)
        else:
            long_skip.append((k, f"unexpected action {op['action']}"))

    M.write_csv(FREEZE / LONG, lh, lrows, M.detect_lineterminator(SRC / LONG))
    M.update_working_panels()

    for (f, k), op in sorted(changed.items()):
        for fld, ov, nv in op["ch"]:
            changelog.append(dict(file=f, editor_row_key=k, editor_name=PR.red(op["editor_name"]),
                                  item=op["item"], action=op["action"], field=fld,
                                  old=PR.red(ov), new=PR.red(nv), note=PR.red(op["note"])))
    for c in changelog:
        for kk in ("old", "new", "note", "editor_name"):
            assert not PR.has_contact(c[kk] or ""), "contact in changelog"
    with open(FREEZE / CHANGELOG_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "editor_row_key", "editor_name", "item", "action", "field", "old", "new", "note"])
        w.writeheader(); w.writerows(changelog)
    with open(FREEZE / SKIPS_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["item", "action", "institution", "file", "editor_row_key", "reason"])
        w.writeheader(); w.writerows(skips)

    v = FR.verify(changed, orig, set(all_rors), nav)
    v["long_skipped"] = long_skip
    # untouched-row audit
    untouched = []
    for k in UNTOUCHED:
        f = FR.file_of(k)
        b = {r["editor_row_key"]: r for r in FR.load(f, SRC)[1]}
        n = {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]}
        if b.get(k) != n.get(k):
            untouched.append(k)
    # Diamond institution: any publish row whose canonical is that name, plus the Shenhar key already in UNTOUCHED
    for f in M.PUBLISH_FILES:
        b = {r["editor_row_key"]: r for r in FR.load(f, SRC)[1]}
        n = {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]}
        for k, r in n.items():
            if (r.get("canonical_name") or "") == "Diamond Leadership Institute" or (b.get(k, {}).get("canonical_name") or "") == "Diamond Leadership Institute":
                if r != b.get(k): untouched.append(k)
    v["untouched_rows_changed"] = sorted(set(untouched))
    v["ok"] = (v["row_counts_unchanged"] and v["long_rows"] == 269545 and v["ajg1_file_rows"] == 12326 and v["ajg1_nav"] == 10 and not v["ajg1_nav_touched"]
               and v["ajg2_rows"] == 5462 and v["ft50_rows"] == 10049 and v["ft50_ror_rows"] == 10049 and not v["header_or_eol_changes"]
               and not v["panel_unexpected"] and not v["raw_changed_outside_drop_or_paauwe"] and not v["long_unexpected"]
               and all(v["pilot_files_byte_identical"].values()) and not v["invented_ror"] and not v["protected_rows_institution_changed"] and not v["contact_n"]
               and v["long_contact_rows"][1] <= v["long_contact_rows"][0] and not v["panel_long_desync_changed_n"] and v["panel_long_desync_full_table"] <= v["base_desync_full_table"]
               and not v["nonlatin_lost"] and not v["near_miss"] and v["keep_11kbw"] and v["unsw"] and v["insead_fr_sg"] and v["working_panels_identical"]
               and not v["untouched_rows_changed"])
    log(f"verify ok={v['ok']}")
    dirdiff, eb, ea = directory_diff(changed)
    counts = {"before": PR.build("nsd_before", eb), "after": PR.build("nsd_after", ea)}
    pub = Counter()
    for (f, k), op in changed.items():
        pub[f"{op['item']}:{op['action']}"] += 1
    summ = dict(stats={k: dict(x) for k, x in stats.items()}, rows=dict(pub), skips=len(skips),
                changelog_lines=len(changelog), directory_diff_lines=len(dirdiff))
    json.dump(dict(summary=summ, verify=v, counts=counts), open(FREEZE / f"_summary_{STAMP}.json", "w"), indent=1, ensure_ascii=False, default=str)
    print(json.dumps(dict(summary=summ, counts=counts, verify_ok=v["ok"],
                          desync=(v["panel_long_desync_full_table"], v["base_desync_full_table"]),
                          unexpected=v["panel_unexpected"], long_unexp=v["long_unexpected"],
                          untouched=v["untouched_rows_changed"]), indent=1, ensure_ascii=False, default=str)[:8000])
    log(f"done ok={v['ok']}")


def directory_diff(changed):
    dk = {}
    for f in glob.glob(WI.DIR_GLOB):
        for r in csv.DictReader(open(f, encoding="utf-8-sig", newline="")): dk[(Path(f).name, r["editor_row_key"])] = r
    out, eb, ea = [], defaultdict(lambda: defaultdict(dict)), defaultdict(lambda: defaultdict(dict))
    for f in M.PUBLISH_FILES:
        b = {r["editor_row_key"]: r for r in FR.load(f, SRC)[1]}
        n = {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]}
        for k, r in n.items():
            d = dk.get((f, k))
            if d is None: continue
            for fld in list(FR.FIELDS) + (FR.NAME_FIELDS if k in FR.PAAUWE else []):
                if fld not in r or fld not in d: continue
                if b[k][fld] != d[fld]: eb[f][k][fld] = b[k][fld]
                if r[fld] != d[fld]:
                    ea[f][k][fld] = r[fld]
                    if (f, k) in changed:
                        out.append(dict(file=f, editor_row_key=k, field=fld, directory_value=PR.red(d[fld]), new_value=PR.red(r[fld])))
    with open(FREEZE / FR.DIRDIFF_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "editor_row_key", "field", "directory_value", "new_value"])
        w.writeheader(); w.writerows(out)
    return out, eb, ea


if __name__ == "__main__":
    main()
