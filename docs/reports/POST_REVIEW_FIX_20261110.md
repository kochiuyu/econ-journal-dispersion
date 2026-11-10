# Post-review Institution fix — editors_post_review_fix_20261110

Published 2026-11-10 (Asia/Taipei). It supersedes `editors_review_resolved_fix_20261110` and is stacked on PR #53.

## What changed

This is a keyed, user-approved fix from the Collector, based on the post-review Institution audit (399 names). Every edit is keyed on `editor_row_key`.

| Item | Institutions | Publish rows (Collector) |
|---|---:|---:|
| 1. Trailing city / state / country: renamed + dropped | 63 + 74 | 67 + 86 |
| 2. Role prefix: renamed + dropped | 22 + 49 | 24 + 58 |
| 3. Department prefix → parent organisation | 30 | 32 |
| 4. Near-duplicates: name merges + ROR merges + drops | 25 + 10 + 2 | 29 + 13 + 5 |
| 5. Fragments (punctuation, credential, address, place, contact): renamed + dropped | 10 + 17 | 10 + 25 |
| 6. Long bios resolved (Swiss Management Center skipped) | 3 | 3 |
| 7. Wrong RORs: STIE ×3 blanked; CUNY → `00453a208`; Abt → `0502afh35` | | 11 |
| 8. Contacts: e-mails (including comma-malformed) and phones removed | | 20 |

DROP follows the Marks mechanism: `canonical_name`, `raw_affiliation` and `ror_id` are blanked, and the printed text is kept in `ror_notes` (in the long table, `ror_match_note`). The 34 shared-name KEEP rows from the audit are untouched. No ROR id is invented.

- **ROR set:**
  - Lost: `021a5w723` (Universitas Patria Artha) and `00qj1mf81` (Schulman, Ronca & Bucuvalas), because their only rows were wrong matches.
  - Gained: `033xgn512` (IIESS, Argentina, verified against the ROR API) and `00njsd438` (Google, already on the Collector's pilot rows).

**Applied here:**
- 368 publish-panel rows differ from the previous Directory copy:
  - ABDC: A* 41, A 82, B 107, C 98.
  - AJG gap: prio43 1, ajg2 16, ajg1 17.
  - FT50: ROR file 4, slim 2.
- 260 long rows changed, including two ABDC B `editor_name` cells (#753 and #754) that held only a phone number. These are now blank, so empty `editor_name` on B is 13 (was 11).
- Every logged cell matched its `old` value (0 mismatches). For the redacted `[email removed]` / `[phone removed]` values, the match was by pattern. 21 cells already equalled the freeze value.
- Every changed panel row equals the Collector freeze row, with one exception: ABDC B `#13`, where only the `ror_notes` trace of the Directory's earlier e-mail scrub differs.
- Pilot panels are not published.

## Directory

| | Before (#53 head 8e16473) | After | Collector |
|---|---:|---:|---:|
| Institutions | 14,440 | 14,195 | 14,195 |
| with ROR (= distinct ROR) | 6,379 | 6,379 | 6,379 |
| Countries | 162 | 162 | 162 |
| Appointments without an institution | 12,487 | 12,659 | 12,659 |
| Shared display names | 49 | 49 | 49 |
| Appointments / editors / journals | 162,576 / 112,719 / 2,853 | 162,576 / 112,719 / 2,853 | |

`scripts/build_site.py` is unchanged (it already has shared-name guard 49 and the word-boundary scrub).

## Checks

- **Spot checks:**
  - The "Subscribe to receive monthly updates" Institution is gone.
  - St Petersburg University (Russia) is on `023znxa73` (28 rows).
  - IIESS is on `033xgn512`, Argentina.
  - The Inria row (prio43, Schoenauer) is on `02kvxyf05`, France.
  - All 121 CUNY rows are on `00453a208`.
  - The 5 Abt rows are on `0502afh35`.
  - The Sriparna Ghosh row (ABDC B `#13`) is clean: University of Cincinnati, `01e3m7079`, with no contact text.
- **Scrub:** the site data has 0 e-mail addresses and 0 phone patterns. Panel `editor_name`, `raw_affiliation`, `canonical_name`, `ror_notes` and `source_note` have none either.
- **Protected names and near-miss pairs:**
  - 11KBW, UNSW Sydney, INSEAD France / Singapore / UAE, 1 Decembrie 1918 University and Bank of England are intact.
  - Bolton/Boston, IIT/Indiana, Queen's Belfast/Canada, Tokyo Tech/Science Tokyo, Petru Maior/Palade and Aachen/RWTH are not merged.
- **Row counts:** unchanged (ajg1 12,316, ajg2 5,462, FT50 10,047). The long table has 181,443 rows and 20 columns.
- **Contact data:** the pinned folder contains no e-mail addresses or phone numbers.
- **Untouched files:** CITATION.cff and core49 are untouched.

## Known drift from the Collector's source panels (not changed here)

39 publish rows have a `raw_affiliation` that differs from the Collector's source panels:

- **38 rows: the Directory keeps the printed text.** In `editors_ror_consistency3b_20261101` (commit 4c3cf76, 2026-11-01, note `directory_guardrail_restore_20261101`), the Directory reverted Collector string rewrites to the published text. The Collector panels still carry those rewrites. Most came from `editors_institution_residual_post35_20261028`, for example `National Law University` replacing University of Leiden, Witwatersrand, Lyon and others, and `(Guangzhou)` dropped from HKUST (Guangzhou). A few came from `editors_institution_dept_country_20261028` and `editors_t39_plus_20261029` (`Nihon University` for 鹿児島大学, `Ikon Science`, `Korea Telecom`, `IZZI Inc`).
- **1 row: FT50 `#2955`.** The Directory's slim-file raw is blank, while the Collector's is a bio naming Colorado State University.

Six Directory keys are not in the Collector's files: `editors_ft50_current` / `_with_ror` `#10046`–`#10048`. These are the three Top 5 seats copied from ABDC A* (Snowberg and Suárez Serrato on AER, Plagborg-Moller on REStud).
