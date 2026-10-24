#!/usr/bin/env python3
"""Build the public editor directory (site/data.js) from current releases.

The site lists current FT50 and ABDC editorial-board appointments only.
core49 is not a source. Authors are not included.

Identity
--------
One displayed row is one appointment: a person, in one role, on one journal.
The same person on two journals is two rows. The same person in two roles on
one journal is two rows.

The identity key is:

    norm_name(editor_name) + norm_journal(journal) + norm_role(role)

* norm_name: strip contact details, turn periods and commas into spaces,
  collapse whitespace, Unicode-casefold.
* norm_journal / norm_role: strip contact details, collapse whitespace,
  Unicode-casefold. Hyphens are kept, so "Coeditors" and "Co-Editors" stay
  distinct if the mastheads actually differ.

Cross-list collapse (FT50 and ABDC)
------------------------------------
Every current FT50 appointment is also in the ABDC A* or ABDC A release
(the ABDC panels were seeded from FT50 where the journals overlap). That is
one seat, not two.

When a key is in FT50 and in exactly one ABDC row, the build emits one row
tagged with both universes (for example FT50 and ABDC A*). Display fields
come from ``editors_ft50_current_with_ror.csv``. A blank affiliation,
country, continent, role, or source URL is filled from the ABDC row.
A non-empty FT50 value is not replaced. This prefers the FT50 text on the
handful of rows where the ABDC ROR match disagrees with the FT50 affiliation.

Subset lists (Top 5 and UTD24)
------------------------------
Top 5 and UTD24 are extra tags on those same rows. They do not add a release
file and they do not scrape. Membership is ``journals/catalog_top5.csv`` and
``journals/catalog_utd24.csv``.

Top 5 is the Editor-Collector ``is_top5`` set: American Economic Review,
Econometrica, Journal of Political Economy, Quarterly Journal of Economics,
and Review of Economic Studies. All five are in the FT50 current release, so
every Top 5 row also carries the FT50 bit.

UTD24 is the UT Dallas Naveen Jindal list of 24 business journals
(https://jsom.utdallas.edu/the-utd-top-100-business-school-research-rankings/list-of-journals).
Twenty-three are tagged from the FT50 freeze. INFORMS Journal on Computing
(the UTD label is Journal on Computing) is tagged from the ABDC A freeze.
Journal of Applied Psychology is on FT50 and is absent from the UTD24 catalog.
Journal of Management is likewise on FT50 and absent from UTD24.

Universe bits: FT50 1, ABDC A* 2, ABDC A 4, ABDC B 8, ABDC C 16, Top 5 32,
UTD24 64.

Within one release file
-----------------------
Rows that share a key and the same affiliation signature (ROR id, else the
normalized display affiliation) collapse to one row. The richer row is kept
(ROR id, then higher ``ror_confidence``, then a non-empty affiliation).

The same key with two different non-empty affiliations is kept as two rows.
Those are either two people who share a name or one masthead line that lists
two institutions. An extra blank-affiliation copy is dropped when the same
key already has a non-empty affiliation.

Display affiliation is ``ror_name``, else ``canonical_name``, else
``raw_affiliation``. Country and continent are ``ror_country`` and
``continent`` as released (including the small "Australasia" label). If
``journal`` is blank, the ABDC catalog name for ``abdc_journal_id`` is used.

Emails and phone numbers are removed from displayed text. A row whose name
is only a phone number or an email address is dropped. ORCID, OpenAlex,
RePEc, coordinates, and photos are not written to the site.

Project Pages
-------------
The published URL is https://kochiuyu.github.io/econ-journal-dispersion/
``site/`` uses relative asset URLs so that path and a local
``python -m http.server -d site`` serve the same files. Do not switch those
references to root-absolute paths (``/style.css``); on project Pages those
resolve at the user-site root instead of ``/econ-journal-dispersion/``.

``main`` also writes ``site/journals-data.js`` and ``site/institutions-data.js``
from those collapsed appointments, then runs ``scripts/build_rankings.py``,
which writes ``site/rankings-data.js``. Journals and institutions regroup the
same boards. They do not add directory chips. Rankings are journal grades
(ABS/AJG), not appointments.

Journal and institution pages
-----------------------------
``site/journals-data.js`` is one row per journal display name, the same string
the directory's journal filter uses. Counts are appointments, distinct editor
names, and distinct countries. List badges are the union of those appointment
masks. ABDC ``field_for`` is joined from the journal catalogs on ``journal_id``
(the release id, or the FT50 catalog id when the names match), otherwise on
the normalized journal name. The board link is the most common ``source_url``
on that journal, or the catalog ``board_url`` when the release has none.

``site/institutions-data.js`` is one row per institution. The key is ``ror_id``
when the collapsed row has one, otherwise the normalized affiliation
(whitespace collapsed, Unicode-casefold). The display name is the most common
affiliation string for that key. Country and continent are the most common
non-empty values. Appointments with no ROR id and no affiliation are omitted.
"""

from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "site"
DATA_JS = SITE_DIR / "data.js"
JOURNALS_JS = SITE_DIR / "journals-data.js"
INSTITUTIONS_JS = SITE_DIR / "institutions-data.js"

# Served at https://kochiuyu.github.io/econ-journal-dispersion/
PAGES_BASE = "/econ-journal-dispersion/"
REPO_URL = "https://github.com/kochiuyu/econ-journal-dispersion"
LIVE_URL = "https://kochiuyu.github.io/econ-journal-dispersion/"

FT50_CANDIDATES = (
    ROOT / "data/editors/ft50/releases/current/editors_ft50_current_with_ror.csv",
    ROOT / "data/editors/ft50/releases/current/editors_ft50_current.csv",
)
ABDC_FILES = (
    ("a_star", ROOT / "data/editors/abdc/releases/current/editors_abdc_a_star_current.csv"),
    ("a", ROOT / "data/editors/abdc/releases/current/editors_abdc_a_current.csv"),
    ("b", ROOT / "data/editors/abdc/releases/current/editors_abdc_b_current.csv"),
    ("c", ROOT / "data/editors/abdc/releases/current/editors_abdc_c_current.csv"),
)
CATALOG_FILES = (
    ROOT / "journals/catalog_abdc_a_star.csv",
    ROOT / "journals/catalog_abdc_a.csv",
    ROOT / "journals/catalog_abdc_b.csv",
    ROOT / "journals/catalog_abdc_c.csv",
    ROOT / "journals/catalog_ft50.csv",
)
TOP5_CATALOG = ROOT / "journals/catalog_top5.csv"
UTD24_CATALOG = ROOT / "journals/catalog_utd24.csv"
FT50_CATALOG = ROOT / "journals/catalog_ft50.csv"
ABDC_A_CATALOG = ROOT / "journals/catalog_abdc_a.csv"
UTD24_SOURCE_URL = (
    "https://jsom.utdallas.edu/the-utd-top-100-business-school-research-rankings/list-of-journals"
)
# Locked to journals/catalog_top5.csv. Editor-Collector is_top5.
TOP5_IDS = frozenset({"aer", "econometrica", "jpe", "qje", "restud"})
# Locked to journals/catalog_utd24.csv. Official UTD list order is in that file.
UTD24_IDS = frozenset(
    {
        "tar",
        "jae",
        "jar",
        "jf",
        "jfe",
        "rfs",
        "isr",
        "informs_journal_computing",
        "misq",
        "jcr",
        "jm",
        "jmr",
        "mktg_sci",
        "ms",
        "or",
        "joom",
        "msom",
        "pom",
        "amj",
        "amr",
        "asq",
        "orgsci",
        "jibs",
        "smj",
    }
)
UTD24_ABDC_ONLY_ID = "informs_journal_computing"
# FT50 journals that must stay off the UTD24 chip.
NOT_UTD24_IDS = frozenset({"jap", "jom"})
UTD24_ALIAS = {
    "rfs": "The Review of Financial Studies",
    "informs_journal_computing": "Journal on Computing",
}

UNIVERSE_ORDER = ("ft50", "a_star", "a", "b", "c", "top5", "utd24")
UNIVERSE_META = (
    {"id": "ft50", "label": "FT50", "bit": 1},
    {"id": "a_star", "label": "ABDC A*", "bit": 2},
    {"id": "a", "label": "ABDC A", "bit": 4},
    {"id": "b", "label": "ABDC B", "bit": 8},
    {"id": "c", "label": "ABDC C", "bit": 16},
    {"id": "top5", "label": "Top 5", "bit": 32},
    {"id": "utd24", "label": "UTD24", "bit": 64},
)
BITS = {item["id"]: item["bit"] for item in UNIVERSE_META}

FAMILIES = (
    "Editor-in-Chief",
    "Editor",
    "Co-Editor",
    "Senior Editor",
    "Managing Editor",
    "Associate Editor",
    "Guest / Special Issue Editor",
    "Editorial Board",
    "Review Board",
    "Advisory Board",
    "Other",
)
FAMILY_INDEX = {name: i for i, name in enumerate(FAMILIES)}

CONF_RANK = {"high": 3, "medium": 2, "low": 1}

EMAIL_RE = re.compile(r"[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}", re.IGNORECASE)
INTL_PHONE_RE = re.compile(r"\+\d{1,3}(?:[\s()./\-]*\d){2,}")
NANP_RE = re.compile(r"\b\d{3}[.\-\s]\d{3}[.\-\s]\d{4}\b")
LABELED_PHONE_RE = re.compile(
    r"\b(?:telephone|phone|mobile|fax|tel)\s*[:.]?\s*\+?(?:\d[\d\s()./\-]{5,})",
    re.IGNORECASE,
)
LEFTOVER_LABEL_RE = re.compile(
    r"\b(?:e-?mail|telephone|phone|mobile|fax|tel)\s*[:.]?",
    re.IGNORECASE,
)
MAILTO_RE = re.compile(r"\bmailto:\s*", re.IGNORECASE)
CONTACT_ASSERT_RE = re.compile(
    r"@|\bmailto:|\b(?:telephone|phone|mobile|fax)\s*[:.]",
    re.IGNORECASE,
)
LETTER_RE = re.compile(r"[A-Za-z\u00C0-\u024F\u0400-\u04FF\u4E00-\u9FFF]")
BAD_NAME_RE = re.compile(
    r"^(?:phone|fax|tel|email|e-mail|n/?a|none|unknown|null|test|editor|editorial)$",
    re.IGNORECASE,
)
ROOT_ABSOLUTE_RE = re.compile(r"""(?:href|src)\s*=\s*["'](/[^"']*)["']""")


@dataclass
class Rec:
    name: str
    name_key: str
    role: str
    role_key: str
    journal: str
    journal_key: str
    origin: str
    universes: set[str] = field(default_factory=set)
    affiliation: str = ""
    country: str = ""
    continent: str = ""
    url: str = ""
    ror_id: str = ""
    confidence: str = ""
    journal_id: str = ""

    def mask(self) -> int:
        bits = 0
        for universe in self.universes:
            bits |= BITS[universe]
        return bits


def scrub(text: str) -> str:
    """Remove emails and phone numbers from a masthead field."""
    if not text:
        return ""
    cleaned = text.replace("\u00a0", " ")
    cleaned = EMAIL_RE.sub(" ", cleaned)
    cleaned = MAILTO_RE.sub(" ", cleaned)
    cleaned = LABELED_PHONE_RE.sub(" ", cleaned)
    cleaned = INTL_PHONE_RE.sub(" ", cleaned)
    cleaned = NANP_RE.sub(" ", cleaned)
    cleaned = LEFTOVER_LABEL_RE.sub(" ", cleaned)
    cleaned = re.sub(r"\bE\s*:", " ", cleaned)
    cleaned = cleaned.replace("|", " ")
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = cleaned.strip(" \t,;:/-")
    return cleaned


def norm_space(text: str) -> str:
    return " ".join((text or "").replace("\u00a0", " ").split()).casefold()


def norm_name(text: str) -> str:
    text = scrub(text)
    text = text.replace(".", " ").replace(",", " ")
    return norm_space(text)


def norm_plain(text: str) -> str:
    return norm_space(scrub(text))


def usable_name(text: str) -> str:
    name = scrub(text)
    if len(name) < 2 or not LETTER_RE.search(name) or BAD_NAME_RE.match(name):
        return ""
    return name


def fold_match(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text.casefold())
    return "".join(ch for ch in decomposed if not unicodedata.combining(ch))


def role_family(role: str) -> str:
    """Group masthead titles for the role filter. The table still shows the original wording."""
    raw = " ".join(role.split())
    folded = fold_match(raw)
    if any(token in raw for token in ("主编",)):
        return "Editor-in-Chief"
    if any(token in raw for token in ("编委", "编辑")):
        return "Editorial Board"

    def has(*phrases: str) -> bool:
        return any(phrase in folded for phrase in phrases)

    if has("editor-in-chief", "editor in chief", "chief editor", "editeur en chef", "redacteur en chef"):
        return "Editor-in-Chief"
    if has("co-editor", "coeditor", "co editor"):
        return "Co-Editor"
    if has("associate editor"):
        return "Associate Editor"
    if has("managing editor"):
        return "Managing Editor"
    if has("senior editor"):
        return "Senior Editor"
    if has("guest editor", "special issue", "special-issue"):
        return "Guest / Special Issue Editor"
    if has("review board", "reviewer", "board of review", "review panel"):
        return "Review Board"
    if has(
        "advisory",
        "advisor",
        "adviser",
        "scientific board",
        "scientific committee",
        "comite scientifique",
    ):
        return "Advisory Board"
    if has(
        "editorial board",
        "board of editor",
        "comite de redaction",
        "comite editorial",
        "membre du comite",
        "redakc",
        "редакцион",
    ):
        return "Editorial Board"
    if "editor" in folded or "editeur" in folded:
        return "Editor"
    return "Other"


def clean_url(url: str) -> str:
    url = (url or "").strip()
    lowered = url.casefold()
    if lowered.startswith("http://") or lowered.startswith("https://"):
        return url
    return ""


def display_affiliation(row: dict[str, str]) -> str:
    for key in ("ror_name", "canonical_name", "raw_affiliation"):
        text = scrub(row.get(key) or "")
        if text:
            return text
    return ""


def richness(rec: Rec) -> tuple[int, int, int, int, int, int]:
    return (
        1 if rec.ror_id else 0,
        CONF_RANK.get((rec.confidence or "").casefold(), 0),
        1 if rec.affiliation else 0,
        1 if rec.country else 0,
        1 if rec.url else 0,
        len(rec.affiliation),
    )


def signature(rec: Rec) -> tuple[str, str]:
    if rec.ror_id:
        return ("ror", rec.ror_id)
    if rec.affiliation:
        return ("aff", norm_space(rec.affiliation))
    return ("empty", "")


def fill_blanks(primary: Rec, other: Rec) -> None:
    """Union universes. Copy affiliation and geography only into empty FT50 fields."""
    primary.universes |= other.universes
    if not primary.affiliation and other.affiliation:
        primary.affiliation = other.affiliation
    if not primary.country and other.country:
        primary.country = other.country
    if not primary.continent and other.continent:
        primary.continent = other.continent
    if not primary.url and other.url:
        primary.url = other.url
    if not primary.role and other.role:
        primary.role = other.role
        primary.role_key = other.role_key
    if not primary.journal_id and other.journal_id:
        primary.journal_id = other.journal_id
    # Keep a ROR id only when it belongs to the affiliation we are showing.
    if not primary.ror_id and other.ror_id and (
        not primary.affiliation or norm_space(primary.affiliation) == norm_space(other.affiliation)
    ):
        primary.ror_id = other.ror_id
        if not primary.confidence and other.confidence:
            primary.confidence = other.confidence


def prefer_display(current: Rec, challenger: Rec) -> Rec:
    current.universes |= challenger.universes
    challenger.universes |= current.universes
    if current.journal_id and not challenger.journal_id:
        challenger.journal_id = current.journal_id
    elif challenger.journal_id and not current.journal_id:
        current.journal_id = challenger.journal_id
    if richness(challenger) > richness(current):
        challenger.universes = set(current.universes)
        return challenger
    return current


@dataclass
class Membership:
    """Extra universe tags keyed by release journal id and by display name."""

    by_id: dict[str, set[str]]
    by_name: dict[str, set[str]]
    id_to_name: dict[str, str]
    names: dict[str, set[str]]
    ids: set[str]

    def tag(self, journal_id: str, journal: str) -> set[str]:
        if journal_id:
            expected = self.id_to_name.get(journal_id)
            if expected is not None and norm_plain(journal) != norm_plain(expected):
                raise SystemExit(
                    f"{journal_id} is {journal!r} in the release and {expected!r} in the membership catalog"
                )
            return set(self.by_id.get(journal_id, ()))
        return set(self.by_name.get(norm_plain(journal), ()))


def read_catalog_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing catalog: {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def catalog_by_id(path: Path) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for row in read_catalog_rows(path):
        journal_id = (row.get("journal_id") or "").strip()
        if not journal_id:
            raise SystemExit(f"Blank journal_id in {path.relative_to(ROOT)}")
        if journal_id in rows:
            raise SystemExit(f"Duplicate journal_id {journal_id} in {path.relative_to(ROOT)}")
        rows[journal_id] = row
    return rows


def load_membership() -> Membership:
    """Load Top 5 and UTD24 catalogs and check them against the host catalogs."""
    ft50 = catalog_by_id(FT50_CATALOG)
    abdc_a = catalog_by_id(ABDC_A_CATALOG)
    hosts = {"ft50": ft50, "abdc_a": abdc_a}
    by_id: dict[str, set[str]] = defaultdict(set)
    by_name: dict[str, set[str]] = defaultdict(set)
    id_to_name: dict[str, str] = {}
    names: dict[str, set[str]] = {"top5": set(), "utd24": set()}

    def bind(universe: str, journal_id: str, journal_name: str) -> None:
        key = norm_plain(journal_name)
        if not key:
            raise SystemExit(f"Blank journal name for {universe} id {journal_id}")
        previous = id_to_name.get(journal_id)
        if previous is not None and norm_plain(previous) != key:
            raise SystemExit(
                f"{journal_id} has two membership names: {previous!r} and {journal_name!r}"
            )
        id_to_name[journal_id] = journal_name
        by_id[journal_id].add(universe)
        by_name[key].add(universe)
        names[universe].add(journal_name)

    top5_rows = read_catalog_rows(TOP5_CATALOG)
    top5_ids = []
    for row in top5_rows:
        journal_id = (row.get("journal_id") or "").strip()
        ft50_journal_id = (row.get("ft50_journal_id") or "").strip()
        journal_name = (row.get("journal_name") or "").strip()
        issn = (row.get("issn") or "").strip()
        if journal_id != ft50_journal_id:
            raise SystemExit(f"Top 5 {journal_id} does not point at itself in the FT50 catalog")
        host = ft50.get(journal_id)
        if host is None:
            raise SystemExit(f"Top 5 id {journal_id} is not in {FT50_CATALOG.name}")
        if journal_name != (host.get("journal_name") or "").strip():
            raise SystemExit(
                f"Top 5 name {journal_name!r} does not match the FT50 catalog name for {journal_id}"
            )
        if issn != (host.get("issn") or "").strip():
            raise SystemExit(f"Top 5 ISSN for {journal_id} does not match the FT50 catalog")
        bind("top5", journal_id, journal_name)
        top5_ids.append(journal_id)
    if len(top5_ids) != len(set(top5_ids)):
        raise SystemExit("Duplicate journal_id in catalog_top5.csv")
    if frozenset(top5_ids) != TOP5_IDS:
        raise SystemExit(f"catalog_top5.csv ids {sorted(top5_ids)} != {sorted(TOP5_IDS)}")

    utd_rows = read_catalog_rows(UTD24_CATALOG)
    utd_ids = []
    abdc_only = []
    for row in utd_rows:
        journal_id = (row.get("journal_id") or "").strip()
        host_journal_id = (row.get("host_journal_id") or "").strip()
        host_list = (row.get("host_list") or "").strip()
        journal_name = (row.get("journal_name") or "").strip()
        utd_name = (row.get("utd_name") or "").strip()
        issn = (row.get("issn") or "").strip()
        source = (row.get("list_source_url") or "").strip()
        if journal_id != host_journal_id:
            raise SystemExit(f"UTD24 {journal_id} host_journal_id is {host_journal_id}")
        if host_list not in hosts:
            raise SystemExit(f"UTD24 {journal_id} host_list {host_list!r} is not ft50 or abdc_a")
        if source != UTD24_SOURCE_URL:
            raise SystemExit(f"UTD24 {journal_id} list_source_url is not the official journal list")
        if not utd_name:
            raise SystemExit(f"UTD24 {journal_id} is missing utd_name")
        host = hosts[host_list].get(journal_id)
        if host is None:
            raise SystemExit(f"UTD24 id {journal_id} is not in the {host_list} catalog")
        if journal_name != (host.get("journal_name") or "").strip():
            raise SystemExit(
                f"UTD24 name {journal_name!r} does not match the {host_list} catalog name for {journal_id}"
            )
        if issn != (host.get("issn") or "").strip():
            raise SystemExit(f"UTD24 ISSN for {journal_id} does not match the {host_list} catalog")
        alias = UTD24_ALIAS.get(journal_id)
        if alias is None and utd_name != journal_name:
            raise SystemExit(f"UTD24 label {utd_name!r} differs from the freeze name for {journal_id}")
        if alias is not None and utd_name != alias:
            raise SystemExit(f"UTD24 label for {journal_id} should be {alias!r}, found {utd_name!r}")
        if journal_id in NOT_UTD24_IDS:
            raise SystemExit(f"{journal_id} is on FT50 and must stay off UTD24")
        bind("utd24", journal_id, journal_name)
        utd_ids.append(journal_id)
        if host_list == "abdc_a":
            abdc_only.append(journal_id)
    if len(utd_ids) != len(set(utd_ids)):
        raise SystemExit("Duplicate journal_id in catalog_utd24.csv")
    if frozenset(utd_ids) != UTD24_IDS:
        raise SystemExit(f"catalog_utd24.csv ids {sorted(utd_ids)} != {sorted(UTD24_IDS)}")
    if abdc_only != [UTD24_ABDC_ONLY_ID]:
        raise SystemExit(
            "UTD24 should take only INFORMS Journal on Computing from ABDC A, "
            f"found {abdc_only}"
        )
    if NOT_UTD24_IDS & set(utd_ids):
        raise SystemExit("Journal of Applied Psychology or Journal of Management is tagged UTD24")
    if set(top5_ids) & set(utd_ids):
        raise SystemExit(f"Top 5 and UTD24 share journal ids: {sorted(set(top5_ids) & set(utd_ids))}")

    return Membership(
        by_id=by_id,
        by_name=by_name,
        id_to_name=id_to_name,
        names=names,
        ids=set(id_to_name),
    )


def load_catalog_names() -> dict[str, str]:
    names: dict[str, str] = {}
    for path in CATALOG_FILES:
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8-sig") as handle:
            for row in csv.DictReader(handle):
                journal_id = (row.get("journal_id") or "").strip()
                journal_name = scrub(row.get("journal_name") or "")
                if journal_id and journal_name and journal_id not in names:
                    names[journal_id] = journal_name
    return names


@dataclass
class JournalCatalog:
    """Catalog field and board URL, keyed by journal id and normalized name."""

    by_id: dict[str, dict[str, str]]
    by_name: dict[str, dict[str, str]]


def load_journal_catalog() -> JournalCatalog:
    """Join ABDC field_for and board_url onto release journal names.

    ABDC catalogs are read first so ``field_for`` sticks. FT50 names are then
    indexed onto the same id, which is how "American Economic Review" picks up
    the field stored under "The American Economic Review".
    """
    by_id: dict[str, dict[str, str]] = {}
    by_name: dict[str, dict[str, str]] = {}
    paths = (
        ROOT / "journals/catalog_abdc_a_star.csv",
        ROOT / "journals/catalog_abdc_a.csv",
        ROOT / "journals/catalog_abdc_b.csv",
        ROOT / "journals/catalog_abdc_c.csv",
        FT50_CATALOG,
    )
    for path in paths:
        if not path.exists():
            raise SystemExit(f"Missing catalog: {path.relative_to(ROOT)}")
        for row in read_catalog_rows(path):
            journal_id = (row.get("journal_id") or "").strip()
            name = scrub(row.get("journal_name") or "")
            field_for = scrub(row.get("field_for") or "")
            board = clean_url(row.get("board_url") or "")
            if not journal_id or not name:
                continue
            meta = by_id.get(journal_id)
            if meta is None:
                meta = {"id": journal_id, "field": field_for, "board": board, "name": name}
                by_id[journal_id] = meta
            else:
                if field_for and not meta["field"]:
                    meta["field"] = field_for
                if board and not meta["board"]:
                    meta["board"] = board
            key = norm_plain(name)
            if key and key not in by_name:
                by_name[key] = meta
    return JournalCatalog(by_id=by_id, by_name=by_name)


def catalog_meta(rec: Rec, catalog: JournalCatalog) -> dict[str, str]:
    if rec.journal_id and rec.journal_id in catalog.by_id:
        return catalog.by_id[rec.journal_id]
    return catalog.by_name.get(rec.journal_key) or {}


def resolve_ft50_path() -> Path:
    for path in FT50_CANDIDATES:
        if path.exists():
            return path
    raise SystemExit(
        "Missing FT50 release. Expected one of:\n"
        + "\n".join(f"  {path.relative_to(ROOT)}" for path in FT50_CANDIDATES)
    )


def journal_name(row: dict[str, str], catalogs: dict[str, str]) -> str:
    name = scrub(row.get("journal") or "")
    if name:
        return name
    journal_id = (row.get("abdc_journal_id") or "").strip()
    if journal_id and journal_id in catalogs:
        return catalogs[journal_id]
    return ""


def row_to_rec(
    row: dict[str, str],
    origin: str,
    catalogs: dict[str, str],
    membership: Membership,
    catalog: JournalCatalog,
) -> Rec | None:
    name = usable_name(row.get("editor_name") or "")
    if not name:
        return None
    journal = journal_name(row, catalogs)
    if not journal:
        return None
    role = scrub(row.get("role") or "")
    affiliation = display_affiliation(row)
    # If scrubbing left only a label fragment, don't publish it as an affiliation.
    if affiliation and not LETTER_RE.search(affiliation):
        affiliation = ""
    if CONTACT_ASSERT_RE.search(affiliation):
        affiliation = scrub(affiliation)
        if CONTACT_ASSERT_RE.search(affiliation):
            affiliation = ""
    journal_id = (row.get("abdc_journal_id") or "").strip()
    if not journal_id:
        named = catalog.by_name.get(norm_plain(journal))
        if named:
            journal_id = named["id"]
    universes = {origin}
    universes |= membership.tag(journal_id, journal)
    return Rec(
        name=name,
        name_key=norm_name(name),
        role=role,
        role_key=norm_plain(role),
        journal=journal,
        journal_key=norm_plain(journal),
        origin=origin,
        universes=universes,
        affiliation=affiliation,
        country=scrub(row.get("ror_country") or ""),
        continent=scrub(row.get("continent") or ""),
        url=clean_url(row.get("source_url") or ""),
        ror_id=(row.get("ror_id") or "").strip(),
        confidence=(row.get("ror_confidence") or "").strip(),
        journal_id=journal_id,
    )


def read_release(
    path: Path,
    origin: str,
    catalogs: dict[str, str],
    dates: list[str],
    years: set[str],
    membership: Membership,
    seen_membership_ids: set[str],
    catalog: JournalCatalog,
) -> tuple[list[Rec], int]:
    records: list[Rec] = []
    dropped = 0
    with path.open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            collected = (row.get("collection_date") or "").strip()
            if collected:
                dates.append(collected)
            year = (row.get("year") or "").strip()
            if year:
                years.add(year)
            journal_id = (row.get("abdc_journal_id") or "").strip()
            if journal_id in membership.ids:
                seen_membership_ids.add(journal_id)
            rec = row_to_rec(row, origin, catalogs, membership, catalog)
            if rec is None:
                dropped += 1
                continue
            records.append(rec)
    return records, dropped


def cluster_rows(rows: list[Rec]) -> tuple[dict[tuple[str, str], Rec], list[Rec]]:
    clusters: dict[tuple[str, str], Rec] = {}
    empties: list[Rec] = []
    for rec in rows:
        sig = signature(rec)
        if sig[0] == "empty":
            empties.append(rec)
            continue
        current = clusters.get(sig)
        if current is None:
            clusters[sig] = rec
        else:
            clusters[sig] = prefer_display(current, rec)
    return clusters, empties


def collapse(groups: dict[tuple[str, str, str], list[Rec]]) -> tuple[list[Rec], dict[str, int]]:
    """Apply the cross-list and within-file rules. See the module docstring."""
    output: list[Rec] = []
    stats = {
        "cross_merged": 0,
        "ft50_only": 0,
        "split_keys": 0,
        "blank_aff_dropped": 0,
    }
    for recs in groups.values():
        ft_rows = [rec for rec in recs if rec.origin == "ft50"]
        other_rows = [rec for rec in recs if rec.origin != "ft50"]
        if ft_rows:
            primary = ft_rows[0]
            for extra in ft_rows[1:]:
                primary = prefer_display(primary, extra)
            clusters, empties = cluster_rows(other_rows)
            partner: Rec | None = None
            sig = signature(primary)
            if sig[0] != "empty" and sig in clusters:
                partner = clusters.pop(sig)
            elif len(clusters) == 1:
                partner = clusters.pop(next(iter(clusters)))
            elif not clusters and empties:
                partner = empties[0]
                for extra in empties[1:]:
                    partner = prefer_display(partner, extra)
                empties = []
            if partner is not None:
                fill_blanks(primary, partner)
                stats["cross_merged"] += 1
            else:
                stats["ft50_only"] += 1
            if clusters:
                stats["split_keys"] += 1
            stats["blank_aff_dropped"] += len(empties)
            output.extend(clusters.values())
            output.append(primary)
            continue

        clusters, empties = cluster_rows(other_rows)
        if clusters:
            if len(clusters) > 1:
                stats["split_keys"] += 1
            stats["blank_aff_dropped"] += len(empties)
            output.extend(clusters.values())
        elif empties:
            kept = empties[0]
            for extra in empties[1:]:
                kept = prefer_display(kept, extra)
            output.append(kept)
    return output, stats


class StringIndex:
    def __init__(self, first: str | None = None) -> None:
        self.values: list[str] = []
        self.lookup: dict[str, int] = {}
        if first is not None:
            self.add(first)

    def add(self, value: str) -> int:
        index = self.lookup.get(value)
        if index is None:
            index = len(self.values)
            self.values.append(value)
            self.lookup[value] = index
        return index


def assert_no_contacts(value: str, label: str) -> None:
    if value and CONTACT_ASSERT_RE.search(value):
        raise SystemExit(f"Contact detail survived in {label}: {value[:180]}")


def assert_static_site() -> None:
    html = (SITE_DIR / "index.html").read_text(encoding="utf-8")
    if PAGES_BASE not in html or LIVE_URL not in html:
        raise SystemExit("site/index.html is missing the project Pages URL")
    app = (SITE_DIR / "app.js").read_text(encoding="utf-8")
    if PAGES_BASE not in app:
        raise SystemExit("site/app.js is missing the project Pages base path")
    rankings = (SITE_DIR / "rankings.html").read_text(encoding="utf-8")
    if PAGES_BASE not in rankings or LIVE_URL not in rankings:
        raise SystemExit("site/rankings.html is missing the project Pages URL")
    if 'href="rankings.html"' not in html:
        raise SystemExit("site/index.html is missing the Rankings nav link")
    rankings_js = (SITE_DIR / "rankings.js").read_text(encoding="utf-8")
    if PAGES_BASE not in rankings_js:
        raise SystemExit("site/rankings.js is missing the project Pages base path")
    page_files = ("index.html", "journals.html", "institutions.html", "rankings.html")
    for name in page_files:
        text = (SITE_DIR / name).read_text(encoding="utf-8")
        if PAGES_BASE not in text or LIVE_URL not in text:
            raise SystemExit(f"site/{name} is missing the project Pages URL")
        for link in ("journals.html", "institutions.html", "rankings.html"):
            if f'href="{link}"' not in text:
                raise SystemExit(f"site/{name} is missing the {link} nav link")
    for script in ("journals.js", "institutions.js"):
        text = (SITE_DIR / script).read_text(encoding="utf-8")
        if PAGES_BASE not in text:
            raise SystemExit(f"site/{script} is missing the project Pages base path")
    for name in (
        "index.html",
        "app.js",
        "style.css",
        "rankings.html",
        "rankings.js",
        "journals.html",
        "journals.js",
        "institutions.html",
        "institutions.js",
    ):
        text = (SITE_DIR / name).read_text(encoding="utf-8")
        match = ROOT_ABSOLUTE_RE.search(text)
        if match:
            raise SystemExit(
                f"Root-absolute URL {match.group(1)} in site/{name}. "
                "Project Pages need relative asset paths under "
                f"{PAGES_BASE}"
            )


def build_payload(records: list[Rec], sources: list[str], dates: list[str], years: set[str]) -> dict:
    roles = StringIndex()
    role_family_idx: list[int] = []
    journals = StringIndex()
    countries = StringIndex("")
    continents = StringIndex("")
    urls = StringIndex("")

    def add_role(role: str) -> int:
        index = roles.add(role)
        if len(role_family_idx) == index:
            role_family_idx.append(FAMILY_INDEX[role_family(role)])
        return index

    rows: list[list] = []
    editor_keys: set[str] = set()
    country_keys: set[str] = set()
    journal_by_universe: dict[str, set[int]] = {uid: set() for uid in BITS}
    appointments_by_universe = {uid: 0 for uid in BITS}

    def sort_name(rec: Rec) -> str:
        # Leading punctuation would otherwise pin bad masthead fragments to the top.
        stripped = re.sub(r"^[^0-9a-z\u00c0-\u024f\u0400-\u04ff\u4e00-\u9fff]+", "", rec.name_key)
        return stripped or rec.name_key

    records.sort(key=lambda rec: (sort_name(rec), rec.journal_key, rec.role_key, norm_space(rec.affiliation), rec.name))

    for rec in records:
        for label, text in (
            ("name", rec.name),
            ("role", rec.role),
            ("journal", rec.journal),
            ("affiliation", rec.affiliation),
            ("country", rec.country),
            ("continent", rec.continent),
        ):
            assert_no_contacts(text, label)
        role_i = add_role(rec.role or "—")
        journal_i = journals.add(rec.journal)
        country_i = countries.add(rec.country)
        continent_i = continents.add(rec.continent)
        url_i = urls.add(rec.url)
        mask = rec.mask()
        rows.append(
            [
                rec.name,
                role_i,
                journal_i,
                mask,
                rec.affiliation,
                country_i,
                continent_i,
                url_i,
            ]
        )
        editor_keys.add(rec.name_key)
        if rec.country:
            country_keys.add(norm_space(rec.country))
        for universe, bit in BITS.items():
            if mask & bit:
                appointments_by_universe[universe] += 1
                journal_by_universe[universe].add(journal_i)

    collected = sorted(set(dates))
    by_universe = {
        uid: {
            "appointments": appointments_by_universe[uid],
            "journals": len(journal_by_universe[uid]),
        }
        for uid in UNIVERSE_ORDER
    }
    return {
        "base": PAGES_BASE,
        "liveUrl": LIVE_URL,
        "repo": REPO_URL,
        "readme": REPO_URL + "#readme",
        "year": sorted(years)[-1] if years else "",
        "years": sorted(years),
        "collectedMin": collected[0] if collected else "",
        "collectedMax": collected[-1] if collected else "",
        "sources": sources,
        "universes": list(UNIVERSE_META),
        "families": list(FAMILIES),
        "roles": roles.values,
        "roleFamily": role_family_idx,
        "journals": journals.values,
        "countries": countries.values,
        "continents": continents.values,
        "urls": urls.values,
        "rows": rows,
        "counts": {
            "appointments": len(rows),
            "editors": len(editor_keys),
            "journals": len(journals.values),
            "countries": len(country_keys),
            "byUniverse": by_universe,
        },
    }


def dump_js(global_name: str, payload: dict, comment: str) -> str:
    raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    raw = (
        raw.replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )
    return "/* " + comment + " */\nwindow." + global_name + " = " + raw + ";\n"


def js_payload(payload: dict) -> str:
    return dump_js(
        "EDITOR_DATA",
        payload,
        "Generated by scripts/build_site.py from the current FT50 and ABDC editor releases.\n"
        "   Top 5 and UTD24 are subset tags from journals/catalog_top5.csv and journals/catalog_utd24.csv.\n"
        "   Do not edit.",
    )


def assert_payload(payload: dict, collapse_stats: dict[str, int], ft50_kept: int) -> None:
    counts = payload["counts"]
    if counts["appointments"] < 100_000:
        raise SystemExit(f"Too few appointments: {counts['appointments']}")
    if counts["journals"] < 2_000:
        raise SystemExit(f"Too few journals: {counts['journals']}")
    if counts["countries"] < 100:
        raise SystemExit(f"Too few countries: {counts['countries']}")
    if counts["editors"] < 80_000:
        raise SystemExit(f"Too few editors: {counts['editors']}")
    ft50 = counts["byUniverse"]["ft50"]
    if ft50["journals"] != 50:
        raise SystemExit(f"Expected 50 FT50 journals, found {ft50['journals']}")
    if ft50["appointments"] != ft50_kept:
        raise SystemExit(
            f"FT50 appointments {ft50['appointments']} != kept FT50 rows {ft50_kept}"
        )
    if collapse_stats["ft50_only"] != 0:
        raise SystemExit(f"FT50 rows without an ABDC partner: {collapse_stats['ft50_only']}")
    if collapse_stats["cross_merged"] != ft50_kept:
        raise SystemExit(
            f"Merged overlap {collapse_stats['cross_merged']} != kept FT50 rows {ft50_kept}"
        )
    if collapse_stats["split_keys"] < 5:
        raise SystemExit("Expected same-name appointments with different affiliations to stay split")
    if payload["base"] != PAGES_BASE:
        raise SystemExit("data.js base path is not the project Pages path")
    # Every FT50 badge row must also carry an ABDC badge.
    ft50_bit = BITS["ft50"]
    abdc_bits = BITS["a_star"] | BITS["a"] | BITS["b"] | BITS["c"]
    for row in payload["rows"]:
        mask = row[3]
        if mask & ft50_bit and not (mask & abdc_bits):
            raise SystemExit(f"FT50 row missing an ABDC badge: {row[0]}")


def assert_subset_lists(payload: dict, membership: Membership) -> None:
    """Top 5 is inside FT50. UTD24 adds INFORMS Journal on Computing from ABDC A."""
    journals = payload["journals"]
    top5_bit = BITS["top5"]
    utd_bit = BITS["utd24"]
    ft50_bit = BITS["ft50"]
    a_bit = BITS["a"]
    top5_journals: set[str] = set()
    utd_journals: set[str] = set()
    ft50_journals: set[str] = set()
    joc_name = "INFORMS Journal on Computing"
    jap_name = "Journal of Applied Psychology"
    jom_name = "Journal of Management"
    joc_rows = 0
    jap_rows = 0
    jom_rows = 0
    for row in payload["rows"]:
        name = journals[row[2]]
        mask = row[3]
        if mask & ft50_bit:
            ft50_journals.add(name)
        if mask & top5_bit:
            if not (mask & ft50_bit):
                raise SystemExit(f"Top 5 appointment outside FT50: {row[0]} / {name}")
            top5_journals.add(name)
        if mask & utd_bit:
            utd_journals.add(name)
        if name == joc_name:
            joc_rows += 1
            if not (mask & utd_bit) or not (mask & a_bit) or (mask & ft50_bit):
                raise SystemExit(f"INFORMS Journal on Computing tag is wrong for {row[0]}: mask {mask}")
        elif mask & utd_bit and not (mask & ft50_bit):
            raise SystemExit(f"UTD24 appointment outside FT50 is not INFORMS Journal on Computing: {name}")
        if name == jap_name:
            jap_rows += 1
            if (mask & utd_bit) or (mask & top5_bit) or not (mask & ft50_bit):
                raise SystemExit(f"Journal of Applied Psychology must stay FT50 only: mask {mask}")
        if name == jom_name:
            jom_rows += 1
            if (mask & utd_bit) or not (mask & ft50_bit):
                raise SystemExit(f"Journal of Management must stay off UTD24: mask {mask}")
    if top5_journals != membership.names["top5"]:
        raise SystemExit(
            "Top 5 journals "
            f"{sorted(top5_journals)} != catalog {sorted(membership.names['top5'])}"
        )
    if utd_journals != membership.names["utd24"]:
        missing = sorted(membership.names["utd24"] - utd_journals)
        extra = sorted(utd_journals - membership.names["utd24"])
        raise SystemExit(f"UTD24 journal mismatch. Missing {missing}. Extra {extra}.")
    counts = payload["counts"]["byUniverse"]
    if counts["top5"]["journals"] != 5:
        raise SystemExit(f"Expected 5 Top 5 journals, found {counts['top5']['journals']}")
    if counts["utd24"]["journals"] != 24:
        raise SystemExit(f"Expected 24 UTD24 journals, found {counts['utd24']['journals']}")
    if counts["top5"]["appointments"] <= 0 or counts["top5"]["appointments"] >= counts["ft50"]["appointments"]:
        raise SystemExit(
            f"Top 5 appointments {counts['top5']['appointments']} are not a proper subset of "
            f"FT50 {counts['ft50']['appointments']}"
        )
    if not top5_journals <= ft50_journals:
        raise SystemExit(f"Top 5 journals outside FT50: {sorted(top5_journals - ft50_journals)}")
    utd_outside = utd_journals - ft50_journals
    if utd_outside != {joc_name}:
        raise SystemExit(f"UTD24 journals outside FT50: {sorted(utd_outside)}")
    if joc_rows < 100:
        raise SystemExit(f"Expected the ABDC A INFORMS Journal on Computing board, found {joc_rows} rows")
    if jap_rows == 0 or jom_rows == 0:
        raise SystemExit("Journal of Applied Psychology or Journal of Management dropped out of FT50")


def mode_text(counter: Counter[str], *, prefer_longer: bool = False) -> str:
    """Most common string. Ties break alphabetically, or toward the longer text."""
    if not counter:
        return ""

    def sort_key(item: tuple[str, int]) -> tuple:
        text, count = item
        if prefer_longer:
            return (-count, -len(text), text.casefold())
        return (-count, text.casefold())

    return sorted(counter.items(), key=sort_key)[0][0]


def shared_meta(directory: dict, page: str) -> dict:
    return {
        "base": PAGES_BASE,
        "liveUrl": LIVE_URL + page,
        "repo": REPO_URL,
        "readme": REPO_URL + "#readme",
        "year": directory["year"],
        "collectedMin": directory["collectedMin"],
        "collectedMax": directory["collectedMax"],
        "universes": list(UNIVERSE_META),
    }


def build_journal_payload(records: list[Rec], catalog: JournalCatalog, directory: dict) -> dict:
    """One row per directory journal name."""
    buckets: dict[str, dict] = {}
    editor_keys: set[str] = set()
    country_keys: set[str] = set()
    for rec in records:
        editor_keys.add(rec.name_key)
        if rec.country:
            country_keys.add(norm_space(rec.country))
        bucket = buckets.get(rec.journal)
        if bucket is None:
            bucket = {
                "name": rec.journal,
                "mask": 0,
                "appointments": 0,
                "editors": set(),
                "countries": set(),
                "urls": Counter(),
                "fields": Counter(),
                "boards": Counter(),
            }
            buckets[rec.journal] = bucket
        bucket["mask"] |= rec.mask()
        bucket["appointments"] += 1
        bucket["editors"].add(rec.name_key)
        if rec.country:
            bucket["countries"].add(rec.country)
        if rec.url:
            bucket["urls"][rec.url] += 1
        meta = catalog_meta(rec, catalog)
        field_for = meta.get("field") or ""
        board = meta.get("board") or ""
        if field_for:
            bucket["fields"][field_for] += 1
        if board:
            bucket["boards"][board] += 1

    fields = StringIndex("")
    urls = StringIndex("")
    rows: list[list] = []
    appointments_by_universe = {uid: 0 for uid in BITS}
    journals_by_universe: dict[str, int] = {uid: 0 for uid in BITS}
    missing_field = 0
    with_board = 0
    mixed_field = 0
    for name in sorted(buckets, key=lambda value: value.casefold()):
        bucket = buckets[name]
        if len(bucket["fields"]) > 1:
            mixed_field += 1
        field_for = mode_text(bucket["fields"])
        if not field_for:
            missing_field += 1
        url = mode_text(bucket["urls"]) or mode_text(bucket["boards"])
        if url:
            with_board += 1
        mask = bucket["mask"]
        rows.append(
            [
                bucket["name"],
                mask,
                bucket["appointments"],
                len(bucket["editors"]),
                len(bucket["countries"]),
                fields.add(field_for),
                urls.add(url),
            ]
        )
        for universe, bit in BITS.items():
            if mask & bit:
                appointments_by_universe[universe] += bucket["appointments"]
                journals_by_universe[universe] += 1

    if mixed_field:
        print(f"Journals with more than one ABDC field: {mixed_field}")
    by_universe = {
        uid: {
            "journals": journals_by_universe[uid],
            "appointments": appointments_by_universe[uid],
        }
        for uid in UNIVERSE_ORDER
    }
    payload = shared_meta(directory, "journals.html")
    payload.update(
        {
            "columns": [
                "journal",
                "mask",
                "appointments",
                "editors",
                "countries",
                "field",
                "url",
            ],
            "fields": fields.values,
            "urls": urls.values,
            "rows": rows,
            "counts": {
                "journals": len(rows),
                "appointments": sum(row[2] for row in rows),
                "editors": len(editor_keys),
                "countries": len(country_keys),
                "withBoard": with_board,
                "withField": len(rows) - missing_field,
                "missingField": missing_field,
                "byUniverse": by_universe,
            },
        }
    )
    return payload


def institution_key(rec: Rec) -> tuple[str, str] | None:
    if rec.ror_id:
        return ("ror", rec.ror_id)
    folded = norm_space(rec.affiliation)
    if folded:
        return ("aff", folded)
    return None


def build_institution_payload(records: list[Rec], directory: dict) -> dict:
    """One row per ROR id, else per normalized affiliation."""
    buckets: dict[tuple[str, str], dict] = {}
    for rec in records:
        key = institution_key(rec)
        if key is None:
            continue
        bucket = buckets.get(key)
        if bucket is None:
            bucket = {
                "ror": key[0] == "ror",
                "names": Counter(),
                "countries": Counter(),
                "continents": Counter(),
                "editors": set(),
                "journals": set(),
                "appointments": 0,
                "mask": 0,
                "by_universe": {uid: 0 for uid in BITS},
            }
            buckets[key] = bucket
        if rec.affiliation:
            bucket["names"][rec.affiliation] += 1
        if rec.country:
            bucket["countries"][rec.country] += 1
        if rec.continent:
            bucket["continents"][rec.continent] += 1
        bucket["editors"].add(rec.name_key)
        bucket["journals"].add(rec.journal)
        bucket["appointments"] += 1
        mask = rec.mask()
        bucket["mask"] |= mask
        for universe, bit in BITS.items():
            if mask & bit:
                bucket["by_universe"][universe] += 1

    countries = StringIndex("")
    continents = StringIndex("")
    prepared: list[dict] = []
    nameless = 0
    for bucket in buckets.values():
        name = mode_text(bucket["names"], prefer_longer=True)
        if not name:
            nameless += bucket["appointments"]
            continue
        prepared.append(
            {
                "name": name,
                "country": mode_text(bucket["countries"]),
                "continent": mode_text(bucket["continents"]),
                "editors": len(bucket["editors"]),
                "appointments": bucket["appointments"],
                "journals": len(bucket["journals"]),
                "mask": bucket["mask"],
                "ror": bucket["ror"],
                "by_universe": bucket["by_universe"],
                "editor_keys": bucket["editors"],
                "country_keys": set(bucket["countries"]),
            }
        )
    prepared.sort(key=lambda item: (item["name"].casefold(), item["country"].casefold(), item["continent"].casefold()))

    rows: list[list] = []
    editor_keys: set[str] = set()
    country_keys: set[str] = set()
    appointments_by_universe = {uid: 0 for uid in BITS}
    institutions_by_universe = {uid: 0 for uid in BITS}
    with_ror = 0
    emitted = 0
    for item in prepared:
        if item["ror"]:
            with_ror += 1
        editor_keys |= item["editor_keys"]
        for country in item["country_keys"]:
            if country:
                country_keys.add(norm_space(country))
        emitted += item["appointments"]
        mask = item["mask"]
        rows.append(
            [
                item["name"],
                countries.add(item["country"]),
                continents.add(item["continent"]),
                item["editors"],
                item["appointments"],
                item["journals"],
                mask,
            ]
        )
        for universe, bit in BITS.items():
            if mask & bit:
                appointments_by_universe[universe] += item["by_universe"][universe]
                institutions_by_universe[universe] += 1

    if nameless:
        print(f"Institution keys with no display name: {nameless} appointments")
    by_universe = {
        uid: {
            "institutions": institutions_by_universe[uid],
            "appointments": appointments_by_universe[uid],
        }
        for uid in UNIVERSE_ORDER
    }
    payload = shared_meta(directory, "institutions.html")
    payload.update(
        {
            "columns": [
                "institution",
                "country",
                "continent",
                "editors",
                "appointments",
                "journals",
                "mask",
            ],
            "countries": countries.values,
            "continents": continents.values,
            "rows": rows,
            "counts": {
                "institutions": len(rows),
                "appointments": emitted,
                "unmatchedAppointments": len(records) - emitted,
                "editors": len(editor_keys),
                "countries": len(country_keys),
                "withRor": with_ror,
                "byUniverse": by_universe,
            },
        }
    )
    return payload


def assert_aggregates(directory: dict, journals: dict, institutions: dict) -> None:
    dcounts = directory["counts"]
    jcounts = journals["counts"]
    icounts = institutions["counts"]
    if jcounts["journals"] != dcounts["journals"]:
        raise SystemExit(
            f"Journal rows {jcounts['journals']} != directory journals {dcounts['journals']}"
        )
    if jcounts["appointments"] != dcounts["appointments"]:
        raise SystemExit("Journal appointment total does not match the directory")
    if jcounts["editors"] != dcounts["editors"]:
        raise SystemExit("Journal editor total does not match the directory")
    if jcounts["countries"] != dcounts["countries"]:
        raise SystemExit("Journal country total does not match the directory")
    if jcounts["missingField"] > 40:
        raise SystemExit(f"Too many journals without an ABDC field: {jcounts['missingField']}")
    if jcounts["withBoard"] < jcounts["journals"] * 0.9:
        raise SystemExit(
            f"Only {jcounts['withBoard']} of {jcounts['journals']} journals have a board link"
        )
    directory_journals = set(directory["journals"])
    for row in journals["rows"]:
        if row[0] not in directory_journals:
            raise SystemExit(f"Journal {row[0]!r} is not in the directory journal list")
        for label, text in (("journal", row[0]),):
            assert_no_contacts(text, label)
    by_name = {row[0]: row for row in journals["rows"]}
    aer = by_name.get("American Economic Review")
    if aer is None:
        raise SystemExit("American Economic Review is missing from the journal aggregate")
    ft50_bit = BITS["ft50"]
    a_star_bit = BITS["a_star"]
    top5_bit = BITS["top5"]
    utd_bit = BITS["utd24"]
    a_bit = BITS["a"]
    if aer[1] & ft50_bit == 0 or aer[1] & a_star_bit == 0 or aer[1] & top5_bit == 0:
        raise SystemExit(f"American Economic Review mask is wrong: {aer[1]}")
    if aer[1] & utd_bit:
        raise SystemExit("American Economic Review must not carry UTD24")
    aer_field = journals["fields"][aer[5]]
    if aer_field != "3801 Applied economics":
        raise SystemExit(f"American Economic Review field is {aer_field!r}")
    if not journals["urls"][aer[6]]:
        raise SystemExit("American Economic Review is missing a board link")
    jap = by_name.get("Journal of Applied Psychology")
    if jap is None or jap[1] & utd_bit or jap[1] & top5_bit or not (jap[1] & ft50_bit):
        raise SystemExit("Journal of Applied Psychology tags are wrong on the journal page")
    joc = by_name.get("INFORMS Journal on Computing")
    if joc is None or not (joc[1] & utd_bit) or not (joc[1] & a_bit) or (joc[1] & ft50_bit):
        raise SystemExit("INFORMS Journal on Computing tags are wrong on the journal page")
    for uid in ("ft50", "top5", "utd24"):
        if jcounts["byUniverse"][uid]["journals"] != dcounts["byUniverse"][uid]["journals"]:
            raise SystemExit(
                f"{uid} journal count {jcounts['byUniverse'][uid]['journals']} != "
                f"directory {dcounts['byUniverse'][uid]['journals']}"
            )

    if icounts["appointments"] + icounts["unmatchedAppointments"] != dcounts["appointments"]:
        raise SystemExit("Institution appointments plus unmatched rows do not match the directory")
    if not 4_000 <= icounts["institutions"] <= 15_000:
        raise SystemExit(f"Unexpected institution count: {icounts['institutions']}")
    if icounts["withRor"] < icounts["institutions"] * 0.9:
        raise SystemExit(
            f"Only {icounts['withRor']} of {icounts['institutions']} institutions have a ROR id"
        )
    if icounts["editors"] > dcounts["editors"] or icounts["editors"] < dcounts["editors"] * 0.8:
        raise SystemExit(
            f"Institution editors {icounts['editors']} are far from directory {dcounts['editors']}"
        )
    directory_affs = {row[4] for row in directory["rows"] if row[4]}
    seen_names: set[str] = set()
    duplicate_names = 0
    for row in institutions["rows"]:
        name, country_i, continent_i, editors, appointments, journals, mask = row
        if name not in directory_affs:
            raise SystemExit(f"Institution {name!r} is not a directory affiliation")
        if name in seen_names:
            duplicate_names += 1
        seen_names.add(name)
        if appointments < 1 or editors < 1 or journals < 1 or mask < 1:
            raise SystemExit(f"Empty institution aggregate: {name!r}")
        country = institutions["countries"][country_i]
        continent = institutions["continents"][continent_i]
        for label, text in (("institution", name), ("country", country), ("continent", continent)):
            assert_no_contacts(text, label)
    if duplicate_names > 50:
        raise SystemExit(f"Too many institutions share a display name: {duplicate_names}")
    dartmouth = [row for row in institutions["rows"] if row[0] == "Dartmouth College"]
    if len(dartmouth) != 1:
        raise SystemExit(f"Expected one Dartmouth College row, found {len(dartmouth)}")
    dartmouth_row = dartmouth[0]
    if institutions["countries"][dartmouth_row[1]] != "United States":
        raise SystemExit("Dartmouth College country is not United States")
    if institutions["continents"][dartmouth_row[2]] != "North America":
        raise SystemExit("Dartmouth College continent is not North America")
    if dartmouth_row[4] < 1:
        raise SystemExit("Dartmouth College has no appointments")
    for uid in ("ft50", "top5", "utd24", "a_star", "a", "b", "c"):
        got = icounts["byUniverse"][uid]["appointments"]
        cap = dcounts["byUniverse"][uid]["appointments"]
        if got <= 0 or got > cap:
            raise SystemExit(f"Institution {uid} appointments {got} are outside 1..{cap}")
    print(
        "Aggregates: "
        f"{jcounts['journals']:,} journals ({jcounts['withField']:,} with a field, "
        f"{jcounts['withBoard']:,} with a board link), "
        f"{icounts['institutions']:,} institutions "
        f"({icounts['withRor']:,} with ROR, {duplicate_names:,} shared names), "
        f"{icounts['unmatchedAppointments']:,} appointments without an institution"
    )


def main() -> int:
    assert_static_site()
    membership = load_membership()
    catalogs = load_catalog_names()
    journal_catalog = load_journal_catalog()
    ft50_path = resolve_ft50_path()
    dates: list[str] = []
    years: set[str] = set()
    grouped: dict[tuple[str, str, str], list[Rec]] = defaultdict(list)
    sources: list[str] = []
    dropped = 0

    seen_membership_ids: set[str] = set()
    ft50_records, ft50_dropped = read_release(
        ft50_path, "ft50", catalogs, dates, years, membership, seen_membership_ids, journal_catalog
    )
    dropped += ft50_dropped
    sources.append(ft50_path.relative_to(ROOT).as_posix())
    print(f"FT50  {ft50_path.name}: {len(ft50_records):,} kept, {ft50_dropped:,} dropped")

    for origin, path in ABDC_FILES:
        if not path.exists():
            raise SystemExit(f"Missing ABDC release: {path.relative_to(ROOT)}")
        records, n_dropped = read_release(
            path, origin, catalogs, dates, years, membership, seen_membership_ids, journal_catalog
        )
        dropped += n_dropped
        sources.append(path.relative_to(ROOT).as_posix())
        print(f"ABDC {origin:6} {path.name}: {len(records):,} kept, {n_dropped:,} dropped")
        for rec in records:
            grouped[(rec.name_key, rec.journal_key, rec.role_key)].append(rec)

    ft50_kept = 0
    for rec in ft50_records:
        grouped[(rec.name_key, rec.journal_key, rec.role_key)].append(rec)
        ft50_kept += 1

    collapsed, collapse_stats = collapse(grouped)
    print(
        "Collapse: "
        f"{collapse_stats['cross_merged']:,} FT50 rows merged with ABDC, "
        f"{collapse_stats['ft50_only']:,} FT50-only, "
        f"{collapse_stats['split_keys']:,} keys kept split, "
        f"{collapse_stats['blank_aff_dropped']:,} blank-affiliation duplicates dropped, "
        f"{dropped:,} rows dropped before grouping"
    )

    missing_ids = membership.ids - seen_membership_ids
    if missing_ids:
        raise SystemExit(
            "Membership journals missing from the ABDC releases: " + ", ".join(sorted(missing_ids))
        )

    payload = build_payload(collapsed, sources, dates, years)
    assert_payload(payload, collapse_stats, ft50_kept)
    assert_subset_lists(payload, membership)

    SITE_DIR.mkdir(parents=True, exist_ok=True)
    text = js_payload(payload)
    DATA_JS.write_text(text, encoding="utf-8")
    counts = payload["counts"]
    family_counts: dict[str, int] = defaultdict(int)
    for row in payload["rows"]:
        family_counts[FAMILIES[payload["roleFamily"][row[1]]]] += 1
    print(
        "Wrote "
        f"{DATA_JS.relative_to(ROOT)} ({len(text) / 1_000_000:.1f} MB) — "
        f"{counts['appointments']:,} appointments, "
        f"{counts['editors']:,} editors, "
        f"{counts['journals']:,} journals, "
        f"{counts['countries']:,} countries"
    )
    print(
        "Universes: "
        + ", ".join(
            f"{UNIVERSE_META[i]['label']} {counts['byUniverse'][uid]['appointments']:,} "
            f"({counts['byUniverse'][uid]['journals']} journals)"
            for i, uid in enumerate(UNIVERSE_ORDER)
        )
    )
    print("Role groups: " + ", ".join(f"{name} {family_counts[name]:,}" for name in FAMILIES))
    print(f"Collected {payload['collectedMin']} – {payload['collectedMax']}; board year {payload['year']}")

    journal_payload = build_journal_payload(collapsed, journal_catalog, payload)
    institution_payload = build_institution_payload(collapsed, payload)
    assert_aggregates(payload, journal_payload, institution_payload)
    journal_text = dump_js(
        "JOURNALS_DATA",
        journal_payload,
        "Generated by scripts/build_site.py. One row per journal. Do not edit.",
    )
    institution_text = dump_js(
        "INSTITUTIONS_DATA",
        institution_payload,
        "Generated by scripts/build_site.py. One row per institution. Do not edit.",
    )
    JOURNALS_JS.write_text(journal_text, encoding="utf-8")
    INSTITUTIONS_JS.write_text(institution_text, encoding="utf-8")
    print(
        "Wrote "
        f"{JOURNALS_JS.relative_to(ROOT)} ({len(journal_text) / 1_000_000:.1f} MB) and "
        f"{INSTITUTIONS_JS.relative_to(ROOT)} ({len(institution_text) / 1_000_000:.1f} MB)"
    )
    build_rankings_page()
    return 0


def build_rankings_page() -> None:
    """Write site/rankings-data.js. Failure here fails the Pages build."""
    script = Path(__file__).resolve().parent / "build_rankings.py"
    completed = subprocess.run([sys.executable, str(script)], check=False)
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)


if __name__ == "__main__":
    sys.exit(main())
