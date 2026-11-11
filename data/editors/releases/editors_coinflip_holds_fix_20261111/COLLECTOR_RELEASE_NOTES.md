# editors_coinflip_holds_fix_20261111 (built 2026-11-11 08:34, Asia/Taipei; UNPUBLISHED)

Base: `releases/editors_nielsen_searca_drop_20261111` (live via PR #58, 83f6a1a7).
Input: `/workspace/institutions_coinflip_holds_20261111.csv` (187 rows) and its .md summary.
User-approved, relayed by Econ-Journal-Web. Keyed on editor_row_key. No raw-text edits. Pilots byte-identical.
Script: `coinflip_holds_fix_20261111.py`.

All 30 target RORs in the file were re-checked active in ROR API v2 on 2026-11-11; name and country fit in every case. The approved specifics matched the file (0 differences). NIT Hamirpur 01nc8zs04 was confirmed active with country Bangladesh and was not in the file, so it was not applied. Saint Mary's was not in the file; no Halifax row was moved.

## Applied 158 / 187 (29 already at the official campus name and ROR — all of them ft50_current slim twins with no canonical_name column)

| Group | File rows | Applied | Already at target |
|---|---:|---:|---:|
| Illinois UIUC 047426m28 | 30 | 25 | 5 (ft50 slim) |
| Illinois Chicago 02mpq6x41 (Hagen ×3, Thomas Lee ×1) | 4 | 3 | 1 (Hagen ft50 slim) |
| James Madison 028pmsz77 | 3 | 3 | 0 |
| Massey 052czxv31 | 3 | 3 | 0 |
| AUE 056c6h780 | 2 | 2 | 0 |
| Naples Federico II 05290cv24 | 4 | 4 | 0 |
| Pacífico Lima 05mmg7t28 | 3 | 3 | 0 |
| Concordia Irvine (Hanson) 0028kf729 | 2 | 2 | 0 |
| Concordia Montreal (Kryzanowski) 0420zvk78 | 1 | 1 | 0 |
| UNC Chapel Hill 0130frc33 | 50 | 35 | 15 |
| UW–Madison 01y2jtd41 | 27 | 22 | 5 |
| UT Austin 00hj54h04 | 19 | 18 | 1 |
| UT Dallas / El Paso / Tyler | 2+1+2 | 2+1+2 | 0 |
| UMass Amherst 0072zz521 | 7 | 5 | 2 |
| IIT Delhi/Kharagpur/Kanpur/Madras/Bombay | 4+3+2+1+1 | same | 0 |
| IIM Udaipur/Bangalore/Lucknow | 1+1+1 | same | 0 |
| Newcastle UK / Newcastle Australia | 2+2 | same | 0 |
| VNU Hanoi, HSE, Paris-Saclay, UTech Jamaica | 4+2+1+2 | same | 0 |
| NIT Hamirpur 01nc8zs04 | 0 in file | — | — (API country Bangladesh; not applied) |

20 University of Texas rows that still carried the system ROR 01gek1696 were moved to the evidenced campus (Austin, Dallas, El Paso or Tyler). That is campus evidence, so the system-ROR guard did not block them.

Rows not in the file were left as printed, including unplaced editors, genuine two-place strings, and Saint Mary's (already Halifax 010zh7098). Diamond Leadership Institute and the Nielsen/SEARCA dropped rows were not in the file and are unchanged.

New ROR on the panels (API-verified): Concordia University Irvine 0028kf729, United States. The other 29 targets were already in the catalog.

## Directory (Web build on a copy)
- before: 11,184 / 6,696 / 6,696 / 169 / 43 (reproduces the live counts)
- after:  11,175 / 6,698 / 6,698 / 169 / 43
- Shared-name guard stays 43; no change needed.
- Appointments without an institution stayed at 13,415.
- Institutions fell by 9 as generic names were merged into confirmed campus entries. With-ROR rose by 2 (including the new Irvine ROR).

## QC: ok
- Row counts, headers and line endings unchanged. Long table 269,545 rows. AJG1 12,326 (nav 10 untouched), AJG2 5,462, FT50 10,049/10,049. Pilots byte-identical.
- No raw edits. 0 invented RORs. Protected names intact. No non-Latin names lost; no near-miss pairs. 0 emails or phones.
- Panel–long mismatches: 0 on changed rows; 882 on the full table (884 in the base).
