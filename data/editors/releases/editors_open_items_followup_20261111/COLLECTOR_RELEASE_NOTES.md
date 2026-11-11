# editors_open_items_followup_20261111 (built 2026-11-11 07:59, Asia/Taipei; UNPUBLISHED)

Base: `releases/editors_open_items_fix_20261111` (live via PR #56, 89aa2f09). Four user-approved items only, relayed by Econ-Journal-Web. Keyed on editor_row_key. No raw-text edits. Pilots byte-identical. Script: `open_items_followup_20261111.py`.

## 1. abdc_b#16107 Aaron Shenhar
Printed: `Rutgers University (Ret.), CEO Diamond Leadership Institute, Israel` (unchanged).
- Before: Rutgers, The State University of New Jersey, 05vt9qd57, United States.
- After: Diamond Leadership Institute, no ROR, Israel (Asia).
- (Ret.) is treated as a former employer. No ROR was invented for Diamond Leadership Institute. That name did not already exist as a panel institution, so a new no-ROR institution was created with country Israel. Long table synced (ROR blanked, country Israel).

## 2. abdc_b#39063 Gerry Bates
Printed raw left unchanged: `independent consultant in environmental law and policy; specialist courses at The University of Sydney and UNSW Australia`.
- Not dropped. Institution is no longer "independent consultant…".
- Before: canonical "independent consultant in environmental law and policy", no ROR, no country; `affiliation_count=2`, `other_ror_ids=https://ror.org/03r8z3t63`.
- After: The University of Sydney, 0384j8v12 (API-verified active; Australia, Oceania, lat/lon from the existing catalog entry). `ror_id_aff_rank=1`. `affiliation_count` still 2; `other_ror_ids` still UNSW 03r8z3t63.
- Long table already had two parts, so no row was added (panel and long-table row counts unchanged, 269,545 long rows):
  - aff_rank 1: raw_aff_part still the consultant + Sydney clause; now Sydney 0384j8v12, is_panel_ror=1, aff_role unknown (the printed board text does not state a role; existing ror_notes already record the Sydney Law adjunct appointment).
  - aff_rank 2: `UNSW Australia`, 03r8z3t63, is_panel_ror=0, aff_role unknown — left in place. The UNSW institution master entry was not renamed, merged, or otherwise altered (audit: every panel row whose ror_id is 03r8z3t63 is byte-identical to base).

## 3. ft50 #4634 (both rows)
Institution remains Xi'an Jiaotong University, 017zhmm22, China. Faculty URL and person key were already blank.
- Also cleared `faculty_match_method` (was masthead_href) and `faculty_match_confidence` (was high), matching every other FT50 row with a blank profile URL.
- #4501 was not touched (still CEIBS, with the CEIBS profile URL and match fields).

## 4. Former employers
- Nielsen, abdc_a#42676, printed `Consultant (former Chief Research Officer, Nielsen), USA` (unchanged). Before: Nielsen (United States) 016x3qj75, United States. After: no canonical name, no ROR, country United States kept (North America). This was the only panel row on that ROR.
- GM, ajg1#4303, printed `GM (retired), USA`. Already on General Motors (United States) 05addee68, United States. API re-check: active, name GM / General Motors (United States), United States. Left unchanged.
- SEARCA, abdc_c#15559, printed `Independent consultant (formerly SEARCA Knowledge Management Department Head)` (unchanged). Before: SEARCA 04qf4zf50, Philippines. After: no canonical name, no ROR, no country. The other SEARCA row, #15558, is unchanged and still carries 04qf4zf50.

Because raw affiliation was left intact (none of these is a Marks-style drop), the Directory still displays Nielsen and SEARCA #15559 under their printed-text labels. Appointments without an institution stayed at 13,413.

## Directory (Web build on a copy)
- before: 11,185 / 6,697 / 6,697 / 169 / 43 (reproduces the live counts)
- after:  11,186 / 6,696 / 6,696 / 169 / 43
- Shared-name guard stays 43; no change needed.
- Net +1 institution: new Diamond Leadership Institute; "independent consultant…" removed (now Sydney, already present). With-ROR −1: Nielsen's ROR was the only copy of 016x3qj75.

## QC: ok
- Row counts, headers and line endings unchanged. Long table 269,545 rows. AJG1 12,326 (nav 10 untouched), AJG2 5,462, FT50 10,049/10,049. Pilots byte-identical.
- No raw edits. 0 invented RORs. UNSW / 11KBW / INSEAD FR+SG protected. No non-Latin names lost; no near-miss pairs. 0 emails or phones.
- Panel–long mismatches: 0 on changed rows; 884 on the full table (same as base).
