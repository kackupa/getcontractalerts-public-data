# Four-trade tender import summary: 26 November 2026

Published by [Contract Alerts](https://getcontractalerts.com/), an independent tender-matching service. This is a first-party data resource. The guides, public notice lists and downloads linked here can be used without signing up.

## What does the summary count?

Stored active-status notice records with a future response deadline and the stated CPV prefix, captured at **2026-11-26T16:39:01.214028+00:00 UTC**. They are imported records, not unique procurements, complete market totals or confirmed invitations still open today. No live buyer-portal check was performed for this aggregation.

| Trade | CPV prefix | Notice records | Within 3 days | 3 to 7 days | 7 to 14 days | More than 14 days |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Cleaning | `9091` | 471 | 18 | 82 | 74 | 297 |
| Grounds maintenance | `773` | 307 | 14 | 34 | 35 | 224 |
| IT support | `725` | 96 | 5 | 14 | 10 | 67 |
| Refurbishment | `45453` | 222 | 8 | 35 | 53 | 126 |

The response-time labels are those of the saved publication, measured at capture time. They are not a current countdown. Groups and countries can overlap; do not add them to estimate unique contracts or market size. CPV is a classification, not confirmation that the scope fits a particular business. Read the original notice for current status, lots, scope and deadline.

## Download or cite the aggregate data

- [Sector counts and response-time buckets (CSV)](trade-summaries/20261126T163901Z/sectors.csv).
- [Aggregate counts, country rows, capture time and provenance (JSON)](trade-summaries/20261126T163901Z/summary.json).
- [Original dated publication and source examples](https://getcontractalerts.com/insights/tender-snapshot-2026-11-26).

The CSV is a byte-for-byte copy of the site's published download. The JSON retains its aggregate fields and omits all notice examples; its provenance records the source URL, original JSON checksum and transformation. No customer data, notice text, buyer contacts or attachments are included. The earlier saved publications in this repository remain unchanged.

Suggested citation: **Contract Alerts, four-trade tender import summary, 2026-11-26T16:39:01.214028+00:00**, with a link to this dated note and the [licence and attribution](LICENSE.md). Our aggregate counts and explanatory text use OGL v3.0; underlying notice rights remain with their respective publishers. A repository publication is not a government endorsement.

## Use the counts to start a practical review

- [Find council cleaning contracts](https://getcontractalerts.com/guides/find-council-cleaning-contracts): official search routes, suggested service searches and the first costing questions.
- [Review a grounds-maintenance tender](https://getcontractalerts.com/guides/grounds-maintenance-tender-checklist): site schedules, seasonal capacity, machinery, disposal and pricing assumptions.
- [Free bid or no-bid checklist](https://getcontractalerts.com/tools/tender-bid-checklist): six questions to identify the evidence needed for a first decision.
- [Choose a delivery country and official sources](https://getcontractalerts.com/countries), or review the [current coverage and limits](https://getcontractalerts.com/coverage).

Those resources are free. If sorting supported notices against a business profile is useful to you, [Contract Alerts explains its separate matching service and trial](https://getcontractalerts.com/how-it-works). It does not write or submit bids, verify eligibility or guarantee a suitable match.

## Verify the publication

Run `python verify.py` and `python verify_trades.py`. The recent-summary checks validate checksums, UTC capture time, the aggregate field allowlist, classification and country formats, response-time partitions and CSV/JSON agreement. They check internal consistency, not completeness against official portals or whether a notice remains open.
