# editors_edpacs_marks_country_fix_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** This is a keyed, user-approved follow-up on the published Directory copy of `editors_paren_num_leftover_fix_20261110` (PR #50), and it supersedes those current panels. The collector pack is at `/workspace/econ-journal-editors/releases/editors_edpacs_marks_country_fix_20261110`.

Only the fields named in the 16-row field-level change log were written, on three `editors_abdc_c_current.csv` seats and ten long-table parts. The collector panels were not overlaid. The Directory's `ror_notes` are kept and the `edpacs_marks_country_fix_20261110:` token is appended. There is no site filter, `*_with_profile_pilot.csv` is not published, and no ROR id changes.

| Action | Where | Detail |
|---|---|---|
| BLANK_RAW_BIO | C #12402 Norman D. Marks | panel `raw_affiliation` and long `raw_aff_part` blanked (user-approved). The original bio `(CPA, CRMA) - Author, Speaker, Thought Leader, OCEG Fellow, Honorary Fellow of the Institute of Risk Management` is kept in `ror_notes` and the long `ror_match_note`. |
| SET_COUNTRY | C #12412 Aditya Birla Group | `ror_country` India, `continent` Asia (panel); long `ror_country` India. No ROR. |
| SET_COUNTRY | C #12391 New York State Comptroller | `ror_country` United States, `continent` North America (panel); long `ror_country` United States. No ROR. |
| FIX_LONG_NO | long #12387, #12390, #12392, #12393, #12398, #12405, #12411, #12412 | `raw_aff_part` `no` (an affiliation-imputed flag) → blank, matching the blank panel `raw_affiliation`. |

AuditNet LLC, Pepperweed, IsecT Ltd. and auditline keep a blank country.

## Long table

`editor_affiliations.csv.gz` (gzip -9 -n, 7,494,567 bytes; 63,404,965 bytes uncompressed, md5 `ef03e06a7658d90360260df48cadb691`). It has 181,443 rows and the same 20-column schema, and it starts from the published #50 long table. Exactly 10 lines differ from it.

## Files

- `editor_affiliations.csv.gz` — long table
- `EDPACS_MARKS_COUNTRY_changes_20261110.csv` — collector field-level change log (16 rows)
- `COLLECTOR_RELEASE_NOTES.md` — collector freeze notes
- `README.md` — this file
