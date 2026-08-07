# OWL 2 Web Ontology Language

**What it is**

OWL 2 is a W3C ontology language for the Semantic Web with formally defined meaning, representing classes, properties, individuals, and data values in Semantic Web documents. This W3C Recommendation is a non-normative overview and roadmap; OWL 2 itself is normatively defined across several core specification documents.

**Key concepts**

- An ontology can be viewed as an abstract structural object or as an RDF graph.
- RDF/XML is the mandatory interchange syntax for conformant tools; OWL/XML, Functional Syntax, Manchester Syntax, and Turtle serve other processing or readability needs.
- Direct Semantics supports OWL 2 DL and description-logic reasoning, while RDF-Based Semantics applies to any OWL 2 ontology as an RDF graph.
- The EL, QL, and RL profiles restrict expressivity to gain particular computational or implementation benefits: large-ontology reasoning, relational querying, or rule-based RDF processing.
- OWL 2 adds features over OWL 1 including keys, property chains, richer datatypes, qualified cardinalities, additional property characteristics, and enhanced annotations.

**How you'd use it**

Define and share a domain vocabulary with explicit relationships, serialize it in a tool-supported syntax, and use reasoners for class consistency, subsumption, or instance retrieval. Select EL, QL, or RL when its stated performance/implementation trade-off matches the application; use the Primer or Quick Reference for a more approachable entry point than the core specifications.

**LLM angle**

none stated

**Pitfalls & lessons**

This overview is informative rather than the normative language definition and notes that later documents may supersede it. OWL 2 DL requires syntactic conditions—for example, transitive properties cannot appear in number restrictions. Rule-based OWL 2 RL reasoning over an arbitrary RDF graph is sound but may be incomplete unless the ontology meets the RL structural definition and the stated query conditions.

**Verdict**

The authoritative starting map for understanding OWL 2’s syntax, semantics, profiles, and document suite, but implementation and conformance decisions must follow the linked normative specifications.

## Sources consulted

- https://www.w3.org/TR/owl2-overview/
- `sources/owl-2-web-ontology-language.txt`
