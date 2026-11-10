# editors_inst_punct_split_20261110

Published 2026-11-10 (Asia/Taipei) into the Directory current panels. It supersedes `editors_inst_drop_rematch_20261110` current panels (PR #46). Collector freeze path: `editors_inst_punct_split_20261110`. No site filter in `scripts/build_site.py`. No invented ROR ids. `11KBW`, UNSW Sydney, and INSEAD stay, with INSEAD France `00ghzk478` and Singapore `05ynf4333` separate. REVIEW and KEEP flags were not part of this freeze.

## Collector vs flag file

Flag work file: 180 rows, 180 unique display names (leftover punctuation starts plus high-confidence Institution splits), DROP + REMATCH_TO_EXISTING only; 97 REVIEW and 14 KEEP were left out (for example Queen's, American University, Northeastern, Concordia, Petru Maior, Universitätsklinikum Aachen).

| Action | Unique displays | Collector panel rows (all) | Published panel rows |
|---|---:|---:|---:|
| DROP | 14 | 21 | 14 |
| REMATCH to an existing panel ROR twin | 161 | 593 | 451 |
| UNIFY name-only, ROR blank | 3 | 6 | 4 |
| GAP | 0 | 0 | 0 |
| NOT_FOUND (not applied) | 2 | — | 0 |
| Invented ROR ids | 0 | 0 | 0 |

NOT_FOUND: `The University of Tokyo` (already the ROR name of `057zh3y96`) and `Georgia Inst of Technology` (the collector matched on a base with no blank-ROR row for that string; on the Directory copy it is still one unmatched Decision Sciences row).

## Directory apply

Only affiliation fields on changelog keys that already exist on the published panels were written. Directory guardrail restores, contact-scrubbed cells, held-out ajg1 / ajg2 navigation rows, and the FT50 Top 5 alignment stay. Row counts: FT50 10,047 / 10,047, A* 25,596, A 45,889, B 42,558, C 27,719, prio43 3,104, ajg2 5,462, ajg1 12,316 (all unchanged).

Examples: Aahous University - Denmark and Aalbarg University Business School → Aarhus / Aalborg twins; Aachen Institute / University of Technology and the Technical University (of) Aachen variants → RWTH Aachen University; Aalen University of Applied Sciences → Hochschule Aalen; the blank-ROR `Aalto University` seats → Aalto University (Finland); `“A.I. Cuza” University, Iaşi` → Alexandru Ioan Cuza University; `Western University` blank-ROR seats → Western University `02grkyz14`; CDCHTA-Universidad de Los Andes → Venezuela `02h1b1x27`.

The published long table (181,443 rows) is the #46 Directory long table with 465 parts updated. gzip -9 -n: 7,492,590 bytes; uncompressed 63,398,163 bytes; md5 `9d12ace7e8d5b74f18fec530383fa979`.

`scripts/build_site.py`: only the shared-display-name invariant moves from 125 to 69, because exact-name splits (a blank-ROR printed name beside the ROR row of the same name) now collapse into one row. No filter is added.

## Directory totals

Appointments 162,575. Editors 112,718. Journals 2,853.
Institutions 15,434 (6,381 with a ROR id), were 15,612 / 6,381.
Countries stay 159. Appointments without an institution: 12,066 (were 12,052). Shared display names 69 (were 125).
Country-only 650, bracket-only 12, and address-only 7 appointments stay off Institutions.

## Open item: University of Tokyo

Institutions still shows two rows: `The University of Tokyo` (ROR `057zh3y96`, 150 appointments) and an unmatched `University of Tokyo` (20 appointments). The second is 22 panel rows (20 after the FT50/ABDC collapse) whose `canonical_name` is `University of Tokyo` with a blank `ror_id` and `ror_notes` `directory_guardrail_restore_20261101: collector string rewrite reverted to published text`. The collector copies of those keys carry a wrong `Italian Cultural Institute` rewrite, which the Directory guardrail reverted, so the collector sees no blank-ROR Tokyo row (NOT_FOUND). `build_site.py` groups by `ror_id` as designed. A follow-up data patch can rematch those 22 keys to `057zh3y96`.
