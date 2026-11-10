# editors_post_review_fix_20261110

Base: `editors_review_resolved_fix_20261110`. Built 2026-11-10 (Asia/Taipei). Approved by the user via Econ-Journal-Web.
Script: `abs_ajg/scripts/post_review_fix_20261110.py`. Per-name decisions: `post_review_decisions_20261110.py`.
Audit input: `institutions_weird_post_review_20261110.csv` (399 names; shared_name_split's 34 KEEP rows left untouched).
Every edit is keyed on `editor_row_key`.

## Directory (Web build_site.py @ 8e16473: guard 49 + word-boundary scrub)
| | before | after |
|---|---|---|
| Institutions | 14,440 | 14,195 (−245) |
| with ROR / distinct ROR | 6,379 / 6,379 | 6,379 / 6,379 |
| Countries | 162 | 162 |
| Shared names | 49 | 49 (guard unchanged) |
| Appointments without an institution | 12,487 | 12,659 (+172, the Marks-style drops) |

ROR set: lost 021a5w723 (Universitas Patria Artha) and 00qj1mf81 (Schulman, Ronca & Bucuvalas), because their only rows were wrong matches. Gained 033xgn512 (IIESS, verified through the ROR API) and 00njsd438 (Google (United States), already on pilot rows).

## Changes (Institutions / publish rows / pilot rows / long rows)
- item1 trailing city/state/country: 63 renamed + 74 dropped / 67 + 86 / 25 + 68 / 23 + 154
- item2 role prefix: 22 renamed + 49 dropped / 24 + 58 / 13 + 26 / 21 + 73
- item3 dept prefix → parent org: 30 / 32 / 18 / 43
- item4 near-duplicates: 25 name merges + 10 ROR merges + 2 drops / 29 + 13 + 5 / 15 + 1 + 3 / 5 + 14 + 4
- item5 fragments (punctuation, credential, address, place, contact): 10 renamed + 17 dropped / 10 + 25 / 2 + 7 / 11 + 31
- item6 long_sentence_bio: 3 resolved / 3 / 1 / 4 (Swiss Management Center listed as a skip)
- item7 wrong RORs: STIE ×3 ROR blanked; CUNY ×5 + ft50 mirror → 00453a208; Abt ×3 → 0502afh35 / 11 / 0 / 11
- item8 contacts: e-mail (incl. comma-malformed) + phones / 20 / 17 / 37 (38 long fields)

## QC (all pass)
- Row counts: AJG1 12,326 (10 nav rows untouched), AJG2 5,462, long 269,539. No header or line-ending changes.
- No invented RORs. One new ROR (033xgn512) verified through the ROR API.
- raw_affiliation is changed only by Marks drops (traced in ror_notes) or contact scrubs.
- No new panel↔long desync (full table: 2,006 now vs 2,019 in base).
- No near-miss merges, and no non-Latin names lost.
- 11KBW, UNSW and INSEAD France + Singapore are intact.
- No e-mail or phone left in the panels or the long table. None are in the logs, which show '[email removed]' / '[phone removed]'.
- Working panels are identical to the freeze.
