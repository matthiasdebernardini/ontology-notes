# Whelk

- **What it is** — Whelk is an OWL reasoner based on the algorithm implemented by ELK. It represents reasoning state as an immutable functional data structure: adding axioms creates a new state while references to earlier states remain unchanged.

- **Key concepts** —
  - OWL EL classification is the core reasoning capability; Whelk also provides OWL RL and a subset of SWRL for reasoning over individuals.
  - Its persistent reasoner states support preclassifying and storing a shared ontology TBox, then independently extending it with multiple axiom sets such as ABoxes or rolling back to an earlier state.
  - Documented reasoning features include object-property-assertion materialization, SWRL class and object-property atoms, ABox-oriented OWL RL features, extended `Self` restrictions for rolification, and limited classification of unions in superclass position, such as inferring a common superclass of the union operands.

- **How you'd use it** — Use Whelk from application code when submitting many description-logic queries, running queries concurrently without blocking, or branching multiple reasoning workloads from a saved TBox classification. A basic OWL API `OWLReasoner` implementation is included, but the documented preferred route for its immutable-state features is the Scala API.

- **LLM angle** — none stated

- **Pitfalls & lessons** —
  - ELK is much faster for ordinary classification of a single ontology; Whelk targets workloads that benefit from persistent states, parallel queries, or its additional ABox/rule features.
  - Classification involving unions in superclass position is explicitly not guaranteed to be complete.
  - The project is under development and its Scala API is in flux; the OWL API interface is described as basic.

- **Verdict** — A specialized OWL reasoner for immutable, branchable, concurrent reasoning workloads and selected ABox/SWRL features, rather than a speed-first replacement for ELK on basic single-ontology classification.

## Sources consulted

- `README.md`
