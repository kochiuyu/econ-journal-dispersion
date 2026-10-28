# editors_institution_residual_junk_20261028

Residual cleanup of institution strings on the current boards. Frozen 2026-10-28 19:29 Asia/Hong_Kong. This supersedes `editors_institution_problem_list_20261028` for Directory Institutions. Both FT50 files stay 10,046 rows. Empty `editor_name` is 0. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

## What the freeze changed

203 editor rows changed across FT50, ABDC, and the AJG-gap files. Pattern classes, as unique displays then editor rows: country_pair_paren 2/2, decorative_quotes 22/134, lead_paren_cred_blank 1/1, lead_paren_role_strip 1/1, lead_punct_blank 2/4, lead_punct_strip 2/2, named_blank_personal_firm 1/1, title_cred_as_name 35/42, trail_country_strip 15/15, wrong_ror_clear 1/1.

On these two files the change is 3 rows in the ROR file and 7 rows in the slim file. The ROR file blanks `, USA` (Wendy Katz) and `CEO & COO; Revlab Inc.` (Jason Bennick), and strips decorative quotes on one masthead paragraph. The slim file also strips a leading comma on two Quarterly Journal of Economics rows (Natalie Bau; Florian Zimmermann) and blanks two title lines (Marilyn Stone on Journal of Marketing and Journal of Marketing Research, plus Jason Bennick).

Where this freeze blanked `raw_affiliation` and left no `ror_name`, `canonical_name` still held the old string. The directory reads `canonical_name` before `raw_affiliation`, so that copy was cleared on the ROR file (Wendy Katz; Jason Bennick). The slim file has no `canonical_name` column. No new affiliation text was written.

| Metric | This publish |
|---|---:|
| Rows | 10,046 |
| `faculty_profile_url` | 8,375 (83.4%) |
| `raw_affiliation` on the ROR file | 9,952 (99.1%) |
| `ror_id` on the ROR file | 9,885 (98.4%) |
| Faculty URL, no `ror_id` | 39 |

The slim file has `raw_affiliation` on 9,951 rows and no ROR columns. The collector slim file again carried a partial ROR copy (122 ids). One of those ids disagrees with the ROR file (Sechan Oh as IBM in the United States; the ROR file keeps IBM (France)). ROR stays on `editors_ft50_current_with_ror.csv`. The directory does not read the slim file while the ROR file is present.

## Publish holds

Two medium hits that name a different organization stay unpublished. The collector file put them back. The affiliation text stays.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School, Spain.

Tom P. Moliterno, Academy of Management Review, stays on `https://ror.org/01vwr6t80`, the Citadel ROR already on these boards. Jaap Paauwe’s display name stays `Jaap Paauwe`. `editor_name_raw` stays `Jaap Paauwe, Tilburg`. The collector file had cleared that cell.

`canonical_name` values cleared in `editors_institution_problem_list_20261028` stay clear. The collector file had restored them (Steve Hunt; Laurie Marshall, and the same pattern on the other panels). No new ROR id was added. Every `ror_id` in this publish was already on a prior panel.

Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay on the Institutions page. No person name or URL was invented. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments stay 158,664. Editors stay 110,345. Journals stay 2,853. Countries stay 176. FT50 seats stay 10,045 across 50 journals. Top 5 stays 363. UTD24 stays 5,178 across 24 journals. Faculty profile links stay 24,817. Institutions are 11,268 rows (9,286 with a ROR id), were 11,304 (9,287). 11,539 appointments have no institution, were 11,499. 627 appointments are omitted because the affiliation is only a country or territory, were 628. One is omitted because the affiliation is only a bracketed fragment, were 3. Eight are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country.
