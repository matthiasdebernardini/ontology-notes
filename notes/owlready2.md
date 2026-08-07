# Owlready2

**What it is**
Owlready2 is an LGPLv3 package for ontology-oriented programming in Python. It loads OWL 2.0 ontologies as Python objects, supports modification and saving, and performs reasoning with the included HermiT reasoner.

**Key concepts**
The package combines Python-level OWL access with an SQLite3-based optimized triplestore/quadstore intended for large ontologies. Its documentation covers classes and individuals, properties, restrictions and logical operators, open and local closed-world reasoning, SWRL rules, general class axioms, annotations, namespaces, SPARQL, persistent or isolated worlds, parallelism, and the PyMedTermino2 integration for UMLS and medical terminology.

**How you'd use it**
Load or create an ontology in Python, manipulate its entities and axioms as objects, persist it to OWL or an SQLite-backed world, query it with SPARQL, and run HermiT for automatic classification and inferred results.

**LLM angle**
none stated

**Pitfalls & lessons**
none stated

**Verdict**
A feature-rich Python interface for applications that need both programmatic OWL manipulation and reasoning.

## Sources consulted
- https://owlready2.readthedocs.io/
- `sources/owlready2.txt`
