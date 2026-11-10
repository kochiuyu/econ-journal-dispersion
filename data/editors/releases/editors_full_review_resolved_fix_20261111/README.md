# editors_full_review_resolved_fix_20261111
Base: releases/editors_full_review_fix_20261111. Inputs (row-level, editor_row_key): institutions_review_resolved_20261111.csv (675: SET_COUNTRY 566, MERGE 97, DROP 7, RENAME 5), then institutions_coinflip_splits_20261111.csv (223 splits; split wins - 0 conflicts). institutions_review_coinflips_20261111.csv not applied.
Resolved: MERGE 97/97, DROP 7/7, RENAME 5/5, SET_COUNTRY 559/566 (6 no-op, 2 11KBW rows protected). Publish rows 1,020 (+17 ft50_current mirror).
Splits: 213 applied, 10 no-op, 0 conflicts.
New RORs (ROR API v2, active, name+country match): 010zh7098 Saint Mary's University (Halifax), 023ahcz89 MPI Comparative & Intl Private Law (Hamburg), 00myn0z94 IRISA (Rennes), 0555ezg60 Huaiyin Inst. of Technology, 05vr1c885 Henan Polytechnic, 00bzdg454 KMA Consulting (Saint Lucia), 05vg74d16 Norwegian Institute of Marine Research, 04k83g518 Concordia University Wisconsin.
Left blank (ROR API 404): 028zh6278 (Mercer), 03jbxjb94 (CTU Prague), 047t3d518 (CY Cergy). Refused system ROR 03ydkyb10 (Wisconsin Extended Campus).
Non-Latin names (Russian, Japanese) keep their printed canonical; RENAME only set country/ROR.
Saint Mary's audit: 05y6c7y19 (Calgary) is on exactly 1 publish row + 1 pilot row + their 2 long rows, all printing 'St. Mary's University, Calgary, Canada' -> correct, kept. No Calgary-ROR rows outside the file.
Directory: 11,426 / 6,387 / 6,387 / 161 / 45 -> 11,330 / 6,396 / 6,396 / 167 / 46.
Pilots byte-identical (au.dk e-mail in pilot #15779 left as-is).
