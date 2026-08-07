# DBpedia Archivo

**What it is**
DBpedia Archivo is an ontology archive that automatically discovers OWL ontologies on the web, checks them every eight hours, and persistently archives changed snapshots on the Databus. At fetch time, its catalog reported 2,009 ontologies and exposed published-web and developer-version views.

**Key concepts**
- Archived ontology snapshots with Databus artifact links and downloads in OWL, Turtle, and N-Triples formats.
- A four-star “minimum viability” rating based on retrievability and parsing, license evidence and interoperability, and successful consistency checking.
- Per-entry metadata including triple count, semantic version, timestamps, addition date, parsing, license, consistency, LODE conformity, and crawling status.

**How you'd use it**
Use the list to discover an ontology, inspect its viability signals, follow its source or Databus record, and download the latest archived serialization. A missing ontology can be submitted through Archivo’s suggestion feature.

**LLM angle**
none stated

**Pitfalls & lessons**
A four-star rating is not a claim that an ontology is high quality; Archivo explicitly says its stars measure only minimum viability and minimal FAIRness. Lower ratings may reflect an ontology that cannot be retrieved or parsed, unclear or non-interoperable licensing, or a failed consistency check, all of which can impede later processing such as SPARQL, reasoning, or SHACL.

**Verdict**
A useful discovery, archival, and first-pass triage index for web ontologies, provided its stars are treated as viability checks rather than a quality ranking.

## Sources consulted
- https://archivo.dbpedia.org/list
- `sources/dbpedia-archivo.txt`
