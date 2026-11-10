#!/usr/bin/env python3
"""Raw-drift freeze 2026-11-10 (Asia/Taipei).
Base: editors_post_review_fix_20261110 -> Freeze: editors_raw_drift_fix_20261110 (user-approved via Econ-Journal-Web).
Keyed on editor_row_key. Comparison: /workspace/raw_drift_20261110.csv (39 differing rows + 6 missing keys).
 item1 restore printed raw (Directory text) on rows where the Directory side matches the source
 item2 fix canonical/ROR/country/continent/lat/lon on those rows (panel RORs or ROR-API verified only)
 item3 FT50 #2955 Tiffany Trzebiatowski -> Colorado State University (raw = affiliation, not bio)
 item4 add Top-5 seats #10046-#10048 to both ft50 files (+ long rows), copied from the Directory (4c3cf76)
 item5 remaining role-prefix names -> parent org + existing ROR (covered by item2 rows)
Pilot files are NOT touched. Root cause (raw overwritten by derived core / ROR name in the 20261028/29
institution_* scripts) patched in those scripts; no current 20261110 script reuses that logic."""
from __future__ import annotations
import csv, json, re, sys, glob, importlib.util, hashlib
from collections import Counter, defaultdict
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("pr", HERE / "post_review_fix_20261110.py")
PR = importlib.util.module_from_spec(spec); spec.loader.exec_module(PR)
WI, T, M = PR.WI, PR.T, PR.M
ROOT = M.ROOT; STAMP = "20261110"; METHOD = "raw_drift_fix_20261110"
FREEZE_ID = "editors_raw_drift_fix_20261110"; BASE_ID = "editors_post_review_fix_20261110"
SRC = ROOT / f"releases/{BASE_ID}"; FREEZE = ROOT / f"releases/{FREEZE_ID}"
for mod in (M, T, WI, PR):
    for a, v in (("SRC_FREEZE", SRC), ("SRC", SRC), ("FREEZE", FREEZE)):
        setattr(mod, a, v)
M.LOGF = ROOT / f"abs_ajg/logs/raw_drift_fix_{STAMP}.log"
log = M.log
LONG, FT, FTR = WI.LONG, WI.FT, WI.FTR
CHANGELOG_NAME = f"RAW_DRIFT_changes_{STAMP}.csv"; SKIPS_NAME = f"RAW_DRIFT_skipped_{STAMP}.csv"
VERIFY_NAME = f"RAW_DRIFT_source_verification_{STAMP}.csv"; LEAK_NAME = f"RAW_DRIFT_leak_scan_{STAMP}.csv"
DRIFT = Path("/workspace/raw_drift_20261110.csv")
R = "https://ror.org/"
EXTRA = {  # ROR API v2 records fetched 2026-11-10 (ror_display name, geonames location); not yet on any panel row
    R + "0558j5q12": ("Universitatea Națională de Știință și Tehnologie Politehnica București", "Romania", "Europe", "44.43225", "26.10626"),
    R + "0545p3742": ("Plovdiv University", "Bulgaria", "Europe", "42.15387", "24.75001"),
    R + "03ss88z23": ("Kagoshima University", "Japan", "Asia", "31.56667", "130.55"),
    R + "014qf4206": ("Gradient (United States)", "United States", "North America", "42.35843", "-71.05977"),
    R + "00k206f19": ("École Nationale de la Statistique et de l'Analyse de l'Information", "France", "Europe", "48.02459", "-1.74709"),
    R + "01f9pza55": ("Springer Nature (Shanghai, China)", "China", "Asia", "31.22222", "121.45806"),
}
HK_GZ = R + "050h0vm43"
# key -> (ror_id, canonical ('ROR' = ror_name, 'DIR' = Directory canonical), item, note)
NLU = "printed text replaced by 'National Law University' (institution_* 20261028/29 raw rewrite) -> printed text restored"
PLAN = {
    "editors_abdc_a_current#14592": (R + "01rk35k63", "ROR", "item1+2", NLU + "; University of Lyon = Université de Lyon (panel ROR)"),
    "editors_abdc_a_current#17220": (R + "0040r6f76", "ROR", "item1+2", NLU + "; Roger Willett, 'University of Wellington' = Victoria University of Wellington (panel ROR)"),
    "editors_abdc_a_current#37088": (R + "0558j5q12", "ROR", "item1+2", NLU + "; Politehnica Bucharest (ROR API 0558j5q12)"),
    "editors_abdc_a_current#45161": (R + "03dbr7087", "ROR", "item1+2+5", NLU + "; role prefix -> University of Toronto (panel ROR)"),
    "editors_abdc_a_current#45426": (R + "00892tw58", "ROR", "item1+2+5", NLU + "; role prefix -> The University of Adelaide (panel ROR)"),
    "editors_abdc_a_current#45563": (R + "00340yn33", "ROR", "item1+2+5", NLU + "; role prefix -> Keele University (panel ROR)"),
    "editors_abdc_a_current#45879": (R + "00eae9z71", "ROR", "item1+2+5", NLU + "; role prefix -> University of Newcastle Australia (Torts Law Journal, Newcastle Law School NSW; panel ROR)"),
    "editors_abdc_a_star_current#25262": (R + "027bh9e22", "ROR", "item1+2+5", NLU + "; role prefix -> Leiden University (panel ROR); also emeritus Oxford (not a second ROR here)"),
    "editors_abdc_b_current#19961": (R + "00bge3r76", "ROR", "item1+2", NLU + "; The University of Law (UK, panel ROR)"),
    "editors_abdc_b_current#20368": (R + "03rp50x72", "ROR", "item1+2", NLU + "; University of the Witwatersrand (panel ROR)"),
    "editors_abdc_b_current#20991": (R + "04yqxxq63", "ROR", "item1+2", NLU + "; Zhongnan University of Economics and Law (panel ROR)"),
    "editors_abdc_b_current#36271": (R + "03rp50x72", "ROR", "item1+2", NLU + "; printed 'Witswatersand' (misspelt) = University of the Witwatersrand (panel ROR)"),
    "editors_abdc_b_current#37879": (R + "01x8rc503", "ROR", "item1+2", NLU + "; University of Louisiana at Lafayette (panel ROR)"),
    "editors_abdc_b_current#38870": (R + "027bh9e22", "ROR", "item1+2", NLU + "; Leiden University (panel ROR)"),
    "editors_abdc_b_current#39148": (R + "04b8v1s79", "ROR", "item1+2+5", NLU + "; role prefix; two universities printed -> first-named Tilburg University as primary (panel ROR); Leiden not added as second ROR"),
    "editors_abdc_b_current#41169": (R + "01x8rc503", "ROR", "item1+2", NLU + "; University of Louisiana at Lafayette (panel ROR)"),
    "editors_abdc_c_current#4320": (R + "01x8rc503", "ROR", "item1+2", NLU + "; University of Louisiana at Lafayette (panel ROR)"),
    "editors_abdc_c_current#12884": (R + "0545p3742", "ROR", "item1+2", NLU + "; Plovdiv University (ROR API 0545p3742)"),
    "editors_abdc_c_current#24186": (R + "027bh9e22", "ROR", "item1+2", NLU + "; Leiden University (panel ROR)"),
    "editors_abdc_c_current#24409": (R + "012zs8222", "ROR", "item1+2", NLU + "; University at Albany, SUNY (panel ROR)"),
    "editors_abs_ajg_gap_ajg2_current#3942": (R + "02kg81z20", "ROR", "item1+2", NLU + "; University of La Verne (panel ROR)"),
    "editors_abdc_c_current#14397": (R + "00k206f19", "ROR", "item1+2", "truncated raw restored; ENSAI, Campus de Ker Lann, Bruz (ROR API 00k206f19)"),
    "editors_abdc_c_current#25991": (R + "03ss88z23", "ROR", "item1+2", "raw replaced by 'Nihon University' (dept_country 20261028) -> printed 鹿児島大学 restored; Kagoshima University (ROR API 03ss88z23); wrong ROR 05jk51a88 removed"),
    "editors_abdc_c_current#27660": (R + "042nb2s44", "ROR", "item1+2", "raw replaced by 'Ikon Science' (dept_country 20261028) -> printed 'MIT Connection Science, USA' restored; MIT (panel ROR; Connection Science is an MIT research initiative)"),
    "editors_abs_ajg_gap_prio43_current#1605": (R + "01f9pza55", "ROR", "item1+2", "truncated raw restored; Springer Nature (Shanghai, China) (ROR API 01f9pza55); country 'Shanghai, China' -> China"),
    "editors_abs_ajg_gap_prio43_current#2898": (R + "014qf4206", "ROR", "item1+2", "raw replaced by 'Korea Telecom' (dept_country 20261028) -> printed 'Gradient Corporation' restored; Lorenz Rhomberg, Gradient (Boston; ROR API 014qf4206); country South Korea -> United States"),
}
for k in ("editors_abdc_a_current#3770", "editors_abdc_a_current#19309", "editors_abdc_a_current#33721", "editors_abdc_a_star_current#17502",
          "editors_abdc_a_star_current#17679", "editors_abdc_b_current#4547", "editors_abdc_b_current#10619", "editors_abdc_b_current#28350",
          "editors_abdc_c_current#4416", "editors_abdc_c_current#15812"):
    PLAN[k] = (HK_GZ, "DIR", "item1+2", "printed '(Guangzhou)' campus dropped by institution_* 20261028 strip -> printed text restored; HKUST (Guangzhou) panel ROR 050h0vm43 (China), as Directory")
PLAN["editors_abdc_c_current#27613"] = (HK_GZ, "DIR", "item1+2", "printed '(Guangzhou)' restored; ROR set to HKUST (Guangzhou) 050h0vm43 / China (Directory row still shows 00q4vv597 / Hong Kong with a Guangzhou canonical: Directory inconsistent here)")
SKIP_KEYS = {"editors_abs_ajg_gap_ajg1_current#10149": "NOT restored: the live source page (risk.net JFMI editorial board, fetched 2026-11-10) prints 'Lawrence Sweet - IZZI Inc'; the Directory text 'Rosalind Franklin University of Medicine' came from the ajg_gap faculty-search remiss (another Lawrence Sweet). Our raw 'IZZI Inc' matches the source; the Directory should take ours."}
TIFF = ("editors_ft50_current#2955", "editors_ft50_current_with_ror#2955")
CSU = R + "03k1gpj17"
NEW_KEYS = ("#10046", "#10047", "#10048")


def main():
    if M.LOGF.exists(): M.LOGF.unlink()
    log(f"start {FREEZE_ID}")
    catalog, all_rors, _ = M.build_twin_catalog(SRC)
    def rorf(rid):
        if rid in EXTRA:
            n, c, ct, la, lo = EXTRA[rid]; return dict(ror_id=rid, ror_name=n, ror_country=c, continent=ct, lat=la, lon=lo)
        t = catalog[rid]; return dict(ror_id=rid, ror_name=t["ror_name"], ror_country=t["ror_country"], continent=t["continent"], lat=t["lat"], lon=t["lon"])
    dir_rows = {}
    for f in glob.glob(WI.DIR_GLOB):
        rd = csv.DictReader(open(f, encoding="utf-8-sig", newline=""))
        dir_rows[Path(f).name] = (rd.fieldnames, list(rd))
    dk = {r["editor_row_key"]: r for _f, (_h, rows) in dir_rows.items() for r in rows}
    drift = {r["key"]: r for r in csv.DictReader(open(DRIFT, encoding="utf-8"))}
    ver = {r["editor_row_key"]: r for r in csv.DictReader(open("/tmp/rd/source_verification.csv", encoding="utf-8"))}
    M.copy_freeze_base()
    data = {f: PR.load(f, FREEZE) for f in M.PANEL_FILES}
    idx = {f: {r["editor_row_key"]: r for r in rows} for f, (_h, rows) in data.items()}
    orig = {f: {k: dict(r) for k, r in d.items()} for f, d in idx.items()}
    changelog, skips, changed = [], [], {}
    def fof(k): return k.split("#")[0] + ".csv"
    def clog(f, k, item, action, fld, old, new, note):
        changelog.append(dict(file=f, editor_row_key=k, editor_name=PR.red(idx[f][k]["editor_name"]) if f != LONG else "", item=item, action=action,
                              field=fld, old=PR.red(old), new=PR.red(new), verification=ver.get(k, {}).get("status", ""), note=note))
    def setrow(f, k, item, action, vals, note):
        row = idx[f][k]; ch = []
        for fld, v in vals.items():
            if fld in row and row[fld] != v: ch.append((fld, row[fld], v)); row[fld] = v
        if ch and "ror_notes" in row:
            nv = f"{row['ror_notes']}; {METHOD}: {item} {action} ({note[:220]})".lstrip("; ")
            ch.append(("ror_notes", row["ror_notes"], nv)); row["ror_notes"] = nv
        for fld, o, n in ch: clog(f, k, item, action, fld, o, n, note)
        if ch: changed[(f, k)] = (item, action, note, ch)
    # ---- items 1, 2, 5 ----
    assert set(PLAN) | set(SKIP_KEYS) | {TIFF[0]} == {k for k in drift if not k.endswith(NEW_KEYS)}, "plan does not cover the 39 drift rows"
    for k, (rid, canon, item, note) in PLAN.items():
        f = fof(k); d = dk[k]; row = idx[f][k]
        assert drift[k]["our_raw"][:60] == d["raw_affiliation"][:60], k
        vals = {"raw_affiliation": d["raw_affiliation"]}
        rf = rorf(rid); vals.update(rf)
        vals["canonical_name"] = rf["ror_name"] if canon == "ROR" else ("The Hong Kong University of Science and Technology (Guangzhou)" if k.endswith("#27613") else d["canonical_name"])
        setrow(f, k, item, "RESTORE_RAW+FIX_INST", vals, note)
    for k, why in SKIP_KEYS.items():
        skips.append(dict(item="item1", file=fof(k), editor_row_key=k, editor_name=idx[fof(k)][k]["editor_name"], our_raw=idx[fof(k)][k]["raw_affiliation"],
                          directory_raw=dk[k]["raw_affiliation"], reason=why))
    # ---- item 3 ----
    tnote = "bio paragraph replaced by the affiliation it states: 'Associate Professor of Management at Colorado State University' (CSU College of Business directory biz.colostate.edu/about/directory/tifftrz, checked 2026-11-10); panel ROR 03k1gpj17"
    for k in TIFF:
        f = fof(k); rf = rorf(CSU); vals = dict(raw_affiliation="Colorado State University", canonical_name="Colorado State University", **rf)
        setrow(f, k, "item3", "BIO_TO_AFFILIATION", vals, tnote)
    # ---- item 4: add Top-5 seats ----
    added = []
    for f in (FT, FTR):
        h, rows = data[f]; dh, drows = dir_rows[f]
        assert dh == h, f"header mismatch {f}"
        have = {r["editor_row_key"] for r in rows}
        for i, dr in enumerate(drows):
            if not dr["editor_row_key"].endswith(NEW_KEYS) or dr["editor_row_key"] in have: continue
            prev = drows[i - 1]["editor_row_key"]
            pos = next(j for j, r in enumerate(rows) if r["editor_row_key"] == prev) + 1
            new = {c: dr.get(c, "") for c in h}
            rows.insert(pos, new); idx[f][new["editor_row_key"]] = new; have.add(new["editor_row_key"])
            added.append((f, new["editor_row_key"], pos, prev))
            changelog.append(dict(file=f, editor_row_key=new["editor_row_key"], editor_name=new["editor_name"], item="item4", action="ADD_ROW", field="__row__", old="",
                                  new=f"{new['journal']} | {new['role']} | {new['raw_affiliation'] or '(no affiliation printed)'} | {new.get('ror_id','')}", verification="Directory copy 4c3cf76 (AER Vol 116 No 10 / REStud Vol 93 No 5 issue front matter)",
                                  note=f"copied verbatim from the Directory copy; inserted after {prev} (Directory order; UPF editor_name rows #577/#578 kept as in base)"))
    ups = [(f, r["editor_row_key"]) for f in (FT, FTR) for r in data[f][1] if r["editor_name"] == "Universitat Pompeu Fabra"]
    for f in M.PANEL_FILES:
        h, rows = data[f]; M.write_csv(FREEZE / f, h, rows, M.detect_lineterminator(SRC / f))
    # ---- long table ----
    lh, lrows = PR.load(LONG, FREEZE)
    parts = defaultdict(list)
    for x in lrows: parts[x["editor_row_key"]].append(x)
    def lset(t, fld, v, k, item, action, note):
        if t[fld] != v:
            changelog.append(dict(file=LONG, editor_row_key=k, editor_name="", item=item, action=action, field=fld, old=PR.red(t[fld]), new=PR.red(v),
                                  verification=ver.get(k, {}).get("status", ""), note=f"aff_rank {t['aff_rank']}"))
            t[fld] = v
    long_missing = []
    for (f, k), (item, action, note, ch) in changed.items():
        ps = parts.get(k)
        if not ps: long_missing.append(k); continue
        assert len(ps) == 1, k
        t = ps[0]; r = idx[f][k]
        lset(t, "raw_aff_part", r["raw_affiliation"], k, item, action, note)
        lset(t, "ror_id", r["ror_id"], k, item, action, note); lset(t, "ror_name", r["ror_name"], k, item, action, note)
        lset(t, "ror_country", r["ror_country"], k, item, action, note); lset(t, "is_panel_ror", "1" if r["ror_id"] else "0", k, item, action, note)
        lset(t, "ror_match_note", f"{t['ror_match_note']}; {METHOD}: {item} raw_aff_part restored to printed text, ROR {r['ror_id'][-9:] or 'blank'}".lstrip("; "), k, item, action, note)
    # new long rows after #10045 of each ft50 group
    for f in (FT, FTR):
        stem = f[:-4]
        newrows = []
        for fk in (FT if f == FT else FTR,):
            for suf in NEW_KEYS:
                k = stem + suf; r = idx[f][k]
                rid = r.get("ror_id", "")
                newrows.append(dict(editor_row_key=k, panel_file=f, row_index=suf[1:], journal=r["journal"], year=r["year"], editor_name=r["editor_name"],
                                    aff_text_source="raw_affiliation", aff_rank="1", raw_aff_part=r["raw_affiliation"], split_basis="single",
                                    ror_id=rid, ror_name=r.get("ror_name", ""), ror_country=r.get("ror_country", ""),
                                    ror_match_kind="panel" if rid else "panel_blank",
                                    ror_match_note=(f"panel ror_id (ror_match_method={r.get('ror_match_method','') or 'ror_consistency_20261031'})" if rid else "panel primary blank (panel ror_id empty); part not re-resolved") + f"; {METHOD}: row added (Top-5 seat copied from the Directory, 4c3cf76)",
                                    aff_role="sole", role_basis="single", role_evidence="", relation_to_primary="same" if rid else "", is_panel_ror="1" if rid else "0"))
        last = max(i for i, x in enumerate(lrows) if x["panel_file"] == f)
        assert lrows[last]["editor_row_key"] == stem + "#10045"
        lrows[last + 1:last + 1] = newrows
        for x in newrows:
            changelog.append(dict(file=LONG, editor_row_key=x["editor_row_key"], editor_name=x["editor_name"], item="item4", action="ADD_LONG_ROW", field="__row__", old="",
                                  new=f"aff_rank 1 | {x['raw_aff_part'] or '(blank)'} | {x['ror_id']}", verification="", note="long row added so panel<->long stay in sync"))
    M.write_csv(FREEZE / LONG, lh, lrows, M.detect_lineterminator(SRC / LONG))
    M.update_working_panels()
    for c in changelog:
        for kk in ("old", "new", "note"): assert not PR.has_contact(c[kk] or ""), "contact leaked into change log"
    with open(FREEZE / CHANGELOG_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(changelog[0].keys())); w.writeheader(); w.writerows(changelog)
    with open(FREEZE / SKIPS_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["item", "file", "editor_row_key", "editor_name", "our_raw", "directory_raw", "reason"]); w.writeheader(); w.writerows(skips)
    v = verify(changed, all_rors, added, ups); v["long_missing"] = long_missing
    edits = defaultdict(lambda: defaultdict(dict))
    for (f, k), (_i, _a, _n, ch) in changed.items():
        for fld, _o, nv in ch: edits[f][k][fld] = nv
    counts = {"before": PR.build("rd_before", None), "after": PR.build("rd_after", edits)}
    summ = dict(rows_changed=Counter(f"{i}:{a}" for (_f, _k), (i, a, _n, _c) in changed.items()), rows_changed_by_file=Counter(f for (f, _k) in changed),
                rows_added=added, upf_rows_kept=ups, skips=len(skips), changelog_lines=len(changelog), extra_rors=sorted(EXTRA))
    json.dump(dict(summary=summ, verify=v, counts=counts), open(FREEZE / f"_summary_{STAMP}.json", "w"), indent=1, ensure_ascii=False, default=str)
    print(json.dumps(dict(summary=summ, verify=v, counts=counts), indent=1, ensure_ascii=False, default=str)[:8000])


def verify(changed, all_rors, added, ups):
    v = {}; allowed = {"raw_affiliation", "canonical_name", "ror_id", "ror_name", "ror_country", "continent", "lat", "lon", "ror_notes"}
    added_k = {k for _f, k, _p, _q in added}
    unexpected, hdr, counts, invented, prot, contact = [], [], {}, set(), 0, []
    for f in M.PANEL_FILES:
        b = list(csv.DictReader(open(SRC / f, encoding="utf-8", newline="")))
        rd = csv.DictReader(open(FREEZE / f, encoding="utf-8", newline="")); n = list(rd)
        counts[f] = (len(b), len(n))
        if rd.fieldnames != list(b[0].keys()) or M.detect_lineterminator(SRC / f) != M.detect_lineterminator(FREEZE / f): hdr.append(f)
        nk = {r["editor_row_key"]: r for r in n}
        if [r["editor_row_key"] for r in n if r["editor_row_key"] not in added_k] != [r["editor_row_key"] for r in b]: unexpected.append((f, "order"))
        for x in b:
            y = nk[x["editor_row_key"]]
            if x == y: continue
            k = y["editor_row_key"]; diff = [c for c in x if x[c] != y[c]]
            if (f, k) not in changed or any(c not in allowed for c in diff): unexpected.append((f, k, diff))
            if y.get("ror_id") and y["ror_id"] not in all_rors and y["ror_id"] not in EXTRA: invented.add(y["ror_id"])
            if M.PROTECT_RX.search(" ".join((x.get(c) or "") for c in ("canonical_name", "raw_affiliation", "ror_name"))): prot += 1
            for c in ("raw_affiliation", "canonical_name", "ror_notes"):
                if PR.has_contact(y.get(c) or ""): contact.append(k)
    pil_ident = {f: open(SRC / f, "rb").read() == open(FREEZE / f, "rb").read() for f in M.PILOT_FILES}
    lb = list(csv.DictReader(open(SRC / LONG, encoding="utf-8", newline=""))); ln = list(csv.DictReader(open(FREEZE / LONG, encoding="utf-8", newline="")))
    lhdr = open(SRC / LONG, "rb").readline() == open(FREEZE / LONG, "rb").readline() and M.detect_lineterminator(SRC / LONG) == M.detect_lineterminator(FREEZE / LONG)
    ln_old = [x for x in ln if x["editor_row_key"] not in added_k]
    lunexp = []
    ck = {k for (_f, k) in changed}
    for x, y in zip(lb, ln_old):
        if x["editor_row_key"] != y["editor_row_key"]: lunexp.append((y["editor_row_key"], "order")); break
        if x != y and (y["editor_row_key"] not in ck or any(c not in {"raw_aff_part", "ror_id", "ror_name", "ror_country", "is_panel_ror", "ror_match_note"} for c in x if x[c] != y[c])): lunexp.append(y["editor_row_key"])
    pilot_long_same = all(x == y for x, y in zip(lb, ln_old) if "pilot" in x["panel_file"])
    by = defaultdict(list)
    for p in ln: by[p["editor_row_key"]].append(p)
    def desync(pdir, L):
        bb = defaultdict(list)
        for p in L: bb[p["editor_row_key"]].append(p)
        out = set()
        for f in M.PANEL_FILES:
            if f == FT: continue
            for r in csv.DictReader(open(pdir / f, encoding="utf-8", newline="")):
                ps = bb.get(r["editor_row_key"])
                if not ps: out.add((r["editor_row_key"], "missing")); continue
                fl = [p for p in ps if p["is_panel_ror"] == "1"]; rid = r.get("ror_id", "")
                if (rid and (len(fl) != 1 or fl[0]["ror_id"] != rid)) or (not rid and fl): out.add((r["editor_row_key"], "ror")); continue
                prim = fl[0] if fl else sorted(ps, key=lambda x: int(x["aff_rank"]) if x["aff_rank"].isdigit() else 99)[0]
                if prim["ror_country"] != r.get("ror_country", ""): out.add((r["editor_row_key"], "country"))
        return out
    ds_new, ds_base = desync(FREEZE, ln), desync(SRC, lb)
    changed_desync = [d for d in ds_new if d[0] in ck or d[0] in added_k]
    raw_sync = []
    for (f, k) in changed:
        r = next(x for x in csv.DictReader(open(FREEZE / f, encoding="utf-8")) if x["editor_row_key"] == k) if False else None
    pk = {}
    for f in M.PUBLISH_FILES:
        for r in csv.DictReader(open(FREEZE / f, encoding="utf-8", newline="")): pk[r["editor_row_key"]] = r
    for (f, k) in changed:
        if f in M.PUBLISH_FILES and by[k][0]["raw_aff_part"] != pk[k]["raw_affiliation"]: raw_sync.append(k)
    for k in added_k:
        if len(by.get(k, [])) != 1 or by[k][0]["raw_aff_part"] != pk[k]["raw_affiliation"] or by[k][0]["ror_id"] != pk[k].get("ror_id", ""): raw_sync.append(k)
    dir_keys = {r["editor_row_key"] for r in csv.DictReader(open(glob.glob("/workspace/edj-web/data/editors/*/releases/current/editors_abs_ajg_gap_ajg1_current.csv")[0], encoding="utf-8"))}
    a1 = [r["editor_row_key"] for r in csv.DictReader(open(FREEZE / "editors_abs_ajg_gap_ajg1_current.csv", encoding="utf-8"))]
    nav = {k for k in a1 if k not in dir_keys}
    keep11, unsw, insead = 0, set(), set()
    for r in pk.values():
        blob = " ".join((r.get(c) or "") for c in ("canonical_name", "raw_affiliation", "ror_name")); rid = r.get("ror_id", "")
        if "11KBW" in blob: keep11 += 1
        if re.search(r"\bUNSW\b", blob) and rid: unsw.add(rid)
        if "INSEAD" in blob and rid: insead.add(rid)
    near = [k for (f, k), (_i, _a, _n, ch) in changed.items() for fld, o, nv in ch if fld == "ror_name" for p in WI.NEAR_MISS
            if (re.search(p[0], o, re.I) and re.search(p[1], nv, re.I)) or (re.search(p[1], o, re.I) and re.search(p[0], nv, re.I))]
    exp_counts = {f: (a, a + (3 if f in (FT, FTR) else 0)) for f, (a, _b) in counts.items()}
    v.update(row_counts=counts, row_counts_as_expected=all(counts[f] == exp_counts[f] for f in counts), long_rows=(len(lb), len(ln)),
             ajg1_file_rows=len(a1), ajg1_nav=len(nav), ajg1_nav_touched=len([1 for (f, k) in changed if k in nav]), ajg2_rows=counts["editors_abs_ajg_gap_ajg2_current.csv"][1],
             header_or_eol_changes=hdr + ([] if lhdr else [LONG]), panel_unexpected=unexpected[:10], panel_unexpected_n=len(unexpected),
             long_unexpected=lunexp[:10], long_unexpected_n=len(lunexp), pilot_files_byte_identical=pil_ident, pilot_long_rows_unchanged=pilot_long_same,
             invented_ror=sorted(invented), new_real_ror_added=sorted(EXTRA), protected_rows_changed=prot, contact_in_changed_rows=contact,
             panel_long_desync_changed_rows=changed_desync, panel_long_desync_full_table=len(ds_new), base_desync_full_table=len(ds_base),
             raw_part_not_synced=raw_sync, near_miss_merges=near, upf_rows_present=ups,
             keep_11kbw=keep11 > 0, unsw=M.UNSW_SYDNEY in unsw, insead_fr_sg=M.INSEAD_FRANCE in insead and M.INSEAD_SINGAPORE in insead,
             working_panels_identical=all(open(FREEZE / f, "rb").read() == open(p, "rb").read() for f, p in M.LIVE_PANELS.items()))
    v["ok"] = (v["row_counts_as_expected"] and len(a1) == 12326 and len(nav) == 10 and not v["ajg1_nav_touched"] and v["ajg2_rows"] == 5462
               and len(lb) == 269539 and len(ln) == 269545 and not v["header_or_eol_changes"] and not unexpected and not lunexp and all(pil_ident.values()) and pilot_long_same
               and not invented and prot == 0 and not contact and not changed_desync and len(ds_new) <= len(ds_base) and not raw_sync and not near
               and len(ups) == 4 and v["keep_11kbw"] and v["unsw"] and v["insead_fr_sg"] and v["working_panels_identical"])
    log(f"verify ok={v['ok']}")
    return v


if __name__ == "__main__":
    main()
