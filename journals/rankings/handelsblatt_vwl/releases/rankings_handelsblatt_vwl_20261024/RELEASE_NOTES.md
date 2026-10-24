# Handelsblatt / VWL (Forschungsmonitoring) rankings freeze

- **Freeze path:** `/workspace/econ-journal-editors/releases/rankings_handelsblatt_vwl_20261024`
- **Built (Asia/Hong_Kong):** 2026-10-25T00:06:41+08:00
- **Current source:** Forschungsmonitoring VWL journal weights
  (`https://www.forschungsmonitoring.org/ranking/vwl/`) — file
  `VWL_Zeitschriftenliste.xlsx` (sheets `SJR main`, `SJR Classes`).
  This is the current Handelsblatt-style VWL journal-weight list.
- **Historical:** Handelsblatt VWL Ranking 2015 journal list PDF
  (`handelsblatt-liste_2015.pdf`, HB-Gewicht bands 1 / 0.6 / 0.3 / …).
- **Methodology PDF (private raw):** `Description_VWL_Main_Journal_weights.pdf`
  — continuous weights relative to top-5 SJR mean; documented class bins A+…F.

## Columns

- `weight` — continuous SJR-based weight (xlsx) or HB-Gewicht (2015 PDF).
- `rating_raw` — same numeric weight as string.
- `rating` — documented SJR class bin (A+, A, B, C, D, E, F) when available from
  `SJR Classes`; blank for HB 2015 PDF rows (no invented bins).

## Coverage

- **SJR_main years:** 1998–2020 (23 years)
- **SJR_main long rows:** 40871
- **HB2015 PDF rows:** 1607
- **Total long rows:** 42478

| Year | Rows | Matched | Match % | Notes |
|---|---:|---:|---:|---|
| 1998 | 1777 | 882 | 49.6% | SJR_main |
| 1999 | 1777 | 882 | 49.6% | SJR_main |
| 2000 | 1777 | 882 | 49.6% | SJR_main |
| 2001 | 1777 | 882 | 49.6% | SJR_main |
| 2002 | 1777 | 882 | 49.6% | SJR_main |
| 2003 | 1777 | 882 | 49.6% | SJR_main |
| 2004 | 1777 | 882 | 49.6% | SJR_main |
| 2005 | 1777 | 882 | 49.6% | SJR_main |
| 2006 | 1777 | 882 | 49.6% | SJR_main |
| 2007 | 1777 | 882 | 49.6% | SJR_main |
| 2008 | 1777 | 882 | 49.6% | SJR_main |
| 2009 | 1777 | 882 | 49.6% | SJR_main |
| 2010 | 1777 | 882 | 49.6% | SJR_main |
| 2011 | 1777 | 882 | 49.6% | SJR_main |
| 2012 | 1777 | 882 | 49.6% | SJR_main |
| 2013 | 1777 | 882 | 49.6% | SJR_main |
| 2014 | 1777 | 882 | 49.6% | SJR_main |
| 2015 | 3384 | 1535 | 45.4% | SJR_main (1777) + HB2015 PDF (1607) |
| 2016 | 1777 | 882 | 49.6% | SJR_main |
| 2017 | 1777 | 882 | 49.6% | SJR_main |
| 2018 | 1777 | 882 | 49.6% | SJR_main |
| 2019 | 1777 | 882 | 49.6% | SJR_main |
| 2020 | 1777 | 882 | 49.6% | SJR_main |

- **Unmatched rows:** 21539
- **Conflicts:** 0

## Mapping

- ISSN normalize (xlsx ISSNs are unhyphenated) → FT50 / core49 / ABDC;
  title fallback (especially for HB2015 PDF, which has no ISSN).
- No invented journal_ids or weights.

## Raw files (private)

- `/workspace/econ-journal-editors/rankings_raw/handelsblatt_vwl/`

## Warnings

- (none)
- RUB/historical 2013 PDF was not reliably fetchable in this run; SJR_main covers 2013.
