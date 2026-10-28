# editors_name_swap_abdc_ajg_20261028

Name and ROR fields on the ABS/AJG gap current boards, frozen 2026-10-28 09:48 Asia/Hong_Kong. This supersedes `editors_name_swap_20261028`. The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). There is still no `faculty_profile_url`. Rankings were not edited.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. An empty `editor_name` is not a person. When that row has a `ror_id`, Institutions still counts the appointment and does not count an editor. The build does not invent a name or a ROR id, and it does not overwrite `raw_affiliation`.

Pure institution-as-name is 0 on these files.

## Files in this repository

The collector live panels in this freeze are 11,238 / 4,986 / 3,445. Fourteen drop-quality chrome rows that were already excluded from `editors_abs_ajg_gap_20261025` (publisher navigation, a paper title, and similar) are still in those live files and stay out, so the published counts are 11,226 / 4,984 / 3,445. None of the fourteen has an empty `editor_name`.

| File | Rows | Empty `editor_name` | With `ror_id` | Nonempty `raw_affiliation` | `ror_id` filled | Fill of affiliation |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,226 | 1 | 1 | 8,666 | 8,457 | 97.6% |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,984 | 1 | 1 | 4,670 | 4,513 | 96.6% |
| `editors_abs_ajg_gap_prio43_current.csv` | 3,445 | 16 | 15 | 2,657 | 2,561 | 96.4% |
| Total | 19,655 | 18 | 17 | 15,993 | 15,531 | 97.1% |

`ror_id` on these files is high or medium confidence only. The previous public panels (`editors_name_swap_20261028`) had `ror_id` on 15,438 of 15,959 nonempty affiliations (96.7%) and 87 empty names.

The empty names that remain are Annals of Work Exposures and Health (ajg1), Journal of Latin American Studies (ajg2), and on prio43: Risk Analysis (11), Journal of Computer-Mediated Communication (2), African Affairs (1), Cognitive Science (1), and Sociology of Health and Illness (1). Eight prio43 rows whose `editor_name` is `Email` (Nature Human Behaviour) stay in the CSV and stay out of the directory. They are not parked blanks.

## Public site

Directory journals stay 2,853. Directory appointments are 159,104. The Institutions page has 10,101 rows (9,678 with a ROR id) and 147,363 appointments. Fifty-five parked rows with a `ror_id`, across ABDC and these boards, are included in that appointment total and are not editors. Seven institutions have only those parked appointments. Thirty appointments are omitted because the affiliation is only a country or territory. One is omitted because the affiliation is only a bracketed fragment. No remaining unmatched affiliation is only a street, PO Box, or postal code.

ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site.

Do not merge these boards into the ABDC files.
