#!/usr/bin/env python3
"""Freeze editors_school_unit_rematch_20261111 on editors_coinflip_holds_fix_20261111
(live via PR #59, 887b6a36). User-approved school/faculty unit rematches from
/workspace/collector_school_units_20261111/school_unit_rematch_20261111.csv
(606 appointments, 505 editors, 94 targets), relayed by Econ-Journal-Web.

Institutions table follows ROR: a school/faculty/centre with its own ROR stays
its own institution; unmatched mastheads rematch to the parent. Leave
raw_affiliation as printed. Re-verify every target ROR in the API. Skip held
campuses and two-place rows, plus file rows whose target contradicts the campus
rule (NUBS China -> UK Nottingham; Newcastle Business School Australia ->
Northumbria UK). Same-raw FT50 with_ror twins are synced and logged. No raw
edits. Pilots untouched. No publish.
"""
from __future__ import annotations
import csv, json, re, sys, glob, shutil, importlib.util, unicodedata
from collections import Counter, defaultdict
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("fr1", HERE / "full_review_fix_20261111.py")
FR = importlib.util.module_from_spec(spec); spec.loader.exec_module(FR)
PR, WI, T, M = FR.PR, FR.WI, FR.T, FR.M
ROOT = M.ROOT; STAMP = "20261111"; METHOD = "school_unit_rematch_20261111"
FREEZE_ID = "editors_school_unit_rematch_20261111"; BASE_ID = "editors_coinflip_holds_fix_20261111"
SRC = ROOT / f"releases/{BASE_ID}"; FREEZE = ROOT / f"releases/{FREEZE_ID}"
for mod in (M, T, WI, PR, FR):
    for a, v in (("SRC_FREEZE", SRC), ("SRC", SRC), ("FREEZE", FREEZE)):
        setattr(mod, a, v)
M.LOGF = ROOT / f"abs_ajg/logs/school_unit_rematch_{STAMP}.log"
FR.DIRDIFF_NAME = f"SCHOOL_UNIT_REMATCH_directory_diff_{STAMP}.csv"
log = M.log
LONG, FT, FTR = WI.LONG, WI.FT, WI.FTR
CHANGELOG_NAME = f"SCHOOL_UNIT_REMATCH_changes_{STAMP}.csv"
SKIPS_NAME = f"SCHOOL_UNIT_REMATCH_skipped_{STAMP}.csv"
SRC_CSV = Path("/workspace/collector_school_units_20261111/school_unit_rematch_20261111.csv")
API = Path("/tmp/fr/api")
R = "https://ror.org/"
NOTTINGHAM_UK = R + "01ee9ar58"
NINGBO = R + "03y4dt428"
NORTHUMBRIA = R + "049e6bc10"
UNTOUCHED = (
    "editors_abdc_c_current#15558",  # SEARCA kept
    "editors_abdc_c_current#15559",  # SEARCA dropped
    "editors_abdc_a_current#42676",  # Nielsen dropped
    "editors_abdc_b_current#16107",  # Diamond Leadership Institute
)
# Held strings checked against printed raw / current institution / panel
# canonical + raw only — never against evidence text.
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


def fold(s):
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().casefold())


def api(rid):
    p = API / f"{rid.replace(R, '')}.json"
    if not p.exists(): return None
    d = json.load(open(p))
    if d.get("_404"): return {"_404": True}
    loc = d["locations"][0]["geonames_details"]
    return dict(status=d["status"], names=[n["value"] for n in d["names"]],
                country=loc.get("country_name", ""), continent=loc.get("continent_name", ""),
                lat=str(loc.get("lat", "")), lon=str(loc.get("lng", "")),
                name=next((n["value"] for n in d["names"] if "ror_display" in n.get("types", [])), d["names"][0]["value"]))


def country_norm(c):
    c = FR.norm_country(c)
    return {"United States of America": "United States", "The Netherlands": "Netherlands",
            "Viet Nam": "Vietnam", "Russian Federation": "Russia"}.get(c, c)


def hold_hit(blob):
    m = HOLD_RX.search(blob or "")
    return m.group(0) if m else ""


def campus_conflict(rec, row):
    """Skip file rows whose target contradicts the approved campus rule."""
    blob = " ".join((
        rec.get("current institution") or "",
        rec.get("printed raw") or "",
        row.get("canonical_name") or "",
        row.get("raw_affiliation") or "",
    ))
    tro = rec["target_ror"].strip()
    if re.search(r"nottingham university business school|\bNUBS\b", blob, re.I):
        if re.search(r"\b(?:China|Ningbo|Zhejiang)\b", blob, re.I) and tro == NOTTINGHAM_UK:
            return ("Nottingham University Business School China/Ningbo/Zhejiang must rematch "
                    "to University of Nottingham Ningbo China 03y4dt428, not UK Nottingham "
                    "01ee9ar58; left as printed (blank is better than the wrong campus)")
    if re.search(r"newcastle business school", blob, re.I):
        au = bool(re.search(r"\bAustralia\b", blob, re.I)) or (row.get("ror_country") or "") == "Australia"
        if au and tro == NORTHUMBRIA:
            return ("Newcastle Business School Australia is the University of Newcastle "
                    "(Australia), not Northumbria University UK; left as printed "
                    "(blank is better than the wrong country)")
    return ""


def special_group(tname, tro, rec):
    if tro.endswith("047ybhc09"): return "Cass/Bayes -> City St George's"
    if tro.endswith("02jjdwm75"): return "Instituto de Empresa / IE Business School -> IE University"
    if tro.endswith("033qfx261"): return "EADA -> EADA Business School"
    if tro.endswith("04q0nd296"): return "EM Strasbourg -> EM Strasbourg Business School"
    if tro.endswith("04mv5gg87"): return "IMD Lausanne -> IMD"
    if tro.endswith("03y4dt428"): return "NUBS China -> Nottingham Ningbo"
    if tro.endswith("05apxxy63"): return "KAIST"
    if tro.endswith("01q8b6q23"): return "LUISS"
    return tname


def main():
    if M.LOGF.exists(): M.LOGF.unlink()
    log(f"start {FREEZE_ID}")
    rows = list(csv.DictReader(open(SRC_CSV, encoding="utf-8")))
    log(f"file rows={len(rows)} editors={len({r['editor'] for r in rows})} keys={len({r['editor_row_key'] for r in rows})} rors={len({r['target_ror'] for r in rows})}")
    catalog, all_rors, name_to_ids = M.build_twin_catalog(SRC)
    cont = T.continent_map()
    for c, v in FR.EXTRA_CONT.items(): cont.setdefault(c, v)
    for c, v in {"Jamaica": "North America", "Vietnam": "Asia", "Peru": "South America",
                 "United Arab Emirates": "Asia", "New Zealand": "Oceania", "Russia": "Europe",
                 "Lithuania": "Europe", "Saudi Arabia": "Asia", "Hong Kong": "Asia",
                 "Mexico": "North America"}.items():
        cont.setdefault(c, v)
    dir_ajg1 = glob.glob("/workspace/edj-web/data/editors/*/releases/current/editors_abs_ajg_gap_ajg1_current.csv")[0]
    dir_keys = {r["editor_row_key"] for r in csv.DictReader(open(dir_ajg1, encoding="utf-8-sig"))}
    M.copy_freeze_base()
    data = {f: FR.load(f, FREEZE) for f in M.PANEL_FILES}
    idx = {f: {r["editor_row_key"]: r for r in rows_} for f, (_h, rows_) in data.items()}
    orig = {f: {k: dict(r) for k, r in d.items()} for f, d in idx.items()}
    nav = {r["editor_row_key"] for r in data["editors_abs_ajg_gap_ajg1_current.csv"][1] if r["editor_row_key"] not in dir_keys}
    skips, changed, extra, stats = [], {}, {}, defaultdict(Counter)

    # Snapshot held rows on the base (must stay byte-identical).
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

    def rorf(rid):
        if rid in catalog:
            tw = catalog[rid]
            return dict(ror_id=rid, ror_name=tw["ror_name"], ror_country=tw["ror_country"],
                        continent=tw["continent"], lat=tw["lat"], lon=tw["lon"])
        a = api(rid); c = country_norm(a["country"])
        extra[rid] = dict(name=a["name"], country=c)
        return dict(ror_id=rid, ror_name=a["name"], ror_country=c,
                    continent=cont.get(c) or a["continent"], lat=a["lat"], lon=a["lon"])

    def check_ror(rid, names, country):
        a = api(rid)
        if a is None: return False, f"{rid} not fetched from ROR API"
        if a.get("_404"): return False, f"{rid} not in ROR API (404)"
        if a["status"] != "active": return False, f"{rid} is {a['status']} in ROR API"
        if M.is_system_ror_name(a["name"]): return False, f"{rid} is a university-system ROR"
        folded = {fold(n) for n in a["names"]}
        if names and not (folded & {fold(x) for x in names if x}):
            return False, f"{rid} names {a['names'][:4]} do not match {names}"
        if country and not FR.same_country(country_norm(a["country"]), country_norm(country)):
            return False, f"{rid} country {a['country']} != {country}"
        return True, ""

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
        fl = dict(fields)
        if FR.mostly_nonlatin(row.get("canonical_name") or row.get("raw_affiliation")) and "canonical_name" in fl:
            fl.pop("canonical_name"); note += "; non-Latin printed name kept"
        if fl.get("ror_name"):
            for a_, b_ in FR.NEAR_MISS:
                o, n_ = row.get("ror_name") or row.get("canonical_name") or "", fl["ror_name"]
                if ((re.search(a_, o, re.I) and re.search(b_, n_, re.I) and not re.search(a_, n_, re.I)) or
                    (re.search(b_, o, re.I) and re.search(a_, n_, re.I) and not re.search(b_, n_, re.I))):
                    skip(item, action, name, f"near-miss pair ({o} -> {n_})", f, k); return False
        ch = []
        for fld, val in fl.items():
            if fld in row and row[fld] != val:
                ch.append((fld, row[fld], val)); row[fld] = val
        if not ch: return False
        changed[(f, k)] = dict(item=item, action=action, name=name, ch=ch, note=note, editor_name=row.get("editor_name", ""))
        return True

    file_keys = {r["editor_row_key"] for r in rows}
    for rec in rows:
        k = rec["editor_row_key"]
        f = FR.file_of(k)
        item = rec["current institution"]
        tname, tro, tcy = rec["target_name"].strip(), rec["target_ror"].strip(), rec["target_country"].strip()
        stats["rows"]["file"] += 1
        stats["by_target"][f"{tname} {tro[-9:] if tro else ''}"] += 1

        row = idx.get(f, {}).get(k)
        if row is None:
            skip(item, "REMATCH", tname, "row key not in panel", f, k); stats["skipped"]["missing"] += 1; continue
        if f in M.PILOT_FILES:
            skip(item, "REMATCH", tname, "pilot file stays untouched", f, k); stats["skipped"]["pilot"] += 1; continue

        printed = " ".join((rec.get("current institution") or "", rec.get("printed raw") or "",
                            row.get("canonical_name") or "", row.get("raw_affiliation") or ""))
        hh = hold_hit(printed)
        if hh:
            skip(item, "REMATCH", tname, f"held string in printed masthead ({hh!r}); left as printed", f, k)
            stats["skipped"]["held"] += 1; continue

        why = campus_conflict(rec, row)
        if why:
            skip(item, "REMATCH", tname, why, f, k); stats["skipped"]["campus_conflict"] += 1; continue

        if not tro:
            skip(item, "REMATCH", tname, "no target ROR; left as printed", f, k); stats["skipped"]["no_ror"] += 1; continue
        good, why = check_ror(tro, [tname], tcy)
        if not good:
            skip(item, "REMATCH", tname, why + "; left as printed", f, k); stats["skipped"]["ror_check"] += 1; continue
        if tro not in catalog:
            # All 94 were already on the published current panels; if one is not, skip rather than invent a Directory row from API alone without the usual new-ROR path being expected.
            skip(item, "REMATCH", tname, f"{tro} is not already on the published current panels; left as printed", f, k)
            stats["skipped"]["not_on_panels"] += 1; continue

        fl = rorf(tro)
        if tcy:
            c = country_norm(tcy)
            fl["ror_country"] = c
            fl["continent"] = cont.get(c, fl.get("continent", ""))
        if "canonical_name" in row:
            fl["canonical_name"] = tname
        note = f"school-unit rematch -> {tname} {tro} ({tcy})"
        if apply("REMATCH", "SET_PARENT", item, k, fl, note):
            stats["applied"]["file"] += 1
            stats["applied_group"][special_group(tname, tro, rec)] += 1
        else:
            if (f, k) not in changed:
                # apply returned False because no field changed, or a guard skip was logged
                if not any(s["editor_row_key"] == k for s in skips):
                    stats["already_at_target"]["file"] += 1

    # Same-raw FT50 with_ror twins not listed in the file.
    for rec in rows:
        k = rec["editor_row_key"]
        if not (k.startswith("editors_ft50_current#") and "with_ror" not in k):
            continue
        tk = "editors_ft50_current_with_ror#" + k.split("#", 1)[1]
        if tk in file_keys:
            continue
        f, tf = FR.file_of(k), FR.file_of(tk)
        slim, twin = idx.get(f, {}).get(k), idx.get(tf, {}).get(tk)
        tname, tro, tcy = rec["target_name"].strip(), rec["target_ror"].strip(), rec["target_country"].strip()
        item = rec["current institution"]
        if slim is None or twin is None:
            skip(item, "REMATCH", tname, "FT50 twin missing on panel", tf, tk)
            stats["skipped"]["ft50_twin_missing"] += 1; continue
        if slim.get("raw_affiliation") != twin.get("raw_affiliation"):
            skip(item, "REMATCH", tname, "FT50 twin printed raw differs; twin left as printed", tf, tk)
            stats["skipped"]["ft50_twin_raw_diff"] += 1; continue
        if (f, k) not in changed:
            # slim was skipped or already at target — do not force the twin
            stats["twin"]["slim_not_applied"] += 1; continue
        fl = rorf(tro)
        if tcy:
            c = country_norm(tcy)
            fl["ror_country"] = c
            fl["continent"] = cont.get(c, fl.get("continent", ""))
        if "canonical_name" in twin:
            fl["canonical_name"] = tname
        note = f"FT50 same-raw twin of {k}; school-unit rematch -> {tname} {tro} ({tcy})"
        if apply("REMATCH", "SET_PARENT_TWIN", item, tk, fl, note):
            stats["applied"]["ft50_twin"] += 1
        else:
            if not any(s["editor_row_key"] == tk for s in skips):
                stats["already_at_target"]["ft50_twin"] += 1

    log(f"stats {json.dumps({k: dict(v) for k, v in stats.items()})} changed={len(changed)} skips={len(skips)}")

    for f, (hdr, rows_) in data.items():
        if f in M.PILOT_FILES: continue
        M.write_csv(FREEZE / f, hdr, rows_, M.detect_lineterminator(SRC / f))

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

    rank = lambda p: int(p["aff_rank"]) if str(p.get("aff_rank", "")).isdigit() else 99
    for (f, k), op in changed.items():
        r, o = idx[f][k], orig[f][k]; ps = by.get(k)
        if not ps: long_skip.append((k, "no long rows")); continue
        if r.get("raw_affiliation", "") != o.get("raw_affiliation", ""):
            long_skip.append((k, "raw changed — unexpected, not synced")); continue
        if r.get("ror_id", "") != o.get("ror_id", ""):
            fl_ = [p for p in ps if p["is_panel_ror"] == "1"]
            if r.get("ror_id"):
                t = fl_[0] if fl_ else sorted(ps, key=rank)[0]
                lset(t, "ror_id", r["ror_id"], k, op)
                lset(t, "ror_name", r.get("ror_name", ""), k, op)
                lset(t, "is_panel_ror", "1", k, op)
            else:
                for x in fl_ or ps[:1]:
                    lset(x, "ror_id", "", k, op); lset(x, "ror_name", "", k, op); lset(x, "is_panel_ror", "0", k, op)
        fl_ = [p for p in ps if p["is_panel_ror"] == "1"]
        prim = fl_[0] if fl_ else sorted(ps, key=rank)[0]
        lset(prim, "ror_country", r.get("ror_country", ""), k, op)

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

    v = FR.verify(changed, orig, set(all_rors) | set(extra), nav)
    v["long_skipped"] = long_skip
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
    v["raw_changed_this_freeze"] = raw_changed
    v["ok"] = (v["row_counts_unchanged"] and v["long_rows"] == 269545 and v["ajg1_file_rows"] == 12326 and v["ajg1_nav"] == 10 and not v["ajg1_nav_touched"]
               and v["ajg2_rows"] == 5462 and v["ft50_rows"] == 10049 and v["ft50_ror_rows"] == 10049 and not v["header_or_eol_changes"]
               and not v["panel_unexpected"] and not v["raw_changed_outside_drop_or_paauwe"] and not raw_changed and not v["long_unexpected"]
               and all(v["pilot_files_byte_identical"].values()) and not v["invented_ror"] and not v["protected_rows_institution_changed"] and not v["contact_n"]
               and v["long_contact_rows"][1] <= v["long_contact_rows"][0] and not v["panel_long_desync_changed_n"] and v["panel_long_desync_full_table"] <= v["base_desync_full_table"]
               and not v["nonlatin_lost"] and not v["near_miss"] and v["keep_11kbw"] and v["unsw"] and v["insead_fr_sg"] and v["working_panels_identical"]
               and not broke and not held_broke)
    log(f"verify ok={v['ok']} held_broke={held_broke} followup={broke}")
    dirdiff, eb, ea = directory_diff(changed)
    counts = {"before": PR.build("su_before", eb), "after": PR.build("su_after", ea)}
    pub, ftm = Counter(), Counter()
    for (f, k), op in changed.items():
        (ftm if f == FT else pub)[f"{op['action']}"] += 1
    summ = dict(stats={k: dict(x) for k, x in stats.items()}, rows_publish=dict(pub), rows_ft50_current_mirror=dict(ftm),
                skips=len(skips), changelog_lines=len(changelog), directory_diff_lines=len(dirdiff),
                new_rors_api_verified={rid: extra[rid] for rid in extra if rid not in catalog},
                held_rows_on_base=len(held_keys), held_rows_changed=held_broke)
    json.dump(dict(summary=summ, verify=v, counts=counts), open(FREEZE / f"_summary_{STAMP}.json", "w"), indent=1, ensure_ascii=False, default=str)
    shutil.copy2(Path(__file__), FREEZE / Path(__file__).name)
    print(json.dumps(dict(summary=summ, counts=counts, verify_ok=v["ok"],
                          desync=(v["panel_long_desync_full_table"], v["base_desync_full_table"]),
                          unexpected=v["panel_unexpected"][:8], invented=v["invented_ror"],
                          followup=broke, held_broke=held_broke, long_skip=long_skip[:8]),
                     indent=1, ensure_ascii=False, default=str)[:12000])
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
