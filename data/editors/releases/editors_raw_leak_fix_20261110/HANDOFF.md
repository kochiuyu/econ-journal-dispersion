# Handoff: editors_raw_leak_fix_20261110
- The Directory should pull every field in RAW_LEAK_directory_diff_20261110.csv (keyed file + editor_row_key): 161 raw_affiliation, 44 canonical, plus the ROR/country/continent/lat/lon fields.
- Residual items:
  - (a) Pilot #15779 faculty_profile_url still contains an au.dk email. It needs a decision to break pilot byte-identity.
  - (b) 5 African Affairs rows were kept with their current institution.
  - (c) 76 restored raws could not be verified online. Each is logged.
  - (d) Qiang Meng: re-check the INFORMS page later.
- QC: ok (see _summary_20261110.json verify).
