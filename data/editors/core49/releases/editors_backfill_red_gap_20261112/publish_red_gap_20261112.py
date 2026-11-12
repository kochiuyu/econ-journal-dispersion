#!/usr/bin/env python3
"""Publish editors_backfill_red_gap_20261112 as a new core49 release folder in /workspace/edj-web."""
import json, shutil, hashlib, csv
from pathlib import Path
P = Path("/workspace/econ-journal-editors/releases/editors_backfill_red_gap_20261112")
WEB = Path("/workspace/edj-web/data/editors/core49/releases")
BASE = WEB / "editors_ra_ta_merge_rebuild_20261112"
OUT = WEB / "editors_backfill_red_gap_20261112"
OUT.mkdir(parents=True, exist_ok=True)
md5 = lambda p: hashlib.md5(p.read_bytes()).hexdigest()
SCRUBBED = "editors_backfill_scale_spotcheck.csv"
stats = {"copied": [], "from_web_base": [], "identical_to_base": [], "changed_vs_base": [], "new_vs_base": []}
assert (P / SCRUBBED).read_bytes() == (BASE / SCRUBBED).read_bytes(), "spotcheck not byte-identical to scrubbed web copy"
stats["spotcheck_byte_identical_to_scrubbed_web_copy"] = True
for p in sorted(P.iterdir()):
    if p.name in ("README.md", "_build.json"): continue
    if p.name == SCRUBBED:
        shutil.copy2(BASE / SCRUBBED, OUT / SCRUBBED); stats["from_web_base"].append(p.name); continue
    shutil.copy2(p, OUT / p.name); stats["copied"].append(p.name)
    bp = BASE / p.name
    (stats["identical_to_base"] if bp.exists() and bp.read_bytes() == p.read_bytes()
     else stats["changed_vs_base"] if bp.exists() else stats["new_vs_base"]).append(p.name)
note = """# editors_backfill_red_gap_20261112 — pinned in this repo (2026-11-12)

**Publish note (2026-11-12, Asia/Taipei).** Published with the current-board freeze `editors_current_leftovers_20261112`, pending PR merge. It supersedes `editors_ra_ta_merge_rebuild_20261112` (PR #69) as the current core49 backfill. The older folders (`editors_ra_ta_merge_rebuild_20261112`, `editors_backfill_scale_ror_20261031`) stay in the tree. The Directory site does not read core49 (it shows current boards only), so Directory counts are unaffected and `build_site.py` is unchanged for this pack. The collector's README follows below the line; its "UNPUBLISHED" status is historical.

- Panel `editors_backfill_scale_ror_panel.csv`: 15,664 rows (was 15,578; +86 appended, base rows byte-identical). Long table `editor_affiliations.csv`: 11,896 rows (was 11,810; +86 appended, one per new key).
- Review of Economic Dynamics 2022 (43 rows, `#15578`–`#15620`) and 2023 (43 rows, `#15621`–`#15663`) are now filled, from the Society for Economic Dynamics "Our Editors" page via Wayback (page versions modified 2021-04-14 and 2023-02-21; captures 20220219234913 and 20230324123429). These are the web page as printed, not the issue front matter.
- RED 2021 inventory fix: the inventory row now reads `ok_issue_front_matter`, rows_parsed 45, rows_with_affiliation 45, matching the 45 panel rows `#15446`–`#15490`. This clears the inconsistency noted at the PR #69 publish.
- Gaps: RED 2021–2023 `blocked` → `resolved` (row count unchanged at 4,568). Match rates: the RED row is recomputed (238 non-staff rows, 237 matched, 1 unmatched). Inventory: 3 rows changed, 312 rows.
- 31 distinct RORs on the new rows, all `active` in the ROR v2 API (re-checked at publish). One new row has no ROR and stays blank: `#15638` Anmol Bhandari (raw "Economics, Minneapolis, MN 55455", no institution printed).
- `editors_backfill_scale_spotcheck.csv` is byte-identical to the phone/fax-scrubbed web copy (md5 da6059469d1eee4d841cc9f2a58626f3, the same file as in `editors_ra_ta_merge_rebuild_20261112` and `editors_backfill_scale_ror_20261031`).
- CRLF line endings are preserved on every CSV. No `raw_html/`, emails, phones, or photos.
- Still open: RED 2024 (RA pack 2 item S22) and RED 2025; JBES 2019–2020 and 2025; JRU 2023.

---

"""
(OUT / "README.md").write_text(note + (P / "README.md").read_text(encoding="utf-8"), encoding="utf-8")
b = json.loads((P / "_build.json").read_text(encoding="utf-8"))
b["web_publish"] = {
    "status": "PUBLISHED (pending PR merge)",
    "published_at": "2026-11-12 (Asia/Taipei)",
    "repo_path": "data/editors/core49/releases/editors_backfill_red_gap_20261112/",
    "branch": "publish-editors-current-leftovers-20261112",
    "replaces_current_backfill": "editors_ra_ta_merge_rebuild_20261112",
    "note": "Top-level status fields are the collector state at hand-off. All files byte-identical to the collector pack; editors_backfill_scale_spotcheck.csv is byte-identical to the phone/fax-scrubbed web copy.",
}
(OUT / "_build.json").write_text(json.dumps(b, indent=1, ensure_ascii=False), encoding="utf-8")
eol = lambda p: (p.read_bytes().count(b"\r\n"), p.read_bytes().count(b"\n"))
stats["eol"] = {}
for p in sorted(OUT.iterdir()):
    c, n = eol(p); bp = BASE / p.name
    stats["eol"][p.name] = {"crlf": c, "lf_total": n, "base": list(eol(bp)) if bp.exists() else None}
    if bp.exists() and p.suffix == ".csv":
        bc, bn = eol(bp); assert (bc == bn) == (c == n), p.name
cnt = lambda f: sum(1 for _ in csv.reader(open(f, encoding="utf-8-sig", newline=""))) - 1
stats["rows"] = {n: {"before": cnt(BASE / n), "after": cnt(OUT / n)} for n in
                 ["editors_backfill_scale_ror_panel.csv", "editor_affiliations.csv", "editors_backfill_scale_inventory.csv", "editors_backfill_scale_gaps.csv"]}
stats["md5"] = {p.name: md5(p) for p in sorted(OUT.iterdir())}
Path("/tmp/red_gap_publish_stats.json").write_text(json.dumps(stats, indent=1) + "\n")
print(json.dumps({k: v for k, v in stats.items() if k not in ("md5", "eol")}, indent=1))
