# RELEASE_NOTES — editors_nonft50_url_aff_20261028

**When (Asia/Hong_Kong):** 2026-10-28 13:07 HKT

## Goal
Same URL→university fill as FT50 (`editors_ft50_url_aff_20261028`) for **non-FT50** panels: ABDC A*/A/B/C. AJG-gap quantified (no `faculty_profile_url` column yet).

## Method
1. Quantify rows with nonempty `faculty_profile_url` but empty `raw_affiliation` / missing `ror_id`.
2. Infer affiliation from faculty profile host (domain-boundary map; never invent); HTTP fetch corroboration; Bing only as fallback.
3. Rematch ROR **high/medium** only; merge into shared crosswalk.
4. Clear junk non-person URLs (e.g. udel.edu registrar “Add Sections”).
5. Cleanup unusable affs with host evidence (Tokyo→UTokyo, CREI→UPF, EPGE/FGV→FGV).
6. Optional: `--apply-only` unused high/medium faculty-web cache hits keyed by name+ROR; second host-map pass for any new URL-without-aff.

## Before → after (ABDC live)

| Panel | URL no aff | → | URL no ROR | → | faculty URL % | aff % |
|---|---:|---:|---:|---:|---:|---:|
| A* | 28 | **0** | 31 | **0** | 8467/25178 → 12523/25178 | 23881/25178 |
| A | 18 | **0** | 18 | **0** | 5202 → 6237 | 43401 |
| B | 1 | **0** | 1 | **0** | 3123 → 3509 | 40020 |
| C | 0 | **0** | 0 | **0** | 1228 → 1379 | 24306 |

- Host-map / cleanup fills (pass 1): **43** + junk URL cleared **4** + aff cleanups **3**.
- Faculty cache apply-only (name+ROR key): A* **+4056**, A **+1043**, B **+386**, C **+151** URL rows.
- Pass-2 host fill after cache: **+48** aff (URL-no-aff back to **0**).

## AJG-gap
| Panel | Rows | Missing aff | `faculty_profile_url` |
|---|---:|---:|---|
| prio43 | 3,166 | 450 | **absent** |
| ajg2 | 4,985 | 306 | **absent** |
| ajg1 | 11,230 | 2,565 | **absent** |

URL→university N/A until a faculty-URL pass is run on AJG-gap.

## Freeze files
| File | Rows | URL filled | Aff filled | URL no aff | URL no ROR | md5 |
|---|---:|---:|---:|---:|---:|---|
| `editors_abdc_a_star_current.csv` | 25,178 | 12,523 (49.7%) | 23,881 (94.8%) | 0 | 0 | 1e36c442287f01b3561954405a7c204b |
| `editors_abdc_a_current.csv` | 45,363 | 6,237 (13.7%) | 43,401 (95.7%) | 0 | 0 | e0289ce255bce3f851177bf63f85235f |
| `editors_abdc_b_current.csv` | 42,139 | 3,509 (8.3%) | 40,020 (95.0%) | 0 | 0 | 3de53fa5e0832a324e01a4f37f7a569f |
| `editors_abdc_c_current.csv` | 26,720 | 1,379 (5.2%) | 24,306 (91.0%) | 0 | 0 | 575cbd1f88858bc72df5a4537d85801a |
| `editors_abs_ajg_gap_prio43_current.csv` | 3,166 | n/a (no faculty_profile_url) | 2,716 | — | — | da5460159ece7777b223ef97908bf4ca |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,985 | n/a (no faculty_profile_url) | 4,679 | — | — | 4ef56cb8f19879c10c08ab0a46273978 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,230 | n/a (no faculty_profile_url) | 8,665 | — | — | 50319ccdf5c0ae9d12e8e879321bcc45 |

## Artifacts
- Script: `abdc/scripts/fill_aff_from_faculty_url_nonft50.py`
- Audit: `abdc/reports/FILL_AFF_FROM_FACULTY_URL_url_aff_nonft50_20261028.csv`
- Report: `abdc/reports/FILL_AFF_FROM_FACULTY_URL_url_aff_nonft50_20261028.md`
- Backups: `*.before_url_aff_nonft50_20261028`
- Crosswalk bak: `data/crosswalk/affiliation_ror_crosswalk_before_url_aff_nonft50_20261028.csv`

## Rules
Never invent names/ROR/URLs. Panel ROR high/medium only. Domain-boundary host matching (no substring traps).

## Published in this repository

These four ABDC CSVs replace `data/editors/abdc/releases/current/`. `data/editors/ft50/` stays freeze `editors_ft50_url_aff_20261028`. The AJG-gap checksums in the table above are the collector’s snapshot at this ABDC freeze; they are not the files this repository publishes. AJG-gap faculty URLs are freeze `editors_ajg_gap_faculty_remiss_20261028` under `data/editors/abs_ajg_gap/releases/current/`.

The directory shows `editor_name` and does not list a blank name. A bare country is not an institution. Emails, phone numbers, and photos are not written to the site. No name, ROR id, affiliation, or faculty URL was invented.

## Public site

Directory appointments stay 158,716. Editors 110,383. Journals 2,853. Countries 173. FT50 seats stay 10,045 across 50 journals. Top 5 appointments stay 363. UTD24 stays 5,178 across 24 journals.

ABDC chips: A* 25,174 (219 journals), A 45,352 (626), B 42,124 (836), C 26,719 (732). One A* row whose name is `___`, and 13 B rows that are only a phone or fax number, stay off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published. Four A rows named `Add Sections` keep that name and no longer link to the Delaware registrar page.

Faculty profile links on the directory were 23,735 after this ABDC freeze alone (were 21,666). The AJG-gap remiss on the same branch brings the directory total to 24,840. See `data/editors/abs_ajg_gap/releases/current/RELEASE_NOTES.md`. The FT50 chunk links 8,376 names: 8,375 from `editors_ft50_url_aff_20261028`, plus Sabine Matook on the Journal of Management Information Systems, whose blank FT50 URL is filled from the ABDC partner (`https://about.uq.edu.au/experts/1654`). Institutions: 10,065 rows (9,659 with a ROR id). 11,084 appointments have no institution. 28 affiliations that are only a country or territory, and 1 bracket-only fragment, stay off that page. Parked blank `editor_name` rows are 0.
