# econ-journal-dispersion

Public research data for **Geographic Dispersion** work on economics (and related) journals.

**Repository:** https://github.com/kochiuyu/econ-journal-dispersion

**Editor directory:** https://kochiuyu.github.io/econ-journal-dispersion/

## What this repo is

Analysis-friendly **catalogs + release panels** only. Use the files under `data/*/releases/` for papers and coauthor analysis. Scrapes, HTML caches, RePEc dumps, and collector scripts stay in separate workspaces and are **not** versioned here.

## Journal universes

| Catalog | Path | Role |
|---------|------|------|
| **core49** | `journals/catalog_core49.csv` | Geographic Dispersion core economics journals |
| **FT50** | `journals/catalog_ft50.csv` | Financial Times Research rank journals |
| **ABDC** | `journals/catalog_abdc_{a_star,a,b,c}.csv` | 2025 ABDC Journal Quality List by rating |
| **Top 5** | `journals/catalog_top5.csv` | AER, Econometrica, JPE, QJE, and ReStud. Subset tag on the FT50 current release |
| **UTD24** | `journals/catalog_utd24.csv` | UT Dallas Naveen Jindal Top 24. Twenty-three journals tagged from the FT50 freeze; INFORMS Journal on Computing tagged from the ABDC A freeze |
| **ABS/AJG** | `journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/` | CABS Academic Journal Guide grades for 2010, 2015, 2018, 2021, and 2024, via the Editor-Collector freeze. Ratings, not editor boards. See `journals/rankings/STATUS.md` |
| **CNRS** | `journals/rankings/cnrs/releases/rankings_cnrs_20261024/` | Section 37 categories for 2011–2015 and 2017–2020. Ratings 1, 1e, 1g, 1eg, 2, 3, 4, plus domain |
| **Handelsblatt/VWL** | `journals/rankings/handelsblatt_vwl/releases/rankings_handelsblatt_vwl_20261024/` | Forschungsmonitoring weights for 1998–2020, plus the 2015 Handelsblatt list. Continuous weight, letter class when present |

Prefer joining on stable keys (`journal_slug` / `journal_id`, `year`, `doi`) — see `docs/README.md`.

## Data layout

```
data/
  editors/
    core49/          # STATUS only for now (wayback / multi-year panels still in collector)
    ft50/releases/current/
    abdc/releases/current/
  authors/           # STATUS only — stream still in progress (no 1GB caches here)
  affiliations/
    releases/canonical/   # TOC-first articles / affiliations / issues
```

**Rule:** analyze from `releases/` only. Do not treat collector folders or `STATUS.md` progress notes as frozen paper inputs until a release is pinned.

## Stream status (summary)

| Stream | State in this repo |
|--------|--------------------|
| Editors — FT50 | Current-board panels in `releases/current/` — freeze `editors_current_20261025` |
| Editors — ABDC A*/A/B/C | Current-board panels in `releases/current/` — same freeze (ROR-enriched where available) |
| Editors — core49 | Documented in `STATUS.md`; multi-year panels not yet copied into a pinned release |
| Affiliations (core49 TOC spine) | Canonical articles / affiliations / issues under `releases/canonical/` |
| Authors (core49) | **In progress** — see `data/authors/STATUS.md`; no analysis dump yet |

## Website

The site root is a short hub. The searchable directory of **current journal editors** is a separate page. Boards are the FT50 list and the ABDC A*, A, B, and C lists only. Top 5 and UTD24 are extra multi-select filters on those same boards. AJG chips are 2024 CABS grades tagged onto those rows. They do not add a separate board scrape, and the full guide is not in the directory. The directory also filters by institution (the row affiliation) and by ABDC field:

**https://kochiuyu.github.io/econ-journal-dispersion/**

**https://kochiuyu.github.io/econ-journal-dispersion/directory.html**

core49 is not included (it is an older ABDC A* subset, not a separate universe in this directory). Authors are out of scope.

`scripts/build_site.py` reads the current editor releases and writes `site/meta.json` plus `site/data/`. The hub fetches only `meta.json` (counts and per-list totals). The directory loads `site/data/shell.js`, then one file per list chip (`ft50.js`, `a_star.js`, `a.js`, `b.js`, `c.js`, `top5.js`, `utd24.js`, `ajg_4star.js`, `ajg_4.js`, `ajg_3.js`, `ajg_2.js`, `ajg_1.js`). A row is copied into every chip whose bit is set; the browser dedupes. The directory opens on FT50. Top 5 rows are already in that file. Other chips download when selected, or when a journal or institution link needs them. `?u=` names chips. `u=-` selects none. `?journal=` or `?aff=` with no `u` loads the chip set that contains that journal or affiliation. An old root URL with a directory query, or `#directory`, redirects to `directory.html`.

The directory is static HTML, CSS, and JS: a filterable table (name, role, journal, field, list, affiliation, country, continent), header counts, and a short note on the release. Institution is a typeahead over the lists loaded so far, not a menu of every affiliation. A name links to `faculty_profile_url` when that cell is filled. Many rows have no profile, and the page does not substitute a faculty home page or an ORCID, OpenAlex, or RePEc id. Emails, phone numbers, and photos are not published. `site/data.js` is not written.

One row is one person in one role on one journal. The same person on two journals is two rows. Where that same appointment is in both the FT50 release and an ABDC rating, the build keeps a single row and tags it with both lists (for example FT50 and ABDC A*). A Top 5, UTD24, or AJG grade keeps that badge on the same row. Wording comes from `editors_ft50_current_with_ror.csv`; a blank affiliation or country is filled from the ABDC row. The same name and role with two different affiliations stays two rows. The full rule is at the top of `scripts/build_site.py`.

Top 5 is American Economic Review, Econometrica, Journal of Political Economy, Quarterly Journal of Economics, and Review of Economic Studies (`journals/catalog_top5.csv`). UTD24 is the official UT Dallas list (`journals/catalog_utd24.csv`): 23 journals already in the FT50 freeze, plus INFORMS Journal on Computing from `editors_abdc_a_current.csv`. Journal of Applied Psychology stays on FT50 only.

AJG list chips and row badges show the grade from the 2024 edition (`journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/abs_ajg_2024.csv`), the latest edition in that freeze: AJG 4*, AJG 4, AJG 3, AJG 2, or AJG 1. The label does not include the year. The join includes 2024 `journal_id_crosswalk.csv` ids, so a board that uses an ABDC id still matches when the freeze's primary id is a core49 slug. That edition has 1,823 journals. 1,378 map to a catalog id, and about 1,356 of those are on a current board and can show a chip. The 445 unmatched titles never get a chip, and a small set of mapped titles are not on these boards. Many ABDC board journals have no AJG grade (about 2,400 board journal ids, against about 1,356 with a hit). The chips do not add boards. ABDC chips stay A*, A, B, and C. Full AJG editions stay on Rankings.

The directory institution field suggests the affiliation on loaded rows (ROR name, otherwise the canonical or masthead affiliation). It uses the same `aff` query the Institutions page already opens. Field is ABDC `field_for`, the same subject string as the Journals page, with the leading code hidden in the menu.

The same boards are also grouped by journal and by institution:

**https://kochiuyu.github.io/econ-journal-dispersion/journals.html**

**https://kochiuyu.github.io/econ-journal-dispersion/institutions.html**

`scripts/build_site.py` writes `site/journals-data.js` (one row per journal: list badges, appointments, distinct editors, countries, ABDC field, board link) and `site/institutions-data.js` (one row per ROR id, or per affiliation name when ROR is missing). A journal name opens `directory.html?journal=`. An institution name opens `directory.html` with `?aff=` set to that affiliation and `?country=` when the row has a country. Those files, `site/meta.json`, and `site/data/` are generated and are not committed.

Journal grades for every ranking system are also a separate page. The directory’s AJG chips are only the 2024 grades that match a current board:

**https://kochiuyu.github.io/econ-journal-dispersion/rankings.html**

`scripts/build_site.py` also runs `scripts/build_rankings.py`, which writes `site/rankings-data.js`. The Rankings page filters by ranking system, edition, rating, and field, and searches by journal title. Field is the ABS/AJG subject, the CNRS domain, or the ABDC `field_for`. Handelsblatt/VWL shows the published weight. FT50, UTD24, and Top 5 have no field and no grades. Systems on the page:

| System | Rows | What the filter shows |
|--------|------|------------------------|
| ABS/AJG | 7,245 | Editions 2010, 2015, 2018, 2021, 2024, ratings 4* / 4 / 3 / 2 / 1 (2010 has no 4*), from freeze `rankings_abs_ajg_20261024` |
| CNRS | 7,361 | Editions 2011–2015 and 2017–2020, ratings 1 / 1e / 1g / 1eg / 2 / 3 / 4, with domain, from freeze `rankings_cnrs_20261024` |
| Handelsblatt/VWL | 42,478 | Editions 1998–2020, continuous weight and letter class A+–F when present, from freeze `rankings_handelsblatt_vwl_20261024` |
| FT50 | 50 | April 2026 membership list. No grades |
| UTD24 | 24 | Membership list. No grades |
| Top 5 | 5 | Membership list. No grades |
| ABDC | 2,651 | 2025 list, ratings A* 219, A 630, B 861, C 941 |

The directory AJG chips are the 2024 grades that match a current board (AJG 4* through AJG 1). The full guide stays on this page. FT50, UTD24, and Top 5 are not given grades on the Rankings page. The other ABS/AJG editions stay there as grades.

### Local build

```bash
python scripts/build_site.py
python -m http.server 8000 -d site
```

Open http://127.0.0.1:8000/ for the hub and http://127.0.0.1:8000/directory.html for the editor table. Styles and scripts use relative URLs, so this is the same tree GitHub Pages serves under `/econ-journal-dispersion/` rather than at the user-site root. Journals are at http://127.0.0.1:8000/journals.html , institutions at http://127.0.0.1:8000/institutions.html , and rankings at http://127.0.0.1:8000/rankings.html . `site/meta.json`, `site/data/`, `site/journals-data.js`, `site/institutions-data.js`, and `site/rankings-data.js` are generated and are not committed.

### Enable GitHub Pages

`.github/workflows/pages.yml` builds the site on every push to `main` and deploys it with GitHub Actions. Once, in the repository settings:

1. **Settings → Pages**
2. **Build and deployment → Source: GitHub Actions**

If Pages is still set to “Deploy from a branch”, switch it to GitHub Actions. Until that source is selected, the workflow can succeed without the site updating. No custom domain is required. The live URL is https://kochiuyu.github.io/econ-journal-dispersion/ .

## License / citation

Dataset intended as **CC-BY-4.0**. See `CITATION.cff`.

Underlying board lists and TOCs are public journal mastheads / publisher pages; enrichment (ROR, OpenAlex) follows each provider’s terms.
