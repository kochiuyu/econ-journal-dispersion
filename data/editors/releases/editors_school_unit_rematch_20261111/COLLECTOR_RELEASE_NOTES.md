# editors_school_unit_rematch_20261111 (built 2026-11-11 18:18, Asia/Taipei; UNPUBLISHED)

Base: `releases/editors_coinflip_holds_fix_20261111` (live via PR #59, 887b6a36).
Input: `/workspace/collector_school_units_20261111/school_unit_rematch_20261111.csv` (606 appointments, 505 editors, 94 targets) and README.md.
User-approved rule (2026-11-11), relayed by Econ-Journal-Web. Keyed on editor_row_key. No raw-text edits. Pilots byte-identical.
Script: `school_unit_rematch_20261111.py`.

The Institutions table follows ROR: a school, faculty or centre with its own ROR stays its own institution; unmatched mastheads rematch to the parent university. `raw_affiliation` is left as the printed masthead; `ror_id` / `ror_name` / `ror_country` (and the matching long-table part) and `canonical_name` (where the column exists) are set to the target.

All 94 target RORs were re-checked active in ROR API v2 on 2026-11-11; name and country fit in every case. All 94 were already on the published current panels. No new ROR was added.

## Applied 599 / 606 file rows (7 skipped)

Plus 50 same-raw `ft50_current_with_ror` twins synced (the file listed 51 `ft50_current` keys and no with_ror twins). 1 twin was already at the target: `editors_ft50_current_with_ror#5191` (Cambridge Judge Business School) already had University of Cambridge `013meh722`; the slim twin was updated.

### Former-name rematches and short-name merges (all applied)
- Cass Business School / Bayes Business School → City St George's, University of London `047ybhc09`: 31/31
- Instituto de Empresa / IE Business School → IE University `02jjdwm75`: 30/30
- EADA → EADA Business School `033qfx261`: 1/1 (own ROR kept)
- EM Strasbourg → EM Strasbourg Business School `04q0nd296`: 3/3 (own ROR kept)
- unmatched IMD Lausanne → International Institute for Management Development `04mv5gg87`: 4/4 (IMD Singapore was not in the file)

Also applied: KAIST 11, LUISS 8 (single-place only), NUBS China → University of Nottingham Ningbo China `03y4dt428` 5/5, Middlesex University London 3 (Dubai/Mauritius not in the file), Nanyang Singapore → NTU 3, Henley UK → University of Reading 1 (Henley Africa not in the file), Rutgers Newark / New Brunswick / Law / SMLR / Public Health → Rutgers `05vt9qd57` 11 (Camden not in the file), St. Mary's University, Texas `03fvnza37` 3.

Largest parent rematches include Harvard University `03vek6s52` 44, Erasmus University Rotterdam 29, Monash 24, Leeds 19, Imperial 18, Sydney 18, Turku 18, Columbia 16, Yale 16.

### Skipped 7 (campus conflict; left as printed, ROR left blank)
The file targeted UK Nottingham `01ee9ar58` or Northumbria `049e6bc10` for foreign-campus mastheads. The approved rule says a named campus rematches to that campus, not the home campus, and a blank ROR is better than a wrong one. These were not rewritten to Ningbo or University of Newcastle Australia.

- `editors_abdc_c_current#18543` Nottingham University Business School (NUBS), China
- `editors_abdc_a_star_current#20062` Nottingham University Business School in China, China
- `editors_abdc_c_current#803` Nottingham University Business School, Ningbo, China
- `editors_abdc_b_current#3138` Nottingham University Business School, Zhejiang, China
- `editors_abdc_b_current#18450`, `#27171` (c), `editors_abdc_a_current#24283` Newcastle Business School Australia (panel canonical already "University of Newcastle", country Australia)

The two UK NUBS rows (Nottingham, United Kingdom / UK) and the five UK Newcastle / Northumbria rows were applied.

## Held rows left as printed
None of the held strings were in the CSV. A scan of the base panels found 47 held (or similarly named) rows, including Henley Business School Africa; IMD, Singapore; Middlesex University Dubai; Nova Business School Africa (Ghana); Peking University HSBC Business School listed as UK (and the Shenzhen listings, which were also not in the file); Rutgers School of Business–Camden and Rutgers University–Camden; and the named two-place rows (Goldman Sachs & Imperial; Consip Spa and LUISS; EGADE and VIVA Idea; Yale SOM / AQR; Public Sector Scorecard and Sheffield Business School; Leeds and Carnegie Mellon; Nanyang Business School & Renmin; Macquarie Business School & MIT CISR). All 47 are byte-identical to the base. Middlesex Mauritius was not present on the current panels.

Diamond Leadership Institute, the Nielsen/SEARCA dropped rows, and `#15558` were not in the file and are unchanged.

## Directory (Web build on a copy)
- before: 11,175 / 6,698 / 6,698 / 169 / 43 (reproduces the live counts)
- after:  11,078 / 6,698 / 6,698 / 169 / 43
- Shared-name guard stays 43; no change needed.
- Appointments without an institution stayed at 13,415.
- Institutions fell by 97 as unmatched school-unit display names folded into parent universities that already had a ROR. With-ROR and distinct ROR were unchanged (no new ROR). Countries unchanged at 169.

## QC: ok
- Row counts, headers and line endings unchanged. Long table 269,545 rows. AJG1 12,326 (nav 10 untouched), AJG2 5,462, FT50 10,049/10,049. Pilots byte-identical.
- No raw edits. 0 invented RORs. Protected names intact (11KBW, UNSW, INSEAD France `00ghzk478` / Singapore `05ynf4333`, 1 Decembrie 1918). No non-Latin names lost; no near-miss pairs. 0 emails or phones.
- Panel–long mismatches: 0 on changed rows; 874 on the full table (882 in the base).
