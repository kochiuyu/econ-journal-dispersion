# editors_institution_junk_cleanup_20261028

Evidenced junk in the institution field was blanked or cleared on the ABDC boards. Frozen 2026-10-28 17:48 Asia/Hong_Kong. This supersedes `editors_institution_paren_geo_20261028`. Both FT50 files stay 10,046 rows and are unchanged from that prior freeze. Empty `editor_name` is 0. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. It does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution.

## What this freeze changed on FT50

The collector file differed from the published paren-geo board in four cells. Those cells are the publish holds from `editors_institution_paren_geo_20261028`, so this publish leaves the FT50 CSVs as they were.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland, USA.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School, Spain.
- Tom P. Moliterno, Academy of Management Review: `https://ror.org/02bygyh83` is The Citadel Foundation. Affiliation kept as The Citadel, USA.
- Jaap Paauwe’s display name stays `Jaap Paauwe`. `editor_name_raw` stays `Jaap Paauwe, Tilburg`, so the ABDC copy of that Human Resource Management seat stays one row.

| Metric | This publish |
|---|---:|
| Rows | 10,046 |
| `faculty_profile_url` | 8,375 (83.4%) |
| `raw_affiliation` on the ROR file | 9,956 (99.1%) |
| `ror_id` on the ROR file | 9,867 (98.2%) |
| Faculty URL, no `ror_id` | 57 |

The slim file has `raw_affiliation` on 9,957 rows. The directory does not read it while the ROR file is present.

Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay on the Institutions page.

No person name, ROR id, or URL was invented. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments stay 158,664. Editors stay 110,345. Journals stay 2,853. Countries stay 172. FT50 seats stay 10,045 across 50 journals. Top 5 stays 363. UTD24 stays 5,178 across 24 journals. Faculty profile links stay 24,817. Institutions are 11,454 rows (9,304 with a ROR id), were 11,482 (9,312). 11,289 appointments have no institution. 628 appointments are omitted because the affiliation is only a country or territory. Three are omitted because the affiliation is only a bracketed fragment. Eight are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country.
