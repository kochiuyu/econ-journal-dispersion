#!/usr/bin/env python3
"""Build site/rankings-data.js from the pinned ABS/AJG freeze and list catalogs.

ABS/AJG grades and journal_id values are copied from
journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/.
FT50, UTD24, Top 5, and ABDC rows are copied from the catalogs under
journals/. ABDC ratings are the catalog file (A*, A, B, C). FT50, UTD24,
and Top 5 have no grade column and are stored with an empty rating.
CNRS and Handelsblatt/VWL rows are copied from their pinned freezes.
CNRS keeps the published category and domain. Handelsblatt/VWL keeps the
published weight and, when the freeze has one, the letter class.

This script does not fetch sources, does not read portal extracts or raw
PDFs, and does not assign ratings, weights, or ids of its own.
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
# Membership catalogs. Edition is the list on file, not a grade.
# FT50 is the April 2026 revision named in data/editors/ft50/STATUS.md.
# ABDC catalogs are the 2025 list named in data/editors/abdc/STATUS.md.
# UTD24 and Top 5 catalogs do not carry an edition year.
FT50_SOURCE = "https://www.ft.com/ft50-journals"
UTD24_SOURCE = (
    "https://jsom.utdallas.edu/the-utd-top-100-business-school-research-rankings/list-of-journals"
)
ABDC_SOURCE = "https://abdc.edu.au/abdc-journal-quality-list/"
ABDC_EDITION = 2025
ABDC_TIERS = (
    ("A*", ROOT / "journals/catalog_abdc_a_star.csv", 219),
    ("A", ROOT / "journals/catalog_abdc_a.csv", 630),
    ("B", ROOT / "journals/catalog_abdc_b.csv", 861),
    ("C", ROOT / "journals/catalog_abdc_c.csv", 941),
)
# Locked to journals/catalog_top5.csv. Same five ids as scripts/build_site.py.
TOP5_IDS = frozenset({"aer", "econometrica", "jpe", "qje", "restud"})
UTD24_ABDC_ONLY_ID = "informs_journal_computing"
LIST_COUNTS = {
    "abs_ajg": 7245,
    "cnrs": 7361,
    "handelsblatt_vwl": 42478,
    "ft50": 50,
    "utd24": 24,
    "top5": 5,
    "abdc": 2651,
}
CNRS_RELEASE = ROOT / "journals/rankings/cnrs/releases/rankings_cnrs_20261024"
CNRS_YEARS = (2011, 2012, 2013, 2014, 2015, 2017, 2018, 2019, 2020)
CNRS_RATINGS = ("1", "1e", "1g", "1eg", "2", "3", "4")
CNRS_EXPECTED = {
    2011: {"rows": 793, "mapped": 653, "match_pct": 82.3},
    2012: {"rows": 794, "mapped": 655, "match_pct": 82.5},
    2013: {"rows": 798, "mapped": 657, "match_pct": 82.3},
    2014: {"rows": 818, "mapped": 675, "match_pct": 82.5},
    2015: {"rows": 827, "mapped": 683, "match_pct": 82.6},
    2017: {"rows": 826, "mapped": 684, "match_pct": 82.8},
    2018: {"rows": 831, "mapped": 694, "match_pct": 83.5},
    2019: {"rows": 834, "mapped": 702, "match_pct": 84.2},
    2020: {"rows": 840, "mapped": 713, "match_pct": 84.9},
}
CNRS_SOURCE = {
    2011: ("cnrs_2011_10.pdf", "2011-10 Vallorem"),
    2012: ("cnrs_2012_06.pdf", "2012-06 Vallorem"),
    2013: ("cnrs_2013_11.pdf", "2013-11 Vallorem"),
    2014: ("cnrs_2014_11.pdf", "2014-11 Vallorem"),
    2015: ("cnrs_2015_11.pdf", "2015-11 Vallorem"),
    2017: ("cnrs_2017_12.pdf", "2017-12 Vallorem"),
    2018: ("cnrs_2018_11.pdf", "2018-11 Coactis mirror (Vallorem copy was corrupt)"),
    2019: ("cnrs_2019_06.pdf", "2019-06 Vallorem"),
    2020: ("cnrs_2020_06.pdf", "2020-06 Vallorem"),
}
HB_RELEASE = ROOT / "journals/rankings/handelsblatt_vwl/releases/rankings_handelsblatt_vwl_20261024"
HB_YEARS = tuple(range(1998, 2021))
HB_RATINGS = ("A+", "A", "B", "C", "D", "E", "F")
HB_COLUMNS = (
    "edition_year",
    "weight",
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
HB_SJR_FILE = "VWL_Zeitschriftenliste.xlsx"
HB_SJR_NOTE = "Forschungsmonitoring VWL SJR_main (HB-style continuous weight)"
HB_PDF_FILE = "handelsblatt-liste_2015.pdf"
HB_PDF_NOTE = "Handelsblatt VWL Ranking 2015 journal list (HB-Gewicht)"
HB_EXPECTED = {year: {"rows": 1777, "mapped": 882, "match_pct": 49.6} for year in HB_YEARS}
HB_EXPECTED[2015] = {"rows": 3384, "mapped": 1535, "match_pct": 45.4}
SYSTEM_ORDER = (
    "abs_ajg",
    "cnrs",
    "handelsblatt_vwl",
    "ft50",
    "utd24",
    "top5",
    "abdc",
)

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


def require_columns(header: list[str], required: tuple[str, ...], path: Path) -> None:
    missing = [column for column in required if column not in header]
    if missing:
        raise SystemExit(f"{path.relative_to(ROOT)} missing columns: {', '.join(missing)}")


def load_catalog(
    path: Path,
    *,
    system: str,
    edition: int | str,
    rating: str,
    expected: int,
    source_url: str | None,
    field_column: str | None = None,
) -> list[list]:
    """Copy one membership catalog. ``rating`` is empty unless the file is a tier."""
    header, rows = read_csv(path)
    required = ("journal_id", "journal_name", "issn")
    if field_column:
        required = required + (field_column,)
    require_columns(header, required, path)
    if len(rows) != expected:
        raise SystemExit(f"{path.name}: {len(rows)} rows, expected {expected}")
    if source_url is not None:
        require_columns(header, ("list_source_url",), path)
        urls = {row["list_source_url"].strip() for row in rows}
        if urls != {source_url}:
            raise SystemExit(f"{path.name}: list_source_url {sorted(urls)} != {source_url}")
    seen: set[str] = set()
    loaded: list[list] = []
    for row in rows:
        journal_id = row["journal_id"].strip()
        title = row["journal_name"].strip()
        if not journal_id or not title:
            raise SystemExit(f"{path.name}: blank id or title")
        if journal_id in seen:
            raise SystemExit(f"{path.name}: duplicate journal_id {journal_id}")
        seen.add(journal_id)
        field = row[field_column].strip() if field_column else ""
        if field_column and not field:
            raise SystemExit(f"{path.name}: blank {field_column} on {title}")
        if rating not in {"", "A*", "A", "B", "C"}:
            raise SystemExit(f"{path.name}: rating {rating!r} is not a catalog tier")
        loaded.append(
            [
                system,
                edition,
                journal_id,
                title,
                rating,
                field,
                row["issn"].strip(),
                "",
                "",
            ]
        )
    return loaded


def load_list_catalogs() -> list[list]:
    ft50 = load_catalog(
        ROOT / "journals/catalog_ft50.csv",
        system="ft50",
        edition="Apr 2026",
        rating="",
        expected=LIST_COUNTS["ft50"],
        source_url=FT50_SOURCE,
    )
    utd24 = load_catalog(
        ROOT / "journals/catalog_utd24.csv",
        system="utd24",
        edition="Current",
        rating="",
        expected=LIST_COUNTS["utd24"],
        source_url=UTD24_SOURCE,
    )
    top5 = load_catalog(
        ROOT / "journals/catalog_top5.csv",
        system="top5",
        edition="Current",
        rating="",
        expected=LIST_COUNTS["top5"],
        source_url=None,
    )
    abdc: list[list] = []
    abdc_ids: dict[str, str] = {}
    for rating, path, expected in ABDC_TIERS:
        tier = load_catalog(
            path,
            system="abdc",
            edition=ABDC_EDITION,
            rating=rating,
            expected=expected,
            source_url=ABDC_SOURCE,
            field_column="field_for",
        )
        for row in tier:
            previous = abdc_ids.get(row[2])
            if previous:
                raise SystemExit(f"ABDC journal_id {row[2]} is in {previous} and {rating}")
            abdc_ids[row[2]] = rating
        abdc.extend(tier)
    if len(abdc) != LIST_COUNTS["abdc"]:
        raise SystemExit(f"ABDC has {len(abdc)} rows, expected {LIST_COUNTS['abdc']}")

    ft50_ids = {row[2] for row in ft50}
    top5_ids = {row[2] for row in top5}
    utd_ids = {row[2] for row in utd24}
    if top5_ids != TOP5_IDS:
        raise SystemExit(f"catalog_top5.csv ids {sorted(top5_ids)} != {sorted(TOP5_IDS)}")
    if not top5_ids <= ft50_ids:
        raise SystemExit(f"Top 5 ids missing from FT50: {sorted(top5_ids - ft50_ids)}")
    outside_ft50 = utd_ids - ft50_ids
    if outside_ft50 != {UTD24_ABDC_ONLY_ID}:
        raise SystemExit(f"UTD24 ids outside FT50: {sorted(outside_ft50)}")
    if UTD24_ABDC_ONLY_ID not in abdc_ids or abdc_ids[UTD24_ABDC_ONLY_ID] != "A":
        raise SystemExit("UTD24 INFORMS Journal on Computing is not in the ABDC A catalog")
    for row in ft50 + utd24 + top5:
        if row[4]:
            raise SystemExit(f"{row[0]} {row[3]} has a grade {row[4]!r}")
        if row[5]:
            raise SystemExit(f"{row[0]} {row[3]} has a field {row[5]!r}")

    lists = ft50 + utd24 + top5 + abdc
    lists.sort(key=lambda row: (row[0], str(row[1]), row[3].casefold(), row[5], row[4]))
    return lists


def check_conflicts(path: Path, expected_rows: int) -> None:
    header, rows = read_csv(path)
    if "journal_title" not in header or "chosen_rating" not in header:
        raise SystemExit(f"Unexpected conflicts header in {path.name}: {header}")
    if len(rows) != expected_rows:
        raise SystemExit(f"{path.name}: {len(rows)} conflict rows, expected {expected_rows}")


def require_sidecars(release: Path) -> None:
    for name in ("journal_id_crosswalk.csv", "unmatched_journals.csv", "RELEASE_NOTES.md"):
        path = release / name
        if not path.exists() or path.stat().st_size == 0:
            raise SystemExit(f"Missing freeze file: {path.relative_to(ROOT)}")


def mapped_id(row: dict[str, str], label: str) -> bool:
    has_id = bool(row["journal_id"].strip())
    if row["match_method"] not in ALLOWED_METHODS:
        raise SystemExit(f"{label}: match_method {row['match_method']!r}")
    if row["match_method"] == "unmatched":
        if has_id or row["catalog"].strip():
            raise SystemExit(f"{label}: unmatched row has an id: {row['journal_title']}")
        return False
    if not has_id or not row["catalog"].strip():
        raise SystemExit(f"{label}: matched row missing id: {row['journal_title']}")
    return True


def load_cnrs() -> list[list]:
    loaded: dict[int, list[dict[str, str]]] = {}
    for year in CNRS_YEARS:
        header, rows = read_csv(CNRS_RELEASE / f"cnrs_{year}.csv")
        if tuple(header) != GRADE_COLUMNS:
            raise SystemExit(f"Unexpected columns in cnrs_{year}.csv: {header}")
        expect = CNRS_EXPECTED[year]
        source_file, source_note = CNRS_SOURCE[year]
        mapped = 0
        for row in rows:
            if row["edition_year"] != str(year):
                raise SystemExit(f"CNRS {year}: edition_year {row['edition_year']!r}")
            if row["rating"] not in CNRS_RATINGS or row["rating"] != row["rating_raw"]:
                raise SystemExit(f"CNRS {year}: rating {row['rating']!r}/{row['rating_raw']!r} on {row['journal_title']}")
            if not row["journal_title"] or not row["field"].strip():
                raise SystemExit(f"CNRS {year}: blank title or field")
            if row["source_file"] != source_file or row["source_note"] != source_note:
                raise SystemExit(f"CNRS {year}: source {row['source_file']!r} / {row['source_note']!r}")
            if mapped_id(row, f"CNRS {year}"):
                mapped += 1
        if len(rows) != expect["rows"] or mapped != expect["mapped"]:
            raise SystemExit(f"CNRS {year}: {len(rows)} rows / {mapped} mapped, expected {expect['rows']} / {expect['mapped']}")
        pct = round(100 * mapped / len(rows), 1)
        if pct != expect["match_pct"]:
            raise SystemExit(f"CNRS {year}: match percent {pct} != {expect['match_pct']}")
        loaded[year] = rows
    long_header, long_rows = read_csv(CNRS_RELEASE / "cnrs_long.csv")
    if tuple(long_header) != GRADE_COLUMNS:
        raise SystemExit(f"Unexpected columns in cnrs_long.csv: {long_header}")
    if len(long_rows) != LIST_COUNTS["cnrs"]:
        raise SystemExit(f"CNRS long panel has {len(long_rows)} rows, expected {LIST_COUNTS['cnrs']}")
    stacked = [row for year in CNRS_YEARS for row in loaded[year]]
    if Counter(row_key(row) for row in long_rows) != Counter(row_key(row) for row in stacked):
        raise SystemExit("cnrs_long.csv does not match the per-year files")
    check_conflicts(CNRS_RELEASE / "conflicts.csv", 26)
    unmatched_header, unmatched = read_csv(CNRS_RELEASE / "unmatched_journals.csv")
    if "journal_title" not in unmatched_header or len(unmatched) != 1245:
        raise SystemExit(f"CNRS unmatched file has {len(unmatched)} rows, expected 1245")
    require_sidecars(CNRS_RELEASE)
    packed: list[list] = []
    for year in sorted(CNRS_YEARS, reverse=True):
        edition = sorted(loaded[year], key=lambda row: (row["journal_title"].casefold(), row["field"], row["rating"]))
        for row in edition:
            packed.append(
                [
                    "cnrs",
                    year,
                    row["journal_id"],
                    row["journal_title"],
                    row["rating"],
                    row["field"],
                    row["print_issn"],
                    row["e_issn"],
                    "",
                ]
            )
    return packed


def load_handelsblatt() -> list[list]:
    loaded: dict[int, list[dict[str, str]]] = {}
    for year in HB_YEARS:
        header, rows = read_csv(HB_RELEASE / f"handelsblatt_vwl_{year}.csv")
        if tuple(header) != HB_COLUMNS:
            raise SystemExit(f"Unexpected columns in handelsblatt_vwl_{year}.csv: {header}")
        expect = HB_EXPECTED[year]
        mapped = 0
        pdf_rows = 0
        sjr_rows = 0
        for row in rows:
            if row["edition_year"] != str(year):
                raise SystemExit(f"HB {year}: edition_year {row['edition_year']!r}")
            if not row["journal_title"]:
                raise SystemExit(f"HB {year}: blank title")
            if row["field"].strip() or row["publisher"].strip():
                raise SystemExit(f"HB {year}: field or publisher on {row['journal_title']}")
            if row["weight"] != row["rating_raw"] or not row["weight"].strip():
                raise SystemExit(f"HB {year}: weight {row['weight']!r} / rating_raw {row['rating_raw']!r}")
            try:
                weight = float(row["weight"])
            except ValueError as exc:
                raise SystemExit(f"HB {year}: weight {row['weight']!r} is not numeric") from exc
            if weight != weight:  # NaN
                raise SystemExit(f"HB {year}: weight {row['weight']!r} is not numeric")
            if row["rating"] and row["rating"] not in HB_RATINGS:
                raise SystemExit(f"HB {year}: rating {row['rating']!r} on {row['journal_title']}")
            if row["source_file"] == HB_SJR_FILE and row["source_note"] == HB_SJR_NOTE:
                sjr_rows += 1
            elif row["source_file"] == HB_PDF_FILE and row["source_note"] == HB_PDF_NOTE:
                if year != 2015 or row["rating"]:
                    raise SystemExit(f"HB {year}: PDF row has a letter rating or is outside 2015")
                pdf_rows += 1
            else:
                raise SystemExit(f"HB {year}: source {row['source_file']!r} / {row['source_note']!r}")
            if mapped_id(row, f"HB {year}"):
                mapped += 1
        if sjr_rows != 1777 or pdf_rows != (1607 if year == 2015 else 0):
            raise SystemExit(f"HB {year}: SJR {sjr_rows} / PDF {pdf_rows}")
        if len(rows) != expect["rows"] or mapped != expect["mapped"]:
            raise SystemExit(f"HB {year}: {len(rows)} rows / {mapped} mapped, expected {expect['rows']} / {expect['mapped']}")
        pct = round(100 * mapped / len(rows), 1)
        if pct != expect["match_pct"]:
            raise SystemExit(f"HB {year}: match percent {pct} != {expect['match_pct']}")
        loaded[year] = rows
    long_header, long_rows = read_csv(HB_RELEASE / "handelsblatt_vwl_long.csv")
    if tuple(long_header) != HB_COLUMNS:
        raise SystemExit(f"Unexpected columns in handelsblatt_vwl_long.csv: {long_header}")
    if len(long_rows) != LIST_COUNTS["handelsblatt_vwl"]:
        raise SystemExit(f"HB long panel has {len(long_rows)} rows, expected {LIST_COUNTS['handelsblatt_vwl']}")
    stacked = [row for year in HB_YEARS for row in loaded[year]]
    long_key = tuple(HB_COLUMNS)
    def hb_key(row: dict[str, str]) -> tuple[str, ...]:
        return tuple(row[column] for column in long_key)
    if Counter(hb_key(row) for row in long_rows) != Counter(hb_key(row) for row in stacked):
        raise SystemExit("handelsblatt_vwl_long.csv does not match the per-year files")
    check_conflicts(HB_RELEASE / "conflicts.csv", 0)
    unmatched_header, unmatched = read_csv(HB_RELEASE / "unmatched_journals.csv")
    if "journal_title" not in unmatched_header or len(unmatched) != 21539:
        raise SystemExit(f"HB unmatched file has {len(unmatched)} rows, expected 21539")
    require_sidecars(HB_RELEASE)
    packed: list[list] = []
    for year in sorted(HB_YEARS, reverse=True):
        edition = sorted(
            loaded[year],
            key=lambda row: (row["journal_title"].casefold(), row["rating"], row["weight"], row["source_file"]),
        )
        for row in edition:
            packed.append(
                [
                    "handelsblatt_vwl",
                    year,
                    row["journal_id"],
                    row["journal_title"],
                    row["rating"],
                    "",
                    row["print_issn"],
                    row["e_issn"],
                    row["weight"],
                ]
            )
    return packed


def payload(
    loaded: dict[int, list[dict[str, str]]],
    list_rows: list[list],
    cnrs_rows: list[list],
    hb_rows: list[list],
) -> dict:
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
                    "",
                ]
            )
    rows.extend(cnrs_rows)
    rows.extend(hb_rows)
    rows.extend(list_rows)
    if any(len(row) != 9 for row in rows):
        raise SystemExit("Ranking row width is not 9")
    counts = Counter(row[0] for row in rows)
    if dict(counts) != LIST_COUNTS:
        raise SystemExit(f"Ranking row counts {dict(counts)} != {LIST_COUNTS}")
    abdc_ratings = Counter(row[4] for row in rows if row[0] == "abdc")
    if dict(abdc_ratings) != {"A*": 219, "A": 630, "B": 861, "C": 941}:
        raise SystemExit(f"ABDC rating counts {dict(abdc_ratings)}")
    return {
        "base": PAGES_BASE,
        "liveUrl": LIVE_URL + "rankings.html",
        "repo": REPO_URL,
        "readme": REPO_URL + "#readme",
        "freeze": FREEZE_ID,
        "source": "CABS Academic Journal Guide via Editor-Collector freeze " + FREEZE_ID,
        "sourceUrl": "https://charteredabs.org/academic-journal-guide/academic-journal-guide-2024",
        "systems": [
            {"id": "abs_ajg", "label": "ABS/AJG"},
            {"id": "cnrs", "label": "CNRS"},
            {"id": "handelsblatt_vwl", "label": "Handelsblatt/VWL", "showWeight": True},
            {"id": "ft50", "label": "FT50"},
            {"id": "utd24", "label": "UTD24"},
            {"id": "top5", "label": "Top 5"},
            {"id": "abdc", "label": "ABDC"},
        ],
        "editions": {
            "abs_ajg": list(EDITIONS),
            "cnrs": list(CNRS_YEARS),
            "handelsblatt_vwl": list(HB_YEARS),
            "ft50": ["Apr 2026"],
            "utd24": ["Current"],
            "top5": ["Current"],
            "abdc": [ABDC_EDITION],
        },
        "ratings": {
            "abs_ajg": ["4*", "4", "3", "2", "1"],
            "cnrs": list(CNRS_RATINGS),
            "handelsblatt_vwl": list(HB_RATINGS),
            "ft50": [],
            "utd24": [],
            "top5": [],
            "abdc": ["A*", "A", "B", "C"],
        },
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
            "weight",
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
        "journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/, "
        "journals/rankings/cnrs/releases/rankings_cnrs_20261024/, "
        "journals/rankings/handelsblatt_vwl/releases/rankings_handelsblatt_vwl_20261024/, "
        "and journals/catalog_{ft50,utd24,top5,abdc_*}.csv. Do not edit. */\n"
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
    list_rows = load_list_catalogs()
    cnrs_rows = load_cnrs()
    hb_rows = load_handelsblatt()
    body = payload(loaded, list_rows, cnrs_rows, hb_rows)
    if body["base"] != PAGES_BASE or body["freeze"] != FREEZE_ID:
        raise SystemExit("rankings payload is not the pinned freeze")
    if [system["id"] for system in body["systems"]] != list(SYSTEM_ORDER):
        raise SystemExit(f"Unexpected ranking systems: {body['systems']}")
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    text = js_payload(body)
    DATA_JS.write_text(text, encoding="utf-8")
    abdc_bits = ", ".join(
        f"{rating} {expected:,}" for rating, _path, expected in ABDC_TIERS
    )
    print(
        f"Wrote {DATA_JS.relative_to(ROOT)} ({len(text) / 1_000_000:.1f} MB) — "
        f"{len(body['rows']):,} rows. "
        f"ABS/AJG {LIST_COUNTS['abs_ajg']:,} "
        f"(AJG 2024 {EXPECTED[2024]['rows']:,} journals, "
        f"{EXPECTED[2024]['mapped']:,} matched, {EXPECTED[2024]['match_pct']}%). "
        f"FT50 {LIST_COUNTS['ft50']}. "
        f"UTD24 {LIST_COUNTS['utd24']}. "
        f"Top 5 {LIST_COUNTS['top5']}. "
        f"ABDC {LIST_COUNTS['abdc']:,} ({abdc_bits}). "
        f"CNRS {LIST_COUNTS['cnrs']:,} "
        f"(2020 {CNRS_EXPECTED[2020]['rows']:,} journals, "
        f"{CNRS_EXPECTED[2020]['mapped']:,} matched, {CNRS_EXPECTED[2020]['match_pct']}%). "
        f"Handelsblatt/VWL {LIST_COUNTS['handelsblatt_vwl']:,} "
        f"(2020 {HB_EXPECTED[2020]['rows']:,} journals, "
        f"{HB_EXPECTED[2020]['mapped']:,} matched, {HB_EXPECTED[2020]['match_pct']}%; "
        f"2015 {HB_EXPECTED[2015]['rows']:,})."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
