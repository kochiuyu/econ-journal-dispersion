# Docs / codebook (placeholder)

Stable join keys used across universes and streams:

| Key | Meaning |
|-----|---------|
| `journal_slug` | Canonical journal id (core49 catalog); FT50/ABDC use `journal_id` in those catalogs — map via overlap columns where present |
| `journal_id` | Top 5 (`journals/catalog_top5.csv`) joins to `catalog_ft50.csv`. UTD24 (`journals/catalog_utd24.csv`) joins to the FT50 catalog, except `informs_journal_computing`, which joins to ABDC A. ABS/AJG rows in freeze `rankings_abs_ajg_20261024`, and the Tilburg, FNEGE, ERIM, Stern, Shanghai, and SHUFE freezes `rankings_tilburg_20261025`, `rankings_fnege_20261025`, `rankings_erim_20261025`, `rankings_stern_20261025`, `rankings_shanghai_20261025`, and `rankings_shufe_20261025`, carry the freeze’s primary catalog id (FT50, core49, or ABDC); empty means unmatched. AJG-gap editor rows (`data/editors/abs_ajg_gap/releases/current/`) use the collector slug in `journal_id`; that slug matches an ABDC catalog id only for a handful of titles |
| `year` | Calendar / cover year of the board or article window |
| `doi` | Article DOI when available (affiliations / author panels) |

Full variable dictionary will land here as releases freeze. Until then, see column headers in each `releases/` CSV and the stream `STATUS.md` files.

## Editor-panel columns added in `editors_single_editor_20261029`

Every current editor CSV under `data/editors/*/releases/current/` has these two columns next to each other (they were the last two columns until `editors_ror_consistency3b_20261101`). `scripts/build_site.py` selects columns by name and does not write either one to the site. `source_url` stays the primary board link.

| Column | Meaning |
|--------|---------|
| `board_urls` | Public board-page URLs, separated by `\|`. A single URL may be filled on any journal (from `editors_ror_consistency3b_20261101`). A multi-URL list is filled only when that journal's board spans more than one page: IEEE Transactions on Intelligent Transportation Systems, Acta Turistica, Management: Journal of Contemporary Management Issues, and PASOS Journal of Tourism and Cultural Heritage; and, from `editors_browser_single_20261029`, Journal of Derivatives and Journal of Portfolio Management; and, from `editors_ror_consistency3b_20261101`, German Economic Review, British Journal of Management, International Journal of Management Reviews, Sydney Law Review, Journal of Korea Trade, International Journal of Small and Medium Enterprises, and BFuP Betriebswirtschaftliche Forschung und Praxis. Blank elsewhere |
| `board_url_count` | Number of URLs in `board_urls`. Blank when `board_urls` is blank |

The cells are page URLs only. They do not contain an email address, a phone number, or a photo.

## Editor-panel columns added in `editors_ror_consistency3b_20261101`

Freeze `editors_ror_consistency3b_20261101` (published 2026-11-01) adds these columns after `board_url_count` on all nine current panels. The slim `editors_ft50_current.csv` also gains `ror_id`, `ror_name`, `ror_country`, and `continent`.

| Column | Meaning |
|--------|---------|
| `board_status` | Collector board status for the row's journal |
| `tenure_start_year`, `tenure_end_year` | Printed tenure years when the masthead gives them; blank otherwise |
| `snapshot_date`, `snapshot_source`, `board_year` | When and from what the board was captured, and the board year |
| `editor_row_key` | Stable row key; joins to `editor_affiliations.csv.gz` |
| `affiliation_count` | Number of affiliation parts parsed from `raw_affiliation` |
| `ror_id_aff_rank`, `primary_aff_basis` | Which affiliation part supplies the panel `ror_id`, and why |
| `former_flag` | Masthead marks the affiliation as former |
| `other_ror_ids` | `;`-separated ROR ids of the other affiliation parts |

Long table: `data/editors/releases/editors_nonlatin_inst_20261110/editor_affiliations.csv.gz`, one row per affiliation part (181,443 rows), keyed by `editor_row_key`. The previous consistency3b long table stays under `data/editors/releases/editors_ror_consistency3b_20261101/`.

## Pinned core49 backfill

`data/editors/core49/releases/editors_backfill_scale_ror_20261031/` holds the multi-year core49 panel (15,446 rows) with its long table, matched/unmatched audits, gaps, inventory, row-key crosswalk, and spot check. The crosswalk maps keys that shifted after a parse fix. Reports for both freezes are in `docs/reports/`.
