# EDPACS / Marks / country fix — editors_edpacs_marks_country_fix_20261110

Published 2026-11-10 (Asia/Taipei). Supersedes `editors_paren_num_leftover_fix_20261110` (PR #50) for the Directory current panels. User-approved follow-up to PR #50.

## What changed

Only `data/editors/abdc/releases/current/editors_abdc_c_current.csv` (3 seats) and the long table (10 parts) change.

- **Norman D. Marks** (`editors_abdc_c_current#12402`, EDPACS): the printed `raw_affiliation` was only a bio, so after #50 dropped the cleaned name the site still showed it as an Institution through the printed-text fallback. The panel `raw_affiliation` and the long `raw_aff_part` are now blank. The original text is kept in `ror_notes` / `ror_match_note`. The seat now counts as an appointment without an institution.
- **Aditya Birla Group** (#12412, N.G. Shankar): India / Asia. No ROR.
- **New York State Comptroller** (#12391, David R. Hancox): United States / North America. No ROR.
- **Long table**: eight EDPACS parts with `raw_aff_part` `no` are blanked.
- AuditNet LLC, Pepperweed, IsecT Ltd. and auditline keep a blank country (no source for one).

## Checks

- Row counts unchanged: FT50 10,047; A* 25,596; A 45,889; B 42,558; C 27,719; prio43 3,104; ajg2 5,462; ajg1 12,316 (nav rows stay out).
- Long table 181,443 rows, 20 columns, gzip -9 -n; 10 lines differ from the #50 table.
- No ROR ids changed (C `ror_id` stays 21,550). No pilot files, no contact data, no "Italian Cultural Institute" introduced. `CITATION.cff`, core49 and `scripts/build_site.py` untouched; shared display names stay 69.

## Directory after build

| | Before (#50) | After |
|---|---:|---:|
| Appointments | 162,575 | 162,575 |
| Editors | 112,718 | 112,718 |
| Journals | 2,853 | 2,853 |
| Institutions | 15,435 | 15,434 |
| Institutions with ROR | 6,387 | 6,387 |
| Countries | 159 | 159 |
| Appointments without an institution | 12,066 | 12,067 |

- The Marks bio no longer appears in `site/institutions-data.js`.
- Parenthesis- or number-start Institutions: 14, all on the keep list (1 Decembrie 1918 University, 11KBW, 11powerN, 125th Street BID, 2050 Alliance, 2W China Investment Consulting, 3 Hare Court, 39 Essex Chambers, 3s Research & Consulting, 5 Wentworth Chambers, 505 Savjetovanje, 53NG, 55 Capital Partners, 720 Strategies).
- Aditya Birla Group shows India / Asia; New York State Comptroller shows United States / North America.
