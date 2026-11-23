# European public tender sources and imported-notice data

Published by [Contract Alerts](https://getcontractalerts.com/), an independent service matching public tenders to small businesses across Europe. Find sources, use free supplier resources and inspect dated aggregate counts from our imports. These are first-party resources, not an official publication, a complete procurement dataset or evidence of contracts won.

## Find work across Europe

- [European tender-search guide and country-source directory](https://getcontractalerts.com/guides/find-european-tenders): TED, national sources, practical searches and free official-alert instructions.
- [Choose a country and language](https://getcontractalerts.com/countries): all 43 supported markets, public sources and current notice samples.
- [Supplier reading notes and free bid checklist](SUPPLIER-RESOURCES.md): browser and printable tools, plus cleaning, grounds-maintenance, IT-support and refurbishment starting points.
- [Current source checks and coverage limits](https://getcontractalerts.com/coverage#current-imports): live aggregate figures after overnight imports.

## European snapshot: 23 November 2026

For a narrower view, see the [four-trade report](TRADE-INSIGHTS.md), captured separately at 21:26:59 UTC on 23 November. It breaks down cleaning, grounds maintenance, IT support and refurbishment by classification, stored country, source and time remaining. Its counts are dated imports, not the whole procurement market. [Download its JSON and CSVs](trade-snapshots/20261123T212659Z/).

Captured **2026-11-23T20:20:47.180668+00:00 (UTC)** from a read-only database transaction. The seven-day first-import window starts at 2026-11-16T20:20:47.180668+00:00 and includes both endpoints.

| Measure | Count |
| --- | ---: |
| Stored notice records | 13,255 |
| First imported during the seven-day window | 13,255 |
| Stored active-status records with a future response deadline | 12,878 |
| Supported country rows | 43 |
| Configured public source rows | 54 |

This launch batch includes notices published earlier. **First imported this week does not mean newly published this week.** Future deadlines are database fields, not a fresh check of whether the buyer still accepts bids. Records, countries and CPV groups can overlap. Do not sum country or classification rows to estimate unique procurements.

Download:

- [Counts, definitions, timestamps and provenance (JSON)](snapshots/2026-11-23T202047Z/snapshot.json)
- [Source import counts and public feed-check metadata (CSV)](snapshots/2026-11-23T202047Z/source-imports.csv)
- [Active future-deadline records by country (CSV)](snapshots/2026-11-23T202047Z/active-future-deadline-by-country.csv)
- [Active future-deadline records by broad CPV group (CSV)](snapshots/2026-11-23T202047Z/active-future-deadline-by-cpv-division.csv)
- [Active future-deadline records by UK region (CSV)](snapshots/2026-11-23T202047Z/active-future-deadline-by-uk-region.csv)

Country assignments use the recorded delivery country where supplied; national feeds can use their publishing market. Check the notice's actual delivery locations. The UK-region table does not describe the other European countries. Schema 2.0 explicitly requires stored active status for deadline populations; the historical schema 1.0 snapshot below used a different definition. Compare definitions before comparing counts.

The export includes no customer profiles, subscriber figures, private match assessments, notice titles, contacts, documents or attachments. Source URLs and last-check metadata are already public on the coverage page. A successful check is not a claim of exhaustive coverage. TED and national feeds can describe the same procurement.

All 54 source rows identify their public portals. TED, national portals across the EU and supported UK regional services are included in the current imports. Countries without a configured national connector can rely on TED or another supported cross-border feed; their presence does not imply complete national coverage.

The snapshot is static. No schedule is promised. Source notice rights remain with their publishers; this publication offers aggregate counts and explanations. See [licence and attribution](LICENSE.md). Run `python verify.py` to check hashes, CSV/JSON agreement, UTC windows and count relationships. These checks verify internal consistency, not completeness or suitability for bidding.

## Historical UK snapshot: 21 November 2026

**As of 2026-11-21T23:53:36.051653+00:00 (UTC).** The seven-day first-import window starts at 2026-11-14T23:53:36.051653+00:00 and includes both endpoints.

| Measure | Notice records |
| --- | ---: |
| First imported during the seven-day window | 176 |
| From Find a Tender | 154 |
| From Contracts Finder | 22 |
| Stored records with a future response deadline | 176 |
| Stored records without a usable deadline | 0 |

Download or inspect:

- [All counts, timestamps and definitions (JSON)](snapshots/2026-11-21T235336Z/snapshot.json)
- [Seven-day first imports by source (CSV)](snapshots/2026-11-21T235336Z/source-imports.csv)
- [Future-deadline notices by stored region (CSV)](snapshots/2026-11-21T235336Z/future-deadline-by-region.csv)
- [Future-deadline notices by broad CPV division (CSV)](snapshots/2026-11-21T235336Z/future-deadline-by-cpv-division.csv)

The CSVs are UTF-8 with a header row. Treat region and CPV codes as text when opening them in a spreadsheet: the CPV division `03` has a leading zero. Region rows include zero counts; the CPV table contains only groups with at least one record. Missing classification counts are separate fields in the JSON.

## What the figures mean

The source table measures **when Contract Alerts first imported a record**, rather than when the buyer published a notice. A batch import can include older publications. It cannot establish how many new opportunities appeared in the entire market during a week.

The region and CPV tables use a different population: all stored records whose parseable response deadline is later than the snapshot time. A future deadline does not establish the current legal or operational status of a procurement. Records with missing or unusable deadlines are excluded from those two tables and counted separately in the JSON.

A notice can appear in more than one region or CPV group. **Do not sum either table to estimate unique opportunities.** The importer uses delivery details, or the buyer's address when delivery information is missing. Postcode mapping is approximate and a buyer's location may differ from where work will be delivered. CPV labels here are simplified group labels used by Contract Alerts.

The importer keeps tender-tagged releases with active, planned or unstated status, excluding deadlines already past at import time. It uses source/OCID records and a normalized buyer-and-title heuristic to suppress some cross-source duplicates. This is not a verified count of unique procurements: updates, lots, similar titles, missing fields and source differences can affect the result. Stored classifications can differ from later source updates.

Imports are bounded and run periodically. Feed checkpoints record importer runs; they do not certify that every release was retrieved. At this historical snapshot, the two direct sources were Find a Tender and Contracts Finder. Current coverage has since expanded; see the European snapshot above and the live coverage page.

These aggregates contain no customer profiles, subscriber counts, private match assessments, notice-level contacts or tender documents. They do not measure contracts won, spending, supplier eligibility or AI matching accuracy.

## Resources for suppliers using these figures

The broad classification totals above are not ready-made lists of contracts your business can deliver.
Our [supplier reading notes](SUPPLIER-RESOURCES.md) explain that distinction and link to free official
search instructions, a free bid/no-bid checklist in browser and printable formats, current cleaning,
grounds-maintenance, IT-support and refurbishment notice lists,
and a comparison of free alerts with paid matching. These resources are published by Contract Alerts;
they are not independent reviews or government endorsements. The dated snapshot files remain unchanged.

## Sources and reuse

- [Find a Tender](https://www.find-tender.service.gov.uk/) — [OCDS API documentation](https://www.find-tender.service.gov.uk/Developer/Documentation).
- [Contracts Finder](https://www.contractsfinder.service.gov.uk/) — [API documentation](https://www.contractsfinder.service.gov.uk/apidocumentation/home).
- [Cabinet Office: published Find a Tender data and reuse](https://www.gov.uk/government/publications/procurement-act-2023-short-guides/buyers-and-suppliers-how-to-use-the-central-digital-platform-the-enhanced-find-a-tender-service-html).
- [Cabinet Office: Contracts Finder data and reuse](https://www.gov.uk/government/publications/ppn-0123-requirements-to-publish-on-contracts-finder/guidance-on-the-transparency-requirements-for-publishing-on-contracts-finder-html).

Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). See [LICENSE.md](LICENSE.md) for the scope and attribution for this publication. Contract Alerts is independent of government and neither source endorses this aggregation.

Suggested attribution: **Contract Alerts, imported-notice coverage snapshot, 2026-11-21T235336Z**, with a link to this repository and the OGL source attribution above. Cite the dated snapshot rather than treating the numbers as current.

## Updates, verification and corrections

This is a static, dated snapshot. No schedule or automatic updates are promised. The [current coverage page](https://getcontractalerts.com/coverage#current-imports) recalculates its figures from our database and can differ from this saved export.

`SHA256SUMS.txt` records file checksums for this publication. To check the files and their internal count relationships with Python 3, run `python verify.py`. This checks consistency, not completeness against the government feeds.

For corrections, open a repository issue with the snapshot timestamp and the field concerned, or contact [hello@getcontractalerts.com](mailto:hello@getcontractalerts.com). Avoid including private business details in public issues.
