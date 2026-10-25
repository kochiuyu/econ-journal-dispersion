#!/usr/bin/env python3
"""Build site/rankings-data.js from the pinned rankings freezes and list catalogs.

ABS/AJG grades and journal_id values are copied from
journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/.
FT50, UTD24, Top 5, and ABDC rows are copied from the catalogs under
journals/. ABDC ratings are the catalog file (A*, A, B, C). FT50, UTD24,
and Top 5 have no grade column and are stored with an empty rating.
FT50 field is the McMaster LibGuide subject area on catalog_ft50.csv.
UTD24 and Top 5 leave field empty.
CNRS, Handelsblatt/VWL, Tilburg/TISEM, FNEGE, ERIM Core, NYU Stern
Economics, and ShanghaiRanking rows are copied from their pinned freezes.
CNRS keeps the published category and domain. Handelsblatt/VWL keeps the
published weight and, when the freeze has one, the letter class. Tilburg
keeps the TISEM tier. FNEGE keeps the published grade. ERIM keeps the Core
class. Stern keeps the memo tier. Shanghai keeps binary membership and the
subject.

This script does not fetch sources, does not read portal extracts or raw
PDFs, and does not assign ratings, weights, or ids of its own.
"""

from __future__ import annotations

import csv
import json
import re
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
# Subject areas are the McMaster LibGuide "Subject Area" column, not an FT grade.
# https://libguides.mcmaster.ca/ft-top50
# Two subjects stay in one cell, comma-separated, as that table prints them.
# The Rankings field filter matches the whole cell, as it does for Shanghai.
FT50_FIELD_SOURCE = "https://libguides.mcmaster.ca/ft-top50"
FT50_SUBJECTS = frozenset({
    "Accounting",
    "Economics",
    "Entrepreneurship",
    "Finance",
    "Human Resources",
    "International Business",
    "Management",
    "Marketing",
    "Operations & Information Systems",
    "Organizational Behaviour",
})
# Titles a loose HTML parse drops. Locked to the LibGuide cells.
FT50_FIELD_CHECKS = {
    "jf": "Finance",
    "jfqa": "Finance",
    "jfe": "Finance",
    "jpe": "Economics",
    "sloan_mr": "Management",
    "jibs": "International Business",
    "asr": "Organizational Behaviour, Human Resources",
    "psych_sci": "Organizational Behaviour, Human Resources",
    "rp": "Economics, Management",
    "jap": "Organizational Behaviour",
}
CONTACT_RE = re.compile(r"@|https?://|mailto:|\d", re.IGNORECASE)
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
    "tilburg": 179,
    "fnege": 2044,
    "erim": 283,
    "stern": 49,
    "shanghai": 76,
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
    "tilburg",
    "fnege",
    "erim",
    "stern",
    "shanghai",
)
TILBURG_RELEASE = ROOT / "journals/rankings/tilburg/releases/rankings_tilburg_20261025"
TILBURG_RATINGS = ("Top-core", "Top", "Very good")
TILBURG_NOTES = {
    "TISEM top-core",
    "TISEM top-core allocation supplement",
    "TISEM top",
    "TISEM very good",
}
TILBURG_EXPECTED = {"rows": 179, "mapped": 164, "match_pct": 91.6}
FNEGE_RELEASE = ROOT / "journals/rankings/fnege/releases/rankings_fnege_20261025"
FNEGE_YEARS = (2019, 2022, 2025)
FNEGE_RATINGS = ("1*", "1", "2", "3", "4", "EM", "NC")
FNEGE_EXPECTED = {
    2019: {"rows": 484, "mapped": 410, "match_pct": 84.7},
    2022: {"rows": 669, "mapped": 577, "match_pct": 86.2},
    2025: {"rows": 891, "mapped": 733, "match_pct": 82.3},
}
FNEGE_FIELD_LABELS = {
    "ACC": "Accounting",
    "BUS HIST": "Business History",
    "BUS SOC": "Business and Society",
    "EDUC": "Education",
    "FIN": "Finance",
    "GEN MAN": "General Management",
    "HLTH": "Health",
    "HRM": "Human Resource Management",
    "INNOV": "Innovation",
    "INT": "International",
    "LOG": "Logistics",
    "MIS": "Management Information Systems",
    "MKG": "Marketing",
    "ORG STUD": "Organisation Studies",
    "PUB MAN": "Public Management",
    "SECTOR": "Sector Studies",
    "STRAT": "Strategy",
}
ERIM_RELEASE = ROOT / "journals/rankings/erim/releases/rankings_erim_20261025"
ERIM_EDITION = "2024–2028"
ERIM_RATINGS = ("STAR", "M-STAR", "P", "EP*", "PA", "S", "S (3=1)", "M")
ERIM_EXPECTED = {"rows": 283, "mapped": 257, "match_pct": 90.8}
ERIM_TRACKS = {
    "LIS": "Logistics and Information Systems",
    "F&A": "Finance and Accounting",
    "ORG": "Organisation",
    "GEN": "General",
    "MKT": "Marketing",
    "S&E": "Strategy and Entrepreneurship",
}
STERN_RELEASE = ROOT / "journals/rankings/stern/releases/rankings_stern_20261025"
STERN_RATINGS = ("Top 5", "Really excellent", "Field", "Review")
STERN_NOTES = {
    "Stern memo 2020 top 5",
    "Stern memo 2020 general interest",
    "Stern memo 2020 field",
    "Stern memo 2020 review",
}
STERN_FIELDS = {
    "Agriculture, natural resources, and the environment",
    "Business economics",
    "Econometrics",
    "Economic history",
    "Economic development",
    "Economic theory",
    "Financial economics",
    "Health economics",
    "Industrial organization",
    "International trade",
    "Labor economics",
    "Macroeconomics",
    "Public economics",
    "Regional and urban economics",
}
STERN_EXPECTED = {"rows": 49, "mapped": 47, "match_pct": 95.9}
SHANGHAI_RELEASE = ROOT / "journals/rankings/shanghai/releases/rankings_shanghai_20261025"
SHANGHAI_YEARS = (2024, 2026)
SHANGHAI_RATINGS = ("Top",)
SHANGHAI_SUBJECTS = ("Economics", "Business Administration", "Finance", "Management")
SHANGHAI_NOTES = {
    "ShanghaiRanking AES 2024",
    "ShanghaiRanking AES 2026",
    "ShanghaiRanking JCR 2024",
}
SHANGHAI_EXPECTED = {
    2024: {"rows": 57, "mapped": 55, "match_pct": 96.5},
    2026: {"rows": 19, "mapped": 19, "match_pct": 100.0},
}

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


def check_ft50_field(field: str, title: str) -> None:
    """McMaster subject area, including a second subject when the cell prints one."""
    if CONTACT_RE.search(field):
        raise SystemExit(f"FT50 field on {title} is not a subject: {field!r}")
    parts = [part.strip() for part in field.split(",")]
    if not parts or any(not part for part in parts) or ", ".join(parts) != field:
        raise SystemExit(f"FT50 field on {title} is not a subject list: {field!r}")
    if len(parts) > 2:
        raise SystemExit(f"FT50 field on {title} has more than two subjects: {field!r}")
    unknown = [part for part in parts if part not in FT50_SUBJECTS]
    if unknown:
        raise SystemExit(
            f"FT50 field on {title} has unknown subject {unknown!r} "
            f"(expected a subject area from {FT50_FIELD_SOURCE})"
        )


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
        field_column="field",
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
    for row in ft50:
        if row[4]:
            raise SystemExit(f"{row[0]} {row[3]} has a grade {row[4]!r}")
        check_ft50_field(row[5], row[3])
    by_id = {row[2]: row for row in ft50}
    for journal_id, expected in FT50_FIELD_CHECKS.items():
        match = by_id.get(journal_id)
        if not match or match[5] != expected:
            got = None if match is None else match[5]
            raise SystemExit(f"FT50 {journal_id} field {got!r} != {expected!r}")
    dual = [row[2] for row in ft50 if ", " in row[5]]
    if len(dual) != 3:
        raise SystemExit(f"FT50 dual-subject rows {sorted(dual)} != 3")
    for row in utd24 + top5:
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


def load_grade_freeze(
    release: Path,
    *,
    stem: str,
    years: tuple[str, ...],
    ratings: tuple[str, ...],
    expected: dict[str, dict[str, int | float]],
    source_file: str,
    source_note_for,
    edition_for,
    system: str,
    unmatched_rows: int,
    conflict_rows: int,
    long_rows_expected: int,
) -> list[list]:
    loaded: dict[str, list[dict[str, str]]] = {}
    for year in years:
        path = release / f"{stem}_{year}.csv"
        header, rows = read_csv(path)
        if tuple(header) != GRADE_COLUMNS:
            raise SystemExit(f"Unexpected columns in {path.name}: {header}")
        expect = expected[year]
        edition = edition_for(year)
        mapped = 0
        for row in rows:
            if row["edition_year"] != edition:
                raise SystemExit(f"{system} {year}: edition_year {row['edition_year']!r} != {edition!r}")
            if row["rating"] not in ratings or row["rating"] != row["rating_raw"]:
                raise SystemExit(f"{system} {year}: rating {row['rating']!r}/{row['rating_raw']!r} on {row['journal_title']}")
            if not row["journal_title"]:
                raise SystemExit(f"{system} {year}: blank title")
            if row["source_file"] != source_file:
                raise SystemExit(f"{system} {year}: source_file {row['source_file']!r}")
            note = source_note_for(row)
            if row["source_note"] != note:
                raise SystemExit(f"{system} {year}: source_note {row['source_note']!r} != {note!r}")
            if mapped_id(row, f"{system} {year}"):
                mapped += 1
        if len(rows) != expect["rows"] or mapped != expect["mapped"]:
            raise SystemExit(
                f"{system} {year}: {len(rows)} rows / {mapped} mapped, expected {expect['rows']} / {expect['mapped']}"
            )
        pct = round(100 * mapped / len(rows), 1)
        if pct != expect["match_pct"]:
            raise SystemExit(f"{system} {year}: match percent {pct} != {expect['match_pct']}")
        loaded[year] = rows
    long_header, long_rows = read_csv(release / f"{stem}_long.csv")
    if tuple(long_header) != GRADE_COLUMNS:
        raise SystemExit(f"Unexpected columns in {stem}_long.csv: {long_header}")
    if len(long_rows) != long_rows_expected:
        raise SystemExit(f"{system} long panel has {len(long_rows)} rows, expected {long_rows_expected}")
    stacked = [row for year in years for row in loaded[year]]
    if Counter(row_key(row) for row in long_rows) != Counter(row_key(row) for row in stacked):
        raise SystemExit(f"{stem}_long.csv does not match the per-year files")
    check_conflicts(release / "conflicts.csv", conflict_rows)
    unmatched_header, unmatched = read_csv(release / "unmatched_journals.csv")
    if "journal_title" not in unmatched_header or len(unmatched) != unmatched_rows:
        raise SystemExit(f"{system} unmatched file has {len(unmatched)} rows, expected {unmatched_rows}")
    require_sidecars(release)
    packed: list[list] = []
    for year in years:
        edition_label = edition_for(year)
        if isinstance(edition_label, str) and edition_label.isdigit():
            edition_label = int(edition_label)
        edition = sorted(loaded[year], key=lambda row: (row["journal_title"].casefold(), row["field"], row["rating"]))
        for row in edition:
            packed.append(
                [
                    system,
                    edition_label,
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


def erim_field_labels(rows: list[dict[str, str]]) -> dict[str, str]:
    labels: dict[str, str] = {}
    for row in rows:
        field = row["field"].strip()
        if not field or field in labels:
            continue
        parts = [part.strip() for part in field.split(",")]
        unknown = [part for part in parts if part not in ERIM_TRACKS]
        if unknown:
            raise SystemExit(f"ERIM track {field!r} has no label")
        labels[field] = "; ".join(ERIM_TRACKS[part] for part in parts)
    return labels


def load_tilburg() -> list[list]:
    rows = load_grade_freeze(
        TILBURG_RELEASE,
        stem="tilburg",
        years=("current",),
        ratings=TILBURG_RATINGS,
        expected={"current": TILBURG_EXPECTED},
        source_file="topjournals",
        source_note_for=lambda row: row["source_note"],
        edition_for=lambda year: "Current",
        system="tilburg",
        unmatched_rows=15,
        conflict_rows=0,
        long_rows_expected=LIST_COUNTS["tilburg"],
    )
    # source_note_for returns "" when the note is unexpected; the loader then
    # compares row["source_note"] != note. Re-check the note set explicitly.
    header, raw = read_csv(TILBURG_RELEASE / "tilburg_current.csv")
    del header
    for row in raw:
        if row["source_note"] not in TILBURG_NOTES:
            raise SystemExit(f"Tilburg source_note {row['source_note']!r}")
        if row["rating"] == "Very good" and not row["field"].strip():
            raise SystemExit(f"Tilburg very good row has no field: {row['journal_title']}")
        if row["rating"] != "Very good" and row["field"].strip():
            raise SystemExit(f"Tilburg {row['rating']} row has a field: {row['journal_title']}")
    by_title = {row[3].casefold(): row for row in rows}
    aer = by_title.get("american economic review")
    if not aer or aer[4] != "Top-core" or aer[2] != "aer":
        raise SystemExit(f"Tilburg AER row {aer}")
    omega = by_title.get("omega-international journal of management science")
    if not omega or omega[2] != "omega" or omega[4] != "Top":
        raise SystemExit(f"Tilburg Omega row {omega}")
    return rows


def load_fnege() -> tuple[list[list], dict[str, str]]:
    def note_for(row: dict[str, str]) -> str:
        return f"FNEGE {row['edition_year']}"

    packed = load_grade_freeze(
        FNEGE_RELEASE,
        stem="fnege",
        years=tuple(str(year) for year in FNEGE_YEARS),
        ratings=FNEGE_RATINGS,
        expected={str(year): FNEGE_EXPECTED[year] for year in FNEGE_YEARS},
        source_file="fnege-journal-quality-list",
        source_note_for=note_for,
        edition_for=lambda year: year,
        system="fnege",
        unmatched_rows=324,
        conflict_rows=3,
        long_rows_expected=LIST_COUNTS["fnege"],
    )
    fields = {row[5] for row in packed if row[5]}
    unknown = sorted(fields - set(FNEGE_FIELD_LABELS))
    if unknown:
        raise SystemExit(f"FNEGE field codes have no label: {unknown}")
    latest = [row for row in packed if row[1] == 2025]
    by_title = {row[3].casefold(): row for row in latest}
    aer = by_title.get("american economic review")
    if not aer or aer[4] != "1*" or aer[2] != "aer":
        raise SystemExit(f"FNEGE 2025 AER row {aer}")
    appetite = by_title.get("appetite")
    if not appetite or appetite[2] != "appetite":
        raise SystemExit(f"FNEGE 2025 Appetite row {appetite}")
    return packed, FNEGE_FIELD_LABELS


def load_erim() -> tuple[list[list], dict[str, str]]:
    header, raw = read_csv(ERIM_RELEASE / "erim_2024_2028.csv")
    if tuple(header) != GRADE_COLUMNS:
        raise SystemExit(f"Unexpected columns in erim_2024_2028.csv: {header}")
    labels = erim_field_labels(raw)
    packed = load_grade_freeze(
        ERIM_RELEASE,
        stem="erim",
        years=("2024_2028",),
        ratings=ERIM_RATINGS,
        expected={"2024_2028": ERIM_EXPECTED},
        source_file="EJL-Core-List-2024-2028.xlsx",
        source_note_for=lambda row: "ERIM Journals List Core 2024-2028",
        edition_for=lambda year: ERIM_EDITION,
        system="erim",
        unmatched_rows=26,
        conflict_rows=1,
        long_rows_expected=LIST_COUNTS["erim"],
    )
    for row in packed:
        if row[1] != ERIM_EDITION:
            raise SystemExit(f"ERIM edition {row[1]!r}")
    by_title = {row[3].casefold(): row for row in packed}
    amj = by_title.get("academy of management journal")
    if not amj or amj[4] != "STAR" or amj[2] != "amj":
        raise SystemExit(f"ERIM AMJ row {amj}")
    ethics = by_title.get("business ethics-a european review")
    if not ethics or ethics[2] != "business_ethics_environment_responsibility":
        raise SystemExit(f"ERIM Business Ethics row {ethics}")
    return packed, labels


def load_stern() -> list[list]:
    rows = load_grade_freeze(
        STERN_RELEASE,
        stem="stern",
        years=("2020",),
        ratings=STERN_RATINGS,
        expected={"2020": STERN_EXPECTED},
        source_file="Econ-Top-Journals-July-2020.pdf",
        source_note_for=lambda row: row["source_note"],
        edition_for=lambda year: year,
        system="stern",
        unmatched_rows=2,
        conflict_rows=0,
        long_rows_expected=LIST_COUNTS["stern"],
    )
    header, raw = read_csv(STERN_RELEASE / "stern_2020.csv")
    del header
    for row in raw:
        if row["source_note"] not in STERN_NOTES:
            raise SystemExit(f"Stern source_note {row['source_note']!r}")
        if row["rating"] == "Field":
            if row["field"] not in STERN_FIELDS:
                raise SystemExit(f"Stern field {row['field']!r} on {row['journal_title']}")
        elif row["field"].strip():
            raise SystemExit(f"Stern {row['rating']} row has a field: {row['journal_title']}")
    by_title = {row[3].casefold(): row for row in rows}
    aer = by_title.get("american economic review")
    if not aer or aer[4] != "Top 5" or aer[2] != "aer" or aer[1] != 2020:
        raise SystemExit(f"Stern AER row {aer}")
    top5 = {row[2] for row in rows if row[4] == "Top 5"}
    if top5 != {"aer", "econometrica", "jpe", "qje", "restud"}:
        raise SystemExit(f"Stern Top 5 ids {sorted(top5)}")
    nber = by_title.get("nber macro annual")
    if not nber or nber[4] != "Review" or nber[2] != "nber_macroeconomics_annual":
        raise SystemExit(f"Stern NBER Macro row {nber}")
    return rows


def load_shanghai() -> list[list]:
    def note_for(row: dict[str, str]) -> str:
        return row["source_note"]

    packed = load_grade_freeze(
        SHANGHAI_RELEASE,
        stem="shanghai",
        years=tuple(str(year) for year in SHANGHAI_YEARS),
        ratings=SHANGHAI_RATINGS,
        expected={str(year): SHANGHAI_EXPECTED[year] for year in SHANGHAI_YEARS},
        source_file="shanghai-top-journals",
        source_note_for=note_for,
        edition_for=lambda year: year,
        system="shanghai",
        unmatched_rows=2,
        conflict_rows=0,
        long_rows_expected=LIST_COUNTS["shanghai"],
    )
    header, raw = read_csv(SHANGHAI_RELEASE / "shanghai_long.csv")
    del header
    for row in raw:
        if row["source_note"] not in SHANGHAI_NOTES:
            raise SystemExit(f"Shanghai source_note {row['source_note']!r}")
        parts = [part.strip() for part in row["field"].split(";")]
        if not parts or any(part not in SHANGHAI_SUBJECTS for part in parts):
            raise SystemExit(f"Shanghai field {row['field']!r} on {row['journal_title']}")
    latest = [row for row in packed if row[1] == 2026]
    by_title = {row[3].casefold(): row for row in latest}
    aer = by_title.get("american economic review")
    if not aer or aer[4] != "Top" or aer[2] != "aer" or aer[5] != "Economics":
        raise SystemExit(f"Shanghai 2026 AER row {aer}")
    econ_ids = {row[2] for row in latest if row[5] == "Economics"}
    if econ_ids != {"aer", "econometrica", "jpe", "qje", "restud"}:
        raise SystemExit(f"Shanghai 2026 Economics ids {sorted(econ_ids)}")
    amj = by_title.get("academy of management journal")
    if not amj or amj[2] != "amj" or amj[5] != "Business Administration; Management":
        raise SystemExit(f"Shanghai 2026 AMJ row {amj}")
    earlier = [row for row in packed if row[1] == 2024]
    governance = next(
        (row for row in earlier if row[3].casefold().startswith("corporate governance")),
        None,
    )
    if not governance or governance[2] != "corporate_governance":
        raise SystemExit(f"Shanghai 2024 Corporate Governance row {governance}")
    return packed


def payload(
    loaded: dict[int, list[dict[str, str]]],
    list_rows: list[list],
    cnrs_rows: list[list],
    hb_rows: list[list],
    tilburg_rows: list[list],
    fnege_rows: list[list],
    erim_rows: list[list],
    stern_rows: list[list],
    shanghai_rows: list[list],
    fnege_labels: dict[str, str],
    erim_labels: dict[str, str],
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
    rows.extend(tilburg_rows)
    rows.extend(fnege_rows)
    rows.extend(erim_rows)
    rows.extend(stern_rows)
    rows.extend(shanghai_rows)
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
            {"id": "tilburg", "label": "Tilburg"},
            {"id": "fnege", "label": "FNEGE"},
            {"id": "erim", "label": "ERIM"},
            {"id": "stern", "label": "Stern"},
            {"id": "shanghai", "label": "Shanghai"},
        ],
        "editions": {
            "abs_ajg": list(EDITIONS),
            "cnrs": list(CNRS_YEARS),
            "handelsblatt_vwl": list(HB_YEARS),
            "ft50": ["Apr 2026"],
            "utd24": ["Current"],
            "top5": ["Current"],
            "abdc": [ABDC_EDITION],
            "tilburg": ["Current"],
            "fnege": list(FNEGE_YEARS),
            "erim": [ERIM_EDITION],
            "stern": [2020],
            "shanghai": list(SHANGHAI_YEARS),
        },
        "ratings": {
            "abs_ajg": ["4*", "4", "3", "2", "1"],
            "cnrs": list(CNRS_RATINGS),
            "handelsblatt_vwl": list(HB_RATINGS),
            "ft50": [],
            "utd24": [],
            "top5": [],
            "abdc": ["A*", "A", "B", "C"],
            "tilburg": list(TILBURG_RATINGS),
            "fnege": list(FNEGE_RATINGS),
            "erim": list(ERIM_RATINGS),
            "stern": list(STERN_RATINGS),
            "shanghai": list(SHANGHAI_RATINGS),
        },
        "subjectLabels": SUBJECT_LABELS,
        "fieldLabels": {
            "fnege": fnege_labels,
            "erim": erim_labels,
        },
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
        "journals/rankings/tilburg/releases/rankings_tilburg_20261025/, "
        "journals/rankings/fnege/releases/rankings_fnege_20261025/, "
        "journals/rankings/erim/releases/rankings_erim_20261025/, "
        "journals/rankings/stern/releases/rankings_stern_20261025/, "
        "journals/rankings/shanghai/releases/rankings_shanghai_20261025/, "
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
    tilburg_rows = load_tilburg()
    fnege_rows, fnege_labels = load_fnege()
    erim_rows, erim_labels = load_erim()
    stern_rows = load_stern()
    shanghai_rows = load_shanghai()
    body = payload(
        loaded,
        list_rows,
        cnrs_rows,
        hb_rows,
        tilburg_rows,
        fnege_rows,
        erim_rows,
        stern_rows,
        shanghai_rows,
        fnege_labels,
        erim_labels,
    )
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
        f"2015 {HB_EXPECTED[2015]['rows']:,}). "
        f"Tilburg {LIST_COUNTS['tilburg']} "
        f"({TILBURG_EXPECTED['mapped']} matched, {TILBURG_EXPECTED['match_pct']}%). "
        f"FNEGE {LIST_COUNTS['fnege']:,} "
        f"(2025 {FNEGE_EXPECTED[2025]['rows']:,} journals, "
        f"{FNEGE_EXPECTED[2025]['mapped']:,} matched, {FNEGE_EXPECTED[2025]['match_pct']}%). "
        f"ERIM {LIST_COUNTS['erim']} "
        f"({ERIM_EXPECTED['mapped']} matched, {ERIM_EXPECTED['match_pct']}%). "
        f"Stern {LIST_COUNTS['stern']} "
        f"({STERN_EXPECTED['mapped']} matched, {STERN_EXPECTED['match_pct']}%). "
        f"Shanghai {LIST_COUNTS['shanghai']} "
        f"(2026 {SHANGHAI_EXPECTED[2026]['rows']} journals, "
        f"{SHANGHAI_EXPECTED[2026]['mapped']} matched, {SHANGHAI_EXPECTED[2026]['match_pct']}%; "
        f"2024 {SHANGHAI_EXPECTED[2024]['rows']})."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
