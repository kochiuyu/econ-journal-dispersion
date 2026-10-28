# editors_institution_problem_list_20261028

Problem-list cleanup of institution strings on the ABDC A*, A, B, and C current boards. Frozen 2026-10-28 18:42 Asia/Hong_Kong. This supersedes `editors_institution_junk_cleanup_20261028` for Directory Institutions. Row counts are unchanged. Empty `editor_name` is 0. No D4 or D5 pass is in this freeze.

`editor_name` is the name the directory shows. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. Faculty URL counts are unchanged.

The collector pass touched flagged institution rows across FT50, ABDC, and the AJG-gap files: junk_name 57 institutions / 152 rows, country_as_name 2 / 5, empty_country_with_geo_hint 1,471 / 2,689, variant_cluster 224 / 1,738, other_suspicious 37 / 51. About 3,905 editor rows changed. A trailing place is stripped from `raw_affiliation` when the country was empty, and `ror_country` is filled from that place. A variant string is unified onto an existing panel `ror_name`. No new ROR id was added.

The directory reads `canonical_name` when `ror_name` is empty. Where this freeze blanked `raw_affiliation` and left no `ror_name`, `canonical_name` still held the old string. That copy was cleared so the row is blank on the site: A* 13, A 41, B 28, C 92. Thirty-three `canonical_name` values that this freeze wrote onto a previously blank row, and that were a role, a credential, or a street, were not published. No new affiliation text was written.

## Files

| File | Rows | `raw_affiliation` | `ror_id` | `faculty_profile_url` | URL, no affiliation | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,178 | 23,848 (94.7%) | 23,644 | 12,523 (49.7%) | 3 | 60 |
| `editors_abdc_a_current.csv` | 45,363 | 43,016 (94.8%) | 42,292 | 6,237 (13.7%) | 4 | 40 |
| `editors_abdc_b_current.csv` | 42,139 | 39,875 (94.6%) | 39,110 | 3,509 (8.3%) | 0 | 19 |
| `editors_abdc_c_current.csv` | 26,720 | 23,993 (89.8%) | 23,317 | 1,379 (5.2%) | 0 | 4 |

The same two medium hits withheld on the FT50 file are withheld on the ABDC A* copy of that seat. Affiliation text stays.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School, Spain.

Tom P. Moliterno on the A* copy of Academy of Management Review uses the same Citadel ROR as the FT50 row, `https://ror.org/01vwr6t80`.

`11KBW` stays on two Public Law rows (Aileen McColgan KC, Chris Knight KC), with no ROR id. UNSW Sydney and INSEAD stay institution rows.

One A* row whose name is `___` stays off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. Directory appointments stay 158,664. ABDC chips stay A* 25,174 (219 journals), A 45,352 (626), B 42,124 (836), and C 26,719 (732). Countries are 176, were 172. Institutions are 11,304 rows (9,287 with a ROR id), were 11,454 (9,304). 11,499 appointments have no institution, were 11,289. 628 country-only appointments, 3 bracket-only appointments, and 8 street, PO Box, or postal-code appointments stay off that page.
