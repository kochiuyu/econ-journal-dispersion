# HANDOFF: editors_post_review_fix_20261110
Path: `releases/editors_post_review_fix_20261110/`. This freeze is not published and nothing was sent.
- Publish set (9): ft50_current, ft50_current_with_ror, abdc_a_star, abdc_a, abdc_b, abdc_c, ajg prio43, ajg2, ajg1.
- Pilots `abdc_a/b_*_with_profile_pilot` were changed the same way but are not in the publish set.
- Change log: `POST_REVIEW_changes_20261110.csv` (2,944 lines). Skips: `POST_REVIEW_skipped_20261110.csv` (70). Copies are in `abs_ajg/reports/`.
- Expected Directory after copying the 9 publish panels into Web's build (guard 49, scrub patch): 14,195 / 6,379 / 6,379 / 162 / 49.
- Item 8 note: phone numbers were also removed from `editor_name` on 14 abdc_b rows (+ pilot + long). These are junk rows whose "name" was a contact line, e.g. 'Tel: …' → blank, and 'Emma Anderson Phone: 44' → 'Emma Anderson'.
- Pre-existing divergence (not changed here): about 45 publish rows have a raw_affiliation that differs from the Directory copy (e.g. ours 'National Law University' vs printed 'University of Leiden' / 'University of Louisiana, Lafayette'). Also, 6 Directory keys are absent from our files. The 10 audit names on those rows were skipped. This needs a separate approved fix.
