#!/usr/bin/env python3
"""Backfill pack editors_backfill_red_gap_20261112 on the live core49 backfill
editors_ra_ta_merge_rebuild_20261112 (web main 59652942; files taken from the web copy, incl. the scrubbed spotcheck).
1. RED 2022 + RED 2023 boards from the official Society for Economic Dynamics "Our Editors" page via Wayback
   (page version modified 2021-04-14, live in captures 2022-02-19 and 2022-06-29 -> board_year 2022;
    version modified 2023-02-21, live in captures 2023-03-24 .. 2023-12-11 -> board_year 2023).
   New keys continue after #15577. Street lines, emails, phones dropped. ROR from existing backfill canonical usage,
   API-verified (active; name + country fit). Blank ROR when no institution is printed.
2. Inventory: RED 2021 row status fixed (filled, rows_parsed 45); RED 2022/2023 rows filled. No other inventory cells touched.
3. Gaps: RED 2021/2022/2023 gap rows marked resolved (cells only; no row-count change).
Not published."""
import csv, json, re, sys, shutil, hashlib, unicodedata
from pathlib import Path
from collections import Counter
sys.path.insert(0, "/workspace/econ-journal-editors/tmp/red_gap_20261112")
from parse_sed import parse
from extract import orgs, clean
BASE = Path("/tmp/backfill_live")
OUT = Path("/workspace/econ-journal-editors/releases/editors_backfill_red_gap_20261112")
SRC = Path("/workspace/econ-journal-editors/tmp/red_gap_20261112")
API = Path("/tmp/fr/api")
METHOD = "red_gap_20261112"; NOW = "2026-11-12T23:30:00+08:00"; CAP = "2026-11-12"
PAGE = "https://www.economicdynamics.org/editors/"
YEARS = {
    "2022": dict(snap="20220219234913", modified="2021-04-14", also=["20220629190402"]),
    "2023": dict(snap="20230324123429", modified="2023-02-21", also=["20231211221936"]),
}
INST = [  # (regex on org lines, canonical, ror)
    (r"University of Minnesota", "University of Minnesota", "017zqws13"),
    (r"Federal Reserve Bank of Minneapolis", "Federal Reserve Bank of Minneapolis", "0380n5h16"),
    (r"Northwestern University", "Northwestern University", "000e0be47"),
    (r"Queen Mary University of London", "Queen Mary University of London", "026zzn846"),
    (r"Federal Reserve Board", "Board of Governors of the Federal Reserve System", "00v448643"),
    (r"University of California, San Diego", "University of California, San Diego", "0168r3w48"),
    (r"University of Toronto", "University of Toronto", "03dbr7087"),
    (r"^CREI$", "Centre de Recerca en Economia Internacional", "0241avf06"),
    (r"Federal Reserve Bank of New York", "Federal Reserve Bank of New York", "05hwvzg47"),
    (r"University of California, Los Angeles|UCLA Anderson", "University of California, Los Angeles", "046rm7j60"),
    (r"New York University|NYU Stern", "New York University", "0190ak572"),
    (r"Arizona State University", "Arizona State University", "03efmqc40"),
    (r"University of Pittsburgh", "University of Pittsburgh", "01an3r305"),
    (r"Stony Brook University", "Stony Brook University", "05qghxh33"),
    (r"University of Rochester", "University of Rochester", "022kthw22"),
    (r"Duke University", "Duke University", "00py81415"),
    (r"University College London", "University College London", "02jx3x895"),
    (r"Columbia University", "Columbia University", "00hj8s172"),
    (r"University of Western Ontario", "University of Western Ontario", "02grkyz14"),
    (r"Einaudi Institute for Economics and Finance", "Einaudi Institute for Economics and Finance", "04e874t64"),
    (r"Federal Reserve Bank of St\. Louis", "Federal Reserve Bank of St. Louis", "02skhjj30"),
    (r"Federal Reserve Bank of Philadelphia", "Federal Reserve Bank of Philadelphia", "02gsb6172"),
    (r"Wisconsin\s*[–-]\s*Madison", "University of Wisconsin–Madison", "01y2jtd41"),
    (r"Carnegie Mellon University", "Carnegie Mellon University", "05x2bcf33"),
    (r"Ohio State\s*University", "The Ohio State University", "00rs6vg23"),
    (r"Stanford University", "Stanford University", "00f54p054"),
    (r"Goethe University Frankfurt", "Goethe University Frankfurt", "04cvxnb49"),
    (r"Brandeis University", "Brandeis University", "05abbep66"),
    (r"Yale University", "Yale University", "03v76x132"),
    (r"Princeton University", "Princeton University", "00hx57361"),
    (r"University of Pennsylvania", "University of Pennsylvania", "00b30xv10"),
]
ROLE_CLASS = {"Coordinating Editor": "editor", "Editor": "editor", "Associate Editor": "board", "Editorial Advisory Board": "advisory"}
EM = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"); PH = re.compile(r"\+?\d[\d\s().\-]{8,}\d")


def api(i):
    d = json.load(open(API / f"{i}.json"))
    loc = d["locations"][0]["geonames_details"]
    return dict(status=d["status"], names=[n["value"] for n in d["names"]],
                name=next(n["value"] for n in d["names"] if "ror_display" in n["types"]),
                country=loc["country_name"], continent=loc["continent_name"], lat=str(loc["lat"]), lon=str(loc["lng"]))


def fold(s): return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower())


def read(p):
    b = p.read_bytes(); lt = "\r\n" if b"\r\n" in b[:20000] else "\n"
    rd = csv.DictReader(open(p, encoding="utf-8", newline="")); return rd.fieldnames, list(rd), lt


def write(p, hdr, rows, lt):
    with open(p, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=hdr, lineterminator=lt); w.writeheader(); w.writerows(rows)


def city_line(addr):
    last = clean(addr[-1]) if addr else ""
    last = PH.sub("", EM.sub("", last)).strip(" ,;")
    last = re.sub(r"^\d+[^,]*,\s*", "", last)  # street number line merged with city
    return re.sub(r"\s{2,}", " ", last).strip()


def main():
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir()
    for p in BASE.iterdir():
        if p.is_file(): shutil.copy2(p, OUT / p.name)
    ph, P, plt = read(BASE / "editors_backfill_scale_ror_panel.csv")
    lh, L, llt = read(BASE / "editor_affiliations.csv")
    nxt = max(int(r["editor_row_key"].split("#")[1]) for r in P) + 1
    assert nxt == 15578, nxt
    apichk, new_rows, new_long, report = {}, [], [], []
    for ror in {x[2] for x in INST}:
        a = api(ror); apichk[ror] = a
    for year, cfg in YEARS.items():
        snap = cfg["snap"]; arch = f"https://web.archive.org/web/{snap}/{PAGE}"
        blocks = parse(SRC / f"ed_{snap}.html")
        for b in blocks:
            name = b["name"].strip(); role = b["role"].strip()
            if role.lower().startswith("associate edit"): role = "Associate Editor"
            ol = orgs(b["addr"]); ol = [re.sub(r",?\s*\d+ [^,]*(?:Ave|Street|St\.)[^,]*,.*$", "", o) for o in ol if not re.fullmatch(r"Stanford CA,?", o)]
            city = city_line(b["addr"])
            raw = ", ".join(ol + ([city] if city and city not in ol else []))
            assert not EM.search(raw) and not PH.search(raw), raw
            hit = None
            for rx, canon, ror in INST:
                if any(re.search(rx, o) for o in ol): hit = (canon, ror); break
            flags = ["street_lines_dropped", METHOD]
            if b["section"] == "Editors" and role == "Associate Editor": flags.append("listed_under_Editors_heading")
            r = {c: "" for c in ph}
            k = f"editors_backfill_scale_panel#{nxt}"; nxt += 1
            note = (f"RED editors list on the Society for Economic Dynamics site ({PAGE}), Wayback snapshot {snap}; page version "
                    f"modified {cfg['modified']} and live in captures {', '.join([snap] + cfg['also'])}, used for board_year {year}; "
                    f"role as printed '{b['role'].strip()}'; name as printed ('{name}'); street address, email and phone lines dropped; method={METHOD}")
            r.update(journal_id="S163499366", journal="Review of Economic Dynamics", year=year, editor_name=name, editor_name_raw=name,
                     role=role, raw_affiliation=raw, affiliation_imputed="no", source_url=PAGE, collection_date=CAP,
                     data_source=f"wayback_snapshot_{year}", capture_timestamp=NOW, source_note=note,
                     board_urls=f"{PAGE}|{arch}", board_url_count="2", board_status="wayback_board_page",
                     snapshot_date=f"{snap[:4]}-{snap[4:6]}-{snap[6:8]}",
                     snapshot_source=f"SED RED editors page, Wayback snapshot {snap}; captured {CAP}", board_year=year, is_former="no",
                     source_file=f"tmp/red_gap_20261112/ed_{snap}.html", capture_date=CAP, name_style="full",
                     role_class=ROLE_CLASS[role], parse_flags=";".join(flags), editor_row_key=k, source_type="wayback",
                     issue=f"web page (Wayback {snap})", archive_url=arch, former_flag="0")
            if hit:
                canon, ror = hit; a = apichk[ror]
                r.update(institution=", ".join(ol), canonical_name=canon, ror_id="https://ror.org/" + ror, ror_name=a["name"],
                         ror_country=a["country"], continent=a["continent"], lat=a["lat"], lon=a["lon"],
                         ror_match_method=f"{METHOD}+backfill_canonical_crosswalk", ror_match_score="1.0", ror_confidence="high",
                         ror_notes=f"printed '{', '.join(ol)}' -> {canon}; ROR {ror} already used for this name in the backfill; API active ({a['name']}, {a['country']})",
                         ror_match_status="matched", affiliation_count="1", ror_id_aff_rank="1", primary_aff_basis="single")
            else:
                r.update(institution=", ".join(ol), ror_match_method=f"{METHOD}", ror_confidence="unmatched",
                         ror_notes="printed lines name a department only (no institution printed); ROR left blank, not inferred from street address",
                         ror_match_status="unmatched", affiliation_count="1" if raw else "0", primary_aff_basis="single" if raw else "none")
            new_rows.append(r)
            if raw:
                q = {c: "" for c in lh}
                q.update(editor_row_key=k, panel_file="editors_backfill_scale_ror_panel.csv", row_index=k.split("#")[1], journal=r["journal"],
                         year=year, editor_name=name, aff_text_source="raw_affiliation", aff_rank="1", raw_aff_part=raw, split_basis="single",
                         ror_id=r["ror_id"], ror_name=r["ror_name"], ror_country=r["ror_country"],
                         ror_match_kind=f"{METHOD}+backfill_canonical_crosswalk" if hit else "unmatched",
                         ror_match_note=f"{METHOD}: {r['ror_notes']}; source {arch}", aff_role="sole", role_basis="single",
                         relation_to_primary="same", is_panel_ror="1" if hit else "0")
                new_long.append(q)
            report.append(dict(year=year, key=k, name=name, role=role, raw=raw, ror=r["ror_id"], country=r["ror_country"]))
    write(OUT / "editors_backfill_scale_ror_panel.csv", ph, P + new_rows, plt)
    write(OUT / "editor_affiliations.csv", lh, L + new_long, llt)

    # inventory (cells only)
    ih, I, ilt = read(BASE / "editors_backfill_scale_inventory.csv")
    raw_inv = (BASE / "editors_backfill_scale_inventory.csv").read_bytes()
    inv_changes = []
    for r in I:
        if r["journal"] != "Review of Economic Dynamics": continue
        y = r["board_year"]; old = dict(r)
        if y == "2021":
            r.update(rows_parsed="45", rows_with_affiliation="45", parser="red_2021_board_20261106", status="ok_issue_front_matter",
                     note="RED 2021 board from ScienceDirect Vol 39 (2021-01) Editorial Board front matter (free PDF verified 2026-11-06); 45 rows on panel #15446-#15490; SED officers excluded (gaps); status fixed red_gap_20261112")
        elif y in YEARS:
            cfg = YEARS[y]; n = sum(1 for x in new_rows if x["board_year"] == y); na = sum(1 for x in new_rows if x["board_year"] == y and x["raw_affiliation"])
            ks = [x["editor_row_key"] for x in new_rows if x["board_year"] == y]
            r.update(source_type="wayback", capture_route="wayback_snapshot",
                     source_file=f"tmp/red_gap_20261112/ed_{cfg['snap']}.html", source_text_file="", source_url=PAGE,
                     archive_url=f"https://web.archive.org/web/{cfg['snap']}/{PAGE}", snapshot_timestamp=cfg["snap"], snapshot_year_offset="0",
                     capture_date=CAP, name_style="full", affiliations_present="yes", rows_parsed=str(n), rows_with_affiliation=str(na),
                     parser=f"tmp/red_gap_20261112/parse_sed.py ({METHOD})", status="ok_wayback",
                     note=f"SED 'Our Editors' page version modified {cfg['modified']}, live in Wayback captures {', '.join([cfg['snap']] + cfg['also'])}; issue front matter blocked from collector (ScienceDirect 403); {n} rows {ks[0]}-{ks[-1]}; {METHOD}")
        if r != old: inv_changes.append((y, {c: (old[c], r[c]) for c in ih if old[c] != r[c]}))
    write(OUT / "editors_backfill_scale_inventory.csv", ih, I, ilt)
    # gaps (cells only)
    gh, G, glt = read(BASE / "editors_backfill_scale_gaps.csv")
    gap_changes = []
    for r in G:
        if r["journal"] == "Review of Economic Dynamics" and r["board_year"] in ("2021", "2022", "2023") and r["gap_type"] in ("blocked", "queued"):
            old = dict(r)
            r["gap_type"] = "resolved"
            r["detail"] = (r["detail"] + f"; resolved {METHOD}: " +
                           ("issue front matter merged 2026-11-06 (45 rows)" if r["board_year"] == "2021" else "SED editors page via Wayback merged"))
            gap_changes.append((r["board_year"], old["gap_type"], r["detail"]))
    write(OUT / "editors_backfill_scale_gaps.csv", gh, G, glt)
    # match rates RED row
    mh, MR, mlt = read(BASE / "BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv")
    allp = P + new_rows
    red = [x for x in allp if x["journal"] == "Review of Economic Dynamics" and x["ror_match_status"] != "staff_excluded"]
    for r in MR:
        if r["journal"] == "Review of Economic Dynamics":
            wa = [x for x in red if x["ror_match_status"] in ("matched", "unmatched")]
            m = [x for x in red if x["ror_match_status"] == "matched"]
            r.update(rows_non_staff=str(len(red)), no_affiliation=str(sum(1 for x in red if x["ror_match_status"] == "no_affiliation")),
                     with_affiliation=str(len(wa)), matched=str(len(m)), unmatched=str(len(wa) - len(m)), match_rate=f"{len(m)/len(wa):.4f}",
                     high=str(sum(1 for x in m if x["ror_confidence"] == "high")), medium=str(sum(1 for x in m if x["ror_confidence"] == "medium")),
                     low=str(sum(1 for x in m if x["ror_confidence"] == "low")))
    write(OUT / "BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv", mh, MR, mlt)
    with open(OUT / "RED_2022_2023_board_changes_20261112.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(report[0]), lineterminator="\r\n"); w.writeheader(); w.writerows(report)
    json.dump(dict(api={k: dict(status=v["status"], name=v["name"], country=v["country"]) for k, v in apichk.items()},
                   new_rows=len(new_rows), new_long=len(new_long), by_year=Counter(x["board_year"] for x in new_rows),
                   unmatched=[(x["editor_row_key"], x["editor_name"], x["raw_affiliation"]) for x in new_rows if not x["ror_id"]],
                   inv_changes=inv_changes, gap_changes=gap_changes), open("/tmp/redgap/build_summary.json", "w"), indent=1, ensure_ascii=False)
    shutil.copy2(Path(__file__), OUT / Path(__file__).name)
    print("built", len(new_rows), len(new_long))


if __name__ == "__main__":
    main()
