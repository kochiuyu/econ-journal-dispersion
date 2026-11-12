# HANDOFF — editors_backfill_red_jbes_20261113 (HELD; not published, no PR)

For Journal-Editor-Web: replace live core49 `editors_backfill_red_gap_20261112` with this freeze. It adds RED 2025 and JBES 2019/2020.

Publish these data files:
- the panel, long, inventory, gaps, match_rates and staff_rows CSVs, plus the other unchanged CSVs;
- `RED_2025_board_changes_20261113.csv`, `JBES_2019_board_changes_20261113.csv`, `JBES_2020_board_changes_20261113.csv`;
- `jbes_20{19,20}_board_extracted.csv`, `jbes_20{19,20}_front_matter_extract.txt`, `red_2025_board_extracted.csv`;
- the transcripts `*.md`, README, RELEASE_NOTES, `_build.json`, the scripts and the log.

**Do NOT publish the source PDFs** (`JBES_2019_editorial_board.pdf`, `JBES_2020_editorial_board.pdf`). Their front matter prints staff contact email and phone lines. They are included here only as evidence. The transcribed and extracted files carry no contact data ([email removed]).

Checks to repeat after publishing:
- panel 15,873 / long 12,102;
- keys #15664–#15872 unique;
- JBES 2019/2020 inventory ok_issue_front_matter 87/84 and 78/75;
- match_rates JBES 0.9302.

Directory and `build_site.py`: no change. The Directory does not read core49.

Open, not touched: RA pack 2 (S21 EUI, S22 RED 2024, S23 JBES 2025, FIX06), the pilots and the user-decision items.
