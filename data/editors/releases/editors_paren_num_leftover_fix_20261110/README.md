# editors_paren_num_leftover_fix_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** This is a keyed, user-approved fix on the published Directory copy of `editors_tokyo_other_inst_fix_20261110` (PR #49), and it supersedes those current panels. The collector pack is at `/workspace/econ-journal-editors/releases/editors_paren_num_leftover_fix_20261110`.

Only institution fields on the 25 changelog keys were written. The collector panels were not overlaid; the collector ajg1 file has 12,326 rows and still carries the ten navigation keys, which stay out. The printed `raw_affiliation` is unchanged on every row. The Directory's `ror_notes` are kept and the `paren_num_leftover_fix_20261110:` token is appended. There is no site filter, `*_with_profile_pilot.csv` is not published, and no new ROR id is added.

| Action | Rows | Detail |
|---|---:|---|
| ORG_ONLY | 10 | A #34068 Hengeler Mueller (Germany); EDPACS C #12387 C.H. Dunn Consulting (Canada), #12390 auditline, #12391 New York State Comptroller, #12392 CMA Holdings Inc. (Canada), #12393 IsecT Ltd., #12398 AuditNet LLC, #12405 Grant Thornton (United States; joins the existing unmatched Grant Thornton row), #12411 Pepperweed, #12412 Aditya Birla Group. No ROR. |
| DROP | 1 | C #12402 Norman D. Marks: `canonical_name`, ROR and geo blank. The printed bio stays in `raw_affiliation`. |
| REMATCH | 2 | C #16656 Balázs Égert → OECD `https://ror.org/0438wbg98` (already on 34 panel rows as "Organisation de Coopération et de Développement Economiques"); ajg1 #7504 Neha Gangwar `(GGSIPU) Periyar…` → Guru Gobind Singh Indraprastha University `https://ror.org/034q1za58` (already on 3 panel rows, same name) |
| RESTORE_GEO_JAPAN | 12 | The 11 Tokyo Institute of Technology seats and Kojima. The Directory already had `ror_country` Japan / Asia, so the only change is the note token. The long-table parts gain `ror_country` Japan. |

Six of the EDPACS organisations have a blank country: Aditya Birla Group, AuditNet LLC, New York State Comptroller, Pepperweed, IsecT Ltd. and auditline.

## Long table

`editor_affiliations.csv.gz` (gzip -9 -n, 7,494,470 bytes; 63,403,880 bytes uncompressed, md5 `30ce66981f2a457ab6e86485bc580f87`). It has 181,443 rows and the same 20-column schema, and it starts from the published #49 long table. 25 of the 27 parts on touched keys are updated, and panel ↔ long ROR sync is checked.

## Files

- `editor_affiliations.csv.gz` — long table
- `PAREN_NUM_LEFTOVER_changes_20261110.csv` — collector row-level change log (25 rows)
- `COLLECTOR_RELEASE_NOTES.md` — collector freeze notes
- `README.md` — this file
