# HANDOFF: editors_backfill_red_gap_20261112 (UNPUBLISHED, core49 backfill)

- **Base:** the live core49 `editors_ra_ta_merge_rebuild_20261112` (web 59652942), with the web's scrubbed spotcheck.
- **What changed:**
  - RED 2021 inventory set to ok_issue_front_matter 45/45.
  - RED 2022 and RED 2023 boards added: 43 + 43 rows (#15578–#15663), with matching long rows.
  - gaps and match_rates rows updated.
- **Files to publish** into data/editors/core49/releases/: `editors_backfill_scale_ror_panel.csv`, `editor_affiliations.csv`, `editors_backfill_scale_inventory.csv`, `editors_backfill_scale_gaps.csv`, `BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv` and `RED_2022_2023_board_changes_20261112.csv`. The other files are identical to the live copy.
- **No build_site change needed** (the Directory does not read core49).
- **Held:** RED 2025, JBES 2019 and JBES 2020 (sources need a browser or CUHK login; see README).

Collector did not open a PR, publish, or message anyone.
