# Contract Alerts imported-notice coverage data

Dated aggregate counts from [Contract Alerts](https://getcontractalerts.com/), an independent UK tender matching service. This resource describes the notices in our own imports. It is **not a complete UK procurement dataset**, an official government publication, or a live feed.

## Available snapshot

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

Imports are bounded and run periodically. Feed checkpoints record importer runs; they do not certify that every release was retrieved. We do not directly import Public Contracts Scotland, Sell2Wales or eTendersNI. Some records relating to those nations can still appear through the two supported national feeds.

These aggregates contain no customer profiles, subscriber counts, private match assessments, notice-level contacts or tender documents. They do not measure contracts won, spending, supplier eligibility or AI matching accuracy.

## Resources for suppliers using these figures

The broad classification totals above are not ready-made lists of contracts your business can deliver.
Our [supplier reading notes](SUPPLIER-RESOURCES.md) explain that distinction and link to free official
search instructions, a free bid/no-bid checklist, current cleaning and grounds-maintenance notice lists,
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
