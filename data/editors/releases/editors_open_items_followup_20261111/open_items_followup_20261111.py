#!/usr/bin/env python3
"""Follow-up freeze editors_open_items_followup_20261111 on editors_open_items_fix_20261111
(live via PR #56, 89aa2f09). Four user-approved items only, relayed by Econ-Journal-Web.
1 Shenhar abdc_b#16107: revert Rutgers; Diamond Leadership Institute, Israel, no ROR.
2 Bates abdc_b#39063: do not drop; primary The University of Sydney 0384j8v12; keep printed text;
  keep UNSW 03r8z3t63 as second affiliation (already present in long table + other_ror_ids).
  Do not alter the UNSW institution master entry.
3 ft50 #4634 both rows: also clear faculty_match_method and faculty_match_confidence. Do not touch #4501.
4 Former employers: Nielsen #42676 blank institution, keep US country; GM ajg1#4303 keep 05addee68 if already set;
  SEARCA #15559 blank institution and country.
No raw edits. Pilots byte-identical. No publish."""
from __future__ import annotations
import csv, json, re, sys, glob, importlib.util, unicodedata
from collections import Counter, defaultdict
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("fr1", HERE / "full_review_fix_20261111.py")
FR = importlib.util.module_from_spec(spec); spec.loader.exec_module(FR)
PR, WI, T, M = FR.PR, FR.WI, FR.T, FR.M
ROOT = M.ROOT; STAMP = "20261111"; METHOD = "open_items_followup_20261111"
FREEZE_ID = "editors_open_items_followup_20261111"; BASE_ID = "editors_open_items_fix_20261111"
SRC = ROOT / f"releases/{BASE_ID}"; FREEZE = ROOT / f"releases/{FREEZE_ID}"
for mod in (M, T, WI, PR, FR):
    for a, v in (("SRC_FREEZE", SRC), ("SRC", SRC), ("FREEZE", FREEZE)):
        setattr(mod, a, v)
M.LOGF = ROOT / f"abs_ajg/logs/open_items_followup_{STAMP}.log"
FR.DIRDIFF_NAME = f"OPEN_ITEMS_FOLLOWUP_directory_diff_{STAMP}.csv"
log = M.log
LONG, FT, FTR = WI.LONG, WI.FT, WI.FTR
CHANGELOG_NAME = f"OPEN_ITEMS_FOLLOWUP_changes_{STAMP}.csv"
SKIPS_NAME = f"OPEN_ITEMS_FOLLOWUP_skipped_{STAMP}.csv"
API = Path("/tmp/fr/api")
R = "https://ror.org/"
SYDNEY, UNSW, GM, RUTGERS = R + "0384j8v12", R + "03r8z3t63", R + "05addee68", R + "05vt9qd57"
K_SHENHAR = "editors_abdc_b_current#16107"
K_BATES = "editors_abdc_b_current#39063"
K4634 = ("editors_ft50_current_with_ror#4634", "editors_ft50_current#4634")
K4501 = ("editors_ft50_current_with_ror#4501", "editors_ft50_current#4501")
K_NIELSEN = "editors_abdc_a_current#42676"
K_GM = "editors_abs_ajg_gap_ajg1_current#4303"
K_SEARCA = "editors_abdc_c_current#15559"
PROFILE_FIELDS = ["faculty_match_method", "faculty_match_confidence"]
# faculty_* are not institution fields; allowed on the two #4634 keys only
# ror_id_aff_rank / ror_notes allowed on Bates so the primary rank is recorded


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


def fold(s):
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().casefold())


def country_norm(c):
    c = FR.norm_country(c)
    return {"United States of America": "United States", "The Netherlands": "Netherlands",
            "Czech Republic": "Czechia", "Viet Nam": "Vietnam"}.get(c, c)


def main():
    if M.LOGF.exists(): M.LOGF.unlink()
    log(f"start {FREEZE_ID}")
    catalog, all_rors, name_to_ids = M.build_twin_catalog(SRC)
    cont = T.continent_map()
    for c, v in FR.EXTRA_CONT.items(): cont.setdefault(c, v)
    cont.setdefault("Israel", "Asia")
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

    def apply(item, action, name, k, fields, note, protect_ok=False):
        f = FR.file_of(k)
        if f in M.PILOT_FILES:
            skip(item, action, name, "pilot file stays untouched", f, k); return False
        row = idx.get(f, {}).get(k)
        if row is None:
            skip(item, action, name, "row key not in panel", f, k); return False
        if k in nav:
            skip(item, action, name, "AJG1 nav row untouched", f, k); return False
        blob = " ".join((row.get(c) or "") for c in ("canonical_name", "raw_affiliation", "ror_name"))
        if (M.PROTECT_RX.search(blob) or re.search(r"1\s*decembrie\s*1918", blob, re.I)) and not protect_ok:
            skip(item, action, name, "protected organisation on row (11KBW/UNSW/INSEAD/1 Decembrie 1918)", f, k); return False
        fl = dict(fields)
        ch = []
        for fld, val in fl.items():
            if fld in row and row[fld] != val:
                ch.append((fld, row[fld], val)); row[fld] = val
        if not ch: return False
        if (f, k) in changed:
            changed[(f, k)]["ch"].extend(ch); changed[(f, k)]["note"] += " | " + note
        else:
            changed[(f, k)] = dict(item=item, action=action, name=name, ch=ch, note=note, editor_name=row.get("editor_name", ""))
        return True

    # ---- 1 Shenhar ----
    row = idx[FR.file_of(K_SHENHAR)][K_SHENHAR]
    stats["1"]["before"] = f"{row.get('canonical_name')} | {row.get('ror_id')} | {row.get('ror_country')}"
    fl = dict(canonical_name="Diamond Leadership Institute", ror_id="", ror_name="", lat="", lon="",
              ror_country="Israel", continent=cont.get("Israel", "Asia"))
    ok = apply("1", "REVERT_RENAME", "Diamond Leadership Institute", K_SHENHAR, fl,
               "revert Rutgers 05vt9qd57; (Ret.) is a former employer; current role is CEO, Diamond Leadership Institute, Israel; no ROR invented")
    stats["1"]["applied"] = int(ok)
    stats["1"]["institution"] = "new: Diamond Leadership Institute (Israel, blank ROR); no existing panel row used that name"

    # ---- 2 Bates ----
    # Inspected: long table already has aff_rank 2 = UNSW Australia / 03r8z3t63 / is_panel_ror=0.
    # Panel already has affiliation_count=2 and other_ror_ids=UNSW. Update in place; no new row.
    brow = idx[FR.file_of(K_BATES)][K_BATES]
    stats["2"]["before"] = f"{brow.get('canonical_name')} | {brow.get('ror_id') or '(blank)'} | {brow.get('ror_country') or '(blank)'} | affiliation_count={brow.get('affiliation_count')} other_ror_ids={brow.get('other_ror_ids')}"
    good, why = check_ror(SYDNEY, ["The University of Sydney", "University of Sydney", "Sydney University", "USYD"], "Australia")
    if not good:
        skip("2", "SET_ROR", "The University of Sydney", why, FR.file_of(K_BATES), K_BATES)
        stats["2"]["skipped"] += 1
    else:
        # confirm UNSW record is untouched and still active (we attach the existing id only)
        ugood, uwhy = check_ror(UNSW, ["UNSW Sydney", "UNSW", "University of New South Wales"], "Australia")
        if not ugood:
            skip("2", "SET_ROR", "UNSW Sydney", "second-org ROR check failed: " + uwhy, FR.file_of(K_BATES), K_BATES)
            stats["2"]["skipped"] += 1
        elif (brow.get("other_ror_ids") or "") != UNSW or (brow.get("affiliation_count") or "") != "2":
            skip("2", "SET_ROR", "The University of Sydney",
                 f"expected existing second affiliation UNSW in other_ror_ids and affiliation_count=2; found other_ror_ids={brow.get('other_ror_ids')} count={brow.get('affiliation_count')}",
                 FR.file_of(K_BATES), K_BATES)
            stats["2"]["skipped"] += 1
        else:
            fl = rorf(SYDNEY)
            fl["canonical_name"] = fl["ror_name"]  # catalog: The University of Sydney
            fl["ror_id_aff_rank"] = "1"
            note = ("primary -> The University of Sydney 0384j8v12 (Adjunct Professor, Sydney Law, already documented in ror_notes); "
                    "UNSW 03r8z3t63 already on long aff_rank 2 and panel other_ror_ids — updated in place, no new row; "
                    "printed raw affiliation left unchanged; UNSW institution master entry not modified")
            # protect_ok: raw names UNSW, but this edit does not rename/merge/alter the UNSW record
            ok = apply("2", "SET_PRIMARY", "The University of Sydney", K_BATES, fl, note, protect_ok=True)
            stats["2"]["applied"] = int(ok)
            stats["2"]["new_row_added"] = 0
            stats["2"]["second_aff"] = "already present: long aff_rank 2 raw_aff_part 'UNSW Australia', ROR 03r8z3t63, aff_role unknown; left in place"
            if brow.get("raw_affiliation") != orig[FR.file_of(K_BATES)][K_BATES]["raw_affiliation"]:
                raise SystemExit("refusing: Bates raw affiliation changed")

    # ---- 3 #4634 match fields ----
    for k in K4634:
        row = idx[FR.file_of(k)][k]
        if (row.get("raw_affiliation") or "").find("Jiaotong") < 0:
            skip("3", "CLEAR_MATCH", "X. Zhao", "institution is not Xi'an Jiaotong; not cleared", FR.file_of(k), k)
            stats["3"]["skipped"] += 1
            continue
        fl = {c: "" for c in PROFILE_FIELDS}
        ok = apply("3", "CLEAR_MATCH", "X. Zhao (JOM ERB)", k, fl,
                   "faculty URL and person key were cleared in the previous freeze; match method/confidence cleared to match every other FT50 row with a blank profile URL")
        stats["3"]["applied"] += int(ok)
    for k in K4501:
        row = idx[FR.file_of(k)][k]
        if row.get("faculty_profile_url") or row.get("faculty_person_key") or row.get("faculty_match_method"):
            stats["3"]["4501_left_untouched"] = 1

    # ---- 4 former employers ----
    # Nielsen
    row = idx[FR.file_of(K_NIELSEN)][K_NIELSEN]
    stats["4_nielsen"]["before"] = f"{row.get('canonical_name')} | {row.get('ror_id')} | {row.get('ror_country')}"
    fl = dict(canonical_name="", ror_id="", ror_name="", lat="", lon="",
              ror_country="United States", continent=cont.get("United States", "North America"))
    ok = apply("4", "BLANK_INSTITUTION", "Nielsen (former employer)", K_NIELSEN, fl,
               "printed 'Consultant (former Chief Research Officer, Nielsen), USA': Nielsen is a former employer; no institution; country United States kept; raw unchanged")
    stats["4_nielsen"]["applied"] = int(ok)

    # GM
    row = idx[FR.file_of(K_GM)][K_GM]
    stats["4_gm"]["before"] = f"{row.get('canonical_name')} | {row.get('ror_id')} | {row.get('ror_country')}"
    good, why = check_ror(GM, ["General Motors (United States)", "GM", "General Motors"], "United States")
    if not good:
        skip("4", "SET_ROR", "General Motors", why, FR.file_of(K_GM), K_GM); stats["4_gm"]["skipped"] += 1
    elif row.get("ror_id") == GM:
        stats["4_gm"]["already_at_target"] = 1
        skip("4", "KEEP", "General Motors (United States)", f"already on {GM} General Motors (United States), United States; left unchanged (printed 'GM (retired), USA' — GM is the only organisation printed)", FR.file_of(K_GM), K_GM)
    else:
        fl = rorf(GM); fl["canonical_name"] = fl["ror_name"]
        ok = apply("4", "SET_ROR", "General Motors (United States)", K_GM, fl, "GM is the only organisation printed; emeritus-style keep")
        stats["4_gm"]["applied"] = int(ok)

    # SEARCA
    row = idx[FR.file_of(K_SEARCA)][K_SEARCA]
    stats["4_searca"]["before"] = f"{row.get('canonical_name')} | {row.get('ror_id')} | {row.get('ror_country')}"
    fl = dict(canonical_name="", ror_id="", ror_name="", lat="", lon="", ror_country="", continent="")
    ok = apply("4", "BLANK_INSTITUTION", "SEARCA (former employer)", K_SEARCA, fl,
               "printed 'Independent consultant (formerly SEARCA Knowledge Management Department Head)': former employer; no institution or country printed; raw unchanged. The other SEARCA row #15558 is untouched.")
    stats["4_searca"]["applied"] = int(ok)

    log(f"stats {json.dumps({k: dict(v) for k, v in stats.items()})} changed={len(changed)}")
    for f, (hdr, rows) in data.items():
        if f in M.PILOT_FILES: continue
        M.write_csv(FREEZE / f, hdr, rows, M.detect_lineterminator(SRC / f))

    # long sync
    lh, lrows = FR.load(LONG, FREEZE)
    by = defaultdict(list)
    for p in lrows: by[p["editor_row_key"]].append(p)
    changelog, long_skip = [], []

    def lset(p, fld, val, k, op):
        if fld in p and p[fld] != val:
            changelog.append(dict(file=LONG, editor_row_key=k, editor_name=PR.red(p.get("editor_name", "")),
                                  item=op["item"], action=op["action"], field=fld, old=PR.red(p[fld]), new=PR.red(val), note="long sync"))
            p[fld] = val

    rank = lambda p: int(p["aff_rank"]) if str(p.get("aff_rank", "")).isdigit() else 99
    bates_long_before = [dict(p) for p in by.get(K_BATES, [])]
    for (f, k), op in changed.items():
        r, o = idx[f][k], orig[f][k]; ps = by.get(k)
        if not ps: long_skip.append((k, "no long rows")); continue
        if r.get("raw_affiliation", "") != o.get("raw_affiliation", ""):
            long_skip.append((k, "raw changed — unexpected, not synced"))
            continue
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

    # Bates: confirm long rank 2 is still the original UNSW row (byte-equal on affiliation fields)
    bates_after = by.get(K_BATES, [])
    stats["2"]["long_parts_after"] = len(bates_after)
    stats["2"]["long_parts_before"] = len(bates_long_before)
    unsw_part = [p for p in bates_after if p.get("aff_rank") == "2"]
    if not unsw_part or unsw_part[0].get("ror_id") != UNSW or unsw_part[0].get("raw_aff_part") != "UNSW Australia":
        raise SystemExit(f"Bates long aff_rank 2 no longer the UNSW row: {unsw_part}")

    M.write_csv(FREEZE / LONG, lh, lrows, M.detect_lineterminator(SRC / LONG))
    M.update_working_panels()

    for (f, k), op in sorted(changed.items()):
        for fld, ov, nv in op["ch"]:
            changelog.append(dict(file=f, editor_row_key=k, editor_name=PR.red(op["editor_name"]),
                                  item=op["item"], action=op["action"], field=fld, old=PR.red(ov), new=PR.red(nv), note=PR.red(op["note"])))
    for c in changelog:
        for kk in ("old", "new", "note", "editor_name"):
            assert not PR.has_contact(c[kk] or ""), "contact in changelog"
    with open(FREEZE / CHANGELOG_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "editor_row_key", "editor_name", "item", "action", "field", "old", "new", "note"])
        w.writeheader(); w.writerows(changelog)
    with open(FREEZE / SKIPS_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["item", "action", "institution", "file", "editor_row_key", "reason"])
        w.writeheader(); w.writerows(skips)

    v = FR.verify(changed, orig, set(all_rors) | set(extra) | {SYDNEY, UNSW, GM}, nav)
    v["long_skipped"] = long_skip
    # allow faculty match fields on #4634; ror_id_aff_rank (and ror_notes if touched) on Bates
    allowed_extra = {
        "editors_ft50_current#4634": set(PROFILE_FIELDS),
        "editors_ft50_current_with_ror#4634": set(PROFILE_FIELDS),
        K_BATES: {"ror_id_aff_rank", "ror_notes"},
    }
    normal_fields = {"raw_affiliation", "canonical_name", "ror_id", "ror_name", "ror_country", "continent",
                     "lat", "lon", "ror_notes", "editor_name", "editor_name_raw"}
    unexp = []
    for u in v["panel_unexpected"]:
        if len(u) == 3 and set(u[2]) - normal_fields <= allowed_extra.get(u[1], set()):
            continue
        unexp.append(u)
    v["panel_unexpected_filtered"] = unexp
    # UNSW master audit: every panel row whose ror_id is UNSW is byte-equal to base
    unsw_changed = []
    for f in M.PUBLISH_FILES:
        b = {r["editor_row_key"]: r for r in FR.load(f, SRC)[1]}
        n = {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]}
        for k, r in n.items():
            if r.get("ror_id") == UNSW and r != b[k]:
                unsw_changed.append(k)
    v["unsw_master_rows_changed"] = unsw_changed
    # raw unchanged
    raw_changed = [k for (f, k), op in changed.items() if any(fld == "raw_affiliation" for fld, _, _ in op["ch"])]
    v["raw_changed_this_freeze"] = raw_changed
    # long row count
    v["long_rows_freeze"] = len(lrows)
    # Bates raw names UNSW, so verify flags the row as a protected institution change.
    # That is expected: we only retarget THIS editor's primary to Sydney and leave the UNSW master entry alone
    # (unsw_master_rows_changed audit). Filter Bates out of the protect-institution fail.
    prot = [k for k in v["protected_rows_institution_changed"] if k != K_BATES]
    v["protected_rows_institution_changed_filtered"] = prot
    v["ok"] = (v["row_counts_unchanged"] and v["long_rows"] == 269545 and v["ajg1_file_rows"] == 12326 and v["ajg1_nav"] == 10 and not v["ajg1_nav_touched"]
               and v["ajg2_rows"] == 5462 and v["ft50_rows"] == 10049 and v["ft50_ror_rows"] == 10049 and not v["header_or_eol_changes"] and not unexp
               and not v["raw_changed_outside_drop_or_paauwe"] and not raw_changed and not v["long_unexpected"]
               and all(v["pilot_files_byte_identical"].values()) and not v["invented_ror"] and not prot and not v["contact_n"]
               and v["long_contact_rows"][1] <= v["long_contact_rows"][0] and not v["panel_long_desync_changed_n"] and v["panel_long_desync_full_table"] <= v["base_desync_full_table"]
               and not v["nonlatin_lost"] and not v["near_miss"] and v["keep_11kbw"] and v["unsw"] and v["insead_fr_sg"] and v["working_panels_identical"]
               and not unsw_changed)
    log(f"verify(ok incl. item-3 match fields and Bates in-place)= {v['ok']}")
    dirdiff, eb, ea = directory_diff(changed)
    counts = {"before": PR.build("oif_before", eb), "after": PR.build("oif_after", ea)}
    pub = Counter(); ftm = Counter()
    for (f, k), op in changed.items():
        (ftm if f == FT else pub)[f"{op['item']}:{op['action']}"] += 1
    summ = dict(stats={k: dict(x) for k, x in stats.items()}, rows_publish=dict(pub), rows_ft50_current_mirror=dict(ftm),
                skips=len(skips), changelog_lines=len(changelog), directory_diff_lines=len(dirdiff),
                new_rors_api_verified=extra, new_row_added=stats["2"].get("new_row_added", "n/a"))
    json.dump(dict(summary=summ, verify=v, counts=counts), open(FREEZE / f"_summary_{STAMP}.json", "w"), indent=1, ensure_ascii=False, default=str)
    print(json.dumps(dict(summary=summ, counts=counts, verify_ok=v["ok"],
                          desync=(v["panel_long_desync_full_table"], v["base_desync_full_table"]),
                          unexp=unexp, unsw_changed=unsw_changed), indent=1, ensure_ascii=False, default=str)[:8000])
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
            extra_f = PROFILE_FIELDS if k in K4634 else []
            for fld in list(FR.FIELDS) + extra_f + (FR.NAME_FIELDS if k in FR.PAAUWE else []):
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
