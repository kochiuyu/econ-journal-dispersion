# editors_blank_rescrape_browser_20261028

Sociology of Health and Illness on the AJG 4*/4/3 gap board, frozen 2026-10-28 10:17 Asia/Hong_Kong. This supersedes the Taylor & Francis-only browser pass. ajg1 and ajg2 are still freeze `editors_blank_rescrape_20261028`. The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). There is still no `faculty_profile_url`. Rankings were not edited.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. Empty `editor_name` is 0. The build does not invent a name or a ROR id. A bare country is not an institution.

## Files in this repository

Fourteen drop-quality chrome rows stay out of ajg1 and ajg2.

| File | Rows | Empty `editor_name` | Nonempty `raw_affiliation` | `ror_id` filled | Fill of affiliation |
|---|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,218 | 0 | 8,665 | 8,456 | 97.6% |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,983 | 0 | 4,678 | 4,524 | 96.7% |
| `editors_abs_ajg_gap_prio43_current.csv` | 3,166 | 0 | 2,716 | 2,656 | 97.8% |
| Total | 19,367 | 0 | 16,059 | 15,636 | 97.4% |

`ror_id` is high or medium confidence only. Sociology of Health and Illness went from 295 rows to 56. The other prio43 journals are unchanged. Eight rows whose `editor_name` is `Email` (Nature Human Behaviour) stay in the CSV and stay out of the directory.

## Public site

Directory journals stay 2,853. Directory appointments are 158,716, down 377 from 159,093. The Institutions page has 10,063 rows (9,657 with a ROR id) and 147,538 appointments. Twenty-nine appointments are omitted because the affiliation is only a country or territory. One is omitted because the affiliation is only a bracketed fragment. No institution row is a bare country.

ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site.

Do not merge these boards into the ABDC files.
