# SHUFE Tenure-Track Journal List rankings freeze

- **Freeze id:** `rankings_shufe_20261025`
- **Freeze path:** `/workspace/econ-journal-editors/releases/rankings_shufe_20261025`
- **Built (Asia/Hong_Kong):** 2026-10-25T19:05:57+08:00
- **Source URL:** https://econen.sufe.edu.cn/6619/list.htm
- **Source file (private raw):** `rankings_raw/shufe/sufe_tenure_track_list.htm` (not in freeze / not in public monorepo)
- **Page title:** SUFE Tenure-Track Journal List (economics)
- **edition_year:** empty string — no edition year printed on the source page.
  List vintage unknown; **retrieved_date=2026-10-25** (Asia/Hong_Kong calendar date of scrape).
  Do not treat empty edition_year as 2026 list vintage.
- **source_note:** `SHUFE tenure-track list retrieved 2026-10-25`
- **Ratings (page vocabulary, `rating` = `rating_raw`):**
  `Top Tier`, `First Tier`, `Second Tier`, `Third Tier`
- **PII:** Contact Us phone/fax/email and “Project supported by …” grant lines on the
  source page are **excluded** from this freeze. No emails or phone numbers appear in
  freeze CSVs.

## Counts

| Tier | Rows |
|---|---:|
| Top Tier | 5 |
| First Tier | 20 |
| Second Tier | 39 |
| Third Tier | 59 |
| **Total** | **123** |

- **Matched (journal_id set):** 120 / 123 (97.6%)
- **Unmatched rows:** 3
- **Conflicts (same title, differing tier):** 0

## Mapping

- Title normalize → FT50 → core49 → ABDC A*/A/B/C catalogs (same priority as CNRS/Stern).
- No ISSNs on source page → title / alias+title match only.
- No invented journal_ids or ratings.
- **AER Papers and Proceedings** left unmatched (same policy as Stern Economics memo for
  AEA Papers & Proceedings — do not invent a map onto AER).
- Manual title aliases (page → catalog title):
  - Economic Journal → The Economic Journal
  - Journal of Economic History → The Journal of Economic History
  - Journal of Industrial Economics → The Journal of Industrial Economics
  - Journal of Economic Education → The Journal of Economic Education
  - Economic Record → The Economic Record
  - World Bank Economic Review → The World Bank Economic Review
  - Oxford Economics Papers → Oxford Economic Papers
  - International Monetary Fund Economic Review → IMF Economic Review
  - World Economy → The World Economy
  - Economics of Transition → Economics of Transition and Institutional Change (rename)
  - Industrial and Labor Relations Review → ILR Review (Industrial and Labor Relations Review)
  - Industrial Relations → Industrial Relations: a journal of economy and society
  - Economic History Review → The Economic History Review: a journal of economic and social history
  - Economic Policy → Economic Policy: a European forum
  - Theory and Decision → Theory and Decision: an international journal for multidisciplinary advances in decision sciences
  - Canadian Journal of Economics → Canadian Journal of Economics / Revue Canadienne D'Economique
  - The B.E. Journal of … → The BE Journal of … (punctuation / catalog spelling)
  - Journal of Law Economics & Organization → Journal of Law, Economics and Organization
  - Left unmatched (no invent): AER Papers and Proceedings; Economic Research Journal; Social Sciences in China

## Files

- `shufe_long.csv` / `shufe_current.csv` — one row per journal (identical; single page snapshot)
- `journal_id_crosswalk.csv` — primary + secondary catalog hits
- `unmatched_journals.csv`
- `conflicts.csv` (header only if none)
- `RELEASE_NOTES.md`
