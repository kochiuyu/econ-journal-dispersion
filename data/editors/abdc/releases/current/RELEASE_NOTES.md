# editors_apjiht_board_fix_20261029

Non-person footer and team rows replaced with rescraped editors on the ABDC A and C current boards. Frozen 2026-10-29 22:28 Asia/Taipei. This supersedes `editors_institution_country_place_20261029`. A* and B row counts are unchanged. Empty `editor_name` is 2 on A*, 1 on A, 0 on B, and 11 on C. No D4 or D5 pass is in this freeze.

`editor_name` is the name the directory shows. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution. Faculty URL counts are unchanged.

This publish replaces the rows of five journals on these files. Other rows stay as published in `editors_institution_country_place_20261029`, including the place-suffix and country corrections from that freeze. The collector CSV also rewrote institution strings on other journals, including `Italian Cultural Institute` on Tokyo mastheads and `National Law University` on other mastheads. Those rows stay as published. A rematch on a new row uses only a ROR id already on these boards. No new ROR id was added.

## Boards

The old rows were footer and team labels (`Publishing Ethics`, `SEARCH Editorial Team`, `Journal Home`, and the same kind of chrome). The new rows are people. Raw affiliation is the masthead text.

| Journal | Rating | Was | Now |
|---|---|---:|---:|
| Asia-Pacific Journal of Innovation in Hospitality and Tourism | C | 2 | 91 |
| The BE Journal of Economic Analysis and Policy | A | 6 | 12 |
| The BE Journal of Macroeconomics | A | 6 | 8 |
| The BE Journal of Theoretical Economics | A | 6 | 6 |
| Scandinavian Journal of Information Systems | A | 8 | 5 |

Asia-Pacific Journal of Innovation in Hospitality and Tourism is 91 people: Editor-in-Chief 1, Co-Editor 1, Associate Editor 2, Managing Editor 1, Technical Editor 1, Advisory Board 17, Editorial Review Board 68. Source `https://fslmjournals.taylors.edu.my/apjiht/`. ROR ids already on these boards are attached on 68 of 91 (67 high, 1 medium). The medium hit is Vineetha Sinha, National University of Singapore, an id already on these boards.

The three BE journals list names only on the De Gruyter journal header, so the affiliation stays blank (26 people). Sources are `https://www.degruyter.com/journal/key/bejeap/html`, `https://www.degruyter.com/journal/key/bejm/html`, and `https://www.degruyter.com/journal/key/bejte/html`. No ROR was attached.

Scandinavian Journal of Information Systems lists a country and no organization: Sweden, Denmark, Finland, Norway, Denmark. Source `https://aisel.aisnet.org/sjis/editorialboard.html`. Those five affiliations stay off the Institutions page. No ROR was attached.

The new rows contain no email address, phone number, or photo.

## Files

| File | Rows | Empty `editor_name` | `raw_affiliation` | `ror_id` | `faculty_profile_url` | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,178 | 2 | 23,806 (94.6%) | 23,600 | 12,523 (49.7%) | 67 |
| `editors_abdc_a_current.csv` | 45,368 | 1 | 42,781 (94.3%) | 41,935 | 6,237 (13.7%) | 50 |
| `editors_abdc_b_current.csv` | 42,139 | 0 | 39,775 (94.4%) | 38,720 | 3,509 (8.3%) | 21 |
| `editors_abdc_c_current.csv` | 26,809 | 11 | 23,936 (89.3%) | 23,069 | 1,379 (5.1%) | 4 |

`ror_id` was 23,600 / 41,935 / 38,720 / 23,001. The C increase is 68 ids already on these boards. A, A*, and B `ror_id` counts stay. Empty `editor_name` on A was 2. The row this publish removed was a blank Scandinavian Journal of Information Systems chrome row. One empty name remains, on AIS Transactions on Human-Computer Interaction.

## Holds carried forward

`11KBW` stays on two Public Law rows (Aileen McColgan KC, Chris Knight KC), with no ROR id. Kai Hockerts stays INSEAD, `https://ror.org/05ynf4333`. Sam Kirshner stays UNSW Sydney, `https://ror.org/03r8z3t63`.

The same two medium hits withheld on the FT50 file stay withheld on the ABDC copy of that seat.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School. Country is Spain.

One A* row whose name is `___` stays off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. Directory appointments are 158,747, were 158,624. Editors are 110,424, were 110,326. Journals stay 2,853. ABDC chips are A* 25,172 (219 journals), A 45,356 (626), B 42,124 (836), and C 26,797 (732). Countries stay 175. Institutions are 10,824 rows (8,662 with a ROR id), were 10,782 (8,662). 12,162 appointments have no institution. 633 country-only appointments, 3 bracket-only appointments, and 10 street, PO Box, or postal-code appointments stay off that page.
