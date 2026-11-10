# Raw-leak fix — editors_raw_leak_fix_20261110

Published 2026-11-10 (Asia/Taipei). It supersedes `editors_raw_drift_fix_20261110` and is stacked on PR #53.

## Why

The Collector's leak scan (`RAW_DRIFT_leak_scan_20261110.csv`) found 166 more rows where a 2026-10-28/29 `institution_*` script had written a canonical or ROR name into `raw_affiliation`. The Directory carried the same text. On some rows the written name was a different organisation, for example 17 Pakistan rows that showed `National Institute of Oceanography`.

## What changed

The Directory took the Collector's directory diff: 341 cells keyed on `editor_row_key`, on 161 rows, with 0 old-value mismatches.

| Group | Rows |
|---|---:|
| Raw-only restore, same organisation (e.g. `The University of Osaka` → printed `Osaka University`) | 111 |
| Raw-only restore, wrong organisation, institution already right | 6 |
| Raw restore + institution fix | 38 |
| Reclassified: 5 Nottingham Trent → University of Nottingham Ningbo China `03y4dt428`; prio43 #1334 → University of Newcastle Australia `00eae9z71` | 6 |
| Skipped by the Collector: African Affairs prio43 #3079/#3084/#3085/#3086/#3092 | 5 |

Examples of the institution fixes:
- **Pakistan rows (17):** printed text restored, e.g. COMSATS University Islamabad `00nqqvk19`, IoBM Karachi `048w4c951`, Muslim Youth University.
- **AM Publications rows:**
  - `SAGE Publications, USA` → SAGE Publishing `05534qc24`.
  - `SAGE Publications, UK` → SAGE Publications (United Kingdom).
  - The role-only "Director, Publications" rows now have no institution.
- **Japan rows that showed `Temple University` (4):** Waseda `00ntfnx83` (×2, printed `Waheda` / `Wadesa`), Otaru University of Commerce, Hiroshima Shudo `05n757p35`.
- **`Beijing University, China`:** ajg2 #2222 (Yiqun Gan) → Peking University `02v51f717`. B #33518 (Wenbo Chen) stays Beihang `00wk2mp56`, because his profile is at Beihang; the printed raw is restored.
- **Galuh University (C #16430):** was Monash; now Universitas Galuh `03m7qjm52` (new ROR, ROR API-verified).
- **Qiang Meng (A* #18960, Transportation Science):** stays NUS, as the INFORMS board prints it. A note records his move to HKUST (Guangzhou) on 2026-08-28.

New ROR ids on the panels: `03m7qjm52` and `05534qc24`, both checked on the ROR API. No ROR id is invented.

Applied with the same commit:
- **(a) Long table:** the 6 long rows for the Top 5 seats FT50 #10046–#10048 (both FT50 files) are added from the Collector's table. It goes from 181,443 to 181,449 rows.
- **(b) FT50 #3821 Jaap Paauwe:** both files already match the Collector's name and Tilburg University `04b8v1s79`. `editor_name_raw` keeps `Jaap Paauwe, Tilburg`: the ABDC A* HRM copy of the seat (#2545) still has that spelling as its `editor_name`. The build uses `editor_name_raw` to merge the two rows, and with it blank, its check that every FT50 row has an ABDC partner fails. Once the Collector cleans A* #2545's name, `editor_name_raw` can be blanked.
- **(c) `faculty_profile_url`:** it stays blank on A #15895 and A* #13053.

Rows changed: A* 12, A 31, B 45, C 47, prio43 3, ajg2 6, ajg1 13, FT50 ROR file 3, FT50 slim 2.

## Directory

| | Before (#53 head 7e1bb69) | After | Collector |
|---|---:|---:|---:|
| Institutions | 14,176 | 14,192 | 14,192 |
| with ROR (= distinct ROR) | 6,384 | 6,386 | 6,386 |
| Countries | 162 | 162 | 162 |
| Appointments without an institution | 12,658 | 12,658 | |
| Shared display names | 49 | 49 | 49 |

## Checks

- **Scrub:** the site data has 0 e-mail addresses and 0 phone patterns. The pinned folder and the changed cells have none either.
- **Protected names and near-miss pairs:**
  - 11KBW, UNSW Sydney, INSEAD France / Singapore / UAE, 1 Decembrie 1918 University and Bank of England are intact.
  - Bolton/Boston, IIT/Indiana, Queen's Belfast/Canada, Tokyo Tech/Science Tokyo, Petru Maior/Palade and Aachen/RWTH stay separate.
- **Row counts:** ajg1 12,316, ajg2 5,462, FT50 10,047. The long table has 181,449 rows and 20 columns.
- **Untouched files:** CITATION.cff, core49 and `scripts/build_site.py`.

## Still open

- 76 restored raw values could not be verified online. Each is logged in `RAW_LEAK_source_verification_20261110.csv`.
- The pilot row `abdc_a_with_profile_pilot#15779` still has the e-mail-bearing URL. Pilots are not published.
