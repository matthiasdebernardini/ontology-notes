# pyfactxx

- **What it is** — `pyfactxx` provides Python bindings that connect the C++ FaCT++ reasoner to RDFLib. FaCT++ is an open-source reasoner for the **SROIQ(D)** description logic with simple datatypes (OWL 2).
- **Key concepts** — FaCT++ represents ontologies as terse directed acyclic graphs through atomic decomposition and applies a tableaux decision procedure for SROIQ(D). The README highlights normalization, synonym replacement, absorption, cycle elimination, backjumping, semantic branching, model merging, and taxonomy clustering among its optimization heuristics. Persistent reasoning saves inferred information and internal state for later reload, while incremental reasoning identifies change-affected inferences and recomputes only a subset.
- **How you'd use it** — Install with `pip install pyfactxx`; create a `coras.Coras` instance, load an ontology (the example uses Turtle), call `parse()` and `realise()`, then query through the unified SPARQL access point. The package also exposes the C++ interfaces RDFLib needs through the `coras` interface and adds improved individual precaching.
- **LLM angle** — none stated
- **Pitfalls & lessons** — OWL 2 reasoning has double-exponential worst-case time complexity, motivating the documented persistent and incremental modes. The linked work on direct C++ usage is explicitly described as unmaintained.
- **Verdict** — A focused RDFLib-facing route to optimized OWL 2/SROIQ(D) reasoning, including SPARQL access and persistence/incremental-reasoning support.

## Sources consulted

- `README.md`
