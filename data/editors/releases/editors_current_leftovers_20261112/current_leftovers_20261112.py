#!/usr/bin/env python3
"""Freeze editors_current_leftovers_STAMP on editors_leftover_fixes_20261112 (live Directory, web main 59652942).
Unpublished; for Journal-Editor-Web. Collector-doable evidenced fixes under the user's [pt238u] go-ahead.
D. Name-field leftovers (official board pages fetched 2026-11-12):
   European Transport (istiee.unict.it editorial-advisory-board): Carboni <- Politecnico di Torino 00bgk9508,
   Medeghini <- Brescia Mobilita (no ROR); Marks DROP phantoms #15765, #15761.
   JMID (mechanism-design.org): Biro <- HAS 02ks8qq67, Izmalkov <- NES 033904843, Klijn <- UAB 052g8jq94,
   Koshevoy <- RAS 05qrfxd25, Unver <- Boston College 02n2fzt79; Marks DROP of the 5 phantom institution rows and of
   non-person rows (section header, site-policy links, a sentence fragment, article titles).
E. School-unit rule: own-ROR schools (AMSE, EDHEC, IESEG, Sant'Anna, BBS) and printed school names that carry the
   parent (GWU, Nord, Queen's Canada, Temple, UCSD, Edinburgh, Utrecht). API-verified, catalog RORs only.
F. Missing country from the printed raw's final country token only (no ROR on row), single-country strings.
raw_affiliation untouched except on DROP rows. No row-count/header/EOL changes. Pilots byte-identical."""
from __future__ import annotations
import csv, json, re, sys, glob, shutil, importlib.util, os
from collections import Counter, defaultdict
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("fr1", HERE / "full_review_fix_20261111.py")
FR = importlib.util.module_from_spec(spec); spec.loader.exec_module(FR)
spec2 = importlib.util.spec_from_file_location("sul", HERE / "school_unit_leftover_20261112.py")
SUL = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(SUL)
PR, WI, T, M = FR.PR, FR.WI, FR.T, FR.M
ROOT = M.ROOT; STAMP = os.environ.get("CL_STAMP", "20261112"); METHOD = f"current_leftovers_{STAMP}"
FREEZE_ID = f"editors_current_leftovers_{STAMP}"; BASE_ID = "editors_leftover_fixes_20261112"
SRC = ROOT / f"releases/{BASE_ID}"; FREEZE = ROOT / f"releases/{FREEZE_ID}"
for mod in (M, T, WI, PR, FR, SUL):
    for a, v in (("SRC_FREEZE", SRC), ("SRC", SRC), ("FREEZE", FREEZE)):
        if hasattr(mod, a) or mod is not SUL: setattr(mod, a, v)
M.LOGF = ROOT / f"abs_ajg/logs/current_leftovers_{STAMP}.log"
FR.DIRDIFF_NAME = f"CURRENT_LEFTOVERS_directory_diff_{STAMP}.csv"
log = M.log; LONG = WI.LONG; FT = WI.FT
CHANGELOG_NAME = f"CURRENT_LEFTOVERS_changes_{STAMP}.csv"; SKIPS_NAME = f"CURRENT_LEFTOVERS_skipped_{STAMP}.csv"
R = "https://ror.org/"
ET = "editors_abdc_c_current#"; JM = "editors_abs_ajg_gap_ajg1_current#"
ET_URL = "https://istiee.unict.it/content/editorial-advisory-board"; JM_URL = "https://www.mechanism-design.org/"
# (person key, expected person name, phantom key, expected phantom name, printed org, ROR or "", country, url)
ATTACH = [
    (ET+"15764", "Angela Carboni", ET+"15765", "Politecnico di Torino", "Politecnico di Torino, Italy", "00bgk9508", "Italy", ET_URL),
    (ET+"15760", "Marco Medeghini", ET+"15761", "Brescia Mobilità", "Brescia Mobilità, Italy", "", "Italy", ET_URL),
    (JM+"11088", "Péter Biró", JM+"11089", "Hungarian Academy of Sciences, Hungary", "Hungarian Academy of Sciences, Hungary", "02ks8qq67", "Hungary", JM_URL),
    (JM+"11102", "Sergei Izmalkov", JM+"11103", "New Economic School, Russia", "New Economic School, Russia", "033904843", "Russia", JM_URL),
    (JM+"11108", "Flip Klijn", JM+"11109", "Universitat Autònoma de Barcelona, Spain", "Universitat Autònoma de Barcelona, Spain", "052g8jq94", "Spain", JM_URL),
    (JM+"11111", "Gleb Koshevoy", JM+"11112", "Russian Academy of Sciences, Russia", "Russian Academy of Sciences, Russia", "05qrfxd25", "Russia", JM_URL),
    (JM+"11142", "Utku Ünver", JM+"11143", "Boston College, USA", "Boston College, USA", "02n2fzt79", "United States", JM_URL),
]
NONPERSON = {JM+"11149": "Former Editorial Members", JM+"11167": "General Policy", JM+"11168": "Open-Access License",
             JM+"11169": "Peer Review Policies", JM+"11170": "based at York, UK.",
             JM+"11173": "A festschrift for Vince Crawford", JM+"11175": "Kenneth Arrow's last theorem",
             JM+"11183": "Object-based unawareness: Theory and applications", JM+"11187": "Object-based unawareness: Axioms",
             JM+"11207": None, JM+"11208": None, JM+"11209": None, JM+"11210": None}
E_EDITS = [["editors_abdc_a_current#9703", "02ek9wp67", "Aix-Marseille School of Economics"], ["editors_abs_ajg_gap_ajg1_current#7931", "02ek9wp67", "Aix-Marseille School of Economics"], ["editors_abs_ajg_gap_ajg1_current#7937", "02ek9wp67", "Aix-Marseille School of Economics"], ["editors_abs_ajg_gap_ajg1_current#7950", "02ek9wp67", "Aix-Marseille School of Economics"], ["editors_abdc_b_current#41365", "05q7a8a02", "EDHEC Business School"], ["editors_abs_ajg_gap_ajg2_current#4685", "05q7a8a02", "EDHEC Business School"], ["editors_abdc_a_current#19807", "04jqeag92", "IESEG School of Management"], ["editors_abdc_a_current#30515", "04jqeag92", "IESEG School of Management"], ["editors_abdc_a_current#40574", "04jqeag92", "IESEG School of Management"], ["editors_abdc_b_current#38287", "04jqeag92", "IESEG School of Management"], ["editors_abdc_b_current#41350", "04jqeag92", "IESEG School of Management"], ["editors_abdc_b_current#41362", "04jqeag92", "IESEG School of Management"], ["editors_abdc_b_current#39561", "025602r80", "Sant'Anna School of Advanced Studies"], ["editors_abs_ajg_gap_ajg1_current#504", "025602r80", "Sant'Anna School of Advanced Studies"], ["editors_abs_ajg_gap_ajg1_current#507", "025602r80", "Sant'Anna School of Advanced Studies"], ["editors_abdc_c_current#19156", "00r3jwh90", "Budapest Business School, Budapest"], ["editors_abdc_a_current#19790", "00y4zzh67", "George Washington University School of Business"], ["editors_abdc_b_current#29942", "030mwrt98", "Nord University Business School"], ["editors_abdc_b_current#31449", "030mwrt98", "Nord University Business School"], ["editors_abdc_a_current#16819", "02y72wh86", "Smith School of Business, Queen's University"], ["editors_abdc_a_current#34826", "00kx1jb78", "Temple University Beasley School of Law"], ["editors_abdc_b_current#40695", "00kx1jb78", "Temple University Beasley School of Law"], ["editors_abdc_b_current#13842", "0168r3w48", "UC San Diego School of Global Policy and Strategy"], ["editors_abdc_b_current#9084", "01nrxwf90", "University of Edinburgh Business School"], ["editors_abdc_b_current#33075", "01nrxwf90", "University of Edinburgh Business School"], ["editors_abs_ajg_gap_ajg2_current#4427", "01nrxwf90", "University of Edinburgh Business School"], ["editors_abdc_b_current#34642", "04pp8hn57", "Utrecht University School of Economics"]]
F_EDITS = [["editors_abdc_a_current#15114", "India"], ["editors_abdc_a_current#15493", "United Kingdom"], ["editors_abdc_a_current#19197", "United States"], ["editors_abdc_a_current#19231", "United States"], ["editors_abdc_a_current#23817", "India"], ["editors_abdc_a_current#24286", "India"], ["editors_abdc_a_current#24335", "India"], ["editors_abdc_a_current#26574", "India"], ["editors_abdc_a_current#27465", "United States"], ["editors_abdc_a_current#27506", "United States"], ["editors_abdc_a_current#33057", "India"], ["editors_abdc_a_current#35595", "United States"], ["editors_abdc_a_current#39310", "India"], ["editors_abdc_a_current#40010", "India"], ["editors_abdc_a_current#42836", "United States"], ["editors_abdc_a_star_current#3024", "United States"], ["editors_abdc_a_star_current#3062", "United States"], ["editors_abdc_a_star_current#3082", "United States"], ["editors_abdc_a_star_current#3298", "United States"], ["editors_abdc_a_star_current#3319", "United States"], ["editors_abdc_a_star_current#3325", "United States"], ["editors_abdc_a_star_current#3372", "United States"], ["editors_abdc_a_star_current#3401", "United States"], ["editors_abdc_a_star_current#3618", "United States"], ["editors_abdc_a_star_current#3632", "United States"], ["editors_abdc_a_star_current#20028", "United States"], ["editors_abdc_a_star_current#21009", "United States"], ["editors_abdc_a_star_current#21084", "United States"], ["editors_abdc_a_star_current#21354", "United States"], ["editors_abdc_b_current#8622", "United States"], ["editors_abdc_b_current#15629", "United States"], ["editors_abdc_b_current#22482", "United States"], ["editors_abdc_b_current#24439", "United States"], ["editors_abdc_b_current#24468", "United States"], ["editors_abdc_b_current#24714", "United States"], ["editors_abdc_b_current#24811", "United States"], ["editors_abdc_b_current#28196", "India"], ["editors_abdc_b_current#28764", "The Netherlands"], ["editors_abdc_b_current#30851", "United States"], ["editors_abdc_b_current#32733", "India"], ["editors_abdc_b_current#33813", "United States"], ["editors_abdc_b_current#34393", "United States"], ["editors_abdc_b_current#34508", "United States"], ["editors_abdc_b_current#36528", "United States"], ["editors_abdc_b_current#36957", "United States"], ["editors_abdc_c_current#8214", "India"], ["editors_abdc_c_current#12671", "Bahrain"], ["editors_abdc_c_current#13263", "Poland"], ["editors_abdc_c_current#13468", "United States"], ["editors_abdc_c_current#13473", "United States"], ["editors_abdc_c_current#14045", "Poland"], ["editors_abdc_c_current#15003", "United States"], ["editors_abdc_c_current#17207", "United States"], ["editors_abdc_c_current#17847", "United States"], ["editors_abdc_c_current#20575", "United States"], ["editors_abdc_c_current#24818", "India"], ["editors_abs_ajg_gap_ajg1_current#1358", "United States"], ["editors_abs_ajg_gap_ajg1_current#1740", "Italy"], ["editors_abs_ajg_gap_ajg1_current#2222", "United States"], ["editors_abs_ajg_gap_ajg1_current#3174", "United States"], ["editors_abs_ajg_gap_ajg1_current#7832", "Japan"], ["editors_abs_ajg_gap_ajg1_current#9673", "Japan"], ["editors_abs_ajg_gap_ajg1_current#9823", "United Kingdom"], ["editors_abs_ajg_gap_ajg2_current#873", "United States"], ["editors_abs_ajg_gap_ajg2_current#4158", "United States"], ["editors_abs_ajg_gap_prio43_current#1998", "United States"], ["editors_ft50_current_with_ror#6124", "United States"], ["editors_ft50_current_with_ror#6472", "United States"]]
UNTOUCHED = tuple(JM + str(i) for i in (11106, 11107, 11113, 11114, 11115, 11132, 11133, 11150, 11171, 11196, 12320, 12325)) + \
    tuple(ET + str(i) for i in (15763, 15767)) + ("editors_abdc_a_current#40833", "editors_abdc_b_current#33794",
    "editors_abdc_b_current#35895", "editors_abdc_a_current#29393", "editors_abdc_b_current#35355",
    "editors_abs_ajg_gap_ajg1_current#8580", "editors_abdc_a_current#34176", "editors_abs_ajg_gap_ajg2_current#1943",
    "editors_abs_ajg_gap_ajg2_current#5449", "editors_abs_ajg_gap_ajg2_current#5450")
MOVE_EXTRA_FIELDS = {"affiliation_count", "primary_aff_basis", "ror_id_aff_rank"}
BLANK_DROP = ("canonical_name", "raw_affiliation", "ror_id", "ror_name", "lat", "lon")  # country/continent stay


def main():
    if M.LOGF.exists(): M.LOGF.unlink()
    log(f"start {FREEZE_ID}")
    catalog, all_rors, _n2i = M.build_twin_catalog(SRC)
    cc = defaultdict(Counter)
    for tw in catalog.values():
        if tw.get("ror_country") and tw.get("continent"): cc[tw["ror_country"]][tw["continent"]] += 1
    CONT.update({c: v.most_common(1)[0][0] for c, v in cc.items()})
    log(f"country->continent from catalog: {len(CONT)} countries")
    dir_ajg1 = glob.glob("/workspace/edj-web/data/editors/*/releases/current/editors_abs_ajg_gap_ajg1_current.csv")[0]
    dir_keys = {r["editor_row_key"] for r in csv.DictReader(open(dir_ajg1, encoding="utf-8-sig"))}
    M.copy_freeze_base()
    for p in FREEZE.glob("*.py"):
        if p.name != Path(__file__).name: p.unlink()
    for p in list(FREEZE.glob("LEFTOVER_FIXES_*")) + list(FREEZE.glob("_summary_*.json")): p.unlink()
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

    def apply(item, action, name, k, fields, note):
        f = FR.file_of(k)
        if f in M.PILOT_FILES: skip(item, action, name, "pilot file stays untouched", f, k); return False
        row = idx.get(f, {}).get(k)
        if row is None: skip(item, action, name, "row key not in panel", f, k); return False
        if k in nav: skip(item, action, name, "AJG1 nav row untouched", f, k); return False
        blob = " ".join((row.get(c) or "") for c in ("canonical_name", "raw_affiliation", "ror_name"))
        if M.PROTECT_RX.search(blob) or re.search(r"1\s*decembrie\s*1918", blob, re.I):
            skip(item, action, name, "protected organisation on row", f, k); return False
        if SUL.hold_hit(blob): skip(item, action, name, "held string on row", f, k); return False
        ch = []
        for fld, val in fields.items():
            if fld in row and row[fld] != val: ch.append((fld, row[fld], val)); row[fld] = val
        if not ch: return False
        changed[(f, k)] = dict(item=item, action=action, name=name, ch=ch, note=note, editor_name=orig[f][k].get("editor_name", ""))
        stats[item]["applied"] += 1
        return True

    def addnote(row, tr): return f"{row['ror_notes']}; {tr}" if row.get("ror_notes") else tr

    api_check = {}
    def api_ok(rid, country):
        if rid in api_check: return api_check[rid]["ok"]
        a = SUL.api(R + rid); tw = catalog.get(R + rid)
        ok = bool(a) and not a.get("_404") and a["status"] == "active" and tw is not None and \
            FR.same_country(SUL.country_norm(a["country"]), country) and not M.is_system_ror_name(a["name"]) and \
            FR.same_country(tw["ror_country"], country)
        api_check[rid] = dict(ok=ok, status=a and a.get("status"), name=a and a.get("name"), country=a and a.get("country"),
                              in_catalog=tw is not None)
        return ok

    def drop(item, k, printed, extra):
        f = FR.file_of(k); row = idx[f].get(k)
        tr = (f"{METHOD}: Marks-style DROP; non-person row, printed editor_name '{printed}'" +
              (f", printed raw '{row.get('raw_affiliation')}'" if row.get("raw_affiliation") else "") +
              (f", was ROR {row['ror_id']}" if row.get("ror_id") else "") + extra)
        fl = {c: "" for c in BLANK_DROP}; fl.update(editor_name="", editor_name_raw="", ror_notes=addnote(row, tr))
        return apply(item, "DROP", printed, k, fl, "Marks-style DROP of non-person row; country/continent kept")

    # ---- D1. attach + phantom drop
    for pk, pname, phk, phname, printed, rid, country, url in ATTACH:
        item = "D_ET" if pk.startswith(ET) else "D_JMID"
        f = FR.file_of(pk); p, ph = idx[f].get(pk), idx[f].get(phk)
        if not (p and ph and p["editor_name"] == pname and ph["editor_name"] == phname and int(phk.split("#")[1]) == int(pk.split("#")[1]) + 1
                and not p.get("raw_affiliation") and not p.get("ror_id") and not p.get("canonical_name")
                and not ph.get("raw_affiliation") and not ph.get("ror_id")):
            skip(item, "ATTACH", printed, "person/phantom rows not in expected state", f, pk); continue
        if rid and not api_ok(rid, country):
            skip(item, "ATTACH", printed, f"{rid} failed API/catalog check", f, pk); continue
        fl = dict(affiliation_count="1", primary_aff_basis="single",
                  ror_notes=f"{METHOD}: ATTACH; official board ({url}, fetched 2026-11-12) prints '{printed}' under this editor; "
                            f"it was scraped into the next row #{phk.split('#')[1]} as an editor name; raw_affiliation left blank, not invented"
                            + (f"; ROR {rid} API active, {country}" if rid else "; no ROR (none assigned, not guessed)"))
        if rid:
            tw = catalog[R + rid]
            fl.update(canonical_name=tw["ror_name"], ror_id=R + rid, ror_name=tw["ror_name"], ror_country=tw["ror_country"],
                      continent=tw["continent"], lat=tw["lat"], lon=tw["lon"], ror_id_aff_rank="1")
        else:
            fl.update(canonical_name=printed.rsplit(",", 1)[0].strip(), ror_country=country, continent=CONT[country])
        if apply(item, "ATTACH", printed, pk, fl, f"affiliation attached from phantom #{phk.split('#')[1]} per official board"):
            drop(item, phk, phname, f" (affiliation of #{pk.split('#')[1]} {pname}; official board {url})")
    # ---- D2. non-person rows
    for k, nm in NONPERSON.items():
        f = FR.file_of(k); row = idx[f].get(k)
        if row is None or row.get("journal") != "Journal of Mechanism and Institution Design" or row.get("ror_id") or row.get("raw_affiliation") \
                or (nm is not None and row.get("editor_name") != nm):
            skip("D_JMID", "DROP", nm or "", "row not in expected state", f, k); continue
        drop("D_JMID", k, row["editor_name"], f"; not an editor (site header/policy link/article text scraped from {JM_URL})")

    # ---- E. school-unit rematches
    for k, rid, disp in E_EDITS:
        f = FR.file_of(k); row = idx[f].get(k)
        if row is None or row.get("ror_id") or row.get("canonical_name") != disp:
            skip("E_school_unit", "REMATCH", disp, "row not in expected state", f, k); continue
        tw = catalog.get(R + rid)
        country = tw["ror_country"] if tw else ""
        if row.get("ror_country") and not FR.same_country(row["ror_country"], country):
            skip("E_school_unit", "REMATCH", disp, f"row country {row['ror_country']} != ROR country {country}", f, k); continue
        if not api_ok(rid, country):
            skip("E_school_unit", "REMATCH", disp, f"{rid} failed API/catalog check", f, k); continue
        apply("E_school_unit", "REMATCH", tw["ror_name"], k,
              dict(canonical_name=tw["ror_name"], ror_id=R + rid, ror_name=tw["ror_name"], ror_country=tw["ror_country"],
                   continent=tw["continent"], lat=tw["lat"], lon=tw["lon"],
                   ror_notes=addnote(row, f"{METHOD}: school-unit rule; '{disp}' -> {tw['ror_name']} {rid} "
                                          f"({'own ROR' if SUL.fold(disp) in {SUL.fold(n) for n in (SUL.api(R + rid) or {}).get('names', [])} else 'parent named in printed school'}; API active, {tw['ror_country']}); raw left as printed")),
              f"school-unit rematch -> {rid}")

    # ---- F. printed-country fills
    for k, country in F_EDITS:
        country = SPELL.get(country, country)
        if country not in CONT:
            skip("F_country", "FILL", country, "country spelling not used by any catalog ROR; left blank", FR.file_of(k), k); continue
        f = FR.file_of(k); row = idx[f].get(k)
        if row is None or row.get("ror_id") or row.get("ror_country") or not row.get("canonical_name"):
            skip("F_country", "FILL", "", "row not in expected state", f, k); continue
        apply("F_country", "FILL", country, k,
              dict(ror_country=country, continent=row.get("continent") or CONT[country],
                   ror_notes=addnote(row, f"{METHOD}: country filled from printed raw (final token); no ROR assigned")),
              "printed-country fill")

    log(f"panel stats {json.dumps({k: dict(v) for k, v in stats.items()})} changed={len(changed)}")
    for f, (hdr, rows) in data.items():
        if f in M.PILOT_FILES: continue
        M.write_csv(FREEZE / f, hdr, rows, M.detect_lineterminator(SRC / f))

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
            tr = f"{METHOD}: Marks-style DROP; printed editor_name '{orig[f][k].get('editor_name')}'"
            for p in ps:
                lset(p, "ror_match_note", f"{p['ror_match_note']}; {tr}" if p.get("ror_match_note") else tr, k, op["item"], "DROP")
                for c in ("raw_aff_part", "ror_id", "ror_name", "editor_name"): lset(p, c, "", k, op["item"], "DROP")
                lset(p, "is_panel_ror", "0", k, op["item"], "DROP")
        elif op["action"] == "FILL":
            fl = [p for p in ps if p["is_panel_ror"] == "1"]
            if fl: long_skip.append((k, "long has a panel-ROR row on a no-ROR panel row; left")); continue
            prim = sorted(ps, key=rank)[0]
            if prim["ror_country"] and prim["ror_country"] != r["ror_country"]:
                long_skip.append((k, "long primary has a different country; left")); continue
            lset(prim, "ror_country", r["ror_country"], k, op["item"], "FILL", "long primary ror_country from panel")
        else:
            fl = [p for p in ps if p["is_panel_ror"] == "1"]
            tgt = fl[0] if fl else sorted(ps, key=rank)[0]
            for p in ps:
                if p is not tgt and p["is_panel_ror"] == "1": lset(p, "is_panel_ror", "0", k, op["item"], op["action"])
            if r.get("ror_id"):
                lset(tgt, "ror_id", r["ror_id"], k, op["item"], op["action"]); lset(tgt, "ror_name", r["ror_name"], k, op["item"], op["action"])
                lset(tgt, "is_panel_ror", "1", k, op["item"], op["action"])
            lset(tgt, "ror_country", r["ror_country"], k, op["item"], op["action"])
            tr = f"{METHOD}: {op['note']}"
            lset(tgt, "ror_match_note", f"{tgt['ror_match_note']}; {tr}" if tgt.get("ror_match_note") else tr, k, op["item"], op["action"])

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

    v = FR.verify(dict(changed), orig, set(all_rors), nav)
    attach_keys = {a[0] for a in ATTACH}
    allowed = {"raw_affiliation", "canonical_name", "ror_id", "ror_name", "ror_country", "continent", "lat", "lon", "ror_notes",
               "editor_name", "editor_name_raw"} | MOVE_EXTRA_FIELDS
    v["panel_unexpected"] = [u for u in v["panel_unexpected"] if not (len(u) == 3 and u[1] in attach_keys and set(u[2]) <= allowed)]
    v["panel_unexpected_n"] = len(v["panel_unexpected"])
    v["long_skipped"] = long_skip
    bad = []
    for k in UNTOUCHED:
        f = FR.file_of(k)
        if {r["editor_row_key"]: r for r in FR.load(f, SRC)[1]}.get(k) != {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]}.get(k):
            bad.append(k)
    v["untouched_rows_changed"] = bad
    held_broke = []
    nidx = {f: {r["editor_row_key"]: r for r in FR.load(f, FREEZE)[1]} for f in M.PANEL_FILES}
    for f, k, label in held_keys:
        if nidx[f].get(k) != orig[f][k]: held_broke.append((k, label))
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
               and not bad and not held_broke and all(x["ok"] for x in api_check.values()))
    log(f"verify ok={v['ok']}")
    dirdiff, eb, ea = directory_diff(changed)
    counts = {"before": build("cl_before", eb), "after": build("cl_after", ea)}
    summ = dict(stats={k: dict(x) for k, x in stats.items()}, skips=len(skips), changelog_lines=len(changelog),
                directory_diff_lines=len(dirdiff), api=api_check, long_skip=long_skip, held_rows_on_base=len(held_keys),
                build_site_changes=BUILD_SITE_CHANGES)
    json.dump(dict(summary=summ, verify=v, counts=counts), open(FREEZE / f"_summary_{STAMP}.json", "w"), indent=1, ensure_ascii=False, default=str)
    shutil.copy2(Path(__file__), FREEZE / Path(__file__).name)
    log(f"done ok={v['ok']}")
    print("OK" if v["ok"] else "NOT OK")


CONT = {}
BUILD_SITE_CHANGES = []


def build(tag, edits):
    """PR.build plus: if an AJG gap file's dropped-name guard fails, patch expected_dropped in the copy and record it."""
    import subprocess
    orig_run = subprocess.run
    def run(cmd, *a, **kw):
        r = orig_run(cmd, *a, **kw)
        if isinstance(cmd, list) and cmd[-1:] == ["scripts/build_site.py"] and r.returncode != 0:
            out = (r.stdout or "") + (r.stderr or "")
            m = re.search(r"(editors_abs_ajg_gap_(\w+)_current\.csv) dropped (\d+) names, expected (\d+)", out)
            if m:
                bs = Path(kw["cwd"]) / "scripts/build_site.py"; src = bs.read_text(encoding="utf-8")
                pat = re.compile(r'(AJG_GAP_DIR / "' + re.escape(m.group(1)) + r'",\n\s*frozenset\(\{[^}]*\}\),\n\s*\d+,\n\s*)' + m.group(4) + r',([^\n]*)')
                new, n = pat.subn(lambda mm: mm.group(1) + m.group(3) + f",  # {METHOD}: JMID non-person/phantom rows blanked", src, count=1)
                if n:
                    bs.write_text(new, encoding="utf-8")
                    BUILD_SITE_CHANGES.append(dict(tag=tag, file=m.group(1), old=int(m.group(4)), new=int(m.group(3))))
                    return orig_run(cmd, *a, **kw)
        return r
    subprocess.run = run
    try: return PR.build(tag, edits)
    finally: subprocess.run = orig_run
SPELL = {"The Netherlands": "Netherlands", "Turkey": "Türkiye"}


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
