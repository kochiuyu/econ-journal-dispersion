# CNRS Section 37 rankings freeze

- **Freeze path:** `/workspace/econ-journal-editors/releases/rankings_cnrs_20261024`
- **Built (Asia/Hong_Kong):** 2026-10-25T00:10:18+08:00
- **Source:** CNRS Section 37 *Catégorisation des revues en Économie et en Gestion* PDFs
  mirrored on Vallorem (`classements-cnrs`). Dauphine direct URL was under maintenance.
- **Discontinued:** Section 37 discontinued maintaining this list (motion Dec 2020);
  final published edition in this freeze is **June 2020**.
- **Ratings:** categories as published: `1`, `1e`, `1g`, `1eg`, `2`, `3`, `4`
  (`rating` = `rating_raw` = category string; letter suffixes preserved).
- **Raw PDFs:** private under `/workspace/econ-journal-editors/rankings_raw/cnrs/` (not in freeze).

## Editions

| Year | Rows | Matched | Match % | Source file |
|---|---:|---:|---:|---|
| 2011 | 793 | 653 | 82.3% | `cnrs_2011_10.pdf` |
| 2012 | 794 | 655 | 82.5% | `cnrs_2012_06.pdf` |
| 2013 | 798 | 657 | 82.3% | `cnrs_2013_11.pdf` |
| 2014 | 818 | 675 | 82.5% | `cnrs_2014_11.pdf` |
| 2015 | 827 | 683 | 82.6% | `cnrs_2015_11.pdf` |
| 2017 | 826 | 684 | 82.8% | `cnrs_2017_12.pdf` |
| 2018 | 831 | 694 | 83.5% | `cnrs_2018_11.pdf` |
| 2019 | 834 | 702 | 84.2% | `cnrs_2019_06.pdf` |
| 2020 | 840 | 713 | 84.9% | `cnrs_2020_06.pdf` |

- **Long panel rows:** 7361
- **Conflicts (same ISSN, differing cat within edition):** 26
- **Unmatched rows:** 1245

## Mapping

- ISSN normalize → FT50 / core49 / ABDC catalogs; title fallback.
- Primary journal_id prefers FT50 then core49 then ABDC A*/A/B/C.
- No invented journal_ids or ratings.


## Source notes / blockers

- Dauphine URL `Categorisation37-Liste-Juin-2020.pdf` returned a maintenance HTML page (not used).
- Vallorem `classement-cnrs-2018-11_…pdf` downloaded corrupted (broken xref); replaced with Coactis mirror
  `https://coactis.org/wp-content/uploads/sites/13/2022/05/CNRS_classement-2018.pdf` (Nov 2018 / v5.04).
- No OCR needed: all ingested PDFs are text-extractable via `pdftotext`.
- Editions ingested: 2011, 2012, 2013, 2014, 2015, 2017, 2018, 2019, 2020 (2016 and 2010 not separately frozen;
  Vallorem “10-2010” link maps to the Oct 2011 PDF we labeled 2011).
