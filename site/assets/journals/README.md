# Journal images

This directory holds local, small journal-specific cover thumbnails and logos.
`manifest.json` records each image's journal title, ISSN, official source page,
original image URL, review date, rights note, and SHA-256 checksum. It also lists
the reviewed FT50 titles that currently use initials. Additional pending candidates
and higher-priority unresolved sources are in `docs/journal-image-candidates.json`.

The shared `site/journal-icons.js` helper matches complete normalized journal
titles. It ignores a leading "The" and normalizes punctuation and `&`/`and`;
it does not infer identity from a publisher, a partial title, or an abbreviation.
Unmatched titles and failed image requests use initials in the same fixed slot.
Icons are decorative; the adjacent journal title and links remain the accessible
identity. Covers identify titles, not historical ranking editions or board dates.

When adding an image, verify its title on an official journal or publisher page,
inspect the artwork, save a small local asset, add its provenance to the manifest,
and update the helper's title-to-file map. Do not substitute a generic publisher
logo for a journal. Image sources are listed on `journal-icon-credits.html`, linked
from the site's main icon credits page.
