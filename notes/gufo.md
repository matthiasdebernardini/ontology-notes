# gUFO

**What it is**

gUFO is a lightweight implementation of the Unified Foundational Ontology for Semantic Web OWL 2 DL applications. It selects a subset of UFO-A and UFO-B and is intended as an implementation artifact for structuring knowledge bases or knowledge graphs, rather than as a full reference ontology.

**Key concepts**

gUFO separates a taxonomy of individuals—such as objects, aspects, events, and situations—from a taxonomy of types, including kinds, phases, roles, categories, and relationship types. It also distinguishes endurants from events and situations, and provides patterns for parts, reified qualities, modes, relators, temporal boundaries, and quality values.

**How you'd use it**

Reuse its domain-independent distinctions by instantiating or specializing gUFO classes and properties in a lightweight ontology. For example, a domain class can both specialize `gufo:Object` and instantiate `gufo:Kind`, while concrete occurrences can instantiate `gufo:Event` and use the supplied temporal properties.

**LLM angle**

none stated

**Pitfalls & lessons**

“Lightweight” is a deliberate trade-off: gUFO uses limited expressiveness, includes only selected UFO-A/UFO-B material, and offers minimal UFO-B support. Some intended constraints are not declared when they would violate OWL 2 DL decidability rules; for example, proper parthood is described as asymmetric and irreflexive, but those characteristics are omitted from the implementation.

**Verdict**

A practical upper-level foundation when an OWL 2 DL knowledge graph needs UFO distinctions without importing the full reference ontology; its omissions and pragmatic formalization choices should be treated as part of the design contract.

## Sources consulted

- http://purl.org/nemo/doc/gufo
- `sources/gufo.txt`
