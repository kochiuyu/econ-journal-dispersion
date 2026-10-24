# ABS / AJG rankings freeze

- **Freeze path:** `/workspace/econ-journal-editors/releases/rankings_abs_ajg_20261024`
- **Built (Asia/Hong_Kong):** 2026-10-24T23:34:38+08:00
- **Source:** CABS Academic Journal Guide portal extracts (via Econ-Journal-Web / user login).
- **Raw private inputs (not in this freeze):** `/workspace/abs-ajg/ajg_2024.csv`, `ajg_2021.csv` (+ methodology PDFs).
- **Raw sizes:** ajg_2024.csv = 1823 journals; ajg_2021.csv = 1698 journals.
- **Years:** AJG 2024, 2021, 2018, 2015; ABS 2010 (`source_note=ABS2010`).
- **Primary file:** `ajg_2024.csv` for overlapping years; gaps filled from `ajg_2021.csv` (ISSN overlap or normalized title).
- **Ratings:** normalized to `{4*, 4, 3, 2, 1}`; blanks = not rated / not in that edition. Original kept in `rating_raw`. No invented ratings.
- **journal_id:** ISSN match to FT50 / core49 / ABDC A*/A/B/C (incl. `issn_online` in catalog notes), else unique normalized title. Cross-catalog different id strings → pick primary by priority ft50 > core49 > abdc_a_star > abdc_a > abdc_b > abdc_c; all hits in `journal_id_crosswalk.csv`. Ambiguous only if one catalog maps the same ISSN/title to multiple ids.

## Row counts

| edition_year | rows | with rating | with journal_id | match % |
|---:|---:|---:|---:|---:|
| 2024 | 1823 | 1823 | 1378 | 75.6% |
| 2021 | 1706 | 1706 | 1317 | 77.2% |
| 2018 | 1545 | 1545 | 1231 | 79.7% |
| 2015 | 1377 | 1377 | 1120 | 81.3% |
| 2010 | 794 | 794 | 721 | 90.8% |

- **Long panel rows:** 7245
- **Conflicts / invalid raw:** 0 (see `conflicts.csv`)
- **Unmatched row-years:** 1478; unique journals ~492
- **Crosswalk rows:** 6250

## Match methods (long panel)

- `issn`: 5736
- `unmatched`: 1478
- `title`: 31

## Primary catalog among matched rows

- `abdc_b`: 2049
- `abdc_a`: 2004
- `abdc_c`: 781
- `abdc_a_star`: 475
- `ft50`: 248
- `core49`: 210

## Rating distribution (long panel)

- `1`: 2736
- `2`: 2393
- `3`: 1498
- `4`: 457
- `4*`: 161

## Schema (`abs_ajg_long.csv` / `abs_ajg_YYYY.csv`)

```
edition_year, rating, rating_raw, journal_title, print_issn, e_issn, field, publisher, journal_id, catalog, match_method, source_file, source_note
```

## Top unmatched (unique journals)

- Academia Revista Latinoamericana de Administracion (1012-8255; IB&AREA; last seen 2024; unmatched)
- Acta Commercii (2413-1903; ETHICS-CSR-MAN; last seen 2024; unmatched)
- Action Research (1476-7503; ORG STUD; last seen 2024; unmatched)
- Advances in Austrian Economics (1529-2134; ECON; last seen 2024; unmatched)
- Advances in Decision Sciences (2090-3359; ECON; last seen 2024; unmatched)
- Advances in Econometrics (0731-9053; ECON; last seen 2024; unmatched)
- Advances in Industrial and Labor Relations (0742-6186; HRM&EMP; last seen 2024; unmatched)
- Advances in Methods and Practices in Psychological Science (AMPPS) (2515-2459; PSYCH (GENERAL); last seen 2024; unmatched)
- Africa Journal of Management (2332-2373; ETHICS-CSR-MAN; last seen 2024; unmatched)
- African Affairs (0001-9909; IB&AREA; last seen 2024; unmatched)
- African Evaluation Journal (2310-4988; REGIONAL STUDIES, PLANNING AND ENVIRONMENT; last seen 2024; unmatched)
- African Finance Journal (1605-9786; FINANCE; last seen 2024; unmatched)
- African Journal of Employee Relations (2664-3731; HRM&EMP; last seen 2024; unmatched)
- Agrekon (0303-1853; ECON; last seen 2024; unmatched)
- American Journal of Psychology (0002-9556; PSYCH (GENERAL); last seen 2024; unmatched)
- Annals of Corporate Governance (2381-6724; FINANCE; last seen 2024; unmatched)
- Annals of Economics and Statistics (2115-4430; ECON; last seen 2024; unmatched)
- Annals of Science and Technology Policy (2475-1820; INNOV; last seen 2024; unmatched)
- Annals of Work Exposures and Health (2398-7308; ETHICS-CSR-MAN; last seen 2024; unmatched)
- Annual Review of Information Science and Technology (0066-4200; INFO MAN; last seen 2024; unmatched)
- Antipode (0066-4812; SOC SCI; last seen 2024; unmatched)
- Applied Ergonomics (0003-6870; PSYCH (WOP-OB); last seen 2024; unmatched)
- Applied Psychology: Health and Well-Being (1758-0846; PSYCH (WOP-OB); last seen 2024; unmatched)
- Area (0004-0894; SOC SCI; last seen 2024; unmatched)
- Asia Pacific Journal of Public Administration (2327-6665; PUB SEC; last seen 2024; unmatched)
- Asia and the Pacific Policy Studies (2050-2680; PUB SEC; last seen 2024; unmatched)
- Asia-Pacific Journal of Operational Research (0217-5959; OR&MANSCI; last seen 2024; unmatched)
- Asian Journal of Technology Innovation (1976-1597; INNOV; last seen 2024; unmatched)
- Aslib Journal of Information Management (2050-3806; INFO MAN; last seen 2024; unmatched)
- Assessment and Evaluation in Higher Education (0260-2938; MDEV&EDU; last seen 2024; unmatched)
- Australian Journal of Psychology (0004-9530; PSYCH (GENERAL); last seen 2024; unmatched)
- Bancaria The Journal of the Italian Banking Association (2499-4472; FINANCE; last seen 2024; unmatched)
- Banks and Bank Systems (1816-7403; FINANCE; last seen 2024; unmatched)
- Behavioral and Brain Sciences (0140-525X; PSYCH (GENERAL); last seen 2024; unmatched)
- Behavioural Public Policy (2398-063X; ECON; last seen 2024; unmatched)
- Brazilian Journal of Public Administration (Revista de Administração Pública - RAP) (0034-7612; PUB SEC; last seen 2024; unmatched)
- British Educational Research Journal (0141-1926; MDEV&EDU; last seen 2024; unmatched)
- British Journal of Guidance and Counselling (0306-9885; MDEV&EDU; last seen 2024; unmatched)
- British Journal of Psychology (0007-1269; PSYCH (GENERAL); last seen 2024; unmatched)
- Canadian Journal of Behavioural Science / Revue canadienne des sciences du comportement (0008-400X; PSYCH (GENERAL); last seen 2024; unmatched)
- … and 452 more (see `unmatched_journals.csv`)

## Files

- `abs_ajg_long.csv` — all years stacked
- `abs_ajg_{2010,2015,2018,2021,2024}.csv` — per-year slices
- `journal_id_crosswalk.csv` — all catalog hits
- `unmatched_journals.csv`
- `conflicts.csv`
- `RELEASE_NOTES.md` — this file

## Reproducibility

```bash
python3 /workspace/econ-journal-editors/scripts/build_abs_ajg_rankings.py
```

Do not copy raw `/workspace/abs-ajg/*.csv` into the public econ-journal-dispersion repo.

