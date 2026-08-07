# Apache Jena Ontology API

**What it is**

The Jena Ontology API is a Java programming interface for working with RDF-backed RDFS and OWL ontologies. It provides language-neutral ontology facets and convenience methods over the RDF triples in an `OntModel`, with configurable language profiles, storage, and reasoning.

**Key concepts**
- `OntModel` extends Jena's RDF `Model`; ontology objects do not hold separate state, and API operations read or assert underlying RDF triples.
- RDF resources can expose multiple Java facets, selected at runtime with `as()` and checked with `canAs()`.
- `OntSpecification` selects profiles and inference recipes; models may expose asserted plus entailed triples through the same model interface.
- `GraphRepository` supports recursive import closure while keeping the base ontology and imported graphs separate.

**How you'd use it**

Create an `OntModel` with the required OWL/RDFS profile and reasoner, read ontology data, then create or inspect classes, class expressions, properties, individuals, annotations, and imports through Java methods. Choose the base model when only asserted statements are wanted, or an inference-enabled model when applications should query entailments too.

**LLM angle**

none stated

**Pitfalls & lessons**

The documentation assumes RDF and Jena familiarity, covers the new API introduced since Jena 5.1.0, and directs readers to Javadoc for full detail. The default model uses OWL2 DL, in-memory storage, and built-in RDFS inference; inference can add many statements, cannot be distinguished from asserted statements through the combined model, and is often undesirable in editors. Imports are not loaded by a basic read unless the model is created with the specialized repository setup.

**Verdict**

A practical Java layer for manipulating RDF-native ontologies with optional inference and modular imports, provided callers deliberately choose the profile, reasoning behavior, and asserted-versus-inferred view they need.

## Sources consulted
- https://jena.apache.org/documentation/ontology/
- `sources/apache-jena-ontology-api.txt`
