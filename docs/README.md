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

Every current editor CSV under `data/editors/*/releases/current/` ends with two columns. `scripts/build_site.py` selects columns by name and does not write either one to the site. `source_url` stays the primary board link.

| Column | Meaning |
|--------|---------|
| `board_urls` | Public board-page URLs, separated by `\|`. Filled only when that journal's board spans more than one page: IEEE Transactions on Intelligent Transportation Systems, Acta Turistica, Management: Journal of Contemporary Management Issues, and PASOS Journal of Tourism and Cultural Heritage; and, from `editors_browser_single_20261029`, Journal of Derivatives and Journal of Portfolio Management. Blank on every other row |
| `board_url_count` | Number of URLs in `board_urls`. Blank when `board_urls` is blank |

The cells are page URLs only. They do not contain an email address, a phone number, or a photo.
