#!/usr/bin/env python3
"""Publish editors_backfill_ra_pack2_20261113 as a new core49 release folder in /workspace/edj-web (PDFs excluded)."""
import json, shutil, hashlib, csv, re
from pathlib import Path
P = Path("/workspace/econ-journal-editors/releases/editors_backfill_ra_pack2_20261113")
WEB = Path("/workspace/edj-web/data/editors/core49/releases")
BASE = WEB / "editors_backfill_red_jbes_20261113"
OUT = WEB / "editors_backfill_ra_pack2_20261113"
OUT.mkdir(parents=True, exist_ok=True)
md5 = lambda p: hashlib.md5(p.read_bytes()).hexdigest()
SCRUBBED = "editors_backfill_scale_spotcheck.csv"
RENAME = {"RELEASE_NOTES.md": "COLLECTOR_RELEASE_NOTES.md"}
SKIP = {"README.md", "_build.json", "_live_manifest_sha256.txt"}  # README/_build rewritten below; manifest describes the collector's own folder
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
for keep in ["publish_red_jbes_20261113.py", "qc_red_jbes_20261113_web_rerun.log"]:
    shutil.copy2(BASE / keep, OUT / keep); stats["from_web_base"].append(keep)
note = '# editors_backfill_ra_pack2_20261113 — pinned in this repo (2026-11-13)\n\n**Publish note (2026-11-13, Asia/Taipei).** Published pending PR merge. It supersedes `editors_backfill_red_jbes_20261113` (PR #71) as the current core49 backfill. The older folders (`editors_backfill_red_jbes_20261113`, `editors_backfill_red_gap_20261112`, `editors_ra_ta_merge_rebuild_20261112`, `editors_backfill_scale_ror_20261031`) stay in the tree. The Directory site does not read core49 (it shows current boards only), so Directory counts are unaffected and `build_site.py` is unchanged. The collector\'s README follows below the line; its "HELD" status is historical. The collector\'s release notes are in `COLLECTOR_RELEASE_NOTES.md`.\n\n- Panel `editors_backfill_scale_ror_panel.csv`: 15,873 rows (unchanged). Exactly 19 existing rows are updated in place (same keys, same order); every other line is byte-identical to `editors_backfill_red_jbes_20261113`.\n- Long table `editor_affiliations.csv`: 12,120 rows (was 12,102; +18 appended, one per names-only fill: rank 1, sole, `is_panel_ror=1`). The only changed existing long row is the Kuersteiner row (`#2046`); all other live long rows are byte-identical.\n- RA pack 2 names-only fills (18 rows, `affiliation_imputed=yes`, flag `ra_pack2_filled_20261113`), from year-specific CVs or faculty pages: AER 2018–2022 (#999, #1055, #1089, #1205, #1260), AER: Insights 2021–2022 (#1630, #1662), JPE 2021–2023 (#12660, #12694, #12737), JOLE 2021–2023 (#11338, #11356, #11368), JLE 2020–2021 (#11452, #11461), QJE 2020–2022 (#14135, #14157, #14206). Names, roles and board source URLs are unchanged.\n- Econometric Theory 2018 G. Kuersteiner (`#2046`): campus ROR `047s2c258` (University of Maryland, College Park) from CV evidence under the campus-from-CV rule; the printed raw "University of Maryland" is kept.\n- Match rates were recomputed for the 7 touched journals only. The recount also includes 17 earlier 2026-11-06 RA-TA / RA-fix fills that the live match-rate file had not reflected (`RA_pack2_match_rate_changes_20261113.csv`). Econometric Theory 0.9469 → 0.9490 (465 of 490 matched); AER, AER: Insights, JPE, JOLE, JLE and QJE are now 1.0000 on their few affiliated rows (previously blank). All other journal rows are byte-identical.\n- All 15 distinct RORs on the 19 changed rows were re-checked as active in the ROR v2 API at publish; none is new to the backfill. `#3864` (CEPR, Montreal) and `#5947` (European U. Institute) stay ROR-blank.\n- Inventory, gaps, staff rows, matched/unmatched, crosswalk and `editors_backfill_scale_spotcheck.csv` are byte-identical to `editors_backfill_red_jbes_20261113`. The spotcheck is the phone/fax-scrubbed web copy (md5 da6059469d1eee4d841cc9f2a58626f3).\n- **The inherited source PDFs (`JBES_2019_editorial_board.pdf`, `JBES_2020_editorial_board.pdf`, `RED_2025_editorial_board.pdf`) were deliberately not published** (staff contact data). The RA pack 2 CV evidence is not published either. `_live_manifest_sha256.txt` (checksums of the collector\'s own working copy) is not published.\n- CRLF line endings and headers are unchanged on every CSV. No emails, phones, or images.\n- Still open: JRU 2023, RED 2024 and JBES 2025 (whole-board gaps); JUE 2018–2019 partial; EJ 2018 low confidence; remaining names-only rows; open ROR decisions S19 (CEPR, Montreal) and S21 (European U. Institute).\n\n---\n\n'
(OUT / "README.md").write_text(note + (P / "README.md").read_text(encoding="utf-8"), encoding="utf-8")
b = json.loads((P / "_build.json").read_text(encoding="utf-8"))
b["web_publish"] = {
    "status": "PUBLISHED (pending PR merge)",
    "published_at": "2026-11-13 (Asia/Taipei)",
    "repo_path": "data/editors/core49/releases/editors_backfill_ra_pack2_20261113/",
    "branch": "publish-editors-backfill-ra-pack2-20261113",
    "replaces_current_backfill": "editors_backfill_red_jbes_20261113",
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
cnt = lambda f: sum(1 for _ in csv.reader(open(f, encoding="utf-8-sig", newline=""))) - 1
stats["rows"] = {n: {"before": cnt(BASE / n), "after": cnt(OUT / n)} for n in
                 ["editors_backfill_scale_ror_panel.csv", "editor_affiliations.csv", "editors_backfill_scale_inventory.csv",
                  "editors_backfill_scale_gaps.csv", "BACKFILL_SCALE_ROR_staff_rows_20261031.csv"]}
stats["byte_identical_to_live_base"] = {n: (OUT / n).read_bytes() == (BASE / n).read_bytes() for n in
                 ["editors_backfill_scale_inventory.csv", "editors_backfill_scale_gaps.csv", "BACKFILL_SCALE_ROR_staff_rows_20261031.csv", SCRUBBED]}
stats["md5"] = {p.name: md5(p) for p in sorted(OUT.iterdir())}
Path("/tmp/ra_pack2_publish_stats.json").write_text(json.dumps(stats, indent=1) + "\n")
print(json.dumps({k: v for k, v in stats.items() if k not in ("md5", "eol")}, indent=1))
