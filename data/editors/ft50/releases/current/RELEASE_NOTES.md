# editors_single_editor_20261029

Fuller boards on ABDC A, ABDC B, ABDC C, and AJG 1, including the five browser-board replacements carried in this freeze. Frozen 2026-10-29 23:18 Asia/Taipei. This supersedes `editors_browser_boards_20261029`. Both FT50 files stay 10,046 rows. The only change on these two files is two trailing columns, `board_urls` and `board_url_count`, and both are blank on every FT50 row. Empty `editor_name` is 1. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

`board_urls` is a pipe-separated list of public board-page URLs, filled only on multi-page boards in the ABDC and AJG-gap files. `board_url_count` is the number of those URLs. The build selects columns by name and does not write `board_urls` to the site. `source_url` stays the primary board link.

## What this publish changed

The collector freeze replaces heading and navigation rows on five journals and expands fifteen journals that had a single editor row. This publish pins those journals on the ABDC A, ABDC B, ABDC C, and AJG 1 files. By panel that is A 2 rows to 411, B 13 rows to 219, C 12 rows to 309, and ajg1 21 rows to 321. The FT50 files, ABDC A*, prio43, and ajg2 are unchanged apart from the two blank columns. A rematch on a new row uses a ROR id already on these boards, or one exact crosswalk hit (`https://ror.org/04a85ht85`, Galgotias College of Engineering & Technology). No ROR id was invented.

Other rows stay as published in `editors_apjiht_board_fix_20261029`. The collector CSV also rewrote institution strings outside those journals. Those rows stay as published, including Tokyo mastheads that the collector would have replaced with `Italian Cultural Institute`. Twelve ajg1 navigation rows stay out, including Vincent Pan on Advances in Decision Sciences. Small Business International Review stays parked. `11KBW`, UNSW Sydney, and INSEAD stay.

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

Directory appointments are 159,961, were 158,747. Editors are 111,154, were 110,424. Journals stay 2,853. Countries stay 175. FT50 seats stay 10,044 across 50 journals. Top 5 stays 362. UTD24 stays 5,178 across 24 journals. Faculty profile links stay 24,817. Institutions are 11,276 rows (8,663 with a ROR id), were 10,824 (8,662). 12,309 appointments have no institution. 641 appointments are omitted because the affiliation is only a country or territory, were 633. Three are omitted because the affiliation is only a bracketed fragment. Ten are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country.
