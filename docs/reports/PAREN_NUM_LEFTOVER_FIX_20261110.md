# editors_paren_num_leftover_fix_20261110

Published 2026-11-10 (Asia/Taipei) into the Directory current panels. It supersedes the `editors_tokyo_other_inst_fix_20261110` current panels (PR #49). It is a keyed, user-approved fix. There is no site filter and no new ROR id, and `scripts/build_site.py` is unchanged.

## Why these were left

The 20261110 punctuation/split audit (`institutions_punct_split_flags_20261110.csv`) flagged every Institution that started with a parenthesis or a digit. #47 applied only the DROP and REMATCH flags. The 12 REVIEW leftovers were:
- Ten EDPACS "Name (credentials) – role, organisation" blurbs.
- `(GGSIPU) Periyar…`.
- `(Partner, retired), Hengeler Mueller`.
- The numbered OECD list for Balázs Égert.

The audit had also marked 14 numbered organisations KEEP.

## What changes

The 25 changelog rows:
- **10 organisation-only names, with no ROR:**
  - Hengeler Mueller
  - C.H. Dunn Consulting
  - auditline
  - New York State Comptroller
  - CMA Holdings Inc.
  - IsecT Ltd.
  - AuditNet LLC
  - Grant Thornton
  - Pepperweed
  - Aditya Birla Group
- **1 DROP:** Norman Marks.
- **2 REMATCH onto ROR ids already on the panels with the same name:** OECD `0438wbg98` and Guru Gobind Singh Indraprastha University `034q1za58`.
- **12 note-only rows:** the Tokyo Institute of Technology / Kojima seats, where the Directory already kept Japan.

The printed `raw_affiliation` is unchanged on every row, and the existing notes are kept with the fix token appended. Row counts are unchanged; ajg1 stays 12,316 and ajg2 stays 5,462.

## Directory totals

Appointments 162,575. Editors 112,718. Journals 2,853. Countries 159.
Institutions 15,435 (6,387 with a ROR id), were 15,438 / 6,387. Appointments without an institution stay 12,066. Shared display names stay 69.

Where the rows land:
- **Grant Thornton:** one row (United States, 2).
- **OECD:** joins the OECD ROR row (35).
- **GGSIPU:** joins Guru Gobind Singh Indraprastha University (India, 4).
- **auditline:** its own unmatched row with no country.

## Remaining parenthesis- and number-start Institutions

There are 15, with 18 appointments:
- **14 kept on purpose:**
  - On the standing keep list: 1 Decembrie 1918 University (ROR `04577k168`) and 11KBW.
  - Kept by the audit: 39 Essex Chambers, 3 Hare Court, 5 Wentworth Chambers, 11powerN, 125th Street BID, 2050 Alliance, 2W China Investment Consulting, 3s Research & Consulting, 505 Savjetovanje, 53NG, 55 Capital Partners and 720 Strategies.
- **`(CPA, CRMA) - Author, Speaker, Thought Leader, OCEG Fellow, Honorary Fellow of the Institute of Risk Management` (1):** Norman Marks. His `canonical_name` is now blank, but the Directory falls back to the printed `raw_affiliation`, which is the bio. It is not hidden with a site filter. Hiding it would mean blanking the printed text, or a display rule, which needs a decision.
