# School and faculty unit rematches — editors_school_unit_rematch_20261111

Published 2026-11-11 (Asia/Taipei). The Collector freeze is applied on top of `editors_coinflip_holds_fix_20261111` (PR #59). It is a keyed, user-approved rematch of unmatched school, faculty, and center mastheads to the parent university when ROR has no record for that unit. Units that have their own ROR stay as their own institution. `raw_affiliation` is left as the printed masthead. No ROR id is invented.

599 of 606 file rows were applied, plus 50 same-raw `editors_ft50_current_with_ror` twins. All 94 target RORs were re-checked on the ROR API and were already on the published current panels. No new ROR.

Former-name rematches: Cass/Bayes 31/31 → City St George's, University of London `047ybhc09`; Instituto de Empresa / IE Business School 30/30 → IE University `02jjdwm75`. Short-name merges into a school that already has its own ROR: EADA 1/1 → `033qfx261`; EM Strasbourg 3/3 → `04q0nd296`; unmatched IMD Lausanne 4/4 → `04mv5gg87`.

Seven campus-conflict rows were left as printed, with the ROR left blank: four Nottingham University Business School China/Ningbo/Zhejiang rows the file had sent to UK Nottingham `01ee9ar58` (`editors_abdc_c_current#18543`, `#803`; `editors_abdc_a_star_current#20062`; `editors_abdc_b_current#3138`), and three Newcastle Business School Australia rows the file had sent to Northumbria UK (`editors_abdc_b_current#18450`, `editors_abdc_c_current#27171`, `editors_abdc_a_current#24283`). Those can be rematched in a follow-up to University of Nottingham Ningbo China `03y4dt428` and to the University of Newcastle Australia, if approved. Five other NUBS China rows already targeted Ningbo and were applied. The two UK NUBS rows and the five UK Newcastle/Northumbria rows were applied.

Held rows were not in the file and were left as printed, including Henley Business School Africa; IMD, Singapore; Middlesex University Dubai; Nova Business School Africa (Ghana); Peking University HSBC Business School listed as UK; Rutgers–Camden; and the named two-place rows. Middlesex Mauritius was not on the current panels.

Rows changed: A* 133, A 194, B 133, C 91, FT50 52 with_ror / 51 slim, ajg1 44, ajg2 13, prio43 1. Row counts are unchanged (ajg1 12,316, ajg2 5,462, FT50 10,047). The long table `data/editors/releases/editors_school_unit_rematch_20261111/editor_affiliations.csv.gz` keeps the published 181,449 parts, with 646 parts changed (`ror_id` / `ror_name` / `is_panel_ror` on 646, `ror_country` on 87; no `raw_aff_part` edits). The earlier web e-mail-scrub note is kept on B #13. Pilot files are not published. `CITATION.cff` is unchanged.

Directory: Institutions 11,078 (was 11,175), 6,698 with a ROR id (unchanged; distinct 6,698). Countries 169 (unchanged). 13,415 appointments have no institution (unchanged). Shared display names 43 (unchanged; the build guard stays 43). Appointments 162,575, editors 112,719, journals 2,853 (unchanged).
