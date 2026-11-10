#!/usr/bin/env python3
"""Raw-leak freeze 2026-11-10 (Asia/Taipei).
Base: editors_raw_drift_fix_20261110 -> Freeze: editors_raw_leak_fix_20261110 (user-approved via Econ-Journal-Web).
Keyed on editor_row_key. Input: RAW_DRIFT_leak_scan_20261110.csv (166 rows where a 20261028/29 institution_* script
overwrote the printed raw with a canonical / ROR name).
 L1 restore printed raw (original capture) on the leak rows; long raw_aff_part synced; contacts scrubbed
 L2 wrong-organisation rows: canonical/ROR/country/continent/lat/lon set to the printed organisation (panel/ROR-API RORs only)
 S1 Qiang Meng A* #18960 (Transportation Science): board still prints NUS -> ror_notes note only
 S2 faculty_profile_url containing an e-mail address blanked (publish panels)
Pilot files untouched."""
from __future__ import annotations
import csv, json, re, sys, glob, importlib.util
from collections import Counter, defaultdict
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("pr", HERE / "post_review_fix_20261110.py")
PR = importlib.util.module_from_spec(spec); spec.loader.exec_module(PR)
WI, T, M = PR.WI, PR.T, PR.M
ROOT = M.ROOT; STAMP = "20261110"; METHOD = "raw_leak_fix_20261110"
FREEZE_ID = "editors_raw_leak_fix_20261110"; BASE_ID = "editors_raw_drift_fix_20261110"
SRC = ROOT / f"releases/{BASE_ID}"; FREEZE = ROOT / f"releases/{FREEZE_ID}"
for mod in (M, T, WI, PR):
    for a, v in (("SRC_FREEZE", SRC), ("SRC", SRC), ("FREEZE", FREEZE)):
        setattr(mod, a, v)
M.LOGF = ROOT / f"abs_ajg/logs/raw_leak_fix_{STAMP}.log"
log = M.log
LONG, FT, FTR = WI.LONG, WI.FT, WI.FTR
CHANGELOG_NAME = f"RAW_LEAK_changes_{STAMP}.csv"; SKIPS_NAME = f"RAW_LEAK_skipped_{STAMP}.csv"; DIRDIFF_NAME = f"RAW_LEAK_directory_diff_{STAMP}.csv"
LEAK = SRC / "RAW_DRIFT_leak_scan_20261110.csv"
ORIG = json.load(open("/tmp/rd/orig_pick.json", encoding="utf-8"))
VER = {r["editor_row_key"]: r for r in csv.DictReader(open("/tmp/rd/verify2.csv", encoding="utf-8"))}
R = "https://ror.org/"
EXTRA = {R + "03m7qjm52": ("Universitas Galuh", "Indonesia", "Asia", "-7.3257", "108.3534")}  # ROR API v2, fetched 2026-11-10 (Ciamis, West Java)
A, AS, B, C = "editors_abdc_a_current#", "editors_abdc_a_star_current#", "editors_abdc_b_current#", "editors_abdc_c_current#"
P43, AJ1, AJ2 = "editors_abs_ajg_gap_prio43_current#", "editors_abs_ajg_gap_ajg1_current#", "editors_abs_ajg_gap_ajg2_current#"
NIO = "was 'National Institute of Oceanography' (trailing_place 20261028 rewrite)"
AMP = "was 'AM Publications' (trailing_place 20261028 rewrite)"
TMP = "was 'Temple University' 00kx1jb78 (trailing_place 20261028 rewrite)"
# key -> (ror_id or None, canonical when no ROR, country when no ROR, note)
FIX = {
    AS + "25101": (None, "SAGE Publications", "United Kingdom", AMP + "; printed SAGE Publications, UK; panel ROR 05534qc24 is SAGE Publishing (United States) -> UK office left without ROR"),
    A + "28483": (R + "05534qc24", None, None, AMP + "; printed SAGE Publications, USA -> SAGE Publishing (United States) panel ROR"),
    B + "18746": (None, "SAGE Publications", "", AMP + "; printed 'SAGE Publications' with no country -> no ROR (US vs UK office not evidenced)"),
    AJ1 + "4225": (None, "SAGE Publications", "United Kingdom", AMP + "; printed SAGE Publications, UK -> no ROR (see A* #25101)"),
    A + "14215": (None, "", "", AMP + "; printed text is a role only ('Lyn Beamesderfer Director, Publications') -> no organisation, India removed"),
    A + "14216": (None, "", "", AMP + "; printed role only ('Director, Publications') -> no organisation, India removed"),
    A + "14217": (None, "", "", AMP + "; printed role only ('Associate, Publications') -> no organisation, India removed"),
    A + "14218": (None, "", "", AMP + "; printed role only ('Manager, Publications') -> no organisation, India removed"),
    A + "45346": (None, "AAIS", "", AMP + "; printed 'Publications and Membership Officer, AAIS' -> AAIS (Australasian Association for Information Systems; no ROR); India removed"),
    C + "7630": (None, "Peter Honey Publications", "United Kingdom", AMP + "; printed Peter Honey Publications - UK; no ROR"),
    C + "22205": (None, "Delta Hedge Publications", "", AMP + "; printed Delta Hedge Publications; no ROR; India removed"),
    A + "14508": (None, "National Institute for Working Life", "Sweden", "was 'National Institute for Sports' (Nigeria); printed The National Institute for Working Life, Sweden (Arbetslivsinstitutet, closed 2007; no ROR in ROR API)"),
    C + "17453": (None, "National Institute for Smart Government", "India", "was 'National Institute for Sports' (Nigeria); printed National Institute for Smart Government, India; no ROR in ROR API"),
    A + "21641": (R + "00ntfnx83", None, None, TMP + "; printed 'Waheda University, Japan' = misprint of Waseda (Airo Hino is Professor at Waseda); panel ROR"),
    B + "22277": (R + "00ntfnx83", None, None, TMP + "; printed 'Wadesa University, Japan' = misprint of Waseda (Hideaki Miyajima, Waseda); panel ROR"),
    B + "14383": (R + "00pbv8y11", None, None, TMP + "; printed Otaru University, Japan = Otaru University of Commerce (only university in Otaru); panel ROR"),
    C + "5528": (R + "05n757p35", None, None, TMP + "; printed 'Hiroshimashudo University' = Hiroshima Shudo University; panel ROR"),
    B + "9304": (R + "04mhzgx49", None, None, "was 'Hellriegel Institut' (Germany); printed '... Department of Labour Studies, Tel Aviv University' (Guy Mundlak) -> Tel Aviv University panel ROR"),
    B + "36164": (None, "PGIM", "", "was University of Colombo 02phn5242 (PGIM read as Post Graduate Institute of Medicine); Josh Cohen (Journal of Retirement) is at PGIM, the Prudential asset manager -> no ROR (ROR 01j78b619 'PGIM' is the Colombo medical institute, not this)"),
    C + "16430": (R + "03m7qjm52", None, None, "was Monash University; printed Galuh University, Indonesia = Universitas Galuh, Ciamis (ROR API 03m7qjm52)"),
    AJ2 + "2222": (R + "02v51f717", None, None, "was Beihang 00wk2mp56; printed 'Beijing University, China'; Yiqun Gan is Professor at Peking University (psy.pku.edu.cn profile; co-EIC of this journal) -> Peking University panel ROR"),
    B + "9508": (R + "00nqqvk19", None, None, NIO + "; printed Center of Islamic Finance, COMSATS University (CUI) = COMSATS University Islamabad panel ROR"),
    C + "22679": (R + "00nqqvk19", None, None, NIO + "; printed Department of Management Sciences, COMSATS University -> COMSATS University Islamabad panel ROR"),
    B + "12844": (R + "048w4c951", None, None, NIO + "; printed IoBM Karachi = Institute of Business Management panel ROR"),
    C + "24728": (R + "03egfpm06", None, None, NIO + "; printed CEIF, IBA-Karachi -> Institute of Business Administration Karachi panel ROR"),
    C + "24729": (R + "03egfpm06", None, None, NIO + "; printed CEIF, IBA-Karachi -> Institute of Business Administration Karachi panel ROR"),
    C + "21222": (R + "03w2j5y17", None, None, NIO + "; printed School of Social Sciences & Humanities NUST -> National University of Sciences and Technology panel ROR"),
    B + "30798": (None, "Government Girls College", "Pakistan", NIO + "; printed Government Girls College - Pakistan; no ROR"),
    C + "21199": (None, "", "Pakistan", NIO + "; printed title only ('HEC Distinguished National Professor, Islamabad') -> no organisation"),
    C + "24689": (None, "Akhuwat University", "Pakistan", NIO + "; printed Vice Chancellor of Akhuwat University; no ROR in ROR API"),
    C + "12708": (None, "Muslim Youth University", "Pakistan", NIO + "; printed Muslim Youth University; no ROR in ROR API"),
    C + "19527": (None, "Center of Sustainability Research and Consultancy", "Pakistan", NIO + "; printed President, Center of Sustainability Research and Consultancy; no ROR"),
    C + "21215": (None, "Pakistan Fisher Folk Forum", "Pakistan", NIO + "; printed Pakistan Fisher Folk Forum, Karachi; no ROR"),
    C + "21211": (None, "State Bank of Pakistan", "Pakistan", NIO + "; printed State Bank of Pakistan, Karachi; no ROR in ROR API"),
    C + "21214": (None, "State Bank of Pakistan", "Pakistan", NIO + "; printed State Bank of Pakistan, Karachi; no ROR in ROR API"),
    C + "21218": (None, "State Bank of Pakistan", "Pakistan", NIO + "; printed State Bank of Pakistan, Karachi; no ROR in ROR API"),
    C + "9831": (None, "", "Pakistan", NIO + "; printed role only ('ex. Senator, Islamic Republic of Pakistan') -> no organisation"),
    C + "24720": (None, "", "Pakistan", NIO + "; printed role only ('Former Auditor General of Pakistan') -> no organisation"),
    # misclassified as same-organisation in the leak scan; actually a different organisation
    AS + "22876": (R + "03y4dt428", None, None, "was Nottingham Trent University 04xyxjd90; printed Nottingham University Ningbo, China = University of Nottingham Ningbo China panel ROR"),
    A + "17596": (R + "03y4dt428", None, None, "was Nottingham Trent University; printed Nottingham University Ningbo, China -> UNNC panel ROR"),
    A + "7050": (R + "03y4dt428", None, None, "was Nottingham Trent University; printed Nottingham University-Ningbo, China -> UNNC panel ROR"),
    C + "9605": (R + "03y4dt428", None, None, "was Nottingham Trent University; printed Nottingham University Ningbo (PRC) -> UNNC panel ROR"),
    C + "9699": (R + "03y4dt428", None, None, "was Nottingham Trent University; printed Nottingham University Business School China -> UNNC panel ROR"),
    P43 + "1334": (R + "00eae9z71", None, None, "was Newcastle University (UK) 01kj2bm70; printed The University of Newcastle, New South Wales, Australia (Scott Brown) -> University of Newcastle Australia panel ROR"),
}
RAW_ONLY_WRONG = {  # in the 46 but the current institution is already the printed organisation
    A + "16537": "University of Genoa already right (printed DIBRIS, University of Genova); raw restored with e-mail removed",
    C + "22128": "Alexandru Ioan Cuza University 022kvet57 already right; raw restored",
    A + "24868": "GITR Limited (UK) already right; raw restored",
    C + "16208": "IESE Business School 00v9d4z37 already right; raw restored",
    AJ1 + "2783": "Canadian Business Success Centre (Canada) already right; raw restored",
    B + "33518": "Beihang 00wk2mp56 kept: printed 'Beijing University' but Wenbo Chen is Professor at Beihang (hss.buaa.edu.cn profile; earlier T&F note 'Beihang University, Beijing'); raw restored",
}
SKIP = {k: "NOT restored: the pre-rewrite value came from the ajg_gap faculty-search remiss/url step, not from the printed board (first capture blank). The African Affairs board prints city only (e.g. 'TOM GOODFELLOW (Sheffield)', 'HAZEL GRAY (Edinburgh)', 'NICHOLAS WESTCOTT (SOAS)'); current institution kept."
        for k in (P43 + "3079", P43 + "3084", P43 + "3085", P43 + "3086", P43 + "3092")}
SKIP[P43 + "3085"] += " Tom Goodfellow = Professor at University of Sheffield (OUP board bio); restoring 'University of Oxford, UK' would be wrong."
SKIP[P43 + "3086"] += " Hazel Gray = University of Edinburgh (IASH profile); restoring 'Oxford University' would be wrong."
QM = AS + "18960"; QM_URL = "https://pubsonline.informs.org/page/trsc/editorial-board"
FPU = (A + "15895", AS + "13053")


def main():
    if M.LOGF.exists(): M.LOGF.unlink()
    log(f"start {FREEZE_ID}")
    catalog, all_rors, _ = M.build_twin_catalog(SRC)
    cont = T.continent_map()
    def rorf(rid):
        if rid in EXTRA:
            n, c, ct, la, lo = EXTRA[rid]; return dict(ror_id=rid, ror_name=n, ror_country=c, continent=ct, lat=la, lon=lo)
        t = catalog[rid]; return dict(ror_id=rid, ror_name=t["ror_name"], ror_country=t["ror_country"], continent=t["continent"], lat=t["lat"], lon=t["lon"])
    leak = {r["editor_row_key"]: r for r in csv.DictReader(open(LEAK, encoding="utf-8"))}
    assert len(leak) == 166 and set(FIX) - set(leak) == set() and set(RAW_ONLY_WRONG) <= set(leak) and set(SKIP) <= set(leak)
    M.copy_freeze_base()
    data = {f: PR.load(f, FREEZE) for f in M.PANEL_FILES}
    idx = {f: {r["editor_row_key"]: r for r in rows} for f, (_h, rows) in data.items()}
    changelog, skips, changed = [], [], {}
    def fof(k): return k.split("#")[0] + ".csv"
    def setrow(f, k, item, action, vals, note, notes_tag=True):
        row = idx[f][k]; ch = []
        for fld, v in vals.items():
            if fld in row and row[fld] != v: ch.append((fld, row[fld], v)); row[fld] = v
        if ch and notes_tag and "ror_notes" in row:
            nv = f"{row['ror_notes']}; {METHOD}: {item} {action} ({PR.red(note)[:230]})".lstrip("; ")
            ch.append(("ror_notes", row["ror_notes"], nv)); row["ror_notes"] = nv
        for fld, o, n in ch:
            changelog.append(dict(file=f, editor_row_key=k, editor_name=PR.red(row["editor_name"]), item=item, action=action, field=fld,
                                  old=PR.red(o) if fld != "faculty_profile_url" else "[email removed] (URL contained an e-mail address)", new=PR.red(n),
                                  verification=VER.get(k, {}).get("status", ""), note=PR.red(note)))
        if ch:
            prev = changed.get((f, k)); changed[(f, k)] = (item if not prev else prev[0] + "+" + item, action, note, (prev[3] if prev else []) + ch)
    contact_scrubbed = []
    for k, lr in leak.items():
        f = fof(k)
        if k in SKIP:
            r = idx[f][k]; skips.append(dict(item="L1", file=f, editor_row_key=k, editor_name=r["editor_name"], current_raw=r["raw_affiliation"],
                                              pre_rewrite_value=ORIG[k]["orig"], reason=SKIP[k])); continue
        o = ORIG[k]["orig"]; new = PR.scrub_contact(o) if PR.has_contact(o) else o
        if new != o: contact_scrubbed.append(k)
        wrong = k in FIX
        vals = {"raw_affiliation": new}
        note = f"printed raw restored from {ORIG[k]['rel'].replace('editors_', '')}" + (" ([email removed])" if new != o else "")
        if wrong:
            rid, can, ctry, why = FIX[k]
            if rid:
                rf = rorf(rid); vals.update(rf); vals["canonical_name"] = rf["ror_name"]
            else:
                vals.update(ror_id="", ror_name="", lat="", lon="", canonical_name=can, ror_country=ctry, continent=cont.get(ctry, "") if ctry else "")
            note += "; " + why
            setrow(f, k, "L1+L2", "RESTORE_RAW+FIX_INST", vals, note)
        else:
            if k in RAW_ONLY_WRONG: note += "; " + RAW_ONLY_WRONG[k]
            else: note += "; same organisation, institution/ROR unchanged"
            setrow(f, k, "L1", "RESTORE_RAW", vals, note)
    # S1 Qiang Meng
    setrow(fof(QM), QM, "S1", "NOTE_ONLY", {}, "", notes_tag=False)
    r = idx[fof(QM)][QM]
    qn = f"moved to HKUST(GZ) 2026-08-28 per https://hksts.org/en/seminar/268/; board page still prints NUS as of 2026-11-10 ({QM_URL})"
    setrow(fof(QM), QM, "S1", "NOTE_ONLY", {"ror_notes": (r["ror_notes"] + "; " + qn).lstrip("; ")}, qn, notes_tag=False)
    # S2 faculty_profile_url e-mail
    fpu_hits = []
    for f in M.PUBLISH_FILES:
        for r in data[f][1]:
            if PR.EM.search(r.get("faculty_profile_url") or ""): fpu_hits.append((f, r["editor_row_key"]))
    for f, k in fpu_hits:
        setrow(f, k, "S2", "BLANK_FACULTY_URL", {"faculty_profile_url": ""}, "faculty_profile_url contained an e-mail address -> blanked", notes_tag=False)
    pilot_fpu = [(f, r["editor_row_key"]) for f in M.PILOT_FILES for r in data[f][1] if PR.EM.search(r.get("faculty_profile_url") or "")]
    for f in M.PANEL_FILES:
        h, rows = data[f]
        if f in M.PILOT_FILES: continue
        M.write_csv(FREEZE / f, h, rows, M.detect_lineterminator(SRC / f))
    # ---- long table ----
    lh, lrows = PR.load(LONG, FREEZE)
    parts = defaultdict(list)
    for x in lrows: parts[x["editor_row_key"]].append(x)
    base_idx = {f: {r["editor_row_key"]: r for r in PR.load(f, SRC)[1]} for f in M.PUBLISH_FILES}
    def lset(t, fld, v, k, item, action):
        if t[fld] != v:
            changelog.append(dict(file=LONG, editor_row_key=k, editor_name="", item=item, action=action, field=fld, old=PR.red(t[fld]), new=PR.red(v),
                                  verification=VER.get(k, {}).get("status", ""), note=f"aff_rank {t['aff_rank']}"))
            t[fld] = v
    long_skip = []
    rank = lambda x: int(x["aff_rank"]) if x["aff_rank"].isdigit() else 99
    for (f, k), (item, action, note, ch) in changed.items():
        fields = {c[0] for c in ch}
        if not fields & {"raw_affiliation", "ror_id", "ror_country"}: continue
        ps = parts.get(k)
        if not ps: long_skip.append((k, "no long rows")); continue
        r = idx[f][k]; o = base_idx[f][k]
        if "raw_affiliation" in fields:
            if len(ps) == 1: tgt = ps[0]
            else:
                m = [p for p in ps if p["raw_aff_part"] == o["raw_affiliation"]]
                tgt = m[0] if len(m) == 1 else None
            if tgt is None: long_skip.append((k, f"{len(ps)} long parts, none equal to the old raw; raw_aff_part not changed"))
            else:
                lset(tgt, "raw_aff_part", r["raw_affiliation"], k, item, action)
                lset(tgt, "ror_match_note", f"{tgt['ror_match_note']}; {METHOD}: raw_aff_part restored to printed text".lstrip("; "), k, item, action)
        if r.get("ror_id", "") != o.get("ror_id", ""):
            fl = [p for p in ps if p["is_panel_ror"] == "1"]
            t = fl[0] if fl else sorted(ps, key=rank)[0]
            if r["ror_id"]:
                lset(t, "ror_id", r["ror_id"], k, item, action); lset(t, "ror_name", r["ror_name"], k, item, action); lset(t, "is_panel_ror", "1", k, item, action)
            else:
                for x in fl: lset(x, "ror_id", "", k, item, action); lset(x, "ror_name", "", k, item, action); lset(x, "is_panel_ror", "0", k, item, action)
        fl = [p for p in ps if p["is_panel_ror"] == "1"]
        prim = fl[0] if fl else sorted(ps, key=rank)[0]
        lset(prim, "ror_country", r.get("ror_country", ""), k, item, action)
    M.write_csv(FREEZE / LONG, lh, lrows, M.detect_lineterminator(SRC / LONG))
    M.update_working_panels()
    for c in changelog:
        for kk in ("old", "new", "note", "editor_name"): assert not PR.has_contact(c[kk] or ""), ("contact leaked into change log", c)
    with open(FREEZE / CHANGELOG_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(changelog[0].keys())); w.writeheader(); w.writerows(changelog)
    for k, why in long_skip: skips.append(dict(item="L1-long", file=LONG, editor_row_key=k, editor_name="", current_raw="", pre_rewrite_value="", reason=why))
    for f, k in pilot_fpu: skips.append(dict(item="S2", file=f, editor_row_key=k, editor_name=idx[f][k]["editor_name"], current_raw="", pre_rewrite_value="",
                                             reason="pilot file: faculty_profile_url also contains the au.dk e-mail URL; not blanked because pilot files must stay byte-identical (needs a decision)"))
    with open(FREEZE / SKIPS_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["item", "file", "editor_row_key", "editor_name", "current_raw", "pre_rewrite_value", "reason"]); w.writeheader(); w.writerows(skips)
    v = verify(changed, all_rors, contact_scrubbed)
    v.update(long_skipped=long_skip, faculty_url_email_blanked=fpu_hits, faculty_url_email_left_in_pilot=pilot_fpu, contact_scrubbed_on_restore=contact_scrubbed)
    # Directory diff + Web build counts on a copy
    dirdiff, e_before, e_after = directory_diff(changed)
    counts = {"before": PR.build("rl_before", e_before), "after": PR.build("rl_after", e_after)}
    summ = dict(rows_changed=Counter(f"{i}:{a}" for (_f, _k), (i, a, _n, _c) in changed.items()), raw_restored=sum(1 for (_f, _k), (_i, _a, _n, c) in changed.items() if any(x[0] == "raw_affiliation" for x in c)),
                inst_fixed=sum(1 for (_f, _k), (i, _a, _n, _c) in changed.items() if "L2" in i), skips=len(skips), changelog_lines=len(changelog), directory_diff_lines=len(dirdiff), extra_rors=sorted(EXTRA))
    json.dump(dict(summary=summ, verify=v, counts=counts), open(FREEZE / f"_summary_{STAMP}.json", "w"), indent=1, ensure_ascii=False, default=str)
    print(json.dumps(dict(summary=summ, verify=v, counts=counts), indent=1, ensure_ascii=False, default=str)[:9000])


FIELDS = ["raw_affiliation", "canonical_name", "ror_id", "ror_name", "ror_country", "continent", "lat", "lon", "faculty_profile_url"]


def directory_diff(changed):
    dk = {}
    for f in glob.glob(WI.DIR_GLOB):
        for r in csv.DictReader(open(f, encoding="utf-8-sig", newline="")): dk[(Path(f).name, r["editor_row_key"])] = r
    out, e_before, e_after = [], defaultdict(lambda: defaultdict(dict)), defaultdict(lambda: defaultdict(dict))
    for f in M.PUBLISH_FILES:
        b = {r["editor_row_key"]: r for r in PR.load(f, SRC)[1]}; n = {r["editor_row_key"]: r for r in PR.load(f, FREEZE)[1]}
        for k, r in n.items():
            d = dk.get((f, k))
            if d is None: continue
            for fld in FIELDS:
                if fld not in r or fld not in d: continue
                if b[k][fld] != d[fld]: e_before[f][k][fld] = b[k][fld]
                if r[fld] != d[fld]:
                    e_after[f][k][fld] = r[fld]
                    if (f, k) in changed:
                        out.append(dict(file=f, editor_row_key=k, field=fld, directory_value=PR.red(d[fld]) if fld != "faculty_profile_url" else "[email removed]", new_value=PR.red(r[fld])))
    with open(FREEZE / DIRDIFF_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "editor_row_key", "field", "directory_value", "new_value"]); w.writeheader(); w.writerows(out)
    return out, e_before, e_after


def verify(changed, all_rors, scrubbed):
    v = {}; allowed = {"raw_affiliation", "canonical_name", "ror_id", "ror_name", "ror_country", "continent", "lat", "lon", "ror_notes", "faculty_profile_url"}
    unexpected, hdr, counts, invented, prot_inst, contact, raw_bad = [], [], {}, set(), [], [], []
    leakk = set(csv.DictReader(open(LEAK, encoding="utf-8")).__iter__().__next__().keys()) and {r["editor_row_key"] for r in csv.DictReader(open(LEAK, encoding="utf-8"))}
    for f in M.PANEL_FILES:
        b = list(csv.DictReader(open(SRC / f, encoding="utf-8", newline=""))); rd = csv.DictReader(open(FREEZE / f, encoding="utf-8", newline="")); n = list(rd)
        counts[f] = (len(b), len(n))
        if rd.fieldnames != list(b[0].keys()) or M.detect_lineterminator(SRC / f) != M.detect_lineterminator(FREEZE / f): hdr.append(f)
        for x, y in zip(b, n):
            if x["editor_row_key"] != y["editor_row_key"]: unexpected.append((f, "order")); break
            if x == y: continue
            k = y["editor_row_key"]; diff = [c for c in x if x[c] != y[c]]
            if (f, k) not in changed or any(c not in allowed for c in diff): unexpected.append((f, k, diff))
            if "raw_affiliation" in diff and k not in leakk: raw_bad.append(k)
            if y.get("ror_id") and y["ror_id"] not in all_rors and y["ror_id"] not in EXTRA: invented.add(y["ror_id"])
            if M.PROTECT_RX.search(" ".join((x.get(c) or "") for c in ("canonical_name", "raw_affiliation", "ror_name"))) and set(diff) - {"raw_affiliation", "ror_notes"}: prot_inst.append(k)
            for c in ("raw_affiliation", "canonical_name", "ror_notes", "faculty_profile_url"):
                if PR.has_contact(y.get(c) or "") or (c == "faculty_profile_url" and PR.EM.search(y.get(c) or "")): contact.append((k, c))
    pil_ident = {f: open(SRC / f, "rb").read() == open(FREEZE / f, "rb").read() for f in M.PILOT_FILES}
    lb = list(csv.DictReader(open(SRC / LONG, encoding="utf-8", newline=""))); ln = list(csv.DictReader(open(FREEZE / LONG, encoding="utf-8", newline="")))
    lhdr = open(SRC / LONG, "rb").readline() == open(FREEZE / LONG, "rb").readline() and M.detect_lineterminator(SRC / LONG) == M.detect_lineterminator(FREEZE / LONG)
    ck = {k for (_f, k) in changed}; lunexp = []
    for x, y in zip(lb, ln):
        if x != y and (y["editor_row_key"] not in ck or "pilot" in y["panel_file"] or any(c not in {"raw_aff_part", "ror_id", "ror_name", "ror_country", "is_panel_ror", "ror_match_note"} for c in x if x[c] != y[c])): lunexp.append(y["editor_row_key"])
    long_contact = sum(1 for y in ln if PR.has_contact(y["raw_aff_part"]) or PR.has_contact(y["ror_match_note"]))
    long_contact_base = sum(1 for y in lb if PR.has_contact(y["raw_aff_part"]) or PR.has_contact(y["ror_match_note"]))
    def desync(pdir, L):
        bb = defaultdict(list)
        for p in L: bb[p["editor_row_key"]].append(p)
        out = set()
        for f in M.PANEL_FILES:
            if f == FT: continue
            for r in csv.DictReader(open(pdir / f, encoding="utf-8", newline="")):
                ps = bb.get(r["editor_row_key"])
                if not ps: continue
                fl = [p for p in ps if p["is_panel_ror"] == "1"]; rid = r.get("ror_id", "")
                if (rid and (len(fl) != 1 or fl[0]["ror_id"] != rid)) or (not rid and fl): out.add((r["editor_row_key"], "ror")); continue
                prim = fl[0] if fl else sorted(ps, key=lambda x: int(x["aff_rank"]) if x["aff_rank"].isdigit() else 99)[0]
                if prim["ror_country"] != r.get("ror_country", ""): out.add((r["editor_row_key"], "country"))
        return out
    dn, dbase = desync(FREEZE, ln), desync(SRC, lb)
    ch_desync = sorted(d for d in dn if d[0] in ck)
    pk = {}
    for f in M.PUBLISH_FILES:
        for r in csv.DictReader(open(FREEZE / f, encoding="utf-8", newline="")): pk[r["editor_row_key"]] = r
    by = defaultdict(list)
    for p in ln: by[p["editor_row_key"]].append(p)
    raw_unsynced = [k for (f, k), (_i, _a, _n, ch) in changed.items() if any(c[0] == "raw_affiliation" for c in ch) and len(by[k]) == 1 and by[k][0]["raw_aff_part"] != pk[k]["raw_affiliation"]]
    dir_keys = {r["editor_row_key"] for r in csv.DictReader(open(glob.glob("/workspace/edj-web/data/editors/*/releases/current/editors_abs_ajg_gap_ajg1_current.csv")[0], encoding="utf-8"))}
    a1 = [r["editor_row_key"] for r in csv.DictReader(open(FREEZE / "editors_abs_ajg_gap_ajg1_current.csv", encoding="utf-8"))]
    nav = {k for k in a1 if k not in dir_keys}
    keep11, unsw, insead = 0, set(), set()
    for r in pk.values():
        blob = " ".join((r.get(c) or "") for c in ("canonical_name", "raw_affiliation", "ror_name")); rid = r.get("ror_id", "")
        if "11KBW" in blob: keep11 += 1
        if re.search(r"\bUNSW\b", blob) and rid: unsw.add(rid)
        if "INSEAD" in blob and rid: insead.add(rid)
    NL = r"[\u0400-\u04FF\u0590-\u06FF\u0E00-\u0E7F\u3040-\u30FF\u4E00-\u9FFF\uAC00-\uD7AF]"
    nonlatin_lost = [k for (f, k), (_i, _a, _n, chs) in changed.items() for (fld, o, nv) in chs if fld in ("canonical_name", "raw_affiliation") and re.search(NL, o) and not re.search(NL, nv)]
    near = [k for (f, k), (_i, _a, _n, ch) in changed.items() for fld, o, nv in ch if fld == "ror_name" for p in WI.NEAR_MISS
            if (re.search(p[0], o, re.I) and re.search(p[1], nv, re.I)) or (re.search(p[1], o, re.I) and re.search(p[0], nv, re.I))]
    v.update(row_counts=counts, row_counts_unchanged=all(a == b for a, b in counts.values()) and len(lb) == len(ln), long_rows=len(ln),
             ajg1_file_rows=len(a1), ajg1_nav=len(nav), ajg1_nav_touched=len([1 for (f, k) in changed if k in nav]), ajg2_rows=counts["editors_abs_ajg_gap_ajg2_current.csv"][1],
             header_or_eol_changes=hdr + ([] if lhdr else [LONG]), panel_unexpected=unexpected[:10], panel_unexpected_n=len(unexpected), raw_changed_outside_leak=raw_bad,
             long_unexpected=lunexp[:10], long_unexpected_n=len(lunexp), pilot_files_byte_identical=pil_ident, invented_ror=sorted(invented), new_real_ror_added=sorted(EXTRA),
             protected_rows_institution_changed=prot_inst, contact_in_changed_panel_rows=contact, long_contact_rows=(long_contact_base, long_contact),
             panel_long_desync_changed_rows=ch_desync, panel_long_desync_full_table=len(dn), base_desync_full_table=len(dbase), raw_part_unsynced=raw_unsynced,
             nonlatin_lost=nonlatin_lost, near_miss=near, keep_11kbw=keep11 > 0, unsw=M.UNSW_SYDNEY in unsw, insead_fr_sg=M.INSEAD_FRANCE in insead and M.INSEAD_SINGAPORE in insead,
             working_panels_identical=all(open(FREEZE / f, "rb").read() == open(p, "rb").read() for f, p in M.LIVE_PANELS.items()))
    v["ok"] = (v["row_counts_unchanged"] and len(a1) == 12326 and len(nav) == 10 and not v["ajg1_nav_touched"] and v["ajg2_rows"] == 5462 and len(ln) == 269545
               and not v["header_or_eol_changes"] and not unexpected and not raw_bad and not lunexp and all(pil_ident.values()) and not invented and not prot_inst
               and not contact and long_contact <= long_contact_base and not ch_desync and len(dn) <= len(dbase) and not raw_unsynced and not nonlatin_lost and not near
               and v["keep_11kbw"] and v["unsw"] and v["insead_fr_sg"] and v["working_panels_identical"])
    log(f"verify ok={v['ok']}")
    return v


if __name__ == "__main__":
    main()
