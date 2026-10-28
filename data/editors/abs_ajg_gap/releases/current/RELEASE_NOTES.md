# editors_institution_empty_country_20261028

Empty-country cleanup of institution strings on the AJG-gap boards. Frozen 2026-10-28 20:41 Asia/Hong_Kong. This supersedes `editors_institution_post31_touchup_20261028` for Directory Institutions. African Affairs stays the 40-row Wayback board. Rankings were not edited. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. Empty `editor_name` is 3 on prio43, 0 on ajg2, and 19 on ajg1. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). Faculty URLs from `editors_ajg_gap_url_aff_20261028` stay. Live OUP for African Affairs is still Cloudflare-blocked. See `african_affairs_needs_browser.md`.

The collector freeze edits 506 editor rows across FT50, ABDC, and these files. On the collector ajg1 file that count sits next to 12 navigation or citation rows, and the ajg2 file has 2 navigation rows. Those 14 rows are not on the published boards and stay out, including Vincent Pan on Advances in Decision Sciences. The pinned files change prio43 22, ajg2 71, and ajg1 86. A street, postal address, city fragment, or other junk string is blank. A masthead that names a university already on these boards is rematched to that existing ROR id. No new ROR id was added.

## Files in this repository

Fourteen drop-quality chrome rows stay out of ajg1 and ajg2. The collector CSV again included 12 ajg1 navigation or citation rows and 2 ajg2 navigation rows. They are not published. Vincent Pan on Advances in Decision Sciences stays out with them. His collector row carries `Architecture Business School` and `https://ror.org/04facnr46`. No replacement ROR was added.

`canonical_name` values cleared in `editors_institution_problem_list_20261028`, `editors_institution_residual_junk_20261028`, and `editors_institution_post31_touchup_20261028` stay clear. The collector file had restored them. Where this freeze blanked `raw_affiliation` and left no `ror_name`, `canonical_name` is clear. Adelaide University variants on these boards use `https://ror.org/028g18b61`, Adelaide University, Australia, an id already on these boards. The city string `Adelaide` on an ajg1 row is blank.

| File | Rows | Empty `editor_name` | `faculty_profile_url` | Nonempty `raw_affiliation` | `ror_id` | URL, blank affiliation | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 3 | 82 | 2,728 | 2,685 | 1 | 2 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,982 | 0 | 386 | 4,732 | 4,608 | 0 | 6 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,217 | 19 | 616 | 8,820 | 8,568 | 2 | 7 |
| Total | 19,303 | 22 | 1,084 | 16,280 | 15,861 | 3 | 15 |

`ror_id` on a nonempty affiliation is 15,861 / 16,280 (97.4%): ajg1 8,568 / 8,820 (97.1%), ajg2 4,608 / 4,732 (97.4%), prio43 2,685 / 2,728 (98.4%). Gap `ror_id` values are high or medium confidence only. A faculty URL with a blank affiliation is 3. Fifteen faculty URLs have no `ror_id`. No name, ROR id, affiliation, or URL was invented.

## Named case

Ian Martin Johnson, Journal of Humanities and Applied Social Sciences, stays Robert Gordon University (`https://ror.org/04f0qj703`, United Kingdom). The masthead already names that university. Shi, Peng and Bing Yan on the prio43 board are Adelaide University (`https://ror.org/028g18b61`, Australia). That id was already on these boards.

## Public site

Directory journals stay 2,853. Directory appointments are 158,624, were 158,628. Editors are 110,326, were 110,327. Countries stay 176. AJG journal chips stay 47 / 98 / 324 / 564 / 763 (1,796). Faculty profile links stay 24,817. The Institutions page has 10,915 rows (9,282 with a ROR id), were 11,261 (9,282), and 11,996 appointments with no institution, were 11,625. 627 appointments are omitted because the affiliation is only a country or territory. One is omitted because the affiliation is only a bracketed fragment. Eight are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country. `11KBW`, UNSW Sydney, and INSEAD stay. Robert Gordon University stays. Adelaide University stays, including the variant mastheads rematched to the existing id. Hengeler Mueller stays. Dunarea de Jos University of Galati and Tribhuvan Sahkari University stay, without decorative quotes. `[C]Worthy` and A. Berland Inc. are not institution rows.

ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site.

Do not merge these boards into the ABDC files.
