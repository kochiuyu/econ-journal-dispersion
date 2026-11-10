#!/usr/bin/env python3
"""Post-full-review freeze 2026-11-11 (Asia/Taipei): editors_post_fullreview_fix_20261111.
Base: editors_full_review_resolved_fix_20261111 (live via PR #54). Keyed on editor_row_key (listed keys + raw-equal FT50 twins).
 A  a_campus_merge_77: keep all 77; FT50 #4634 set to what the JOM board prints (approved raw edit on ft50_current#4634)
 B  b_drop_real_org_44: 38 RENAME (API-verified ROR or name+country), 6 KEEP_AS_IS
 C  c_ror_checks: Mercer 04bk7v425, CTU Prague 03kqpb082, CY Cergy 043htjv09
 D  approved pilot scrub: faculty_profile_url blanked on editors_abdc_a_current_with_profile_pilot#15779 only
 Residual file (982 rows): WRONG_ROR successors, NEAR_DUPLICATE, MISSING_ROR, WRONG_COUNTRY, NON_INSTITUTION, MISSING_COUNTRY;
 BIO_OR_MULTI_ORG has no targets (left as printed); HELD_COIN_FLIP + NON_LATIN untouched."""
from __future__ import annotations
import csv, json, re, sys, glob, importlib.util, unicodedata, os
from collections import Counter, defaultdict
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("fr1", HERE / "full_review_fix_20261111.py")
FR = importlib.util.module_from_spec(spec); spec.loader.exec_module(FR)
PR, WI, T, M = FR.PR, FR.WI, FR.T, FR.M
ROOT = M.ROOT; STAMP = "20261111"; METHOD = "post_fullreview_fix_20261111"
FREEZE_ID = "editors_post_fullreview_fix_20261111"; BASE_ID = "editors_full_review_resolved_fix_20261111"
SRC = ROOT / f"releases/{BASE_ID}"; FREEZE = ROOT / f"releases/{FREEZE_ID}"
for mod in (M, T, WI, PR, FR):
    for a, v in (("SRC_FREEZE", SRC), ("SRC", SRC), ("FREEZE", FREEZE)):
        setattr(mod, a, v)
M.LOGF = ROOT / f"abs_ajg/logs/post_fullreview_fix_{STAMP}.log"
FR.DIRDIFF_NAME = f"POST_FULLREVIEW_directory_diff_{STAMP}.csv"
log = M.log
LONG, FT, FTR = WI.LONG, WI.FT, WI.FTR
CHANGELOG_NAME = f"POST_FULLREVIEW_changes_{STAMP}.csv"; SKIPS_NAME = f"POST_FULLREVIEW_skipped_{STAMP}.csv"
ANS = Path("/workspace/collector_answers_20261111")
RESID = Path("/workspace/institutions_post_fullreview_residual_20261111.csv")
API = Path("/tmp/fr/api")
R = "https://ror.org/"
PILOT_SCRUB = ("editors_abdc_a_current_with_profile_pilot.csv", "editors_abdc_a_current_with_profile_pilot#15779")
K4634 = "editors_ft50_current#4634"
RAW_OK = {K4634}
FR.PAAUWE = dict(FR.PAAUWE); FR.PAAUWE[K4634] = FT   # verify: approved raw edit allowed on this key
MPG, CNRS = R + "01hhn8329", R + "02feahw73"
ND_SKIP = {  # NEAR_DUPLICATE targets refused by the guards (reason)
    "Max Planck Institute, Germany": "would collapse to the Max Planck Society", "Max Planck Institute Germany": "would collapse to the Max Planck Society",
    "Max Planck Institute": "would collapse to the Max Planck Society",
    "CNRS – École Polytechnique and London School of Economi": "multi-org string; would collapse to CNRS only",
    "CNRS - CEPREMA P and EHESS Paris": "multi-org string; would collapse to CNRS only",
    "Indian Institute of Information Technology, Raichur": "IIIT Raichur stays a distinct campus",
    "Monash University in China": "Monash China is not Monash (Australia); fixed by WRONG_COUNTRY instead",
    "Concordia U., CA": "coin-flip Canada/California (held)", "Universidad del Pacifico, Engineering": "coin-flip Peru/Chile (held)",
    "University of Naples, Naples": "which Naples university is unclear (held coin-flip)",
    "The University of Texas, United States": "university system; no campus evidenced",
    "Swedish School of Economics, Finland and EM Lyon": "two-organisation string stays as printed",
    "HEC Liège – Liège University and Belfius Asset Manageme": "two-organisation string stays as printed",
    "Michigan State University, USA; Queen Mary, University ": "two-organisation string stays as printed",
    "Linklaters, London": "target 'LINKLATERS' sits in Portugal; London office must not inherit it",
    "Facultad Latinoamericana de Ciencias Sociales (FLASCO)": "which national FLACSO is not evidenced",
}
LOW_MR_OK = {"Telethon Kids Institute", "Mercy College"}   # optional low-confidence generic names accepted only if API alias + country agree
MULTI_OFFICE = {"Emerald Publishing", "Emerald Group Publishing", "IFPRI", "Putnam", "IMD"}
WC_SKIP = {"Creative New Zealand": "printed text is 'Creative Capital, New York' - institution name is wrong, not the country; needs a rename",
           "St. Catharine's": "coin-flip: St Catharine's College (UK) vs St. Catharines (Canada); printed text gives no evidence"}


def fold(s): return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().casefold())


def api(rid):
    p = API / f"{rid.replace(R, '')}.json"
    if not p.exists(): return None
    d = json.load(open(p))
    if d.get("_404"): return {"_404": True}
    loc = d["locations"][0]["geonames_details"]
    return dict(status=d["status"], names=[n["value"] for n in d["names"]], country=loc.get("country_name", ""), continent=loc.get("continent_name", ""),
                lat=str(loc.get("lat", "")), lon=str(loc.get("lng", "")), name=next((n["value"] for n in d["names"] if "ror_display" in n.get("types", [])), d["names"][0]["value"]),
                succ=[r["id"] for r in d.get("relationships", []) if r["type"] == "successor"], types=d.get("types", []))


def main():
    if M.LOGF.exists(): M.LOGF.unlink()
    log(f"start {FREEZE_ID}")
    catalog, all_rors, name_to_ids = M.build_twin_catalog(SRC)
    cont = T.continent_map()
    for c, v in FR.EXTRA_CONT.items(): cont.setdefault(c, v)
    for c, v in {"Guam": "Oceania", "Isle of Man": "Europe", "Luxembourg": "Europe", "Thailand": "Asia", "Israel": "Asia", "South Africa": "Africa", "Vietnam": "Asia", "Saint Lucia": "North America"}.items(): cont.setdefault(c, v)
    dir_ajg1 = glob.glob("/workspace/edj-web/data/editors/*/releases/current/editors_abs_ajg_gap_ajg1_current.csv")[0]
    dir_keys = {r["editor_row_key"] for r in csv.DictReader(open(dir_ajg1, encoding="utf-8-sig"))}
    M.copy_freeze_base()
    data = {f: FR.load(f, FREEZE) for f in M.PANEL_FILES}
    idx = {f: {r["editor_row_key"]: r for r in rows} for f, (_h, rows) in data.items()}
    orig = {f: {k: dict(r) for k, r in d.items()} for f, d in idx.items()}
    nav = {r["editor_row_key"] for r in data["editors_abs_ajg_gap_ajg1_current.csv"][1] if r["editor_row_key"] not in dir_keys}
    skips, changed, extra, stats = [], {}, {}, defaultdict(Counter)

    def skip(item, action, name, reason, f="", k=""):
        skips.append(dict(item=item, action=action, institution=PR.red(name), file=f, editor_row_key=k, reason=PR.red(reason)))

    def country_norm(c):
        c = FR.norm_country(c)
        return {"United States of America": "United States", "Czech Republic": "Czechia", "Viet Nam": "Vietnam", "Korea, Republic of": "South Korea",
                "Russian Federation": "Russia", "Turkey": "Türkiye", "Republic of Türkiye": "Türkiye"}.get(c, c)

    def rorf(rid):
        if rid in catalog:
            tw = catalog[rid]; return dict(ror_id=rid, ror_name=tw["ror_name"], ror_country=tw["ror_country"], continent=tw["continent"], lat=tw["lat"], lon=tw["lon"])
        a = api(rid); c = country_norm(a["country"])
        extra[rid] = dict(name=a["name"], country=c)
        return dict(ror_id=rid, ror_name=a["name"], ror_country=c, continent=cont.get(c) or a["continent"], lat=a["lat"], lon=a["lon"])

    def check_ror(rid, names, country, require_name=True):
        """(ok, reason). Catalog RORs need only be active (if fetched); new ones must be active and match name + country."""
        a = api(rid)
        if a is None:
            if rid in catalog: return True, ""
            return False, f"{rid} not fetched from ROR API"
        if a.get("_404"): return False, f"{rid} not in ROR API (404)"
        if a["status"] != "active": return False, f"{rid} is {a['status']} in ROR API"
        if M.is_system_ror_name(a["name"]): return False, f"{rid} is a university-system ROR"
        if rid in catalog: return True, ""
        if require_name and not ({fold(n) for n in a["names"]} & {fold(re.sub(r"\s*\([^)]*\)\s*$", "", x)) for x in names if x} | {fold(x) for x in names if x}):
            return False, f"{rid} names {a['names'][:3]} do not match {names}"
        if country and not FR.same_country(country_norm(a["country"]), country_norm(country)):
            return False, f"{rid} country {a['country']} != {country}"
        return True, ""

    def apply(item, action, name, k, fields, note):
        f = FR.file_of(k)
        if f in M.PILOT_FILES: skip(item, action, name, "pilot file stays untouched", f, k); return False
        row = idx.get(f, {}).get(k)
        if row is None: skip(item, action, name, "row key not in panel", f, k); return False
        if k in nav: skip(item, action, name, "AJG1 nav row untouched", f, k); return False
        if (f, k) in changed and changed[(f, k)]["item"] != item:
            skip(item, action, name, f"row already changed by {changed[(f, k)]['item']} in this freeze; not changed twice", f, k); return False
        blob = " ".join((row.get(c) or "") for c in ("canonical_name", "raw_affiliation", "ror_name"))
        if (M.PROTECT_RX.search(blob) or re.search(r"1\s*decembrie\s*1918", blob, re.I)) and action != "SET_COUNTRY":
            skip(item, action, name, "protected organisation on row (11KBW/UNSW/INSEAD/1 Decembrie 1918)", f, k); return False
        fl = dict(fields)
        if FR.mostly_nonlatin(row.get("canonical_name") or row.get("raw_affiliation")) and "canonical_name" in fl and action != "DROP":
            fl.pop("canonical_name"); note += "; non-Latin printed name kept"
        if fl.get("ror_name"):
            for a_, b_ in FR.NEAR_MISS:
                o, n = row.get("ror_name") or row.get("canonical_name", ""), fl["ror_name"]
                if (re.search(a_, o, re.I) and re.search(b_, n, re.I) and not re.search(a_, n, re.I)) or (re.search(b_, o, re.I) and re.search(a_, n, re.I) and not re.search(b_, n, re.I)):
                    skip(item, action, name, f"near-miss pair ({o} -> {n})", f, k); return False
        ch = []
        for fld, val in fl.items():
            if fld in row and row[fld] != val: ch.append((fld, row[fld], val)); row[fld] = val
        if not ch: return False
        if (f, k) in changed: changed[(f, k)]["ch"].extend(ch)
        else: changed[(f, k)] = dict(item=item, action=action, name=name, ch=ch, note=note, editor_name=row.get("editor_name", ""))
        return True

    def keys_with_twins(keys):
        out = []
        for k in keys:
            out.append(k); tk = FR.twin_of(k)
            if tk and tk not in keys:
                a, b = idx.get(FR.file_of(k), {}).get(k), idx.get(FR.file_of(tk), {}).get(tk)
                if a is not None and b is not None and a.get("raw_affiliation") == b.get("raw_affiliation"): out.append(tk)
        return out

    def rename_fields(tname, rid, tcy):
        if rid:
            fl = rorf(rid); fl["canonical_name"] = tname or fl["ror_name"]
            return fl
        fl = dict(canonical_name=tname, ror_id="", ror_name="", lat="", lon="")
        if tcy: c = country_norm(tcy); fl.update(ror_country=c, continent=cont.get(c, ""))
        return fl

    # ---- A: FT50 #4634 ----
    a_rows = list(csv.DictReader(open(ANS / "a_campus_merge_77.csv", encoding="utf-8")))
    stats["A"]["keep_as_is"] = sum(1 for r in a_rows if r["editor_row_key"] != "editors_ft50_current_with_ror#4634")
    fl = rorf(R + "017zhmm22"); fl["raw_affiliation"] = "Xi'an Jiaotong University, China"
    ok = apply("A", "BOARD_RECHECK", "X. Zhao (JOM ERB)", K4634, fl,
               "JOM board https://www.jom-hub.com/team (live 2026-11-11): Editorial Review Board prints 'X. Zhao, Xi'an Jiaotong University, China' (the AE 'X. Zhao, China Europe Intl. Bus. School (CEIBS), China' is #4501)")
    stats["A"]["ft50_4634_fixed"] = int(ok)
    # ---- B ----
    for r in csv.DictReader(open(ANS / "b_drop_real_org_44.csv", encoding="utf-8")):
        if r["recommendation"] != "RENAME": stats["B"]["keep_as_is"] += 1; continue
        rid = r["target_ror"].strip()
        if rid:
            good, why = check_ror(rid, [r["target_name"]], r["target_country"], require_name=False)
            if not good: skip("B", "RENAME", r["target_name"], why + "; ROR left blank", FR.file_of(r["editor_row_key"]), r["editor_row_key"]); rid = ""
        fl = rename_fields(r["target_name"], rid, r["target_country"])
        if r["target_country"]: c = country_norm(r["target_country"]); fl.update(ror_country=c, continent=cont.get(c, fl.get("continent", "")))
        stats["B"]["applied" if apply("B", "RENAME", r["dropped_institution"], r["editor_row_key"], fl, f"answer (b): {r['note'][:160]}") else "not_applied"] += 1
    # ---- C ----
    for r in csv.DictReader(open(ANS / "c_ror_checks.csv", encoding="utf-8")):
        rid = r["recommended_ror"]; good, why = check_ror(rid, [r["recommended_name"]], r["recommended_country"])
        if not good: skip("C", "SET_ROR", r["recommended_name"], why, FR.file_of(r["editor_row_key"]), r["editor_row_key"]); stats["C"]["skipped"] += 1; continue
        fl = rename_fields(r["recommended_name"], rid, r["recommended_country"])
        stats["C"]["applied" if apply("C", "SET_ROR", r["printed_raw"], r["editor_row_key"], fl, f"answer (c): {r['evidence'][:160]}") else "not_applied"] += 1
    # ---- residual ----
    res = list(csv.DictReader(open(RESID, encoding="utf-8")))
    log(f"residual={len(res)} {dict(Counter(r['category'] for r in res))}")
    order = ["WRONG_ROR", "NEAR_DUPLICATE", "MISSING_ROR", "WRONG_COUNTRY", "NON_INSTITUTION", "MISSING_COUNTRY", "BIO_OR_MULTI_ORG", "HELD_COIN_FLIP", "NON_LATIN"]
    nd_sources = {r["institution"] for r in res if r["category"] == "NEAR_DUPLICATE"}
    nd_done_targets = set()
    for cat in order:
        for r in [x for x in res if x["category"] == cat]:
            inst = r["institution"]; keys = keys_with_twins(FR.keys_of(r["editor_row_keys"])); n = 0
            tname, rid, tcy = r["suggested_target"].strip(), r["suggested_ror"].strip(), r["suggested_country"].strip()
            if cat in ("HELD_COIN_FLIP", "NON_LATIN"): stats[cat]["left_as_printed"] += 1; continue
            if cat == "BIO_OR_MULTI_ORG":
                stats[cat]["left_as_printed"] += 1
                skip(cat, r["suggested_action"], inst, "no target in the residual file (REVIEW / two-place); left as printed"); continue
            if cat == "WRONG_ROR":
                old = r["ror"]; a_old, a_new = api(old), api(rid)
                if not a_old or a_old.get("_404") or a_old["status"] == "active" or rid not in a_old["succ"]:
                    skip(cat, "SUCCESSOR", inst, f"old record {old} does not name {rid} as successor (or is active)"); stats[cat]["skipped"] += 1; continue
                good, why = check_ror(rid, [], tcy, require_name=False)
                if not good: skip(cat, "SUCCESSOR", inst, why); stats[cat]["skipped"] += 1; continue
                fl = rorf(rid); fl["canonical_name"] = fl["ror_name"]
                tgt = [(f, k) for f in M.PUBLISH_FILES for k, row in idx[f].items() if row.get("ror_id") == old]
                for f, k in tgt:
                    n += apply(cat, "SUCCESSOR", inst, k, dict(fl), f"inactive ROR {old} -> successor {rid} (ROR API: old record lists successor; successor active)")
                for p in M.PILOT_FILES:
                    left = sum(1 for row in idx[p].values() if row.get("ror_id") == old)
                    if left: skip(cat, "SUCCESSOR", inst, f"{left} pilot rows keep {old} (pilots untouched)", p)
            elif cat == "NEAR_DUPLICATE":
                why = ND_SKIP.get(inst) or ND_SKIP.get(inst[:55])
                if r["confidence"] == "low": why = why or "low-confidence generic name -> one campus/other org; not merged"
                if not why and (rid in (MPG, CNRS) or fold(tname) in ("cnrs", "maxplancksociety")): why = "target is bare CNRS / Max Planck Society"
                if not why and FR.mostly_nonlatin(inst): why = "non-Latin printed name kept"
                if not why and inst in nd_done_targets: why = "target of another near-duplicate merge (cycle); not merged back"
                if not why and FR.near_miss(inst, tname): why = "near-miss pair"
                if not why and rid:
                    good, w = check_ror(rid, [tname], tcy, require_name=False)
                    if not good: why = w
                if why: skip(cat, "MERGE", inst, why); stats[cat]["skipped"] += 1; continue
                nd_done_targets.add(tname)
                fl = rename_fields(tname, rid, tcy)
                for k in keys:
                    row = idx.get(FR.file_of(k), {}).get(k)
                    if row is not None and row.get("ror_id") and rid and row["ror_id"] != rid:
                        skip(cat, "MERGE", inst, f"row already on {row['ror_id']}", FR.file_of(k), k); continue
                    if row is not None and row.get("ror_id") and not rid:
                        skip(cat, "MERGE", inst, f"row carries ROR {row['ror_id']}; name-only merge not applied", FR.file_of(k), k); continue
                    n += apply(cat, "MERGE", inst, k, fl, f"near-duplicate -> {tname} ({r['confidence']})")
            elif cat == "MISSING_ROR":
                if r["confidence"] == "low" and inst not in LOW_MR_OK:
                    skip(cat, "SET_ROR", inst, f"optional low-confidence generic match {tname} ({rid}) not clearly the printed organisation; left"); stats[cat]["skipped"] += 1; continue
                good, why = check_ror(rid, [inst, tname], tcy, require_name=True)
                if not good: skip(cat, "SET_ROR", inst, why + "; ROR left blank"); stats[cat]["skipped"] += 1; continue
                fl = rorf(rid); fl["canonical_name"] = fl["ror_name"]
                for k in keys:
                    row = idx.get(FR.file_of(k), {}).get(k)
                    if row is None: skip(cat, "SET_ROR", inst, "row key not in panel", FR.file_of(k), k); continue
                    if row.get("ror_id") and row["ror_id"] != rid: skip(cat, "SET_ROR", inst, f"row already on {row['ror_id']}", FR.file_of(k), k); continue
                    pc = FR.office_country(row.get("raw_affiliation", ""))
                    if pc and not FR.same_country(pc, fl["ror_country"]): skip(cat, "SET_ROR", inst, f"printed country {pc} != ROR country {fl['ror_country']}", FR.file_of(k), k); continue
                    n += apply(cat, "SET_ROR", inst, k, fl, f"exact ROR name/alias match ({r['confidence']}); ROR API active, country {fl['ror_country']}")
            elif cat == "WRONG_COUNTRY":
                if inst in WC_SKIP: skip(cat, "FIX_COUNTRY", inst, WC_SKIP[inst]); stats[cat]["skipped"] += 1; continue
                c = country_norm(tcy)
                for k in keys:
                    row = idx.get(FR.file_of(k), {}).get(k)
                    if row is None: continue
                    pc = FR.office_country(row.get("raw_affiliation", ""))
                    if inst in MULTI_OFFICE and pc and not FR.same_country(pc, c):
                        skip(cat, "FIX_COUNTRY", inst, f"multi-office organisation; printed office country {pc} kept (not HQ {c})", FR.file_of(k), k); continue
                    if row.get("ror_id") and row.get("ror_country") and not FR.same_country(row["ror_country"], c):
                        skip(cat, "FIX_COUNTRY", inst, f"row carries ROR {row['ror_id']} in {row['ror_country']}", FR.file_of(k), k); continue
                    n += apply(cat, "FIX_COUNTRY", inst, k, dict(ror_country=c, continent=cont.get(c, "")), f"country -> {c}")
            elif cat == "NON_INSTITUTION":
                if r["suggested_action"] == "RENAME":
                    if rid:
                        good, why = check_ror(rid, [tname], tcy, require_name=True)
                        if not good: skip(cat, "RENAME", inst, why + "; ROR left blank"); rid = ""
                    fl = rename_fields(tname, rid, tcy)
                    if not rid: fl = {k_: v_ for k_, v_ in fl.items() if k_ in ("canonical_name",) or (tcy and k_ in ("ror_country", "continent"))}
                    for k in keys: n += apply(cat, "RENAME", inst, k, fl, f"role/annotation removed -> {tname}")
                else:
                    for k in keys:
                        f = FR.file_of(k); row = idx.get(f, {}).get(k)
                        if row is None: skip(cat, "DROP", inst, "row key not in panel", f, k); continue
                        if (f, k) in changed: skip(cat, "DROP", inst, f"row already fixed by answer {changed[(f, k)]['item']} ({changed[(f, k)]['action']}) in this freeze; not dropped", f, k); continue
                        if row.get("ror_id"): skip(cat, "DROP", inst, f"row carries ROR {row['ror_id']}; not dropped", f, k); continue
                        own_w = sorted(set(w.casefold() for w in PR.ORGWORD.findall(row.get("raw_affiliation", ""))))
                        if own_w: skip(cat, "DROP", inst, f"printed raw itself names an organisation ({', '.join(own_w)}); not dropped - needs a decision", f, k); continue
                        extra_w = set(w.casefold() for w in PR.ORGWORD.findall(row.get("raw_affiliation", ""))) - set(w.casefold() for w in PR.ORGWORD.findall(inst))
                        if extra_w: skip(cat, "DROP", inst, f"printed raw names an organisation ({', '.join(sorted(extra_w))}); not dropped", f, k); continue
                        raw = row.get("raw_affiliation", "")
                        fl = dict(canonical_name="", raw_affiliation="", ror_id="", ror_name="", lat="", lon="")
                        if "ror_notes" in row:
                            tr = f"{METHOD}: user-approved DROP (Marks); printed text: {PR.red(raw or inst)}"
                            fl["ror_notes"] = f"{row['ror_notes']}; {tr}" if row.get("ror_notes") else tr
                        n += apply(cat, "DROP", inst, k, fl, "Marks-style DROP")
            elif cat == "MISSING_COUNTRY":
                for k in keys:
                    row = idx.get(FR.file_of(k), {}).get(k)
                    if row is None: continue
                    if row.get("ror_country"): continue
                    c = FR.office_country(row.get("raw_affiliation", ""))
                    src = "printed text"
                    if not c and row.get("ror_id") and catalog.get(row["ror_id"], {}).get("ror_country"): c, src = catalog[row["ror_id"]]["ror_country"], "ROR record"
                    if not c: skip(cat, "SET_COUNTRY", inst, "no country in printed text or ROR record; left blank", FR.file_of(k), k); continue
                    c = country_norm(c)
                    n += apply(cat, "SET_COUNTRY", inst, k, dict(ror_country=c, continent=cont.get(c, "")), f"country from {src}")
            stats[cat]["applied" if n else "not_applied"] += 1
            if not n and not any(s["institution"] == PR.red(inst) for s in skips[-(len(keys) + 2):]): skip(cat, r["suggested_action"], inst, "no-op: rows already at target / nothing to fill")
    log(f"stats {json.dumps({k: dict(v) for k, v in stats.items()})} changed={len(changed)}")
    for f, (hdr, rows) in data.items():
        if f in M.PILOT_FILES: continue
        M.write_csv(FREEZE / f, hdr, rows, M.detect_lineterminator(SRC / f))
    # ---- D: pilot scrub (the one approved pilot cell) ----
    pf, pk = PILOT_SCRUB
    prow = idx[pf][pk]; had_email = bool(PR.EM.search(prow.get("faculty_profile_url", "")))
    if had_email:
        prow["faculty_profile_url"] = ""
        M.write_csv(FREEZE / pf, data[pf][0], data[pf][1], M.detect_lineterminator(SRC / pf))
    stats["D"]["pilot_cell_blanked"] = int(had_email)
    # ---- long sync ----
    lh, lrows = FR.load(LONG, FREEZE)
    by = defaultdict(list)
    for p in lrows: by[p["editor_row_key"]].append(p)
    changelog, long_skip = [], []
    def lset(p, fld, val, k, op):
        if fld in p and p[fld] != val:
            changelog.append(dict(file=LONG, editor_row_key=k, editor_name=PR.red(p.get("editor_name", "")), item=op["item"], action=op["action"], field=fld, old=PR.red(p[fld]), new=PR.red(val), note="long sync")); p[fld] = val
    rank = lambda p: int(p["aff_rank"]) if str(p.get("aff_rank", "")).isdigit() else 99
    for (f, k), op in changed.items():
        r, o = idx[f][k], orig[f][k]; ps = by.get(k)
        if not ps: long_skip.append((k, "no long rows")); continue
        if r.get("raw_affiliation", "") != o.get("raw_affiliation", ""):
            tgt = ps if len(ps) == 1 else [p for p in ps if p["raw_aff_part"] == o["raw_affiliation"]]
            if not tgt: long_skip.append((k, "multi-part long row; raw_aff_part not synced"))
            for p in tgt:
                if op["action"] == "DROP":
                    tr = f"{METHOD}: user-approved DROP (Marks); printed text: {PR.red(o['raw_affiliation'])}"
                    lset(p, "ror_match_note", f"{p['ror_match_note']}; {tr}" if p["ror_match_note"] else tr, k, op); lset(p, "raw_aff_part", "", k, op)
                else: lset(p, "raw_aff_part", r["raw_affiliation"], k, op)
        if r.get("ror_id", "") != o.get("ror_id", ""):
            fl_ = [p for p in ps if p["is_panel_ror"] == "1"]
            if r.get("ror_id"):
                t = fl_[0] if fl_ else sorted(ps, key=rank)[0]
                lset(t, "ror_id", r["ror_id"], k, op); lset(t, "ror_name", r.get("ror_name", ""), k, op); lset(t, "is_panel_ror", "1", k, op)
            else:
                for x in fl_: lset(x, "ror_id", "", k, op); lset(x, "ror_name", "", k, op); lset(x, "is_panel_ror", "0", k, op)
        fl_ = [p for p in ps if p["is_panel_ror"] == "1"]
        prim = fl_[0] if fl_ else sorted(ps, key=rank)[0]
        lset(prim, "ror_country", r.get("ror_country", ""), k, op)
    # inactive ROR ids carried on non-primary long parts of changed rows are left (other_ror parts untouched)
    M.write_csv(FREEZE / LONG, lh, lrows, M.detect_lineterminator(SRC / LONG))
    M.update_working_panels()
    for (f, k), op in sorted(changed.items()):
        for fld, ov, nv in op["ch"]:
            changelog.append(dict(file=f, editor_row_key=k, editor_name=PR.red(op["editor_name"]), item=op["item"], action=op["action"], field=fld, old=PR.red(ov), new=PR.red(nv), note=PR.red(op["note"])))
    if had_email: changelog.append(dict(file=pf, editor_row_key=pk, editor_name="Helena Skyt Nielsen", item="D", action="PILOT_SCRUB", field="faculty_profile_url", old="[email removed]", new="", note="user-approved scrub; only pilot cell changed"))
    for c in changelog:
        for kk in ("old", "new", "note", "editor_name"): assert not PR.has_contact(c[kk] or ""), "contact in changelog"
    with open(FREEZE / CHANGELOG_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "editor_row_key", "editor_name", "item", "action", "field", "old", "new", "note"]); w.writeheader(); w.writerows(changelog)
    with open(FREEZE / SKIPS_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["item", "action", "institution", "file", "editor_row_key", "reason"]); w.writeheader(); w.writerows(skips)
    v = FR.verify(changed, orig, set(all_rors) | set(extra), nav)
    # pilot: only the approved cell may differ
    pb = list(csv.DictReader(open(SRC / pf, encoding="utf-8", newline=""))); pn = list(csv.DictReader(open(FREEZE / pf, encoding="utf-8", newline="")))
    pdiff = [(y["editor_row_key"], c) for x, y in zip(pb, pn) for c in x if x[c] != y[c]]
    other_pilot = [p for p in M.PILOT_FILES if p != pf]
    v["pilot_cells_changed"] = pdiff
    v["pilot_ok"] = pdiff == [(pk, "faculty_profile_url")] and all(open(SRC / p, "rb").read() == open(FREEZE / p, "rb").read() for p in other_pilot) \
        and open(SRC / pf, "rb").readline() == open(FREEZE / pf, "rb").readline() and M.detect_lineterminator(SRC / pf) == M.detect_lineterminator(FREEZE / pf) and len(pb) == len(pn)
    v["pilot_email_left"] = sum(1 for y in pn if PR.EM.search(y.get("faculty_profile_url", "")))
    v["long_skipped"] = long_skip
    vocab_b = {r.get("ror_country", "") for f in M.PUBLISH_FILES for r in csv.DictReader(open(SRC / f, encoding="utf-8"))}
    v["new_country_values"] = sorted({r.get("ror_country", "") for (f, k), op in changed.items() for r in [idx[f][k]]} - vocab_b)
    unexp = [u for u in v["panel_unexpected"] if not (len(u) == 3 and u[1] == pk)]
    v["ok"] = (v["row_counts_unchanged"] and v["long_rows"] == 269545 and v["ajg1_file_rows"] == 12326 and v["ajg1_nav"] == 10 and not v["ajg1_nav_touched"]
               and v["ajg2_rows"] == 5462 and v["ft50_rows"] == 10049 and v["ft50_ror_rows"] == 10049 and not v["header_or_eol_changes"] and not unexp
               and v["panel_unexpected_n"] - (len(v["panel_unexpected"]) - len(unexp)) == 0 and not v["raw_changed_outside_drop_or_paauwe"] and not v["long_unexpected"]
               and v["pilot_ok"] and v["pilot_email_left"] == 0 and not v["invented_ror"] and not v["protected_rows_institution_changed"] and not v["contact_n"]
               and v["long_contact_rows"][1] <= v["long_contact_rows"][0] and not v["panel_long_desync_changed_n"] and v["panel_long_desync_full_table"] <= v["base_desync_full_table"]
               and not v["nonlatin_lost"] and not v["near_miss"] and v["keep_11kbw"] and v["unsw"] and v["insead_fr_sg"] and v["working_panels_identical"])
    log(f"verify(ok incl. pilot scrub)={v['ok']}")
    dirdiff, eb, ea = directory_diff(changed)
    counts = {"before": PR.build("pfr_before", eb), "after": PR.build("pfr_after", ea)}
    pub = Counter(); ftm = Counter()
    for (f, k), op in changed.items(): (ftm if f == FT else pub)[f"{op['item']}:{op['action']}"] += 1
    summ = dict(stats={k: dict(x) for k, x in stats.items()}, rows_publish=dict(pub), rows_ft50_current_mirror=dict(ftm), skips=len(skips),
                skip_reasons=dict(Counter(f"{s['item']}:{s['action']}: {s['reason'][:60]}" for s in skips).most_common(50)),
                changelog_lines=len(changelog), directory_diff_lines=len(dirdiff), new_rors_api_verified=extra)
    json.dump(dict(summary=summ, verify=v, counts=counts), open(FREEZE / f"_summary_{STAMP}.json", "w"), indent=1, ensure_ascii=False, default=str)
    print(json.dumps(dict(summary=summ, counts=counts), indent=1, ensure_ascii=False, default=str)[:8000])
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
