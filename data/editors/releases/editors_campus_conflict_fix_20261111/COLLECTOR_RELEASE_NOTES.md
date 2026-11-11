# editors_campus_conflict_fix_20261111 (built 2026-11-11 19:18, Asia/Taipei; UNPUBLISHED)

Base: `releases/editors_school_unit_rematch_20261111` (live via Directory PR #63, 3b2b238d).
Input: `/workspace/collector_campus_conflict_20261111/campus_conflict_rematch_20261111.csv` (7 appointments, 7 editors, 2 targets) and README.md.
User-approved follow-up (2026-11-11), relayed by Econ-Journal-Web. Keyed on editor_row_key. No raw-text edits. Pilots byte-identical.
Script: `campus_conflict_fix_20261111.py`.

These seven rows were correctly left unmatched in the school-unit freeze because the earlier rematch file targeted the wrong home campus. This freeze applies only those seven. `raw_affiliation` is left as the printed masthead; `ror_id` / `ror_name` / `ror_country` (and the matching long-table part) and `canonical_name` are set to the campus target.

Both target RORs were re-checked active in ROR API v2 on 2026-11-11; name and country fit in both cases. Both were already on the published current panels. No new ROR was added.
- University of Nottingham Ningbo China `03y4dt428` (China, active)
- University of Newcastle Australia `00eae9z71` (Australia, active)

## Applied 7 / 7 (0 skips)

| Key | Editor | Before (institution / ROR / country) | After (institution / ROR / country) |
|---|---|---|---|
| `editors_abdc_c_current#18543` | Kingsley Dogah | Nottingham University Business School China / (blank) / China | University of Nottingham Ningbo China / `03y4dt428` / China |
| `editors_abdc_a_star_current#20062` | Jie Wang | Nottingham University Business School China / (blank) / China | University of Nottingham Ningbo China / `03y4dt428` / China |
| `editors_abdc_c_current#803` | Frithjof Arp | Nottingham University Business School China / (blank) / China | University of Nottingham Ningbo China / `03y4dt428` / China |
| `editors_abdc_b_current#3138` | Bruno Deschamps | Nottingham University Business School China / (blank) / China | University of Nottingham Ningbo China / `03y4dt428` / China |
| `editors_abdc_b_current#18450` | Marianna Sigala | Newcastle Business School, University of Newcastle / (blank) / Australia | University of Newcastle Australia / `00eae9z71` / Australia |
| `editors_abdc_c_current#27171` | Alison Dean | Newcastle Business School, University of Newcastle / (blank) / Australia | University of Newcastle Australia / `00eae9z71` / Australia |
| `editors_abdc_a_current#24283` | Mojtaba Barari | Newcastle Business School, University of Newcastle / (blank) / Australia | University of Newcastle Australia / `00eae9z71` / Australia |

Printed raw was unchanged on every row. UK Nottingham `01ee9ar58` and Northumbria `049e6bc10` were not assigned.

Two other unmatched NUBS China mastheads (`editors_abdc_a_current#4924`, `#5221`) were not in this file and were left as printed, so the “Nottingham University Business School China” display name remains on the Directory.

Held campus and two-place rows from the previous send were not in the file and were left as printed (47 matching rows on the base, all byte-identical). Diamond Leadership Institute and the Nielsen/SEARCA rows were not in the file and are unchanged. UK NUBS and UK Newcastle/Northumbria rows already applied in the previous freeze were not touched.

## Directory (Web build on a copy)
- before: 11,078 / 6,698 / 6,698 / 169 / 43 (reproduces the live counts)
- after:  11,077 / 6,698 / 6,698 / 169 / 43
- Shared-name guard stays 43; no change needed.
- Appointments without an institution stayed at 13,415.
- Institutions fell by 1: the Newcastle Australia display name folded into University of Newcastle Australia, which already had a ROR. The NUBS China display name remains because of the two unmatched rows not in this file. With-ROR and distinct ROR were unchanged (no new ROR). Countries unchanged at 169.

## QC: ok
- Row counts, headers and line endings unchanged. Long table 269,545 rows. AJG1 12,326 (nav 10 untouched), AJG2 5,462, FT50 10,049/10,049. Pilots byte-identical.
- No raw edits. 0 invented RORs. Protected names intact (11KBW, UNSW, INSEAD France `00ghzk478` / Singapore `05ynf4333`, 1 Decembrie 1918). No non-Latin names lost; no near-miss pairs. 0 emails or phones.
- Panel–long mismatches: 0 on changed rows; 874 on the full table (874 in the base).
