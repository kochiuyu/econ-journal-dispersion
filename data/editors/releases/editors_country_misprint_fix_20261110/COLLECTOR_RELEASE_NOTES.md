# RELEASE NOTES — editors_country_misprint_fix_20261110

**When:** 2026-11-10 20:53 Asia/Taipei
**Base:** `editors_trailing_country_fix_20261110` (Directory PR #53 pending)
**Script:** `abs_ajg/scripts/country_misprint_fix_20261110.py`

## Fix 1 — misprinted countries
- Scope: Web's 24 Institutions plus 3 unambiguous extras from the scan.
- Matching: rows are matched on the Directory display key and the listed wrong country. `ror_country` and `continent` are set to the real country, and the long table's `ror_country` follows on the matching part.
- Totals: 30 publish rows, 19 pilot rows and 49 long rows across 27 Institutions.
  - Web list: 26 publish rows, 16 pilot rows and 42 long rows.
  - Scan extras: 4 publish rows, 3 pilot rows and 7 long rows.
- Extras:
  - Richmond American University London, ajg1 #1758: US → UK.
  - The Ivey Business School at Western University Canada, abdc_a #22532: Germany → Canada.
  - Xian Jiaotong-Liverpool University, China, abdc_b #39658 and #39666 (printed 'China-UK'): UK → China.
- Imperial College of London, abdc_c #17649: rematched to the existing panel ROR https://ror.org/041kmwe10 Imperial College London (255 base rows). It is the exact normalized-name twin. canonical, ror_name, geo and lat/lon are copied from the panel, and long ror_id/ror_name/is_panel_ror are set.
- University of New South Wales, abdc_c #17506 (Indonesia → Australia):
  - Its ROR stays blank. No wrong ROR is assigned, and UNSW Sydney 03r8z3t63 is intact elsewhere.
  - Scan extra: the twin row abdc_b #26907 plus its pilot (printed 'University of New South Wales, UK', country blank) is set to Australia.

## Fix 2 — fragment canonicals (raw never edited)
- Court of Appeal of England and / Court of Appeal, England and / Lord Justice of Appeal, Court of Appeal of England and → 'Court of Appeal of England and Wales' (UK).
- Justice of the Supreme Court, England and → 'Supreme Court of the United Kingdom' (UK).
- Greece and / Italy & / Finland and / Solicitor, Australia, New Zealand and → canonical blank, ROR blank, country and continent blank. Each raw names two or more countries and no organisation.
- SE → canonical blank, printed country UK kept.
- Independent Scholar, UK and / Independent Scholar - Iran & (scan extra) → 'Independent Scholar', country blank (two countries).
- Totals: 11 publish rows, 8 pilot rows and 9 long rows across 11 Institutions. The scan extra accounts for 1 publish, 1 pilot and 2 long rows.
- **Note:** with the canonical blank, the Directory display falls back to the printed raw. 'Greece and UK', 'Italy & UK', 'Finland and Tanzania', 'SE, UK' and the Solicitor string therefore show as Institutions with no country, as they did before the trailing pass. Removing them needs a Web-side rule for multi-country-only strings, or an approved DROP.

## Fix 3
- 'University of the North, Barranquilla, .' (abdc_c #5115) → 'University of the North, Barranquilla'. It merges with its twin #5152, which is unmatched, so no ROR is copied. Totals: 1 publish row, 0 pilot rows, 0 long rows.

## Directory (Web build, read-only)
- before: Aggregates: 2,853 journals (2,426 with a field, 2,835 with a board link), 15,165 institutions (6,387 with ROR, 69 shared names), 12,068 appointments without an institution
- after: Aggregates: 2,853 journals (2,426 with a field, 2,835 with a board link), 15,159 institutions (6,387 with ROR, 69 shared names), 12,068 appointments without an institution
- The before base is the Directory copy plus the trailing_country edits (PR #53 simulation).
- Countries: 162 → 162.

## QC (ok=True)
- ROR: invented []; existing ror_id changed 0.
- Protected orgs: protected rows changed 0; 11KBW True; UNSW True; INSEAD FR+SG True.
- Raw text: raw_affiliation changed 0; raw_aff_part changed 0.
- Unexpected diffs: panel 0, long 0. Panel↔long desync: 0.
- Format: header/EOL changes []; row counts unchanged True.
- Sizes: AJG1 12326 rows (10 nav rows untouched), AJG2 5462, long 269539.
- Pilots: changed by design, not for publish. Working panels match the freeze: True.
