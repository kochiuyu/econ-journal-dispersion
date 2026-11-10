# editors_inst_drop_rematch_20261110

Published 2026-11-10 (Asia/Taipei) into the Directory current panels. Base: the published Directory copy of `editors_nonlatin_inst_20261110` (PR #45). Collector freeze path: `editors_inst_drop_rematch_20261110`. No site filter in `scripts/build_site.py`. No invented ROR ids. `11KBW`, UNSW Sydney, and INSEAD stay, with INSEAD France `00ghzk478` and Singapore `05ynf4333` separate. REVIEW and KEEP flags were not part of this freeze.

## Collector vs flag file

Flag work file: 723 rows, 657 unique display names, DROP 88 / REMATCH_TO_EXISTING 635 (58 / 599 unique displays). The collector applied DROP+REMATCH only.

| Action | Flag rows (unique displays) | Collector panel rows | Published panel rows |
|---|---:|---:|---:|
| DROP | 88 (58) | 84 | 71 |
| REMATCH to an existing panel ROR twin | 635 (599) | 669 | 577 |
| GAP, wrong/missing twin, ROR left blank | — | 1 | 1 |
| NOT_FOUND (not applied) | — | 34 | 0 |
| Invented ROR ids | 0 | 0 | 0 |

DROP 88 vs 84: some displays were flagged in two classes (for example EXCEEDINGLY_LONG and SINGLETON_LIKELY_VARIANT), and some appear on more than one panel row. All 58 unique DROP displays were applied. REMATCH 635 vs 669: one display can sit on several appointments; 34 of the 599 unique rematch displays were NOT_FOUND (mostly official `ror_name` strings that already have a `ror_id` on every matching #45 row, plus a stale `Georgia Inst of Technology` that is already `Georgia Institute of Technology` on Decision Sciences) and 1 was GAP (`The Universidad Nacional Experimental Politécnica`; the proposed twin was Universidad Nacional, Costa Rica).

The 71 published DROPs are the collector DROP keys on the nine current panels, plus Tiffany Trzebiatowski's Journal of Management Studies CV on slim `editors_ft50_current.csv` (the collector only patched the with_ror copy). Pilots are not published (44 A + 62 B changelog rows).

## Directory apply

The collector pack's panels are based on collector consistency3b, not the published Directory copy, so they were not overlaid. Only affiliation fields on changelog keys that already exist on the published panels were written. Directory guardrail restores (Tokyo mastheads, HKUST (Guangzhou), contact-scrubbed emails and phone-as-name cells, Jaap Paauwe's `editor_name_raw`, and similar) stay. The ten extra ajg1 keys in the collector file (Vincent Pan; Information For; Latest News; a blank Journal of Information Technology Management row; A regulatory arbitrage game: Off; Privacy Policy; Sign in with Google; Supplementary Materials; Search Articles; Contact Us) stay out. Published ajg1 remains 12,316. Live and freeze ajg2 are both 5,462; the two Policy Design and Practice navigation rows stay out. FT50 stays 10,047 (three Top 5 alignment seats kept, two UPF institution-as-name rows not restored).

Elizabeth M. Lee on slim FT50 is rematched to Saint Joseph's University `https://ror.org/05q87sg56`. That rematch is not copied onto `editors_ft50_current_with_ror.csv`, which already blanks the id as Saint Joseph's (PA) vs St. Joseph's (NY) ambiguous; the Directory reads the with_ror file.

Spot checks: Bocconni University → Bocconi University `05crjpb27` (raw typo kept); Indian Institute of Technology, Dehli → IIT Delhi `049tgcd06`; Queen’s University Management School, Belfast → Queen's University Belfast `00hswnk62` (not Canada); UNSW Australia, Sydney → UNSW Sydney `03r8z3t63`; UNSW Canberra variants stay `0125wpx05`; INSEAD Fontainebleau → INSEAD France `00ghzk478` (not Singapore); Aaarhus University → Aarhus University.

The published long table (181,443 rows) is the #45 Directory long table with 662 parts updated. gzip -9 -n: 7,475,173 bytes; uncompressed 63,315,461 bytes; md5 `0e1c6a1ff951b3d02a438415b1da0f74`. The collector long table's 88,082 pilot parts, +10 ajg1 navigation parts, and +2 / +2 FT50 UPF parts were not added.

## Directory totals

Appointments 162,575. Editors 112,718. Journals 2,853.
Institutions 15,612 (6,381 with a ROR id), were 16,234 / 6,381.
Countries stay 159. Appointments without an institution: 12,052 (were 11,991). Shared display names stay 125.
Country-only 650, bracket-only 12, and address-only 7 appointments stay off Institutions.
