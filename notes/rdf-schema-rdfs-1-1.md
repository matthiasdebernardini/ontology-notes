# RDF Schema (RDFS) 1.1

**What it is**
RDF Schema 1.1 is a W3C data-modeling vocabulary and semantic extension for RDF. It describes groups of related resources and their relationships using RDF itself.

**Key concepts**
Its core terms include classes and instances (`rdfs:Class`, `rdf:type`), transitive class and property hierarchies (`rdfs:subClassOf`, `rdfs:subPropertyOf`), global property domains and ranges, and human-facing documentation (`rdfs:label`, `rdfs:comment`).

**How you'd use it**
Define an application vocabulary, classify resources, organize class/property hierarchies, and state the classes to which property subjects and values belong. Applications may use domain/range information for inference, editing suggestions, or error discovery.

**LLM angle**
none stated

**Pitfalls & lessons**
Domains and ranges do not directly express restrictions local to one class, and multiple declarations mean membership in all declared classes. RDFS does not prescribe how applications act on this information, and the specification says RDF Semantics is authoritative if the two documents disagree.

**Verdict**
A compact, extensible vocabulary layer for RDF; use a richer ontology language such as OWL when the required meaning exceeds its deliberately basic facilities.

## Sources consulted
- https://www.w3.org/TR/rdf-schema/
- `sources/rdf-schema-rdfs-1-1.txt`
