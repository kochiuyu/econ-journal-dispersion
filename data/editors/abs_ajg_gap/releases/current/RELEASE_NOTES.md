# editors_ajg_gap_url_aff_20261028

University and ROR filled where an AJG-gap row already had `faculty_profile_url` and a missing or unusable institution. Junk non-person URLs were cleared. Frozen 2026-10-28 15:05 Asia/Hong_Kong. This supersedes `editors_ajg_gap_faculty_remiss_20261028`. ABDC stays freeze `editors_nonft50_url_aff_20261028`. FT50 stays freeze `editors_ft50_url_aff_20261028`.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. Empty `editor_name` is 0. The build does not invent a name, a ROR id, an affiliation, or a faculty URL. A bare country is not an institution. `faculty_home_page` is not written to the site.

Names stay the blank-rescrape boards: ajg1 and ajg2 are `editors_blank_rescrape_20261028`; Sociology of Health and Illness on prio43 is `editors_blank_rescrape_browser_20261028`. The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). Rankings were not edited.

## Collector freeze

Host-map fills: **59**. ROR rematch on an existing affiliation: **3**. Junk URLs cleared: **3**. Junk affiliation text cleared, then refilled where the URL remained: **7**.

| Panel | Rows in the collector file | Faculty URL | Miss aff | URL, no university | URL, no ROR |
|---|---:|---:|---:|---:|---:|
| prio43 | 3,166 | 102 → **102** | 402 → **397** | 5 → **0** | 5 → **0** |
| ajg2 | 4,985 | 388 → **386** | 206 → **179** | 27 → **0** | 28 → **0** |
| ajg1 | 11,230 | 618 → **617** | 2,350 → **2,330** | 21 → **0** | 29 → **0** |
| Total | 19,381 | **1,108 → 1,105** | **2,958 → 2,906** | **53 → 0** | **62 → 0** |

Junk URLs cleared:

- Maurice Teasdale, Innovations in Education and Teaching International: `https://www.seda.ac.uk/staff/maurice-teasdale/`
- Wendy Ashall, Innovations in Education and Teaching International: `https://www.seda.ac.uk/staff/wendy-ashall/`
- Peter Cappelli, SA Journal of Human Resource Management: `https://executiveeducation.wharton.upenn.edu/faculty/peter-cappelli/`

## Published in this repository

Fourteen drop-quality chrome rows stay out of ajg1 and ajg2, the same exclusion as `editors_abs_ajg_gap_20261025`. Vincent Pan on Advances in Decision Sciences stays out with them, including his collector URL. Published faculty URLs are **1,104** (the collector’s 1,105, minus that row). Published rows with no `raw_affiliation` are **2,894** (the collector’s 2,906, minus twelve chrome rows that have no affiliation). A faculty URL with no university is **0**. A faculty URL with no `ror_id` is **0**.

| File | Rows | Empty `editor_name` | `faculty_profile_url` | Nonempty `raw_affiliation` | `ror_id` | URL, no university | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,166 | 0 | 102 | 2,769 | 2,709 | 0 | 0 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,983 | 0 | 386 | 4,805 | 4,653 | 0 | 0 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,218 | 0 | 616 | 8,899 | 8,694 | 0 | 0 |
| Total | 19,367 | 0 | 1,104 | 16,473 | 16,056 | 0 | 0 |

`ror_id` on a nonempty affiliation is 16,056 / 16,473 (97.5%): ajg1 8,694 / 8,899 (97.7%), ajg2 4,653 / 4,805 (96.8%), prio43 2,709 / 2,769 (97.8%). New and replaced ROR ids on this publish are high or medium only. Eight prio43 rows whose `editor_name` is `Email` stay in the CSV and stay out of the directory. No name, ROR id, affiliation, or URL was invented.

## Public site

Directory appointments stay 158,716. Editors stay 110,383. Journals stay 2,853. Countries stay 173. FT50 seats stay 10,045 across 50 journals. Top 5 stays 363. UTD24 stays 5,178. ABDC chips stay A* 25,174, A 45,352, B 42,124, C 26,719. AJG journal chips stay 47 / 98 / 324 / 564 / 763 (1,796).

Faculty profile links on the directory are 24,837 (were 24,840 after the remiss freeze). The three cleared junk URLs are the difference. Institutions are 10,087 (9,685 with a ROR id), were 10,093 (9,684 with a ROR id). Appointments with no institution are 10,672 (were 10,724). 28 country-only affiliations and 1 bracket-only fragment stay off that page. Parked blank `editor_name` rows are 0. Eight `Email` names on prio43 stay out of the directory.

Cherry Leonardi on African Affairs now shows Durham University and still links to `https://www.durham.ac.uk/staff/d-c-leonardi/`. The row carries only the AJG 3 badge.
