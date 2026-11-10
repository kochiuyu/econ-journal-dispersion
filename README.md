# econ-journal-dispersion

Public research data for **Geographic Dispersion** work on economics (and related) journals.

**Repository:** https://github.com/kochiuyu/econ-journal-dispersion

**Editor directory:** https://kochiuyu.github.io/econ-journal-dispersion/

## What this repo is

Analysis-friendly **catalogs + release panels** only. Use the files under `data/*/releases/` for papers and coauthor analysis. Scrapes, HTML caches, RePEc dumps, and collector scripts stay in separate workspaces and are **not** versioned here.

## Journal universes

| Catalog | Path | Role |
|---------|------|------|
| **core49** | `journals/catalog_core49.csv` | Geographic Dispersion core economics journals |
| **FT50** | `journals/catalog_ft50.csv` | Financial Times Research rank journals |
| **ABDC** | `journals/catalog_abdc_{a_star,a,b,c}.csv` | 2025 ABDC Journal Quality List by rating |
| **Top 5** | `journals/catalog_top5.csv` | AER, Econometrica, JPE, QJE, and ReStud. Subset tag on the FT50 current release |
| **UTD24** | `journals/catalog_utd24.csv` | UT Dallas Naveen Jindal Top 24. Twenty-three journals tagged from the FT50 freeze; INFORMS Journal on Computing tagged from the ABDC A freeze |
| **ABS/AJG** | `journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/` | CABS Academic Journal Guide grades for 2010, 2015, 2018, 2021, and 2024, via the Editor-Collector freeze. Ratings, not editor boards. See `journals/rankings/STATUS.md` |
| **CNRS** | `journals/rankings/cnrs/releases/rankings_cnrs_20261024/` | Section 37 categories for 2011–2015 and 2017–2020. Ratings 1, 1e, 1g, 1eg, 2, 3, 4, plus domain |
| **Handelsblatt/VWL** | `journals/rankings/handelsblatt_vwl/releases/rankings_handelsblatt_vwl_20261024/` | Forschungsmonitoring weights for 1998–2020, plus the 2015 Handelsblatt list. Continuous weight, letter class when present |
| **Tilburg** | `journals/rankings/tilburg/releases/rankings_tilburg_20261025/` | TISEM top journal list. Tiers Top-core, Top, and Very good. Rankings page only |
| **FNEGE** | `journals/rankings/fnege/releases/rankings_fnege_20261025/` | FNEGE Journal Quality List grades for 2019, 2022, and 2025. Rankings page only |
| **ERIM** | `journals/rankings/erim/releases/rankings_erim_20261025/` | ERIM Journals List Core 2024–2028. Classes as published in the Core file. Rankings page only |
| **Stern** | `journals/rankings/stern/releases/rankings_stern_20261025/` | NYU Stern top-tier journals by department, 2020 and 2021 (TOpS). Accounting, Economics, Finance, Management, Marketing, and TOpS. Rankings page only |
| **Shanghai** | `journals/rankings/shanghai/releases/rankings_shanghai_20261025/` | ShanghaiRanking top journals for 2024 and 2026. Economics, Business Administration, Finance, and Management. Rankings page only |
| **SHUFE** | `journals/rankings/shufe/releases/rankings_shufe_20261025/` | SUFE Tenure-Track Journal List. Tiers Top Tier, First Tier, Second Tier, and Third Tier. No edition year on the source page. Rankings page only |

Prefer joining on stable keys (`journal_slug` / `journal_id`, `year`, `doi`) — see `docs/README.md`.

## Data layout

```
data/
  editors/
    releases/editors_weird_inst_fix_20261110/   # long table (editor_affiliations.csv.gz) + change log for the current freeze
    core49/releases/editors_backfill_scale_ror_20261031/   # pinned multi-year core49 backfill (not read by the site)
    ft50/releases/current/
    abdc/releases/current/
    abs_ajg_gap/releases/current/   # AJG journals not already in the FT50/ABDC board freezes
  authors/           # STATUS only — stream still in progress (no 1GB caches here)
  affiliations/
    releases/canonical/   # TOC-first articles / affiliations / issues
```

**Rule:** analyze from `releases/` only. Do not treat collector folders or `STATUS.md` progress notes as frozen paper inputs until a release is pinned.

Current editor panels are freeze **`editors_weird_inst_fix_20261110`** (published 2026-11-10). It supersedes `editors_country_misprint_fix_20261110` for the Directory current panels. It is a keyed, user-approved clean-up of weird Institution names on top of `editors_country_misprint_fix_20261110` (PR #53), from the non-REVIEW rows of the Institution audit: DROP 178 Institutions (391 publish rows; place-only, generic-role and credential names such as `Maryland`, `Independent Researcher, Vermont`, `Associate Professor`) plus 5 country-only fallbacks (`Greece and UK`, `Italy & UK`, `Finland and Tanzania`, `SE, UK`, the Solicitor string); STRIP 594 (632 rows; role prefixes, addresses, postcodes, URLs, punctuation and trailing state codes cut, e.g. `Harvard Business School, Cambridge, MA` → `Harvard Business School`); SET_COUNTRY 122 (137 rows, from a trailing state or code); REMATCH 186 (249 rows, to an existing panel twin ROR); and the University of Georgia fix (US rows on the Tbilisi ROR `02bjhwk41` → `00te3t702` / United States). DROP follows the Marks mechanism: `canonical_name`, `raw_affiliation` and `ror_id` are blanked, the printed text is kept in `ror_notes` (long table: `raw_aff_part` blanked, trace in `ror_match_note`); country stays. 120 rows whose printed raw still names an organisation (e.g. `Sydney Law School`, `Tokyo Institute of Technology`) are not dropped and are listed for a later restore. The audit's REVIEW names are untouched; no ROR id is invented. Institutions 14,672 (was 15,160), 6,387 with a ROR id (unchanged). Countries 162 (unchanged). 12,460 appointments have no institution (was 12,068). Shared display names stay 69. Before it, `editors_country_misprint_fix_20261110` superseded `editors_trailing_country_fix_20261110` for the Directory current panels. It is a keyed, user-approved fix on top of `editors_trailing_country_fix_20261110` (PR #53): 30 publish rows get the real country for 27 Institutions whose printed country was wrong (e.g. ESADE Business School → Spain, TU Berlin → Germany, Queens University Belfast → United Kingdom); Imperial College of London (C #17649) is rematched to the existing panel ROR `041kmwe10` Imperial College London. 11 fragment rows (the 11 held back in PR #53) get a clean `canonical_name` or a blank one: the Court of Appeal / Supreme Court rows become `Court of Appeal of England and Wales` / `Supreme Court of the United Kingdom` (UK), the two Independent Scholar rows become `Independent Scholar`, and `Greece and`, `Italy &`, `Finland and`, `SE` and the Solicitor row are blanked, so the Directory falls back to the printed text (e.g. `Greece and UK`). `University of the North, Barranquilla, .` loses its trailing `, .` and merges with its twin. The printed `raw_affiliation` is unchanged; no ROR id is invented. Institutions 15,160 (was 15,166); 6,387 with ROR and 162 countries unchanged. Before it, `editors_trailing_country_fix_20261110` superseded `editors_raw_aff_part_no_fix_20261110`. It is a keyed, user-approved fix for Institution names that ended in a printed country. 6,036 publish-panel rows get the country stripped from `canonical_name` and `ror_country` / `continent` set from it (137 Institutions are rematched to an existing panel twin, reusing that twin's ROR id where it has one; no ROR id is invented). The printed `raw_affiliation` is unchanged. The audit's REVIEW and KEEP names are untouched, and 11 rows whose stripped name would end in a dangling `and` / `&` (e.g. `Court of Appeal of England and`) are held back.

Before that, `editors_raw_aff_part_no_fix_20261110` was a long-table-only fix: 9,695 affiliation parts in `editor_affiliations.csv.gz` whose `raw_aff_part` was exactly `no` (an `affiliation_imputed` flag that leaked into the text column on seats with a blank panel `raw_affiliation`) are blanked. The panel CSVs are unchanged.

Before that, `editors_edpacs_marks_country_fix_20261110` was a keyed, user-approved ABDC C follow-up on three EDPACS seats: Norman Marks' printed bio is blanked from `raw_affiliation` (and the long `raw_aff_part`), so it no longer shows as an Institution, with the original text kept in the notes; Aditya Birla Group is set to India / Asia and New York State Comptroller to United States / North America (still no ROR id); and eight EDPACS long-table parts with `raw_aff_part` `no` are blanked to match their blank panel text.

Before that, `editors_paren_num_leftover_fix_20261110` was a keyed fix for the parenthesis- and number-start Institutions left as REVIEW, applied with user approval:
- Nine EDPACS credential blurbs and the Hengeler Mueller role prefix become organisation-only names, with no ROR id.
- Norman Marks' bio is dropped from the cleaned name; his printed text is kept.
- GGSIPU Periyar is rematched to Guru Gobind Singh Indraprastha University `034q1za58`.
- Égert's numbered list is rematched to OECD `0438wbg98`.

Before that, `editors_tokyo_other_inst_fix_20261110` was a keyed ABDC-only fix that gives 34 seats whose canonical name was the bare `Tokyo` their printed Tokyo institution: 23 are rematched to that institution's ROR id and 11 Tokyo Institute of Technology seats keep a blank ROR. Fuhito Kojima's printed `Tokyo` stays unmatched. Before that, `editors_tokyo_gatech_fix_20261110` was a keyed panel-only fix: 27 University of Tokyo seats whose ROR the Directory guardrail had left blank are rematched to The University of Tokyo `057zh3y96`, and one Decision Sciences `Georgia Inst of Technology` seat is rematched to Georgia Institute of Technology `01zkghx44` (printed `raw_affiliation` kept). Before that, `editors_inst_punct_split_20261110` blanked punctuation-start junk and rematched high-confidence name splits. REVIEW and KEEP flags were excluded. There is no site filter. The core49 multi-year backfill **`editors_backfill_scale_ror_20261031`** stays pinned under `data/editors/core49/releases/`. Reports: `docs/reports/`.

Every current editor CSV keeps `board_urls` and `board_url_count` next to each other (added in `editors_single_editor_20261029`). From `editors_ror_consistency3b_20261101` they are followed by `board_status`, `tenure_start_year`, `tenure_end_year`, `snapshot_date`, `snapshot_source`, `board_year`, `editor_row_key`, `affiliation_count`, `ror_id_aff_rank`, `primary_aff_basis`, `former_flag`, and `other_ror_ids`; the slim `editors_ft50_current.csv` also gains `ror_id`, `ror_name`, `ror_country`, and `continent`. `board_urls` is a pipe-separated list of public board-page URLs (one URL is allowed on any journal; multi-page lists only on the journals listed in `docs/README.md`). `scripts/build_site.py` selects columns by name and does not write the board columns to the site. One row per affiliation part is in `data/editors/releases/editors_paren_num_leftover_fix_20261110/editor_affiliations.csv.gz` (gzipped because it is 63 MB uncompressed; md5 `30ce66981f2a457ab6e86485bc580f87`). See `docs/README.md`.

## Stream status (summary)

| Stream | State in this repo |
|--------|--------------------|
| Editors — FT50 | Current-board panels in `releases/current/` — freeze `editors_weird_inst_fix_20261110` (weird-name fix on 18 / 8 rows; `ror_id` 9,703 / 9,624; before it, `editors_country_misprint_fix_20261110`: FT50 files unchanged from `editors_trailing_country_fix_20261110`; trailing-country fix on 81 / 84 rows; 10,047 rows: two REStud institution-as-name rows stay out, three Top 5 seats stay so they match ABDC A*; empty `editor_name` is 1; `faculty_profile_url` on 8,375 rows; `raw_affiliation` on 9,941 in the ROR file the build reads; `ror_id` on 9,701, was 9,699). The slim file carries ROR columns too (`ror_id` on 9,622, was 9,620; `raw_affiliation` on 9,936) |
| Editors — ABDC A*/A/B/C | Current-board panels in `releases/current/` — freeze `editors_weird_inst_fix_20261110` (weird-name fix on A* 117, A 352, B 350, C 427 rows; `ror_id` 23,406 / 40,588 / 36,963 / 21,567; before it, country-misprint / fragment fix on A* 2, A 13, B 14, C 10 rows; C `ror_id` 21,552; before it, trailing-country fix on A* 273, A 1,096, B 1,682, C 1,728 rows; `ror_id` B 36,946, C 21,551; A* 25,596, A 45,889, B 42,558, C 27,719 rows; empty `editor_name` is 1 / 1 / 11 / 6; `faculty_profile_url` 12,522 / 6,236 / 3,509 / 1,379; `ror_id` 23,399 / 40,578 / 36,945 / 21,550, C was 21,549). The bare-`Tokyo` seats get their printed Tokyo institution (23 rematched, 11 Tokyo Institute of Technology with blank ROR); printed names are kept. The collector blanks a ROR id when the masthead text is ambiguous, so ROR coverage is lower than in `editors_browser_single_20261029`. `11KBW`, UNSW Sydney, and INSEAD (France `00ghzk478` and Singapore `05ynf4333` separate) stay; ESSEC is France `02dga6j42` |
| Editors — AJG gap | Current-board panels in `releases/current/` — freeze `editors_weird_inst_fix_20261110` (weird-name fix on prio43 22, ajg2 54, ajg1 81 rows; `ror_id` 2,547 / 4,750 / 8,708; before it, country-misprint fix on prio43 1, ajg1 2 rows; before it, trailing-country fix on prio43 52, ajg2 198, ajg1 842 rows; ajg1 `ror_id` 8,700; prio43 and ajg2 unchanged from `editors_tokyo_gatech_fix_20261110`; prio43 3,104, ajg2 5,462, ajg1 12,316 rows; `faculty_profile_url` prio43 82, ajg2 386, ajg1 615; empty `editor_name` is 3 / 0 / 15; `ror_id` 2,546 / 4,746 / 8,698; ajg1 was 8,697). The twelve ajg1 navigation rows (including Vincent Pan) and the two ajg2 Policy Design and Practice navigation rows stay out, as do the fourteen drop-quality chrome rows |
| Editors — core49 | Pinned release `releases/editors_backfill_scale_ror_20261031/` (15,446 rows, 39 journals, 301 journal-years). Not read by the site. See `data/editors/core49/STATUS.md` for coverage gaps |
| Affiliations (core49 TOC spine) | Canonical articles / affiliations / issues under `releases/canonical/` |
| Authors (core49) | **In progress** — see `data/authors/STATUS.md`; no analysis dump yet |

## Website

The site root is a short hub. The searchable directory of **current journal editors** is a separate page. Boards are the FT50 list, the ABDC A*, A, B, and C lists, and AJG-gap boards (journals in the 2024 Academic Journal Guide that are not already in those editor files). Top 5 and UTD24 are extra multi-select filters on the FT50 and ABDC boards. AJG chips are 2024 CABS grades on those boards: joined by catalog id on FT50 and ABDC rows, and taken from the gap panel (4*/4/3, then 2, then 1) on gap rows. The id join does not add a board. The full guide is larger than these boards and stays on Rankings. The directory also filters by institution (the row affiliation) and by ABDC field:

**https://kochiuyu.github.io/econ-journal-dispersion/**

**https://kochiuyu.github.io/econ-journal-dispersion/directory.html**

core49 is not included (it is an older ABDC A* subset, not a separate universe in this directory). Authors are out of scope.

`scripts/build_site.py` reads the current editor releases and writes `site/meta.json` plus `site/data/`. The hub fetches only `meta.json` (counts and per-list totals). The directory loads `site/data/shell.js`, then one file per list chip (`ft50.js`, `a_star.js`, `a.js`, `b.js`, `c.js`, `top5.js`, `utd24.js`, `ajg_4star.js`, `ajg_4.js`, `ajg_3.js`, `ajg_2.js`, `ajg_1.js`). A row is copied into every chip whose bit is set; the browser dedupes. The directory opens on FT50. Top 5 rows are already in that file. Other chips download when selected, or when a journal or institution link needs them. `?u=` names chips. `u=-` selects none. `?journal=` or `?aff=` with no `u` loads the chip set that contains that journal or affiliation. An old root URL with a directory query, or `#directory`, redirects to `directory.html`.

The directory is static HTML, CSS, and JS: a filterable table (name, role, journal, field, list, affiliation, country, continent), header counts, and a short note on the release. Institution is a typeahead over the lists loaded so far, not a menu of every affiliation. The name on the row is `editor_name`. FT50, ABDC A*/A/B/C, and AJG-gap are freeze `editors_weird_inst_fix_20261110` (2026-11-10), which supersedes `editors_country_misprint_fix_20261110` (itself superseding `editors_trailing_country_fix_20261110`, which superseded superseding `editors_raw_aff_part_no_fix_20261110`); the text below describes earlier freezes that are still in the history of these rows. Emails and phone numbers that the collector left in `source_note` cells were removed before publishing. Earlier: `editors_single_editor_20261029`. It supersedes `editors_browser_boards_20261029`. Heading and navigation rows are replaced with the people on those boards, and journals that had a single editor row now have the fuller board. Other rows stay as published in `editors_apjiht_board_fix_20261029`, including the eight-journal board fix, a place suffix stripped from an institution name, and a country mismatch corrected when the affiliation text names that country. Faculty URLs filled by the earlier URL freezes stay on rows this freeze did not replace. The previous spelling is `editor_name_raw` on the CSV when the name changed. The page does not invent a name. A row with an empty `editor_name` is not listed. Empty `editor_name` is 1 on FT50, 1 / 1 / 11 / 6 on ABDC A* / A / B / C, and 3 / 0 / 15 on the AJG-gap panels. The directory does not list those rows. A name links to `faculty_profile_url` when that cell is filled. On the FT50 current release, `faculty_profile_url` is filled on 8,375 of 10,047 rows (83.4%) in the ROR file the build reads. `raw_affiliation` is filled on 9,941 of 10,047 rows (99.0%). On the ABDC current release, `faculty_profile_url` is filled on 12,522 of 25,596 A* rows (48.9%), 6,236 of 45,889 A rows (13.6%), 3,509 of 42,558 B rows (8.2%), and 1,379 of 27,719 C rows (5.0%). On the AJG-gap files it is filled on 1,083 of 20,882 rows (5.2%). A blank affiliation is not an institution, and a bare country is not an institution. Rows that are still blank stay plain text, and the page does not substitute a faculty home page or an ORCID, OpenAlex, or RePEc id. Emails, phone numbers, and photos are not published. `site/data.js` is not written.

One row is one person in one role on one journal. The same person on two journals is two rows. Where that same appointment is in both the FT50 release and an ABDC rating, the build keeps a single row and tags it with both lists (for example FT50 and ABDC A*). The match key is the cleaned `editor_name`. If the FT50 row was cleaned and the ABDC copy of that seat still has the pre-clean spelling, the build still keeps one row and shows the FT50 name. A Top 5, UTD24, or AJG grade keeps that badge on the same row. Wording comes from `editors_ft50_current_with_ror.csv`; a blank affiliation or country is filled from the ABDC row. The same name and role with two different affiliations stays two rows. The full rule is at the top of `scripts/build_site.py`.

Top 5 is American Economic Review, Econometrica, Journal of Political Economy, Quarterly Journal of Economics, and Review of Economic Studies (`journals/catalog_top5.csv`). UTD24 is the official UT Dallas list (`journals/catalog_utd24.csv`): 23 journals already in the FT50 freeze, plus INFORMS Journal on Computing from `editors_abdc_a_current.csv`. Journal of Applied Psychology stays on FT50 only.

AJG list chips and row badges show the grade from the 2024 edition (`journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/abs_ajg_2024.csv`), the latest edition in that freeze: AJG 4*, AJG 4, AJG 3, AJG 2, or AJG 1. The label does not include the year. On FT50 and ABDC rows the join includes 2024 `journal_id_crosswalk.csv` ids, so a board that uses an ABDC id still matches when the freeze's primary id is a core49 slug. That edition has 1,823 journals. 1,378 map to a catalog id. About 1,356 of those sit on an FT50 or ABDC board and show a chip from the id join. The 445 unmatched titles have no catalog id, so that join does not tag them and does not add a board. Many ABDC board journals have no AJG grade (about 2,400 board journal ids, against about 1,356 with a hit). AJG-gap rows (`data/editors/abs_ajg_gap/releases/current/`, freeze `editors_paren_num_leftover_fix_20261110`, journals from `editors_abs_ajg_gap_20261025`) are extra boards for journals not already in those editor files. Their grade is the 2024 title rating, constrained to the file: `prio43` is 4*, 4, or 3 (this freeze is 4 and 3), `ajg2` is 2, and `ajg1` is 1. A gap row carries that grade only. African Affairs is 40 rows from the 2024-04-27 Wayback snapshot. `faculty_profile_url` is filled on 1,083 of 20,882 rows, so those names link and the rest stay plain text. The journal links to `source_url` when it is http(s). With those boards the directory shows a chip on 1,796 journals. 27 titles in the 2024 guide still have no board. ABDC chips stay A*, A, B, and C. Full AJG editions stay on Rankings.

The directory institution field suggests the affiliation on loaded rows (ROR name, otherwise the canonical or masthead affiliation). It uses the same `aff` query the Institutions page already opens. Field is ABDC `field_for`, the same subject string as the Journals page, with the leading code hidden in the menu.

The same boards are also grouped by journal and by institution:

**https://kochiuyu.github.io/econ-journal-dispersion/journals.html**

**https://kochiuyu.github.io/econ-journal-dispersion/institutions.html**

`scripts/build_site.py` writes `site/journals-data.js` (one row per journal: list badges, appointments, distinct editors, countries, ABDC field, board link) and `site/institutions-data.js` (one row per ROR id, or per affiliation name when ROR is missing). AJG-gap rows join that ROR key when `ror_id` is filled. The gap boards are freeze `editors_paren_num_leftover_fix_20261110`. A country suffix on the masthead collapses into the same institution. A row with an empty `editor_name` and a `ror_id` counts as an appointment there and does not count as an editor. Rows that are still unmatched stay one row per affiliation string, except a bare country or territory, a string fully enclosed in brackets, or a street, PO Box, or postal code with no organization name. With freeze `editors_paren_num_leftover_fix_20261110` Institutions are 15,435 rows (6,387 with a ROR id), were 15,438 (6,387). Grant Thornton, OECD, and Guru Gobind Singh Indraprastha University absorb their leftover rows. The only Institutions that still start with a parenthesis or a digit are 14 numbered organisations kept on purpose (1 Decembrie 1918 University, 11KBW, 39 Essex Chambers, and others) and Norman Marks' printed bio. That bio still shows through the printed-text fallback, because his cleaned name is blank and his printed text is kept. With `editors_tokyo_other_inst_fix_20261110` before it, the unmatched `Tokyo` (Japan) row falls from 35 appointments to 1 (Fuhito Kojima's printed `Tokyo`), and ten Tokyo institutions get their own row, six with ROR ids new to the published panels. Tokyo Institute of Technology is one unmatched row (15 appointments), separate from Institute of Science Tokyo `05dqf9946`. Before that, with `editors_tokyo_gatech_fix_20261110`, the unmatched `University of Tokyo` and `Georgia Inst of Technology` rows fold into their ROR rows, so The University of Tokyo is one row (`057zh3y96`). Shared display names stay 69. 12,066 appointments have no institution (unchanged). `editors_inst_punct_split_20261110` before it blanked punctuation-start junk and rematched high-confidence name splits (Institutions 15,612 → 15,434, shared display names 125 → 69). Directory countries stay 159. Directory totals stay 162,575 appointments, 112,718 editors, and 2,853 journals. `raw_affiliation` on the CSV is left as the masthead text. A journal name opens `directory.html?journal=`. An institution name opens `directory.html` with `?aff=` set to that affiliation and `?country=` when the row has a country. Those files, `site/meta.json`, and `site/data/` are generated and are not committed.

Journal grades for every ranking system are also a separate page. The directory’s AJG chips are the 2024 grades on the current FT50, ABDC, and AJG-gap boards:

**https://kochiuyu.github.io/econ-journal-dispersion/rankings.html**

`scripts/build_site.py` also runs `scripts/build_rankings.py`, which writes `site/rankings-data.js`. The Rankings page filters by ranking system, edition, rating, and field, and searches by journal title. Field is the ABS/AJG subject, the CNRS domain, the ABDC `field_for`, the FNEGE domain, the ERIM track, the TISEM very-good group, the Stern department, the Shanghai subject, or the FT50 subject area from the McMaster LibGuide (https://libguides.mcmaster.ca/ft-top50). A Stern memo heading is shown after the department when the row has one. Handelsblatt/VWL shows the published weight. FT50, UTD24, and Top 5 have no grades. UTD24, Top 5, and SHUFE have no field. Tilburg, FNEGE, ERIM, Stern, Shanghai, and SHUFE are Rankings lists only. They are not directory chips. Systems on the page:

| System | Rows | What the filter shows |
|--------|------|------------------------|
| ABS/AJG | 7,245 | Editions 2010, 2015, 2018, 2021, 2024, ratings 4* / 4 / 3 / 2 / 1 (2010 has no 4*), from freeze `rankings_abs_ajg_20261024` |
| CNRS | 7,361 | Editions 2011–2015 and 2017–2020, ratings 1 / 1e / 1g / 1eg / 2 / 3 / 4, with domain, from freeze `rankings_cnrs_20261024` |
| Handelsblatt/VWL | 42,478 | Editions 1998–2020, continuous weight and letter class A+–F when present, from freeze `rankings_handelsblatt_vwl_20261024` |
| FT50 | 50 | April 2026 membership list. No grades. Field is the McMaster LibGuide subject area |
| UTD24 | 24 | Membership list. No grades |
| Top 5 | 5 | Membership list. No grades |
| ABDC | 2,651 | 2025 list, ratings A* 219, A 630, B 861, C 941 |
| Tilburg | 179 | TISEM tiers Top-core / Top / Very good, from freeze `rankings_tilburg_20261025`. 164 matched (91.6%) |
| FNEGE | 2,044 | Editions 2019, 2022, and 2025, grades 1* / 1 / 2 / 3 / 4 (EM and NC kept when printed), from freeze `rankings_fnege_20261025`. 2025 has 891 journals, 733 matched (82.3%) |
| ERIM | 283 | Core 2024–2028 classes as published (STAR, M-STAR, P, EP*, PA, S, S (3=1), M), from freeze `rankings_erim_20261025`. 257 matched (90.8%) |
| Stern | 233 | NYU Stern departments Accounting, Economics, Finance, Management, Marketing, and TOpS, from freeze `rankings_stern_20261025`. 2020 has 176 journals (157 matched, 89.2%). 2021 is TOpS, 57 journals (31 matched, 54.4%). 188 of 233 rows are matched (80.7%) |
| Shanghai | 76 | Editions 2024 and 2026, binary Top, subjects Economics, Business Administration, Finance, and Management, from freeze `rankings_shanghai_20261025`. 2026 has 19 journals, all matched |
| SHUFE | 123 | SUFE Tenure-Track tiers Top Tier / First Tier / Second Tier / Third Tier (5 / 20 / 39 / 59), from freeze `rankings_shufe_20261025`. The source page has no edition year, so the selector is Current. 120 matched (97.6%) |

The directory AJG chips are the 2024 grades on current FT50, ABDC, and AJG-gap boards (AJG 4* through AJG 1). The full guide stays on this page, including titles that still have no board. FT50, UTD24, and Top 5 are not given grades on the Rankings page. The other ABS/AJG editions stay there as grades.

### Local build

```bash
python scripts/build_site.py
python -m http.server 8000 -d site
```

Open http://127.0.0.1:8000/ for the hub and http://127.0.0.1:8000/directory.html for the editor table. Styles and scripts use relative URLs, so this is the same tree GitHub Pages serves under `/econ-journal-dispersion/` rather than at the user-site root. Journals are at http://127.0.0.1:8000/journals.html , institutions at http://127.0.0.1:8000/institutions.html , and rankings at http://127.0.0.1:8000/rankings.html . `site/meta.json`, `site/data/`, `site/journals-data.js`, `site/institutions-data.js`, and `site/rankings-data.js` are generated and are not committed.

### Enable GitHub Pages

`.github/workflows/pages.yml` builds the site on every push to `main` and deploys it with GitHub Actions. Once, in the repository settings:

1. **Settings → Pages**
2. **Build and deployment → Source: GitHub Actions**

If Pages is still set to “Deploy from a branch”, switch it to GitHub Actions. Until that source is selected, the workflow can succeed without the site updating. No custom domain is required. The live URL is https://kochiuyu.github.io/econ-journal-dispersion/ .

## License / citation

Dataset intended as **CC-BY-4.0**. See `CITATION.cff`.

Underlying board lists and TOCs are public journal mastheads / publisher pages; enrichment (ROR, OpenAlex) follows each provider’s terms.
