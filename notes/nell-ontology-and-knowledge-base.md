# NELL ontology and knowledge base

**What it is**
This archived Linked Data server publishes the ontology and knowledge base produced by NELL, the Never-Ending Language Learning project in Carnegie Mellon’s Read-The-Web initiative. NELL has iteratively visited web pages and extracted knowledge from their unstructured content since January 2010, while NELL2RDF publishes that material as RDF.

**Key concepts**
Release identifiers combine the NELL2RDF software version with the source NELL iteration, so `0.3#1100` means software 0.3 over iteration 1100. The server offered vanilla RDF plus provenance modeled through RDF reification, n-ary relations, named graphs, singleton properties, or NDFluents, distributed as compressed N-Triples or HDT and licensed CC0 1.0.

**How you'd use it**
Download the ontology, NELL2RDF metadata ontology, and a dump matching the required provenance representation, or query the corresponding SPARQL endpoint using the documented anonymous credentials.

**LLM angle**
none stated

**Pitfalls & lessons**
The fetched page is an archived snapshot, and the provenance-rich dumps are much larger than the 315 MB vanilla HDT: listed variants range from 13.4 GB to 19 GB before zipped alternatives. Record both parts of the release identifier so the converter version and NELL iteration remain clear.

**Verdict**
A provenance-conscious RDF publication of web-extracted general knowledge, best approached through the dump variant that matches the project’s storage and provenance needs.

## Sources consulted
- https://web.archive.org/web/20241014060631/http://nell-ld.telecom-st-etienne.fr/
- `sources/nell-ontology-and-knowledge-base.txt`
