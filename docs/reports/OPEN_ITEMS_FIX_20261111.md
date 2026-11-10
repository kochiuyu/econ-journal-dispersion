# Collector open items — editors_open_items_fix_20261111

Published 2026-11-11 (Asia/Taipei). The Collector freeze is applied on top of `editors_post_fullreview_fix_20261111` (main `9618a616`, PR #55).

## Why

PR #55 left open items: bio and multi-organisation strings, unmerged near-duplicates, low-confidence ROR names, printed-vs-ROR country conflicts, undropped rows, a CEIBS profile URL on the wrong X. Zhao, and the re-check finds (wrong RORs on wrong canonicals, wrong countries). The user approved the recommendations file `collector_open_items_20261111.csv`, and the Collector froze them.

## What changed

The Directory took `OPEN_ITEMS_directory_diff_20261111.csv`, keyed on `file` + `editor_row_key`: 306 cells, 0 old-value mismatches, 0 missing keys. Fields changed: `canonical_name` 58, `ror_id` / `ror_name` 46, `lat` / `lon` 41, `ror_country` 38, `continent` 32, and `faculty_profile_url` / `faculty_person_key` 2 (FT50 #4634). There are no `raw_affiliation` edits.

| Item | Applied |
|---|---|
| Bio / multi-org (24) | 15 retargets (23 rows), e.g. Cambridge `013meh722`, Asia School of Business `037hqgd69`, CIDE `014zxe029`, CSSSC `024rfjv05`, Tilburg `04b8v1s79`, Tongji `03rc6as71`, Woxsen `0305fyb87`. Allens is set to Australia. The other 7 stay as printed. |
| Near-duplicates (37) | RSM folded one way into "Rotterdam School of Management, Erasmus University"; MPI comma variant; FLACSO México `02wdjwg88`; HEC Liège → ULiège; MSU; Assumption University `039k72y49`; CESS `04ch3q361`; 5 Rutgers rows → `05vt9qd57`; Lones Smith → UW–Madison. Country fills on kept rows. Holds and the kept-distinct rows (MPI, CNRS, IIIT Raichur, Monash China) are unchanged. |
| Low-confidence names | Nutraceutical → Better Being Co. `05bqa2z43`; University of Africa → Toru-Orua `052vhkx86`. SRH Berlin and Bank of the West keep no ROR. |
| Country conflicts | Niagara `05309tf52` with country Canada (Ontario campus); Emden/Leer `01bc76c69`; WUNU `047988g19`; Southwestern UFE `04ewct822` |
| Creative NZ / St. Catharine's | Creative Capital Foundation `021e5n641`; Brock `056am2717` |
| Undropped rows | #18771 → Dalhousie `01e6qks80`; #9281 → Nova Southeastern `042bbge36`; #18673 country Australia. #39063 not dropped (it names UNSW). |
| Re-check | Guangxi University `02c9qn167`, QianFoShan Hospital `03wnrsb51`, Lego (Denmark) `04vx9dd09`, CIMMYT HQ `03gvhpa76` for the Mexico row, Macao University of Tourism `00nx0vn86` (Macao), and the Indecon (Ireland), Rutgers–New Brunswick (US) and CINVESTAV (Mexico) countries |

Rows changed: A* 12, A 11, B 12, C 24, ajg1 7, ajg2 3, prio43 1, FT50 4 with_ror / 4 slim. Row counts are unchanged (ajg1 12,316, ajg2 5,462, FT50 10,047). The long table `data/editors/releases/editors_open_items_fix_20261111/editor_affiliations.csv.gz` keeps the published 181,449 parts, with 64 parts changed. Pilot files are not published. `CITATION.cff` is unchanged.

## Directory

| | PR #55 (live) | This freeze |
|---|---:|---:|
| Institutions | 11,213 | 11,185 |
| With ROR id | 6,692 | 6,697 |
| Countries | 169 | 169 |
| Shared display names | 44 | 43 (CIMMYT collapses) |
| Appointments without institution | 13,413 | 13,413 |

The shared-name guard in `scripts/build_site.py` is now 43.

## Checks

- Protected names are unchanged. UNSW Sydney gains one appointment (the "Chapman" row), and its display name and ROR are unchanged.
- No near-miss pair is merged.
- 0 emails or phones.

Left open:
- abdc_b#39063 (Gerry Bates).
- Former-employer RORs: Nielsen, GM, SEARCA.
- abdc_b#16107 (Shenhar, "Rutgers University (Ret.)"), which was moved to Rutgers with the other split rows.
- `faculty_match_method` / `faculty_match_confidence` still read masthead_href/high on the two #4634 rows.
