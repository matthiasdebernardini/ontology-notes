# OBO Format (OBOF)

**What it is**
This is the working-draft specification for OBO Flat File Format 1.4, providing a BNF grammar and a mapping to OWL 2 DL. It defines how physical OBO files parse into abstract documents, imposes structural constraints, and gives their semantics through OWL translation rules.

**Key concepts**
An OBO document has one header frame followed by zero or more term, typedef, or instance frames made of tag/value clauses. The specification covers identifiers and frame merging, tag cardinalities, header macros, OWL mappings, an `owl-axioms` escape hatch, the restrictive OBO Basic sublanguage, and informative OWL macros.

**How you'd use it**
Use it to implement or validate OBO parsers and serializers, translate OBO constructs into OWL 2 DL, or determine whether a document satisfies OBO Basic assumptions such as being a DAG, fully asserted, fully labeled, and free of imports and dangling clauses.

**LLM angle**
none stated

**Pitfalls & lessons**
The document labels itself a working draft and says some parts may be unstable. Translation into a sublanguage is generally lossy; arbitrary OWL axioms can round-trip through `owl-axioms` but remain opaque to many OBO applications; and the specification explicitly says OBOF is not a good choice for knowledge bases that use individuals.

**Verdict**
The authoritative source in this fetch for OBOF 1.4 syntax and OWL semantics, but its draft status and legacy-compatibility constraints matter when implementing against it.

## Sources consulted
- http://purl.obolibrary.org/obo/oboformat/spec.html
- `sources/obo-format-obof.txt`
