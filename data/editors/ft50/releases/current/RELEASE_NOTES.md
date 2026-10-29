# editors_apjiht_board_fix_20261029

Non-person footer and team rows replaced with rescraped editors on the ABDC A, ABDC C, and AJG 1 boards. Frozen 2026-10-29 22:28 Asia/Taipei. This supersedes `editors_institution_country_place_20261029`. Both FT50 files stay 10,046 rows and are unchanged in this publish. Empty `editor_name` is 1. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

## What this publish changed

The collector freeze replaces footer and team rows on eight journals. This publish pins those journals on the ABDC A, ABDC C, and AJG 1 files. By panel that is A 26 rows to 31, C 2 rows to 91, and ajg1 7 rows to 34. The FT50 files, ABDC A*, ABDC B, prio43, and ajg2 are unchanged. A rematch on a new row uses only a ROR id already on these boards. No new ROR id was added.

Other rows stay as published in `editors_institution_country_place_20261029`. The collector CSV also rewrote institution strings outside those eight journals. Those rows stay as published, including Tokyo mastheads that the collector would have replaced with `Italian Cultural Institute`. Twelve ajg1 navigation rows stay out, including Vincent Pan on Advances in Decision Sciences. `11KBW`, UNSW Sydney, and INSEAD stay.

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

Directory appointments are 158,747, were 158,624. Editors are 110,424, were 110,326. Journals stay 2,853. Countries stay 175. FT50 seats stay 10,044 across 50 journals. Top 5 stays 362. UTD24 stays 5,178 across 24 journals. Faculty profile links stay 24,817. Institutions are 10,824 rows (8,662 with a ROR id), were 10,782 (8,662). 12,162 appointments have no institution. 633 appointments are omitted because the affiliation is only a country or territory. Three are omitted because the affiliation is only a bracketed fragment. Ten are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country.
