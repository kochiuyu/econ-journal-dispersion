# Pre-publish check — 2026-11-01 (Asia/Hong_Kong, UTC+8)

**Verdict: GO-WITH-CAVEATS**

Nothing was published, pushed, or handed to Web. No file under `releases/` was modified. Post-check md5 reconfirm: scale panel and consistency3 `editors_ft50_current_with_ror.csv` still match `_build.json`.

Work artifacts: `reports/prepublish_check_20261101/` (integrity CSVs, spotcheck, defects, this report’s inputs). Defects summary: `reports/prepublish_check_20261101/defects.csv`.

---

## A. Integrity

| check | result |
|---|---|
| `baseline2_md5_releases.txt` (1,219 files of every release that existed before the 2026-11-01 rebuild) | **1,219 OK, 0 drift, 0 missing** |
| `editors_backfill_scale_ror_20261031` `out_md5` + `docs_md5` | **all OK** |
| `editors_ror_consistency3_20261101` `out_md5` (+ `out_md5.txt`) | **all OK** |
| Other packs with `_build.json` `out_md5`/`outputs_md5`/`docs_md5` | **all OK** |
| New on disk since baseline2 | 41 files = whole `editors_backfill_scale_20261101/`, `editors_backfill_scale_ror_20261031/`, `editors_ror_consistency3_20261101/` (expected) |

**Conclusion:** held releases are byte-stable; this check did not alter them.

---

## B. Pack inventory

71 folders under `releases/` (editors_* + rankings_* + `_stern_ref`).

### Include in a consolidated publish (newest line)

| pack | main rows | role |
|---|---|---|
| `editors_backfill_scale_ror_20261031` | 15,446 panel; 11,661 long | Multi-year core49-scale backfill with ROR |
| `editors_ror_consistency3_20261101` | 11 current panels + long | Current FT50 / ABDC / AJG-gap panels after foreign-namesake ROR fix |
| `rankings_*` (5 packs) | as frozen | Include only if not already live on the Web repo |

### Retire / do not hand as current

- Entire prior ROR line: `editors_ror_consistency2_20261031`, `editors_ror_consistency_20261031`, `editors_ror_multiaff_20261031`, `editors_ror_campus2_20261031`, `editors_ror_campus_20261031`, `editors_ror_fix_post15_20261031`
- Pre-ROR / superseded scale inputs: `editors_backfill_pilot_*`, `editors_backfill_scale_20261031`, `editors_backfill_scale_20261101` (parse input only)
- Older current-board freezes (`editors_t39_final*`, institution-fix packs, blank-rescrape packs, etc.): superseded by the consistency3 panels for anything Web would treat as “current editors”

Full table: `reports/prepublish_check_20261101/B_pack_inventory.csv`.

---

## C. Scale panel QC (`editors_backfill_scale_ror_20261031`)

### Counts and match rate

| metric | value |
|---|---|
| Panel rows | 15,446 |
| Long rows | 11,661 |
| Staff rows | 222 |
| Non-staff with raw affiliation | 11,373 |
| Non-staff matched | 11,013 (96.83%) |
| High / medium / low | 8,704 / 2,244 / 65 |
| Unmatched (with aff) | 360 |
| `ror_match_status` | matched 11,021; unmatched 360; no_affiliation 4,017; staff_excluded 48 |
| Distinct ROR ids | 474 |

By-journal rates: pack file `BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv`. Unmatched strings: `BACKFILL_SCALE_ROR_unmatched_strings_20261031.csv`.

### Panel ↔ `editor_affiliations.csv`

- `affiliation_count` == long part count: **0 mismatches**
- Panel `ror_id` vs long `is_panel_ror=1`: **0 mismatches**
- `other_ror_ids`: **0 real set mismatches**. Panel stores multiple ids with `|`; 17 rows looked like diffs only because of separator. Two Nuffield College rows correctly omit a duplicate Oxford id from `other_ror_ids` (both parts resolve to the same ROR).

### Standing rules

| rule | result |
|---|---|
| System names (Nebraska/Alaska/Hawaii system ids, etc.) | **0** rows still carry the blanked system ROR ids |
| ESSEC → France `02dga6j42` when no Singapore | **21/21** |
| CEU → `02zx40v98` | **5/5** (1 prints Budapest — open country note, kept by prior decision) |
| INSEAD France `00ghzk478` / Singapore `05ynf4333` | **15/15** separated correctly |
| UNSW | Present (39 → UNSW Sydney `03r8z3t63`); no Canberra print in this panel |
| 11KBW | Not in scale journals (core49); present in consistency3 ABDC-A as institution `11KBW` (blank ROR, as before) |
| Names-only journals (AER, AER: Insights, JPE, JOLE, JLE, QJE) | **771** rows; **0** with institution or ROR filled |
| Staff | 8 Data Editor rows matched; 48 `staff_excluded`; rest `no_affiliation` |
| Inactive RORs on panel | **0** active matches to inactive records; 10 Adelaide rows blanked with inactive note (successor open) |

### Source / low-confidence flags

- `source_type` / `source_note` / Wayback fields preserved.
- EJ 2018: inventory note **low confidence (2019 page for 2018)** intact (`status=ok_wayback`).
- Wayback offset / reused-snapshot columns present on inventory.

### Spotcheck (this check)

Sampled 50 matched + 25 unmatched + 25 names-only against `.txt` / Wayback `.html` sidecars (not PDFs).

| bucket | pass | fail |
|---|---|---|
| matched | 49 | 1 |
| unmatched | 25 | 0 |
| names_only | 25 | 0 |

Single fail: **Carlos Alós-Ferrer**, Economic Theory 2021 Wayback HTML — “Carlos”/“Ferrer” present, “Alós” missing from the HTML text layer (encoding). Not a panel invent.

---

## D. Consistency3 QC (`editors_ror_consistency3_20261101`)

| check | result |
|---|---|
| Headers vs consistency2 (all 11 panels) | **identical** |
| Row counts vs consistency2 | **identical** |
| Non-ROR cells changed | **0** |
| `ror_id` rows changed (by file) | ft50 36; ft50_with_ror 36; A* 62; A 89; A+profile 82; B 78; B+profile 72; C 38; prio43 16; ajg2 24; ajg1 7 (matches build log) |
| Residual Nicaragua / Cambodia / ENS Ivory Coast / China Petroleum Indonesia / Los Andes Bolivia / Concordia-US-wrong | **0** |
| Northeastern China `03awzbc87` when China printed | **kept** (40); Boston → `04t5xt781`; bare blanked |
| Victoria Australia `04j757h98` when Australia printed | **kept** (106); Wellington corrections 42 |
| Korea University Tokyo when Tokyo/Japan printed | **1 kept** (correct) |

### Defects

1. **HIGH — missed blank:** `editors_abdc_c_current#2971` (Salil Khetani, `Heidelberg University`) still on Ohio `04rcqnp59`. Same bare-Heidelberg rule blanked elsewhere in C3; this row was missed. **Blank before publish.**
2. **MEDIUM — pre-existing panel↔long desync (~17 rows):** panel `ror_id` set but no long part with `is_panel_ror=1` (e.g. Maryland→College Park with system part `blocked`; Brookings/Kauffman; Georgian Academy; BUPT; LMU). Present in consistency2 already; C3 did not change these cells. Flag to Web; optional follow-up fix pack.

---

## E. Coverage gaps (must show user before publish)

| gap | detail |
|---|---|
| RED 2021–2025 | ScienceDirect bulk-download limit; inventory `blocked`/`queued`; not parsed |
| JBES 2018, 2019, 2020, 2025 | `no_snapshot` (board not in issues; no usable Wayback in window) |
| JRU 2023 | `no_snapshot` |
| JUE 2018–2019 | Only **9** rows/year (2020+ have 48–66) — partial boards |
| EJ 2018 | Low confidence (Oxford 2019 page after Wiley→Oxford move) |
| Names-only / no affiliation | **4,017** `no_affiliation` status rows (AER, Insights, JPE, JOLE, JLE, QJE, plus sparse boards) |
| Open ROR decisions | Virginia University Charlottesville→UVA?; INRA-AgroParisTech; Adelaide / Cergy-Pontoise successors; country-conflict blanks (CEPR Montreal, George Mason “UK”, Imperial “USA”, Sydney “USA”, Notre Dame Paris); ECARES/CORE; Cowles; CEU one Budapest print |

---

## F. Header / column changes to flag to Web

### Scale ROR panel vs scale parse panel

**17 columns added** (none removed):

Inserted before `ror_match_status`:
`institution`, `other_affiliations`, `canonical_name`, `ror_id`, `ror_name`, `ror_country`, `continent`, `lat`, `lon`, `ror_match_method`, `ror_match_score`, `ror_confidence`, `ror_notes`

Appended:
`ror_id_aff_rank`, `primary_aff_basis`, `former_flag`, `other_ror_ids`

Changed existing values:
- `ror_match_status`: new value **`staff_excluded`**
- `affiliation_count`: recomputed on staff/bleed-fix rows
- `editor_row_key`: **8,723 keys shifted** vs prior scale build; crosswalk `editors_backfill_scale_row_key_crosswalk.csv` required

Full header (49 cols):
```
journal_id
journal
year
editor_name
editor_name_raw
role
raw_affiliation
affiliation_imputed
source_url
collection_date
data_source
capture_timestamp
source_note
board_urls
board_url_count
board_status
snapshot_date
snapshot_source
board_year
is_former
former_flag_note
source_file
capture_date
name_style
role_class
parse_flags
institution
other_affiliations
canonical_name
ror_id
ror_name
ror_country
continent
lat
lon
ror_match_method
ror_match_score
ror_confidence
ror_notes
ror_match_status
editor_row_key
affiliation_count
source_type
issue
archive_url
ror_id_aff_rank
primary_aff_basis
former_flag
other_ror_ids
```

`other_ror_ids` separator in this panel: **`|`** (not `;`).

### Consistency3 vs consistency2 / multiaff

- **Header changes: none**
- New `ror_match_method` values: `ror_consistency3_20261101`, `ror_consistency3_20261101_blanked`
- New long-table `ror_match_kind` values: `consistency3_fix`, `consistency3_blank`

### Retired packs for Web

Supersede prior handed ROR/current packs with consistency3; add scale ROR as new multi-year product. Do not publish pilot or pre-ROR scale parse as the public panel.

---

## G. Publish readiness

### Verdict: **GO-WITH-CAVEATS**

Not NO-GO: integrity clean; scale match rate and standing rules hold; consistency3 only touched ROR cells; foreign-namesake cleanup verified.

Caveats before / with publish:
1. Blank the 1 missed Heidelberg Ohio ABDC-C row (or accept and note).
2. Accept known capture gaps (RED/JBES/JRU/JUE partial/EJ2018).
3. Accept open ROR decisions still blank.
4. Flag ~17 panel↔long `is_panel_ror` desyncs as known debt.
5. Flag all header / value / key-crosswalk changes above to Web.

### Exact file set to hand Web (when user says publish)

```
releases/editors_backfill_scale_ror_20261031/
releases/editors_ror_consistency3_20261101/
reports/BACKFILL_scale_ror_20261031.md
reports/ROR_CONSISTENCY3_20261101.md
reports/PREPUBLISH_CHECK_20261101.md
```

(Optional: rankings_* if not already live.)

### Proposed handoff paragraph (do NOT send until user says publish)

> HELD→publish request: two packs superseding the prior ROR/current line. (1) `releases/editors_backfill_scale_ror_20261031/` — multi-year editors panel, 15,446 rows / 39 journals / 301 journal-years, 96.83% ROR match on rows with a printed affiliation; long table `editor_affiliations.csv`; row-key crosswalk included because 8,723 keys shifted after a parse fix. Header adds 13 ROR columns before `ror_match_status` plus `ror_id_aff_rank`, `primary_aff_basis`, `former_flag`, `other_ror_ids` (pipe-separated); new `ror_match_status=staff_excluded`. (2) `releases/editors_ror_consistency3_20261101/` — 11 current FT50/ABDC/AJG panels + long table; headers unchanged vs consistency2; 111 wrong foreign-namesake ROR ids corrected and 429 blanked; new method values `ror_consistency3_20261101` / `_blanked`. Retire consistency2/multiaff/campus/post15 and pilot/scale-parse packs for public current use. Known gaps: RED 2021–25, JBES 2018–20/2025, JRU 2023, JUE 2018–19 partial, EJ 2018 low confidence, ~4k names-only rows, open successor/campus ROR decisions. Pre-publish QC: `reports/PREPUBLISH_CHECK_20261101.md` (GO-WITH-CAVEATS); one recommended pre-hand blank: ABDC-C Heidelberg Ohio residual `#2971`.

---

*Check completed 2026-11-01 Asia/Hong_Kong (UTC+8). Releases untouched.*
