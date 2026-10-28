# editors_name_swap_20261028

Name and ROR fields on the ABS/AJG gap current boards, frozen 2026-10-28 09:31 Asia/Hong_Kong. This supersedes `editors_abs_ajg_gap_ror_20261026_bracketfix` for the cells this freeze changed. The journal set and the row filter are still `editors_abs_ajg_gap_20261025`. There is still no `faculty_profile_url`. ABDC B and C were not edited. Rankings were not edited.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. An empty `editor_name` is not a person. When that row has a `ror_id`, Institutions still counts the appointment and does not count an editor. The build does not invent a name or a ROR id, and it does not overwrite `raw_affiliation`.

## Files in this repository

The collector live panels are 11,288 / 5,032 / 3,490. Fourteen of those rows were already excluded from `editors_abs_ajg_gap_20261025` as drop-quality chrome (publisher navigation, a paper title, and similar). They are in this freeze's live files and stay out of the public files, so the row counts are unchanged. None of the fourteen is a blank `editor_name`.

| File | Rows | Empty `editor_name` | Nonempty `raw_affiliation` | `ror_id` filled | Fill of affiliation |
|---|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,276 | 24 | 8,654 | 8,426 | 97.4% |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5,030 | 41 | 4,671 | 4,488 | 96.1% |
| `editors_abs_ajg_gap_prio43_current.csv` | 3,490 | 22 | 2,634 | 2,524 | 95.8% |
| Total | 19,796 | 87 | 15,959 | 15,438 | 96.7% |

The previous public panels had `ror_id` on 15,384 of 15,929 nonempty affiliations (96.6%). `ror_id` on these files is high or medium confidence only. Low-confidence hits stay off `ror_id`.

Empty `editor_name` cells with a `ror_id`: ajg1 19, ajg2 19, prio43 22, total 60. Those 60 are institution appointments. The other blank-name rows stay in the CSV and are not institution rows, because they have no `ror_id`. Eight prio43 rows whose `editor_name` is `Email` (Nature Human Behaviour) stay in the CSV and stay out of the directory. They are not parked blanks.

The collector change log records 86 `blank_org_as_name` actions (ajg1 22, ajg2 41, prio43 21, plus 2 on ABDC A*). The published gap files have 87 empty `editor_name` cells. No person name was filled in for those rows.

## Public site

Directory journals stay 2,853. Directory appointments are 159,308 (were 159,399). The Institutions page has 10,091 rows (9,673 with a ROR id) and 147,233 appointments (was 10,099 rows, 9,674 with a ROR id, and 147,195 appointments). Sixty parked rows with a `ror_id` are included in the appointment total and are not editors. One of those is the only appointment at Roche (Chile): the frozen medium match on the Journal of Latin American Studies affiliation `Chile Chile`. That ROR id was not cleared here. Sixty-four appointments are omitted because the affiliation is only a country or territory (was 100). Two are omitted because the affiliation is only a bracketed fragment. No remaining unmatched affiliation is only a street, PO Box, or postal code.

Bare-country, fully bracketed, and address-only unmatched affiliations stay off Institutions, as in the previous build. A filled `ror_id` stays. ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site.

Do not merge these boards into the ABDC files.
