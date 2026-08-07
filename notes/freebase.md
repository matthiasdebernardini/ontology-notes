# Freebase

**What it is**
Freebase was a data-sharing project that ran from 2007 to 2015; its API has been shut down. Google now hosts the last available dumps for citation and possible contribution to open-data and graph-database work.

**Key concepts**
The available artifacts include Freebase triples, deleted triples, and Freebase/Wikidata mappings. The main RDF snapshot uses UTF-8 N-Triples compressed with Gzip, while the mapping dataset links Freebase entities to Wikidata entities.

**How you'd use it**
Download the historical dumps for reproducibility, legacy graph analysis, or mapping old Freebase identifiers to Wikidata. When parsing the large RDF snapshot, the page recommends reading directly from the Gzip file rather than first expanding it.

**LLM angle**
none stated

**Pitfalls & lessons**
The dumps are substantially out of date, may contain information that was never accurate, are unmaintained, and come without support. The API is unavailable; Freebase dumps are CC BY, while the Freebase/Wikidata mappings are CC0.

**Verdict**
Useful as a frozen legacy dataset and identifier bridge, not as a current or supported knowledge service.

## Sources consulted
- https://developers.google.com/freebase/
- `sources/freebase.txt`
