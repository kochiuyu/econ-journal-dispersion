# CHANGES: editors_backfill_red2024_20261114 vs editors_backfill_ra_pack2_20261113

## Added: RED 2024 board (44 people), keys #15873–#15916

The full list is in `RED_2024_board_changes_20261114.csv`. Each row carries a `red_2025_twin_key`.

| Role (as printed) | n | People (printed form) |
|---|---|---|
| CO-ORDINATING EDITOR | 1 | Loukas Karabarbounis |
| EDITORS | 9 | M. Bassetto, M. Doepke, A. Gancia, M. Iacoviello, D. Lagakos, M. de Nardi, E. Schaal, A. Tambalotti, P.-O. Weill |
| ASSOCIATE EDITORS | 30 | S. Albanesi, C. Arellano, M. Azzimonti Renzo, Y. Bai, D. Berger, A. Bhandari, A. Burstein, H. Chade, M. Eden, J. Eeckhout, A.L. Eisfeldt, D. Fitzgerald, J. La'O, J. Lise, M. Mazzocco, L. Paciello, F. Postel-Vinay, P. Restrepo-Echavarria, L. Rudanko, K.J. Ruhl, T. Schoellman, A. Shourideh, V. Sterk, J.K. Thomas, C. Tonetti, M. Trabandt, V. Venkateswaren, G. Vereshchagina, J. Wieland, C. Zimmermann |
| EDITORIAL ADVISORY BOARD | 4 | T.F. Cooley, B. Jovanovic, E.C. Prescott, T.J. Sargent (expanded in `editor_name` as in RED 2021/2025) |

Provenance on every new row:
- `source_url` = `board_urls` = https://www.sciencedirect.com/science/article/pii/S1094202524000061, with `board_url_count` 1;
- `issue` Vol 52 (2024-04); `source_type` official_issue; `board_status` issue_front_matter; `data_source` publisher_issue_pdf_2024;
- `source_note` cites DOI 10.1016/S1094-2025(24)00006-1, page ii;
- method `red_2024_board_20261114`.

ROR: the same institution→ROR map as RED 2025, with the same printed strings. 44 of 44 are matched and 0 are blank.

| ROR | Display name | Rows |
|---|---|---|
| 017zqws13 | University of Minnesota (Twin Cities campus record) | 3 |
| 046rm7j60 | University of California, Los Angeles | 4 |
| 0190ak572 | New York University (incl. Stern, school-unit rule) | 4 |
| 0380n5h16 | Federal Reserve Bank of Minneapolis | 3 |
| 03efmqc40 | Arizona State University | 3 |
| 03n7scr80 | Federal Reserve Bank of Chicago | 2 |
| 02jx3x895 | University College London | 2 |
| 02skhjj30 | Federal Reserve Bank of St. Louis | 2 |
| 0241avf06 | CREI (research centre keeps own ROR) | 1 |
| 04e874t64 | EIEF (research institute keeps own ROR) | 1 |
| 04n0g0b29 | Universitat Pompeu Fabra (Dept of Economics and Business → parent) | 1 |
| 04p491231 | Pennsylvania State University (University Park, as printed) | 1 |
| other 17 ids | one row each | 17 |

## Inventory

RED 2024 row: `queued` → `ok_issue_front_matter`.
- rows_parsed / rows_with_affiliation: 44/44
- `capture_route`: publisher_pdf_capture_institutional
- `source_file`: abs_ajg/reports/RED_2024_editorial_board.pdf (kept unpublished)
- `source_url`: unchanged (the ScienceDirect article URL)

## Gaps

- RED 2024 `queued` → `resolved`.
- 3 lines appended, each with `gap_type=excluded_sed_society_officer_line_excluded` (the same gap_type as 2025):
  - Ellen McGrattan, President
  - Erwan Quintin, Treasurer
  - Marina Azzimonti, Secretary

## Match rates (RED row only)

| | rows_non_staff | with_affiliation | matched | unmatched | match_rate | high |
|---|---|---|---|---|---|---|
| before | 282 | 282 | 281 | 1 | 0.9965 | 234 |
| after | 326 | 326 | 325 | 1 | 0.9969 | 278 |

RED panel rows by board year: 2018 36, 2019 36, 2020 35, 2021 45, 2022 43, 2023 43, **2024 44**, 2025 44.
