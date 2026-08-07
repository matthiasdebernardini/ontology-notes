# Horned OWL

- **What it is** — Horned OWL is a Rust library for processing and manipulating OWL documents inside Rust applications. It supports OWL 2 and SWRL, targets ontologies with millions of terms, and describes preliminary validation benchmarks as potentially 20–40× faster than competing OWL API-based implementations.
- **Key concepts** —
  - OWL 2 is the core ontology language, with profile reporting for EL, QL, RL, and DL.
  - SWRL rules are supported alongside OWL 2 ontologies.
  - Ontologies can import other ontologies; the `materialize` tool downloads and resolves an ontology's imports.
  - Parsing can be syntactically successful yet semantically incomplete when some RDF triples cannot be represented as ontology components. A visitor trait supports navigating and manipulating the resulting ontology structures.
- **How you'd use it** — Add `horned-owl = "2.1.0"` to a Rust project's `Cargo.toml`. The library reads and writes RDF/XML, OWL/XML, Functional Syntax, and Manchester Syntax; optional features add non-UTF-8 OWL/XML parsing (`encoding`) and non-local RDF/XML import resolution (`remote`). The `horned` CLI provides generation, parsing, validation, conversion, import materialization, profile checks, summaries, comparison, round-tripping, raw triple output, and inspection of unparsed content. The workspace also documents a pretty RDF/XML writer that produces more readable RDF/XML and can translate to and plug into the `oxrdfio` data model and serializers.
- **LLM angle** — none stated
- **Pitfalls & lessons** — Most parsing-oriented CLI tools exit successfully after a syntax-valid parse even when the ontology model is semantically incomplete; use `validate` for CI or scripts that require a hard failure, or inspect `unparsed`/`dump` output for the remainder. `triples` bypasses axiom construction, so incomplete ontology-model parsing does not apply to it. The reported 20–40× performance improvement is explicitly described as preliminary and potential.
- **Verdict** — A Rust-focused OWL 2/SWRL library and CLI suite for large-ontology parsing, manipulation, conversion, validation, import handling, and profile inspection.

## Sources consulted

- `README.md`
- `horned-bin/README.md`
- `horned-pretty-rdf/README.md`
- `doc/roadmap.org` (empty)
