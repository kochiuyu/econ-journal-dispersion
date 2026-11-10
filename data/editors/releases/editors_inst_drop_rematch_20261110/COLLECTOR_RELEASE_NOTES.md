# RELEASE NOTES — editors_inst_drop_rematch_20261110

**When (Asia/Taipei):** 2026-11-10 12:28 Asia/Taipei
**Base:** `editors_nonlatin_inst_20261110` (PR #45)
**Source flags:** `/workspace/institutions_number_long_singleton_drop_rematch_20261110.csv` (723 flag rows; 657 unique display_names; DROP+REMATCH only)
**Scope:** panel-only Institutions cleanup. Unchanged panels byte-copied from base. Working panels under ft50/abdc/abs_ajg updated to match this freeze.

## Summary
- flag rows in work file: 723
- unique display_names: 657
- unique display_names applied (DROP/REMATCH/GAP): 623
- panel-row updates: 754 (DROP=84, REMATCH=669, GAP=1)
- unique editor_row_keys touched: 754
- NOT_FOUND (flagged display not present as unmatched on base panels): 34
- panels patched: 11
- User rule: **keep printed raw_affiliation** on rematch; set canonical_name to the twin's existing panel ror_name
- Never invent ROR ids; every new ror_id verified present on the base freeze
- KEEP 11KBW / UNSW Sydney / INSEAD (France and Singapore remain separate)
- Panel ↔ long sync: parts=803 rematch_keys=669 desync=0

## Panel-row updates
- `editors_abdc_c_current.csv`: 198
- `editors_abs_ajg_gap_ajg1_current.csv`: 191
- `editors_abdc_b_current.csv`: 84
- `editors_abdc_a_current.csv`: 78
- `editors_abdc_b_current_with_profile_pilot.csv`: 62
- `editors_abdc_a_current_with_profile_pilot.csv`: 44
- `editors_abs_ajg_gap_ajg2_current.csv`: 44
- `editors_abdc_a_star_current.csv`: 29
- `editors_ft50_current.csv`: 11
- `editors_ft50_current_with_ror.csv`: 11
- `editors_abs_ajg_gap_prio43_current.csv`: 2

## Unchanged panels (byte-copied from base)
_none_

## Top REMATCH twins (by ror_name, panel-row counts)
- University of Science and Technology of China: 12
- The University of Adelaide: 10
- University of South Australia: 9
- Institute of Management Technology: 8
- University of the West Indies: 6
- National Institutes of Health: 6
- Massey University: 6
- National Research Council: 5
- University of Ljubljana: 5
- Kansas State University: 4
- Bocconi University: 4
- Stanford University: 4
- University of St.Gallen: 4
- Xi’an Jiaotong-Liverpool University: 4
- Tsinghua University: 4
- Dalhousie University: 4
- Xiamen University: 4
- United Nations: 4
- Vienna University of Economics and Business: 4
- Temple University: 3
- Lakehead University: 3
- Maastricht University: 3
- Concordia University: 3
- Insper: 3
- Southeast University: 3

## GAP (leave ROR blank; keep printed name)
- The Universidad Nacional Experimental Politécnica

## NOT_FOUND
Most of these are `source=ror_name` official names that already have a ror_id on every matching base-panel row (stale unmatched flags vs PR #45). `Georgia Inst of Technology` is not present on the base panels (Decision Sciences already uses `Georgia Institute of Technology` with the Georgia Tech ROR).
- Asia University
- Bern University of Applied Sciences
- Campbell Collaboration
- Centers for Disease Control and Prevention
- Centraal Bureau voor de Statistiek
- European Bioinformatics Institute
- Georgia Inst of Technology
- Institut Mines-Télécom Business School
- International Business School
- London School of Economics and Political Science
- Magna Graecia University
- Nanyang Technological University
- Northwestern University
- Patient-Centered Outcomes Research Institute
- Roma Tre University
- Roosevelt University
- Saint Francis University
- Seattle University
- St. John's University
- St. Thomas University
- Stockholm School of Economics
- Tilburg University
- United Nations Conference on Trade and Development
- United Nations University
- University of Bergamo
- University of Bonn
- University of Glasgow
- University of Houston
- University of Luxembourg
- University of Michigan
- University of Minnesota
- University of Pennsylvania
- University of Southern California
- Vel Tech Rangarajan Dr. Sagunthala R&D Institute of Science and Technology

## Conflicts (same display_name, multiple actions)
_none_

## Campus / system overrides
_none_

## Work-file typo aliases (unique intended panel string)
- typo alias: RFW-University of Bonn, Ecole Supérieure Multinationale des ecommunications, Germany → RFW-University of Bonn, Ecole Supérieure Multinationale des Telecommunications, Germany

## Multi-aff note
Existing long parts were **not** split and no new parts were invented.
REMATCH writes the twin onto the long part that already carries that ror_id, or else the first empty-ror part, and marks that part `is_panel_ror=1`. Secondary parts keep any pre-existing ror_id.
DROP blanks `raw_aff_part` and clears ROR on every part of the touched key.

## Ambiguous / judgment calls
- `The Universidad Nacional Experimental Politécnica` → GAP (proposed twin Universidad Nacional Costa Rica `01t466c14` is the wrong org; no UNEXPO ROR on base panels).
- `KU Leuven / North-West University` uses the work-file proposed twin (North-West University); KU Leuven is also already on the panels and remains on the other long part. Logged, not overridden (not a campus-vs-system case).
- INSEAD Fontainebleau / Boulevard de Constance rematched to INSEAD France `00ghzk478` (not Singapore).
- UNSW Australia, Sydney → UNSW Sydney `03r8z3t63`; UNSW Canberra variants → UNSW Canberra `0125wpx05`.
- Trailing `/` on the Rainer Lenz EDPACS bio was normalized so the DROP still applied.

## Verification
- invented_ror_ids: []
- applied_ror_not_on_base: []
- remaining_bad_n: 0
- panel_long_desync_n: 0
- 11KBW present: True (n=4)
- UNSW Sydney present: True
- INSEAD France + Singapore present: True

## Files
- 11 current panels (patched where flagged; others byte-copied)
- `editor_affiliations.csv` (synced for touched keys)
- `INST_DROP_REMATCH_changes_20261110.csv`
- `HANDOFF.md`, `SENDTO_BLURB.txt`, this file
