# Four public-contract trades: a dated view of imported notices

Published by Contract Alerts. Captured at **21:26:59 UTC on 23 November 2026**. This is a first-party analysis of our imports, not a complete European market report, an independent review or a count of contracts won.

[Download the one-page factsheet (PDF)](factsheets/european-tender-trade-snapshot-2026-11-23.pdf) for suppliers, advisers and trade organisations. It keeps the date, count definitions, caveats and links to the pinned data alongside the figures.

| Classification | CPV prefix | Stored active records with a future deadline | Due within 3 days | More than 7 days remaining |
| --- | --- | ---: | ---: | ---: |
| Cleaning | `9091` | 199 | 28 | 149 |
| Grounds maintenance | `773` | 137 | 18 | 103 |
| IT support / computer-related services | `725` | 44 | 1 | 35 |
| Refurbishment | `45453` | 103 | 22 | 64 |

The four groups contain **477 distinct stored records**. A record can belong to several groups, so their totals should not be added to estimate unique procurements. Source duplicates can also remain within a group. These are stored records with future deadlines, not notices verified as still accepting bids.

## Cleaning

The cleaning classification had 199 records; 28 had no more than three days remaining and 149 had more than seven. The practical lesson is to check the deadline before investing time in the specification. Then check buildings, travel, cleaning hours and staffing. A large total does not mean every record is a suitable cleaning lot.

This group uses CPV `9091`. Wider facilities management or pest-control work without that stored prefix is outside the count. [Current cleaning notices and selection checks](https://getcontractalerts.com/tenders/cleaning).

## Grounds maintenance

The grounds classification had 137 records, including 18 due within three days and 103 with more than seven days remaining. Check the site schedule and seasonal workload early: time to submit a bid does not establish that your team can cover the work when it starts.

This group uses CPV `773`, which includes horticultural services. It is not every landscaping or tree-work contract. [Current grounds-maintenance notices and selection checks](https://getcontractalerts.com/tenders/grounds-maintenance).

## IT support

The computer-services classification had 44 records, of which 35 had more than seven days remaining. That is time for an initial review, not proof of easy delivery. Check users, systems, support hours, security requirements and handover obligations before deciding to bid.

This narrow group uses CPV `725`. Hardware-only purchases, software development and support recorded only under other classifications are outside the count. [Current IT-support notices and selection checks](https://getcontractalerts.com/tenders/it-support).

## Refurbishment

The refurbishment classification had 103 records. Twenty-two were due within three days, while 64 had more than seven days remaining. For a contractor, the next question is whether there is time to inspect the site, review available surveys, confirm trades and price the work reliably.

This group uses CPV `45453`, rather than every construction or repairs classification. [Current refurbishment notices and selection checks](https://getcontractalerts.com/tenders/refurbishment).

## Use country and source counts carefully

### What does the feed mix tell us?

| Classification | Records assigned to TED | Records assigned to other public feeds | Total |
| --- | ---: | ---: | ---: |
| Cleaning | 39 | 160 | 199 |
| Grounds maintenance | 26 | 111 | 137 |
| IT support / computer-related services | 14 | 30 | 44 |
| Refurbishment | 15 | 88 | 103 |

These figures are derived from the `source_code` rows in [sources.csv](trade-snapshots/20261123T212659Z/sources.csv). Each stored record has one assigned source, so the two source columns add to the trade total. That assigned source can depend on import order and duplicate suppression. It does not establish whether the original procurement also appears on TED or another portal.

For a supplier, the useful next step is to combine relevant official sources and inspect the actual notice. The table cannot tell you how many additional unique contracts a particular feed provides, or whether paying for an alert service will find more suitable work than your own searches.

Feed concentration also affects country comparisons. For example, 69 cleaning records in this extraction were assigned to the Greek KIMDIS feed. Different publication and import scopes can make one feed prominent in our stored sample. Treat country totals as a description of this extraction when selecting sources to inspect, rather than a measure of national demand or an endorsement of a market.

### What can an adviser safely cite?

A precise statement is: “Contract Alerts recorded 199 active-status cleaning-classified notice records with future deadlines at 21:26:59 UTC on 23 November 2026, using stored CPV prefix 9091.” Link to the dated data and retain the definitions when reusing the figure. A claim about the total number of European cleaning contracts, or contracts available to a particular business, would require different evidence.

The downloads include all 43 supported country rows per trade and the source records behind each total. They are useful for understanding which parts of our imports contribute to a list. They are not a ranking of national demand or the best countries for a business to enter. National feeds have different scopes, import limits, classification quality and update behavior. Some national feeds assign their publishing market rather than the actual delivery country.

Country rows can overlap. A zero means no qualifying record in this particular extraction, not no public work in that country. Sources partition the stored records within a trade, but that does not remove real-world duplication between feeds.

## Downloads and definitions

Directory: [trade-snapshots/20261123T212659Z](trade-snapshots/20261123T212659Z/).

- [JSON: counts, classifications, definitions, UTC capture and provenance](trade-snapshots/20261123T212659Z/trade-snapshot.json)
- [CSV: four trade totals](trade-snapshots/20261123T212659Z/sectors.csv)
- [CSV: country counts](trade-snapshots/20261123T212659Z/countries.csv)
- [CSV: source counts and public portal references](trade-snapshots/20261123T212659Z/sources.csv)
- [CSV: remaining-time buckets](trade-snapshots/20261123T212659Z/deadlines.csv)

Extraction uses one SQLite read-only transaction and five public fields from the tender table: source, CPV, stored country codes, deadline and status. A record qualifies when stored status is `active` and its parseable deadline is strictly after capture. Timezone-free stored dates are interpreted as UTC. CPV membership uses stored strings beginning with the stated prefix. Duplicate CPV or country entries within a record count once.

Deadline buckets are mutually exclusive: more than zero up to three days, more than three up to seven, more than seven up to thirty, and more than thirty. Upper boundaries are included. All buckets use the same UTC capture instant. Source rows and deadline buckets each sum to their trade total; country rows need not.

The extraction contains no notice titles, buyer contacts, private customer profiles, subscriber counts, match scores, documents or tender values. Records with missing/unusable deadlines or other stored statuses are excluded from trade totals and counted in the JSON's population fields. Full notice documents and source rights remain with their publishers.

This is a static publication. It measures neither newly published notices this week nor demand growth. Do not compare its counts with another snapshot without comparing time, coverage and definitions. Run `python verify.py` and `python verify_trades.py` to check saved file hashes, JSON/CSV agreement and count relationships. They verify internal consistency, not the raw notices or market completeness.

Suggested attribution: **Contract Alerts, four-trade imported-notice snapshot, 23 November 2026, 21:26:59 UTC**, linking to this dated directory and [licence](LICENSE.md). Use a commit-pinned URL when quoting a specific downloaded version.
