# ELOT

- **What it is** — ELOT is a literate ontology-engineering environment in which one plain-text Org notebook is both the ontology source and its documentation. It has an Emacs reference implementation, a VS Code extension, and an editor-independent CLI; the README says it has been used in scores of ontology projects, including ISO 23726-3.

- **Key concepts** —
  - The document outline carries formal meaning: headlines declare classes, properties, and individuals, while nesting expresses subclass or subproperty hierarchy.
  - Description-list rows attach annotations and OWL axioms, with axiom values written in Manchester Syntax; annotations can themselves be attached to annotations and axioms.
  - One source file may declare multiple ontologies. Under an Individuals section, an inherited and overridable `ELOT-subheading-relation` can make immediate-parent nesting assert relations such as `skos:broader`, so the outline is also the source of a SKOS hierarchy.
  - Identifier policy belongs to each ontology rather than to ELOT globally: documented schemes include UUIDs, label-derived slugs, formatted counters, and ACME identifiers, and custom schemes can be registered.
  - Queries, diagrams, prose, and formal content can live together: SPARQL `SELECT`/`CONSTRUCT` blocks and rdfpuml/PlantUML output form part of the same document.

- **How you'd use it** — Author an `.org` file in Emacs or VS Code, insert an ontology header and skeleton, then add resource headings and description-list axioms. Tangle Org to OWL Manchester Syntax, optionally use ROBOT to produce Turtle and perform ontology operations, import existing OWL into Org with the Java/OWLAPI `elot-exporter`, and export documentation to HTML or other Org/Pandoc formats. Emacs additionally runs in-place SPARQL and rdfpuml diagrams; `elot-cli` supplies Org-to-OWL, HTML export, and shared SQLite label-index management outside an editor. Label display, lookup, hover details, and cross-references help work with opaque CURIEs.

- **LLM angle** — The optional Emacs `elot-gptel` integration lets an LLM inspect resources and conventions, search labels, lint, query with SPARQL, run ROBOT-backed consistency/unsatisfiability/explanation checks, mint policy-compliant identifiers, and edit or restructure ELOT files. File writes are project-scoped, disabled by default, confirmation-gated, and revalidated with rollback; semantic reasoning remains a separate check from the automatic lint-and-parse validation. ROBOT is optional but required for conversion, SPARQL, reasoning, and report tools.

- **Pitfalls & lessons** —
  - The long-form manual is explicitly under construction; several manual files are stubs or drafts and may be inaccurate. The documentation status page identifies the root README and the gptel, toolsheet, and identifier documents as reliable.
  - Emacs is the reference implementation and receives features first; the documented VS Code matrix marks SPARQL, AI-assisted authoring, and diagrams as planned rather than available.
  - `elot-exporter` requires Java 21 or newer, while ROBOT and diagram tooling are separate optional dependencies.
  - Automatic LLM mutation validation checks lint and OWL parsing, not semantic consistency; run the separate consistency check after edits. A newly minted CURIE also cannot be used as an axiom subject in the same batch, so insertion and axiom editing require two calls.
  - Numeric-only counter identifiers are technically invalid XML NCNames, so an alphabetic counter template is recommended. ACME slugs are lossy and have finite per-slug/day random entropy; labels, not CURIEs, should carry human-readable meaning.

- **Verdict** — A strong fit when an ontology team wants a version-control-friendly Org document to be the shared source for OWL structure, explanatory prose, queries, diagrams, and guarded LLM-assisted editing, especially in Emacs.

## Sources consulted

- `README.md`
- `documentation/README.org`
- `documentation/elot-gptel.org`
- `documentation/elot-id.org`
