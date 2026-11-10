#!/usr/bin/env python3
"""Open-items freeze editors_open_items_fix_20261111 on editors_post_fullreview_fix_20261111 (input /workspace/collector_open_items_20261111.csv). Helper code inherited from the post-full-review freeze 2026-11-11 (Asia/Taipei): editors_post_fullreview_fix_20261111.
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
ROOT = M.ROOT; STAMP = "20261111"; METHOD = "open_items_fix_20261111"
FREEZE_ID = "editors_open_items_fix_20261111"; BASE_ID = "editors_post_fullreview_fix_20261111"
SRC = ROOT / f"releases/{BASE_ID}"; FREEZE = ROOT / f"releases/{FREEZE_ID}"
for mod in (M, T, WI, PR, FR):
    for a, v in (("SRC_FREEZE", SRC), ("SRC", SRC), ("FREEZE", FREEZE)):
        setattr(mod, a, v)
M.LOGF = ROOT / f"abs_ajg/logs/open_items_fix_{STAMP}.log"
FR.DIRDIFF_NAME = f"OPEN_ITEMS_directory_diff_{STAMP}.csv"
log = M.log
LONG, FT, FTR = WI.LONG, WI.FT, WI.FTR
CHANGELOG_NAME = f"OPEN_ITEMS_changes_{STAMP}.csv"; SKIPS_NAME = f"OPEN_ITEMS_skipped_{STAMP}.csv"
ANS = Path("/workspace/collector_answers_20261111")
RESID = Path("/workspace/institutions_post_fullreview_residual_20261111.csv")
API = Path("/tmp/fr/api")
R = "https://ror.org/"
PILOT_SCRUB = ("editors_abdc_a_current_with_profile_pilot.csv", "editors_abdc_a_current_with_profile_pilot#15779")
K4634 = "editors_ft50_current#4634"
OI = Path("/workspace/collector_open_items_20261111.csv")
PROFILE_FIELDS = ["faculty_profile_url", "faculty_person_key"]
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
        # open-items freeze: catalog RORs also get the name + country check
        GEN = {"university", "of", "the", "and", "for", "school", "business", "institute", "college", "center", "centre", "de", "la", "national", "state", "studies", "sciences", "social", "economic", "economics", "&", "-", "co", "co."}
        tok = lambda x: {w for w in re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode().casefold()) if w not in GEN and len(w) > 2}
        full = {fold(n) for n in a["names"]} & ({fold(re.sub(r"\s*\([^)]*\)\s*$", "", x)) for x in names if x} | {fold(x) for x in names if x})
        part = any(tok(x) and tok(x) <= set().union(*[tok(n) for n in a["names"]]) for x in names if x)
        if require_name and not full and not part:
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


    APPROVED = {  # user-approved specifics (relayed by Web 2026-11-11): key -> (target_ror or None, country or None)
        "editors_abdc_c_current#27627": (R + "02c9qn167", "China"), "editors_abdc_c_current#27484": (R + "03wnrsb51", "China"),
        "editors_abdc_c_current#26986": (R + "04vx9dd09", "Denmark"), "editors_abdc_a_current#10607": (R + "03gvhpa76", "Mexico"),
        "editors_abdc_a_star_current#21570": (R + "05vt9qd57", "United States"), "editors_abdc_b_current#33133": (None, "Ireland"),
        "editors_abdc_c_current#20171": (R + "00nx0vn86", "Macao"), "editors_abs_ajg_gap_prio43_current#1194": (None, "Mexico"),
        "editors_abs_ajg_gap_ajg1_current#4547": (R + "05bqa2z43", "United States"), "editors_abdc_c_current#22898": (R + "052vhkx86", "Nigeria"),
        "editors_abdc_b_current#33364": (R + "01bc76c69", "Germany"), "editors_abdc_c_current#18900": (R + "047988g19", "Ukraine"),
        "editors_abdc_c_current#27684": (R + "04ewct822", "China"), "editors_abdc_c_current#27472": (R + "021e5n641", "United States"),
        "editors_abs_ajg_gap_ajg2_current#1791": (R + "056am2717", "Canada"), "editors_abdc_c_current#18771": (R + "01e6qks80", "Canada"),
        "editors_abdc_c_current#18673": (None, "Australia"), "editors_abdc_b_current#9281": (R + "042bbge36", "United States"),
        "editors_abdc_a_current#36407": (R + "05309tf52", "Canada"),
    }
    COUNTRY_OVERRIDE_OK = {"editors_abdc_a_current#36407"}   # Niagara: US ROR record, printed Ontario campus -> country Canada (approved)
    HOLD_KEYS = {"editors_abdc_a_current#26625", "editors_abdc_a_current#33759", "editors_abdc_c_current#26820", "editors_abdc_b_current#24781"}
    KEEP_NO_ROR = {"editors_abdc_c_current#20888", "editors_abdc_b_current#16662", "editors_abdc_a_current#30025", "editors_abs_ajg_gap_ajg1_current#11934"}
    rows_oi = list(csv.DictReader(open(OI, encoding="utf-8")))
    log(f"open items={len(rows_oi)} {dict(Counter(r['item_no'] for r in rows_oi))}")
    diffs = []
    seen = set()
    for r in rows_oi:
        k, rec, it = r["editor_row_key"], r["recommendation"], "item" + r["item_no"]
        tname, rid, tcy = r["target_name"].strip(), r["target_ror"].strip(), r["target_country"].strip()
        if k in APPROVED:
            seen.add(k); arid, acy = APPROVED[k]
            if arid is not None and arid != rid: diffs.append((k, f"file ror {rid} != approved {arid}; approved applied")); rid = arid
            if acy and not FR.same_country(country_norm(acy), country_norm(tcy)): diffs.append((k, f"file country {tcy} != approved {acy}; approved applied")); tcy = acy
        f = FR.file_of(k)
        stats[it]["rows"] += 1
        if rec in ("CLOSED",): stats[it]["closed_no_change"] += 1; continue
        if rec == "HOLD" or k in HOLD_KEYS: stats[it]["hold_left_as_printed"] += 1; skip(it, rec, r["institution_now"], "hold: left as printed (approved)", f, k); continue
        if rec == "REVIEW":
            stats[it]["review_no_change"] += 1
            skip(it, rec, r["institution_now"], "file recommends REVIEW with no target (former-employer ROR: Nielsen; GM ajg1#4303 and SEARCA abdc_c#15559 named in evidence) - left unchanged", f, k); continue
        if rec == "SPLIT_WHERE_EVIDENCED" and k != "editors_abdc_b_current#1581":
            stats[it]["split_not_evidenced_kept"] += 1; continue
        keys = keys_with_twins([k])
        if rec in ("KEEP_AS_PRINTED", "KEEP_DISTINCT", "KEEP_AS_IS", "KEEP"):
            row = idx.get(f, {}).get(k)
            c = country_norm(tcy) if tcy else ""
            if row is not None and c and not FR.same_country(row.get("ror_country", ""), c) and not row.get("ror_id"):
                n = sum(apply(it, "SET_COUNTRY", r["institution_now"], kk, dict(ror_country=c, continent=cont.get(c, "")), f"kept as printed; country per open-items file ({r['evidence'][:120]})") for kk in keys)
                stats[it]["kept_country_set" if n else "kept_unchanged"] += 1
            else: stats[it]["kept_unchanged"] += 1
            continue
        if rec == "CLEAR_PROFILE_URL":
            n = sum(apply(it, "CLEAR_PROFILE_URL", r["institution_now"], kk, {x: "" for x in PROFILE_FIELDS}, "CEIBS profile URL + person key belong to X. Zhao #4501 (match was by initials); cleared") for kk in [k])
            stats[it]["applied" if n else "not_applied"] += 1; continue
        if rec == "FIX_COUNTRY" or rec == "SET_COUNTRY":
            c = country_norm(tcy)
            n = sum(apply(it, rec, r["institution_now"], kk, dict(ror_country=c, continent=cont.get(c, "")), f"country -> {c} ({r['evidence'][:120]})") for kk in keys)
            stats[it]["applied" if n else "not_applied"] += 1; continue
        if rec == "DROP":
            row = idx.get(f, {}).get(k)
            if row is None or row.get("ror_id"): skip(it, "DROP", r["institution_now"], "row missing or carries a ROR; not dropped", f, k); stats[it]["skipped"] += 1; continue
            raw = row.get("raw_affiliation", "")
            fl = dict(canonical_name="", raw_affiliation="", ror_id="", ror_name="", lat="", lon="")
            if tcy: c = country_norm(tcy); fl.update(ror_country=c, continent=cont.get(c, ""))
            if "ror_notes" in row:
                tr = f"{METHOD}: user-approved DROP (Marks); printed text: {PR.red(raw)}"
                fl["ror_notes"] = f"{row['ror_notes']}; {tr}" if row.get("ror_notes") else tr
            n = apply(it, "DROP", r["institution_now"], k, fl, "Marks-style DROP (approved)")
            stats[it]["applied" if n else "not_applied"] += 1; continue
        # RENAME / MERGE / SET_ROR / SPLIT / SPLIT_WHERE_EVIDENCED
        if k in KEEP_NO_ROR: stats[it]["kept_no_ror"] += 1; continue
        if rid:
            good, why = check_ror(rid, [tname], tcy if k not in COUNTRY_OVERRIDE_OK else "", require_name=True)
            if not good: skip(it, rec, r["institution_now"], why + "; not applied", f, k); stats[it]["skipped_ror_check"] += 1; continue
        fl = rename_fields(tname, rid, tcy)
        if tcy: c = country_norm(tcy); fl.update(ror_country=c, continent=cont.get(c, fl.get("continent", "")))
        note = f"open item {r['item_no']} {rec} -> {tname}" + (f" {rid}" if rid else " (no ROR)") + (f"; country {tcy} (approved override of ROR country)" if k in COUNTRY_OVERRIDE_OK else "")
        n = 0
        for kk in keys:
            row = idx.get(FR.file_of(kk), {}).get(kk)
            if row is not None and not rid and row.get("ror_id"):
                skip(it, rec, r["institution_now"], f"row carries ROR {row['ror_id']} and target has none; not renamed", FR.file_of(kk), kk); continue
            n += apply(it, rec, r["institution_now"], kk, dict(fl), note)
        stats[it]["applied" if n else "not_applied"] += 1
    for k in APPROVED:
        if k not in seen: diffs.append((k, "approved key not in open-items file; not applied"))
    for k, d_ in diffs: skip("APPROVED_VS_FILE", "", "", d_, FR.file_of(k), k)
    stats["approved_vs_file_differences"]["n"] = len(diffs)
    log(f"stats {json.dumps({k: dict(v) for k, v in stats.items()})} changed={len(changed)}")
    for f, (hdr, rows) in data.items():
        if f in M.PILOT_FILES: continue
        M.write_csv(FREEZE / f, hdr, rows, M.detect_lineterminator(SRC / f))
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
    for c in changelog:
        for kk in ("old", "new", "note", "editor_name"): assert not PR.has_contact(c[kk] or ""), "contact in changelog"
    with open(FREEZE / CHANGELOG_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "editor_row_key", "editor_name", "item", "action", "field", "old", "new", "note"]); w.writeheader(); w.writerows(changelog)
    with open(FREEZE / SKIPS_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["item", "action", "institution", "file", "editor_row_key", "reason"]); w.writeheader(); w.writerows(skips)
    v = FR.verify(changed, orig, set(all_rors) | set(extra), nav)
    v["long_skipped"] = long_skip
    vocab_b = {r.get("ror_country", "") for f in M.PUBLISH_FILES for r in csv.DictReader(open(SRC / f, encoding="utf-8"))}
    v["new_country_values"] = sorted({r.get("ror_country", "") for (f, k), op in changed.items() for r in [idx[f][k]]} - vocab_b)
    # item 8: faculty_profile_url / faculty_person_key cleared on the two #4634 rows are the only extra allowed fields
    allowed8 = {"editors_ft50_current_with_ror#4634", "editors_ft50_current#4634"}
    unexp = [u for u in v["panel_unexpected"] if not (len(u) == 3 and u[1] in allowed8 and set(u[2]) <= set(PROFILE_FIELDS))]
    n_allowed = len(v["panel_unexpected"]) - len(unexp)
    v["item8_profile_cells_cleared_rows"] = n_allowed
    v["ok"] = (v["row_counts_unchanged"] and v["long_rows"] == 269545 and v["ajg1_file_rows"] == 12326 and v["ajg1_nav"] == 10 and not v["ajg1_nav_touched"]
               and v["ajg2_rows"] == 5462 and v["ft50_rows"] == 10049 and v["ft50_ror_rows"] == 10049 and not v["header_or_eol_changes"] and not unexp
               and v["panel_unexpected_n"] - n_allowed == 0 and not v["raw_changed_outside_drop_or_paauwe"] and not v["long_unexpected"]
               and all(v["pilot_files_byte_identical"].values()) and not v["invented_ror"] and not v["protected_rows_institution_changed"] and not v["contact_n"]
               and v["long_contact_rows"][1] <= v["long_contact_rows"][0] and not v["panel_long_desync_changed_n"] and v["panel_long_desync_full_table"] <= v["base_desync_full_table"]
               and not v["nonlatin_lost"] and not v["near_miss"] and v["keep_11kbw"] and v["unsw"] and v["insead_fr_sg"] and v["working_panels_identical"])
    log(f"verify(ok incl. item-8 profile cells)={v['ok']}")
    dirdiff, eb, ea = directory_diff(changed)
    counts = {"before": PR.build("oi_before", eb), "after": PR.build("oi_after", ea)}
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
            for fld in FR.FIELDS + ["faculty_person_key"] + (FR.NAME_FIELDS if k in FR.PAAUWE else []):
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
