# editors_institution_empty_country_20261028

Empty-country cleanup of institution strings on the current boards. Frozen 2026-10-28 20:41 Asia/Hong_Kong. This supersedes `editors_institution_post31_touchup_20261028` for Directory Institutions. Both FT50 files stay 10,046 rows. Empty `editor_name` is 1. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

## What the freeze changed

The collector freeze edits 506 editor rows across FT50, ABDC, and the AJG-gap files. Twelve ajg1 navigation rows and two ajg2 navigation rows in those files are not on the published boards, so they stay out. The pinned files change 480 rows. Pattern classes, as unique displays then editor rows: address_street_postal 59/62, address_with_country 22/22, chrome_nav 44/67, city_only_fragment 27/61, credential_title_junk 56/86, other_nonsense 87/98, paper_title_abstract_junk 12/12, university_variant_existing_ror 42/98. Actions: blank 407, blank_editor_and_inst 1, blank_no_template 1, rematch 97. Sixteen flagged displays matched no panel row and were not forced.

On these two files the change is 7 rows in the slim file and 5 rows in the ROR file. A role or credential used as the institution is blank (`Production Editor`, `Senior Copy Editor`). The slim file also blanks `ESSEC` on three Organization Science rows. No new affiliation text was written. No new ROR id was added on the ROR file.

The collector slim file again carried a partial ROR copy (126 ids). One of those ids disagrees with the ROR file (Sechan Oh as IBM in the United States; the ROR file keeps IBM (France)). ROR stays on `editors_ft50_current_with_ror.csv`. The directory does not read the slim file while the ROR file is present.

| Metric | This publish |
|---|---:|
| Rows | 10,046 |
| Empty `editor_name` | 1 |
| `faculty_profile_url` | 8,375 (83.4%) |
| `raw_affiliation` on the ROR file | 9,948 (99.0%) |
| `ror_id` on the ROR file | 9,885 (98.4%) |
| Faculty URL, no `ror_id` | 39 |

The slim file has `raw_affiliation` on 9,944 rows and no ROR columns.

## Publish holds

Two medium hits that name a different organization stay unpublished. The collector file put them back. The affiliation text stays.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School, Spain.

Tom P. Moliterno, Academy of Management Review, stays on `https://ror.org/01vwr6t80`, the Citadel ROR already on these boards. Jaap Paauwe’s display name stays `Jaap Paauwe`. `editor_name_raw` stays `Jaap Paauwe, Tilburg`. The collector file had cleared that cell.

`canonical_name` values cleared in `editors_institution_problem_list_20261028`, `editors_institution_residual_junk_20261028`, and `editors_institution_post31_touchup_20261028` stay clear. The collector file had restored them. Where this freeze blanked `raw_affiliation` and left no `ror_name`, `canonical_name` is clear. No new ROR id was added. Every `ror_id` in this publish was already on a prior panel.

Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay on the Institutions page. No person name or URL was invented. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments are 158,624, were 158,628. Editors are 110,326, were 110,327. Journals stay 2,853. Countries stay 176. FT50 seats stay 10,044 across 50 journals. Top 5 stays 362. UTD24 stays 5,178 across 24 journals. Faculty profile links stay 24,817. Institutions are 10,915 rows (9,282 with a ROR id), were 11,261 (9,282). 11,996 appointments have no institution, were 11,625. 627 appointments are omitted because the affiliation is only a country or territory. One is omitted because the affiliation is only a bracketed fragment. Eight are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country.
