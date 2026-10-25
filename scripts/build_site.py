#!/usr/bin/env python3
"""Build the public editor site from current releases.

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

AJG grades
-----------
AJG grades are extra tags on those same rows. They do not add a board file
and they do not scrape. The grade is the 2024 edition in
``journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/``, the latest
edition in that freeze. ``rating`` on ``abs_ajg_2024.csv`` is ``4*``, ``4``,
``3``, ``2``, or ``1``. A journal is tagged when its catalog id is a
``journal_id`` on that file or on a 2024 row of ``journal_id_crosswalk.csv``.
The crosswalk is required for journals whose primary id is a core49 slug
while the board file uses the ABDC id (The Economic Journal is ``ej``,
grade 4). The 2024 edition has 1,823 journals. 1,378 map to a catalog id.
1,356 of those are on a current board and receive a chip. The 445 unmatched
titles have no id and are not tagged. A small set of mapped titles are not
on the current boards. Many ABDC board journals have no AJG grade (about
2,400 board journal ids versus about 1,356 with a hit). Each tagged
journal gets one grade, labeled ``AJG 4*``, ``AJG 4``, ``AJG 3``, ``AJG 2``,
or ``AJG 1`` on both the list chip and the row badge. The label does not
include the edition year. Earlier editions, and titles that never receive
a chip, stay on the Rankings page.
ABDC chips stay A*, A, B, and C.

Universe bits: FT50 1, ABDC A* 2, ABDC A 4, ABDC B 8, ABDC C 16, Top 5 32,
UTD24 64, AJG 4* 128, AJG 4 256, AJG 3 512, AJG 2 1024, AJG 1 2048.

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

``faculty_profile_url`` is the person link on the directory. A non-empty
http(s) value is kept. A blank FT50 value is filled from the ABDC partner.
A non-empty FT50 value is not replaced. ``faculty_home_page`` is not
written to the site. A profile URL that contains an email address is
dropped, so a person slug like ``name@university`` is not published.

Emails and phone numbers are removed from displayed text. A row whose name
is only a phone number or an email address is dropped. ORCID, OpenAlex,
RePEc, coordinates, and photos are not written to the site. The directory
does not invent those ids as person links.

Project Pages
-------------
The published URL is https://kochiuyu.github.io/econ-journal-dispersion/
``site/`` uses relative asset URLs so that path and a local
``python -m http.server -d site`` serve the same files. Do not switch those
references to root-absolute paths (``/style.css``); on project Pages those
resolve at the user-site root instead of ``/econ-journal-dispersion/``.

``main`` also writes ``site/journals-data.js`` and ``site/institutions-data.js``
from those collapsed appointments, then runs ``scripts/build_rankings.py``,
which writes ``site/rankings-data.js`` from the ABS/AJG, CNRS, and
Handelsblatt/VWL freezes and the FT50, UTD24, Top 5, and ABDC catalogs.
Journals and institutions regroup the same boards and show the same list
chips, including a 2024 AJG grade when the journal has one. Rankings still
list every ABS/AJG edition, plus CNRS and Handelsblatt/VWL. The directory
AJG chips are that edition's grade on current boards, not a membership
flag, not the full guide, and not the earlier editions.

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

Hub, directory, and list chunks
-------------------------------
``site/index.html`` is a static hub. It does not load appointment rows.
``scripts/build_site.py`` writes ``site/meta.json`` (headline counts and
per-list appointment totals) for that page.

``site/directory.html`` is the searchable directory. It loads
``site/data/shell.js`` first (list metadata, journal names, and which chips
cover each journal). Appointment rows are ``site/data/<id>.js``, one file per
chip id: ``ft50``, ``a_star``, ``a``, ``b``, ``c``, ``top5``, ``utd24``,
``ajg_4star``, ``ajg_4``, ``ajg_3``, ``ajg_2``, ``ajg_1``. A row is copied into
every chip whose bit is set. The browser dedupes. Shared strings (roles,
journals, countries, board URLs, profile URLs) live inside each chunk so an
unloaded list does not ship its profile URLs.

The directory opens on FT50 (``data/ft50.js``) when the URL does not name a
list. Top 5 is not a second default download: every Top 5 row also has the
FT50 bit, so that chip is covered once FT50 is in memory. Top 5 alone would
be smaller, and it would hide the rest of the FT50 boards this directory is
built from. ``?u=`` loads those chips. ``u=-`` selects no list.
``?journal=`` with no ``u`` loads the smallest chip set that contains that
journal and does not force FT50. ``?aff=`` with no ``u`` loads
``site/data/institution-index.js`` (affiliation to a cover-chunk bitmask),
then the chips that contain that affiliation. Other filters search the chips
already loaded.

``index.html`` with a directory query string, or with ``#directory``,
redirects to ``directory.html``. ``site/data.js`` is not written.
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
DATA_DIR = SITE_DIR / "data"
META_JSON = SITE_DIR / "meta.json"
SHELL_JS = DATA_DIR / "shell.js"
INSTITUTION_INDEX_JS = DATA_DIR / "institution-index.js"
MONOLITH_JS = SITE_DIR / "data.js"
JOURNALS_JS = SITE_DIR / "journals-data.js"
INSTITUTIONS_JS = SITE_DIR / "institutions-data.js"
# FT50 is the directory's first chunk. Top 5 is a subset of those rows.
DEFAULT_UNIVERSES = ("ft50",)

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
AJG_FREEZE = ROOT / "journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024"
AJG_EDITION = 2024
AJG_YEAR = AJG_FREEZE / "abs_ajg_2024.csv"
AJG_CROSSWALK = AJG_FREEZE / "journal_id_crosswalk.csv"
# Locked to RELEASE_NOTES.md in rankings_abs_ajg_20261024.
AJG_EXPECTED_ROWS = 1823
AJG_EXPECTED_MAPPED = 1378
AJG_RATINGS = ("4*", "4", "3", "2", "1")
# Chip and badge text. The edition year stays in the title, not the label.
AJG_GRADE_META = (
    {"id": "ajg_4star", "label": "AJG 4*", "bit": 128, "rating": "4*"},
    {"id": "ajg_4", "label": "AJG 4", "bit": 256, "rating": "4"},
    {"id": "ajg_3", "label": "AJG 3", "bit": 512, "rating": "3"},
    {"id": "ajg_2", "label": "AJG 2", "bit": 1024, "rating": "2"},
    {"id": "ajg_1", "label": "AJG 1", "bit": 2048, "rating": "1"},
)
AJG_RATING_TO_ID = {item["rating"]: item["id"] for item in AJG_GRADE_META}
AJG_IDS = tuple(item["id"] for item in AJG_GRADE_META)

UNIVERSE_META = (
    {"id": "ft50", "label": "FT50", "bit": 1},
    {"id": "a_star", "label": "ABDC A*", "bit": 2},
    {"id": "a", "label": "ABDC A", "bit": 4},
    {"id": "b", "label": "ABDC B", "bit": 8},
    {"id": "c", "label": "ABDC C", "bit": 16},
    {"id": "top5", "label": "Top 5", "bit": 32},
    {"id": "utd24", "label": "UTD24", "bit": 64},
    *(
        {
            "id": item["id"],
            "label": item["label"],
            "bit": item["bit"],
            "title": f"CABS Academic Journal Guide 2024, grade {item['rating']}",
        }
        for item in AJG_GRADE_META
    ),
)
UNIVERSE_ORDER = tuple(item["id"] for item in UNIVERSE_META)
BITS = {item["id"]: item["bit"] for item in UNIVERSE_META}
AJG_MASK = 0
for _ajg_id in AJG_IDS:
    AJG_MASK |= BITS[_ajg_id]

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
    profile_url: str = ""
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


def profile_url(row: dict[str, str]) -> str:
    """Faculty profile link, or blank when the cell is empty or contains an email."""
    url = clean_url(row.get("faculty_profile_url") or "")
    if not url or EMAIL_RE.search(url) or "@" in url:
        return ""
    return url


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
    if not primary.profile_url and other.profile_url:
        primary.profile_url = other.profile_url
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
        winner, other = challenger, current
    else:
        winner, other = current, challenger
    winner.universes = set(current.universes)
    if not winner.profile_url and other.profile_url:
        winner.profile_url = other.profile_url
    return winner


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


def load_ajg_grades() -> dict[str, str]:
    """Catalog id to AJG 2024 rating, including non-primary crosswalk ids.

    The year file's primary id is sometimes a core49 slug. The board files
    use the ABDC id, which the crosswalk keeps with ``is_primary`` no.
    Every matched id gets the ``rating`` on that 2024 row (``4*``, ``4``,
    ``3``, ``2``, or ``1``). Earlier editions are not read.
    """
    rows = read_catalog_rows(AJG_YEAR)
    if len(rows) != AJG_EXPECTED_ROWS:
        raise SystemExit(f"AJG 2024 has {len(rows)} rows, expected {AJG_EXPECTED_ROWS}")
    primary: dict[str, str] = {}
    for row in rows:
        if (row.get("edition_year") or "").strip() != str(AJG_EDITION):
            raise SystemExit(f"AJG edition_year {row.get('edition_year')!r}")
        if (row.get("source_note") or "").strip() != "AJG2024":
            raise SystemExit(f"AJG source_note {row.get('source_note')!r}")
        rating = (row.get("rating") or "").strip()
        if rating not in AJG_RATINGS:
            raise SystemExit(f"AJG rating {rating!r} on {row.get('journal_title')}")
        journal_id = (row.get("journal_id") or "").strip()
        method = (row.get("match_method") or "").strip()
        if method == "unmatched":
            if journal_id or (row.get("catalog") or "").strip():
                raise SystemExit(f"Unmatched AJG row has an id: {row.get('journal_title')}")
            continue
        if method not in {"issn", "title"}:
            raise SystemExit(f"AJG match_method {method!r}")
        if not journal_id:
            raise SystemExit(f"Matched AJG row missing id: {row.get('journal_title')}")
        if journal_id in primary:
            raise SystemExit(f"Duplicate AJG 2024 journal_id {journal_id}")
        primary[journal_id] = rating
    if len(primary) != AJG_EXPECTED_MAPPED:
        raise SystemExit(f"AJG 2024 mapped {len(primary)}, expected {AJG_EXPECTED_MAPPED}")

    grades = dict(primary)
    xwalk_primary: set[str] = set()
    xwalk_rows = 0
    grouped: dict[tuple[str, str], set[str]] = defaultdict(set)
    grouped_primary: dict[tuple[str, str], str] = {}
    for row in read_catalog_rows(AJG_CROSSWALK):
        if (row.get("edition_year") or "").strip() != str(AJG_EDITION):
            continue
        xwalk_rows += 1
        journal_id = (row.get("journal_id") or "").strip()
        rating = (row.get("rating") or "").strip()
        if not journal_id:
            raise SystemExit(f"AJG 2024 crosswalk row missing id: {row.get('journal_title')}")
        if rating not in AJG_RATINGS:
            raise SystemExit(f"AJG crosswalk rating {rating!r} on {journal_id}")
        existing = grades.get(journal_id)
        if existing is not None and existing != rating:
            raise SystemExit(f"AJG 2024 id {journal_id} has ratings {existing} and {rating}")
        grades[journal_id] = rating
        key = (
            (row.get("journal_title") or "").strip(),
            (row.get("print_issn") or "").strip(),
        )
        grouped[key].add(rating)
        if (row.get("is_primary") or "").strip() == "yes":
            xwalk_primary.add(journal_id)
            grouped_primary[key] = journal_id
            if primary.get(journal_id) != rating:
                raise SystemExit(
                    f"AJG 2024 primary {journal_id} crosswalk rating {rating} != year file {primary.get(journal_id)}"
                )
    if not xwalk_rows:
        raise SystemExit("AJG crosswalk has no 2024 rows")
    if xwalk_primary != set(primary):
        missing = sorted(set(primary) - xwalk_primary)[:8]
        extra = sorted(xwalk_primary - set(primary))[:8]
        raise SystemExit(f"AJG 2024 crosswalk primary ids differ. Missing {missing}. Extra {extra}.")
    for key, ratings in grouped.items():
        if len(ratings) != 1:
            raise SystemExit(f"AJG 2024 title {key[0]!r} has ratings {sorted(ratings)}")
        primary_id = grouped_primary.get(key)
        if primary_id and primary.get(primary_id) not in ratings:
            raise SystemExit(f"AJG 2024 title {key[0]!r} disagrees with {primary_id}")
    # Board id, not the core49 slug stored as the freeze's primary id.
    if grades.get("ej") != "4" or "ej" in primary:
        raise SystemExit(f"The Economic Journal should be AJG 4 via crosswalk id ej, found {grades.get('ej')}")
    if grades.get("jeh") != "3" or "jeh" in primary:
        raise SystemExit(
            f"The Journal of Economic History should be AJG 3 via crosswalk id jeh, found {grades.get('jeh')}"
        )
    if "accounting_educators_journal" in grades:
        raise SystemExit("Accounting Educators Journal is not on AJG 2024")
    for journal_id in sorted(TOP5_IDS):
        if grades.get(journal_id) != "4*":
            raise SystemExit(f"{journal_id} AJG grade is {grades.get(journal_id)!r}, expected 4*")
    if grades.get("informs_journal_computing") != "3":
        raise SystemExit(
            f"INFORMS Journal on Computing AJG grade is {grades.get('informs_journal_computing')!r}, expected 3"
        )
    if grades.get("jap") != "4*":
        raise SystemExit(f"Journal of Applied Psychology AJG grade is {grades.get('jap')!r}, expected 4*")
    ft50_ids = {
        (row.get("journal_id") or "").strip()
        for row in read_catalog_rows(FT50_CATALOG)
        if (row.get("journal_id") or "").strip()
    }
    missing_ft50 = sorted(journal_id for journal_id in ft50_ids if journal_id not in grades)
    if len(ft50_ids) != 50 or missing_ft50:
        raise SystemExit(f"FT50 ids missing an AJG 2024 grade: {missing_ft50 or sorted(ft50_ids)}")
    return grades


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
    ajg_grades: dict[str, str],
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
    if journal_id:
        rating = ajg_grades.get(journal_id)
        if rating:
            universes.add(AJG_RATING_TO_ID[rating])
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
        profile_url=profile_url(row),
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
    ajg_grades: dict[str, str],
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
            rec = row_to_rec(row, origin, catalogs, membership, catalog, ajg_grades)
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
    index = (SITE_DIR / "index.html").read_text(encoding="utf-8")
    directory = (SITE_DIR / "directory.html").read_text(encoding="utf-8")
    app = (SITE_DIR / "app.js").read_text(encoding="utf-8")
    hub = (SITE_DIR / "hub.js").read_text(encoding="utf-8")
    if PAGES_BASE not in index or LIVE_URL not in index:
        raise SystemExit("site/index.html is missing the project Pages URL")
    if PAGES_BASE not in directory or LIVE_URL not in directory:
        raise SystemExit("site/directory.html is missing the project Pages URL")
    if PAGES_BASE not in app:
        raise SystemExit("site/app.js is missing the project Pages base path")
    if PAGES_BASE not in hub or "meta.json" not in hub:
        raise SystemExit("site/hub.js must load meta.json with the project Pages base")
    if 'href="rankings.html"' not in index or 'href="directory.html"' not in index:
        raise SystemExit("site/index.html is missing Directory or Rankings nav")
    if 'id="rows"' in index or 'src="data.js"' in index or "data/ft50.js" in index:
        raise SystemExit("site/index.html still embeds the directory or appointment rows")
    if "directory.html" not in index or "#directory" not in index:
        raise SystemExit("site/index.html does not redirect old directory URLs")
    if 'id="institution"' not in directory or 'id="field"' not in directory:
        raise SystemExit("site/directory.html is missing the institution or field filter")
    if "AJG 4*" not in directory or "AJG 1" not in directory:
        raise SystemExit("site/directory.html does not name the AJG grades")
    if "faculty profile" not in directory.casefold():
        raise SystemExit("site/directory.html does not say a name opens a faculty profile")
    if "EDITOR_SHELL" not in app or "profiles.values[row[8]]" not in app:
        raise SystemExit("site/app.js does not read the directory shell or faculty profile URLs")
    if 'src="data.js"' in directory or 'src="data/shell.js"' not in directory:
        raise SystemExit("site/directory.html must load data/shell.js and not data.js")
    if "AJG 2024" in index or "AJG 2024" in directory:
        raise SystemExit("Hub or directory still labels AJG with the edition year")
    rankings_js = (SITE_DIR / "rankings.js").read_text(encoding="utf-8")
    if PAGES_BASE not in rankings_js:
        raise SystemExit("site/rankings.js is missing the project Pages base path")
    page_files = ("index.html", "directory.html", "journals.html", "institutions.html", "rankings.html")
    for name in page_files:
        text = (SITE_DIR / name).read_text(encoding="utf-8")
        if PAGES_BASE not in text or LIVE_URL not in text:
            raise SystemExit(f"site/{name} is missing the project Pages URL")
        for link in ("directory.html", "journals.html", "institutions.html", "rankings.html"):
            if f'href="{link}"' not in text:
                raise SystemExit(f"site/{name} is missing the {link} nav link")
        if 'href="./#directory"' in text:
            raise SystemExit(f"site/{name} still points Directory at the hub")
        if name != "rankings.html" and "AJG 2024" in text:
            raise SystemExit(f"site/{name} still labels AJG with the edition year")
    for script in ("journals.js", "institutions.js", "hub.js"):
        text = (SITE_DIR / script).read_text(encoding="utf-8")
        if PAGES_BASE not in text:
            raise SystemExit(f"site/{script} is missing the project Pages base path")
        if "index.html?" in text:
            raise SystemExit(f"site/{script} still opens the directory on index.html")
    for name in (
        "index.html",
        "directory.html",
        "hub.js",
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


def build_payload(
    records: list[Rec],
    sources: list[str],
    dates: list[str],
    years: set[str],
    catalog: JournalCatalog,
) -> dict:
    roles = StringIndex()
    role_family_idx: list[int] = []
    journals = StringIndex()
    countries = StringIndex("")
    continents = StringIndex("")
    urls = StringIndex("")
    profiles = StringIndex("")
    field_counts: dict[int, Counter[str]] = defaultdict(Counter)

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
        field_for = (catalog_meta(rec, catalog).get("field") or "")
        if field_for:
            field_counts[journal_i][field_for] += 1
            assert_no_contacts(field_for, "field")
        country_i = countries.add(rec.country)
        continent_i = continents.add(rec.continent)
        url_i = urls.add(rec.url)
        profile_i = profiles.add(rec.profile_url)
        mask = rec.mask()
        # name, role, journal, mask, affiliation, country, continent, board url, faculty profile
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
                profile_i,
            ]
        )
        editor_keys.add(rec.name_key)
        if rec.country:
            country_keys.add(norm_space(rec.country))
        for universe, bit in BITS.items():
            if mask & bit:
                appointments_by_universe[universe] += 1
                journal_by_universe[universe].add(journal_i)

    fields = StringIndex("")
    journal_field = [
        fields.add(mode_text(field_counts[index])) for index in range(len(journals.values))
    ]
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
        "fields": fields.values,
        "journalField": journal_field,
        "countries": countries.values,
        "continents": continents.values,
        "urls": urls.values,
        "profiles": profiles.values,
        "rows": rows,
        "counts": {
            "appointments": len(rows),
            "editors": len(editor_keys),
            "journals": len(journals.values),
            "countries": len(country_keys),
            "byUniverse": by_universe,
        },
    }


def js_object(payload: object) -> str:
    raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return (
        raw.replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def dump_js(global_name: str, payload: dict, comment: str) -> str:
    if "*/" in comment:
        raise SystemExit("Generated JS comment contains */ and would close early")
    return "/* " + comment + " */\nwindow." + global_name + " = " + js_object(payload) + ";\n"


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
        raise SystemExit("directory payload base path is not the project Pages path")
    labels = {item["id"]: item["label"] for item in payload["universes"]}
    expected_labels = {
        "ft50": "FT50",
        "a_star": "ABDC A*",
        "a": "ABDC A",
        "b": "ABDC B",
        "c": "ABDC C",
        "top5": "Top 5",
        "utd24": "UTD24",
        "ajg_4star": "AJG 4*",
        "ajg_4": "AJG 4",
        "ajg_3": "AJG 3",
        "ajg_2": "AJG 2",
        "ajg_1": "AJG 1",
    }
    if labels != expected_labels:
        raise SystemExit(f"List labels {labels} != {expected_labels}")
    for item in payload["universes"]:
        if re.search(r"20\d{2}", item["label"]):
            raise SystemExit(f"List label includes a year: {item['label']}")
    for row in payload["rows"]:
        ajg_bits = row[3] & AJG_MASK
        if ajg_bits & (ajg_bits - 1):
            raise SystemExit(f"Appointment has two AJG grades: {row[0]} mask {row[3]}")
    # Every FT50 badge row must also carry an ABDC badge.
    ft50_bit = BITS["ft50"]
    abdc_bits = BITS["a_star"] | BITS["a"] | BITS["b"] | BITS["c"]
    for row in payload["rows"]:
        mask = row[3]
        if mask & ft50_bit and not (mask & abdc_bits):
            raise SystemExit(f"FT50 row missing an ABDC badge: {row[0]}")
    assert_profiles(payload)


def assert_profiles(payload: dict) -> None:
    """Person links are faculty_profile_url only, and they carry no email address."""
    profiles = payload.get("profiles") or []
    if not profiles or profiles[0] != "":
        raise SystemExit("profiles string table must start with an empty URL")
    linked = 0
    luttmer = False
    for row in payload["rows"]:
        if len(row) != 9:
            raise SystemExit(f"Directory row width {len(row)}, expected 9")
        url = profiles[row[8]]
        if not url:
            continue
        linked += 1
        if not (url.startswith("http://") or url.startswith("https://")):
            raise SystemExit(f"Profile URL is not http(s): {url[:180]}")
        if "@" in url or CONTACT_ASSERT_RE.search(url):
            raise SystemExit(f"Profile URL contains contact text: {url[:180]}")
        if row[0] == "Erzo F.P. Luttmer" and "dartmouth.edu/people/erzo-fp-luttmer" in url:
            luttmer = True
    if linked < 10_000:
        raise SystemExit(f"Too few faculty profile links: {linked}")
    if not luttmer:
        raise SystemExit("Expected Erzo F.P. Luttmer to link to the Dartmouth faculty profile")
    helena = [
        profiles[row[8]]
        for row in payload["rows"]
        if row[0] == "Helena Skyt Nielsen" and profiles[row[8]]
    ]
    if helena:
        raise SystemExit(f"Helena Skyt Nielsen profile contains an email and must not be published: {helena[:2]}")
    print(f"Faculty profile links: {linked:,}")


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
    def ajg_on(mask: int) -> list[str]:
        return [uid for uid in AJG_IDS if mask & BITS[uid]]

    aer_ajg = ajg_on(aer[1])
    if aer_ajg != ["ajg_4star"]:
        raise SystemExit(f"American Economic Review AJG grade {aer_ajg}, expected AJG 4*")
    aer_field = journals["fields"][aer[5]]
    if aer_field != "3801 Applied economics":
        raise SystemExit(f"American Economic Review field is {aer_field!r}")
    if not journals["urls"][aer[6]]:
        raise SystemExit("American Economic Review is missing a board link")
    jap = by_name.get("Journal of Applied Psychology")
    if jap is None or jap[1] & utd_bit or jap[1] & top5_bit or not (jap[1] & ft50_bit):
        raise SystemExit("Journal of Applied Psychology tags are wrong on the journal page")
    if ajg_on(jap[1]) != ["ajg_4star"]:
        raise SystemExit("Journal of Applied Psychology should carry AJG 4*")
    joc = by_name.get("INFORMS Journal on Computing")
    if joc is None or not (joc[1] & utd_bit) or not (joc[1] & a_bit) or (joc[1] & ft50_bit):
        raise SystemExit("INFORMS Journal on Computing tags are wrong on the journal page")
    if ajg_on(joc[1]) != ["ajg_3"]:
        raise SystemExit("INFORMS Journal on Computing should carry AJG 3")
    ej = by_name.get("The Economic Journal")
    if ej is None or ajg_on(ej[1]) != ["ajg_4"]:
        raise SystemExit("The Economic Journal should carry AJG 4 via crosswalk id ej")
    jeh = by_name.get("The Journal of Economic History")
    if jeh is None or ajg_on(jeh[1]) != ["ajg_3"]:
        raise SystemExit("The Journal of Economic History should carry AJG 3 via crosswalk id jeh")
    educators = by_name.get("Accounting Educators Journal")
    if educators is None or ajg_on(educators[1]):
        raise SystemExit("Accounting Educators Journal must not carry an AJG grade")
    ft50_bad_ajg = [
        f"{row[0]} {ajg_on(row[1])}"
        for row in journals["rows"]
        if (row[1] & ft50_bit) and len(ajg_on(row[1])) != 1
    ]
    if ft50_bad_ajg:
        raise SystemExit(f"FT50 journals should have one AJG grade: {ft50_bad_ajg}")
    multi_ajg = [
        row[0] for row in journals["rows"] if len(ajg_on(row[1])) > 1
    ]
    if multi_ajg:
        raise SystemExit(f"Journals with more than one AJG grade: {multi_ajg[:8]}")
    # 4*, 4, and 3 are every matched journal in abs_ajg_2024.csv.
    # 2 and 1 drop the matched titles that are not on a current board.
    expected_ajg_journals = {
        "ajg_4star": 47,
        "ajg_4": 89,
        "ajg_3": 287,
        "ajg_2": 459,
        "ajg_1": 474,
    }
    ajg_journals = 0
    for uid, expected in expected_ajg_journals.items():
        got = jcounts["byUniverse"][uid]["journals"]
        ajg_journals += got
        if got != expected:
            raise SystemExit(f"{uid} journals {got}, expected {expected}")
    if ajg_journals != 1_356:
        raise SystemExit(f"Unexpected AJG journal count: {ajg_journals}")
    if len(directory.get("journalField") or []) != len(directory["journals"]):
        raise SystemExit("directory journalField does not line up with journals")
    directory_field = {
        name: directory["fields"][directory["journalField"][index]]
        for index, name in enumerate(directory["journals"])
    }
    for row in journals["rows"]:
        expect = journals["fields"][row[5]]
        got = directory_field.get(row[0])
        if got != expect:
            raise SystemExit(f"{row[0]} field {got!r} != journal page {expect!r}")
    for uid in ("ft50", "top5", "utd24", *AJG_IDS):
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
    for uid in ("ft50", "top5", "utd24", *AJG_IDS, "a_star", "a", "b", "c"):
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


def universe_preference(payload: dict) -> tuple[str, ...]:
    """Smaller lists first so a journal deep link fetches the smallest chip that holds it."""
    return tuple(
        sorted(
            UNIVERSE_ORDER,
            key=lambda uid: (
                payload["counts"]["byUniverse"][uid]["appointments"],
                UNIVERSE_ORDER.index(uid),
            ),
        )
    )


def cover_mask(masks: set[int], preference: tuple[str, ...]) -> int:
    """Bitmask of chips whose union contains every row mask. Ties prefer the smaller chip."""
    remaining = set(masks)
    chosen = 0
    while remaining:
        best_id = ""
        best_score = 0
        for uid in preference:
            bit = BITS[uid]
            score = sum(1 for mask in remaining if mask & bit)
            if score > best_score:
                best_score = score
                best_id = uid
        if not best_id:
            break
        chosen |= BITS[best_id]
        bit = BITS[best_id]
        remaining = {mask for mask in remaining if not (mask & bit)}
    return chosen


def build_covers(payload: dict) -> dict[str, list[str]]:
    """Chip ids that each contain every appointment of a list. FT50 covers Top 5."""
    holders: dict[str, set[int]] = {uid: set() for uid in UNIVERSE_ORDER}
    for row in payload["rows"]:
        mask = row[3]
        for uid, bit in BITS.items():
            if mask & bit:
                holders[uid].add(mask)
    covers: dict[str, list[str]] = {}
    for uid in UNIVERSE_ORDER:
        masks = holders[uid]
        ok: list[str] = []
        for other in UNIVERSE_ORDER:
            obit = BITS[other]
            if masks and all(mask & obit for mask in masks):
                ok.append(other)
        if uid not in ok:
            ok.append(uid)
        covers[uid] = ok
    return covers


def chunk_for_universe(payload: dict, universe_id: str) -> dict:
    """Rows with this list bit, and only the strings those rows use."""
    bit = BITS[universe_id]
    roles = StringIndex()
    role_family: list[int] = []
    journals = StringIndex()
    journal_fields: list[str] = []
    countries = StringIndex("")
    continents = StringIndex("")
    urls = StringIndex("")
    profiles = StringIndex("")
    fields = StringIndex("")

    def add_role(role: str, family: int) -> int:
        index = roles.add(role)
        if len(role_family) == index:
            role_family.append(family)
        return index

    def add_journal(name: str, field_text: str) -> int:
        index = journals.add(name)
        if len(journal_fields) == index:
            journal_fields.append(field_text)
        return index

    rows: list[list] = []
    for row in payload["rows"]:
        if not (row[3] & bit):
            continue
        field_text = payload["fields"][payload["journalField"][row[2]]]
        rows.append(
            [
                row[0],
                add_role(payload["roles"][row[1]], payload["roleFamily"][row[1]]),
                add_journal(payload["journals"][row[2]], field_text),
                row[3],
                row[4],
                countries.add(payload["countries"][row[5]]),
                continents.add(payload["continents"][row[6]]),
                urls.add(payload["urls"][row[7]]),
                profiles.add(payload["profiles"][row[8]]),
            ]
        )
    return {
        "id": universe_id,
        "roles": roles.values,
        "roleFamily": role_family,
        "journals": journals.values,
        "fields": fields.values,
        "journalField": [fields.add(text) for text in journal_fields],
        "countries": countries.values,
        "continents": continents.values,
        "urls": urls.values,
        "profiles": profiles.values,
        "rows": rows,
    }


def build_journal_routes(
    payload: dict, preference: tuple[str, ...]
) -> tuple[list[str], list[int], list[int]]:
    """Parallel arrays: journal name, full list mask, and the chips to fetch for that journal."""
    masks: dict[str, set[int]] = defaultdict(set)
    for row in payload["rows"]:
        name = payload["journals"][row[2]]
        if name:
            masks[name].add(row[3])
    names: list[str] = []
    full_masks: list[int] = []
    covers: list[int] = []
    for name, row_masks in masks.items():
        full = 0
        for mask in row_masks:
            full |= mask
        cover = cover_mask(row_masks, preference)
        if not cover:
            raise SystemExit(f"No chip covers journal {name}")
        names.append(name)
        full_masks.append(full)
        covers.append(cover)
    return names, full_masks, covers


def build_institution_index(payload: dict, preference: tuple[str, ...]) -> dict[str, int]:
    """Exact affiliation string to the bitmask of chips that contain it."""
    masks: dict[str, set[int]] = defaultdict(set)
    for row in payload["rows"]:
        affiliation = row[4]
        if affiliation:
            masks[affiliation].add(row[3])
    return {name: cover_mask(row_masks, preference) for name, row_masks in masks.items()}


def build_shell(
    payload: dict,
    covers: dict[str, list[str]],
    journal_names: list[str],
    journal_masks: list[int],
    journal_covers: list[int],
) -> dict:
    universes = []
    for item in UNIVERSE_META:
        uid = item["id"]
        info = dict(item)
        info["file"] = f"data/{uid}.js"
        info["appointments"] = payload["counts"]["byUniverse"][uid]["appointments"]
        info["journals"] = payload["counts"]["byUniverse"][uid]["journals"]
        universes.append(info)
    return {
        "base": PAGES_BASE,
        "liveUrl": LIVE_URL + "directory.html",
        "repo": REPO_URL,
        "readme": REPO_URL + "#readme",
        "year": payload["year"],
        "collectedMin": payload["collectedMin"],
        "collectedMax": payload["collectedMax"],
        "universes": universes,
        "families": list(FAMILIES),
        "counts": payload["counts"],
        "defaultUniverses": list(DEFAULT_UNIVERSES),
        "noUniverse": "-",
        "covers": covers,
        "journals": journal_names,
        "journalMask": journal_masks,
        "journalCover": journal_covers,
    }


def build_meta(shell: dict) -> dict:
    return {
        "base": PAGES_BASE,
        "liveUrl": LIVE_URL,
        "year": shell["year"],
        "collectedMin": shell["collectedMin"],
        "collectedMax": shell["collectedMax"],
        "counts": {
            "appointments": shell["counts"]["appointments"],
            "editors": shell["counts"]["editors"],
            "journals": shell["counts"]["journals"],
            "countries": shell["counts"]["countries"],
        },
        "universes": [
            {
                "id": item["id"],
                "label": item["label"],
                "bit": item["bit"],
                "title": item.get("title", ""),
                "appointments": item["appointments"],
                "journals": item["journals"],
                "href": "directory.html?u=" + item["id"],
            }
            for item in shell["universes"]
        ],
        "defaultUniverses": list(DEFAULT_UNIVERSES),
        "directory": "directory.html",
    }


def dump_chunk(universe_id: str, payload: dict) -> str:
    if not re.fullmatch(r"[a-z0-9_]+", universe_id):
        raise SystemExit(f"Unsafe chunk id {universe_id}")
    comment = (
        "Generated by scripts/build_site.py. Appointments with the "
        + universe_id
        + " list bit. Do not edit."
    )
    if "*/" in comment:
        raise SystemExit("Generated JS comment contains */ and would close early")
    return (
        "/* " + comment + " */\n"
        "window.EDITOR_CHUNKS = window.EDITOR_CHUNKS || {};\n"
        "window.EDITOR_CHUNKS[" + json.dumps(universe_id) + "] = " + js_object(payload) + ";\n"
    )


def decode_directory_row(row: list, tables: dict) -> tuple:
    return (
        row[0],
        tables["roles"][row[1]],
        tables["journals"][row[2]],
        row[3],
        row[4],
        tables["countries"][row[5]],
        tables["continents"][row[6]],
        tables["urls"][row[7]],
        tables["profiles"][row[8]],
    )


def assert_directory_chunks(
    payload: dict,
    chunks: dict[str, dict],
    covers: dict[str, list[str]],
    journal_names: list[str],
    journal_masks: list[int],
    journal_covers: list[int],
    institution_index: dict[str, int],
    shell: dict,
    meta: dict,
) -> None:
    if shell["base"] != PAGES_BASE or meta["base"] != PAGES_BASE:
        raise SystemExit("shell or meta base path is not the project Pages path")
    if shell["defaultUniverses"] != ["ft50"] or meta["defaultUniverses"] != ["ft50"]:
        raise SystemExit("directory default list must be FT50")
    if "ft50" not in covers.get("top5", []):
        raise SystemExit("FT50 chunk should cover every Top 5 appointment")
    if "ft50" in covers.get("utd24", []):
        raise SystemExit("FT50 must not be treated as covering UTD24; INFORMS Journal on Computing is ABDC A")
    original_counts: Counter[tuple] = Counter(
        decode_directory_row(row, payload) for row in payload["rows"]
    )
    for uid in UNIVERSE_ORDER:
        chunk = chunks[uid]
        bit = BITS[uid]
        if not chunk["rows"]:
            raise SystemExit(f"Chunk {uid} has no rows")
        for key in ("profiles", "countries", "continents", "urls"):
            if not chunk[key] or chunk[key][0] != "":
                raise SystemExit(f"Chunk {uid} {key} table must start with an empty string")
        if len(chunk["roleFamily"]) != len(chunk["roles"]):
            raise SystemExit(f"Chunk {uid} role family table has the wrong length")
        if len(chunk["journalField"]) != len(chunk["journals"]):
            raise SystemExit(f"Chunk {uid} journal field table has the wrong length")
        for url in chunk["profiles"]:
            if url and ("@" in url or CONTACT_ASSERT_RE.search(url)):
                raise SystemExit(f"Profile URL in {uid} contains contact text: {url[:180]}")
        local: Counter[tuple] = Counter()
        for row in chunk["rows"]:
            if len(row) != 9 or not (row[3] & bit):
                raise SystemExit(f"Chunk {uid} row is missing the {uid} bit")
            local[decode_directory_row(row, chunk)] += 1
        for decoded, count in original_counts.items():
            if decoded[3] & bit and local[decoded] != count:
                raise SystemExit(f"Chunk {uid} dropped or duplicated an appointment")
        for decoded in local:
            if decoded not in original_counts:
                raise SystemExit(f"Chunk {uid} has an appointment that is not in the directory")
    journal_rows: dict[str, set[int]] = defaultdict(set)
    for row in payload["rows"]:
        name = payload["journals"][row[2]]
        if name:
            journal_rows[name].add(row[3])
    if journal_names != list(journal_rows):
        raise SystemExit("Shell journal list does not match the directory journals")
    for name, full_mask, cover in zip(journal_names, journal_masks, journal_covers):
        union = 0
        for mask in journal_rows[name]:
            union |= mask
            if not (mask & cover):
                raise SystemExit(f"Journal cover for {name} misses a row")
        if full_mask != union or not cover:
            raise SystemExit(f"Journal mask for {name} is wrong")
    aff_rows: dict[str, set[int]] = defaultdict(set)
    for row in payload["rows"]:
        if row[4]:
            aff_rows[row[4]].add(row[3])
    if set(institution_index) != set(aff_rows):
        raise SystemExit("Institution index does not match directory affiliations")
    for name, cover in institution_index.items():
        for mask in aff_rows[name]:
            if not (mask & cover):
                raise SystemExit(f"Institution cover for {name} misses a row")
    if "Dartmouth College" not in institution_index:
        raise SystemExit("Institution index is missing Dartmouth College")
    if meta["counts"]["appointments"] != payload["counts"]["appointments"]:
        raise SystemExit("meta.json appointment count does not match the directory")
    for item in meta["universes"]:
        if item["href"] != "directory.html?u=" + item["id"]:
            raise SystemExit(f"Hub link for {item['id']} is not a relative directory URL")
        if item["appointments"] != payload["counts"]["byUniverse"][item["id"]]["appointments"]:
            raise SystemExit(f"meta.json count for {item['id']} does not match the directory")


def write_directory_assets(payload: dict) -> None:
    preference = universe_preference(payload)
    covers = build_covers(payload)
    journal_names, journal_masks, journal_covers = build_journal_routes(payload, preference)
    institution_index = build_institution_index(payload, preference)
    chunks = {uid: chunk_for_universe(payload, uid) for uid in UNIVERSE_ORDER}
    shell = build_shell(payload, covers, journal_names, journal_masks, journal_covers)
    meta = build_meta(shell)
    assert_directory_chunks(
        payload,
        chunks,
        covers,
        journal_names,
        journal_masks,
        journal_covers,
        institution_index,
        shell,
        meta,
    )

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for path in DATA_DIR.glob("*.js"):
        path.unlink()
    if MONOLITH_JS.exists():
        MONOLITH_JS.unlink()

    shell_text = dump_js(
        "EDITOR_SHELL",
        shell,
        "Generated by scripts/build_site.py. Directory shell: counts, journals, and chunk map. Do not edit.",
    )
    SHELL_JS.write_text(shell_text, encoding="utf-8")
    index_text = (
        "/* Generated by scripts/build_site.py. Affiliation to cover-chunk bitmask. Do not edit. */\n"
        "window.EDITOR_INSTITUTION_INDEX = " + js_object(institution_index) + ";\n"
    )
    INSTITUTION_INDEX_JS.write_text(index_text, encoding="utf-8")
    META_JSON.write_text(js_object(meta) + "\n", encoding="utf-8")

    written: list[tuple[str, int, int]] = []
    for uid in UNIVERSE_ORDER:
        text = dump_chunk(uid, chunks[uid])
        path = DATA_DIR / f"{uid}.js"
        path.write_text(text, encoding="utf-8")
        written.append((uid, len(text), len(chunks[uid]["rows"])))
    if MONOLITH_JS.exists():
        raise SystemExit("site/data.js was written; the directory must load list chunks instead")

    meta_bytes = META_JSON.stat().st_size
    shell_bytes = SHELL_JS.stat().st_size
    index_bytes = INSTITUTION_INDEX_JS.stat().st_size
    ft50_bytes = (DATA_DIR / "ft50.js").stat().st_size
    if meta_bytes > 64_000:
        raise SystemExit(f"meta.json is {meta_bytes:,} bytes; the hub summary should stay tiny")
    if shell_bytes > 2_000_000:
        raise SystemExit(f"shell.js is {shell_bytes:,} bytes")
    if index_bytes > 4_000_000:
        raise SystemExit(f"institution-index.js is {index_bytes:,} bytes")
    if ft50_bytes > 4_000_000:
        raise SystemExit(
            f"FT50 chunk is {ft50_bytes:,} bytes. The default directory download is too large."
        )
    for name in ("shell.js", "institution-index.js", *(f"{uid}.js" for uid in UNIVERSE_ORDER)):
        text = (DATA_DIR / name).read_text(encoding="utf-8")
        if 'src="/' in text or 'href="/' in text:
            raise SystemExit(f"site/data/{name} contains a root-absolute URL")
    print(
        "Wrote "
        f"{META_JSON.relative_to(ROOT)} ({meta_bytes / 1000:.1f} KB), "
        f"{SHELL_JS.relative_to(ROOT)} ({shell_bytes / 1000:.1f} KB), "
        f"{INSTITUTION_INDEX_JS.relative_to(ROOT)} ({index_bytes / 1_000_000:.1f} MB)"
    )
    print(
        "Chunks: "
        + ", ".join(f"{uid} {size / 1_000_000:.2f} MB ({rows:,} rows)" for uid, size, rows in written)
    )
    print(
        "Default directory chunk is FT50 "
        f"({ft50_bytes / 1_000_000:.2f} MB). Top 5 rows are included in that file."
    )


def main() -> int:
    assert_static_site()
    membership = load_membership()
    ajg_grades = load_ajg_grades()
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
        ft50_path,
        "ft50",
        catalogs,
        dates,
        years,
        membership,
        seen_membership_ids,
        journal_catalog,
        ajg_grades,
    )
    dropped += ft50_dropped
    sources.append(ft50_path.relative_to(ROOT).as_posix())
    print(f"FT50  {ft50_path.name}: {len(ft50_records):,} kept, {ft50_dropped:,} dropped")

    for origin, path in ABDC_FILES:
        if not path.exists():
            raise SystemExit(f"Missing ABDC release: {path.relative_to(ROOT)}")
        records, n_dropped = read_release(
            path,
            origin,
            catalogs,
            dates,
            years,
            membership,
            seen_membership_ids,
            journal_catalog,
            ajg_grades,
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

    payload = build_payload(collapsed, sources, dates, years, journal_catalog)
    assert_payload(payload, collapse_stats, ft50_kept)
    assert_subset_lists(payload, membership)

    SITE_DIR.mkdir(parents=True, exist_ok=True)
    counts = payload["counts"]
    family_counts: dict[str, int] = defaultdict(int)
    for row in payload["rows"]:
        family_counts[FAMILIES[payload["roleFamily"][row[1]]]] += 1
    print(
        "Directory: "
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
    write_directory_assets(payload)

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
