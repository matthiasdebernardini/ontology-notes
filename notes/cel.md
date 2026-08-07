# CEL

**What it is**

CEL is a lightweight description-logic reasoner aimed at large-scale biomedical ontologies. It reasons over EL+, the core expressive features of the tractable OWL 2 EL profile, and its main task is computing the subsumption hierarchy induced by an ontology using a polynomial-time algorithm.

**Key concepts**

- EL+ / OWL 2 EL reasoning tailored to medical and biological ontologies.
- Ontology classification and output as superclass sets, a direct subclass/superclass taxonomy, or an indented hierarchy.
- Supplemental features from version 1.0 including incremental classification, modularization, and axiom pinpointing.
- An OWL API wrapper and Protégé plug-in, plus a simple interactive interface and command-line mode.

**How you'd use it**

Load and classify an EL+ ontology from the CLI, emit its taxonomy or hierarchy, or start an interactive session with a preprocessed ontology. It can also act as the backend reasoner inside Protégé through the OWL API plug-in; module extraction is exposed for a concept or a signature.

**LLM angle**

none stated

**Pitfalls & lessons**

The site describes CEL as an OWL 2 EL reasoner “with some limitations,” and says extending expressivity toward EL++ is ongoing work. It also says the downloadable compiled releases are Linux 32-bit only; other platforms require compiling the Allegro Common Lisp sources.

**Verdict**

A focused choice when tractable classification of large EL+-style biomedical ontologies is the priority, provided its expressivity and platform constraints match the deployment.

## Sources consulted

- https://julianmendez.github.io/cel/
- Local fetched source: `sources/cel.txt`
