# editors_inst_drop_rematch_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** Panel-only Institutions cleanup on the published Directory copy of `editors_nonlatin_inst_20261110` (PR #45). The collector pack is at `/workspace/econ-journal-editors/releases/editors_inst_drop_rematch_20261110`. There is no site filter in `scripts/build_site.py`. The `*_with_profile_pilot.csv` files are **not** published. REVIEW and KEEP flags were excluded; only DROP and REMATCH_TO_EXISTING were applied. No ROR id was invented.

## What this Directory copy changes vs the published #45 panels

The collector freeze is based on the collector consistency3b pack, not the published Directory copy (guardrail restores, contact scrub, AJG1 navigation rows held out, FT50 Top 5 alignment). This publish applies only the DROP + REMATCH + GAP delta for keys that exist on the published panels. Directory guardrail text, contact-scrubbed cells, the twelve ajg1 navigation rows (ten of which still appear as extra keys in the collector file, including Vincent Pan), the two ajg2 Policy Design and Practice navigation rows, the two dropped REStud institution-as-name rows, and the three Top 5 FT50 alignment seats stay as published.

| Change | Published panel rows |
|---|---:|
| DROP bio/CV/address junk: blank `raw_affiliation` and `canonical_name` (no ROR id) | 71 |
| REMATCH to an existing ROR twin already on these panels (printed `raw_affiliation` kept; `canonical_name` set to the twin `ror_name`) | 577 |
| GAP: proposed twin was the wrong org; printed name kept, ROR left blank | 1 |
| NOT_FOUND flag (mostly already-matched official `ror_name` strings, plus a stale `Georgia Inst of Technology`) | 34 (not applied) |
| Invented ROR ids | 0 |

The 71 DROPs include one slim-FT50 completion: Tiffany Trzebiatowski's Journal of Management Studies CV was in the with_ror changelog and is now also blanked on `editors_ft50_current.csv` (same string; slim has no `canonical_name`, so the collector only patched with_ror). Elizabeth M. Lee's slim-FT50 rematch to Saint Joseph's University is not copied onto with_ror: that file already blanks the id as Saint Joseph's (PA) vs St. Joseph's (NY) ambiguous, and the Directory reads with_ror.

`11KBW`, UNSW Sydney, and INSEAD stay, with INSEAD France `00ghzk478` and Singapore `05ynf4333` separate. Every new `ror_id` was already on the #45 panels.

Collector vs flag-file counts (unique display names / flag rows, all panels including unpublished pilots): DROP 88 flag rows (58 unique displays) applied as 84 collector panel rows; REMATCH 635 flag rows (599 unique displays) applied as 669 collector panel rows, with 34 NOT_FOUND and 1 GAP. This Directory copy publishes the 9 current panels only (648 changelog keys, plus the slim Tiffany DROP).

## Long table

`editor_affiliations.csv.gz` (gzip -9 -n, 7,475,173 bytes; 63,315,461 bytes uncompressed, md5 `0e1c6a1ff951b3d02a438415b1da0f74`). 181,443 rows, one per affiliation part, keyed by `editor_row_key`. Started from the published #45 long table (same 20-column schema). Unpublished `*_with_profile_pilot.csv` parts (45,586 + 42,496) stay out. The collector long table's +10 ajg1 navigation parts and +2 / +2 FT50 Universitat Pompeu Fabra institution-as-name parts stay out. 662 parts are updated to match the published panel patch (661 from the collector changelog, plus the slim Tiffany DROP). The GAP key is unchanged.

## Files

- `editor_affiliations.csv.gz` — long table (see above)
- `INST_DROP_REMATCH_changes_20261110.csv` — collector row-level change log (788 rows: 669 REMATCH, 84 DROP, 1 GAP, 34 NOT_FOUND)
- `COLLECTOR_RELEASE_NOTES.md` — collector freeze notes
- `README.md` — this file
