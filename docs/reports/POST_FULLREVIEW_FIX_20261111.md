# Post-full-review fix — editors_post_fullreview_fix_20261111

Published 2026-11-11 (Asia/Taipei). The Collector freeze is applied on top of `editors_full_review_resolved_fix_20261111` (main `182ad663`, PR #54).

## Why

The re-review of the PR #54 Institutions list (11,330 names) left 982 residual rows. The Collector froze the approved part of those rows together with the user's answers (a)–(c): inactive ROR records, remaining near-duplicates, missing RORs, wrong or missing countries, and non-institution strings.

## What changed

The Directory took the freeze's `POST_FULLREVIEW_directory_diff_20261111.csv`, keyed on `file` + `editor_row_key`: 4,593 cells, 0 old-value mismatches, 0 missing keys. `ror_notes` comes from the freeze on 9 rows.

| Residual class | Applied |
|---|---|
| WRONG_ROR | 5/5. UniSA and Adelaide → Adelaide University `028g18b61`; TEI Piraeus → University of West Attica `00r2r5k05`; UPMC → Sorbonne Université `02en5vm52`; Rennes 1 → Université de Rennes `015m7wh34`. Each old record is inactive and names its successor. |
| NEAR_DUPLICATE | 101/138. Not applied: MPI institutes, CNRS labs, IIIT Raichur, Monash China, the non-Latin names and the two-organisation strings. The Rotterdam cycle is applied one way only. |
| MISSING_ROR | 298/306 (269 new RORs, all active in the API) |
| WRONG_COUNTRY | 7 in full, 5 partly. Multi-office organisations keep the printed office country. |
| NON_INSTITUTION | 18/51 (9 Marks DROPs; the printed text stays in `ror_notes`) |
| MISSING_COUNTRY | 11 (only where the printed text or ROR gives a country) |
| Answers | (b) 38 RENAMEs; (c) Mercer → `04bk7v425`, CTU Prague → `03kqpb082`, CY Cergy → `043htjv09`; (a) FT50 slim #4634 printed `Xi'an Jiaotong University, China` (`017zhmm22`) |

Rows changed: A* 68, A 263, B 288, C 283, ajg1 114, ajg2 41, prio43 22, FT50 19 with_ror / 12 slim. Row counts are unchanged (ajg1 12,316, ajg2 5,462, FT50 10,047). The long table `data/editors/releases/editors_post_fullreview_fix_20261111/editor_affiliations.csv.gz` keeps the published 181,449 parts, with 1,081 parts changed. Pilot files are not published. `CITATION.cff` is unchanged.

## Directory

| | PR #54 (live) | This freeze |
|---|---:|---:|
| Institutions | 11,330 | 11,213 |
| With ROR id | 6,396 | 6,692 |
| Countries | 167 | 169 (Guam, New Caledonia) |
| Shared display names | 46 | 44 (Mercer, CTU and CY gone; CIMMYT Kenya/Mexico new) |
| Appointments without institution | 13,404 | 13,413 |

The shared-name guard in `scripts/build_site.py` is now 44. Appointments 162,575, editors 112,719, journals 2,853 (unchanged).

## Checks

- Protected names (11KBW, UNSW, the INSEAD campuses, 1 Decembrie 1918, Bank of England) are unchanged.
- No near-miss pair is merged (Bolton/Boston, IIT/Indiana, Queen's Belfast/Canada, Tokyo Tech/Science Tokyo, Petru Maior/Palade, Aachen clinic/RWTH).
- `site/data` and the pinned files contain 0 emails and no phone numbers.

Known follow-ups for the Collector:
- 3 RORs on wrong canonicals: Junior Achievement for Guangxi University; Union Hospital for Qianfoshan Hospital, Jinan; The LEGO Foundation for the Lego Group.
- RORs on former employers (Nielsen, GM, SEARCA).
- Countries: Rutgers–New Brunswick printed "Canada"; Indecon Dublin set to United Kingdom; Macao IFT set to China; CINVESTAV prio43#1194 blank.
- UniSA editors now display as Adelaide University, the ROR successor.
