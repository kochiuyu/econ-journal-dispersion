# HANDOFF: editors_raw_drift_fix_20261110

**Status:** QC ok. Not published. No messages sent.

## Residual drift vs the Directory copy (all intended)
These are the remaining differences on raw_affiliation and the institution fields:

- **raw_affiliation (3 rows)**
  - ft50_current #2955 and ft50_current_with_ror #2955: 'Colorado State University'. The Directory is blank. This raw edit is approved.
  - ajg1 #10149: ours is 'IZZI Inc' (the live source); the Directory has 'Rosalind Franklin University of Medicine', which is wrong (a faculty-search hit for another Lawrence Sweet).
- **Institution fields (29 rows):** RORs and countries we set where the Directory has none and still shows India:
  - the 21 former NLU rows;
  - ENSAI, Kagoshima, MIT, Springer Shanghai, Gradient;
  - HKUST-GZ #27613 (the Directory shows 00q4vv597 / Hong Kong);
  - Tiffany ×2.
- **Row-level:** UPF editor_name rows #577/#578 in both ft50 files and the 10 AJG1 nav rows. The Directory excludes these by design.

## Root cause
- The 20261028/29 `institution_*` scripts wrote derived text into raw_affiliation:
  - `attach_ror_from_template` set raw = ROR name;
  - `set_stripped_org` set raw = core;
  - `new_raw` decisions and `campus_disp` also wrote into raw.
- When a row's display came from a wrong ROR (e.g. National Law University), that name replaced the printed text. The ROR was later removed, but the raw text and the India country stayed.
- Fix: those writers in 6 scripts were patched to keep raw untouched. Backups are `*.py.bak_raw_drift_20261110`.
- No current 20261110 script reuses this logic. They only blank raw on approved DROPs or restore printed text.

## Leak scan
- `RAW_DRIFT_leak_scan_20261110.csv` has 166 more rows where an institution_* script rewrote raw with a canonical/ROR name. The Directory carries the same text on all of them.
  - **120 are same-org normalisations**, e.g. 'Osaka University, Japan' → 'The University of Osaka'.
  - **46 are suspected different-org leaks**:
    - 17 Pakistan rows → 'National Institute of Oceanography';
    - 9 Publications rows → 'AM Publications';
    - 4 Japan rows → 'Temple University';
    - 2 'Beijing University' → Beihang;
    - Oxford → Sheffield/Edinburgh;
    - others.
- Restoring these needs a separate approval. They were not touched.
