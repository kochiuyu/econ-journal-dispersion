#!/usr/bin/env python3
"""Backfill freeze editors_backfill_red2024_20261114 (HELD, unpublished) on live core49 editors_backfill_ra_pack2_20261113 (PR #72).
Adds the RED 2024 board (whole-board gap; inventory 'queued') from the official journal-issued front matter:
Review of Economic Dynamics Vol 52 (2024-04), Editorial Board, page ii, DOI 10.1016/S1094-2025(24)00006-1,
ScienceDirect PII S1094202524000061 (captured via CUHK Easy Access 2 with user sign-in on 2026-11-14; proxy URL not recorded).
Conventions copied verbatim from RED 2025 (backfill_red_2025_20261113.py, itself following RED 2021 red_2021_board_20261106):
printed role headings, printed initials kept (except the 4 advisory-board expansions to prior RED full names, as in 2021/2025),
editor_name_raw = printed form, raw = printed address lines joined, SED society officers excluded and logged in gaps.
ROR: same institution->ROR map as RED 2025 (every id already in the backfill), re-verified live in the ROR v2 API (/tmp/red24api).
Every new row is cross-checked against the live RED 2025 row for the same person: identical except provenance fields.
No existing row is changed. Keys from #15873. The source PDF is NOT copied into the release folder."""
import csv, json, re, shutil, hashlib
from pathlib import Path
from collections import Counter
import pymupdf
ROOT = Path("/workspace/econ-journal-editors")
REL = ROOT / "releases"
BASE = REL / "editors_backfill_ra_pack2_20261113"
OUT = REL / "editors_backfill_red2024_20261114"
PDF = ROOT / "abs_ajg/reports/RED_2024_editorial_board.pdf"
TRANSCRIPT = ROOT / "abs_ajg/reports/RED_2024_board_source_20261114.md"
EXTRACT = ROOT / "tmp/red_2024_board_extracted.csv"
API = Path("/tmp/red24api")
METHOD = "red_2024_board_20261114"; NOW = "2026-11-14T09:30:00+08:00"; CAP = "2026-11-14"
URL = "https://www.sciencedirect.com/science/article/pii/S1094202524000061"
DOI = "10.1016/S1094-2025(24)00006-1"; ISSUE = "Vol 52 (2024-04)"
JID, JN = "S163499366", "Review of Economic Dynamics"
HEAD = {"CO-ORDINATING EDITOR": "editor", "EDITORS": "editor", "ASSOCIATE EDITORS": "board", "EDITORIAL ADVISORY BOARD": "advisory"}
EXPAND = {"T.F. Cooley": "Thomas F. Cooley", "B. Jovanovic": "Boyan Jovanovic", "E.C. Prescott": "Edward C. Prescott",
          "T.J. Sargent": "Thomas J. Sargent"}  # same 4 expansions as RED 2021/2025 (prior RED full names)
NAME_NORM = {"J. La\u2019O": "J. La'O"}  # RED 2021/2025 panel uses the straight apostrophe
INST = [  # identical to RED 2025 builder
    (r"^University of Minnesota( Twin Cities)?,", "017zqws13", "Twin Cities/Minneapolis campus record (not a system record)"),
    (r"^Federal Reserve Bank of Chicago", "03n7scr80", ""), (r"^Northwestern University", "000e0be47", ""),
    (r"^Queen Mary University of London", "026zzn846", ""), (r"^Board of Governors of the Federal Reserve System", "00v448643", ""),
    (r"^Boston University", "05qwgg493", ""), (r"^Centre for Research in International Economics", "0241avf06", "research centre keeps own ROR (CREI)"),
    (r"^Federal Reserve Bank New York", "05hwvzg47", ""), (r"^University of California Los Angeles", "046rm7j60", ""),
    (r"^University of Pittsburgh", "01an3r305", ""), (r"^Federal Reserve Bank of Minneapolis", "0380n5h16", ""),
    (r"^Stony Brook University", "05qghxh33", ""), (r"^University of Rochester", "022kthw22", ""), (r"^Duke University", "00py81415", ""),
    (r"^Arizona State University", "03efmqc40", ""), (r"^Brandeis University", "05abbep66", ""),
    (r"^Pompeu Fabra University Department of Economics and Business", "04n0g0b29", "department has no own ROR -> parent UPF (school-unit rule)"),
    (r"^Columbia University", "00hj8s172", ""), (r"^Einaudi Institute for Economics and Finance", "04e874t64", "research institute keeps own ROR (EIEF)"),
    (r"^University College London", "02jx3x895", ""), (r"^Federal Reserve Bank of St Louis", "02skhjj30", ""),
    (r"^Federal Reserve Bank of Philadelphia", "02gsb6172", ""),
    (r"^The Pennsylvania State University, University Park", "04p491231", "University Park campus record, as printed"),
    (r"^Carnegie Mellon University", "05x2bcf33", ""), (r"^The Ohio State University", "00rs6vg23", ""), (r"^Stanford University", "00f54p054", ""),
    (r"^Goethe University Frankfurt", "04cvxnb49", ""),
    (r"^New York University Stern School of Business", "0190ak572", "Stern has no own ROR -> parent NYU (school-unit rule)"),
    (r"^New York University,", "0190ak572", ""), (r"^University of California San Diego", "0168r3w48", ""),
]
COUNTRIES = ("United States of America", "United Kingdom", "Spain", "Italy", "Germany")
EM = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"); PH = re.compile(r"\+?\d[\d\s().\-]{8,}\d")
DOCS = {"README.md", "HANDOFF.md", "RELEASE_NOTES.md", "_build.json", "SENDTO_BLURB.txt", "_summary_20261113.json", "_live_manifest_sha256.txt"}
# provenance fields that legitimately differ from the RED 2025 twin row
PROV = {"year", "source_url", "board_urls", "source_note", "capture_timestamp", "collection_date", "data_source", "snapshot_date",
        "snapshot_source", "board_year", "capture_date", "parse_flags", "ror_match_method", "ror_notes", "issue", "editor_row_key"}
LPROV = {"editor_row_key", "row_index", "year", "ror_match_kind", "ror_match_note"}
LOG = []
def log(*a): s = " ".join(str(x) for x in a); LOG.append(s); print(s)


def api(i):
    d = json.load(open(API / f"{i}.json")); loc = d["locations"][0]["geonames_details"]
    return dict(status=d["status"], name=next(n["value"] for n in d["names"] if "ror_display" in n["types"]),
                country=loc["country_name"], continent=loc["continent_name"], lat=str(loc["lat"]), lon=str(loc["lng"]))


def read(p):
    b = p.read_bytes(); lt = "\r\n" if b"\r\n" in b[:20000] else "\n"
    rd = csv.DictReader(open(p, encoding="utf-8", newline="")); return rd.fieldnames, list(rd), lt


def write(p, hdr, rows, lt):
    with open(p, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=hdr, lineterminator=lt); w.writeheader(); w.writerows(rows)


def parse_pdf():  # identical to the RED 2025 parser
    pg = pymupdf.open(PDF)[0]
    blocks = [(b[0], b[1], b[4]) for b in pg.get_text("blocks")]
    heads = sorted((y, t.strip()) for x, y, t in blocks if t.strip() in HEAD)
    footer_y = min(y for x, y, t in blocks if t.startswith("The Review of Economic Dynamics is the"))
    def section(y): return [h for hy, h in heads if hy <= y][-1]
    names = [(x, y, t.strip()) for x, y, t in blocks if "\n" not in t.strip() and t.strip() not in HEAD and y < footer_y
             and not t.strip().startswith("The Review")]
    people = []
    for x, y, t in blocks:
        lines = [l.strip() for l in t.strip().split("\n")]
        if y < footer_y and len(lines) > 1 and section(y) == "CO-ORDINATING EDITOR":
            people.append(dict(section="CO-ORDINATING EDITOR", printed=lines[0], lines=lines[1:], x=x, y=y))
    for nx, ny, nm in names:
        if section(ny) == "CO-ORDINATING EDITOR": continue
        addr = [(x, y, t) for x, y, t in blocks if abs(x - (nx + 7)) < 2 and 0 < y - ny < 15]
        assert len(addr) == 1, (nm, addr)
        people.append(dict(section=section(ny), printed=nm, lines=[l.strip() for l in addr[0][2].strip().split("\n")], x=nx, y=ny))
    footer = [l.strip() for x, y, t in blocks if y > footer_y for l in t.strip().split("\n") if re.search(r", (President|Treasurer|Secretary)$", l.strip())]
    order = {h: i for i, h in enumerate(HEAD)}
    people.sort(key=lambda p: (order[p["section"]], round(p["x"]), p["y"]))
    return people, footer


def main():
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    base_manifest = "\n".join(f"{sha(f)}  {f.name}" for f in sorted(BASE.iterdir()) if f.is_file()) + "\n"
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / "_live_manifest_sha256.txt").write_text(base_manifest)
    for p in BASE.iterdir():
        if p.is_file() and p.name not in DOCS: shutil.copy2(p, OUT / p.name)  # scripts/logs of earlier freezes kept as in pack2
    people, footer = parse_pdf()
    assert len(people) == 44, len(people)
    assert Counter(p["section"] for p in people) == Counter({"CO-ORDINATING EDITOR": 1, "EDITORS": 9, "ASSOCIATE EDITORS": 30, "EDITORIAL ADVISORY BOARD": 4})
    assert footer == ["Ellen McGrattan, President", "Erwan Quintin, Treasurer", "Marina Azzimonti, Secretary"], footer
    ph, P, plt = read(BASE / "editors_backfill_scale_ror_panel.csv")
    lh, L, llt = read(BASE / "editor_affiliations.csv")
    assert len(P) == 15873 and len(L) == 12120, (len(P), len(L))
    assert not any(r["journal_id"] == JID and r["board_year"] == "2024" for r in P)
    nxt = max(int(r["editor_row_key"].split("#")[1]) for r in P) + 1
    assert nxt == 15873, nxt
    used = {r["ror_id"] for r in P if r["ror_id"]}
    apichk = {}
    for _rx, ror, _n in INST:
        a = api(ror); apichk[ror] = a
        assert a["status"] == "active", ror
        assert "https://ror.org/" + ror in used, ("ROR not already in backfill", ror)
    twin25 = [r for r in P if r["journal_id"] == JID and r["board_year"] == "2025"]
    lk = {}
    for q in L: lk.setdefault(q["editor_row_key"], []).append(q)
    assert len(twin25) == 44
    new_rows, new_long, report, extract = [], [], [], []
    for p, t in zip(people, twin25):
        printed = p["printed"]; name = EXPAND.get(printed, NAME_NORM.get(printed, printed))
        name_raw = NAME_NORM.get(printed, printed)
        raw = re.sub(r"\s{2,}", " ", " ".join(p["lines"])).strip()
        assert not EM.search(raw) and not PH.search(raw), raw
        segs = [s.strip() for s in raw.split(",")]
        country_txt = segs[-1] if segs[-1] in COUNTRIES else ""
        inst = ", ".join(segs[:-1]) if country_txt else raw
        ror, rnote = next(((ror, n) for rx, ror, n in INST if re.search(rx, raw)))
        a = apichk[ror]
        assert {"United States of America": "United States"}.get(country_txt, country_txt) == a["country"], (raw, a["country"])
        k = f"editors_backfill_scale_panel#{nxt}"; nxt += 1
        notes = [f"role as printed '{p['section']}'", f"name as printed on board ('{printed}')"]
        if printed in EXPAND: notes.append(f"name expanded to prior RED panel full name '{name}' (as in RED 2021/2025)")
        if printed in NAME_NORM: notes.append("printed with a curly apostrophe (U+2019); stored with the straight apostrophe as on the RED 2021/2025 panel")
        if printed == "V. Venkateswaren":
            notes.append("printed spelling 'Venkateswaren' kept (visually confirmed on the PDF; same on RED 2025); prior RED years print 'V. Venkateswaran' at NYU Stern")
        src_note = (f"RED {ISSUE} issue front matter; printed issue board, captured {CAP}; source ScienceDirect Editorial Board PDF "
                    f"DOI {DOI} (page ii; retrieved via CUHK Easy Access 2 institutional sign-in on {CAP}); " + "; ".join(notes) + f"; method={METHOD}")
        r = {c: "" for c in ph}
        r.update(journal_id=JID, journal=JN, year="2024", editor_name=name, editor_name_raw=name_raw,
                 role=p["section"], raw_affiliation=raw, affiliation_imputed="no", source_url=URL, collection_date=CAP,
                 data_source="publisher_issue_pdf_2024", capture_timestamp=NOW, source_note=src_note, board_urls=URL, board_url_count="1",
                 board_status="issue_front_matter", snapshot_date=CAP,
                 snapshot_source=f"RED {ISSUE} issue front matter; printed issue board, captured {CAP}", board_year="2024", is_former="no",
                 capture_date=CAP, name_style="full" if (printed in EXPAND or not re.match(r"^([A-Z]\.-?)+[A-Z]?\.? ", printed)) else "initials",
                 role_class=HEAD[p["section"]], parse_flags=f"address_lines_joined;{METHOD}", institution=inst,
                 canonical_name=a["name"], ror_id="https://ror.org/" + ror, ror_name=a["name"], ror_country=a["country"],
                 continent=a["continent"], lat=a["lat"], lon=a["lon"], ror_match_method=f"{METHOD}+backfill_canonical_crosswalk",
                 ror_match_score="1.0", ror_confidence="high",
                 ror_notes=(f"printed '{inst}' -> {a['name']} (canonical = ROR display name); ROR {ror} already used in the backfill (same string on RED 2025); "
                            f"API active, re-checked {CAP} ({a['name']}, {a['country']})" + (f"; {rnote}" if rnote else "") + f" ({METHOD})"),
                 ror_match_status="matched", editor_row_key=k, affiliation_count="1", source_type="official_issue", issue=ISSUE,
                 ror_id_aff_rank="1", primary_aff_basis="single", former_flag="0")
        diff = {c for c in ph if r[c] != t[c]} - PROV
        assert not diff, (printed, {c: (t[c], r[c]) for c in diff})
        new_rows.append(r)
        q = {c: "" for c in lh}
        q.update(editor_row_key=k, panel_file="editors_backfill_scale_ror_panel.csv", row_index=k.split("#")[1], journal=JN,
                 year="2024", editor_name=name, aff_text_source="raw_affiliation", aff_rank="1", raw_aff_part=raw, split_basis="single",
                 ror_id=r["ror_id"], ror_name=r["ror_name"], ror_country=r["ror_country"], ror_match_kind=f"{METHOD}+panel_crosswalk",
                 ror_match_note=(f"{METHOD}: ROR from unambiguous existing backfill crosswalk (same string on RED 2025); institution='{inst}'; source={URL}; DOI {DOI}; "
                                 f"printed name '{printed}'" + ("; printed spelling kept" if printed == "V. Venkateswaren" else "")),
                 aff_role="sole", role_basis="single", relation_to_primary="same", is_panel_ror="1")
        tl = lk[t["editor_row_key"]]; assert len(tl) == 1
        ld = {c for c in lh if q[c] != tl[0][c]} - LPROV
        assert not ld, (printed, ld)
        new_long.append(q)
        report.append(dict(action="panel_insert+long_insert", editor_row_key=k, role=p["section"], printed_name=printed, editor_name=name,
                           raw_affiliation=raw, institution=inst, ror_id=r["ror_id"], ror_name=a["name"], ror_country=a["country"],
                           name_expanded="yes" if printed in EXPAND else "no", source_url=URL, red_2025_twin_key=t["editor_row_key"]))
        extract.append(dict(role=p["section"], printed_name=printed, editor_name=name, raw_affiliation=raw, institution=inst,
                            ror_id=r["ror_id"], ror_name=a["name"], expanded_from_red_prior="yes" if printed in EXPAND else "no"))
    write(OUT / "editors_backfill_scale_ror_panel.csv", ph, P + new_rows, plt)
    write(OUT / "editor_affiliations.csv", lh, L + new_long, llt)
    write(EXTRACT, list(extract[0]), extract, "\n"); shutil.copy2(EXTRACT, OUT / EXTRACT.name)
    # inventory: RED 2024 row only
    ih, I, ilt = read(BASE / "editors_backfill_scale_inventory.csv"); inv_changes = []
    for r in I:
        if r["journal_id"] == JID and r["board_year"] == "2024":
            old = dict(r)
            assert r["issue"] == ISSUE and r["source_url"] == URL and r["status"] == "queued"
            r.update(source_type="official_issue", capture_route="publisher_pdf_capture_institutional",
                     source_file="abs_ajg/reports/RED_2024_editorial_board.pdf", source_text_file="tmp/red_2024_board_extracted.csv",
                     snapshot_year_offset="0", capture_date=CAP, name_style="mixed_initials_full", affiliations_present="yes",
                     rows_parsed=str(len(new_rows)), rows_with_affiliation=str(sum(1 for x in new_rows if x["raw_affiliation"])),
                     parser=METHOD, status="ok_issue_front_matter",
                     note=(f"RED 2024 board from ScienceDirect {ISSUE} Editorial Board front matter (page ii, DOI {DOI}; retrieved via CUHK Easy Access 2 "
                           f"institutional sign-in on {CAP}); {len(new_rows)} rows on panel {new_rows[0]['editor_row_key'].split('#')[1]}-"
                           f"{new_rows[-1]['editor_row_key'].split('#')[1]}; SED officers excluded (gaps); {METHOD}"))
            inv_changes.append({c: (old[c], r[c]) for c in ih if old[c] != r[c]})
    assert len(inv_changes) == 1
    write(OUT / "editors_backfill_scale_inventory.csv", ih, I, ilt)
    # gaps: RED 2024 queued -> resolved; append the 3 society-officer exclusion lines (as for 2018-2021, 2025)
    gh, G, glt = read(BASE / "editors_backfill_scale_gaps.csv"); gap_changes = []
    for r in G:
        if r["journal_id"] == JID and r["board_year"] == "2024" and r["gap_type"] == "queued":
            gap_changes.append(("2024", r["gap_type"], "resolved"))
            r["gap_type"] = "resolved"; r["detail"] += f"; resolved {METHOD}: issue front matter merged {CAP} ({len(new_rows)} rows)"
    assert len(gap_changes) == 1
    added_gaps = []
    for line in footer:
        g = {c: "" for c in gh}
        g.update(journal_id=JID, journal=JN, board_year="2024", source_file="abs_ajg/reports/RED_2024_editorial_board.pdf",
                 gap_type="excluded_sed_society_officer_line_excluded", text_as_printed=line, detail="line excluded (not a board member)")
        added_gaps.append(g)
    # insert after the last RED 2024 gap line? keep append-only like RED 2025
    write(OUT / "editors_backfill_scale_gaps.csv", gh, G + added_gaps, glt)
    # match rates: RED row recount
    mh, MR, mlt = read(BASE / "BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv"); mr = None
    red = [x for x in P + new_rows if x["journal_id"] == JID and x["ror_match_status"] != "staff_excluded"]
    for r in MR:
        if r["journal_id"] == JID:
            before = dict(r)
            wa = [x for x in red if x["ror_match_status"] in ("matched", "unmatched")]; m = [x for x in red if x["ror_match_status"] == "matched"]
            r.update(rows_non_staff=str(len(red)), no_affiliation=str(sum(1 for x in red if x["ror_match_status"] == "no_affiliation")),
                     with_affiliation=str(len(wa)), matched=str(len(m)), unmatched=str(len(wa) - len(m)), match_rate=f"{len(m)/len(wa):.4f}",
                     high=str(sum(1 for x in m if x["ror_confidence"] == "high")), medium=str(sum(1 for x in m if x["ror_confidence"] == "medium")),
                     low=str(sum(1 for x in m if x["ror_confidence"] == "low")))
            mr = (before, dict(r))
    write(OUT / "BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv", mh, MR, mlt)
    cols = [c for c in mh if c not in ("journal_id",)]
    mrc = {"journal": JN}
    for suf, d in (("before", mr[0]), ("after", mr[1])):
        for c in cols[1:]: mrc[f"{c}_{suf}"] = d[c]
    write(OUT / "RED_2024_match_rate_changes_20261114.csv", list(mrc), [mrc], "\r\n")
    write(OUT / "RED_2024_board_changes_20261114.csv", list(report[0]), report, "\r\n")
    shutil.copy2(TRANSCRIPT, OUT / TRANSCRIPT.name)
    summ = dict(api=apichk, new_rows=len(new_rows), new_long=len(new_long), totals=dict(panel=len(P) + len(new_rows), long=len(L) + len(new_long)),
                by_role=Counter(x["role"] for x in new_rows), by_role_class=Counter(x["role_class"] for x in new_rows),
                keys=[new_rows[0]["editor_row_key"], new_rows[-1]["editor_row_key"]], ror_matched=sum(1 for x in new_rows if x["ror_id"]),
                ror_blank=[x["raw_affiliation"] for x in new_rows if not x["ror_id"]], footer_excluded=footer,
                inv_changes=inv_changes, gap_changes=gap_changes, gaps_added=len(added_gaps), match_rates={"before": mr[0], "after": mr[1]},
                ror_new_to_backfill=sorted({x["ror_id"] for x in new_rows if x["ror_id"]} - used))
    json.dump(summ, open(OUT / "_summary_20261114.json", "w"), indent=1, ensure_ascii=False)
    shutil.copy2(Path(__file__), OUT / Path(__file__).name)
    log("built", len(new_rows), "panel rows,", len(new_long), "long rows; totals", summ["totals"])
    log("roles", dict(summ["by_role"])); log("match rate RED", mr[0]["match_rate"], "->", mr[1]["match_rate"])
    (OUT / "backfill_red2024_20261114.log").write_text("\n".join(LOG) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
