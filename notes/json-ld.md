# JSON-LD

**What it is**

JSON-LD (“JavaScript Object Notation for Linked Data”) is a W3C Recommendation for encoding linked data in JSON while retaining a form similar to traditional JSON. It is designed so linked-data semantics can be introduced by modifying JSON documents.

**Key concepts**

- An `@context` maps JSON properties and types to concepts in an ontology using the RDF model.
- Contexts may be embedded in a document or referenced for traditional JSON through an HTTP `Link` header.
- Values can be coerced to specified types or tagged with a language; `@id` and `@type` support IRI-based identity and typing.
- Resolvable IRIs let clients follow links to discover additional RDF data, and RDF processors can interpret mapped properties when they understand the vocabulary.

**How you'd use it**

Add a context to ordinary JSON to map application fields to vocabulary IRIs, identify entities unambiguously, and expose linked-data meaning to RDF-aware processors. The page reports use in Schema.org and search-engine optimization, biomedical informatics, provenance, Activity Streams/ActivityPub, and IoT Thing Descriptions.

**LLM angle**

none stated

**Pitfalls & lessons**

none stated

**Verdict**

A practical bridge between familiar JSON structures and RDF-linked semantics, with documented adoption across web metadata, federated activity data, provenance, biomedicine, and IoT.

## Sources consulted

- https://en.wikipedia.org/wiki/JSON-LD
- `sources/json-ld.txt`
