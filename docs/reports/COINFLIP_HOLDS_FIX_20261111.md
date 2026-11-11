# Coin-flip hold placements — editors_coinflip_holds_fix_20261111

Published 2026-11-11 (Asia/Taipei). The Collector freeze is applied on top of `editors_nielsen_searca_drop_20261111` (main `83f6a1a7`, PR #58).

## Why

The remaining Institution coin-flip holds — 199 residual shared-name / generic-name holds, plus the four open-item holds (Pacífico, Naples, Concordia, and the UT System) — were left as printed after PR #58. The user approved per-editor campus placements from `/workspace/institutions_coinflip_holds_20261111.csv` (187 rows; 158 applied, 29 already at the official campus name and ROR).

## What changed

The Directory took `COINFLIP_HOLDS_directory_diff_20261111.csv`, keyed on `file` + `editor_row_key`: 421 cells, 0 old-value mismatches, 0 missing keys. No `raw_affiliation` edits. The long table updates `ror_id` / `ror_name` on 68 parts, `ror_country` on 17 and `is_panel_ror` on 48.

| Group | Applied |
|---|---|
| Illinois | Mostly Urbana-Champaign `047426m28`. Linda Hagen and Thomas Lee stay / move to Chicago `02mpq6x41`. |
| Madison University | James Madison University `028pmsz77` (Parks-Leduc). |
| University of New Zealand | Massey University `052czxv31` (Stuart Carr; defunct umbrella renamed). |
| American University, UAE | American University in the Emirates `056c6h780` (Haddad, Mateev; printed 2010s campus). |
| Naples / Napoli | University of Naples Federico II `05290cv24` (Severino, Rippa, Zollo, Pavone). |
| Pacífico | Universidad del Pacífico, Lima `05mmg7t28` (Bravo, Talavera, Libaque-Saenz). |
| Concordia | Bruce Hanson → Concordia University Irvine `0028kf729` (new ROR, API-verified). Lawrence Kryzanowski (`Concordia U., CA`) → Concordia University, Montreal `0420zvk78`. Other Concordia rows already at Montreal are unchanged. |
| Texas system | 20 rows that still carried the system ROR `01gek1696` moved to the evidenced campus: Austin `00hj54h04`, Dallas `049emcs32`, El Paso `04d5vba33`, or Tyler `01azfw069`. Wei-Na Lee (`The University of Texas, United States`) → Austin. |
| Other confirmed campuses | UNC Chapel Hill, UW–Madison, UMass Amherst, IIT (Delhi / Kharagpur / Kanpur / Madras / Bombay), IIM (Udaipur / Bangalore / Lucknow), VNU Hanoi, HSE, Paris-Saclay (Hautbois only), University of Technology Jamaica, Newcastle UK / Newcastle Australia. |
| Left as printed | Unplaced editors, genuine two-place strings, NIT Hamirpur (not in the file; ROR `01nc8zs04` is active with country Bangladesh), Saint Mary's (already Halifax `010zh7098`), Diamond Leadership Institute, and the Nielsen/SEARCA dropped rows. |

Rows changed: A* 40, A 34, B 32, C 13, FT50 30 with_ror / 1 slim, ajg1 6, ajg2 2, prio43 0. Row counts are unchanged (ajg1 12,316, ajg2 5,462, FT50 10,047). The long table `data/editors/releases/editors_coinflip_holds_fix_20261111/editor_affiliations.csv.gz` keeps the published 181,449 parts, with 68 parts changed. Pilot files are not published. `CITATION.cff` is unchanged.

## Directory

| | PR #58 (live) | This freeze |
|---|---:|---:|
| Institutions | 11,184 | 11,175 |
| With ROR id | 6,696 | 6,698 |
| Countries | 169 | 169 |
| Shared display names | 43 | 43 |
| Appointments without institution | 13,415 | 13,415 |

The shared-name guard in `scripts/build_site.py` stays 43. Institutions fell by 9 as generic names merged into confirmed campus entries. With-ROR rose by 2, including the new Irvine ROR.

## Checks

- Protected names (11KBW, UNSW Sydney, the INSEAD campuses, 1 Decembrie 1918, Bank of England) are unchanged. No near-miss pair is merged (Bolton/Boston, IIT/Indiana, Queen's Belfast/Canada, Tokyo Institute of Technology/Institute of Science Tokyo, Petru Maior/George Emil Palade, Universitätsklinikum Aachen/RWTH).
- NIT Hamirpur was not applied. Saint Mary's Halifax remains on `010zh7098`.
- Pacífico panels carry canonical `Universidad del Pacífico` and ROR `05mmg7t28` / Peru. The Institutions list displays the ROR name `University of the Pacific` (Peru), distinct from the US Stockton row of the same display name (already one of the 43 shared names).
- `site/data` and the pinned files contain 0 emails and no phone numbers.
