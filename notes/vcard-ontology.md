# vCard Ontology

**What it is** — A W3C Interest Group Note mapping vCard RFC 6350 to RDF/OWL for describing people and organizations with Semantic Web techniques. Its goal is compatibility between semantic vCard representations and traditional vCard implementations without changing RFC 6350 semantics.

**Key concepts** —
- The ontology keeps the `http://www.w3.org/2006/vcard/ns#` namespace for backward compatibility and also uses it as the JSON-LD context.
- URI-like resources are generally represented by OWL object properties named `hasX`, while literals such as strings and dates use data properties named `x`.
- Direct properties provide simpler resources; `hasValue`/`value` support n-ary structures when vCard property parameters require added metadata.
- Mapped kinds include Individual, Organization, Group, and Location; mapped fields cover identification, addresses, communications, geography, organizations, explanatory data, security keys, and calendar links.

**How you'd use it** — Represent contact data as RDF using the documented classes and properties, choosing direct relationships for simple values and n-ary relationships for parameterized values. The note supplies equivalent examples in RDF/XML, RDFa, Turtle, and JSON-LD, plus mapping tables from RFC 6350 properties.

**LLM angle** — none stated

**Pitfalls & lessons** — The note deprecates `rdf:value` for property parameters in favor of `hasValue`/`value`, and lists numerous deprecated or mapped terms from the previous ontology. Some RFC parameters are represented through general RDF mechanisms such as `rdf:type`, `rdf:Seq`, `rdf:Alt`, or `rdf:ID`, while others are unnecessary or assumed by the ontology.

**Verdict** — A detailed interoperability mapping for publishing RFC 6350-style contact information in RDF/OWL, with explicit migration guidance and serialization examples.

## Sources consulted

- https://www.w3.org/TR/vcard-rdf/
- `sources/vcard-ontology.txt`
