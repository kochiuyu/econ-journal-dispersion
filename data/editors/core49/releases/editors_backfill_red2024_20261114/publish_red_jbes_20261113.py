#!/usr/bin/env python3
"""Publish editors_backfill_red_jbes_20261113 as a new core49 release folder in /workspace/edj-web (PDFs excluded)."""
import json, shutil, hashlib, csv, re
from pathlib import Path
P = Path("/workspace/econ-journal-editors/releases/editors_backfill_red_jbes_20261113")
WEB = Path("/workspace/edj-web/data/editors/core49/releases")
BASE = WEB / "editors_backfill_red_gap_20261112"
OUT = WEB / "editors_backfill_red_jbes_20261113"
OUT.mkdir(parents=True, exist_ok=True)
md5 = lambda p: hashlib.md5(p.read_bytes()).hexdigest()
SCRUBBED = "editors_backfill_scale_spotcheck.csv"
RENAME = {"RELEASE_NOTES.md": "COLLECTOR_RELEASE_NOTES.md"}
stats = {"copied": [], "from_web_base": [], "excluded_pdfs": [], "identical_to_base": [], "changed_vs_base": [], "new_vs_base": []}
assert (P / SCRUBBED).read_bytes() == (BASE / SCRUBBED).read_bytes(), "spotcheck not byte-identical to scrubbed web copy"
stats["spotcheck_byte_identical_to_scrubbed_web_copy"] = True
stats["spotcheck_md5"] = md5(BASE / SCRUBBED)
for p in sorted(P.iterdir()):
    if p.suffix.lower() == ".pdf": stats["excluded_pdfs"].append(p.name); continue
    if p.name in ("README.md", "_build.json"): continue
    if p.name == SCRUBBED:
        shutil.copy2(BASE / SCRUBBED, OUT / SCRUBBED); stats["from_web_base"].append(p.name); continue
    dst = RENAME.get(p.name, p.name)
    shutil.copy2(p, OUT / dst); stats["copied"].append(dst)
    bp = BASE / p.name
    (stats["identical_to_base"] if bp.exists() and bp.read_bytes() == p.read_bytes()
     else stats["changed_vs_base"] if bp.exists() else stats["new_vs_base"]).append(dst)
note = """# editors_backfill_red_jbes_20261113 — pinned in this repo (2026-11-13)

**Publish note (2026-11-13, Asia/Taipei).** Published pending PR merge. It supersedes `editors_backfill_red_gap_20261112` (PR #70) as the current core49 backfill. The older folders (`editors_backfill_red_gap_20261112`, `editors_ra_ta_merge_rebuild_20261112`, `editors_backfill_scale_ror_20261031`) stay in the tree. The Directory site does not read core49 (it shows current boards only), so Directory counts are unaffected and `build_site.py` is unchanged. The collector's README follows below the line; its "HELD, unpublished" status is historical. The collector's release notes are in `COLLECTOR_RELEASE_NOTES.md`.

- Panel `editors_backfill_scale_ror_panel.csv`: 15,873 rows (was 15,664; +209 appended, base rows byte-identical). Long table `editor_affiliations.csv`: 12,102 rows (was 11,896; +206 appended).
- Review of Economic Dynamics 2025: 44 rows, `#15664`–`#15707`, from the RED Vol 55 (2025-01) issue front matter (re-used verbatim from the collector's intermediate freeze `editors_backfill_red_2025_20261113`). Inventory `ok_issue_front_matter` 44/44; 44 long rows.
- Journal of Business and Economic Statistics 2019: 87 rows, `#15708`–`#15794`, from Vol 37 No. 1 (January 2019) front matter, https://www.jstor.org/stable/45181150. Inventory `ok_issue_front_matter` 87/84; 87 long rows (3 two-place rows split; 3 panel-only rows with no printed affiliation).
- Journal of Business and Economic Statistics 2020: 78 rows, `#15795`–`#15872`, from Vol 38 No. 1 (January 2020) front matter, https://www.jstor.org/stable/45282197. Inventory `ok_issue_front_matter` 78/75; 75 long rows.
- Match rates: JBES 0.9302 (681 non-staff rows, 546 matched, 41 unmatched; was 0.9322); RED 0.9965 (282 rows, 281 matched; was 0.9958). Gaps: 4,620 rows (was 4,568): RED 2025 `queued` → `resolved`, plus RED 2025 society-officer exclusions and the JBES 2019/2020 ASA Committee on Publications exclusions and no-affiliation rows. Staff rows: 225 (was 223; editorial coordinator 2019 and 2020).
- Two printed accents restored in the 2020 rows only, after a visual check of the 2020 page: `#15843` Marcelo Medeiros, "Pontificia Universidade Católica" (left unmatched, ROR blank: several PUCs, no campus printed); `#15853` Christoph Rothe, "Universität Mannheim" (ROR `031bsb921`, University of Mannheim). 2021–2024 rows are unchanged.
- One ROR is new to the backfill: `02jkmyk67` (Academy of Mathematics and Systems Science, CAS). All 83 distinct RORs on the new rows were re-checked as active in the ROR v2 API at publish (collector QC re-run: 51 PASS, 0 FAIL).
- **The source PDFs (`JBES_2019_editorial_board.pdf`, `JBES_2020_editorial_board.pdf`, and `RED_2025_editorial_board.pdf`) were deliberately not published.** The JBES front matter prints staff contact emails and a phone number. The transcriptions and extracts here carry no contact data.
- `editors_backfill_scale_spotcheck.csv` is byte-identical to the phone/fax-scrubbed web copy (md5 da6059469d1eee4d841cc9f2a58626f3, the same file as in `editors_backfill_red_gap_20261112`).
- Byte-prefix: the live base bytes are an exact prefix of the new panel, long table, and staff rows. The collector's intermediate freeze (base + RED 2025) is an exact prefix of the panel, long, gaps, and staff files. The gaps file is not a byte prefix of the live base, because the RED 2025 `queued` row was resolved in place.
- CRLF line endings and headers are unchanged on every CSV. No `raw_html/`, emails, phones, or photos.
- Still open: RED 2024 (RA pack 2 item S22); JBES 2025 (RA pack 2 item S23); JRU 2023.

---

"""
(OUT / "README.md").write_text(note + (P / "README.md").read_text(encoding="utf-8"), encoding="utf-8")
b = json.loads((P / "_build.json").read_text(encoding="utf-8"))
b["web_publish"] = {
    "status": "PUBLISHED (pending PR merge)",
    "published_at": "2026-11-13 (Asia/Taipei)",
    "repo_path": "data/editors/core49/releases/editors_backfill_red_jbes_20261113/",
    "branch": "publish-editors-backfill-red-jbes-20261113",
    "replaces_current_backfill": "editors_backfill_red_gap_20261112",
    "excluded_files": stats["excluded_pdfs"],
    "renamed_files": RENAME,
    "note": "Top-level status fields are the collector state at hand-off. Data files are byte-identical to the collector pack; the source PDFs are not published (staff contact data); editors_backfill_scale_spotcheck.csv is byte-identical to the phone/fax-scrubbed web copy.",
}
(OUT / "_build.json").write_text(json.dumps(b, indent=1, ensure_ascii=False), encoding="utf-8")
eol = lambda p: (p.read_bytes().count(b"\r\n"), p.read_bytes().count(b"\n"))
stats["eol"] = {}
for p in sorted(OUT.iterdir()):
    c, n = eol(p); bp = BASE / p.name
    stats["eol"][p.name] = {"crlf": c, "lf_total": n, "base": list(eol(bp)) if bp.exists() else None}
    if bp.exists() and p.suffix == ".csv":
        bc, bn = eol(bp); assert (bc == bn) == (c == n), p.name
assert not any(p.suffix.lower() in (".pdf", ".jpg", ".jpeg", ".png", ".gif", ".webp") for p in OUT.iterdir())
EMAIL = re.compile(rb"[\w.+-]+@[\w-]+\.[A-Za-z]{2,}")
stats["email_hits"] = [p.name for p in OUT.iterdir() if EMAIL.search(p.read_bytes())]
assert not stats["email_hits"]
cnt = lambda f: sum(1 for _ in csv.reader(open(f, encoding="utf-8-sig", newline=""))) - 1
stats["rows"] = {n: {"before": cnt(BASE / n), "after": cnt(OUT / n)} for n in
                 ["editors_backfill_scale_ror_panel.csv", "editor_affiliations.csv", "editors_backfill_scale_inventory.csv",
                  "editors_backfill_scale_gaps.csv", "BACKFILL_SCALE_ROR_staff_rows_20261031.csv"]}
stats["prefix_of_live_base"] = {n: (OUT / n).read_bytes().startswith((BASE / n).read_bytes()) for n in
                 ["editors_backfill_scale_ror_panel.csv", "editor_affiliations.csv", "editors_backfill_scale_gaps.csv", "BACKFILL_SCALE_ROR_staff_rows_20261031.csv"]}
stats["md5"] = {p.name: md5(p) for p in sorted(OUT.iterdir())}
Path("/tmp/red_jbes_publish_stats.json").write_text(json.dumps(stats, indent=1) + "\n")
print(json.dumps({k: v for k, v in stats.items() if k not in ("md5", "eol")}, indent=1))
