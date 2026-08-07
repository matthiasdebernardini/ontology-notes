# OWL-RL

- **What it is** — OWL-RL is a simple RDFLib-based implementation of the OWL 2 RL profile plus basic RDFS inference. It computes inference by forward chaining and can run RDFS and/or OWL-RL reasoning.

- **Key concepts** —
  - OWL 2 RL reasoning is presented as rule-based inference over RDF graphs; RDFS inference is also supported.
  - A deductive closure expands a graph with inferred triples, with an optional destination named graph for those results.
  - The documentation exposes datatype handling for XSD and RDF literal datatypes, including conversions for numeric, temporal, URI, binary, XML, HTML, language-tag-like, and string forms.

- **How you'd use it** — Install `owlrl` from PyPI with pip or Poetry; it requires RDFLib 7.6.0 or newer. In Python, pass an RDFLib `Graph` or `Dataset` to `owlrl.DeductiveClosure(...).expand(...)`; with the `oxigraph` extra, the same closure entry points accept a PyOxigraph in-memory `Store`. The package also ships a local `scripts/owlrl` file-to-RDF/stdout command and an adaptable CGI service.

- **LLM angle** — none stated

- **Pitfalls & lessons** — The Oxigraph integration is for compatibility, not speed: conversion to and from RDFLib objects removes most of Oxigraph's performance benefit, and inference still uses RDFLib types and logic internally. The CGI script may need adaptation to the local server setup. The dedicated Sphinx installation and usage pages are still marked “Coming soon.”

- **Verdict** — A narrowly scoped forward-chaining choice for materializing OWL 2 RL and RDFS inferences in RDFLib-oriented Python workflows.

## Sources consulted

- `README.md`
- `docs/source/index.rst`
- `docs/source/installation.rst`
- `docs/source/usage.rst`
- `docs/source/indices_and_tables.rst`
- `docs/source/stubs/owlrl.__index__.rst`
- `docs/source/stubs/owlrl.DeductiveClosure.rst`
- `docs/source/AxiomaticTriples.rst`
- `docs/source/AxiomaticTriples_source.rst`
- `docs/source/Closure.rst`
- `docs/source/CombinedClosure.rst`
- `docs/source/DatatypeHandling.rst`
- `docs/source/DatatypeHandling_source.rst`
- `docs/source/OWLRL.rst`
- `docs/source/OWLRLExtras.rst`
- `docs/source/RDFSClosure.rst`
- `docs/source/RestrictedDatatype.rst`
- `docs/source/XsdDatatypes.rst`
- `docs/source/XsdDatatypes_source.rst`
