# ROR pre-publish fix — 2026-11-01 (Asia/Hong_Kong, UTC+8)

**New held pack:** `releases/editors_ror_consistency3b_20261101/`  
**Source:** `releases/editors_ror_consistency3_20261101/` (untouched; md5 reconfirmed)  
**Scale pack:** not modified (`editors_backfill_scale_ror_20261031` standing rules already held)  
**Published / handed to Web:** no

## Verdict after fix: **GO** (with known coverage caveats unchanged)

The HIGH Heidelberg blank request and MEDIUM panel↔long desyncs from `reports/PREPUBLISH_CHECK_20261101.md` are resolved as follows. Coverage gaps / open ROR decisions / scale caveats from the prepublish check are unchanged and still need to be shown to Web at handoff — they are not blockers introduced by this pack.

## 1. Heidelberg `editors_abdc_c_current#2971` (HIGH)

| | |
|---|---|
| Editor | Salil Khetani |
| `canonical_name` | Heidelberg University |
| `raw_affiliation` | **Heidelberg University, Ohio, United States** |
| ROR | `https://ror.org/04rcqnp59` Heidelberg University (United States) |
| Action | **KEEP** (no blank) |

Reason: the prepublish residual treated this as a missed bare-Heidelberg blank. It is not bare — Ohio is printed. Consistency3 rule (`Ohio|Tiffin` → keep `04rcqnp59`) correctly retained the row; only this ABDC-C Ohio print remained, which is intentional. Method note recorded as audit `keep` in the changes CSV (not a `ror_consistency3_miss_20261101` blank).

## 2. Panel ↔ long `is_panel_ror` desyncs (MEDIUM) — 17 fixed

All 17 keys from `D_long_sync.json` now have a long part with `is_panel_ror=1` whose `ror_id` equals the panel primary. Direction: **long synced to panel** (campus-over-system / existing panel primary preserved; system RORs not reintroduced).

Long `ror_match_kind` = `consistency3b_sync`. Panel: `ror_id_aff_rank` filled where empty; `ror_notes` appended with `ror_prepublish_fix_20261101: panel↔long is_panel_ror sync...`.

Keys:
- Maryland College Park (10): `editors_ft50_current_with_ror#6052,#9767,#9807`; `editors_abdc_a_star_current#2642,#2682,#4556,#22143,#22149`; `editors_abdc_a_current#37343`; `editors_abdc_a_current_with_profile_pilot#36824`
- Kauffman (2): `editors_abdc_b_current#33167`; `editors_abdc_b_current_with_profile_pilot#33034`
- Georgian Academy (2): `editors_abdc_c_current#18381,#18433`
- BUPT (1): `editors_abdc_c_current#18440`
- Salisbury (1): `editors_abdc_c_current#18941`
- LMU (1): `editors_abs_ajg_gap_prio43_current#321`

Post-fix mismatch count: **0** across all 11 panels.

## 3. Alós accent (LOW)

No change. Panel/source name left as captured; accent not invented. HTML text-layer missing "Alós" is encoding, not a data error to "fix" by inventing characters.

## Rows changed

| file | rows touched |
|---|---|
| editor_affiliations.csv | 17 |
| editors_ft50_current_with_ror.csv | 3 |
| editors_abdc_a_star_current.csv | 5 |
| editors_abdc_a_current.csv | 1 |
| editors_abdc_a_current_with_profile_pilot.csv | 1 |
| editors_abdc_b_current.csv | 1 |
| editors_abdc_b_current_with_profile_pilot.csv | 1 |
| editors_abdc_c_current.csv | 4 (sync meta only; #2971 unchanged) |
| editors_abs_ajg_gap_prio43_current.csv | 1 |
| editors_ft50_current.csv / ajg1 / ajg2 | 0 |

## Verification checklist

- [x] Heidelberg #2971 still on `04rcqnp59` with Ohio in raw text
- [x] 0 panel↔long `is_panel_ror` mismatches of the kinds fixed
- [x] `affiliation_count` matches long part counts on synced keys
- [x] Headers / row counts identical to consistency3
- [x] Consistency3 source md5 unchanged
- [x] `_build.json` out_md5 recorded for new pack
- [x] Changes CSV lists every changed cell/row (+ audits)

## Publish readiness

**GO** to hand (when user says publish):

```
releases/editors_backfill_scale_ror_20261031/
releases/editors_ror_consistency3b_20261101/
reports/BACKFILL_scale_ror_20261031.md
reports/ROR_CONSISTENCY3_20261101.md
reports/ROR_PREPUBLISH_FIX_20261101.md
reports/PREPUBLISH_CHECK_20261101.md
```

Retire consistency3 (and older ROR line) for public current use in favour of consistency3b. Still flag to Web: scale header/+columns/`staff_excluded`/`other_ror_ids` `|` / row-key crosswalk; consistency3/3b new method values; coverage gaps (RED/JBES/JRU/JUE/EJ2018/~4k names-only); open ROR decisions.

*Fix completed 2026-11-01 Asia/Hong_Kong (UTC+8). No publish.*
