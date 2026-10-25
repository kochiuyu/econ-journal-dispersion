# editors_abs_ajg_gap_20261025

Frozen ABS/AJG **gap** current editor panels (journals not already covered by FT50/ABDC freezes), cleaned for public Directory display.

Generated: 2026-10-25 11:49 HKT (Asia/Hong_Kong).

## Files
| File | Freeze rows | Live panel rows | Excluded drop-quality |
|---|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3490 | 3490 | 0 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5030 | 5032 | 2 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11276 | 11288 | 12 |

Columns include `tenure_start`, `tenure_end`, `tenure_raw`, `is_current` plus existing ROR / impute / id fields. No faculty_profile_url on these gap panels yet.

## QC summary (Collector, 2026-10-25)
1. **Name-year strip + tenure:** term years like `(2004–2022)` stripped from `editor_name`; tenure_* filled (12 name strips, 80 year-only aff clears, 91 tenure fills across AJG).
2. **Junk drop pass:** Emerald metrics, TOC `Vol/Issue`, postal lines, role-only, non-person titles removed from live panels (277 rows).
3. **Manual-review pass 2:** 209 flags → 126 drop, 75 safe_fix (single-year→tenure, Vol markers, role parens, A-and-B splits, HTML unescape), 8 residual.
4. **Residual-8 hand fix:** all 8 mashed strings fixed (institution/dept moved into `raw_affiliation` or titles stripped; no invented given names). See `abs_ajg/reports/RESIDUAL8_FIX_20261025.csv`.
5. **Aff email strip:** parenthetical `(name @ domain)` removed from `raw_affiliation`, institution text kept. Log: `abs_ajg/reports/AFF_EMAIL_STRIP_20261025.csv`.
6. **Freeze filter:** any remaining drop-quality `editor_name` patterns excluded from this release (not deleted from live panels if any). Log: `abs_ajg/reports/FREEZE_EXCLUDED_DROP_QUALITY_20261025.csv`.

## Do not display
Rows matching publisher metrics, volume TOC lines, postal fragments, role-only labels, ethics/mission blurbs — excluded above. Aff-only prose blobs may remain rare; Web may hide empty/`editor_name` blanks.

## Handoff
Copy these three CSVs into the public monorepo under `data/editors/abs_ajg_gap/` (or project equivalent) `releases/editors_abs_ajg_gap_20261025/`.  
Collector does **not** push GitHub; Econ-Journal-Web publishes.  
See sibling `HANDOFF_WEB.md` in this folder.

## In this repository

Published at `data/editors/abs_ajg_gap/releases/current/`, the same current-board layout as the FT50 and ABDC freezes. The freeze id is `editors_abs_ajg_gap_20261025`.

`scripts/build_site.py` reads the three CSVs into the directory, the journal list, and the institution list. ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site. There is no `faculty_profile_url` on these files, so person names stay plain text. A board link is `source_url` when that value is http(s). Paths that are not http(s) are omitted.

Eight prio43 rows whose `editor_name` is `Email` (Nature Human Behaviour) stay in the CSV and are omitted from the directory by the existing non-person name filter. The ROR columns are on the files and are empty in this freeze, so those appointments group by affiliation text.
