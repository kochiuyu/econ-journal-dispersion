# editors_single_editor_20261029

Fuller boards for journals that had one editor row, plus the five browser-board replacements carried in this freeze. Frozen 2026-10-29 23:18 Asia/Taipei. This supersedes `editors_browser_boards_20261029`. A* row count is unchanged. Empty `editor_name` is 2 on A*, 1 on A, 0 on B, and 11 on C. No D4 or D5 pass is in this freeze.

`editor_name` is the name the directory shows. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

Every current editor CSV ends with `board_urls` and `board_url_count`. `board_urls` is a pipe-separated list of public board-page URLs, filled only when that board spans more than one page. `board_url_count` is the number of those URLs. Both cells are blank on every other row. `source_url` stays the primary board link. `scripts/build_site.py` selects columns by name and does not write `board_urls` to the site.

This publish replaces the rows of fourteen journals on these files. Other rows stay as published in `editors_apjiht_board_fix_20261029`, including the eight-journal board fix and the place-suffix and country corrections from earlier freezes. The collector CSV also rewrote institution strings on other journals, including `Italian Cultural Institute` on Tokyo mastheads. Those rows stay as published. A rematch on a new row uses a ROR id already on these boards, or one exact crosswalk hit. No ROR id was invented.

## Boards

Heading and navigation rows on three journals are replaced with the people on those boards. Eleven journals that had a single editor row now have the fuller board. Defense Transportation Journal stays one row: the junk line is replaced by the named managing editor. Raw affiliation is the masthead text.

| Journal | Rating | Was | Now |
|---|---|---:|---:|
| IEEE Transactions on Intelligent Transportation Systems | A | 1 | 299 |
| Academy of Management Perspectives | A | 1 | 112 |
| Naval Research Logistics | B | 8 | 119 |
| Journal of Personnel Psychology | B | 1 | 65 |
| New Directions for Evaluation | B | 4 | 35 |
| Journal of Eastern Asia Society for Transportation Studies | C | 1 | 90 |
| Acta Turistica | C | 1 | 51 |
| Management: Journal of Contemporary Management Issues | C | 1 | 51 |
| Journal of International Technology and Information Management | C | 1 | 34 |
| Economic Affairs | C | 4 | 32 |
| Agricultural Economics Review | C | 1 | 20 |
| Applied Econometrics | C | 1 | 19 |
| Electronic Journal of Knowledge Management | C | 1 | 11 |
| Defense Transportation Journal | C | 1 | 1 |

IEEE Transactions on Intelligent Transportation Systems is 299 people. The `journal` cell stays blank, as on the old row; the id is `ieee_transactions_intelligent_transportation_systems`. Source `https://ieee-itss.org/pub/t-its/board/`. `board_urls` is `https://ieee-itss.org/pub/t-its/|https://ieee-itss.org/pub/t-its/board/` (`board_url_count` 2) on all 299 rows. ROR ids are attached on 107 of 299 (102 high, 5 medium). One of those ids was not already on the published panels: Sachin Kumar, Galgotias College of Engineering & Technology, `https://ror.org/04a85ht85`, an exact crosswalk hit. Xingwang Li stays on the masthead string Henan Polytechnic University, with no ROR id.

Academy of Management Perspectives is 112 people. Source `https://www.aom.org/publications/journals/perspectives/perspectives-editorial-team/`. ROR ids already on these boards are attached on 24 of 112 (23 high, 1 medium).

Naval Research Logistics is 119 people. The department stays in the role text. Source `https://onlinelibrary.wiley.com/page/journal/15206750/homepage/editorialboard.html`. ROR ids already on these boards are attached on 94 of 119.

Journal of Personnel Psychology is 65 people. Source `https://www.hogrefe.com/us/journal/journal-of-personnel-psychology`. ROR ids already on these boards are attached on 49 of 65, all high.

New Directions for Evaluation is 35 people. Source `https://onlinelibrary.wiley.com/page/journal/1534875x/homepage/editorialboard.html`. ROR ids already on these boards are attached on 21 of 35.

Journal of the Eastern Asia Society for Transportation Studies is 90 people. Source `https://www.jstage.jst.go.jp/browse/easts/_pubinfo/-char/en`. The old row was the association address. ROR ids already on these boards are attached on 60 of 90 (59 high, 1 medium).

Acta Turistica is 51 people. `board_urls` lists the Srce editorial team and the faculty editorial board (`board_url_count` 2). ROR ids already on these boards are attached on 37 of 51, all high.

Management: Journal of Contemporary Management Issues is 51 people. `board_urls` lists the Srce editorial team and the about page (`board_url_count` 2). No ROR id is attached.

Journal of International Technology and Information Management is 34 people. Source `https://iima.org/wp/jitim/`. ROR ids already on these boards are attached on 19 of 34, all high.

Economic Affairs is 32 people, including four Previous Editors with `is_current` false and a blank affiliation. Source `https://onlinelibrary.wiley.com/page/journal/14680270/homepage/editorialboard.html`. ROR ids already on these boards are attached on 11 of 32, all high.

Agricultural Economics Review is 20 people. The original Antonios REZITIS row stays Managing Editor. The page's Antony Rezitis spelling is not a second row. One further ROR id already on these boards is attached.

Applied Econometrics is 19 people. The original editor row stays, including its low-confidence ROR id. The new rows add no ROR id.

Electronic Journal of Knowledge Management is 11 people. The old row was the `One moment, please...` interstitial. Reviewers are not on this board. No ROR id is attached.

Defense Transportation Journal stays one row. Barbara Parus, Managing Editor, replaces the interstitial. No ROR id is attached.

The new rows contain no email address, phone number, or photo.

## Files

| File | Rows | Empty `editor_name` | `raw_affiliation` | `ror_id` | `faculty_profile_url` | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,178 | 2 | 23,806 (94.6%) | 23,600 | 12,523 (49.7%) | 67 |
| `editors_abdc_a_current.csv` | 45,777 | 1 | 43,060 (94.1%) | 42,065 | 6,237 (13.6%) | 50 |
| `editors_abdc_b_current.csv` | 42,345 | 0 | 39,985 (94.4%) | 38,876 | 3,509 (8.3%) | 21 |
| `editors_abdc_c_current.csv` | 27,106 | 11 | 24,206 (89.3%) | 23,189 | 1,379 (5.1%) | 4 |

`ror_id` was 23,600 / 41,935 / 38,720 / 23,069. The increases are A 130, B 156, and C 120. All but one of those ids were already on these boards. The exception is `https://ror.org/04a85ht85`. A* `ror_id` stays 23,600. Empty `editor_name` stays 2 / 1 / 0 / 11. Faculty URL counts stay A* 12,523, A 6,237, B 3,509, and C 1,379. A faculty URL with no `ror_id` stays 67 on A*, 50 on A, 21 on B, and 4 on C.

## Holds carried forward

`11KBW` stays on two Public Law rows (Aileen McColgan KC, Chris Knight KC), with no ROR id. Kai Hockerts stays INSEAD, `https://ror.org/05ynf4333`. Sam Kirshner stays UNSW Sydney, `https://ror.org/03r8z3t63`.

The same two medium hits withheld on the FT50 file stay withheld on the ABDC copy of that seat.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School. Country is Spain.

One A* row whose name is `___` stays off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. Directory appointments are 159,961, were 158,747. Editors are 111,154, were 110,424. Journals stay 2,853. ABDC chips are A* 25,172 (219 journals), A 45,765 (626), B 42,330 (836), and C 27,094 (732). Countries stay 175. Institutions are 11,276 rows (8,663 with a ROR id), were 10,824 (8,662). 12,309 appointments have no institution. 641 country-only appointments, were 633, plus 3 bracket-only appointments and 10 street, PO Box, or postal-code appointments, stay off that page.
