# editors_open_items_fix_20261111 (built 2026-11-11 07:36, Asia/Taipei; UNPUBLISHED)
Base: `releases/editors_post_fullreview_fix_20261111` (live via PR #55, 9618a616). Input: /workspace/collector_open_items_20261111.csv (223 rows) and its .md summary.
User-approved (relayed by Econ-Journal-Web). Keyed on editor_row_key. FT50 twins are edited only when both print the same raw. Script: open_items_fix_20261111.py.
Every ROR applied was re-checked in the ROR API v2 for active status, a name fit and a country fit: 33 distinct RORs, 8 of them new to the panels (OPEN_ITEMS_rors_verified_20261111.csv).
- Niagara 05309tf52 is the US record; it gets country Canada per the approved override.
- Woxsen matches on the distinctive token only: the ROR record is "Woxsen School of Business".
The approved specifics all match the file: 0 differences.

| Item | File rows | Applied | Kept / no change | Skipped |
|---|---|---|---|---|
| 1 BIO/multi-org | 54 | 23 retarget rows (15 retargets) + Allens #45775 country -> Australia | 30 kept as printed | 0 |
| 2 near-dup | 141 | 21 rows: RSM 9 one-way, MPI comma 1, FLACSO 1, HEC Liège->ULiège, MSU, Assumption, CESS, Rutgers 5, UW-Madison abdc_b#1581; plus 9 country fills on kept rows | 36 kept, 37 closed by (c), 34 UW rows stay on the system record | 4 holds (Pacífico, Naples, Concordia, UT System) |
| 3 low-confidence | 6 | Nutraceutical -> 05bqa2z43; University of Africa -> 052vhkx86 | SRH Berlin x3 and Bank of the West: no ROR | 0 |
| 4 country conflicts | 4 | Niagara (Canada), Emden/Leer, WUNU, SWUFE 04ewct822 | | 0 |
| 5 Creative NZ | 1 | -> Creative Capital Foundation 021e5n641, US | | 0 |
| 6 St. Catharine's | 1 | -> Brock 056am2717, Canada | | 0 |
| 7 undropped | 4 | #18771 -> Dalhousie; #9281 -> Nova Southeastern; #18673 kept, country Australia | | #39063 DROP: printed raw names UNSW (protected) |
| 8 CEIBS URL | 3 | faculty_profile_url and faculty_person_key cleared on ft50_current_with_ror#4634 and ft50_current#4634 | #4501 kept | 0 |
| 9 re-check | 9 | Guangxi U, QianFoShan, Lego (Denmark), CIMMYT Mexico 03gvhpa76, Macao 00nx0vn86 (Macao), Indecon Ireland, Rutgers-NB US, CINVESTAV Mexico | | Nielsen REVIEW, no target. GM ajg1#4303 and SEARCA abdc_c#15559 are only named in that evidence and stay unchanged |

Directory, from a Web build on a copy:
- before: 11,213 / 6,692 / 6,692 / 169 / 44 (reproduces the live counts)
- after: 11,185 / 6,697 / 6,697 / 169 / 43
- Web's shared-name guard must change from 44 to 43.

QC ok:
- Row counts, headers and line endings unchanged. Long table 269,545 rows, AJG1 12,326 (nav 10 untouched), AJG2 5,462, FT50 10,049/10,049. Pilots byte-identical.
- No raw edits; the only drop was skipped.
- 0 invented RORs. Protected names OK. No non-Latin names lost; no near-miss pairs.
- 0 emails or phones.
- The only non-institution panel cells changed are the two #4634 profile cells.
- Panel-long mismatches: 0 on changed rows; 884 on the full table (base 885).
