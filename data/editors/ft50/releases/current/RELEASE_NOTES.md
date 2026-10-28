# editors_institution_residual_post35_20261028

Residual place-in-name, country, and variant cleanup of institution strings on the current boards. Frozen 2026-10-28 23:40 Asia/Hong_Kong. This supersedes `editors_institution_dept_country_20261028` for Directory Institutions. Both FT50 files stay 10,046 rows. Empty `editor_name` is 1. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

## What this publish changed

The collector freeze touches 711 editor rows. Decided actions: strip_place 429, fix_country_only 83, strip_place_fix_country 148, merge_variant 45, strip_and_rematch 1, blank 3, rematch 2. This publish pins 539 of those rows: strip_place 331, strip_place_fix_country 148, merge_variant 45, fix_country 10, blank 3, and two `K.U.Leuven` spellings rematched to KU Leuven. By panel the pinned rows are A* 13, A 130, B 147, C 161, prio43 18, ajg2 19, and ajg1 51. The FT50 files are unchanged.

One hundred seventy-two collector rows stay as published in `editors_institution_dept_country_20261028`. Eighty-five would have copied a stripped ROR name onto a different masthead (`Italian Cultural Institute` onto Tokyo universities, or `National Law University` onto other universities). Eleven would have collapsed HKUST (Guangzhou) into The Hong Kong University of Science and Technology. Guillaume Chauvet would have lost ENSAI and kept a job title. Xiao Wang would have kept a broken parenthesis and the country `Shanghai, China`. Xiao-Wei Jiang would have swapped China University of Geosciences (Beijing) onto the parent university’s ROR. Seventy-three country-only edits are not pinned. Universidade de Santiago de Compostela stays Spain. Oxford colleges stay the United Kingdom. A masthead that says US is not moved to Sweden. `The Netherlands` stays the country label. A country change is pinned when the affiliation text names that country. A stripped ROR name is not copied onto a different affiliation. A campus in the official name stays distinct. No new ROR id was added.

The slim file still has no ROR columns. Twelve ajg1 navigation rows and two ajg2 navigation rows in the collector files stay out, including Vincent Pan on Advances in Decision Sciences.

| Metric | This publish |
|---|---:|
| Rows | 10,046 |
| Empty `editor_name` | 1 |
| `faculty_profile_url` | 8,375 (83.4%) |
| `raw_affiliation` on the ROR file | 9,946 (99.0%) |
| `ror_id` on the ROR file | 9,864 (98.2%) |
| Faculty URL, no `ror_id` | 48 |

The slim file has `raw_affiliation` on 9,942 rows and no ROR columns.

## Publish holds

Two medium hits that name a different organization stay unpublished.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. That id stays off. The masthead is `ESADE Business School`. Country stays Spain.

Jaap Paauwe’s display name stays `Jaap Paauwe`. `editor_name_raw` stays `Jaap Paauwe, Tilburg`.

`canonical_name` values cleared in earlier institution freezes stay clear on rows this publish did not edit. Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay on the Institutions page. No person name or URL was invented. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments stay 158,624. Editors stay 110,326. Journals stay 2,853. Countries stay 175. FT50 seats stay 10,044 across 50 journals. Top 5 stays 362. UTD24 stays 5,178 across 24 journals. Faculty profile links stay 24,817. Institutions are 10,835 rows (8,663 with a ROR id), were 10,888 (8,669). 12,164 appointments have no institution, were 12,161. 628 appointments are omitted because the affiliation is only a country or territory. Three are omitted because the affiliation is only a bracketed fragment. Ten are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country.
