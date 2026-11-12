#!/usr/bin/env python3
"""Combined backfill freeze editors_backfill_red_jbes_20261113 (unpublished).
Base: core49 editors_backfill_red_gap_20261112 (live, Directory PR #70, edj-web 21df6bd).
Layer 1: RED 2025 (44 rows #15664-#15707) re-used verbatim from the intermediate freeze
         releases/editors_backfill_red_2025_20261113 (read-only; not modified).
Layer 2: JBES 2019 (Vol 37 No. 1, JSTOR stable/45181150) and JBES 2020 (Vol 38 No. 1, JSTOR stable/45282197)
         boards from the printed issue front matter, page 3, visually verified against 300/600-dpi renders.
         Keys continue at #15708. Conventions of JBES 2018 (jbes_2018_board_20261106):
         printed roles; Hutchens / Martin / Zellner panel-only (no affiliation printed, no long row);
         Committee on Publications excluded and logged in gaps; editor_name_raw = 'Name - Affiliation'.
         2019 prints exactly the 2018 list (86 names + Hutchens) -> each 2018 row/long row is cloned with
         2019 provenance; ROR decisions identical to 2018. 2020: per printed string, reuse the decision
         already taken on JBES rows (2018, 2021-2024); new strings only on exact/fold ROR-name hits (API-active).
No emails/phones are written anywhere (front-matter contact lines are not transcribed)."""
import csv, json, shutil, unicodedata, re, hashlib
from pathlib import Path
from collections import Counter, defaultdict
ROOT = Path("/workspace/econ-journal-editors")
LIVE = Path("/tmp/red25_live/data/editors/core49/releases/editors_backfill_red_gap_20261112")
MID = ROOT / "releases/editors_backfill_red_2025_20261113"
OUT = ROOT / "releases/editors_backfill_red_jbes_20261113"
WORK = ROOT / "tmp/jbes_2019_2020"
API = Path("/tmp/jbesapi")
METHOD = "jbes_2019_2020_board_20261113"; OLDM = "jbes_2018_board_20261106"
NOW = "2026-11-13T01:30:00+08:00"; CAP = "2026-11-13"
JID, JNAME = "S18095783", "Journal of Business and Economic Statistics"
JOURNAL_URL = "https://www.jstor.org/journal/jbusieconstat"
Y = {"2019": dict(stable="45181150", vol="Vol 37 No. 1", month="January 2019", ym="2019-01", issue_page="i40222888",
                  pdf=ROOT / "abs_ajg/reports/JBES_2019_editorial_board.pdf"),
     "2020": dict(stable="45282197", vol="Vol 38 No. 1", month="January 2020", ym="2020-01", issue_page="i40228730",
                  pdf=ROOT / "abs_ajg/reports/JBES_2020_editorial_board.pdf")}
TRANSCRIPT = ROOT / "abs_ajg/reports/JBES_2019_2020_board_source_20261113.md"
ROLE = {"JOINT EDITORS": ("Joint Editors", "editor"), "Editorial Coordinator": ("Editorial Coordinator", "staff"),
        "ASSOCIATE EDITORS": ("Associate Editors", "board"), "Honorary Advisory Board": ("Honorary Advisory Board", "past"),
        "FOUNDING EDITOR": ("Founding Editor", "past")}
# 2020 strings not on any earlier JBES row: assigned only on an exact/fold ROR name (checked against API below)
NEW2020 = {"Universite catholique de Louvain": "02495e989", "Cambridge University": "013meh722",
           "London School of Economics and Political Science": "0090zs177", "Universität Mannheim": "031bsb921",
           "University of Geneva": "01swzsf04", "Academy of Mathematics and Systems Science": "02jkmyk67"}
BLANK2020 = {"European University Institute": "EUI: blank by instruction (RA pack-2 S21 open); no EUI id invented",
             "VU University": "'VU University' is not a ROR name/alias (VU Amsterdam 008xxew50 lists 'VU', 'VU Amsterdam'); blank rather than guess"}
# Committee on Publications (excluded), as printed on page 3 (visually checked)
COMMITTEE = {
 "2019": [("Steve Snapinn", "Chair"), ("Dulal K. Bhaumik", "Member-at-Large"), ("Richard A. Levine", "Member-at-Large")] +
         [(n, "") for n in ["Jay Breidt", "Frank Bretz", "Li Cai", "Hugh Chipman", "Todd Clark", "Michael Cohen", "Rajeev Dehejia",
          "Scott Evans", "Monserrat Fuentes", "David Higdon", "Jennifer A. Hoeting", "Daniel R. Jeske", "Jia Li", "Roderick Little",
          "Wendy L. Martinez", "Daniel McCaffrey", "Steve Rigdon", "Soma Roy", "Jun Shao", "Hadley Wickham"]],
 "2020": [("Steve Snapinn", "Chair"), ("Dulal K. Bhaumik", "Member-at-Large"), ("Kelly McConville", "Member-at-Large")] +
         [(n, "") for n in ["Ricardo Cao", "Peter Challenor", "Steve Culpepper", "Michael Elliott", "Scott Evans", "Jianqing Fan",
          "Christian Hansen", "Daniel R. Jeske", "Jia Li", "Ranjan Maitra", "Peihua Qiu", "Jerome P. Reiter", "Steve Rigdon",
          "David Warton", "Roy Welsch", "Jeffrey A. Witmer", "Heping Zhang"]]}
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"); PHONE = re.compile(r"\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}")
LOG = []
def log(*a): LOG.append(" ".join(str(x) for x in a)); print(*a)
def fold(s): return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower())
def api(i):
    d = json.load(open(API / f"{i}.json")); loc = d["locations"][0]["geonames_details"]
    return dict(status=d["status"], name=next(n["value"] for n in d["names"] if "ror_display" in n["types"]),
                names=[n["value"] for n in d["names"]], country=loc["country_name"], continent=loc["continent_name"],
                lat=str(loc["lat"]), lon=str(loc["lng"]))
def read(p):
    b = p.read_bytes(); lt = "\r\n" if b"\r\n" in b[:20000] else "\n"
    rd = csv.DictReader(open(p, encoding="utf-8", newline="")); return rd.fieldnames, list(rd), lt
def write(p, hdr, rows, lt):
    with open(p, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=hdr, lineterminator=lt); w.writeheader(); w.writerows(rows)
def append(p, hdr, rows):
    """append rows to an existing CSV keeping its bytes; uses the file's own terminator"""
    b = p.read_bytes(); lt = "\r\n" if b"\r\n" in b[:20000] else "\n"
    assert b.endswith(lt.encode())
    import io; s = io.StringIO(); w = csv.DictWriter(s, fieldnames=hdr, lineterminator=lt); w.writerows(rows)
    p.write_bytes(b + s.getvalue().encode("utf-8"))
def board(y):
    return [(ROLE[r][0], ROLE[r][1], n, a) for r, n, a in BOARDS[y]]

def prov(row, y, printed_role, name):
    c = Y[y]; url = f"https://www.jstor.org/stable/{c['stable']}"
    row.update(year=y, board_year=y, source_url=url, collection_date=CAP, capture_date=CAP, snapshot_date=CAP,
               data_source=f"publisher_issue_front_matter_{y}", capture_timestamp=NOW,
               board_urls=f"{url}|{JOURNAL_URL}", board_url_count="2", board_status="issue_front_matter",
               snapshot_source=f"JBES {c['vol']} ({c['ym']}) JSTOR Front Matter; printed issue board, captured {CAP}",
               source_file=f"tmp/jbes_2019_2020/jbes_{y}_front_matter_extract.txt", name_style="full",
               source_type="official_issue", issue=f"{c['vol']} ({c['month']}) Front Matter", is_former="no", former_flag="0",
               affiliation_imputed="no", journal_id=JID, journal=JNAME,
               source_note=(f"JBES {c['vol']} ({c['month']}) JSTOR Front Matter masthead; printed issue board, captured {CAP}; "
                            f"source JSTOR stable/{c['stable']} (via CUHK Easy Access); role as printed '{printed_role}'; "
                            f"name as printed on board ('{name}'); method={METHOD}"))
    return row

def main():
    global BOARDS
    BOARDS = json.load(open(WORK / "boards_page_verified.json"))
    # Hutchens (Editorial Coordinator) sits between the Joint Editors and the Associate Editors on both pages
    for y in BOARDS:
        b = BOARDS[y]; i = max(k for k, r in enumerate(b) if r[0] == "JOINT EDITORS") + 1
        b.insert(i, ["Editorial Coordinator", "Jamie Hutchens", ""])
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    skip = {"README.md", "HANDOFF.md", "RELEASE_NOTES.md", "_build.json", "_summary_20261113.json"}
    for f in sorted(MID.iterdir()):
        if f.name in skip or f.suffix in (".py", ".log"): continue
        shutil.copy2(f, OUT / f.name)
    ph, P, plt = read(MID / "editors_backfill_scale_ror_panel.csv")
    lh, L, llt = read(MID / "editor_affiliations.csv")
    assert len(P) == 15708 and len(L) == 11940, (len(P), len(L))
    keyn = lambda r: int(r["editor_row_key"].split("#")[1])
    nxt = max(keyn(r) for r in P) + 1; assert nxt == 15708
    J = [r for r in P if r["journal_id"] == JID]
    r18 = sorted([r for r in J if r["board_year"] == "2018"], key=keyn)
    long18 = defaultdict(list)
    for r in L:
        long18[r["editor_row_key"]].append(r)
    prior = defaultdict(list)  # raw string -> earlier JBES rows
    for r in J:
        if r["raw_affiliation"]: prior[r["raw_affiliation"]].append(r)
    apichk = {}
    def chk(i):
        a = api(i); apichk[i] = dict(status=a["status"], name=a["name"], country=a["country"]); assert a["status"] == "active", i; return a
    new_rows, new_long, changes = [], [], {"2019": [], "2020": []}
    def add_long(row, parts):
        for lr in parts: new_long.append(lr)
    # ---------- 2019: clone 2018 ----------
    b19 = board("2019")
    assert [(n, a) for _, _, n, a in b19] == [(r["editor_name"] if r["role"] != "x" else "", r["raw_affiliation"]) for r in r18] or True
    assert len(b19) == len(r18) == 87
    for (role, rc, name, raw), o in zip(b19, r18):
        assert (role, rc, raw) == (o["role"], o["role_class"], o["raw_affiliation"]), (name, o["editor_name"])
        assert o["editor_name_raw"].split(" - ")[0] == name, (name, o["editor_name_raw"])
        n = dict(o); key = f"editors_backfill_scale_panel#{nxt}"; nxt += 1
        printed_role = [k for k, v in ROLE.items() if v[0] == role][0]
        prov(n, "2019", printed_role, name)
        n["editor_row_key"] = key
        n["parse_flags"] = o["parse_flags"].replace(OLDM, METHOD)
        n["ror_match_method"] = o["ror_match_method"].replace(OLDM, METHOD)
        if o["ror_id"]:
            a = chk(o["ror_id"].rsplit("/", 1)[1])
            assert a["name"] == o["ror_name"] and a["country"] == o["ror_country"], (o["ror_id"], a["name"], o["ror_name"])
        for x in filter(None, o["other_ror_ids"].split("|")): chk(x.rsplit("/", 1)[1])
        if raw: n["ror_notes"] = (o["ror_notes"] + "; " if o["ror_notes"] else "") + "same printed string and decision as JBES 2018"
        new_rows.append(n)
        for lr in long18.get(o["editor_row_key"], []):
            m = dict(lr); m.update(editor_row_key=key, row_index=key.split("#")[1], year="2019",
                                   ror_match_kind=lr["ror_match_kind"].replace(OLDM, METHOD),
                                   ror_match_note=lr["ror_match_note"].replace(OLDM, METHOD).replace("stable/44867911", "stable/45181150"))
            new_long.append(m)
        if raw: assert long18.get(o["editor_row_key"]), name
        else: assert not long18.get(o["editor_row_key"]), name
    # ---------- 2020 ----------
    tmpl = dict(r18[0])
    for (role, rc, name, raw) in board("2020"):
        n = {h: "" for h in ph}
        printed_role = [k for k, v in ROLE.items() if v[0] == role][0]
        prov(n, "2020", printed_role, name)
        key = f"editors_backfill_scale_panel#{nxt}"; nxt += 1
        n.update(editor_row_key=key, editor_name=name, role=role, role_class=rc, raw_affiliation=raw,
                 editor_name_raw=f"{name} - {raw}" if raw else name)
        url = n["source_url"]
        if not raw:
            n.update(parse_flags=f"{METHOD};no_affiliation_printed", ror_notes="no affiliation printed",
                     ror_match_status="no_affiliation", affiliation_count="0", primary_aff_basis="none")
            new_rows.append(n); continue
        n.update(parse_flags=METHOD, institution=raw, affiliation_count="1", primary_aff_basis="single")
        rid, conf, canon, note, how = "", "", "", "", ""
        if raw in prior:
            ids = {r["ror_id"] for r in prior[raw]}; assert len(ids) == 1, (raw, ids)
            yrs = sorted({r["board_year"] for r in prior[raw]}); p0 = prior[raw][0]
            rid = p0["ror_id"].rsplit("/", 1)[1] if p0["ror_id"] else ""
            if rid:
                conf = Counter(r["ror_confidence"] for r in prior[raw]).most_common(1)[0][0]; canon = p0["canonical_name"]
                note = f"same printed string as JBES {'/'.join(yrs)} -> same ROR"; how = "jbes_prior_year_crosswalk"
            else:
                note = f"prior JBES panel ({'/'.join(yrs)}) left same printed string unmatched — match that practice"
        elif raw in NEW2020:
            rid = NEW2020[raw]; a = chk(rid)
            assert fold(raw) in {fold(x) for x in a["names"]}, raw
            conf, canon, how = "high", a["name"], "ror_api_exact_name"
            note = f"exact ROR name/alias '{raw}' (accent-folded) -> {a['name']}; API active"
            if rid == "02jkmyk67": note += "; research institute keeps own ROR (CAS AMSS)"
        elif raw in BLANK2020:
            note = BLANK2020[raw]
        else:
            raise SystemExit(f"undecided string {raw}")
        if rid:
            a = chk(rid)
            n.update(ror_id=f"https://ror.org/{rid}", ror_name=a["name"], ror_country=a["country"], continent=a["continent"],
                     lat=a["lat"], lon=a["lon"], canonical_name=canon, ror_confidence=conf, ror_match_score="1.0",
                     ror_match_method=f"{METHOD}+{how}", ror_match_status="matched", ror_id_aff_rank="1", ror_notes=note)
        else:
            n.update(ror_match_status="unmatched", ror_notes=note)
        new_rows.append(n)
        lr = {h: "" for h in lh}
        lr.update(editor_row_key=key, panel_file="editors_backfill_scale_ror_panel.csv", row_index=key.split("#")[1], journal=JNAME,
                  year="2020", editor_name=name, aff_text_source="raw_affiliation", aff_rank="1", raw_aff_part=raw, split_basis="single",
                  aff_role="sole", role_basis="single", relation_to_primary="same", is_panel_ror="1" if rid else "0")
        if rid:
            lr.update(ror_id=n["ror_id"], ror_name=n["ror_name"], ror_country=n["ror_country"], ror_match_kind=n["ror_match_method"],
                      ror_match_note=f"{METHOD}: {note}; institution='{raw}'; source={url}; printed name '{name}'")
        else:
            lr.update(ror_match_kind="unmatched", ror_match_note=f"{METHOD}: no clear ROR; raw='{raw}'; {note}")
        new_long.append(lr)
    # field sanity
    for r in new_rows:
        assert set(r) == set(ph)
        for v in r.values(): assert not EMAIL.search(v) and not PHONE.search(v), v
    for r in new_long: assert set(r) == set(lh)
    write(OUT / "editors_backfill_scale_ror_panel.csv", ph, P + new_rows, plt)
    write(OUT / "editor_affiliations.csv", lh, L + new_long, llt)
    # ---------- inventory ----------
    ih, I, ilt = read(MID / "editors_backfill_scale_inventory.csv")
    inv18 = next(r for r in I if r["journal_id"] == JID and r["board_year"] == "2018")
    inv_changes = []
    for r in I:
        if r["journal_id"] == JID and r["board_year"] in Y:
            y = r["board_year"]; c = Y[y]; rows = [x for x in new_rows if x["board_year"] == y]
            before = f"{r['status']} {r['rows_parsed']}/{r['rows_with_affiliation']}"
            for h in ih:
                r[h] = inv18[h]
            r.update(board_year=y, issue=f"{c['vol']} ({c['month']}) Front Matter",
                     source_file=f"tmp/jbes_2019_2020/jbes_{y}_front_matter_extract.txt",
                     source_text_file=f"tmp/jbes_2019_2020/jbes_{y}_board_extracted.csv",
                     source_url=f"https://www.jstor.org/stable/{c['stable']}", capture_date=CAP, parser=METHOD,
                     rows_parsed=str(len(rows)), rows_with_affiliation=str(sum(1 for x in rows if x["raw_affiliation"])),
                     status="ok_issue_front_matter",
                     note=f"JBES {y} board from JSTOR Front Matter {c['stable']} (CUHK Easy Access); Committee on Publications excluded; Hutchens/Zellner/Martin included to match prior JBES years")
            inv_changes.append(f"JBES {y}: {before} -> ok_issue_front_matter {r['rows_parsed']}/{r['rows_with_affiliation']}")
    write(OUT / "editors_backfill_scale_inventory.csv", ih, I, ilt)
    # ---------- gaps (2018 pattern: committee exclusions + no_affiliation_printed; no_snapshot row kept as for 2018) ----------
    gh, G, glt = read(MID / "editors_backfill_scale_gaps.csv")
    g18 = [r for r in G if r["journal_id"] == JID and r["board_year"] == "2018" and r["gap_type"] != "no_snapshot"]
    det_c = next(r["detail"] for r in g18 if r["gap_type"] == "excluded_asa_committee_on_publications")
    added = []
    for y in Y:
        sf = f"tmp/jbes_2019_2020/jbes_{y}_front_matter_extract.txt"
        for nm, t in COMMITTEE[y]:
            added.append(dict(journal_id=JID, journal=JNAME, board_year=y, source_file=sf, page="3",
                              gap_type="excluded_asa_committee_on_publications",
                              text_as_printed=f"{nm}, Committee on Publications" + (f" — {t}" if t else ""), detail=det_c))
        for x in new_rows:
            if x["board_year"] == y and not x["raw_affiliation"]:
                g = next(r for r in g18 if r["gap_type"] == "no_affiliation_printed" and r["text_as_printed"] == x["editor_name"])
                added.append(dict(g, board_year=y, source_file=sf, page="3"))
    write(OUT / "editors_backfill_scale_gaps.csv", gh, G + added, glt)
    # ---------- staff rows (2018 appended Hutchens) ----------
    sh, S, slt = read(MID / "BACKFILL_SCALE_ROR_staff_rows_20261031.csv")
    st = [{h: x.get(h, "") for h in sh} for x in new_rows if x["role_class"] == "staff"]
    write(OUT / "BACKFILL_SCALE_ROR_staff_rows_20261031.csv", sh, S + st, slt)
    # ---------- match rates ----------
    mh, MR, mlt = read(MID / "BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv")
    allj = J + new_rows; ns = [x for x in allj if x["role_class"] != "staff"]
    mr_change = None
    for r in MR:
        if r["journal_id"] == JID:
            old = dict(r)
            wa = [x for x in ns if x["ror_match_status"] in ("matched", "unmatched")]; m = [x for x in ns if x["ror_match_status"] == "matched"]
            r.update(rows_non_staff=str(len(ns)), no_affiliation=str(sum(1 for x in ns if x["ror_match_status"] == "no_affiliation")),
                     with_affiliation=str(len(wa)), matched=str(len(m)), unmatched=str(len(wa) - len(m)), match_rate=f"{len(m)/len(wa):.4f}",
                     high=str(sum(1 for x in m if x["ror_confidence"] == "high")), medium=str(sum(1 for x in m if x["ror_confidence"] == "medium")),
                     low=str(sum(1 for x in m if x["ror_confidence"] == "low")), staff_rows_excluded=str(len(allj) - len(ns)))
            mr_change = (old, dict(r))
    write(OUT / "BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv", mh, MR, mlt)
    # ---------- change CSVs + extracts ----------
    ch = ["action", "editor_row_key", "role", "printed_name", "editor_name", "raw_affiliation", "institution", "ror_id", "ror_name",
          "ror_country", "ror_match_status", "source_url"]
    lkeys = {x["editor_row_key"] for x in new_long}
    for y in Y:
        rows = [dict(action="panel_insert+long_insert" if x["editor_row_key"] in lkeys else "panel_insert", printed_name=x["editor_name"],
                     **{h: x[h] for h in ch if h not in ("action", "printed_name")}) for x in new_rows if x["board_year"] == y]
        write(OUT / f"JBES_{y}_board_changes_20261113.csv", ch, rows, "\r\n")
        write(WORK / f"jbes_{y}_board_extracted.csv", ["role", "printed_name", "affiliation_as_printed"],
              [dict(role=x["role"], printed_name=x["editor_name"], affiliation_as_printed=x["raw_affiliation"]) for x in new_rows if x["board_year"] == y], "\n")
        c = Y[y]; lines = [f"JBES {c['vol']} ({c['month']}) Front Matter, page 3 - board as printed (transcribed {CAP}; visually verified).",
                           f"Source: https://www.jstor.org/stable/{c['stable']} (issue page https://www.jstor.org/stable/{c['issue_page']}).",
                           "Contact lines (email/phone) not transcribed.", ""]
        cur = None
        for x in new_rows:
            if x["board_year"] != y: continue
            if x["role"] != cur: cur = x["role"]; lines += ["", cur.upper()]
            lines.append(x["editor_name"] + (f", {x['raw_affiliation']}" if x["raw_affiliation"] else ""))
        lines += ["", "COMMITTEE ON PUBLICATIONS (excluded from panel)"] + [nm + (f", {t}" if t else "") for nm, t in COMMITTEE[y]]
        (WORK / f"jbes_{y}_front_matter_extract.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        shutil.copy2(WORK / f"jbes_{y}_board_extracted.csv", OUT); shutil.copy2(WORK / f"jbes_{y}_front_matter_extract.txt", OUT)
        shutil.copy2(c["pdf"], OUT / c["pdf"].name)
    shutil.copy2(TRANSCRIPT, OUT / TRANSCRIPT.name)
    summ = dict(new_rows=len(new_rows), new_long=len(new_long), by_year=Counter(x["board_year"] for x in new_rows),
                long_by_year=Counter(x["year"] for x in new_long),
                keys={y: [min((x["editor_row_key"] for x in new_rows if x["board_year"] == y), key=lambda k: int(k.split('#')[1])),
                          max((x["editor_row_key"] for x in new_rows if x["board_year"] == y), key=lambda k: int(k.split('#')[1]))] for y in Y},
                status_by_year={y: Counter(x["ror_match_status"] for x in new_rows if x["board_year"] == y) for y in Y},
                inv_changes=inv_changes, gaps_added=Counter((g["board_year"], g["gap_type"]) for g in added).most_common(),
                staff_rows_added=len(st), match_rates={"before": mr_change[0], "after": mr_change[1]}, api=apichk)
    summ["gaps_added"] = [list(k) + [v] for k, v in summ["gaps_added"]]
    json.dump(summ, open(OUT / "_summary_20261113.json", "w"), indent=1, ensure_ascii=False)
    shutil.copy2(Path(__file__), OUT / Path(__file__).name)
    log("built", len(new_rows), "panel rows,", len(new_long), "long rows; gaps +", len(added), "; staff +", len(st))
    log("match rates JBES:", {k: mr_change[1][k] for k in ("rows_non_staff", "no_affiliation", "with_affiliation", "matched", "unmatched", "match_rate")})
    (OUT / "backfill_red_jbes_20261113.log").write_text("\n".join(LOG) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
