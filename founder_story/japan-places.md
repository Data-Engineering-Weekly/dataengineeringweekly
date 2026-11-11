# Building a Pay-Per-Call Data API as a One-Person Shop in Japan

*By Lexus — founder of RegBase / Japan Places*

I run a one-person data shop in Japan. My product is unglamorous:
structured data about Japanese places and companies, sold by the call.
This is the story of how the stack got built, and what running it alone
teaches you about data engineering.

## The corpus comes first

Everything sits on one corpus: 2,944,081 Japanese points of interest,
harvested from OpenPOI and Japanese government open data, refreshed on
a weekly harvest with a daily collection layer on top. Around it I
keep the reference datasets a location decision actually needs —
municipality census figures for 1,917 municipalities (2020 census),
station catchments, official land prices, and registry data.

The pipeline lesson I relearned the hard way: provenance is not
metadata you add later. Every record carries its source, licence and
fetch date, because the day a customer asks "can I legally ship this?"
the answer has to come from the data itself. I also publish a data
quality distribution for the corpus (200,000 POIs scored, mean score
84.9) as a free endpoint — if you sell data, your quality numbers
should be as easy to fetch as your prices.

## The 402 response is the price list

The API (20 OpenAPI paths) is pay-per-call over x402. Paid endpoints
answer HTTP 402 with machine-readable payment requirements; the
client settles in USDC on Base — $0.02 to $0.05 per call — and retries
the same request to get the data. Two endpoints, municipality census
and the quality distribution, are free with no key, so anyone can
verify the data is real before paying for anything.

Selling data this way removes the entire account layer: no signups,
no API keys to leak, no subscription tiers to design. For a
one-person shop that is not a philosophical choice, it is the only
support burden I can afford — zero.

## Records you can verify without trusting me

The second product line, RegBase, publishes Japanese corporate
registry records as Ed25519-signed JSON. A buyer fetches a record by
corporate number and verifies the signature locally; the same records
are served over MCP and as dated snapshot packs. "Trust the signature,
not the shop" is a much easier promise for a solo operator to keep
than uptime guarantees.

## MCP is a distribution surface, not a demo

The same 16 datasets are exposed as an MCP server
(`mcp-japan-places` on npm, zero-dependency Node, stdio). Agent
clients are becoming a real discovery channel for data products, and
the marginal cost of the MCP face was low because the tool canon is
generated from the live OpenAPI spec — the spec is the single source
of truth, and a drift check fails the build when the server and the
spec disagree.

## What I'd tell another solo data founder

Start with the corpus and its provenance, not the API. Pick a payment
rail that needs no accounts. Publish your quality metrics next to
your prices. And generate every client surface from one spec, because
a team of one cannot afford to keep three copies of the truth in sync
by hand.
