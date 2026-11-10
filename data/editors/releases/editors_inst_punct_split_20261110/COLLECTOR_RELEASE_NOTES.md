# RELEASE NOTES — editors_inst_punct_split_20261110

**When (Asia/Taipei):** 2026-11-10 13:51 Asia/Taipei
**Base:** `editors_inst_drop_rematch_20261110` (PR #46, merge b5d18e4a)
**Source flags:** `/workspace/institutions_punct_split_drop_rematch_20261110.csv` (180 rows; 180 unique display_names; DROP + REMATCH_TO_EXISTING only — 97 REVIEW + 14 KEEP left out)
**Scope:** panel-only Institutions cleanup (leftover punctuation starts + high-confidence splits).

## Publish set
FT50 + ABDC + AJG-gap current panels and `editor_affiliations.csv`:
- `editors_ft50_current.csv`
- `editors_ft50_current_with_ror.csv`
- `editors_abdc_a_star_current.csv`
- `editors_abdc_a_current.csv`
- `editors_abdc_b_current.csv`
- `editors_abdc_c_current.csv`
- `editors_abs_ajg_gap_prio43_current.csv`
- `editors_abs_ajg_gap_ajg2_current.csv`
- `editors_abs_ajg_gap_ajg1_current.csv`

`*_with_profile_pilot.csv` are carried through (patched the same way, for consistency) but are **NOT for publish**.

## Summary (unique display_names)
- DROP: 14
- REMATCH (existing panel ROR twin): 161
- UNIFY (name-only, ROR blank): 3
- GAP (left blank): 0
- NOT_FOUND: 2
- EXCLUDED (protected): 0

## Panel rows on publish panels (excluding profile_pilot)
- DROP 14, REMATCH 451, UNIFY 4, GAP 0, EXCLUDED 0
- appointments touched (rows): 469; logical (FT50 pair collapsed): 456
- profile_pilot rows also patched (not for publish): 151

## Rows changed by panel
- `editors_abdc_b_current.csv`: 97
- `editors_abdc_a_current.csv`: 89
- `editors_abdc_a_star_current.csv`: 88
- `editors_abdc_c_current.csv`: 88
- `editors_abdc_b_current_with_profile_pilot.csv`: 85 (profile_pilot — not for publish)
- `editors_abdc_a_current_with_profile_pilot.csv`: 66 (profile_pilot — not for publish)
- `editors_abs_ajg_gap_ajg1_current.csv`: 51
- `editors_ft50_current_with_ror.csv`: 20
- `editors_abs_ajg_gap_ajg2_current.csv`: 14
- `editors_ft50_current.csv`: 13
- `editors_abs_ajg_gap_prio43_current.csv`: 9

## Name-unifies (canonical_name only; ROR blank)
- (CIA, CFE, CFSA, CRMA, CICP, CPA) - Head of Accounting and Finance, Izmir Bakircay University, Izmir Türkiye → Izmir Bakircay University
- 39 Essex Chambers, UK → 39 Essex Chambers
- 1. Global Labor Organization, 45141 Essen, Germany → Global Labor Organization (GLO), Essen, Germany
Izmir: `Bakırçay Üniversitesi` https://ror.org/017v96566 exists only on `editors_abdc_b_current_with_profile_pilot.csv`, not on the publish panels, so it was **not** used (ROR left blank; logged).

## GAP
_none_

## NOT_FOUND
Flags whose display is not on any blank-ROR row of the base panels (already matched, e.g. `The University of Tokyo` rows all already carry `https://ror.org/057zh3y96`; or stale strings).
- Georgia Inst of Technology
- The University of Tokyo

## EXCLUDED (protected; never touched)
_none_

## Overrides / required twins
_none_

## Conflicts
_none_

## Matching note
Flags were matched against the site display (`ror_name` → `canonical_name` → `raw_affiliation`) on rows with no `ror_id`.
The work file's `source=ror_name` flags are exact-twin names; on the panels those rows carry the name in `canonical_name` (or `raw_affiliation` on `editors_ft50_current.csv`) with a blank ROR.
Printed `raw_affiliation` kept on every REMATCH/UNIFY. On `editors_ft50_current.csv` (no `canonical_name` column) the twin `ror_name` is the display.

## Verification
- invented_ror_ids: []
- remaining_bad_n: 0
- panel_long_desync_n: 0
- excluded rows changed: 0
- Los Andes: CDCHTA → ['https://ror.org/02h1b1x27'] (Venezuela `https://ror.org/02h1b1x27`; not Colombia `https://ror.org/02mhbdp94`) ok=True
- Tokyo: 269 rows on `https://ror.org/057zh3y96`, ror_name `The University of Tokyo`, bad=0
- 11KBW present: True; UNSW Sydney present: True; INSEAD France+Singapore present: True
- long sync: {"parts": 627, "rematch_keys": 593, "drop_keys": 21, "unify_keys": 6, "keys": 620} missing_long=0

## Files
- 11 current panels (11 patched; 2 are profile_pilot, not for publish)
- `editor_affiliations.csv`, `INST_PUNCT_SPLIT_changes_20261110.csv`, `HANDOFF.md`, `SENDTO_BLURB.txt`, this file
