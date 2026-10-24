#!/usr/bin/env python3
"""Build site/rankings-data.js from the pinned ABS/AJG freeze.

Source is journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/.
Grades and journal_id values are copied from that freeze. This script does
not fetch CABS, does not read portal extracts, and does not assign ratings
or ids of its own.
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "site"
DATA_JS = SITE_DIR / "rankings-data.js"
FREEZE_ID = "rankings_abs_ajg_20261024"
RELEASE = ROOT / "journals/rankings/abs_ajg/releases" / FREEZE_ID

# Keep these three in sync with scripts/build_site.py.
PAGES_BASE = "/econ-journal-dispersion/"
REPO_URL = "https://github.com/kochiuyu/econ-journal-dispersion"
LIVE_URL = "https://kochiuyu.github.io/econ-journal-dispersion/"

EDITIONS = (2010, 2015, 2018, 2021, 2024)
GRADE_COLUMNS = (
    "edition_year",
    "rating",
    "rating_raw",
    "journal_title",
    "print_issn",
    "e_issn",
    "field",
    "publisher",
    "journal_id",
    "catalog",
    "match_method",
    "source_file",
    "source_note",
)
NOTE_FOR_YEAR = {
    2010: "ABS2010",
    2015: "AJG2015",
    2018: "AJG2018",
    2021: "AJG2021",
    2024: "AJG2024",
}
# Locked to RELEASE_NOTES.md in the freeze. rows, with journal_id, match percent.
EXPECTED = {
    2010: {"rows": 794, "mapped": 721, "match_pct": 90.8},
    2015: {"rows": 1377, "mapped": 1120, "match_pct": 81.3},
    2018: {"rows": 1545, "mapped": 1231, "match_pct": 79.7},
    2021: {"rows": 1706, "mapped": 1317, "match_pct": 77.2},
    2024: {"rows": 1823, "mapped": 1378, "match_pct": 75.6},
}
ALLOWED_RATINGS = {"4*", "4", "3", "2", "1"}
ALLOWED_METHODS = {"issn", "title", "unmatched"}
ALLOWED_SOURCES = {"ajg_2024.csv", "ajg_2021.csv"}
# Display names for the field codes stored on the freeze. Not a second rating.
SUBJECT_LABELS = {
    "ACCOUNT": "Accounting",
    "BUS HIST & ECON HIST": "Business and Economic History",
    "ECON": "Economics, Econometrics and Statistics",
    "ENT-SBM": "Entrepreneurship and Small Business Management",
    "ETHICS-CSR-MAN": "General Management, Ethics, Gender and Social Responsibility",
    "FINANCE": "Finance",
    "HRM&EMP": "Human Resource Management and Employment Studies",
    "IB&AREA": "International Business and Area Studies",
    "INFO MAN": "Information Management",
    "INNOV": "Innovation",
    "MDEV&EDU": "Management Development and Education",
    "MKT": "Marketing",
    "OPS&TECH": "Operations and Technology Management",
    "OR&MANSCI": "Operations Research and Management Science",
    "ORG STUD": "Organisation Studies",
    "PSYCH (GENERAL)": "Psychology (General)",
    "PSYCH (WOP-OB)": "Psychology (Organisational)",
    "PUB SEC": "Public Sector and Health Care",
    "REGIONAL STUDIES, PLANNING AND ENVIRONMENT": "Regional Studies, Planning and Environment",
    "SECTOR": "Sector Studies",
    "SOC SCI": "Social Sciences",
    "STRAT": "Strategy",
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.exists():
        raise SystemExit(f"Missing freeze file: {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        header = list(reader.fieldnames or [])
        return header, list(reader)


def row_key(row: dict[str, str]) -> tuple[str, ...]:
    return tuple(row[column] for column in GRADE_COLUMNS)


def validate(loaded: dict[int, list[dict[str, str]]], long_rows: list[dict[str, str]]) -> None:
    stacked: list[dict[str, str]] = []
    for year in EDITIONS:
        rows = loaded[year]
        expect = EXPECTED[year]
        mapped = 0
        for row in rows:
            if row["edition_year"] != str(year):
                raise SystemExit(f"{year}: edition_year {row['edition_year']!r} on {row['journal_title']}")
            if row["rating"] not in ALLOWED_RATINGS or row["rating_raw"] not in ALLOWED_RATINGS:
                raise SystemExit(f"{year}: rating {row['rating']!r}/{row['rating_raw']!r} on {row['journal_title']}")
            if row["rating"] != row["rating_raw"]:
                raise SystemExit(f"{year}: rating differs from rating_raw on {row['journal_title']}")
            if not row["journal_title"]:
                raise SystemExit(f"{year}: blank title")
            if row["field"] not in SUBJECT_LABELS:
                raise SystemExit(f"{year}: unknown field {row['field']!r}")
            if row["match_method"] not in ALLOWED_METHODS:
                raise SystemExit(f"{year}: match_method {row['match_method']!r}")
            if row["source_file"] not in ALLOWED_SOURCES:
                raise SystemExit(f"{year}: source_file {row['source_file']!r}")
            if row["source_note"] != NOTE_FOR_YEAR[year]:
                raise SystemExit(f"{year}: source_note {row['source_note']!r}")
            has_id = bool(row["journal_id"].strip())
            if row["match_method"] == "unmatched":
                if has_id or row["catalog"].strip():
                    raise SystemExit(f"{year}: unmatched row has an id: {row['journal_title']}")
            elif not has_id or not row["catalog"].strip():
                raise SystemExit(f"{year}: matched row missing id: {row['journal_title']}")
            else:
                mapped += 1
        if len(rows) != expect["rows"] or mapped != expect["mapped"]:
            raise SystemExit(f"{year}: {len(rows)} rows / {mapped} mapped, expected {expect['rows']} / {expect['mapped']}")
        pct = round(100 * mapped / len(rows), 1)
        if pct != expect["match_pct"]:
            raise SystemExit(f"{year}: match percent {pct} != {expect['match_pct']}")
        stacked.extend(rows)

    if len(long_rows) != 7245:
        raise SystemExit(f"Long panel has {len(long_rows)} rows, expected 7245")
    if Counter(row_key(row) for row in long_rows) != Counter(row_key(row) for row in stacked):
        raise SystemExit("abs_ajg_long.csv does not match the per-year files")

    methods = Counter(row["match_method"] for row in long_rows)
    if methods != {"issn": 5736, "unmatched": 1478, "title": 31}:
        raise SystemExit(f"Unexpected match methods: {dict(methods)}")

    ft50_2024 = sum(1 for row in loaded[2024] if row["catalog"] == "ft50")
    if ft50_2024 != 50:
        raise SystemExit(f"AJG 2024 ft50 matches {ft50_2024}, expected 50")

    by_title = {row["journal_title"].casefold(): row["rating"] for row in loaded[2024]}
    for title, rating in (
        ("american economic review", "4*"),
        ("journal of finance", "4*"),
        ("harvard business review", "3"),
    ):
        if by_title.get(title) != rating:
            raise SystemExit(f"2024 {title} rating {by_title.get(title)!r} != {rating!r}")


def payload(loaded: dict[int, list[dict[str, str]]]) -> dict:
    rows: list[list] = []
    for year in sorted(EDITIONS, reverse=True):
        edition = sorted(loaded[year], key=lambda row: (row["journal_title"].casefold(), row["field"]))
        for row in edition:
            rows.append(
                [
                    "abs_ajg",
                    year,
                    row["journal_id"],
                    row["journal_title"],
                    row["rating"],
                    row["field"],
                    row["print_issn"],
                    row["e_issn"],
                ]
            )
    return {
        "base": PAGES_BASE,
        "liveUrl": LIVE_URL + "rankings.html",
        "repo": REPO_URL,
        "readme": REPO_URL + "#readme",
        "freeze": FREEZE_ID,
        "source": "CABS Academic Journal Guide via Editor-Collector freeze " + FREEZE_ID,
        "sourceUrl": "https://charteredabs.org/academic-journal-guide/academic-journal-guide-2024",
        "systems": [{"id": "abs_ajg", "label": "ABS/AJG"}],
        "editions": {"abs_ajg": list(EDITIONS)},
        "ratings": {"abs_ajg": ["4*", "4", "3", "2", "1"]},
        "subjectLabels": SUBJECT_LABELS,
        "columns": [
            "system",
            "year",
            "journal_id",
            "journal_title",
            "rating",
            "field",
            "print_issn",
            "e_issn",
        ],
        "rows": rows,
    }


def js_payload(body: dict) -> str:
    raw = json.dumps(body, ensure_ascii=False, separators=(",", ":"))
    raw = (
        raw.replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )
    return (
        "/* Generated by scripts/build_rankings.py from "
        "journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/. Do not edit. */\n"
        "window.RANKINGS_DATA = "
        + raw
        + ";\n"
    )


def main() -> int:
    loaded: dict[int, list[dict[str, str]]] = {}
    for year in EDITIONS:
        header, rows = read_csv(RELEASE / f"abs_ajg_{year}.csv")
        if tuple(header) != GRADE_COLUMNS:
            raise SystemExit(f"Unexpected columns in abs_ajg_{year}.csv: {header}")
        loaded[year] = rows
    long_header, long_rows = read_csv(RELEASE / "abs_ajg_long.csv")
    if tuple(long_header) != GRADE_COLUMNS:
        raise SystemExit(f"Unexpected columns in abs_ajg_long.csv: {long_header}")
    conflict_header, conflicts = read_csv(RELEASE / "conflicts.csv")
    if conflicts:
        raise SystemExit(f"conflicts.csv is not empty: {len(conflicts)} rows")
    if "journal_title" not in conflict_header:
        raise SystemExit(f"Unexpected conflicts.csv header: {conflict_header}")
    for name in ("journal_id_crosswalk.csv", "unmatched_journals.csv", "RELEASE_NOTES.md"):
        path = RELEASE / name
        if not path.exists() or path.stat().st_size == 0:
            raise SystemExit(f"Missing freeze file: {path.relative_to(ROOT)}")

    validate(loaded, long_rows)
    body = payload(loaded)
    if body["base"] != PAGES_BASE or body["freeze"] != FREEZE_ID:
        raise SystemExit("rankings payload is not the pinned freeze")
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    text = js_payload(body)
    DATA_JS.write_text(text, encoding="utf-8")
    print(
        f"Wrote {DATA_JS.relative_to(ROOT)} ({len(text) / 1_000_000:.1f} MB) — "
        f"{len(body['rows']):,} rating rows from {FREEZE_ID}, "
        f"AJG 2024 {EXPECTED[2024]['rows']:,} journals, "
        f"{EXPECTED[2024]['mapped']:,} matched ({EXPECTED[2024]['match_pct']}%)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
