# RELEASE NOTES — editors_paren_num_leftover_fix_20261110

**When (Asia/Taipei):** 2026-11-10 14:49 Asia/Taipei
**Base:** `editors_tokyo_other_inst_fix_20261110` (PR #49, 2f69435f)

## 0. Tokyo blank-ROR geo restore (12 rows)
ror_country Japan and continent Asia restored on the 11 Tokyo Institute of Technology rows and Kojima “Tokyo”. Done in the panel and in the long file (ror_country), to match the Directory. ROR stays blank.

## 1–5. User-approved fixes (13 rows)
- `editors_abdc_a_current#34068` Hendrik Haag: ORG_ONLY → canonical “Hengeler Mueller”, no ROR, Germany
- `editors_abdc_c_current#12387` Chris Dunn: ORG_ONLY → canonical “C.H. Dunn Consulting”, no ROR, Canada
- `editors_abdc_c_current#12390` Ulrich Hahn: ORG_ONLY → canonical “auditline”, no ROR
- `editors_abdc_c_current#12391` David R. Hancox: ORG_ONLY → canonical “New York State Comptroller”, no ROR
- `editors_abdc_c_current#12392` Peter Hillier: ORG_ONLY → canonical “CMA Holdings Inc.”, no ROR, Canada
- `editors_abdc_c_current#12393` Gary Hinson: ORG_ONLY → canonical “IsecT Ltd.”, no ROR
- `editors_abdc_c_current#12398` Jim Kaplan: ORG_ONLY → canonical “AuditNet LLC”, no ROR
- `editors_abdc_c_current#12402` Norman D. Marks: DROP → canonical “”, no ROR
- `editors_abdc_c_current#12405` Sridhar Ramamoorti: ORG_ONLY → canonical “Grant Thornton”, no ROR, United States
- `editors_abdc_c_current#12411` George Spafford: ORG_ONLY → canonical “Pepperweed”, no ROR
- `editors_abdc_c_current#12412` N.G. Shankar: ORG_ONLY → canonical “Aditya Birla Group”, no ROR
- `editors_abdc_c_current#16656` Balázs Égert: REMATCH → canonical “OECD”, ROR https://ror.org/0438wbg98, France
- `editors_abs_ajg_gap_ajg1_current#7504` Neha Gangwar: REMATCH → canonical “Guru Gobind Singh Indraprastha University”, ROR https://ror.org/034q1za58, India

Notes:
- Printed raw_affiliation and raw_aff_part are unchanged everywhere, and existing ror_notes (including guardrail notes) are kept. A `paren_num_leftover_fix_20261110` note is appended, carrying the previous printed canonical.
- The EDPACS rows have a blank raw_affiliation. Their printed credential string was only in canonical_name, so it is preserved in the appended ror_notes and in the change log.
- Grant Thornton joins the existing unmatched form ('Grant Thornton', 'United States', 'North America', '', ''). Auditline: no existing form on panels → 'auditline'.
- OECD row uses the most common OECD canonical on the panels (“OECD”) with the base twin ror_name/country/geo. The long part 1 is now the panel ROR; part 2 (Paris Nanterre `013bkhk48`) is unchanged.
- Marks DROP: canonical, ROR and geo are blank, and the printed raw bio is kept as instructed. The site display therefore falls back to the raw bio unless Web suppresses it.
- Unchanged by design: 1 Decembrie 1918 University, 11KBW, 39 Essex Chambers, 3 Hare Court, 5 Wentworth Chambers, 11powerN, 125th Street BID, 2050 Alliance, 2W China, 3s Research, 505 Savjetovanje, 53NG, 55 Capital Partners, 720 Strategies.

## Verification
- ok: True
- invented ROR: []; row counts unchanged: True (ajg1 12326 in freeze = 12,316 published + 10 nav rows not in the Directory and untouched; ajg2 5462); long line count unchanged: True
- unlogged/non-institution field changes: 0; raw changed: 0; header/EOL changes: []
- panel↔long desync: 0; protected changed: 0; keep-list rows touched: []
- 11KBW True; UNSW Sydney True; INSEAD FR+SG True; pilots byte-identical: {'editors_abdc_a_current_with_profile_pilot.csv': True, 'editors_abdc_b_current_with_profile_pilot.csv': True}
- Directory name mismatches: none; keys not found: none
