# Owlish

- **What it is** — Owlish is a Rust library providing OWL 2 data structures for building and working with ontologies. Its model follows OWL functional-style syntax, representing constructs such as `ClassAssertion(:Person :Mary)` with correspondingly shaped Rust tuple structs; the project also publishes Node.js/WASM packaging.
- **Key concepts** —
  - OWL functional-style constructs are represented directly as typed data structures rather than hidden behind a higher-level abstraction.
  - The documented/released model includes declarations and class assertions; object, data, and annotation properties; domains and ranges; equivalent classes, unions, and subproperty axioms; annotations and reification/resource IDs; and typed literals including numeric, boolean, date/time, and duration values.
  - Ontologies can be combined with `Ontology.append`; a planned “conceptual API” would concatenate OWL data for relevant types, but the README marks it TBD.
- **How you'd use it** — In Rust, use the low-level functional-syntax representation exported from `owlish::owl::*`. Releases document RDF-triple/Turtle parsing, parsing individual triples, Turtle serialization, JSON deserialization/mutation, and WASM bindings. In Node.js, read `owlish_bg.wasm` from the npm package with `fs` and pass its bytes explicitly to the module initialization function before calling Owlish APIs.
- **LLM angle** — none stated
- **Pitfalls & lessons** — The higher-level conceptual API is still marked TBD. Node.js initialization currently requires explicit WASM loading, and the changelog records that blank nodes are ignored rather than causing parser failure; it also documents repeated historical fixes around parser coverage, TypeScript types, annotations, and WASM integration.
- **Verdict** — A low-level, functional-syntax-shaped OWL 2 data model with Rust and WASM access plus documented RDF/Turtle tooling, but not a finished higher-level conceptual API.

## Sources consulted

- `README.md`
- `CHANGELOG.md`
