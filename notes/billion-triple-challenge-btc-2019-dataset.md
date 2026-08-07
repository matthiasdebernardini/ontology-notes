# Billion Triple Challenge (BTC) 2019 Dataset

**What it is**

BTC 2019 is an open dataset produced by an LDspider crawl of RDF/XML, Turtle, and N-Triples documents from 12 December 2018 to 11 January 2019. It contains 2,155,856,033 quads from 2,641,253 RDF documents across 394 pay-level domains; merging them and removing duplicate triples yields 256,059,356 unique triples.

**Key concepts**

- Each quad’s fourth element records the Web document from which its triple was parsed.
- The release separates gzipped N-Quads, a deduplicated gzipped N-Triples graph, and a VoID statistics file.
- The quads/triples contain 38,156 unique predicates and instances of 120,037 unique classes.
- Files are divided by the top 100 contributing pay-level domains, with the remaining 294 domains combined; very large domain files are split at roughly 150 million quads.

**How you'd use it**

Use the N-Quads when source-document provenance matters, the deduplicated N-Triples for one merged RDF graph, and the VoID file for dataset statistics. The page recommends a streaming parser such as Raptor, RDF4j/Rio, or NxParser.

**LLM angle**

none stated

**Pitfalls & lessons**

The collection is highly skewed: Wikidata contributes 93.06% of all quads and 52.15% of unique triples, so raw counts should not be treated as balanced coverage of the Linked Data Web. Its scale also makes streaming processing important. Reuse is under CC BY 4.0, and the record asks research users to cite the accompanying BTC-2019 paper.

**Verdict**

A large, provenance-preserving snapshot suited to Web-scale RDF processing and dataset-analysis work, but its strong domain skew must be kept visible in any conclusions.

## Sources consulted

- https://zenodo.org/record/2634588
- `sources/billion-triple-challenge-btc-2019-dataset.txt`
