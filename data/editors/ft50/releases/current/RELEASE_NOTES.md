# editors_ft50_faculty_20261025

FT50 current boards after a faculty-profile fill on 2026-10-25 (Asia/Hong_Kong, 19:22). This folder replaces the FT50 slice of `editors_current_20261025`. ABDC and AJG-gap panels are not part of this freeze.

## Files

`editors_ft50_current.csv` is the slim panel: 10,050 rows, with no ROR columns. Person profile columns are `faculty_profile_url`, `faculty_home_page`, `faculty_match_method`, `faculty_match_confidence`, and `faculty_person_key`. `faculty_profile_url` is filled on 8,199 rows (81.6%), up from 4,724 rows (47.0%) in `editors_current_20261025`. 1,851 rows are still blank. `faculty_home_page` is filled on 1,824 rows (18.1%), the same count as that earlier slice.

`editors_ft50_current_with_ror.csv` is the file `scripts/build_site.py` reads when it is present (`FT50_CANDIDATES` prefers it over the slim CSV). It has the same 10,050 rows and the same `faculty_*` values, including `faculty_profile_url` on 8,199 rows (81.6%). ROR, imputation, OpenAlex, and RePEc columns match the previous file in this folder. `ror_id` was not changed (9,895 rows still have one). The five `faculty_*` columns changed only where `faculty_profile_url` had been blank: 3,475 new URLs, all `web_search` (2,998 high, 477 medium). A non-empty `faculty_profile_url` was not replaced, and no filled URL was cleared.

## Fill

| Milestone | Filled / 10,050 | Fill % |
|---|---:|---:|
| `editors_current_20261025` | 4,724 | 47.0% |
| This freeze | 8,199 | 81.6% |

Blank cells were not filled with invented OpenAlex, ORCID, or Google Scholar links. New URLs are http(s) faculty profiles. LinkedIn, ResearchGate, Wikipedia, GitHub, and publisher hubs were not added as profile URLs.

Field buckets on this freeze:

| Bucket | Filled | Rows | Fill % |
|---|---:|---:|---:|
| econ_fin_acct | 1,318 | 1,490 | 88.5% |
| other | 497 | 591 | 84.1% |
| mgmt_om_mkt_ent | 5,507 | 6,828 | 80.7% |
| psych_soc | 877 | 1,141 | 76.9% |

## Public site

The public directory links a name to `faculty_profile_url` when that value is a non-empty http(s) URL. It prefers that column over `faculty_home_page`. It does not link `faculty_home_page`, and it does not invent OpenAlex or ORCID person links. Where an FT50 appointment is also on an ABDC board, display fields, including `faculty_profile_url`, come from this FT50 file. A blank FT50 profile URL may be filled from the ABDC partner. A non-empty FT50 URL is not replaced.

Emails, phone numbers, and photos are not written to the site. ORCID, OpenAlex, and RePEc ids stay on the ROR CSV and are not published as person links. This release has no raw HTML and no search cache.
