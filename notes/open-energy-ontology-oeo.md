# Open Energy Ontology (OEO)

- **What it is** — The OEO is an open domain ontology for the energy-system-analysis context and part of the Open Energy Family. It represents standard terminology used by human experts to improve the transparency, comparability, and transferability of energy-system modelling and scenario analysis.

- **Key concepts** —
  - The ontology follows Basic Formal Ontology (BFO) principles and reuses external ontologies.
  - It has a modular structure: OEO-owned modules are collected separately from imported modules and assembled by the main ontology file.
  - Releases distinguish an asserted class hierarchy (`oeo-full.owl`) from a hierarchy inferred by the HermiT reasoner (`oeo-closure.owl`).
  - Ontology changes are treated as interdisciplinary work: content additions call for domain-expert review, restructuring for ontology-expert review, and changes involving both for both kinds of expertise.

- **How you'd use it** — Download a released OWL artifact, browse the inferred version through the TIB terminology service, or inspect it in the Open Energy Platform viewer. For editing, the repository uses Manchester OWL Syntax and recommends Protégé; contributors work in the appropriate module, validate the assembled ontology for inconsistencies, and submit changes through issues and reviewed pull requests. Individual classes can be referenced by label and full OEO URI.

- **LLM angle** — none stated

- **Pitfalls & lessons** — The ontology is continually extended, so the stable release, latest development branch, and inferred lookup view are distinct artifacts. Contributors are cautioned that the main `oeo.omn` file is usually not the correct place for a change, must check for introduced inconsistencies, and should merge promptly to reduce conflicts. Substantive proposals require discussion and domain/ontology review before implementation rather than unilateral edits.

- **Verdict** — A well-governed, modular ontology specifically scoped to shared terminology and formal organization for energy-system modelling and scenario analysis.

## Sources consulted

- `README.md`
- `CONTRIBUTING.md`
