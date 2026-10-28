# editors_blank_rescrape_20261028

Blank `editor_name` rows on the ABS/AJG gap boards, frozen 2026-10-28 Asia/Hong_Kong. This supersedes the parked blanks in `editors_name_swap_abdc_ajg_20261028`. The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). There is still no `faculty_profile_url`. Rankings were not edited.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. Empty `editor_name` is 0. The standing rule still drops an empty name from the person directory. The build does not invent a name or a ROR id, and it does not overwrite `raw_affiliation`. A bare country is not an institution.

## Files in this repository

Fourteen drop-quality chrome rows that were already excluded from `editors_abs_ajg_gap_20261025` stay out. The published counts below are after that exclusion.

| File | Rows | Empty `editor_name` | Nonempty `raw_affiliation` | `ror_id` filled | Fill of affiliation |
|---|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,218 | 0 | 8,665 | 8,456 | 97.6% |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,983 | 0 | 4,678 | 4,524 | 96.7% |
| `editors_abs_ajg_gap_prio43_current.csv` | 3,405 | 0 | 2,708 | 2,647 | 97.7% |
| Total | 19,606 | 0 | 16,051 | 15,627 | 97.4% |

`ror_id` is high or medium confidence only. The previous public panels had 18 empty names and `ror_id` on 15,531 of 15,993 nonempty affiliations (97.1%).

Restored boards: Risk Analysis 68, Journal of Computer-Mediated Communication 96, Journal of Latin American Studies 34. Cognitive Science and African Affairs dropped only the empty row. Annals of Work Exposures and Health merged the University of Washington affiliation onto Noah Seixas and dropped the role and UI junk (19 rows). The empty Sociology of Health and Illness row was dropped. Eight prio43 rows whose `editor_name` is `Email` (Nature Human Behaviour) stay in the CSV and stay out of the directory.

## Public site

Directory journals stay 2,853. Directory appointments are 159,093, down 11 from 159,104. The Institutions page has 10,049 rows (9,662 with a ROR id) and 147,414 appointments. No parked blank-name row is counted. Thirty-one appointments are omitted because the affiliation is only a country or territory. One is omitted because the affiliation is only a bracketed fragment. No institution row is a bare country.

ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site.

Do not merge these boards into the ABDC files.
