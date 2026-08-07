# owl-cli

- **What it is** — This repository now documents **Cool RDF**, the project formed by merging and updating the former `owl-cli` and `turtle-formatter`. It provides high-level Java libraries and the `cool` command-line tool for formatting and converting RDF documents, diagramming OWL ontologies, and performing OWL 2 DL reasoning.
- **Key concepts**
  - RDF graph edges have no serialization order, so two text files can differ while representing the same RDF model; the formatter therefore enforces reproducible ordering and configurable Turtle style, especially for version-controlled artifacts.
  - OWL visualization must make semantics explicit: putting properties inside UML-like class boxes is ambiguous because a property restriction and a property domain have different meanings.
  - Because OWL has no standardized graphical notation, Cool RDF defines one intended to represent all OWL axioms meaningfully, remain familiar to Protégé users, and cover element types, data ranges, class expressions, axioms, assertions, and SWRL rules.
  - The `infer` operation performs OWL 2 DL reasoning over an input ontology and writes the inferred result.
- **How you'd use it**
  - Install Java 25 or later and run the executable JAR as `cool`. `cool diagram ontology.ttl` produces an automatically laid-out SVG by default (PNG is also supported) through Graphviz `dot`.
  - Use `cool write` to read RDF/Turtle, RDF/XML, N-Triples, or N3 from a file, URL, or standard input and emit one of those formats. Turtle output exposes controls for prefixes, ordering, indentation, encoding, literal style, blank-node IDs, and related formatting choices.
  - Use `cool infer ontology.ttl -` to reason over an ontology and write to standard output. Ontology-taking commands also accept OWL API formats including Turtle, RDF/XML, OWL/XML, and OWL Functional Syntax.
  - In Java, the documented `cool-rdf-formatter` API takes an Apache Jena `Model` plus a `FormattingStyle` and returns or streams reproducibly formatted Turtle.
- **LLM angle** — none stated
- **Pitfalls & lessons**
  - The current CLI is named `cool`, not `owl`; migration also changed the build from Gradle to Maven, moved formatter packages to `cool.rdf.formatter`, and raised the Java requirement to 25.
  - No native executables are currently provided, and diagram generation needs the optional Graphviz dependency.
  - `cool infer` overwrites a file input when no output argument is supplied; pass an explicit output or `-` when that is not intended.
  - The graphical notation is project-specific because OWL has no standard diagram notation, and the diagrams target documentation rather than necessarily supporting interactive ontology editing.
  - The Java API page says documentation is not yet available for some libraries; only the formatter module is described there.
- **Verdict** — A focused utility for reproducible RDF serialization, static OWL diagram generation, and OWL 2 DL inference, with the formatter being the documented Java integration point.

## Sources consulted

- `README.md`
- `docs/src/docs/antora/modules/ROOT/pages/index.adoc`
- `docs/src/docs/antora/modules/ROOT/pages/cool-cli.adoc`
- `docs/src/docs/antora/modules/ROOT/pages/diagram-notation.adoc`
- `docs/src/docs/antora/modules/ROOT/pages/java-api.adoc`
- `docs/src/docs/antora/modules/ROOT/pages/release-notes.adoc`
