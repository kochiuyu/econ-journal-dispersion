# editors_nonlatin_inst_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** Panel-only Institutions fix on ABDC C, on top of the published Directory copy of `editors_ror_consistency3b_20261101` (PR #41). The collector pack is at `/workspace/econ-journal-editors/releases/editors_nonlatin_inst_20261110`. Other current panels (FT50, ABDC A*/A/B, AJG-gap) are unchanged from that Directory copy. There is no site filter in `scripts/build_site.py`. The `*_with_profile_pilot.csv` files are **not** published.

## What this Directory copy changes vs the published consistency3b panels

The collector freeze is based on the collector consistency3b pack, not the published Directory copy (guardrail restores, contact scrub, AJG1 navigation rows held out, FT50 Top 5 alignment). This publish applies only the ABDC C delta, 79 appointments, onto the published panels. No overlap with the Directory guardrail or contact-scrub rows.

| Change | Rows |
|---|---:|
| DROP bio/CV blurbs: blank `raw_affiliation` and `canonical_name` (no ROR id) | 19 |
| REMATCH to an existing Latin ROR twin already on these panels (printed non-Latin `raw_affiliation` / `canonical_name` kept) | 60 |
| GAP: no Latin twin on these panels; printed non-Latin name kept, ROR left blank | 8 (no panel-field change) |
| Stale flag not on the consistency3b panel | 1 (not applied) |
| Appointments touched (19 + 60 + 8) | 87 |
| Invented ROR ids | 0 |

Boards: Journal of the New Economic Association, Applied Econometrics, Academia Economic Papers, Journal of the Japan Statistical Society. `11KBW`, UNSW Sydney, and INSEAD stay. Every new `ror_id` was already on the consistency3b panels.

ABDC C stays 27,719 rows. `ror_id` is 21,297 (was 21,237). `raw_affiliation` is 24,887 (was 24,906). Empty `editor_name` stays 6; `faculty_profile_url` stays 1,379.

## Long table

`editor_affiliations.csv.gz` (gzip -9 -n, 7,461,347 bytes; 63,236,288 bytes uncompressed, md5 `e829cd1ccd0187d7800fb0770e362ae0`). 181,443 rows, one per affiliation part, keyed by `editor_row_key`. Same row set as the published consistency3b long table: the unpublished `*_with_profile_pilot.csv` parts and 14 unpublished nav/junk parts stay out, and the Directory text restores stay. 79 parts are updated to match the ABDC C panel patch (60 rematch, 19 drop). The eight GAP keys are unchanged.

## Files

- `editor_affiliations.csv.gz` — long table (see above)
- `NONLATIN_INST_changes_20261110.csv` — collector row-level change log (88 rows, including 8 GAP and 1 stale flag)
- `README.md` — this file
