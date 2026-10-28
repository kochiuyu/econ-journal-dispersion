# editors_institution_trailing_place_20261028

Trailing-place cleanup of institution strings on the AJG-gap boards. Frozen 2026-10-28 21:14 Asia/Hong_Kong. This supersedes `editors_institution_empty_country_20261028` for Directory Institutions. African Affairs stays the 40-row Wayback board. Rankings were not edited. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. Empty `editor_name` is 3 on prio43, 0 on ajg2, and 19 on ajg1. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). Faculty URLs from `editors_ajg_gap_url_aff_20261028` stay. Live OUP for African Affairs is still Cloudflare-blocked. See `african_affairs_needs_browser.md`.

The collector freeze edits 2,044 editor rows across FT50, ABDC, and these files. On the collector ajg1 file that count sits next to 12 navigation or citation rows, and the ajg2 file has 2 navigation rows. Those 14 rows are not on the published boards and stay out, including Vincent Pan on Advances in Decision Sciences. The pinned files change prio43 24, ajg2 73, and ajg1 173. A trailing place or country is stripped from the organization. A role title used as the institution is blank. A masthead that names an organization already on these boards is rematched only to that existing ROR id. Where the ROR name was the place-laden string, that id is cleared. No new ROR id was added.

## Files in this repository

Fourteen drop-quality chrome rows stay out of ajg1 and ajg2. The collector CSV again included 12 ajg1 navigation or citation rows and 2 ajg2 navigation rows. They are not published. Vincent Pan on Advances in Decision Sciences stays out with them. His collector row carries `Architecture Business School` and `https://ror.org/04facnr46`. No replacement ROR was added.

`canonical_name` values cleared in `editors_institution_problem_list_20261028`, `editors_institution_residual_junk_20261028`, and `editors_institution_post31_touchup_20261028` stay clear on rows this freeze did not edit. The collector file had restored them. Where this freeze blanked `raw_affiliation` and left no `ror_name`, `canonical_name` is clear. Adelaide University variants on these boards stay on `https://ror.org/028g18b61`, Adelaide University, Australia, an id already on these boards.

| File | Rows | Empty `editor_name` | `faculty_profile_url` | Nonempty `raw_affiliation` | `ror_id` | URL, blank affiliation | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 3 | 82 | 2,723 | 2,685 | 1 | 2 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,982 | 0 | 386 | 4,728 | 4,607 | 0 | 6 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,217 | 19 | 616 | 8,810 | 8,561 | 2 | 7 |
| Total | 19,303 | 22 | 1,084 | 16,261 | 15,853 | 3 | 15 |

`ror_id` on a nonempty affiliation is 15,853 / 16,261 (97.5%): ajg1 8,561 / 8,810 (97.2%), ajg2 4,607 / 4,728 (97.4%), prio43 2,685 / 2,723 (98.6%). Gap `ror_id` values are high or medium confidence only. A faculty URL with a blank affiliation is 3. Fifteen faculty URLs have no `ror_id`. No name, ROR id, affiliation, or URL was invented.

## Named case

Jack T Boorman, Global Journal of Emerging Market Economies, was an advisor title with a Washington place. The institution is `IMF's Independent Evaluation Office`. Country is United States.

Ian Martin Johnson, Journal of Humanities and Applied Social Sciences, stays Robert Gordon University (`https://ror.org/04f0qj703`, United Kingdom). Shi, Peng and Bing Yan on the prio43 board stay Adelaide University (`https://ror.org/028g18b61`, Australia). That id was already on these boards.

## Public site

Directory journals stay 2,853. Directory appointments stay 158,624. Editors stay 110,326. Countries are 175, were 176. The Scotland label was only on a blanked city string (`Edinburgh, Scotland` on an ajg1 row). AJG journal chips stay 47 / 98 / 324 / 564 / 763 (1,796). Faculty profile links stay 24,817. The Institutions page has 10,726 rows (9,266 with a ROR id), were 10,915 (9,282), and 12,141 appointments with no institution, were 11,996. 627 appointments are omitted because the affiliation is only a country or territory. One is omitted because the affiliation is only a bracketed fragment. Eight are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country. `11KBW`, UNSW Sydney, and INSEAD stay. Robert Gordon University stays. Adelaide University stays, including the variant mastheads rematched to the existing id. Hengeler Mueller stays. Dunarea de Jos University of Galati and Tribhuvan Sahkari University stay, without decorative quotes. `[C]Worthy` and A. Berland Inc. are not institution rows.

ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site.

Do not merge these boards into the ABDC files.
