# Weird Institution-name fix — editors_weird_inst_fix_20261110

Published 2026-11-10 (Asia/Taipei). Supersedes `editors_country_misprint_fix_20261110` (stacked on PR #53).

## What changed

Keyed, user-approved clean-up of the non-REVIEW rows of the Institution audit (`institutions_weird_send_20261110.csv`):

| Action | Institutions | Publish rows | Long rows |
|---|---:|---:|---:|
| DROP (place-only, generic role, credential) | 178 / 187 | 391 | 505 (incl. pilot-linked) |
| Country-only fallback dropped | 5 | 5 | 8 |
| STRIP (role prefix, address, postcode, URL, punctuation, state code) | 594 / 715 | 632 | 55 |
| SET_COUNTRY (trailing state / code) | 122 / 124 | 137 | 222 |
| REMATCH (existing panel twin ROR) | 186 / 214 | 249 | 124 |
| University of Georgia (US rows on Tbilisi `02bjhwk41` → `00te3t702`) | 1 | 7 (+2 FT50 mirror) | 11 |

Counts are the Collector's (publish + pilot for long rows). DROP uses the Marks mechanism: `canonical_name`, `raw_affiliation` and `ror_id` blanked, printed text kept in `ror_notes`; long `raw_aff_part` blanked with the trace in `ror_match_note`; country kept. 120 rows whose printed raw still names an organisation (e.g. `Sydney Law School`, `Tokyo Institute of Technology`, `T-Mobile`) were not dropped; they are in `WEIRD_INST_skipped_20261110.csv` (level=row) with a suggested canonical for a later restore. REVIEW names are untouched. No ROR id is invented.

Applied here: 1,429 publish-panel rows (A* 117, A 352, B 350, C 427, prio43 22, ajg2 54, ajg1 81, FT50 ROR file 18, FT50 slim 8) and 630 long rows. Details: `data/editors/releases/editors_weird_inst_fix_20261110/README.md`.

## Directory

| | Before (#53 head b33462e) | After | Collector |
|---|---:|---:|---:|
| Institutions | 15,160 | 14,672 | 15,160 → 14,672 |
| with ROR | 6,387 | 6,387 | 6,387 |
| Countries | 162 | 162 | 162 |
| Appointments without an institution | 12,068 | 12,460 | 12,068 → 12,460 |
| Shared display names | 69 | 69 | 69 |
| Appointments / editors / journals | 162,575 / 112,718 / 2,853 | unchanged | |

All Collector numbers match.

## Checks

- Old values: every publish cell checked against the change log `old`; 2 of 2,657 panel cells differed (long: 0 of 1,142) from the published Directory copy and were resolved by hand:
  - A* #11663 `ror_notes`: the Directory copy carries an older note prefix; the DROP trace was appended to the published note (raw and canonical blanked as logged).
  - C #12376 `canonical_name`: the Collector's `old` still had an email address that the Directory had already removed; set to the logged new value `Dan Swanson & Associates`.
- Dropped rows: 0 site rows of the 381 dropped editors still show their dropped name or printed raw. The printed text survives only in the `ror_notes` / `ror_match_note` trace, which the site does not render.
- Contact data: 0 emails and 0 phone numbers in the site data files and in any added panel line.
- Spot checks: Harvard Business School, Cambridge, MA → `Harvard Business School` (Porter, Amabile); `Sydney` (Sydney Law School rows) skipped, not dropped; University of Georgia US rows → `00te3t702` / United States; role prefix `Executive Director, Global Deloitte AI Institute` → `Global Deloitte AI Institute`; `Independent Researcher, Vermont` (Laurie Marshall) dropped.
- Row counts unchanged (ajg1 12,316 and ajg2 5,462 with navigation rows out; FT50 10,047); long table 181,443 rows, 20 columns. Protected names unchanged; no pilot files; CITATION.cff, core49 and `scripts/build_site.py` untouched.
