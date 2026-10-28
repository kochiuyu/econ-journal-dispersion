# editors_institution_problem_list_20261028

Problem-list cleanup of institution strings on the current boards. Frozen 2026-10-28 18:42 Asia/Hong_Kong. This supersedes `editors_institution_junk_cleanup_20261028` for Directory Institutions. Both FT50 files stay 10,046 rows. Empty `editor_name` is 0. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution.

## What the freeze changed

The collector pass touched flagged institution rows. Counts are institutions touched, then editor rows changed, across FT50, ABDC, and the AJG-gap files:

| Category | Institutions | Editor rows |
|---|---:|---:|
| junk_name | 57 | 152 |
| country_as_name | 2 | 5 |
| empty_country_with_geo_hint | 1,471 | 2,689 |
| variant_cluster | 224 | 1,738 |
| other_suspicious | 37 | 51 |

About 3,905 editor rows changed in that pass. On the FT50 ROR file this publish changes 117 `raw_affiliation` cells, 19 `ror_id` cells, and 71 `ror_country` cells. The slim file changes 118 `raw_affiliation` cells. It keeps the prior columns and does not carry ROR. The collector slim file had a partial ROR copy on 121 rows, and one of those ids disagreed with the ROR file (Sechan Oh as IBM in the United States; the ROR file keeps IBM (France)). ROR stays on `editors_ft50_current_with_ror.csv`.

## Publish holds

Two medium hits that name a different organization stay unpublished. The affiliation text stays.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School, Spain.

Tom P. Moliterno, Academy of Management Review, is matched to `https://ror.org/01vwr6t80`, the Citadel ROR already on these boards (high, exact `ror_name`). That replaces the earlier hold against The Citadel Foundation (`https://ror.org/02bygyh83`). The display name is Citadel. Country is United States.

Jaap Paauwe’s display name stays `Jaap Paauwe`. `editor_name_raw` stays `Jaap Paauwe, Tilburg`, so the ABDC copy of that Human Resource Management seat stays one row.

Where this freeze blanked `raw_affiliation` and left no `ror_name`, `canonical_name` still held the old string. Those two cells (Steve Hunt; Laurie Marshall) were cleared so the row is blank on the site. No new affiliation text was written.

| Metric | This publish |
|---|---:|
| Rows | 10,046 |
| `faculty_profile_url` | 8,375 (83.4%) |
| `raw_affiliation` on the ROR file | 9,954 (99.1%) |
| `ror_id` on the ROR file | 9,885 (98.4%) |
| Faculty URL, no `ror_id` | 39 |

The slim file has `raw_affiliation` on 9,955 rows. The directory does not read it while the ROR file is present.

Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay on the Institutions page. Every `ror_id` in this publish was already on a prior panel. No person name or URL was invented. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments stay 158,664. Editors stay 110,345. Journals stay 2,853. Countries are 176, were 172. FT50 seats stay 10,045 across 50 journals. Top 5 stays 363. UTD24 stays 5,178 across 24 journals. Faculty profile links stay 24,817. Institutions are 11,304 rows (9,287 with a ROR id), were 11,454 (9,304). 11,499 appointments have no institution, were 11,289. 628 appointments are omitted because the affiliation is only a country or territory. Three are omitted because the affiliation is only a bracketed fragment. Eight are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country.
