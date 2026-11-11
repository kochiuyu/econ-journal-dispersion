#!/usr/bin/env python3
"""Freeze editors_coinflip_holds_fix_20261111 on editors_nielsen_searca_drop_20261111
(live via PR #58, 83f6a1a7). User-approved coin-flip hold placements from
/workspace/institutions_coinflip_holds_20261111.csv (187 rows), relayed by Econ-Journal-Web.
Re-verify every ROR in the API. Do not apply NIT Hamirpur 01nc8zs04 (API country Bangladesh).
Saint Mary's already on Halifax 010zh7098: skip any move off Halifax. No raw edits. Pilots untouched.
No publish."""
from __future__ import annotations
import csv, json, re, sys, glob, importlib.util, unicodedata
from collections import Counter, defaultdict
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("fr1", HERE / "full_review_fix_20261111.py")
FR = importlib.util.module_from_spec(spec); spec.loader.exec_module(FR)
PR, WI, T, M = FR.PR, FR.WI, FR.T, FR.M
ROOT = M.ROOT; STAMP = "20261111"; METHOD = "coinflip_holds_fix_20261111"
FREEZE_ID = "editors_coinflip_holds_fix_20261111"; BASE_ID = "editors_nielsen_searca_drop_20261111"
SRC = ROOT / f"releases/{BASE_ID}"; FREEZE = ROOT / f"releases/{FREEZE_ID}"
for mod in (M, T, WI, PR, FR):
    for a, v in (("SRC_FREEZE", SRC), ("SRC", SRC), ("FREEZE", FREEZE)):
        setattr(mod, a, v)
M.LOGF = ROOT / f"abs_ajg/logs/coinflip_holds_fix_{STAMP}.log"
FR.DIRDIFF_NAME = f"COINFLIP_HOLDS_directory_diff_{STAMP}.csv"
log = M.log
LONG, FT, FTR = WI.LONG, WI.FT, WI.FTR
CHANGELOG_NAME = f"COINFLIP_HOLDS_changes_{STAMP}.csv"
SKIPS_NAME = f"COINFLIP_HOLDS_skipped_{STAMP}.csv"
SRC_CSV = Path("/workspace/institutions_coinflip_holds_20261111.csv")
API = Path("/tmp/fr/api")
R = "https://ror.org/"
HALIFAX = R + "010zh7098"
HAMIRPUR = R + "01nc8zs04"
UIUC, UIC = R + "047426m28", R + "02mpq6x41"
# new to panels (API-verified 2026-11-11)
EXTRA = {
    R + "0028kf729": ("Concordia University Irvine", "United States", "North America", "33.66946", "-117.82311"),
}
UNTOUCHED = (
    "editors_abdc_c_current#15558",  # SEARCA kept
    "editors_abdc_c_current#15559",  # SEARCA dropped
    "editors_abdc_a_current#42676",  # Nielsen dropped
    "editors_abdc_b_current#16107",  # Diamond Leadership Institute
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


def approved_target(rec):
    """Return (name, ror, country, override_reason_or_empty) from the user-approved specifics."""
    cur, editor = rec["current institution"], rec["editor"]
    if cur.startswith("University of Illinois"):
        chicago = editor == "Linda Hagen" or editor == "Thomas (Yew Sing) Lee"
        if chicago:
            return "University of Illinois Chicago", UIC, "United States", ""
        return "University of Illinois Urbana-Champaign", UIUC, "United States", ""
    if cur == "Madison University":
        return "James Madison University", R + "028pmsz77", "United States", ""
    if cur == "University of New Zealand":
        return "Massey University", R + "052czxv31", "New Zealand", ""
    if cur == "American University, UAE":
        return "American University in the Emirates", R + "056c6h780", "United Arab Emirates", ""
    if cur in ("University of Naples", "University of Naples, Naples", "University of Napoli"):
        return "University of Naples Federico II", R + "05290cv24", "Italy", ""
    if "Pacifico" in cur or "Pacífico" in cur:
        return "Universidad del Pacífico", R + "05mmg7t28", "Peru", ""
    if editor == "Bruce Hanson" and cur.startswith("Concordia"):
        return "Concordia University Irvine", R + "0028kf729", "United States", ""
    if editor == "Lawrence Kryzanowski":
        return "Concordia University", R + "0420zvk78", "Canada", ""
    return rec["target_name"].strip(), rec["target_ror"].strip(), rec["target_country"].strip(), ""


def main():
    if M.LOGF.exists(): M.LOGF.unlink()
    log(f"start {FREEZE_ID}")
    rows = list(csv.DictReader(open(SRC_CSV, encoding="utf-8")))
    log(f"file rows={len(rows)} editors={len({r['editor_row_key'] for r in rows})} rors={len({r['target_ror'] for r in rows})}")
    catalog, all_rors, name_to_ids = M.build_twin_catalog(SRC)
    cont = T.continent_map()
    for c, v in FR.EXTRA_CONT.items(): cont.setdefault(c, v)
    for c, v in {"Jamaica": "North America", "Vietnam": "Asia", "Peru": "South America",
                 "United Arab Emirates": "Asia", "New Zealand": "Oceania", "Russia": "Europe"}.items():
        cont.setdefault(c, v)
    dir_ajg1 = glob.glob("/workspace/edj-web/data/editors/*/releases/current/editors_abs_ajg_gap_ajg1_current.csv")[0]
    dir_keys = {r["editor_row_key"] for r in csv.DictReader(open(dir_ajg1, encoding="utf-8-sig"))}
    M.copy_freeze_base()
    data = {f: FR.load(f, FREEZE) for f in M.PANEL_FILES}
    idx = {f: {r["editor_row_key"]: r for r in rows_} for f, (_h, rows_) in data.items()}
    orig = {f: {k: dict(r) for k, r in d.items()} for f, d in idx.items()}
    nav = {r["editor_row_key"] for r in data["editors_abs_ajg_gap_ajg1_current.csv"][1] if r["editor_row_key"] not in dir_keys}
    skips, changed, extra, stats = [], {}, dict(EXTRA), defaultdict(Counter)

    def skip(item, action, name, reason, f="", k=""):
        skips.append(dict(item=item, action=action, institution=PR.red(name), file=f, editor_row_key=k, reason=PR.red(reason)))

    def rorf(rid):
        if rid in EXTRA:
            n, c, co, la, lo = EXTRA[rid]
            return dict(ror_id=rid, ror_name=n, ror_country=c, continent=co, lat=la, lon=lo)
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

    diffs = 0
    for rec in rows:
        k = rec["editor_row_key"]
        f = FR.file_of(k)
        item = rec["current institution"]
        tname, tro, tcy, _ = approved_target(rec)
        file_t, file_r, file_c = rec["target_name"].strip(), rec["target_ror"].strip(), rec["target_country"].strip()
        if (tname, tro, country_norm(tcy)) != (file_t, file_r, country_norm(file_c)):
            skip("APPROVED_VS_FILE", "PLACE", item,
                 f"file said {file_t} {file_r} {file_c}; approved mapping applied: {tname} {tro} {tcy}", f, k)
            diffs += 1
        stats["rows"]["file"] += 1
        stats["by_target"][f"{tname} {tro[-9:] if tro else ''}"] += 1

        if tro == HAMIRPUR or "01nc8zs04" in tro:
            skip(item, "PLACE", tname, "NIT Hamirpur 01nc8zs04: API country is Bangladesh; not applied (user instruction)", f, k)
            stats["skipped"]["nit_hamirpur"] += 1; continue

        row = idx.get(f, {}).get(k)
        if row is None:
            skip(item, "PLACE", tname, "row key not in panel", f, k); stats["skipped"]["missing"] += 1; continue
        if f in M.PILOT_FILES:
            skip(item, "PLACE", tname, "pilot file stays untouched", f, k); stats["skipped"]["pilot"] += 1; continue

        # Saint Mary's Halifax must not be moved off 010zh7098
        blob = " ".join((row.get(c) or "") for c in ("canonical_name", "raw_affiliation", "ror_name"))
        if row.get("ror_id") == HALIFAX and tro != HALIFAX:
            skip(item, "PLACE", tname, "Saint Mary's is already on Halifax 010zh7098; not moved", f, k)
            stats["skipped"]["saint_marys"] += 1; continue
        if re.search(r"saint\s*mary'?s university", blob, re.I) and tro != HALIFAX and row.get("ror_id") in ("", HALIFAX):
            skip(item, "PLACE", tname, "Saint Mary's University (Halifax) left on 010zh7098", f, k)
            stats["skipped"]["saint_marys"] += 1; continue

        if not tro:
            skip(item, "PLACE", tname, "no target ROR; left as printed", f, k); stats["skipped"]["no_ror"] += 1; continue
        good, why = check_ror(tro, [tname], tcy)
        if not good:
            skip(item, "PLACE", tname, why + "; ROR left unchanged", f, k); stats["skipped"]["ror_check"] += 1; continue

        fl = rorf(tro)
        if tcy:
            c = country_norm(tcy)
            fl["ror_country"] = c
            fl["continent"] = cont.get(c, fl.get("continent", ""))
        if "canonical_name" in row:
            fl["canonical_name"] = tname
        note = f"coinflip hold placement -> {tname} {tro} ({tcy}); {rec.get('evidence','')[:160]}"
        if apply("PLACE", "SET_CAMPUS", item, k, fl, note):
            stats["applied"]["rows"] += 1
            # group tags
            tag = tname
            if tro == UIUC: tag = "Illinois UIUC"
            elif tro == UIC: tag = "Illinois Chicago"
            elif tro.endswith("028pmsz77"): tag = "James Madison"
            elif tro.endswith("052czxv31"): tag = "Massey"
            elif tro.endswith("056c6h780"): tag = "AUE"
            elif tro.endswith("05290cv24"): tag = "Naples Federico II"
            elif tro.endswith("05mmg7t28"): tag = "Pacifico Lima"
            elif tro.endswith("0028kf729"): tag = "Concordia Irvine (Hanson)"
            elif tro.endswith("0420zvk78") and rec["editor"] == "Lawrence Kryzanowski": tag = "Concordia Montreal (Kryzanowski)"
            stats["applied_group"][tag] += 1
        else:
            stats["already_at_target"]["rows"] += 1

    stats["approved_vs_file"]["differences"] = diffs
    log(f"stats {json.dumps({k: dict(v) for k, v in stats.items()})} changed={len(changed)}")

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

    v = FR.verify(changed, orig, set(all_rors) | set(extra) | set(EXTRA), nav)
    v["long_skipped"] = long_skip
    # follow-up rows must stay untouched unless they were in this file
    file_keys = {r["editor_row_key"] for r in rows}
    broke = []
    for k in UNTOUCHED:
        if k in file_keys: continue
        f = FR.file_of(k)
        b = {r["editor_row_key"]: r for r in FR.load(f, SRC)[1]}
        n = {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]}
        if b.get(k) != n.get(k): broke.append(k)
    v["followup_rows_changed"] = broke
    raw_changed = [k for (f, k), op in changed.items() if any(fld == "raw_affiliation" for fld, _, _ in op["ch"])]
    v["raw_changed_this_freeze"] = raw_changed
    v["ok"] = (v["row_counts_unchanged"] and v["long_rows"] == 269545 and v["ajg1_file_rows"] == 12326 and v["ajg1_nav"] == 10 and not v["ajg1_nav_touched"]
               and v["ajg2_rows"] == 5462 and v["ft50_rows"] == 10049 and v["ft50_ror_rows"] == 10049 and not v["header_or_eol_changes"]
               and not v["panel_unexpected"] and not v["raw_changed_outside_drop_or_paauwe"] and not raw_changed and not v["long_unexpected"]
               and all(v["pilot_files_byte_identical"].values()) and not v["invented_ror"] and not v["protected_rows_institution_changed"] and not v["contact_n"]
               and v["long_contact_rows"][1] <= v["long_contact_rows"][0] and not v["panel_long_desync_changed_n"] and v["panel_long_desync_full_table"] <= v["base_desync_full_table"]
               and not v["nonlatin_lost"] and not v["near_miss"] and v["keep_11kbw"] and v["unsw"] and v["insead_fr_sg"] and v["working_panels_identical"]
               and not broke)
    log(f"verify ok={v['ok']}")
    dirdiff, eb, ea = directory_diff(changed)
    counts = {"before": PR.build("cfh_before", eb), "after": PR.build("cfh_after", ea)}
    pub, ftm = Counter(), Counter()
    for (f, k), op in changed.items():
        (ftm if f == FT else pub)[f"{op['action']}"] += 1
    summ = dict(stats={k: dict(x) for k, x in stats.items()}, rows_publish=dict(pub), rows_ft50_current_mirror=dict(ftm),
                skips=len(skips), changelog_lines=len(changelog), directory_diff_lines=len(dirdiff),
                new_rors_api_verified={rid: (EXTRA[rid] if rid in EXTRA else extra[rid]) for rid in set(EXTRA) | set(extra) if rid not in catalog or rid in extra})
    json.dump(dict(summary=summ, verify=v, counts=counts), open(FREEZE / f"_summary_{STAMP}.json", "w"), indent=1, ensure_ascii=False, default=str)
    print(json.dumps(dict(summary=summ, counts=counts, verify_ok=v["ok"],
                          desync=(v["panel_long_desync_full_table"], v["base_desync_full_table"]),
                          unexpected=v["panel_unexpected"][:8], invented=v["invented_ror"],
                          followup=broke), indent=1, ensure_ascii=False, default=str)[:10000])
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
