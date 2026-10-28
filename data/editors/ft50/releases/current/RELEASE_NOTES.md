# editors_institution_country_place_20261029

Place-suffix and country cleanup of institution strings on the current boards. Frozen 2026-10-29 00:37 Asia/Hong_Kong. This supersedes `editors_institution_residual_post35_20261028` for Directory Institutions. Both FT50 files stay 10,046 rows and are unchanged in this publish. Empty `editor_name` is 1. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

## What this publish changed

The collector freeze touches 161 editor rows: place-suffix variants 116 and country mismatches 45. This publish pins 159 of those rows on the ABDC and AJG-gap boards. By panel that is A* 5, A 36, B 60, C 46, prio43 8, ajg2 2, and ajg1 2. The FT50 files are unchanged. A place suffix is stripped. A country is corrected when the affiliation text names that country. Nine rows clear a wrong Office of Science & Technology Austria ROR and keep the masthead. A rematch uses only a ROR id already on these boards. No new ROR id was added.

The collector’s FT50 touches stay off this file. They would have copied `Italian Cultural Institute` onto University of Tokyo mastheads, attached University of Goma to Rebecca Ratner, and cleared Jaap Paauwe’s `editor_name_raw`. Those rows stay as published. Universidade de Santiago de Compostela stays Spain. HKUST (Guangzhou) stays distinct. `The Netherlands` stays the country label. A masthead that says US is not moved to Sweden. Twelve ajg1 navigation rows and two ajg2 navigation rows stay out, including Vincent Pan on Advances in Decision Sciences. `11KBW`, UNSW Sydney, and INSEAD stay.

`IBM - UK` keeps that string so the seat does not collapse into the United States `IBM` row. The country on that seat is the United Kingdom. Philip Marcovici, Suneet Trivedy, Rahul Garella, and Louise Trevaskis keep the canonical names from the previous publish.

The slim file still has no ROR columns.

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

Directory appointments stay 158,624. Editors stay 110,326. Journals stay 2,853. Countries stay 175. FT50 seats stay 10,044 across 50 journals. Top 5 stays 362. UTD24 stays 5,178 across 24 journals. Faculty profile links stay 24,817. Institutions are 10,782 rows (8,662 with a ROR id), were 10,835 (8,663). 12,164 appointments have no institution. 628 appointments are omitted because the affiliation is only a country or territory. Three are omitted because the affiliation is only a bracketed fragment. Ten are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country.
