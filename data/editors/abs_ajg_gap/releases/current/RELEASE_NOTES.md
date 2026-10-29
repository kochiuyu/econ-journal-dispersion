# editors_apjiht_board_fix_20261029

Non-person footer and team rows replaced with rescraped editors on the AJG 1 board. Frozen 2026-10-29 22:28 Asia/Taipei. This supersedes `editors_institution_country_place_20261029`. prio43 and ajg2 are unchanged. African Affairs stays the 40-row Wayback board. Rankings were not edited. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. Empty `editor_name` is 3 on prio43, 0 on ajg2, and 18 on ajg1. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). Faculty URLs from `editors_ajg_gap_url_aff_20261028` stay. Live OUP for African Affairs is still Cloudflare-blocked. See `african_affairs_needs_browser.md`.

This publish replaces the rows of three ajg1 journals. Other rows stay as published in `editors_institution_country_place_20261029`, including the place-suffix and country corrections from that freeze. The collector ajg1 file again included 12 navigation or citation rows. They are not published. Vincent Pan on Advances in Decision Sciences stays out with them. His collector row carries `Architecture Business School` and `https://ror.org/04facnr46`. No replacement ROR was added. The collector file counted ajg1 as 11,229 to 11,256 because those 12 rows were still in it. The published file is 11,217 to 11,244.

## Boards

The old rows were footer and team labels (`Submission Guidelines`, `NeilsonJournals Publishing`, `Nj Home`, and one blank name). The new rows are people. Raw affiliation is the masthead text.

| Journal | Was | Now |
|---|---:|---:|
| Interdisciplinary Journal of Economics and Business Law | 3 | 22 |
| Journal of Business Ethics Education | 2 | 6 |
| Operations Management Education Review | 2 | 6 |

Interdisciplinary Journal of Economics and Business Law is 22 people: Editor 1, Associate Editor 1, International Board of Advisors 19, Book Review Editor 1. Source `https://www.ijebl.co.uk/ijebl_editorial_board.html`. ROR ids already on these boards are attached on 2 of 22 (Ruth Taplin, University of Leicester; Kenneth Friedman, Regis University). The other 20 stay on the masthead string. No new ROR id was added.

Journal of Business Ethics Education is 6 people: Lead Editor, Africa Editor, Asia Editor, Europe Editor, North America Editor, and Senior Advisory Editor. Source `https://www.neilsonjournals.com/JBEE/`. ROR ids already on these boards are attached on 4 of 6. Tara Ceranic Salinas and Olukunle Iyanda stay on the masthead string.

Operations Management Education Review is 6 people: Editor-in-Chief 1, Senior Editors 5. Source `https://www.neilsonjournals.com/OMER/`. ROR ids already on these boards are attached on all 6. Kathryn Stecke is medium confidence on The University of Texas at Dallas, an id already on these boards. The other five are high.

The new rows contain no email address, phone number, or photo.

## Files in this repository

Fourteen drop-quality chrome rows stay out of ajg1 and ajg2. The collector CSV again included 12 ajg1 navigation or citation rows and 2 ajg2 navigation rows. They are not published. Vincent Pan on Advances in Decision Sciences stays out with them.

| File | Rows | Empty `editor_name` | `faculty_profile_url` | Nonempty `raw_affiliation` | `ror_id` | URL, blank affiliation | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 3 | 82 | 2,723 | 2,651 | 1 | 2 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,982 | 0 | 386 | 4,727 | 4,574 | 0 | 7 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,244 | 18 | 616 | 8,843 | 8,490 | 2 | 7 |
| Total | 19,330 | 21 | 1,084 | 16,293 | 15,715 | 3 | 16 |

`ror_id` on a nonempty affiliation is 15,715 / 16,293 (96.5%): ajg1 8,490 / 8,843 (96.0%), ajg2 4,574 / 4,727 (96.8%), prio43 2,651 / 2,723 (97.4%). Gap `ror_id` was 15,703. The 12 added ids were already on these boards. Gap `ror_id` values are high or medium confidence only. A faculty URL with a blank affiliation is 3. Sixteen faculty URLs have no `ror_id`. No name, ROR id, affiliation, or URL was invented.

## Public site

Directory journals stay 2,853. Directory appointments are 158,747, were 158,624. Editors are 110,424, were 110,326. Countries stay 175. AJG journal chips stay 47 / 98 / 324 / 564 / 763 (1,796). Faculty profile links stay 24,817. The Institutions page has 10,824 rows (8,662 with a ROR id), were 10,782 (8,662), and 12,162 appointments with no institution. 633 appointments are omitted because the affiliation is only a country or territory. Three are omitted because the affiliation is only a bracketed fragment. Ten are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country. `11KBW`, UNSW Sydney, and INSEAD stay.

ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site.

Do not merge these boards into the ABDC files.
