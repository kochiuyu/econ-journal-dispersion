#!/usr/bin/env python3
"""Follow-up freeze 2026-11-11 (Asia/Taipei): editors_full_review_resolved_fix_20261111.
Base: editors_full_review_fix_20261111. Keyed on editor_row_key (row-level; no display-key spreading).
 R*: /workspace/institutions_review_resolved_20261111.csv (675 previously held Institutions)
 S*: /workspace/institutions_coinflip_splits_20261111.csv (223 row-level campus splits), applied after R; split wins on conflicts.
Not applied: institutions_review_coinflips_20261111.csv. Pilots untouched; raw only blanked on Marks DROPs."""
from __future__ import annotations
import csv, json, re, sys, glob, importlib.util
from collections import Counter, defaultdict
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("fr1", HERE / "full_review_fix_20261111.py")
FR = importlib.util.module_from_spec(spec); spec.loader.exec_module(FR)
PR, WI, T, M = FR.PR, FR.WI, FR.T, FR.M
ROOT = M.ROOT; STAMP = "20261111"; METHOD = "full_review_resolved_fix_20261111"
FREEZE_ID = "editors_full_review_resolved_fix_20261111"; BASE_ID = "editors_full_review_fix_20261111"
SRC = ROOT / f"releases/{BASE_ID}"; FREEZE = ROOT / f"releases/{FREEZE_ID}"
for mod in (M, T, WI, PR, FR):
    for a, v in (("SRC_FREEZE", SRC), ("SRC", SRC), ("FREEZE", FREEZE)):
        setattr(mod, a, v)
M.LOGF = ROOT / f"abs_ajg/logs/full_review_resolved_fix_{STAMP}.log"
FR.DIRDIFF_NAME = f"FULL_REVIEW_RESOLVED_directory_diff_{STAMP}.csv"
log = M.log
LONG, FT, FTR = WI.LONG, WI.FT, WI.FTR
CHANGELOG_NAME = f"FULL_REVIEW_RESOLVED_changes_{STAMP}.csv"; SKIPS_NAME = f"FULL_REVIEW_RESOLVED_skipped_{STAMP}.csv"
RES = Path("/workspace/institutions_review_resolved_20261111.csv")
SPL = Path("/workspace/institutions_coinflip_splits_20261111.csv")
R = "https://ror.org/"
# ROR API v2, fetched 2026-11-11 (Asia/Taipei): not yet on any panel row; active and matching name + country
EXTRA = {
    R + "010zh7098": ("Saint Mary's University", "Canada", "North America", "44.64269", "-63.57688"),          # Halifax
    R + "023ahcz89": ("Max Planck Institute for Comparative and International Private Law", "Germany", "Europe", "53.55073", "9.99302"),  # Hamburg
    R + "00myn0z94": ("Institut de Recherche en Informatique et Systèmes Aléatoires", "France", "Europe", "48.11109", "-1.67431"),  # IRISA Rennes
    R + "0555ezg60": ("Huaiyin Institute of Technology", "China", "Asia", "33.58861", "119.01917"),
    R + "05vr1c885": ("Henan Polytechnic University", "China", "Asia", "35.23972", "113.23306"),
    R + "00bzdg454": ("KMA Consulting Ltd. (Saint Lucia)", "Saint Lucia", "North America", "13.9957", "-61.00614"),
    R + "05vg74d16": ("Norwegian Institute of Marine Research", "Norway", "Europe", "60.39299", "5.32415"),
    R + "04k83g518": ("Concordia University Wisconsin", "United States", "North America", "43.21555", "-88.03001"),
}
# ROR API returned 404 (no such record): ROR left blank, logged
API_404 = {R + "028zh6278": "Mercer University", R + "03jbxjb94": "Czech Technical University in Prague", R + "047t3d518": "CY Cergy Paris Université"}
CALGARY = R + "05y6c7y19"


def main():
    if M.LOGF.exists(): M.LOGF.unlink()
    log(f"start {FREEZE_ID}")
    res = list(csv.DictReader(open(RES, encoding="utf-8")))
    spl = list(csv.DictReader(open(SPL, encoding="utf-8")))
    log(f"resolved={len(res)} {dict(Counter(r['action'] for r in res))} splits={len(spl)}")
    catalog, all_rors, name_to_ids = M.build_twin_catalog(SRC)
    cont = T.continent_map()
    for c, v in FR.EXTRA_CONT.items(): cont.setdefault(c, v)
    cont.setdefault("Saint Lucia", "North America"); cont.setdefault("Vietnam", "Asia"); cont.setdefault("Uzbekistan", "Asia"); cont.setdefault("Oman", "Asia")
    dir_ajg1 = glob.glob("/workspace/edj-web/data/editors/*/releases/current/editors_abs_ajg_gap_ajg1_current.csv")[0]
    dir_keys = {r["editor_row_key"] for r in csv.DictReader(open(dir_ajg1, encoding="utf-8-sig"))}
    M.copy_freeze_base()
    data = {f: FR.load(f, FREEZE) for f in M.PANEL_FILES}
    idx = {f: {r["editor_row_key"]: r for r in rows} for f, (_h, rows) in data.items()}
    orig = {f: {k: dict(r) for k, r in d.items()} for f, d in idx.items()}
    nav = {r["editor_row_key"] for r in data["editors_abs_ajg_gap_ajg1_current.csv"][1] if r["editor_row_key"] not in dir_keys}
    skips, changed = [], {}
    st = defaultdict(Counter)

    def skip(src, action, name, reason, f="", k=""):
        skips.append(dict(item=src, action=action, institution=PR.red(name), file=f, editor_row_key=k, reason=PR.red(reason)))

    def rorf(rid):
        if rid in EXTRA:
            n, c, co, la, lo = EXTRA[rid]; return dict(ror_id=rid, ror_name=n, ror_country=c, continent=co, lat=la, lon=lo)
        tw = catalog[rid]; return dict(ror_id=rid, ror_name=tw["ror_name"], ror_country=tw["ror_country"], continent=tw["continent"], lat=tw["lat"], lon=tw["lon"])

    def resolve(src, action, inst, tro, tname, tcy, k):
        """-> (rid or '', reason-if-blank)"""
        if tro:
            if tro in API_404: return "", f"target ROR {tro} not found in ROR API (404); ROR left blank"
            if tro not in catalog and tro not in EXTRA: return "", f"target ROR {tro} not in panels and not API-verified; ROR left blank"
            nm = rorf(tro)["ror_name"]
            if M.is_system_ror_name(nm) or M.is_system_ror_name(tname): return "", f"university-system ROR {tro} refused"
            if tcy and not FR.same_country(rorf(tro)["ror_country"], tcy): return None, f"target ROR {tro} country {rorf(tro)['ror_country']} != target_country {tcy}"
            return tro, ""
        return "", ""

    def targets(k):
        out = [k]
        tk = FR.twin_of(k)
        if tk: out.append(tk)
        return out

    def apply(src, action, inst, k, fields, note):
        f = FR.file_of(k)
        if f in M.PILOT_FILES: skip(src, action, inst, "pilot file must stay byte-identical", f, k); return False
        row = idx.get(f, {}).get(k)
        if row is None: skip(src, action, inst, "row key not in panel", f, k); return False
        if k in nav: skip(src, action, inst, "AJG1 nav row untouched", f, k); return False
        blob = " ".join((row.get(c) or "") for c in ("canonical_name", "raw_affiliation", "ror_name"))
        if M.PROTECT_RX.search(blob) or re.search(r"1\s*decembrie\s*1918", blob, re.I):
            skip(src, action, inst, "protected organisation on row (11KBW/UNSW/INSEAD/1 Decembrie 1918)", f, k); return False
        if f == FT:  # ft50_current twin: same printed raw as the with_ror row required
            tw = idx[FTR].get(FR.twin_of(k))
            if tw is not None and tw.get("raw_affiliation") != row.get("raw_affiliation") and not k.startswith("editors_ft50_current#") is False:
                pass
        fl = dict(fields)
        if FR.mostly_nonlatin(row.get("canonical_name") or row.get("raw_affiliation")) and "canonical_name" in fl and action != "DROP":
            fl.pop("canonical_name"); note += "; non-Latin printed name kept as canonical (ROR/country only)"
        cur = (row.get("ror_id") or "").strip()
        if action in ("MERGE", "RENAME", "SPLIT") and cur and fl.get("ror_id") and cur != fl["ror_id"]:
            for a, b in FR.NEAR_MISS:
                o, n = row.get("ror_name", ""), fl.get("ror_name", "")
                if (re.search(a, o, re.I) and re.search(b, n, re.I)) or (re.search(b, o, re.I) and re.search(a, n, re.I)):
                    skip(src, action, inst, f"near-miss pair ({o} -> {n}); not rematched", f, k); return False
            note += f"; ROR replaced {cur} -> {fl['ror_id']} (row-level evidence)"
        if action in ("MERGE", "RENAME", "SPLIT") and cur and not fl.get("ror_id") and "ror_id" in fl:
            # target has no verified ROR: keep the row's existing ROR only if it agrees with target country, else blank
            if FR.same_country(row.get("ror_country", ""), fields.get("ror_country", "")) and cur != CALGARY:
                for x in ("ror_id", "ror_name", "lat", "lon"): fl.pop(x, None)
                note += f"; existing ROR {cur} kept (no verified target ROR)"
        ch = []
        for fld, val in fl.items():
            if fld in row and row[fld] != val: ch.append((fld, row[fld], val)); row[fld] = val
        if not ch: return False
        if (f, k) in changed:
            changed[(f, k)]["ch"].extend(ch); changed[(f, k)]["note"] += " | " + note; changed[(f, k)]["item"] += "+" + src
        else:
            changed[(f, k)] = dict(item=src, action=action, name=inst, ch=ch, note=note, editor_name=row.get("editor_name", ""))
        return True

    split_keys = {r["editor_row_key"] for r in spl}
    conflicts = []

    def do(src, action, inst, keys, tname, tro, tcy, note):
        tcy = FR.norm_country(tcy)
        n = 0
        if action == "DROP":
            for k in keys:
                for kk in targets(k):
                    f = FR.file_of(kk); row = idx.get(f, {}).get(kk)
                    if row is None: skip(src, action, inst, "row key not in panel", f, kk); continue
                    if row.get("ror_id"): skip(src, action, inst, f"row carries ROR {row['ror_id']}; not dropped", f, kk); continue
                    raw = row.get("raw_affiliation", "")
                    fl = dict(canonical_name="", raw_affiliation="", ror_id="", ror_name="", lat="", lon="")
                    if "ror_notes" in row:
                        tr = f"{METHOD}: user-approved DROP (Marks); printed text: {PR.red(raw or inst)}"
                        fl["ror_notes"] = f"{row['ror_notes']}; {tr}" if row.get("ror_notes") else tr
                    n += apply(src, action, inst, kk, fl, "Marks-style DROP")
            return n
        rid, why = resolve(src, action, inst, tro, tname, tcy, keys[0] if keys else "")
        if rid is None: 
            for k in keys: skip(src, action, inst, why, FR.file_of(k), k)
            return 0
        if why: skip(src, action, inst, why + " (row still renamed/country set)")
        if action == "SET_COUNTRY":
            fl = dict(ror_country=tcy, continent=cont.get(tcy, ""))
            if tname and tname != inst: fl["canonical_name"] = tname
            if rid: fl.update(rorf(rid))
        else:
            fl = dict(canonical_name=tname)
            if rid: fl.update(rorf(rid))
            else:
                fl.update(dict(ror_id="", ror_name="", lat="", lon=""))
                if tcy: fl.update(ror_country=tcy, continent=cont.get(tcy, ""))
        for k in keys:
            for kk in targets(k):
                f = FR.file_of(kk); row = idx.get(f, {}).get(kk)
                if action == "SET_COUNTRY" and row is not None and row.get("ror_id") and not rid and row.get("ror_country") and not FR.same_country(row["ror_country"], tcy):
                    skip(src, action, inst, f"row carries ROR {row['ror_id']} in {row['ror_country']}; country not overridden", f, kk); continue
                if kk != k and row is not None and idx.get(FR.file_of(k), {}).get(k, {}).get("raw_affiliation") != row.get("raw_affiliation"):
                    skip(src, action, inst, "FT50 twin prints different raw; twin not changed", f, kk); continue
                n += apply(src, action, inst, kk, fl, note)
        return n

    # R: resolved file
    for r in res:
        keys = FR.keys_of(r["editor_row_keys"])
        ck = [k for k in keys if k in split_keys]
        for k in ck: conflicts.append(dict(editor_row_key=k, resolved_action=r["action"], resolved_target=r["target_name"], split_target=next(s["target_name"] for s in spl if s["editor_row_key"] == k)))
        keys = [k for k in keys if k not in split_keys]
        note = f"{r['action']} ({r['evidence']}{': ' + r['evidence_url'] if r['evidence_url'] else ''})"
        n = do("R", r["action"], r["institution"], keys, (r["target_name"] or "").strip(), (r["target_ror"] or "").strip(), r["target_country"], note) if keys else 0
        st["R"][(r["action"], "applied" if n else "no_change_or_skipped")] += 1
        if not n and keys and not any(s["institution"] == PR.red(r["institution"]) for s in skips[-6:]): skip("R", r["action"], r["institution"], "no-op: rows already at target")
    # S: coinflip splits (win)
    for s in spl:
        k = s["editor_row_key"]
        note = f"SPLIT ({s['evidence']}{': ' + s['evidence_url'] if s['evidence_url'] else ''})"
        n = do("S", "SPLIT", s["current institution"], [k], s["target_name"].strip(), s["target_ror"].strip(), s["target_country"], note)
        st["S"]["applied" if n else "no_change_or_skipped"] += 1
        if not n and not any(x["editor_row_key"] == k for x in skips[-3:]): skip("S", "SPLIT", s["current institution"], "no-op: row already at target", FR.file_of(k), k)
    log(f"stats R={dict(st['R'])} S={dict(st['S'])} conflicts={len(conflicts)} changed={len(changed)}")

    for f, (hdr, rows) in data.items():
        if f in M.PILOT_FILES: continue
        M.write_csv(FREEZE / f, hdr, rows, M.detect_lineterminator(SRC / f))
    # long sync (same as freeze 1)
    lh, lrows = FR.load(LONG, FREEZE)
    by = defaultdict(list)
    for p in lrows: by[p["editor_row_key"]].append(p)
    changelog, long_skip = [], []
    def lset(p, fld, val, k, op):
        if fld in p and p[fld] != val:
            changelog.append(dict(file=LONG, editor_row_key=k, editor_name=PR.red(p.get("editor_name", "")), item=op["item"], action=op["action"], field=fld, old=PR.red(p[fld]), new=PR.red(val), verification="", note="long sync")); p[fld] = val
    rank = lambda p: int(p["aff_rank"]) if str(p.get("aff_rank", "")).isdigit() else 99
    for (f, k), op in changed.items():
        r, o = idx[f][k], orig[f][k]; ps = by.get(k)
        if not ps: long_skip.append((k, "no long rows")); continue
        if r.get("raw_affiliation", "") != o.get("raw_affiliation", ""):
            tgt = ps if len(ps) == 1 else [p for p in ps if p["raw_aff_part"] == o["raw_affiliation"]]
            if not tgt: long_skip.append((k, "multi-part long row; DROP raw_aff_part not auto-blanked"))
            for p in tgt:
                tr = f"{METHOD}: user-approved DROP (Marks); printed text: {PR.red(o['raw_affiliation'])}"
                lset(p, "ror_match_note", f"{p['ror_match_note']}; {tr}" if p["ror_match_note"] else tr, k, op); lset(p, "raw_aff_part", "", k, op)
        if r.get("ror_id", "") != o.get("ror_id", ""):
            fl = [p for p in ps if p["is_panel_ror"] == "1"]
            if r.get("ror_id"):
                t = fl[0] if fl else sorted(ps, key=rank)[0]
                for x in fl:
                    if x is not t: lset(x, "is_panel_ror", "0", k, op)
                lset(t, "ror_id", r["ror_id"], k, op); lset(t, "ror_name", r.get("ror_name", ""), k, op); lset(t, "is_panel_ror", "1", k, op)
            else:
                for x in fl: lset(x, "ror_id", "", k, op); lset(x, "ror_name", "", k, op); lset(x, "is_panel_ror", "0", k, op)
        fl = [p for p in ps if p["is_panel_ror"] == "1"]
        prim = fl[0] if fl else sorted(ps, key=rank)[0]
        lset(prim, "ror_country", r.get("ror_country", ""), k, op)
    M.write_csv(FREEZE / LONG, lh, lrows, M.detect_lineterminator(SRC / LONG))
    M.update_working_panels()
    for (f, k), op in sorted(changed.items()):
        for fld, ov, nv in op["ch"]:
            changelog.append(dict(file=f, editor_row_key=k, editor_name=PR.red(op["editor_name"]), item=op["item"], action=op["action"], field=fld, old=PR.red(ov), new=PR.red(nv), verification="", note=PR.red(op["note"])))
    for c in changelog:
        for kk in ("old", "new", "note", "editor_name"): assert not PR.has_contact(c[kk] or ""), "contact in changelog"
    with open(FREEZE / CHANGELOG_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "editor_row_key", "editor_name", "item", "action", "field", "old", "new", "verification", "note"]); w.writeheader(); w.writerows(changelog)
    with open(FREEZE / SKIPS_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["item", "action", "institution", "file", "editor_row_key", "reason"]); w.writeheader(); w.writerows(skips)
    with open(FREEZE / f"FULL_REVIEW_RESOLVED_split_conflicts_{STAMP}.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["editor_row_key", "resolved_action", "resolved_target", "split_target"]); w.writeheader(); w.writerows(conflicts)
    # verify: reuse freeze-1 checks; new RORs = EXTRA
    all2 = set(all_rors) | set(EXTRA)
    v = FR.verify(changed, orig, all2, nav)
    v["long_skipped"] = long_skip
    # Calgary audit
    cal = []
    for f in M.PANEL_FILES:
        for r in csv.DictReader(open(FREEZE / f, encoding="utf-8")):
            if r.get("ror_id") == CALGARY: cal.append((r["editor_row_key"], r["raw_affiliation"], bool(re.search(r"calgary", r["raw_affiliation"], re.I))))
    lcal = [(p["editor_row_key"], p["raw_aff_part"]) for p in lrows if p["ror_id"] == CALGARY]
    v["calgary_ror_rows"] = cal; v["calgary_ror_long"] = lcal
    v["ok"] = v["ok"] and all(c[2] for c in cal)
    # Directory: before = Directory + F1 values (incl. Paauwe names), after = + this freeze
    dirdiff, eb, ea = directory_diff(changed)
    counts = {"before": PR.build("frr_before", eb), "after": PR.build("frr_after", ea)}
    pub = Counter(); ftm = Counter()
    for (f, k), op in changed.items():
        (ftm if f == FT else pub)[op["item"][0] + ":" + op["action"]] += 1
    summ = dict(resolved_file=dict(Counter(r["action"] for r in res)), resolved_outcome={f"{a}|{b}": n for (a, b), n in st["R"].items()},
                splits_file=len(spl), splits_outcome=dict(st["S"]), split_conflicts=len(conflicts), rows_publish=dict(pub), rows_ft50_current_mirror=dict(ftm),
                skips=len(skips), skip_reasons=dict(Counter(f"{s['item']}:{s['action']}: {s['reason'][:70]}" for s in skips).most_common(40)),
                changelog_lines=len(changelog), directory_diff_lines=len(dirdiff), new_rors_api_verified=sorted(EXTRA), api_404_left_blank=API_404)
    json.dump(dict(summary=summ, verify=v, counts=counts), open(FREEZE / f"_summary_{STAMP}.json", "w"), indent=1, ensure_ascii=False, default=str)
    print(json.dumps(dict(summary=summ, verify={k: x for k, x in v.items() if k not in ("row_counts",)}, counts=counts), indent=1, ensure_ascii=False, default=str)[:12000])
    log(f"done ok={v['ok']}")


def directory_diff(changed):
    dk = {}
    for f in glob.glob(WI.DIR_GLOB):
        for r in csv.DictReader(open(f, encoding="utf-8-sig", newline="")): dk[(Path(f).name, r["editor_row_key"])] = r
    out, eb, ea = [], defaultdict(lambda: defaultdict(dict)), defaultdict(lambda: defaultdict(dict))
    for f in M.PUBLISH_FILES:
        b = {r["editor_row_key"]: r for r in FR.load(f, SRC)[1]}; n = {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]}
        for k, r in n.items():
            d = dk.get((f, k))
            if d is None: continue
            for fld in FR.FIELDS + (FR.NAME_FIELDS if k in FR.PAAUWE else []):
                if fld not in r or fld not in d: continue
                if b[k][fld] != d[fld]: eb[f][k][fld] = b[k][fld]
                if r[fld] != d[fld]:
                    ea[f][k][fld] = r[fld]
                    if (f, k) in changed: out.append(dict(file=f, editor_row_key=k, field=fld, directory_value=PR.red(d[fld]), new_value=PR.red(r[fld])))
    with open(FREEZE / FR.DIRDIFF_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "editor_row_key", "field", "directory_value", "new_value"]); w.writeheader(); w.writerows(out)
    return out, eb, ea


if __name__ == "__main__":
    main()
