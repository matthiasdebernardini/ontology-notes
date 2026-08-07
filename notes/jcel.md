# jcel

- **What it is** — jcel is a Java reasoner for description logics in the EL family, described specifically as an EL+ / OWL 2 EL reasoner. It computes consequences from axioms and supports ontology classification and entailment through an OWL API interface, a Protégé plug-in, or a standalone application.

- **Key concepts** —
  - Description logics are presented as knowledge-representation languages and as formal foundations of the Semantic Web; a reasoner derives consequences from a set of axioms.
  - The documented operational fragment includes EL with general concept inclusions (top, conjunction, existential restriction, and subsumption), bottom, role hierarchies, transitive roles, and role composition.
  - Classification translates OWL API axioms into integer-based jcel axioms, detects expressivity, normalizes axioms (creating auxiliary entities when needed), saturates object-property deductions, applies completion rules to a fixed point, removes auxiliaries, and builds a graph of direct parents, children, and equivalent concepts.
  - The architecture separates all supported axioms and normalization from normalized axioms, classification algorithms, the reasoner, OWL API translation, and Protégé integration.

- **How you'd use it** — Use jcel as a Protégé plug-in, standalone application, or Java library. The documented Maven dependency is `de.tu-dresden.inf.lat.jcel:jcel-owlapi:0.24.1`; the standalone example invokes a JAR with `--ontology`, `--output`, and `--loglevel`, and the repository includes an OWL RDF/XML example ontology. The README also points to OWL and KRSS inputs and inferred XML outputs for several biomedical ontologies.

- **LLM angle** — none stated

- **Pitfalls & lessons** — The README explicitly says OWL 2 EL support currently has limitations. The FAQ marks inverse roles, functional roles, ABox assertions, and nominals as experimental; concrete predicates are planned; universal restrictions, disjunction, negation, and qualified or unqualified number restrictions are not planned. The release notes list version 0.25.0 as unreleased and version 0.24.1 (2017-04-28) as the latest dated release.

- **Verdict** — A focused EL-family ontology reasoner with clearly documented normalization/completion architecture and OWL API, Protégé, standalone, and library entry points, but with an explicitly bounded expressivity profile.

## Sources consulted

- `docs/README.md`
- `docs/faq.md`
- `docs/RELEASE-NOTES.md`
- `docs/data/start-jcel.sh.txt`
- `docs/data/example.owl`
