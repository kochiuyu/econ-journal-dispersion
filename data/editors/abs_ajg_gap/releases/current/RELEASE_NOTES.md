# editors_institution_residual_junk_20261028

Residual cleanup of institution strings on the AJG-gap boards. Frozen 2026-10-28 19:29 Asia/Hong_Kong. This supersedes `editors_institution_problem_list_20261028` for Directory Institutions. African Affairs stays the 40-row Wayback board. Rankings were not edited. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. Empty `editor_name` is 0. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). Faculty URLs from `editors_ajg_gap_url_aff_20261028` stay. Live OUP for African Affairs is still Cloudflare-blocked. See `african_affairs_needs_browser.md`.

203 editor rows changed across FT50, ABDC, and these files. On these files the change is prio43 2, ajg2 8, and ajg1 16. Decorative quotes are stripped and the same `ror_id` is kept. A title or credential used as the institution name is blanked. A trailing country is stripped from an unmatched masthead string. A. Berland Inc. is blank. No new ROR id was added.

## Files in this repository

Fourteen drop-quality chrome rows stay out of ajg1 and ajg2. The collector CSV again included 12 ajg1 navigation or citation rows and 2 ajg2 navigation rows. They are not published. Vincent Pan on Advances in Decision Sciences stays out with them. His collector row carries `Architecture Business School` and `https://ror.org/04facnr46`. No replacement ROR was added.

Where this freeze blanked or shortened `raw_affiliation` and left no `ror_name`, `canonical_name` still held the old string. That copy was cleared so the row shows the cleaned text, or a blank, on the site: ajg2 1, ajg1 10. prio43 had none. `canonical_name` values cleared in `editors_institution_problem_list_20261028` stay clear (prio43 6, ajg2 12, ajg1 18). The collector file had restored them.

| File | Rows | Empty `editor_name` | `faculty_profile_url` | Nonempty `raw_affiliation` | `ror_id` | URL, no university | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 0 | 82 | 2,740 | 2,675 | 0 | 2 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,982 | 0 | 386 | 4,771 | 4,580 | 0 | 6 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,217 | 0 | 616 | 8,857 | 8,532 | 0 | 7 |
| Total | 19,303 | 0 | 1,084 | 16,368 | 15,787 | 0 | 15 |

`ror_id` on a nonempty affiliation is 15,787 / 16,368 (96.4%): ajg1 8,532 / 8,857 (96.3%), ajg2 4,580 / 4,771 (96.0%), prio43 2,675 / 2,740 (97.6%). Gap `ror_id` values are high or medium confidence only. A faculty URL with no university is 0. Fifteen faculty URLs have no `ror_id`. No name, ROR id, affiliation, or URL was invented.

## Public site

Directory journals stay 2,853. Directory appointments stay 158,664. Editors stay 110,345. Countries stay 176. AJG journal chips stay 47 / 98 / 324 / 564 / 763 (1,796). Faculty profile links stay 24,817. The Institutions page has 11,268 rows (9,286 with a ROR id), were 11,304 (9,287), and 11,539 appointments with no institution, were 11,499. 627 appointments are omitted because the affiliation is only a country or territory, were 628. One is omitted because the affiliation is only a bracketed fragment, were 3. Eight are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country. `11KBW`, UNSW Sydney, and INSEAD stay. Hengeler Mueller stays. Dunarea de Jos University of Galati and Tribhuvan Sahkari University stay, without decorative quotes. `[C]Worthy` and A. Berland Inc. are not institution rows.

ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site.

Do not merge these boards into the ABDC files.
