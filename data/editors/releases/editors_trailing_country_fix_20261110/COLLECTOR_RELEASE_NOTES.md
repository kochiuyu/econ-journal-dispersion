# RELEASE NOTES — editors_trailing_country_fix_20261110

**When (Asia/Taipei):** 2026-11-10 19:17 Asia/Taipei
**Base:** `editors_raw_aff_part_no_fix_20261110` (Directory PR #52, f8b015e6)
**Scope:** user-approved trailing-country fix on Institutions (`/workspace/institutions_trailing_country_send_20261110.csv`). The audit's 190 REVIEW and 403 KEEP rows are a do-not-touch set.

## Mapping (edj-web `scripts/build_site.py`)
- An Institution is keyed by `ror_id`, or else by `norm_space(display_affiliation)`.
- `display_affiliation` = `ror_name` → `canonical_name` → `raw_affiliation` (scrubbed). Only the primary affiliation of each row is used; `other_ror_ids` and the long table are not read.
- All 5,009 send Institutions are unmatched (no ROR). Rows were matched with the Directory's own key on the Directory copies, then edited in our panels by `editor_row_key`. Each row's own display had to agree.
- **Name:** `canonical_name` is set (it overrides raw in the display). `raw_affiliation` is never edited.
- **Geo:** `ror_country` and `continent` are set. The continent is the panels' own country→continent mode; 5 countries missing from the panels were mapped by hand.
- `editors_ft50_current.csv` has no canonical_name column, so it gets the geo change only. The Directory reads `editors_ft50_current_with_ror.csv`.
- **Pilots:** the same change is applied to the pilots, matched by their own display, following the drop_rematch and punct_split precedent. They are not for publish.
- **Long table:** `ror_country` is updated on the matching part (the is_panel_ror part, else rank 1); for REMATCH-with-ROR, `ror_id`, `ror_name` and `is_panel_ror` are updated too. `raw_aff_part` is never edited.

## Counts
| action | requested | Institutions applied | publish panel rows | pilot rows | long rows |
|---|---|---|---|---|---|
| STRIP_AND_SET_COUNTRY | 4634 | 4546 | 5600 | 2538 | 8138 |
| STRIP | 220 | 220 | 242 | 103 | 242 |
| STRIP_AND_FIX_COUNTRY | 7 | 3 | 3 | 5 | 8 |
| REMATCH | 148 | 137 | 202 | 110 | 312 |

Skipped Institutions: 96
- city/region/country-only remainder: 75
- generic remainder would merge different organisations across countries: 16
- protected org: 2
- twin is REVIEW/KEEP: 2
- different King's College: 1
Row-level skips (our display differs from the Directory copy): 7. Full list: `TRAILING_COUNTRY_skipped_20261110.csv`.

Directory build (read-only, temp copy of edj-web; Directory copy before, and the same copy with this freeze's edits by key after):
- before: Aggregates: 2,853 journals (2,426 with a field, 2,835 with a board link), 15,434 institutions (6,387 with ROR, 69 shared names), 12,067 appointments without an institution
- after: Aggregates: 2,853 journals (2,426 with a field, 2,835 with a board link), 15,165 institutions (6,387 with ROR, 69 shared names), 12,068 appointments without an institution

## Verification (ok=True)
- invented ROR: []; existing ror_id changed: 0; system ROR assigned: 0
- protected rows changed: 0; 11KBW True, UNSW True, INSEAD FR+SG True
- raw_affiliation changed: 0; raw_aff_part changed: 0
- unexpected panel/long diffs: 0/0; panel↔long desync (ror + country on changed keys): 0
- headers/EOL changes: []; rows unchanged True; AJG1 12326 (10 nav untouched: True), AJG2 5462
- pilots byte-identical: {'editors_abdc_a_current_with_profile_pilot.csv': False, 'editors_abdc_b_current_with_profile_pilot.csv': False} (changed by design)

## Risks / notes
- Strips that merge different-country variants into one Institution are listed in the summary JSON (`risks`). Generic remainders and city-only remainders were held back.
- Row-level skips: 5 rows where our canonical is “National Law University” while the Directory shows the printed name. This is a pre-existing collector rewrite that the Directory guardrail masks. 2 more rows have truncated canonicals.
