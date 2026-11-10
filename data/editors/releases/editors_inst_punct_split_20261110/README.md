# editors_inst_punct_split_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** Panel-only Institutions cleanup on the published Directory copy of `editors_inst_drop_rematch_20261110` (PR #46). It supersedes `editors_inst_drop_rematch_20261110` current panels. The collector pack is at `/workspace/econ-journal-editors/releases/editors_inst_punct_split_20261110`. Flag work file: `/workspace/institutions_punct_split_drop_rematch_20261110.csv` (180 rows, 180 unique displays; DROP + REMATCH_TO_EXISTING only). There is no site filter in `scripts/build_site.py`. The `*_with_profile_pilot.csv` files are **not** published. REVIEW (97) and KEEP (14) flags were excluded. No ROR id was invented.

## What this Directory copy changes vs the published #46 panels

The collector freeze panels differ from the Directory copy (guardrail restores, contact scrub, AJG1 navigation rows held out, FT50 Top 5 alignment), so they were not overlaid. This publish applies only the DROP + REMATCH + UNIFY delta, writing affiliation fields on changelog keys that already exist on the published panels. Directory guardrail text, contact-scrubbed cells, the twelve ajg1 navigation rows (ten of which still appear as extra keys in the collector file, including Vincent Pan), the two ajg2 Policy Design and Practice navigation rows, the two dropped REStud institution-as-name rows, and the three Top 5 FT50 alignment seats stay as published. Row counts are unchanged on every panel (DROP blanks the institution fields; it does not delete editor rows).

| Change | Published panel rows |
|---|---:|
| DROP leftover punctuation-start junk (CV/credential blurbs, year spans, `), Zhang, Lin (`): blank `canonical_name` / `raw_affiliation`, no ROR id | 14 (B 7, C 7) |
| REMATCH to an existing ROR twin already on these panels (printed `raw_affiliation` kept; `canonical_name` = twin `ror_name`) | 451 |
| UNIFY name-only (ROR left blank): `39 Essex Chambers` (B 2), `Izmir Bakircay University` (C 1), `Global Labor Organization (GLO), Essen, Germany` (C 1) | 4 |
| GAP | 0 |
| NOT_FOUND flag (`The University of Tokyo`, `Georgia Inst of Technology`) | 2 (not applied) |
| Invented ROR ids | 0 |

REMATCH by panel: FT50 slim 13, FT50 with_ror 20, A* 88, A 89, B 88, C 79, prio43 9, ajg2 14, ajg1 51. 469 changelog rows on published panels (456 with the FT50 slim/with_ror pair collapsed); 151 pilot rows are in the change log but not published.

`11KBW`, UNSW Sydney, and INSEAD stay, with INSEAD France `00ghzk478` and Singapore `05ynf4333` separate. CDCHTA-Universidad de Los Andes goes to Venezuela `02h1b1x27` (not Colombia). Every new `ror_id` was already on the #46 panels.

## Long table

`editor_affiliations.csv.gz` (gzip -9 -n, 7,492,590 bytes; 63,398,163 bytes uncompressed, md5 `9d12ace7e8d5b74f18fec530383fa979`). 181,443 rows, one per affiliation part, keyed by `editor_row_key`. Started from the published #46 long table (same 20-column schema), not from the collector long table (which includes pilot parts and the extra ajg1 / FT50 parts). 465 of the 474 parts on touched published keys are updated to match the collector parts; panel ↔ long sync checked on every touched key.

## Files

- `editor_affiliations.csv.gz` — long table (see above)
- `INST_PUNCT_SPLIT_changes_20261110.csv` — collector row-level change log (622 rows: 593 REMATCH, 21 DROP, 6 UNIFY, 2 NOT_FOUND; includes 151 unpublished pilot rows)
- `COLLECTOR_RELEASE_NOTES.md` — collector freeze notes
- `README.md` — this file
