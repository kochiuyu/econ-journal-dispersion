#!/usr/bin/env python3
"""Publish editors_backfill_red2024_20261114 as a new core49 release folder in /workspace/edj-web (PDFs excluded)."""
import json, shutil, hashlib, csv, re
from pathlib import Path
P = Path("/workspace/econ-journal-editors/releases/editors_backfill_red2024_20261114")
WEB = Path("/workspace/edj-web/data/editors/core49/releases")
BASE = WEB / "editors_backfill_ra_pack2_20261113"
OUT = WEB / "editors_backfill_red2024_20261114"
OUT.mkdir(parents=True, exist_ok=True)
md5 = lambda p: hashlib.md5(p.read_bytes()).hexdigest()
SCRUBBED = "editors_backfill_scale_spotcheck.csv"
RENAME = {"RELEASE_NOTES.md": "COLLECTOR_RELEASE_NOTES.md"}
SKIP = {"README.md", "_build.json", "_live_manifest_sha256.txt"}  # README/_build rewritten below; manifest describes the collector's own folder
SELF = {"publish_red2024_20261114.py", "qc_red2024_20261114_web_rerun.log"}
stats = {"copied": [], "from_web_base": [], "excluded_pdfs": [], "excluded_other": ["_live_manifest_sha256.txt"],
         "identical_to_base": [], "changed_vs_base": [], "new_vs_base": []}
assert (P / SCRUBBED).read_bytes() == (BASE / SCRUBBED).read_bytes(), "spotcheck not byte-identical to scrubbed web copy"
stats["spotcheck_byte_identical_to_scrubbed_web_copy"] = True
stats["spotcheck_md5"] = md5(BASE / SCRUBBED)
assert stats["spotcheck_md5"] == "da6059469d1eee4d841cc9f2a58626f3"
for p in sorted(P.iterdir()):
    if p.suffix.lower() == ".pdf": stats["excluded_pdfs"].append(p.name); continue
    if p.name in SKIP: continue
    if p.name == SCRUBBED:
        shutil.copy2(BASE / SCRUBBED, OUT / SCRUBBED); stats["from_web_base"].append(p.name); continue
    dst = RENAME.get(p.name, p.name)
    shutil.copy2(p, OUT / dst); stats["copied"].append(dst)
    bp = BASE / dst
    (stats["identical_to_base"] if bp.exists() and bp.read_bytes() == p.read_bytes()
     else stats["changed_vs_base"] if bp.exists() else stats["new_vs_base"]).append(dst)
# previous web-only provenance kept from the base folder
for keep in ["publish_red_jbes_20261113.py", "qc_red_jbes_20261113_web_rerun.log",
             "publish_ra_pack2_20261113.py", "qc_ra_pack2_20261113_web_rerun.log"]:
    shutil.copy2(BASE / keep, OUT / keep); stats["from_web_base"].append(keep)
note = '''# editors_backfill_red2024_20261114 — pinned in this repo (2026-11-14)

**Publish note (2026-11-14, Asia/Hong_Kong).** Published pending PR merge. It supersedes `editors_backfill_ra_pack2_20261113` (PR #72) as the current core49 backfill. The older folders (`editors_backfill_ra_pack2_20261113`, `editors_backfill_red_jbes_20261113`, `editors_backfill_red_gap_20261112`, `editors_ra_ta_merge_rebuild_20261112`, `editors_backfill_scale_ror_20261031`) stay in the tree. The Directory site does not read core49 (it shows current boards only), so Directory counts are unaffected and `build_site.py` is unchanged. The collector's README follows below the line; its "HELD" status is historical. The collector's release notes are in `COLLECTOR_RELEASE_NOTES.md`.

- Adds one journal-year, **Review of Economic Dynamics 2024** (previously a whole-board coverage gap), from the official RED Vol 52 (April 2024) Editorial Board, page ii: https://www.sciencedirect.com/science/article/pii/S1094202524000061 (DOI 10.1016/S1094-2025(24)00006-1).
- Panel `editors_backfill_scale_ror_panel.csv`: 15,917 rows (was 15,873; +44 appended, keys `editors_backfill_scale_panel#15873`–`#15916`). The live panel is an exact byte prefix of the new file: no existing row changed.
- Long table `editor_affiliations.csv`: 12,164 rows (was 12,120; +44 appended, one per new key: rank 1, sole, `is_panel_ror=1`). The live long table is an exact byte prefix: no existing long row changed.
- Roles as printed: CO-ORDINATING EDITOR 1, EDITORS 9, ASSOCIATE EDITORS 30, EDITORIAL ADVISORY BOARD 4. Conventions follow RED 2021/2025.
- ROR: 44 of 44 matched, 0 blank; 29 distinct ids, all already used in the backfill, all re-checked as active in the ROR v2 API at publish. No new ROR id.
- The 3 SED society officers (President, Treasurer, Secretary) are excluded from the panel and logged in gaps.
- Inventory: only the RED 2024 row changed (`queued` → `ok_issue_front_matter`, 44/44). Gaps: only the RED 2024 line changed (`queued` → `resolved`) plus the 3 officer lines appended. Match rates: only the RED row changed, 0.9965 (281/282) → 0.9969 (325/326).
- Staff rows, matched/unmatched, crosswalk and `editors_backfill_scale_spotcheck.csv` are byte-identical to `editors_backfill_ra_pack2_20261113`. The spotcheck is the phone/fax-scrubbed web copy (md5 da6059469d1eee4d841cc9f2a58626f3).
- **No PDF is published.** The inherited `JBES_2019_editorial_board.pdf`, `JBES_2020_editorial_board.pdf` and `RED_2025_editorial_board.pdf` (staff contact data) were deliberately withheld; the RED 2024 PDF was never in the freeze (the inventory/gaps `source_file` path refers to the collector's private copy). `_live_manifest_sha256.txt` (checksums of the collector's own working copy) is not published.
- CRLF line endings and headers are unchanged on every CSV. No emails, phones, or images.
- Still open: JBES 2025 and JRU 2023 (whole-board gaps); JUE 2018–2019 partial; EJ 2018 low confidence; remaining names-only rows; open ROR decisions S19 (CEPR, Montreal) and S21 (European U. Institute).

---

'''
(OUT / "README.md").write_text(note + (P / "README.md").read_text(encoding="utf-8"), encoding="utf-8")
b = json.loads((P / "_build.json").read_text(encoding="utf-8"))
b["web_publish"] = {
    "status": "PUBLISHED (pending PR merge)",
    "published_at": "2026-11-14 (Asia/Hong_Kong)",
    "repo_path": "data/editors/core49/releases/editors_backfill_red2024_20261114/",
    "branch": "publish-editors-backfill-red2024-20261114",
    "replaces_current_backfill": "editors_backfill_ra_pack2_20261113",
    "excluded_files": stats["excluded_pdfs"] + stats["excluded_other"],
    "renamed_files": RENAME,
    "note": "Top-level status fields are the collector state at hand-off. Data files are byte-identical to the collector pack; the inherited source PDFs are not published (staff contact data); _live_manifest_sha256.txt (checksums of the collector's own live folder) is not published; editors_backfill_scale_spotcheck.csv is byte-identical to the phone/fax-scrubbed web copy.",
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
assert not stats["email_hits"], stats["email_hits"]
for big in ["editors_backfill_scale_ror_panel.csv", "editor_affiliations.csv"]:
    assert (OUT / big).read_bytes().startswith((BASE / big).read_bytes()), big
cnt = lambda f: sum(1 for _ in csv.reader(open(f, encoding="utf-8-sig", newline=""))) - 1
stats["rows"] = {n: {"before": cnt(BASE / n), "after": cnt(OUT / n)} for n in
                 ["editors_backfill_scale_ror_panel.csv", "editor_affiliations.csv", "editors_backfill_scale_inventory.csv",
                  "editors_backfill_scale_gaps.csv", "BACKFILL_SCALE_ROR_staff_rows_20261031.csv"]}
stats["byte_prefix_of_live"] = {"editors_backfill_scale_ror_panel.csv": True, "editor_affiliations.csv": True}
stats["byte_identical_to_live_base"] = {n: (OUT / n).read_bytes() == (BASE / n).read_bytes() for n in
                 ["BACKFILL_SCALE_ROR_staff_rows_20261031.csv", "editors_backfill_scale_ror_matched.csv",
                  "editors_backfill_scale_ror_unmatched.csv", "editors_backfill_scale_row_key_crosswalk.csv", SCRUBBED]}
stats["md5"] = {p.name: md5(p) for p in sorted(OUT.iterdir()) if p.name not in SELF}
Path("/tmp/red2024_publish_stats.json").write_text(json.dumps(stats, indent=1) + "\n")
print(json.dumps({k: v for k, v in stats.items() if k not in ("md5", "eol")}, indent=1))
