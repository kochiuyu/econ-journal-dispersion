#!/usr/bin/env python3
"""Full Institutions review freeze 2026-11-11 (Asia/Taipei).
Base: editors_raw_leak_fix_20261110 -> Freeze: editors_full_review_fix_20261111
(user-approved via Econ-Journal-Web after reviewing the live Institutions page).
Keyed on editor_row_key. Input: /workspace/institutions_full_review_send_20261111.csv
(3,517 Institutions). The hold file is not applied.
 MERGE  : rematch publish/long rows to target_name / target_ror / target_country; raw untouched
 DROP   : Marks-style — blank canonical, raw and ROR; keep printed text in ror_notes / long ror_match_note; keep country/continent
 RENAME : set institution to the printed organisation (ROR only if send/panel-verified); raw untouched
 SET_COUNTRY (CSV action FIX_COUNTRY): fix/fill country and continent; office in the printed text wins over HQ
 Paauwe : A* #2545 and FT50 #3821 — name 'Jaap Paauwe', Tilburg in the affiliation, blank editor_name_raw
Pilot files stay byte-identical. No invented RORs. No publish/message."""
from __future__ import annotations
import csv, json, re, sys, glob, importlib.util
from collections import Counter, defaultdict
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("pr", HERE / "post_review_fix_20261110.py")
PR = importlib.util.module_from_spec(spec); spec.loader.exec_module(PR)
WI, T, M = PR.WI, PR.T, PR.M
ROOT = M.ROOT; STAMP = "20261111"; METHOD = "full_review_fix_20261111"
FREEZE_ID = "editors_full_review_fix_20261111"; BASE_ID = "editors_raw_leak_fix_20261110"
SRC = ROOT / f"releases/{BASE_ID}"; FREEZE = ROOT / f"releases/{FREEZE_ID}"
for mod in (M, T, WI, PR):
    for a, v in (("SRC_FREEZE", SRC), ("SRC", SRC), ("FREEZE", FREEZE)):
        setattr(mod, a, v)
M.LOGF = ROOT / f"abs_ajg/logs/full_review_fix_{STAMP}.log"
log = M.log
LONG, FT, FTR = WI.LONG, WI.FT, WI.FTR
CHANGELOG_NAME = f"FULL_REVIEW_changes_{STAMP}.csv"
SKIPS_NAME = f"FULL_REVIEW_skipped_{STAMP}.csv"
DIRDIFF_NAME = f"FULL_REVIEW_directory_diff_{STAMP}.csv"
SEND = Path("/workspace/institutions_full_review_send_20261111.csv")
HOLD = Path("/workspace/institutions_full_review_hold_20261111.csv")
R = "https://ror.org/"
TILBURG = R + "04b8v1s79"
PAAUWE = {
    "editors_abdc_a_star_current#2545": "editors_abdc_a_star_current.csv",
    "editors_ft50_current#3821": "editors_ft50_current.csv",
    "editors_ft50_current_with_ror#3821": "editors_ft50_current_with_ror.csv",
}
NEAR_MISS = list(WI.NEAR_MISS) + [
    (r"\bde la salle\b", r"(?<!\bde )\bla salle\b"),
    (r"1\s*decembrie\s*1918|decembrie\s*1918", r"decembrie"),
]
SKIP_MERGE_NAMES = {
    "Concordia U., CA": "coin-flip: 'CA' is Canada vs California; target Concordia University is in the hold file (US ROR on some rows); not merged",
    "Universidad del Pacifico, Engineering": "target Universidad del Pacífico is a hold-file COIN_FLIP (Peru vs Chile); raw names no country; not merged",
}
# When printed text names an office country/city, that office wins over an HQ target.
OFFICE_WINS = True
EXTRA_CONT = {
    "Puerto Rico": "North America", "Bahrain": "Asia", "Trinidad and Tobago": "North America",
    "Lithuania": "Europe", "Greece": "Europe", "Iran": "Asia", "Indonesia": "Asia",
    "Malaysia": "Asia", "Brazil": "South America", "United Arab Emirates": "Asia",
    "Egypt": "Africa", "Hong Kong": "Asia", "Czechia": "Europe", "Slovakia": "Europe",
    "Turks and Caicos Islands": "North America", "Cayman Islands": "North America", "Mexico": "North America", "Netherlands": "Europe", "The Netherlands": "Europe",
    "Poland": "Europe", "Switzerland": "Europe", "Germany": "Europe", "Australia": "Oceania",
    "India": "Asia", "China": "Asia", "Japan": "Asia", "France": "Europe", "United Kingdom": "Europe",
    "United States": "North America", "Italy": "Europe", "Spain": "Europe", "Canada": "North America",
    "Belgium": "Europe", "Singapore": "Asia", "Norway": "Europe", "Finland": "Europe",
    "Sweden": "Europe", "Ireland": "Europe", "Iceland": "Europe", "Portugal": "Europe",
}
# extra country tokens for office detection
CTRY_EXTRA = {
    "brasil": "Brazil", "brazil": "Brazil", "the netherlands": "Netherlands", "netherlands": "Netherlands",
    "holland": "Netherlands", "switzerland": "Switzerland", "uae": "United Arab Emirates",
    "united arab emirates": "United Arab Emirates", "bahrein": "Bahrain", "bahrain": "Bahrain",
    "puerto rico": "Puerto Rico", "czech republic": "Czechia", "czechia": "Czechia",
    "hong kong": "Hong Kong", "hong kong sar": "Hong Kong", "iran": "Iran",
    "islamic republic of iran": "Iran", "iran, islamic republic of": "Iran",
    "lithuania": "Lithuania", "greece": "Greece", "indonesia": "Indonesia", "malaysia": "Malaysia",
    "poland": "Poland", "egypt": "Egypt", "mexico": "Mexico", "slovakia": "Slovakia",
    "trinidad and tobago": "Trinidad and Tobago", "trinidad": "Trinidad and Tobago",
    "eswatini": "Eswatini", "swaziland": "Eswatini", "rak": "United Arab Emirates",
    "ras al khaimah": "United Arab Emirates", "singapore": "Singapore", "norway": "Norway",
    "belgium": "Belgium", "ireland": "Ireland", "iceland": "Iceland", "portugal": "Portugal",
    "sweden": "Sweden", "finland": "Finland", "japan": "Japan", "china": "China",
    "india": "India", "australia": "Australia", "germany": "Germany", "france": "France",
    "italy": "Italy", "spain": "Spain", "canada": "Canada", "brazil": "Brazil",
}

def same_country(a, b):
    def n(x):
        t = re.sub(r"^the ", "", (x or "").strip().casefold())
        if t in ("holland", "netherlands"): return "netherlands"
        if t in ("usa", "us", "u.s.", "u.s.a.", "united states of america", "united states of america (the)"): return "united states"
        if t in ("uk", "u.k.", "england", "scotland", "wales", "great britain"): return "united kingdom"
        return t
    return bool(a) and bool(b) and n(a) == n(b)

def norm_country(c):
    t = (c or "").strip()
    if not t: return ""
    if t.casefold() in ("the netherlands", "netherlands", "holland"): return "Netherlands"
    if t.casefold() in ("brasil", "brazil"): return "Brazil"
    if t.casefold() in ("usa", "us", "u.s.", "u.s.a."): return "United States"
    if t.casefold() in ("uk", "u.k.", "england"): return "United Kingdom"
    if t == "SWITZERLAND": return "Switzerland"
    return t

def office_country(raw):
    # prefer PR.raw_country then extra trailing tokens
    c = PR.raw_country(raw or "")
    if c: return norm_country(c)
    segs = [s.strip(" .()") for s in re.split(r"\s*[,;]\s*|\s+-\s+|\s*/\s*", raw or "") if s.strip(" .()")]
    for s in reversed(segs):
        v = CTRY_EXTRA.get(s.casefold()) or PR.CTRY.get(s.casefold())
        if v: return norm_country(v)
    return None

def keys_of(s):
    return [k.strip() for k in (s or "").split(";") if k.strip()]

def file_of(k):
    return k.split("#")[0] + ".csv"

def twin_of(k):
    if k.startswith("editors_ft50_current_with_ror#"):
        return "editors_ft50_current#" + k.split("#")[1]
    if k.startswith("editors_ft50_current#") and "with_ror" not in k:
        return "editors_ft50_current_with_ror#" + k.split("#")[1]
    return None

def near_miss(src, tgt):
    hits = []
    for a, b in NEAR_MISS:
        if (re.search(a, src or "", re.I) and re.search(b, tgt or "", re.I)) or (re.search(b, src or "", re.I) and re.search(a, tgt or "", re.I)):
            # require they actually differ on the pair (avoid 'decembrie' self-match)
            if (re.search(a, src or "", re.I) and re.search(a, tgt or "", re.I)) and (re.search(b, src or "", re.I) and re.search(b, tgt or "", re.I)):
                continue
            hits.append((a, b))
    return hits

NLRX = re.compile(r"[\u0370-\u03FF\u0400-\u04FF\u0590-\u06FF\u0E00-\u0E7F\u3040-\u30FF\u3400-\u9FFF\uAC00-\uD7AF]")
def mostly_nonlatin(s):
    letters = [c for c in (s or "") if c.isalpha()]
    return bool(letters) and sum(1 for c in letters if NLRX.match(c)) * 2 > len(letters)
ACADEMIC = re.compile(r"universi|college|institut|school|polytechn|academ|hochschule|ecole|école|centre|center", re.I)

def is_system_name(name):
    return bool(name) and M.is_system_ror_name(name)


def load(fname, base=SRC):
    rd = csv.DictReader(open(base / fname, encoding="utf-8", newline=""))
    return list(rd.fieldnames), list(rd)


def main():
    if M.LOGF.exists(): M.LOGF.unlink()
    log(f"start {FREEZE_ID}")
    send = list(csv.DictReader(open(SEND, encoding="utf-8")))
    hold = list(csv.DictReader(open(HOLD, encoding="utf-8")))
    hold_names = {r["institution"] for r in hold}
    act_counts = Counter((r["collector_action"] or r["action"], r["confidence"]) for r in send)
    log(f"send={len(send)} hold={len(hold)} actions={dict(Counter(r['collector_action'] for r in send))} overlap={len({r['institution'] for r in send}&hold_names)}")
    catalog, all_rors, name_to_ids = M.build_twin_catalog(SRC)
    key_ids = defaultdict(set)
    for rid, tw in catalog.items():
        if tw.get("ror_name"): key_ids[T.key_of(tw["ror_name"])].add(rid)
    cont = T.continent_map()
    for c, v in EXTRA_CONT.items(): cont.setdefault(c, v)

    def ror_fields(rid):
        tw = catalog[rid]
        return dict(ror_id=rid, ror_name=tw["ror_name"], ror_country=tw["ror_country"],
                    continent=tw["continent"], lat=tw["lat"], lon=tw["lon"])

    def lookup_ror(name, country):
        if not name: return None
        ids = set(name_to_ids.get(name.lower(), set())) | set(key_ids.get(T.key_of(name), set()))
        if not ids: return None
        if country:
            m = [i for i in ids if same_country(catalog[i]["ror_country"], country)]
            if len(m) == 1: return m[0]
            if len(m) != 1 and len(ids) != 1: return None
        if len(ids) == 1: return next(iter(ids))
        return None

    # nav rows (AJG1) must stay untouched
    dir_ajg1 = glob.glob("/workspace/edj-web/data/editors/*/releases/current/editors_abs_ajg_gap_ajg1_current.csv")[0]
    dir_ajg1_keys = {r["editor_row_key"] for r in csv.DictReader(open(dir_ajg1, encoding="utf-8-sig"))}
    M.copy_freeze_base()
    data = {f: load(f, FREEZE) for f in M.PANEL_FILES}
    idx = {f: {r["editor_row_key"]: r for r in rows} for f, (_h, rows) in data.items()}
    orig = {f: {k: dict(r) for k, r in d.items()} for f, d in idx.items()}
    # display and ror indexes (publish only)
    by_disp = defaultdict(list)
    by_ror = defaultdict(list)
    nav = set()
    for f in M.PUBLISH_FILES:
        for r in data[f][1]:
            k = r["editor_row_key"]
            if f == "editors_abs_ajg_gap_ajg1_current.csv" and k not in dir_ajg1_keys:
                nav.add(k)
            a = T.disp(r)
            if a: by_disp[T.key_of(a)].append((f, k))
            if r.get("ror_id"): by_ror[r["ror_id"]].append((f, k))
    log(f"ajg1 nav rows={len(nav)}")

    skips, changelog, changed = [], [], {}
    stats = Counter()

    def skip(item, action, name, reason, f="", k=""):
        skips.append(dict(item=item, action=action, institution=PR.red(name), file=f, editor_row_key=k, reason=PR.red(reason)))

    def setf(row, fld, val, ch):
        if fld not in row: return
        cur = row.get(fld, "")
        if cur != val:
            ch.append((fld, cur, val))
            row[fld] = val

    def apply_row(item, action, name, f, k, fields, note=""):
        if f in M.PILOT_FILES:
            skip(item, action, name, "pilot file must stay byte-identical", f, k); return False
        row = idx[f].get(k)
        if row is None:
            skip(item, action, name, "row key not in panel", f, k); return False
        if k in nav:
            skip(item, action, name, "AJG1 nav row untouched", f, k); return False
        blob = " ".join((row.get(c) or "") for c in ("canonical_name", "raw_affiliation", "ror_name"))
        if M.PROTECT_RX.search(blob) and action in ("MERGE", "DROP", "RENAME"):
            skip(item, action, name, "protected organisation on row (11KBW/UNSW/INSEAD)", f, k); return False
        ch = []
        for fld, val in fields.items():
            setf(row, fld, val, ch)
        if not ch: return False
        key = (f, k)
        if key in changed:
            prev = changed[key]
            # fold later field changes into the same row record
            prev["ch"].extend(ch)
            prev["note"] = (prev["note"] + "; " + note).strip("; ")
        else:
            changed[key] = dict(item=item, action=action, name=name, ch=ch, note=note, editor_name=row.get("editor_name", ""))
        return True

    def collect_rows(inst, listed, ror):
        """Publish rows carrying this institution name, plus listed keys and FT50 twins."""
        seen, out = set(), []
        def add(f, k, how):
            if (f, k) in seen: return
            if f in M.PILOT_FILES: return
            seen.add((f, k)); out.append((f, k, how))
        for k in listed:
            f = file_of(k)
            add(f, k, "listed")
            tk = twin_of(k)
            if tk: add(file_of(tk), tk, "ft50_twin")
        for f, k in by_disp.get(T.key_of(inst), []):
            add(f, k, "display")
        if ror:
            for f, k in by_ror.get(ror, []):
                add(f, k, "ror")
        return out

    def resolve_ror(target_ror, target_name, target_country, action, inst):
        rid = (target_ror or "").strip()
        if rid:
            if rid not in catalog:
                skip(action, action, inst, f"send target_ror {rid} is not in the panel catalog and was not used")
                return None
            tw = catalog[rid]
            if is_system_name(tw["ror_name"]) or is_system_name(target_name):
                skip(action, action, inst, f"would assign university-system ROR {rid} ({tw['ror_name']}); name applied, ROR left blank")
                return None
            return rid
        # existing unique panel ROR for the target name only — never invent
        rid = lookup_ror(target_name, target_country)
        if rid and (is_system_name(catalog[rid]["ror_name"]) or is_system_name(target_name)):
            skip(action, action, inst, f"panel ROR {rid} looks like a university system; left blank")
            return None
        return rid

    # ---- plan + apply send file (MERGE/RENAME/DROP first, then SET_COUNTRY) ----
    applied_inst = Counter()
    skipped_inst = Counter()
    send_merge = [r for r in send if (r["collector_action"] or r["action"]) in ("MERGE", "RENAME", "DROP")]
    send_country = [r for r in send if (r["collector_action"] or r["action"]) == "SET_COUNTRY"]
    assert len(send_merge)+len(send_country)==len(send), (len(send_merge),len(send_country),len(send))

    for rec in send_merge + send_country:
        inst = rec["institution"]
        action = rec["collector_action"] or rec["action"]
        if action == "SET_COUNTRY" and rec["action"] == "FIX_COUNTRY":
            action = "SET_COUNTRY"
        tgt = (rec.get("target_name") or "").strip()
        tro = (rec.get("target_ror") or "").strip()
        tcy = norm_country(rec.get("target_country") or "")
        listed = keys_of(rec.get("editor_row_keys"))
        src_ror = (rec.get("ror") or "").strip()
        item = {"MERGE": "L1", "DROP": "L2", "RENAME": "L3", "SET_COUNTRY": "L4"}.get(action, "LX")

        if action == "MERGE" and inst in SKIP_MERGE_NAMES:
            skip(item, action, inst, SKIP_MERGE_NAMES[inst]); skipped_inst[action] += 1; continue
        if action == "MERGE" and tgt:
            nm = near_miss(inst, tgt)
            if nm:
                skip(item, action, inst, f"near-miss pair would collapse ({nm}); MERGE skipped"); skipped_inst[action] += 1; continue

        if action == "SET_COUNTRY" and not getattr(main, "_reindexed", False):
            by_disp.clear(); by_ror.clear()
            for f_ in M.PUBLISH_FILES:
                for r_ in data[f_][1]:
                    a = T.disp(r_)
                    if a: by_disp[T.key_of(a)].append((f_, r_["editor_row_key"]))
                    if r_.get("ror_id"): by_ror[r_["ror_id"]].append((f_, r_["editor_row_key"]))
            main._reindexed = True
            log("reindexed display/ror maps after MERGE/RENAME/DROP")
        hits = collect_rows(inst, listed, src_ror if action == "SET_COUNTRY" else "")
        if not hits:
            skip(item, action, inst, "no publish row with this name or listed key"); skipped_inst[action] += 1; continue

        # DROP
        if action == "DROP":
            n = 0
            for f, k, how in hits:
                row = idx[f].get(k)
                if row is None:
                    skip(item, action, inst, "row key not in panel", f, k); continue
                if row.get("ror_id"):
                    skip(item, action, inst, f"row carries ROR {row['ror_id']}; not dropped", f, k); continue
                raw = row.get("raw_affiliation", "") or inst
                extra = set(w.casefold() for w in PR.ORGWORD.findall(row.get("raw_affiliation", ""))) - set(w.casefold() for w in PR.ORGWORD.findall(inst))
                if extra:
                    skip(item, action, inst, f"printed raw names an organisation not in the dropped text ({', '.join(sorted(extra))}); not dropped", f, k); continue
                raw_s = PR.red(raw)
                fields = dict(canonical_name="", raw_affiliation="", ror_id="", ror_name="", lat="", lon="")
                # keep ror_country + continent; write trace into ror_notes when the column exists
                if "ror_notes" in row:
                    prev = (row.get("ror_notes") or "").strip()
                    trace = f"{METHOD}: user-approved DROP (Marks); printed text: {raw_s}"
                    fields["ror_notes"] = f"{prev}; {trace}" if prev else trace
                if apply_row(item, action, inst, f, k, fields, note="Marks-style DROP"): n += 1
            if n: applied_inst[action] += 1
            else:
                skipped_inst[action] += 1
                if not any(s["institution"] == PR.red(inst) for s in skips[-len(hits)-2:]):
                    skip(item, action, inst, "no-op: every matched row already at the target value")
            continue

        # SET_COUNTRY
        if action == "SET_COUNTRY":
            if not tcy:
                skip(item, action, inst, "no target_country"); skipped_inst[action] += 1; continue
            n = 0
            for f, k, how in hits:
                row = idx[f].get(k)
                if row is None:
                    skip(item, action, inst, "row key not in panel", f, k); continue
                raw = row.get("raw_affiliation", "")
                oc = office_country(raw)
                use, note = tcy, f"SET_COUNTRY -> {tcy}"
                if OFFICE_WINS and oc and not same_country(oc, tcy) and not ACADEMIC.search(inst):
                    use, note = oc, f"office in printed text is {oc}; not HQ {tcy}"
                # Ahlia University: printed says UAE, send (and the real HQ) is Bahrain
                if inst.startswith("Ahlia University") and tcy == "Bahrain":
                    use, note = "Bahrain", "printed text says UAE; send target Bahrain (Ahlia University HQ is Bahrain)"
                continent = cont.get(use, row.get("continent") or "")
                if apply_row(item, action, inst, f, k, dict(ror_country=use, continent=continent), note=note): n += 1
            if n: applied_inst[action] += 1
            else:
                skipped_inst[action] += 1
                if not any(s["institution"] == PR.red(inst) for s in skips[-len(hits)-2:]):
                    skip(item, action, inst, "no-op: every matched row already at the target value")
            continue

        # MERGE / RENAME
        if action in ("MERGE", "RENAME"):
            if not tgt:
                skip(item, action, inst, "no target_name"); skipped_inst[action] += 1; continue
            rid = resolve_ror(tro, tgt, tcy, action, inst)
            # WRONG_NAME (C.K. Tedam): keep Ghana ROR and put the Ghana name on ror_name too
            wrong_name = rec.get("category") == "WRONG_NAME"
            if wrong_name and tro and tro in catalog:
                rid = tro
            fields_base = dict(canonical_name=tgt)
            if tcy:
                fields_base["ror_country"] = tcy
                fields_base["continent"] = cont.get(tcy, "")
            if rid:
                rf = ror_fields(rid)
                if tcy: rf["ror_country"] = tcy; rf["continent"] = cont.get(tcy, rf["continent"])
                if wrong_name:
                    rf["ror_name"] = tgt
                    rf["canonical_name"] = tgt
                else:
                    rf["canonical_name"] = tgt or rf["ror_name"]
                fields_base.update(rf)
            else:
                fields_base.update(dict(ror_id="", ror_name="", lat="", lon=""))
                if tcy:
                    fields_base["ror_country"] = tcy
                    fields_base["continent"] = cont.get(tcy, "")
            n = 0
            for f, k, how in hits:
                row = idx[f].get(k)
                if row is None:
                    skip(item, action, inst, "row key not in panel", f, k); continue
                # do not overwrite a different existing ROR unless the send names it (or WRONG_NAME keeps it)
                if mostly_nonlatin(row.get("canonical_name") or row.get("raw_affiliation")):
                    skip(item, action, inst, "non-Latin printed name kept as-is (not translated by MERGE/RENAME)", f, k); continue
                cur = (row.get("ror_id") or "").strip()
                flds = dict(fields_base)
                if cur and rid and cur != rid and not wrong_name:
                    skip(item, action, inst, f"row already carries a different ROR {cur}; not rematched to {rid}", f, k); continue
                if cur and not rid and not wrong_name and action == "MERGE":
                    # keep existing ROR only if it already is the target; else leave ror fields off the name-only merge? 
                    # Safer: skip assigning blank over an existing ROR
                    skip(item, action, inst, f"row carries ROR {cur} but merge has no verified target ROR; name not applied over an existing ROR", f, k); continue
                if apply_row(item, action, inst, f, k, flds, note=rec.get("note", "")[:200] or action): n += 1
            if n: applied_inst[action] += 1
            else:
                skipped_inst[action] += 1
                if not any(s["institution"] == PR.red(inst) for s in skips[-len(hits)-2:]):
                    skip(item, action, inst, "no-op: every matched row already at the target value")
            continue

        skip("LX", action, inst, f"unrecognised action {action}")
        skipped_inst[action] += 1

    log(f"send applied institutions={dict(applied_inst)} skipped_institutions={dict(skipped_inst)} rows_so_far={len(changed)}")

    # ---- Paauwe ----
    tw = catalog[TILBURG]
    paauwe_geo = dict(ror_id=TILBURG, ror_name=tw["ror_name"] or "Tilburg University",
                      ror_country="Netherlands", continent=cont.get("Netherlands", tw["continent"] or "Europe"),
                      lat=tw["lat"], lon=tw["lon"], canonical_name="Tilburg University")
    paauwe_before = {}
    for k, f in PAAUWE.items():
        row = orig[f][k]
        paauwe_before[k] = {c: row.get(c, "") for c in
                            ("editor_name", "editor_name_raw", "raw_affiliation", "canonical_name",
                             "ror_id", "ror_name", "ror_country", "continent")}
        fields = dict(editor_name="Jaap Paauwe", editor_name_raw="", **paauwe_geo)
        if k == "editors_abdc_a_star_current#2545":
            fields["raw_affiliation"] = "Tilburg, Netherlands"
        # FT50 raw already has Tilburg University, Netherlands — leave it
        apply_row("S1", "PAAUWE", "Tilburg University", f, k, fields,
                  note="Wayback HRM board: name 'Jaap Paauwe' followed by ', Tilburg, Netherlands'")
    log(f"Paauwe applied; total changed rows={len(changed)}")

    # write panels
    for f, (hdr, rows) in data.items():
        M.write_csv(FREEZE / f, hdr, rows, M.detect_lineterminator(SRC / f))

    # ---- long sync ----
    lh, lrows = load(LONG, FREEZE)
    by_long = defaultdict(list)
    for p in lrows: by_long[p["editor_row_key"]].append(p)
    long_skip = []

    def lset(part, fld, val, k, item, action):
        if fld not in part: return
        if part[fld] != val:
            changelog.append(dict(file=LONG, editor_row_key=k, editor_name=part.get("editor_name", ""),
                                  item=item, action=action, field=fld, old=PR.red(part[fld]), new=PR.red(val),
                                  verification="", note="long sync"))
            part[fld] = val

    for (f, k), op in list(changed.items()):
        if f == FT:  # long is keyed; ft50 current also has long rows
            pass
        r = idx[f][k]
        o = orig[f][k]
        ps = by_long.get(k)
        if not ps:
            long_skip.append((k, "no long rows for key")); continue
        item, action = op["item"], op["action"]
        # editor_name
        if r.get("editor_name", "") != o.get("editor_name", ""):
            for p in ps: lset(p, "editor_name", r["editor_name"], k, item, action)
        old_raw, new_raw = o.get("raw_affiliation", ""), r.get("raw_affiliation", "")
        if new_raw != old_raw:
            if len(ps) == 1:
                if action == "DROP":
                    trace = PR.red(old_raw or op["name"])
                    prev = (ps[0].get("ror_match_note") or "").strip()
                    note = f"{METHOD}: user-approved DROP (Marks); printed text: {trace}"
                    lset(ps[0], "ror_match_note", f"{prev}; {note}" if prev else note, k, item, action)
                    lset(ps[0], "raw_aff_part", "", k, item, action)
                else:
                    lset(ps[0], "raw_aff_part", new_raw, k, item, action)
            else:
                matched = [p for p in ps if p.get("raw_aff_part") == old_raw]
                if not matched and action == "DROP":
                    # blank every part that equals the old panel raw; if none, leave and log
                    long_skip.append((k, "multi-part long row; no part equals old raw; DROP raw_aff_part not auto-blanked"))
                else:
                    for p in (matched or []):
                        if action == "DROP":
                            trace = PR.red(old_raw or op["name"])
                            prev = (p.get("ror_match_note") or "").strip()
                            note = f"{METHOD}: user-approved DROP (Marks); printed text: {trace}"
                            lset(p, "ror_match_note", f"{prev}; {note}" if prev else note, k, item, action)
                            lset(p, "raw_aff_part", "", k, item, action)
                        else:
                            lset(p, "raw_aff_part", new_raw, k, item, action)
        # ROR / country on primary (or all is_panel_ror parts when clearing)
        def rank(p):
            try: return int(p.get("aff_rank") or 99)
            except ValueError: return 99
        if r.get("ror_id", "") != o.get("ror_id", ""):
            fl = [p for p in ps if p.get("is_panel_ror") == "1"]
            if r.get("ror_id"):
                t = fl[0] if fl else sorted(ps, key=rank)[0]
                lset(t, "ror_id", r["ror_id"], k, item, action)
                lset(t, "ror_name", r.get("ror_name", ""), k, item, action)
                lset(t, "is_panel_ror", "1", k, item, action)
            else:
                for x in fl:
                    lset(x, "ror_id", "", k, item, action)
                    lset(x, "ror_name", "", k, item, action)
                    lset(x, "is_panel_ror", "0", k, item, action)
        fl = [p for p in ps if p.get("is_panel_ror") == "1"]
        prim = fl[0] if fl else sorted(ps, key=rank)[0]
        lset(prim, "ror_country", r.get("ror_country", ""), k, item, action)

    M.write_csv(FREEZE / LONG, lh, lrows, M.detect_lineterminator(SRC / LONG))
    M.update_working_panels()

    # panel changelog lines
    for (f, k), op in sorted(changed.items()):
        for fld, ov, nv in op["ch"]:
            changelog.append(dict(file=f, editor_row_key=k, editor_name=PR.red(op.get("editor_name") or ""),
                                  item=op["item"], action=op["action"], field=fld, old=PR.red(ov), new=PR.red(nv),
                                  verification="", note=PR.red(op.get("note") or "")))
    for c in changelog:
        for kk in ("old", "new", "note", "editor_name"):
            assert not PR.has_contact(c[kk] or ""), ("contact leaked into change log", c[kk][:80] if c[kk] else c)

    ch_fields = ["file", "editor_row_key", "editor_name", "item", "action", "field", "old", "new", "verification", "note"]
    with open(FREEZE / CHANGELOG_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=ch_fields); w.writeheader(); w.writerows(changelog)
    sk_fields = ["item", "action", "institution", "file", "editor_row_key", "reason"]
    with open(FREEZE / SKIPS_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=sk_fields); w.writeheader(); w.writerows(skips)

    v = verify(changed, orig, all_rors, nav)
    v.update(long_skipped=long_skip, paauwe_before=paauwe_before)
    v["paauwe_after"] = {}
    for k, f in PAAUWE.items():
        r = idx[f][k]
        v["paauwe_after"][k] = {c: r.get(c, "") for c in
                                ("editor_name", "editor_name_raw", "raw_affiliation", "canonical_name",
                                 "ror_id", "ror_name", "ror_country", "continent")}

    dirdiff, e_before, e_after = directory_diff(changed, orig)
    counts = {"before": PR.build("fr_before", e_before), "after": PR.build("fr_after", e_after)}
    # action tallies (publish, not long, not ft50 mirror double-count for inst)
    inst_done = defaultdict(set)
    rows_pub = Counter(); rows_ft = Counter()
    for (f, k), op in changed.items():
        if f in M.PILOT_FILES: continue
        if f == FT: rows_ft[op["action"]] += 1
        else:
            rows_pub[op["action"]] += 1
            inst_done[op["action"]].add(op["name"])
    summ = dict(
        send_file=dict(Counter(r["collector_action"] for r in send)),
        institutions_applied={a: len(s) for a, s in inst_done.items()},
        rows_publish=dict(rows_pub), rows_ft50_current_mirror=dict(rows_ft),
        skipped_institutions=dict(skipped_inst), skips=len(skips),
        changelog_lines=len(changelog), directory_diff_lines=len(dirdiff),
        extra_rors=[], new_rors_api_verified=[],
        send_vs_applied=dict(applied_institutions=dict(applied_inst), skipped_institutions=dict(skipped_inst)),
    )
    json.dump(dict(summary=summ, verify=v, counts=counts), open(FREEZE / f"_summary_{STAMP}.json", "w"),
              indent=1, ensure_ascii=False, default=str)
    print(json.dumps(dict(summary=summ, verify={k: val for k, val in v.items() if k != "paauwe_before"}, counts=counts),
                     indent=1, ensure_ascii=False, default=str)[:12000])
    log(f"done ok={v.get('ok')}")


FIELDS = ["raw_affiliation", "canonical_name", "ror_id", "ror_name", "ror_country", "continent", "lat", "lon", "faculty_profile_url"]
NAME_FIELDS = ["editor_name", "editor_name_raw"]


def directory_diff(changed, orig):
    dk = {}
    for f in glob.glob(WI.DIR_GLOB):
        for r in csv.DictReader(open(f, encoding="utf-8-sig", newline="")):
            dk[(Path(f).name, r["editor_row_key"])] = r
    out, e_before, e_after = [], defaultdict(lambda: defaultdict(dict)), defaultdict(lambda: defaultdict(dict))
    for f in M.PUBLISH_FILES:
        b = {r["editor_row_key"]: r for r in load(f, SRC)[1]}
        n = {r["editor_row_key"]: r for r in load(f, FREEZE)[1]}
        for k, r in n.items():
            d = dk.get((f, k))
            if d is None: continue
            for fld in FIELDS + (NAME_FIELDS if k in PAAUWE else []):
                if fld not in r or fld not in d: continue
                if fld in NAME_FIELDS and (f, k) not in changed: continue
                if b[k][fld] != d[fld] and fld not in NAME_FIELDS: e_before[f][k][fld] = b[k][fld]
                if r[fld] != d[fld]:
                    e_after[f][k][fld] = r[fld]
                    if (f, k) in changed:
                        out.append(dict(file=f, editor_row_key=k, field=fld,
                                        directory_value=PR.red(d[fld]), new_value=PR.red(r[fld])))
    with open(FREEZE / DIRDIFF_NAME, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "editor_row_key", "field", "directory_value", "new_value"])
        w.writeheader(); w.writerows(out)
    return out, e_before, e_after


def verify(changed, orig, all_rors, nav):
    v = {}
    allowed = {"raw_affiliation", "canonical_name", "ror_id", "ror_name", "ror_country", "continent",
               "lat", "lon", "ror_notes", "editor_name", "editor_name_raw"}
    drop_keys = {k for (f, k), op in changed.items() if op["action"] == "DROP"}
    paauwe_keys = set(PAAUWE)
    unexpected, hdr, counts, invented, prot_inst, contact, raw_bad = [], [], {}, set(), [], [], []
    for f in M.PANEL_FILES:
        b = list(csv.DictReader(open(SRC / f, encoding="utf-8", newline="")))
        rd = csv.DictReader(open(FREEZE / f, encoding="utf-8", newline="")); n = list(rd)
        counts[f] = (len(b), len(n))
        if rd.fieldnames != list(b[0].keys()) or M.detect_lineterminator(SRC / f) != M.detect_lineterminator(FREEZE / f):
            hdr.append(f)
        for x, y in zip(b, n):
            if x["editor_row_key"] != y["editor_row_key"]:
                unexpected.append((f, "order")); break
            if x == y: continue
            k = y["editor_row_key"]; diff = [c for c in x if x[c] != y[c]]
            if (f, k) not in changed or any(c not in allowed for c in diff):
                unexpected.append((f, k, diff))
            if "raw_affiliation" in diff and k not in drop_keys and k not in paauwe_keys:
                raw_bad.append(k)
            if y.get("ror_id") and y["ror_id"] not in all_rors:
                invented.add(y["ror_id"])
            if M.PROTECT_RX.search(" ".join((x.get(c) or "") for c in ("canonical_name", "raw_affiliation", "ror_name"))) \
                    and set(diff) - {"ror_country", "continent", "ror_notes"}:
                prot_inst.append(k)
            for c in ("raw_affiliation", "canonical_name", "ror_notes", "faculty_profile_url", "editor_name", "editor_name_raw"):
                if PR.has_contact(y.get(c) or "") or (c == "faculty_profile_url" and PR.EM.search(y.get(c) or "")
                                                       and "pilot" not in f):
                    contact.append((k, c))
    pil_ident = {f: open(SRC / f, "rb").read() == open(FREEZE / f, "rb").read() for f in M.PILOT_FILES}
    lb = list(csv.DictReader(open(SRC / LONG, encoding="utf-8", newline="")))
    ln = list(csv.DictReader(open(FREEZE / LONG, encoding="utf-8", newline="")))
    lhdr = open(SRC / LONG, "rb").readline() == open(FREEZE / LONG, "rb").readline() and \
        M.detect_lineterminator(SRC / LONG) == M.detect_lineterminator(FREEZE / LONG)
    ck = {k for (_f, k) in changed}
    lunexp = []
    long_allowed = {"raw_aff_part", "ror_id", "ror_name", "ror_country", "is_panel_ror", "ror_match_note", "editor_name"}
    for x, y in zip(lb, ln):
        if x != y and (y["editor_row_key"] not in ck or "pilot" in y.get("panel_file", "") or
                       any(c not in long_allowed for c in x if x[c] != y[c])):
            lunexp.append(y["editor_row_key"])
    long_contact = sum(1 for y in ln if PR.has_contact(y["raw_aff_part"]) or PR.has_contact(y["ror_match_note"]) or PR.has_contact(y.get("editor_name") or "", True))
    long_contact_base = sum(1 for y in lb if PR.has_contact(y["raw_aff_part"]) or PR.has_contact(y["ror_match_note"]) or PR.has_contact(y.get("editor_name") or "", True))

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
                if (rid and (len(fl) != 1 or fl[0]["ror_id"] != rid)) or (not rid and fl):
                    out.add((r["editor_row_key"], "ror")); continue
                prim = fl[0] if fl else sorted(ps, key=lambda x: int(x["aff_rank"]) if str(x.get("aff_rank","")).isdigit() else 99)[0]
                if prim["ror_country"] != r.get("ror_country", ""):
                    out.add((r["editor_row_key"], "country"))
        return out
    dn, dbase = desync(FREEZE, ln), desync(SRC, lb)
    ch_desync = sorted(d for d in dn if d[0] in ck)
    pk = {}
    for f in M.PUBLISH_FILES:
        for r in csv.DictReader(open(FREEZE / f, encoding="utf-8", newline="")): pk[r["editor_row_key"]] = r
    keep11, unsw, insead = 0, set(), set()
    for r in pk.values():
        blob = " ".join((r.get(c) or "") for c in ("canonical_name", "raw_affiliation", "ror_name")); rid = r.get("ror_id", "")
        if "11KBW" in blob: keep11 += 1
        if re.search(r"\bUNSW\b", blob) and rid: unsw.add(rid)
        if "INSEAD" in blob and rid: insead.add(rid)
    NL = r"[\u0400-\u04FF\u0590-\u06FF\u0E00-\u0E7F\u3040-\u30FF\u4E00-\u9FFF\uAC00-\uD7AF]"
    nonlatin_lost = [k for (f, k), op in changed.items() for (fld, o, nv) in op["ch"]
                     if fld in ("canonical_name", "raw_affiliation") and op["action"] != "DROP"
                     and mostly_nonlatin(o) and not mostly_nonlatin(nv)]
    near = []
    for (f, k), op in changed.items():
        if op["action"] not in ("MERGE", "RENAME"): continue
        for fld, o, nv in op["ch"]:
            if fld in ("ror_name", "canonical_name") and near_miss(o, nv):
                near.append(k)
    a1 = [r["editor_row_key"] for r in csv.DictReader(open(FREEZE / "editors_abs_ajg_gap_ajg1_current.csv", encoding="utf-8"))]
    ajg2_n = counts["editors_abs_ajg_gap_ajg2_current.csv"][1]
    nav_touched = [k for (f, k) in changed if k in nav]
    v.update(row_counts=counts, row_counts_unchanged=all(a == b for a, b in counts.values()) and len(lb) == len(ln),
             long_rows=len(ln), ajg1_file_rows=len(a1), ajg1_nav=len(nav), ajg1_nav_touched=len(nav_touched),
             ajg2_rows=ajg2_n, header_or_eol_changes=hdr + ([] if lhdr else [LONG]),
             panel_unexpected=unexpected[:15], panel_unexpected_n=len(unexpected),
             raw_changed_outside_drop_or_paauwe=raw_bad,
             long_unexpected=lunexp[:15], long_unexpected_n=len(lunexp),
             pilot_files_byte_identical=pil_ident, invented_ror=sorted(invented),
             protected_rows_institution_changed=prot_inst,
             contact_in_changed_panel_rows=contact[:10], contact_n=len(contact),
             long_contact_rows=(long_contact_base, long_contact),
             panel_long_desync_changed_rows=ch_desync[:20], panel_long_desync_changed_n=len(ch_desync),
             panel_long_desync_full_table=len(dn), base_desync_full_table=len(dbase),
             nonlatin_lost=nonlatin_lost, near_miss=near,
             keep_11kbw=keep11 > 0, unsw=M.UNSW_SYDNEY in unsw,
             insead_fr_sg=M.INSEAD_FRANCE in insead and M.INSEAD_SINGAPORE in insead,
             working_panels_identical=all(open(FREEZE / f, "rb").read() == open(p, "rb").read() for f, p in M.LIVE_PANELS.items()),
             ft50_rows=counts[FT][1], ft50_ror_rows=counts[FTR][1])
    v["ok"] = (v["row_counts_unchanged"] and len(a1) == 12326 and len(nav) == 10 and not v["ajg1_nav_touched"]
               and v["ajg2_rows"] == 5462 and len(ln) == 269545 and v["ft50_rows"] == 10049 and v["ft50_ror_rows"] == 10049
               and not v["header_or_eol_changes"] and not unexpected and not raw_bad and not lunexp
               and all(pil_ident.values()) and not invented and not prot_inst
               and not contact and long_contact <= long_contact_base and not ch_desync and len(dn) <= len(dbase)
               and not nonlatin_lost and not near and v["keep_11kbw"] and v["unsw"] and v["insead_fr_sg"]
               and v["working_panels_identical"])
    log(f"verify ok={v['ok']}")
    return v


if __name__ == "__main__":
    main()
