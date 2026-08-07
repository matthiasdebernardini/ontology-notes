# pyLODE

- **What it is** — pyLODE is a Python reimplementation of LODE that parses OWL/RDF with RDFLib and generates human-readable, static HTML ontology documentation. It also documents SKOS vocabularies and, through its `supermodel` mode, standalone or multipart models built from profiles and modules.
- **Key concepts** — It treats good ontology annotation as a prerequisite for good documentation and intentionally supports a conventional subset rather than translating every RDF statement. Its documented model includes `owl:Ontology` definitions, classes, properties, richer agent metadata, PROF profiles and resource descriptors, recursive graph closure for multipart models, `lode:Module` configuration, SHACL- or `schema:domainIncludes`-described class properties, label overrides, and vocabulary bindings to SKOS concept schemes.
- **How you'd use it** — Install it from PyPI and provide a local file or URL to the CLI, selecting `ontpub` for ontologies, `vocpub` for SKOS vocabularies, or `supermodel` for profiles/modules; output can be written as HTML, sorted, and emitted with or without embedded CSS. It is also usable as Python classes (`OntPub` and `VocPub`), a Falcon HTTP service, standalone executables, or Docker; remote ontology URLs served to the API must support RDF HTTP content negotiation.
- **LLM angle** — none stated
- **Pitfalls & lessons** — pyLODE deliberately does not render everything expressible in RDF, so unsupported patterns require a feature request and poorly annotated inputs produce poor results. A `supermodel` entry document must contain either an `owl:Ontology` or exactly one `prof:Profile`; imported resource descriptors are limited to Turtle, N-Triples, and N-Quads. Authors recommend keeping pyLODE-specific `lode:` statements out of published profiles and importing them separately with the `lode:config` role so downstream profiles can override documentation choices; the docs also mark configurable label predicates and downstream module disabling/ignore behavior as future or unsettled work.
- **Verdict** — A focused ontology-publication utility for turning conventionally annotated OWL, SKOS, PROF, and SHACL model descriptions into static HTML, not a general RDF-to-HTML renderer.

## Sources consulted

- `README.md`
- `supermodel.md`
