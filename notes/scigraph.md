# SciGraph

- **What it is** — SciGraph represents ontologies and ontology-encoded data as a Neo4j property graph. It is an OWL-centric, domain-agnostic loader and access layer with graph, vocabulary, annotation, and REST operations.

- **Key concepts** —
  - Ontologies are presented as formal, explicit specifications of shared conceptualizations that can serve as data, vocabulary, or semantics.
  - OWL classes, subclass relations, object properties, and existential restrictions are mapped into graph structure; the documentation stresses that “the IRI is king” and distinguishes IRIs, CURIEs, and fragments as identifiers.
  - Vocabulary support connects ontology identity to application features: label-to-node resolution, CURIE-to-IRI resolution, search, autocomplete, suggestions, OpenRefine resolution, and free-text entity identification.
  - The graph enables relationship-pattern queries across combined ontological and biological data, illustrated with subclass, phenotype, interaction, orthology, and sequence relationships.

- **How you'd use it** —
  - Ingest OWLAPI-supported formats—including OWL, RDF, OBO, and TTL—into Neo4j with the batch loader and YAML configuration; configuration can name ontologies, reasoner settings, categories, and mapped properties.
  - Consume the result directly through Neo4j/Cypher, add `scigraph-core` for convenience and vocabulary operations, or run `scigraph-services` as a Dropwizard REST service. The documented REST surface includes vocabulary lookup/search/autocomplete, lexical annotation, graph lookup/neighborhoods, and configurable domain-specific Cypher queries.
  - Graph endpoints can return `json-bbop`, GraphML, GraphSON, GML, JPEG, or PNG. Once generated, the graph can also be used by an application with no SciGraph dependency.

- **LLM angle** — none stated

- **Pitfalls & lessons** —
  - The mapping is explicitly lossy and does not round-trip ontologies; SciGraph does not create, manage, or version ontologies, is not a primary data store, and does not support CRUD operations.
  - Reasoning support is a stated non-goal. The presentation also says OWL mapping requires declarations in cases such as SKOS.
  - SciGraph is OWL-centric: an arbitrary SKOS ontology whose `skos:Concept` resources are not asserted as `owl:Class` will not expose those concepts to OWLAPI and they will not be loaded.
  - The authors list Neo4j limitations for this use: poor fit for global aggregate number crunching and binary/blob/object storage, Neo4j-specific Cypher, and a conceptual shift; an earlier presentation also flags replication.
  - Because Neo4j uses memory-mapped I/O, its database cannot be stored in a Vagrant shared directory.

- **Verdict** — A focused OWL-to-Neo4j ingestion and access toolkit for ontology-backed graph, vocabulary, and annotation services—not an ontology authoring, versioning, round-tripping, or general reasoning system.

## Sources consulted

- `README.md`
- `docs/presentation/20150211 SciGraph.pptx`
- `docs/presentation/20150801 SciGraph.pptx`
