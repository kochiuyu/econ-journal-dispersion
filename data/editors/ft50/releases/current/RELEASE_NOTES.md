# editors_institution_post31_touchup_20261028

Post-#31 touchup of institution strings on the current boards. Frozen 2026-10-28 20:04 Asia/Hong_Kong. This supersedes `editors_institution_residual_junk_20261028` for Directory Institutions. Both FT50 files stay 10,046 rows. Empty `editor_name` is 1. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

## What the freeze changed

The collector freeze edits 167 editor rows across FT50, ABDC, and the AJG-gap files. Two of those are ajg1 navigation rows that are not on the published boards, so they stay out. The pinned files change 165 rows. Pattern classes, as unique displays then editor rows: aberdeen_wrong_ror_clear 1/3, nav_chrome_editor 20/40, nav_chrome_inst 97/122, rgu_rematch 2/2.

On these two files the change is 1 row in the slim file and 1 row in the ROR file. `Read more` on Review of Economic Studies is blank. That row is not a person. The affiliation was already empty.

No new affiliation text was written on these files. No new ROR id was added. The collector slim file again carried a partial ROR copy (122 ids). One of those ids disagrees with the ROR file (Sechan Oh as IBM in the United States; the ROR file keeps IBM (France)). ROR stays on `editors_ft50_current_with_ror.csv`. The directory does not read the slim file while the ROR file is present.

| Metric | This publish |
|---|---:|
| Rows | 10,046 |
| Empty `editor_name` | 1 |
| `faculty_profile_url` | 8,375 (83.4%) |
| `raw_affiliation` on the ROR file | 9,952 (99.1%) |
| `ror_id` on the ROR file | 9,885 (98.4%) |
| Faculty URL, no `ror_id` | 39 |

The slim file has `raw_affiliation` on 9,951 rows and no ROR columns.

## Publish holds

Two medium hits that name a different organization stay unpublished. The collector file put them back. The affiliation text stays.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School, Spain.

Tom P. Moliterno, Academy of Management Review, stays on `https://ror.org/01vwr6t80`, the Citadel ROR already on these boards. Jaap Paauwe’s display name stays `Jaap Paauwe`. `editor_name_raw` stays `Jaap Paauwe, Tilburg`. The collector file had cleared that cell.

`canonical_name` values cleared in `editors_institution_problem_list_20261028` and `editors_institution_residual_junk_20261028` stay clear. The collector file had restored them. No new ROR id was added. Every `ror_id` in this publish was already on a prior panel.

Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay on the Institutions page. No person name or URL was invented. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments are 158,628, were 158,664. Editors are 110,327, were 110,345. Journals stay 2,853. Countries stay 176. FT50 seats are 10,044 across 50 journals, were 10,045. Top 5 is 362, was 363. UTD24 stays 5,178 across 24 journals. Faculty profile links stay 24,817. Institutions are 11,261 rows (9,282 with a ROR id), were 11,268 (9,286). 11,625 appointments have no institution, were 11,539. 627 appointments are omitted because the affiliation is only a country or territory. One is omitted because the affiliation is only a bracketed fragment. Eight are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country.
