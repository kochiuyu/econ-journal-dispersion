# HANDOFF: editors_current_leftovers_20261112 (UNPUBLISHED)

- **Base:** editors_leftover_fixes_20261112 (Directory PR #69, 59652942). Web main is now c4d24a7, which only adds icons and CSS, so the data is identical. verify ok.
- **D (name-field leftovers, checked against the official board pages):**
  - European Transport: Carboni → Politecnico di Torino 00bgk9508; Medeghini → Brescia Mobilità (no ROR, Italy). Phantoms #15765 and #15761 dropped.
  - JMID: Biró → HAS 02ks8qq67; Izmalkov → NES 033904843; Klijn → UAB 052g8jq94; Koshevoy → RAS 05qrfxd25; Ünver → Boston College 02n2fzt79. Their 5 phantom rows dropped.
  - JMID: 12 more non-person rows dropped (a section header, site-policy links, a sentence fragment, article titles).
- **E (school-unit rule):** 27 rows rematched to API-active catalog RORs, either the school's own ROR or the parent named in the printed school. raw_affiliation is left as printed.
- **F:** 68 missing countries filled from the printed final country token. No ROR was assigned.
- **Directory:** 11,074 → 11,065 institutions. With ROR 6,698 → 6,698; distinct ROR 6,698; countries 169; shared names 43.
- **Required `build_site.py` change** (AJG_GAP_FILES, ajg1 tuple): expected_dropped `15` → `32`. Without it the build fails with "editors_abs_ajg_gap_ajg1_current.csv dropped 32 names, expected 15". The shared-name guard stays at 43.
- **Files to publish:** the 9 panels plus editor_affiliations.csv. The pilots are unchanged.

Collector did not open a PR, publish, or message anyone.
