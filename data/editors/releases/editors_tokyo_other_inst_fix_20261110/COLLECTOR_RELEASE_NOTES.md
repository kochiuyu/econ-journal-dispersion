# RELEASE NOTES — editors_tokyo_other_inst_fix_20261110

**When (Asia/Taipei):** 2026-11-10 14:21 Asia/Taipei
**Base:** `editors_tokyo_gatech_fix_20261110` (PR #48, merged)
**Scope:** the 35 remaining “Italian Cultural Institute” rows (other Tokyo institutions + Kojima “Tokyo”).

The printed raw_affiliation (panel) and raw_aff_part (long file) for every row are restored from the Directory copy (`/workspace/edj-web/data/editors/*/releases/current/`). No old “Italian Cultural Institute” value is reused.
Rows per panel: {'editors_abdc_a_star_current.csv': 1, 'editors_abdc_a_current.csv': 7, 'editors_abdc_b_current.csv': 13, 'editors_abdc_c_current.csv': 14}. Rematched: 23. ROR left blank: 12.

| Institution | ROR | ROR source | Rows |
|---|---|---|---|
| Tokyo Institute of Technology | blank | — | 11 |
| Tokyo University of Science | https://ror.org/05sj3n476 | base | 7 |
| Tokyo Metropolitan University | https://ror.org/00ws30h19 | base | 3 |
| Tokyo University of Agriculture and Technology | https://ror.org/00qg0kr10 | base | 3 |
| Tokyo International University | https://ror.org/01g9ekh39 | base | 3 |
| Tokyo University of Marine Science and Technology | https://ror.org/048nxq511 | base | 2 |
| Tokyo Keizai University | https://ror.org/03b0ym704 | base | 2 |
| (blank; printed 'Tokyo') | blank | — | 1 |
| Tokyo Gakugei University | https://ror.org/00khh5r84 | base | 1 |
| Tokyo Women's Medical University | https://ror.org/03kjjhe36 | NEW-to-panels (ROR API verified) | 1 |
| Tokyo University of Foreign Studies | https://ror.org/027tyzk91 | NEW-to-panels (ROR API verified) | 1 |

## Judgment calls
- **Tokyo Institute of Technology:** ROR left blank, canonical “Tokyo Institute of Technology”. On base, Institute of Science Tokyo `https://ror.org/05dqf9946` appears only on rows printed “Institute of Science Tokyo”/東京科学大学, never on Tokyo Tech rows. The existing ajg1 Tokyo Tech rows are already canonical-only with a blank ROR.
- **Fuhito Kojima** (`editors_abdc_a_star_current#11663`, Theoretical Economics, printed “Tokyo”): raw “Tokyo”, canonical blank, ROR blank. No faculty-page evidence was used.
- **New-to-panels ROR ids** (verified 2026-11-10 via api.ror.org v2, exact ror_display match, status active; metadata from the API):
  - `https://ror.org/03kjjhe36` Tokyo Women's Medical University
  - `https://ror.org/027tyzk91` Tokyo University of Foreign Studies
- **Multi-part printed strings** (#29311 “…; Chinese University of Hong Kong - Shenzen”, #18410 “…; Professor, Department of Management”): the full printed string is kept as a single long part (split_basis unchanged). The panel ROR is that of the first institution.
- Keys not found / unmatched: none

## Sweep (Italian Cultural Institute / 015e2vx95 / powerful_key=Tokyo)
- No other publish-panel or long-file row has “Italian Cultural Institute” in raw/canonical/ror_name, and none carries ROR `015e2vx95`.
- Notes-only mentions, already correct, left as is: ajg1 #7832/#9673 Tokyo Institute of Technology (canonical only, ROR blank; `low_candidate_ror=015e2vx95` was rejected) and a_star #5237 (Simon Fraser; history note).
- Related but different (other “Italian Cultural Institute, London/Tunis” ROR ids, already cleared, printed raw intact): abdc_b #11746, abdc_c #14206, abdc_c #21631. No change.
- profile_pilot panels (not for publish) keep the Directory-style printed raw, with notes mentioning powerful_key=Tokyo. Not changed; the 2 Tokyo University of Agriculture and Technology pilot rows carry `05crbcr45` (Tokyo University of Agriculture), which is wrong, and the Tokyo Tech pilot rows have canonical “Tokyo”. Fix these if the pilots are ever published.

## Verification
- invented ROR ids: []
- unlogged changes vs base: 0; protected rows changed: 0; header/EOL changes: []
- panel↔long desync: 0 (long parts 35/35 keys)
- 11KBW True; UNSW Sydney True; INSEAD FR+SG True
- “Italian Cultural Institute” in raw/canonical/ror_name on publish panels + long: 0
- profile_pilot panels: byte-identical to base, **not for publish**.
