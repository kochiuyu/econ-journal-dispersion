# editors_institution_post31_touchup_20261028

Post-#31 touchup of institution strings on the AJG-gap boards. Frozen 2026-10-28 20:04 Asia/Hong_Kong. This supersedes `editors_institution_residual_junk_20261028` for Directory Institutions. African Affairs stays the 40-row Wayback board. Rankings were not edited. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. Empty `editor_name` is 3 on prio43, 0 on ajg2, and 19 on ajg1. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). Faculty URLs from `editors_ajg_gap_url_aff_20261028` stay. Live OUP for African Affairs is still Cloudflare-blocked. See `african_affairs_needs_browser.md`.

The collector freeze edits 167 editor rows across FT50, ABDC, and these files. On the collector ajg1 file that count includes 21 navigation-chrome rows. Two of those rows are not on the published board, so the pinned ajg1 file changes 20 rows: 19 chrome names blanked, and Ian Martin Johnson rematched. prio43 changes 3 rows. ajg2 changes 0. No new ROR id was added.

## Files in this repository

Fourteen drop-quality chrome rows stay out of ajg1 and ajg2. The collector CSV again included 12 ajg1 navigation or citation rows and 2 ajg2 navigation rows. They are not published. Two of the ajg1 extras were blanked in this freeze (`Abstracting & Indexing` on TPM - Testing, Psychometrics, Methodology in Applied Psychology, and a newsletter row on Journal of Information Technology Management) and still stay out. Vincent Pan on Advances in Decision Sciences stays out with them. His collector row carries `Architecture Business School` and `https://ror.org/04facnr46`. No replacement ROR was added.

`canonical_name` values cleared in `editors_institution_problem_list_20261028` and `editors_institution_residual_junk_20261028` stay clear (prio43 6, ajg2 12, ajg1 18, plus the clears those freezes made on the changed rows). The collector file had restored them. This freeze did not have to clear another canonical on these files. Ian Martin Johnson’s canonical is `Robert Gordon University`, the ROR name, and the masthead already says that university.

| File | Rows | Empty `editor_name` | `faculty_profile_url` | Nonempty `raw_affiliation` | `ror_id` | URL, no university | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 3 | 82 | 2,740 | 2,675 | 0 | 2 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,982 | 0 | 386 | 4,771 | 4,580 | 0 | 6 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,217 | 19 | 616 | 8,857 | 8,533 | 0 | 7 |
| Total | 19,303 | 22 | 1,084 | 16,368 | 15,788 | 0 | 15 |

`ror_id` on a nonempty affiliation is 15,788 / 16,368 (96.5%): ajg1 8,533 / 8,857 (96.3%), ajg2 4,580 / 4,771 (96.0%), prio43 2,675 / 2,740 (97.6%). Gap `ror_id` values are high or medium confidence only. A faculty URL with no university is 0. Fifteen faculty URLs have no `ror_id`. No name, ROR id, affiliation, or URL was invented.

## Named case

Ian Martin Johnson, Journal of Humanities and Applied Social Sciences: raw is `Aberdeen Business School, The Robert Gordon University, UK`. ROR is `https://ror.org/04f0qj703`, Robert Gordon University, United Kingdom. That id was already on these boards.

## Public site

Directory journals stay 2,853. Directory appointments are 158,628, were 158,664. Editors are 110,327, were 110,345. Countries stay 176. AJG journal chips stay 47 / 98 / 324 / 564 / 763 (1,796). Faculty profile links stay 24,817. The Institutions page has 11,261 rows (9,282 with a ROR id), were 11,268 (9,286), and 11,625 appointments with no institution, were 11,539. 627 appointments are omitted because the affiliation is only a country or territory. One is omitted because the affiliation is only a bracketed fragment. Eight are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country. `11KBW`, UNSW Sydney, and INSEAD stay. Robert Gordon University stays, now including the Aberdeen Business School mastheads that name it. Aberdeen Regional Hospital is not an institution row. Hengeler Mueller stays. Dunarea de Jos University of Galati and Tribhuvan Sahkari University stay, without decorative quotes. `[C]Worthy` and A. Berland Inc. are not institution rows.

ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site.

Do not merge these boards into the ABDC files.
