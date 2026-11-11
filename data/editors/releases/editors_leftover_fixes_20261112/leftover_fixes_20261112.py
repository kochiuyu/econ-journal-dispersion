#!/usr/bin/env python3
"""Freeze editors_leftover_fixes_20261112 on editors_school_unit_leftover_20261112 (unpublished;
handed to Journal-Editor-Web). User-approved 2026-11-12 in Collector chat ("yes fix them").
A. AJG1 #1185, #2555, #2583 (UK "Henley Management College, UK") -> University of Reading 05v62cm79.
B1. REStud phantom rows (editor_name "Universitat Pompeu Fabra"): ft50 #577/#578 + with_ror twins -> Marks DROP.
B2. JLAS: move Unicamp (printed as phantom name on ajg2 #5450) onto Sônia Miriam Draibe ajg2 #5449
    (ROR 04wffgt70, API-verified); Marks DROP phantom #5450.
C. Long-table primary ror_country sync for panel-long country mismatches where panel has a country
    and the long primary row is blank (the 874). No panel changes in C.
Raw edits only on the B drops. No row-count/header/EOL changes. Pilots byte-identical. No publish."""
from __future__ import annotations
import csv, json, re, sys, glob, shutil, importlib.util
from collections import Counter, defaultdict
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("fr1", HERE / "full_review_fix_20261111.py")
FR = importlib.util.module_from_spec(spec); spec.loader.exec_module(FR)
spec2 = importlib.util.spec_from_file_location("sul", HERE / "school_unit_leftover_20261112.py")
SUL = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(SUL)
PR, WI, T, M = FR.PR, FR.WI, FR.T, FR.M
ROOT = M.ROOT; STAMP = "20261112"; METHOD = "leftover_fixes_20261112"
FREEZE_ID = "editors_leftover_fixes_20261112"; BASE_ID = "editors_school_unit_leftover_20261112"
SRC = ROOT / f"releases/{BASE_ID}"; FREEZE = ROOT / f"releases/{FREEZE_ID}"
for mod in (M, T, WI, PR, FR, SUL):
    for a, v in (("SRC_FREEZE", SRC), ("SRC", SRC), ("FREEZE", FREEZE)):
        if hasattr(mod, a) or mod is not SUL: setattr(mod, a, v)
M.LOGF = ROOT / f"abs_ajg/logs/leftover_fixes_{STAMP}.log"
FR.DIRDIFF_NAME = f"LEFTOVER_FIXES_directory_diff_{STAMP}.csv"
log = M.log; LONG = WI.LONG; FT = WI.FT
CHANGELOG_NAME = f"LEFTOVER_FIXES_changes_{STAMP}.csv"
SKIPS_NAME = f"LEFTOVER_FIXES_skipped_{STAMP}.csv"
R = "https://ror.org/"
READING = R + "05v62cm79"; UNICAMP = R + "04wffgt70"
HENLEY = ["editors_abs_ajg_gap_ajg1_current#1185", "editors_abs_ajg_gap_ajg1_current#2555",
          "editors_abs_ajg_gap_ajg1_current#2583"]
RES_PHANTOM = ["editors_ft50_current#577", "editors_ft50_current#578",
               "editors_ft50_current_with_ror#577", "editors_ft50_current_with_ror#578"]
DRAIBE = "editors_abs_ajg_gap_ajg2_current#5449"; JLAS_PHANTOM = "editors_abs_ajg_gap_ajg2_current#5450"
UNTOUCHED = ("editors_ft50_current#640", "editors_ft50_current#608", "editors_ft50_current#627",
             "editors_ft50_current_with_ror#640", "editors_ft50_current_with_ror#608", "editors_ft50_current_with_ror#627",
             "editors_abdc_b_current#18374", "editors_abdc_c_current#15558", "editors_abdc_c_current#15559",
             "editors_abdc_a_current#42676", "editors_abdc_b_current#16107",
             "editors_abs_ajg_gap_ajg2_current#5448", "editors_abs_ajg_gap_ajg2_current#5451")
MOVE_EXTRA_FIELDS = {"affiliation_count", "primary_aff_basis", "ror_id_aff_rank"}
BLANK_INST = ("canonical_name", "raw_affiliation", "ror_id", "ror_name", "ror_country", "continent", "lat", "lon")


def main():
    if M.LOGF.exists(): M.LOGF.unlink()
    log(f"start {FREEZE_ID}")
    catalog, all_rors, _n2i = M.build_twin_catalog(SRC)
    dir_ajg1 = glob.glob("/workspace/edj-web/data/editors/*/releases/current/editors_abs_ajg_gap_ajg1_current.csv")[0]
    dir_keys = {r["editor_row_key"] for r in csv.DictReader(open(dir_ajg1, encoding="utf-8-sig"))}
    M.copy_freeze_base()
    data = {f: FR.load(f, FREEZE) for f in M.PANEL_FILES}
    idx = {f: {r["editor_row_key"]: r for r in rows} for f, (_h, rows) in data.items()}
    orig = {f: {k: dict(r) for k, r in d.items()} for f, d in idx.items()}
    nav = {r["editor_row_key"] for r in data["editors_abs_ajg_gap_ajg1_current.csv"][1] if r["editor_row_key"] not in dir_keys}
    skips, changed, stats = [], {}, defaultdict(Counter)
    held_keys = [(f, k, SUL.hold_hit(" ".join((r.get("canonical_name") or "", r.get("raw_affiliation") or ""))))
                 for f, d in orig.items() if f not in M.PILOT_FILES for k, r in d.items()
                 if SUL.hold_hit(" ".join((r.get("canonical_name") or "", r.get("raw_affiliation") or "")))]
    log(f"held rows on base panels: {len(held_keys)}")

    def skip(item, action, name, reason, f="", k=""):
        skips.append(dict(item=item, action=action, institution=PR.red(name), file=f, editor_row_key=k, reason=PR.red(reason)))
        stats[item]["skipped"] += 1

    def snap(k, rows_src):
        f = FR.file_of(k); r = rows_src[f].get(k, {})
        return {c: r.get(c, "") for c in ("editor_name", "raw_affiliation", "canonical_name", "ror_id", "ror_name",
                                          "ror_country", "continent", "affiliation_count") if c in r}

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
            skip(item, action, name, "protected organisation on row", f, k); return False
        if SUL.hold_hit(blob):
            skip(item, action, name, "held string on row", f, k); return False
        ch = []
        for fld, val in fields.items():
            if fld in row and row[fld] != val:
                ch.append((fld, row[fld], val)); row[fld] = val
        if not ch: return False
        changed[(f, k)] = dict(item=item, action=action, name=name, ch=ch, note=note, editor_name=orig[f][k].get("editor_name", ""))
        stats[item]["applied"] += 1
        return True

    def addnote(row, tr):
        return f"{row['ror_notes']}; {tr}" if row.get("ror_notes") else tr

    # ROR API checks (cache refreshed this run in /tmp/fr/api)
    api_check = {}
    for rid, names, country in ((READING, ["University of Reading"], "United Kingdom"),
                                (UNICAMP, ["Universidade Estadual de Campinas"], "Brazil")):
        a = SUL.api(rid)
        ok = bool(a) and not a.get("_404") and a["status"] == "active" and \
            bool({SUL.fold(n) for n in a["names"]} & {SUL.fold(x) for x in names}) and \
            FR.same_country(SUL.country_norm(a["country"]), country) and not M.is_system_ror_name(a["name"])
        api_check[rid] = dict(ok=ok, status=a and a.get("status"), name=a and a.get("name"), country=a and a.get("country"),
                              in_catalog=rid in catalog)
    log(f"api {json.dumps(api_check, ensure_ascii=False)}")
    before = {k: snap(k, orig) for k in HENLEY + RES_PHANTOM + [DRAIBE, JLAS_PHANTOM]}

    # ---- A. Henley UK -> Reading
    if not (api_check[READING]["ok"] and READING in catalog):
        for k in HENLEY: skip("A_Henley", "REMATCH", "University of Reading", "05v62cm79 failed API/catalog check", FR.file_of(k), k)
    else:
        tw = catalog[READING]
        for k in HENLEY:
            f = FR.file_of(k); row = idx[f].get(k)
            if row is None: skip("A_Henley", "REMATCH", "", "row key not in panel", f, k); continue
            raw = row.get("raw_affiliation") or ""
            if not re.search(r"\bHenley\b", raw, re.I) or re.search(r"africa", raw + " " + (row.get("canonical_name") or ""), re.I) \
                    or not re.search(r"\b(?:UK|United Kingdom|England)\b", raw) or row.get("ror_id"):
                skip("A_Henley", "REMATCH", raw, "printed raw not a UK Henley masthead, mentions Africa, or ROR already set", f, k); continue
            apply("A_Henley", "REMATCH", "University of Reading", k,
                  dict(canonical_name="University of Reading", ror_id=READING, ror_name=tw["ror_name"],
                       ror_country=tw["ror_country"], continent=tw["continent"], lat=tw["lat"], lon=tw["lon"],
                       ror_notes=addnote(row, f"{METHOD}: user-approved rematch UK Henley Management College -> University of Reading 05v62cm79 (API active, United Kingdom); raw left as printed")),
                  "UK Henley -> Reading")

    # ---- B1. REStud phantoms
    for k in RES_PHANTOM:
        f = FR.file_of(k); row = idx[f].get(k)
        if row is None: skip("B1_REStud", "DROP", "", "row key not in panel", f, k); continue
        if row.get("journal") != "Review of Economic Studies" or row.get("editor_name") != "Universitat Pompeu Fabra":
            skip("B1_REStud", "DROP", row.get("editor_name", ""), "not the REStud 'Universitat Pompeu Fabra' phantom", f, k); continue
        tr = (f"{METHOD}: user-approved DROP (Marks); phantom row, printed editor_name 'Universitat Pompeu Fabra'"
              + (f", printed raw '{row.get('raw_affiliation')}'" if row.get("raw_affiliation") else "")
              + (f", was ROR {row['ror_id']}" if row.get("ror_id") else "")
              + "; real editors are #640 Enikolopov, #608 Penta, #627 Vanasco")
        fl = {c: "" for c in BLANK_INST}; fl.update(editor_name="", editor_name_raw="")
        if "ror_notes" in row: fl["ror_notes"] = addnote(row, tr)
        apply("B1_REStud", "DROP", "Universitat Pompeu Fabra", k, fl, "Marks-style DROP of phantom row (no real appointment; country/continent blanked)")

    # ---- B2. JLAS: move Unicamp onto Draibe, drop phantom
    f2 = FR.file_of(DRAIBE)
    dr, ph = idx[f2].get(DRAIBE), idx[f2].get(JLAS_PHANTOM)
    ph_ok = ph is not None and ph.get("editor_name") == "Universidade Estadual de Campinas, Brazil" and \
        ph.get("journal") == "Journal of Latin American Studies" and not ph.get("ror_id") and not ph.get("raw_affiliation")
    dr_ok = dr is not None and dr.get("editor_name") == "Sônia Miriam Draibe" and not dr.get("raw_affiliation") and not dr.get("ror_id") \
        and not dr.get("canonical_name")
    if not (ph_ok and dr_ok):
        skip("B2_JLAS", "MOVE", "Unicamp", "Draibe/phantom rows not in the expected state", f2, DRAIBE)
    else:
        if not (api_check[UNICAMP]["ok"] and UNICAMP in catalog):
            skip("B2_JLAS", "MOVE", "Unicamp", "04wffgt70 failed API/catalog check; Draibe left blank", f2, DRAIBE)
        else:
            tw = catalog[UNICAMP]
            apply("B2_JLAS", "MOVE", "Universidade Estadual de Campinas (UNICAMP)", DRAIBE,
                  dict(canonical_name=tw["ror_name"], ror_id=UNICAMP, ror_name=tw["ror_name"], ror_country=tw["ror_country"],
                       continent=tw["continent"], lat=tw["lat"], lon=tw["lon"],
                       affiliation_count="1", primary_aff_basis="single", ror_id_aff_rank="1",
                       ror_notes=f"{METHOD}: user-approved MOVE; board prints 'Universidade Estadual de Campinas, Brazil' under this editor (it was scraped into the next row #5450 as an editor name); raw_affiliation left blank, not invented; ROR 04wffgt70 API active, Brazil"),
                  "Unicamp moved from phantom #5450 onto Draibe")
        tr = f"{METHOD}: user-approved DROP (Marks); phantom row, printed editor_name 'Universidade Estadual de Campinas, Brazil' (affiliation of #5449 Sônia Miriam Draibe)"
        fl = {c: "" for c in BLANK_INST}; fl.update(editor_name="", editor_name_raw="", ror_notes=addnote(ph, tr))
        apply("B2_JLAS", "DROP", "Universidade Estadual de Campinas, Brazil", JLAS_PHANTOM, fl, "Marks-style DROP of phantom row")

    log(f"panel stats {json.dumps({k: dict(v) for k, v in stats.items()})} changed={len(changed)}")
    for f, (hdr, rows) in data.items():
        if f in M.PILOT_FILES: continue
        M.write_csv(FREEZE / f, hdr, rows, M.detect_lineterminator(SRC / f))

    # ---- long table
    lh, lrows = FR.load(LONG, FREEZE)
    by = defaultdict(list)
    for p in lrows: by[p["editor_row_key"]].append(p)
    changelog, long_skip = [], []

    def lset(p, fld, val, k, item, action, note="long sync"):
        if fld in p and p[fld] != val:
            changelog.append(dict(file=LONG, editor_row_key=k, editor_name=PR.red(p.get("editor_name", "")), item=item,
                                  action=action, field=fld, old=PR.red(p[fld]), new=PR.red(val), note=note))
            p[fld] = val

    def rank(x): return int(x["aff_rank"]) if str(x.get("aff_rank", "")).isdigit() else 99

    for (f, k), op in changed.items():
        r = idx[f][k]; ps = by.get(k)
        if not ps: long_skip.append((k, "no long-table row; panel-only (not invented)")); continue
        if op["action"] == "DROP":
            tr = f"{METHOD}: user-approved DROP (Marks); printed editor_name '{orig[f][k].get('editor_name')}'" + \
                 (f", printed raw '{orig[f][k].get('raw_affiliation')}'" if orig[f][k].get("raw_affiliation") else "")
            for p in ps:
                lset(p, "ror_match_note", f"{p['ror_match_note']}; {tr}" if p.get("ror_match_note") else tr, k, op["item"], "DROP")
                for c in ("raw_aff_part", "ror_id", "ror_name", "ror_country", "editor_name"): lset(p, c, "", k, op["item"], "DROP")
                lset(p, "is_panel_ror", "0", k, op["item"], "DROP")
        else:
            fl = [p for p in ps if p["is_panel_ror"] == "1"]
            tgt = fl[0] if fl else sorted(ps, key=rank)[0]
            for p in ps:
                if p is not tgt and p["is_panel_ror"] == "1": lset(p, "is_panel_ror", "0", k, op["item"], op["action"])
            lset(tgt, "ror_id", r["ror_id"], k, op["item"], op["action"]); lset(tgt, "ror_name", r["ror_name"], k, op["item"], op["action"])
            lset(tgt, "is_panel_ror", "1", k, op["item"], op["action"]); lset(tgt, "ror_country", r["ror_country"], k, op["item"], op["action"])
            tr = f"{METHOD}: {op['note']}"
            lset(tgt, "ror_match_note", f"{tgt['ror_match_note']}; {tr}" if tgt.get("ror_match_note") else tr, k, op["item"], op["action"])

    # ---- C. country sync (same definition as FR.verify desync; slim ft50 excluded there too)
    c_changed, c_skip = {}, []
    for f in M.PANEL_FILES:
        if f == FT: continue
        for k, r in idx[f].items():
            ps = by.get(k)
            if not ps or (f, k) in changed: continue
            fl = [p for p in ps if p["is_panel_ror"] == "1"]; rid = r.get("ror_id", "")
            if (rid and (len(fl) != 1 or fl[0]["ror_id"] != rid)) or (not rid and fl): continue
            prim = fl[0] if fl else sorted(ps, key=rank)[0]
            if prim["ror_country"] == r.get("ror_country", ""): continue
            if f in M.PILOT_FILES or "pilot" in prim.get("panel_file", ""):
                c_skip.append(dict(editor_row_key=k, reason="pilot row; left as is")); continue
            if not r.get("ror_country") or prim["ror_country"]:
                c_skip.append(dict(editor_row_key=k, reason=f"not panel-has/long-blank pattern (panel={r.get('ror_country')!r}, long={prim['ror_country']!r})")); continue
            lset(prim, "ror_country", r["ror_country"], k, "C_country_sync", "SYNC", "long primary ror_country from panel")
            c_changed[(f, k)] = dict(item="C_country_sync", action="SYNC", ch=[], note="", editor_name="")
    for s in c_skip: skip("C_country_sync", "SYNC", "", s["reason"], FR.file_of(s["editor_row_key"]), s["editor_row_key"])
    stats["C_country_sync"]["applied"] = len(c_changed)
    log(f"C synced={len(c_changed)} skipped={len(c_skip)}")

    M.write_csv(FREEZE / LONG, lh, lrows, M.detect_lineterminator(SRC / LONG))
    M.update_working_panels()

    for (f, k), op in sorted(changed.items()):
        for fld, ov, nv in op["ch"]:
            changelog.append(dict(file=f, editor_row_key=k, editor_name=PR.red(op["editor_name"]), item=op["item"],
                                  action=op["action"], field=fld, old=PR.red(ov), new=PR.red(nv), note=PR.red(op["note"])))
    for c in changelog:
        for kk in ("old", "new", "note", "editor_name"):
            assert not PR.has_contact(c[kk] or ""), "contact in changelog"
    with open(FREEZE / CHANGELOG_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "editor_row_key", "editor_name", "item", "action", "field", "old", "new", "note"])
        w.writeheader(); w.writerows(changelog)
    with open(FREEZE / SKIPS_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["item", "action", "institution", "file", "editor_row_key", "reason"])
        w.writeheader(); w.writerows(skips)

    allc = dict(changed); allc.update(c_changed)
    v = FR.verify(allc, orig, set(all_rors), nav)
    # Draibe MOVE also sets affiliation_count/primary_aff_basis/ror_id_aff_rank (approved: she now has one affiliation)
    allowed = {"raw_affiliation", "canonical_name", "ror_id", "ror_name", "ror_country", "continent", "lat", "lon", "ror_notes",
               "editor_name", "editor_name_raw"} | MOVE_EXTRA_FIELDS
    v["panel_unexpected"] = [u for u in v["panel_unexpected"] if not (len(u) == 3 and u[1] == DRAIBE and set(u[2]) <= allowed)]
    v["panel_unexpected_n"] = len(v["panel_unexpected"])
    v["long_skipped"] = long_skip
    bad = []
    for k in UNTOUCHED:
        f = FR.file_of(k)
        if {r["editor_row_key"]: r for r in FR.load(f, SRC)[1]}.get(k) != {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]}.get(k):
            bad.append(k)
    v["untouched_rows_changed"] = bad
    held_broke = []
    for f, k, label in held_keys:
        if {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]}.get(k) != orig[f][k]: held_broke.append((k, label))
    v["held_rows_changed"] = held_broke
    raw_changed = sorted(k for (f, k), op in changed.items() if any(fld == "raw_affiliation" for fld, _, _ in op["ch"]))
    v["raw_changed_this_freeze"] = raw_changed
    v["raw_changed_only_on_drops"] = all(changed[(FR.file_of(k), k)]["action"] == "DROP" for k in raw_changed)
    v["ok"] = (v["row_counts_unchanged"] and v["long_rows"] == 269545 and v["ajg1_file_rows"] == 12326 and v["ajg1_nav"] == 10 and not v["ajg1_nav_touched"]
               and v["ajg2_rows"] == 5462 and v["ft50_rows"] == 10049 and v["ft50_ror_rows"] == 10049 and not v["header_or_eol_changes"]
               and not v["panel_unexpected"] and not v["raw_changed_outside_drop_or_paauwe"] and v["raw_changed_only_on_drops"] and not v["long_unexpected"]
               and all(v["pilot_files_byte_identical"].values()) and not v["invented_ror"] and not v["protected_rows_institution_changed"] and not v["contact_n"]
               and v["long_contact_rows"][1] <= v["long_contact_rows"][0] and not v["panel_long_desync_changed_n"] and v["panel_long_desync_full_table"] <= v["base_desync_full_table"]
               and not v["nonlatin_lost"] and not v["near_miss"] and v["keep_11kbw"] and v["unsw"] and v["insead_fr_sg"] and v["working_panels_identical"]
               and not bad and not held_broke)
    log(f"verify ok={v['ok']}")
    nidx = {f: {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]} for f in M.PANEL_FILES}
    after = {k: snap(k, nidx) for k in before}
    dirdiff, eb, ea = directory_diff(changed)
    counts = {"before": PR.build("lof_before", eb), "after": PR.build("lof_after", ea)}
    # unmapped panel keys (no long row) -- report only
    unm = Counter()
    for f in M.PANEL_FILES:
        for k in nidx[f]:
            if k not in by: unm[f] += 1
    summ = dict(stats={k: dict(x) for k, x in stats.items()}, skips=len(skips), changelog_lines=len(changelog),
                directory_diff_lines=len(dirdiff), api=api_check, long_skip=long_skip, unmapped_keys=dict(unm),
                unmapped_total=sum(unm.values()), held_rows_on_base=len(held_keys), before=before, after=after)
    json.dump(dict(summary=summ, verify=v, counts=counts), open(FREEZE / f"_summary_{STAMP}.json", "w"), indent=1, ensure_ascii=False, default=str)
    shutil.copy2(Path(__file__), FREEZE / Path(__file__).name)
    log(f"done ok={v['ok']}")
    print("OK" if v["ok"] else "NOT OK")


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
            for fld in list(FR.FIELDS) + FR.NAME_FIELDS:
                if fld not in r or fld not in d: continue
                if fld in FR.NAME_FIELDS and (f, k) not in changed and k not in FR.PAAUWE: continue
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
