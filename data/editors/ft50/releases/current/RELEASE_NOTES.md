# editors_institution_dept_country_20261028

Department and country-in-name cleanup of institution strings on the current boards. Frozen 2026-10-28 22:41 Asia/Hong_Kong. This supersedes `editors_institution_trailing_place_20261028` for Directory Institutions. Both FT50 files stay 10,046 rows. Empty `editor_name` is 1. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

## What the freeze changed

The collector freeze edits 1,168 editor rows. Pattern classes, as unique displays then editor rows: both 2/2, country_in_name 611/1,131, department_suffix 30/35. Decided actions: blank 1, blank_bad_remainder 14, clear_wrong_ror_keep_raw 1,050, rematch 11, strip_and_rematch 13, strip_both 1, strip_dept 8, strip_fallback_no_ror 2, strip_paren 67, strip_to_keep_org 1. Unmatched flag displays: 0. By panel, the collector count is FT50 ROR 18, slim FT50 4, ABDC A* 48, A 246, B 393, C 302, AJG-gap prio43 35, ajg2 38, ajg1 84.

A country string inside the institution display name is stripped. A department or faculty suffix is stripped. A rematch attaches only a ROR id already on these boards. Where `ror_name` was the parenthesis-laden string and the masthead is a different organization, the ROR is cleared and the masthead stays. No new affiliation text was written except that strip, and no new ROR id was added.

Twelve ajg1 navigation rows and two ajg2 navigation rows in the collector files are not on the published boards, so they stay out. The pinned ROR file changes 18 rows. The slim file updates 3 `raw_affiliation` cells (`Google (United States)` and `Microsoft (India)` lose the parenthesis) so the masthead matches the ROR file. The collector slim file again carried ROR columns. ROR stays on `editors_ft50_current_with_ror.csv`.

`ror_id` is on 9,864 rows, was 9,882. The cleared ids were parenthesis-laden organization names (`Google (United States)`, `Microsoft (India)`, and the same pattern on other seats). The country already stored on the row stays.

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

Two medium hits that name a different organization stay unpublished. The collector file put University of Goma back on Rebecca Ratner. The ROR stays empty.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. That id stays off. The masthead is `ESADE Business School`. Country stays Spain.

Jaap Paauwe’s display name stays `Jaap Paauwe`. `editor_name_raw` stays `Jaap Paauwe, Tilburg`. The collector file had cleared that cell.

`canonical_name` values cleared in earlier institution freezes stay clear on rows this freeze did not edit. The collector file had restored them. Where this freeze blanked `raw_affiliation` and left no `ror_name`, `canonical_name` is clear. A stripped wrong ROR name is not copied onto a different affiliation. No new ROR id was added. Every `ror_id` in this publish was already on a prior panel.

Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay on the Institutions page. No person name or URL was invented. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments stay 158,624. Editors stay 110,326. Journals stay 2,853. Countries stay 175. FT50 seats stay 10,044 across 50 journals. Top 5 stays 362. UTD24 stays 5,178 across 24 journals. Faculty profile links stay 24,817. Institutions are 10,888 rows (8,669 with a ROR id), were 10,726 (9,266). 12,161 appointments have no institution, were 12,141. 628 appointments are omitted because the affiliation is only a country or territory, were 627. Three are omitted because the affiliation is only a bracketed fragment, was 1. Ten are omitted because the affiliation is only a street, PO Box, or postal code, were 8. No institution row is a bare country.
