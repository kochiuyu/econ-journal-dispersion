# NYU Stern top-tier journals freeze (all departments)

- **Freeze id:** `rankings_stern_20261025`
- **Built:** 2026-10-25 17:34 HKT
- **Department page:** <https://www.stern.nyu.edu/portal-partners/faculty-guide/employment/full-time-faculty/top-tier-journals-department>
- **Scope:** all six Stern department top-tier journal PDFs linked from that page (user choice: `all_depts`).
- **Supersedes:** the Economics-only content previously published under the same freeze id.
- **Raw PDFs:** kept under `rankings_raw/stern/` locally; **not** in the public monorepo.
- **Optional context (not ingested as a department list):** Top-Tier Journals Task Force Report 2020 (Google Drive link on the department page).

## Sources

| Department code | Label | Source file | Document date | `edition_year` |
|---|---|---|---|---:|
| `accounting` | Accounting | Accounting-Top-Journals-FINAL-8.26.20.pdf | P&T meeting 30 Jul 2020; list FINAL 8.26.20 | 2020 |
| `economics` | Economics | Econ-Top-Journals-July-2020.pdf | 31 Jul 2020 | 2020 |
| `finance` | Finance | FINC-Top-tier-journals-12.12.20.pdf | 10 Dec 2020 | 2020 |
| `management` | Management & Organizations | Management-Journal-Subcommittee-Memo-AY20-21.pdf | 3 Sep 2020 (AY20-21) | 2020 |
| `marketing` | Marketing | Marketing-Dpt-Top-Journal-List-12.16.20.pdf | 16 Dec 2020 | 2020 |
| `tops` | Technology, Operations & Statistics | TOpS-Top-Publication-List-8_9_21_Final.pdf | August 2021 | 2021 |

PDF URLs (Stern site):

1. Accounting: https://www.stern.nyu.edu/sites/default/files/assets/documents/Accounting%20Department%20Top%20Journals%20list%20-%20FINAL%208.26.20.pdf
2. Economics: https://www.stern.nyu.edu/sites/default/files/assets/documents/Econ%20Top%20Journals%20-%20July%202020.pdf
3. Finance: https://www.stern.nyu.edu/sites/default/files/assets/documents/FINC%20Top-tier%20journals%20list%20updated%2012.12.20.pdf
4. Management & Organizations: https://www.stern.nyu.edu/sites/default/files/assets/documents/Management%20Journal%20Subcommittee%20Memo%20with%20List%20for%20AY20-21%20Final%20w%20Appendix.pdf
5. Marketing: https://www.stern.nyu.edu/sites/default/files/assets/documents/Marketing%20Dpt%20Top%20Journal%20List%2012.16.20.pdf
6. TOpS: https://www.stern.nyu.edu/sites/default/files/assets/documents/TOpS%20Top%20Publication%20List%208_9_21_Final.pdf

## Tier vocabulary (as printed; `rating` = `rating_raw`)

- **Accounting:** `Top-tier` — single alphabetical list of six journals (FT + SJR). Cross-department deference (“top non-Accounting journals on other Stern departments’ lists”) is **not** expanded here.
- **Economics:** `Top 5`, `Really excellent`, `Field`, `Review`. For `Field`, `field` holds the memo’s field heading. Other tiers have empty `field`.
- **Finance:** `Top-tier` (eight journals) and `Other notable` (non-comprehensive notable outlets, with `field` = Finance / Economics / Accounting / Other disciplines). Narrative “such as” review-outlet examples are **not** encoded as a formal list. Second-tier mentions used only as contrast are excluded.
- **Management & Organizations:** `Top-tier`, `Other notable`, `Notable review`. `field` holds the memo’s subfield heading. The 2014 school-wide appendix is historical context only and is **not** ingested.
- **Marketing:** `Top-tier` only (section “(1) TOP TIER JOURNAL LIST”). `field` holds Marketing / Psychology / General Science headings. Deferrals to other Stern departments are **not** expanded.
- **TOpS:** `Top-tier` and `Specialized high-impact`. `field` holds the research-area heading. **Top Conferences** are excluded (not journals). Cross-department deference is **not** expanded.

## Counts

| Edition | Rows | Matched | Match % |
|---|---:|---:|---:|
| 2020 | 176 | 157 | 89.2% |
| 2021 | 57 | 31 | 54.4% |
| **All** | **233** | **188** | **80.7%** |

Rows by department: {'accounting': 6, 'economics': 49, 'finance': 52, 'management': 49, 'marketing': 20, 'tops': 57}

### Accounting (`accounting`)

- Rows: 6 · Matched: 6 · Match %: 100.0%
- Ratings:
  - **Top-tier:** 6

### Economics (`economics`)

- Rows: 49 · Matched: 47 · Match %: 95.9%
- Ratings:
  - **Field:** 27
  - **Really excellent:** 10
  - **Review:** 7
  - **Top 5:** 5

### Finance (`finance`)

- Rows: 52 · Matched: 50 · Match %: 96.2%
- Ratings:
  - **Other notable:** 44
  - **Top-tier:** 8

### Management & Organizations (`management`)

- Rows: 49 · Matched: 40 · Match %: 81.6%
- Ratings:
  - **Notable review:** 6
  - **Other notable:** 22
  - **Top-tier:** 21

### Marketing (`marketing`)

- Rows: 20 · Matched: 14 · Match %: 70.0%
- Ratings:
  - **Top-tier:** 20

### Technology, Operations & Statistics (`tops`)

- Rows: 57 · Matched: 31 · Match %: 54.4%
- Ratings:
  - **Specialized high-impact:** 31
  - **Top-tier:** 26


- **Unmatched rows:** 45
- **Conflicts** (same journal+department+edition, different ratings): 0

## Mapping

- No ISSNs on these memos. Match is a unique normalized title to FT50, then core49, then ABDC A*/A/B/C.
- Primary `journal_id` prefers FT50, then core49, then ABDC A*/A/B/C.
- Economics rows preserve titles, tiers, field headings, and source notes from the prior Economics-only freeze; `journal_id` rematched with the same rules for consistency.
- Manual title aliases (memo → catalog title):
  - `NBER Macro Annual` → `NBER Macroeconomics Annual`
  - `Accounting Review` → `The Accounting Review`
  - `Economic Journal` → `The Economic Journal`
  - `Journal of Economic History` → `The Journal of Economic History`
  - `Journal of Industrial Economics` → `The Journal of Industrial Economics`
  - `Information System Research` → `Information Systems Research`
  - `Journal of Law, Economics and Organizations` → `Journal of Law, Economics, and Organization`
  - `Journal of the Royal Statistical Society, Series B` → `Journal of the Royal Statistical Society, Series B (Statistical Methodology)`
  - `Electronic Journal of Statistics` → `The Electronic Journal of Statistics`
- No invented journal ids or tiers. Ambiguous short titles (e.g. Finance’s `Applied Psychology`, `Journal of Computing`) left unmatched rather than guessed.
- TOpS memo title `IEEE Transactions on Pattern Recognition and Machine Intelligence` kept as printed (likely meant Pattern Analysis / TPAMI); not in FT50/core49/ABDC catalogs → unmatched.

## Unmatched

- [economics] American Economic Association Papers & Proceedings (Review)
- [economics] Carnegie-Rochester Series (Review)
- [finance] Applied Psychology (Other notable)
- [finance] Journal of Computing (Other notable)
- [management] Nature (Top-tier)
- [management] Nature Human Behaviour (Other notable)
- [management] Personality and Social Psychology Review (Top-tier)
- [management] Proceedings of the National Academy of Sciences (PNAS) (Top-tier)
- [management] Science (Top-tier)
- [management] Social Networks (Other notable)
- [management] Social Psychology Quarterly (Other notable)
- [management] Social Studies of Science (Other notable)
- [management] Theory and Society (Other notable)
- [marketing] Nature (Top-tier)
- [marketing] Perspectives on Psychological Science (Top-tier)
- [marketing] Proceedings of the National Academy of Sciences (PNAS) (Top-tier)
- [marketing] Psychometrika (Top-tier)
- [marketing] Science (Top-tier)
- [marketing] Trends in Cognitive Sciences (Top-tier)
- [tops] ACM Transactions on Intelligent Systems and Technology (Top-tier)
- [tops] ACM Transactions on Management Information Systems (Specialized high-impact)
- [tops] Annales de l'Institut Henri Poincare (Specialized high-impact)
- [tops] Big Data (research articles) (Specialized high-impact)
- [tops] Communications of the ACM (research articles) (Specialized high-impact)
- [tops] Computational Linguistics (Top-tier)
- [tops] Data Mining and Knowledge Discovery (Top-tier)
- [tops] IEEE Transactions on Automatic Control (Specialized high-impact)
- [tops] IEEE Transactions on Information Theory (Specialized high-impact)
- [tops] IEEE Transactions on Knowledge and Data Engineering (Top-tier)
- [tops] IEEE Transactions on Pattern Recognition and Machine Intelligence (Top-tier)
- [tops] Journal of Artificial Intelligence Research (Top-tier)
- [tops] Journal of Machine Learning Research (Top-tier)
- [tops] Machine Learning (Top-tier)
- [tops] Mathematical Programming (Specialized high-impact)
- [tops] Nature (Top-tier)
- [tops] Network Science (Specialized high-impact)
- [tops] PLOS One (Specialized high-impact)
- [tops] Proceedings of the National Academy of Sciences (Top-tier)
- [tops] Science (Top-tier)
- [tops] SIAM Journal on Control and Optimization (Specialized high-impact)
- [tops] SIAM Journal on Optimization (Specialized high-impact)
- [tops] SIAM Journal on the Mathematics of Data Science (Top-tier)
- [tops] Social Networks (Specialized high-impact)
- [tops] Stochastic Systems (Specialized high-impact)
- [tops] Transactions of the Association for Computational Linguistics (Top-tier)

## Schema

`edition_year,department,rating,rating_raw,journal_title,print_issn,e_issn,field,publisher,journal_id,catalog,match_method,source_file,source_note`

Department codes are stable filters analogous to Shanghai subject. Human labels are in the Sources table above.
