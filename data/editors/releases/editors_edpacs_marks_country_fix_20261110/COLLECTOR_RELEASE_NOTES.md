# RELEASE NOTES — editors_edpacs_marks_country_fix_20261110

**When (Asia/Taipei):** 2026-11-10 15:29 Asia/Taipei
**Base:** `editors_paren_num_leftover_fix_20261110` (PR #50)

## (a) Norman Marks (`editors_abdc_c_current#12402`, EDPACS)
The printed raw_affiliation and the long raw_aff_part are blanked; the editor row is kept. The original bio text is kept as a trace in the panel ror_notes and the long ror_match_note.

## (b) Country + continent (no ROR)
- `editors_abdc_c_current#12412` Aditya Birla Group → India / Asia
- `editors_abdc_c_current#12391` New York State Comptroller → United States / North America

Left blank (unverifiable). The EDPACS board page (https://web.archive.org/web/20250529200822/https://www.tandfonline.com/journals/uedp20/about-this-journal, “Updated 19-05-2025”) and the preserved credential strings give no location for:
- `editors_abdc_c_current#12398` Jim Kaplan — AuditNet LLC
- `editors_abdc_c_current#12411` George Spafford — Pepperweed
- `editors_abdc_c_current#12393` Gary Hinson — IsecT Ltd.
- `editors_abdc_c_current#12390` Ulrich Hahn — auditline

## (c) Long raw_aff_part = 'no'
The 8 EDPACS rows edited in PR #50 (#12387, #12390, #12392, #12393, #12398, #12405, #12411, #12412) had raw_aff_part 'no', taken from the affiliation_imputed flag column because their panel raw_affiliation is blank. They are set to '' to match the panel; aff_text_source is unchanged. This follows the existing convention for blank-raw rows (affiliation_imputed + '').
Not fixed: the same artifact exists across the long file (13,723 rows with aff_text_source=affiliation_imputed, almost all 'no', including other EDPACS rows such as #12375/#12381/#12384/#12397/#12401). It is systemic and is left for a separate pass.

## Verification
- ok: True; row counts unchanged: True; header/EOL changes: []
- unlogged changes: 0; ROR / is_panel_ror changes: 0; protected changed: 0
- panel↔long desync (touched keys, incl. raw): 0
- ajg1: 12316 published + 10 nav rows (untouched); pilots byte-identical: {'editors_abdc_a_current_with_profile_pilot.csv': True, 'editors_abdc_b_current_with_profile_pilot.csv': True}; other publish panels byte-identical: True
- 11KBW True; UNSW Sydney True; INSEAD FR+SG True
