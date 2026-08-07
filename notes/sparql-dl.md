# SPARQL-DL

**What it is**
SPARQL-DL is a substantial subset of SPARQL with semantics based directly on OWL-DL entailment. It is designed to combine TBox, RBox, and ABox queries while remaining implementable over standard services from existing OWL-DL reasoners.

**Key concepts**
Queries are conjunctions of typed atoms such as `Type`, `PropertyValue`, `SubClassOf`, `SubPropertyOf`, and property-characteristic tests. The paper defines their model-theoretic satisfaction, solution mappings, and translation into SPARQL basic graph patterns.

**How you'd use it**
Express mixed schema, property, and instance questions in the defined abstract atoms, translate them to RDF graph form, and evaluate them through an OWL-DL reasoner. The Pellet prototype first evaluates TBox/RBox atoms, substitutes their bindings, and reduces the remainder to ABox queries.

**LLM angle**
none stated

**Pitfalls & lessons**
Variables inside complex class expressions were excluded because they prevent reduction to standard reasoner services; arbitrary class expressions in results can also produce infinitely many answers. The prototype had no overall performance evaluation, did not support cyclic non-distinguished-variable ABox queries, and called broad queries such as `Type(?x, ?C)` impractical on a large ABox.

**Verdict**
A pragmatic middle ground between unstructured RDF query languages and less expressive DL query interfaces, with explicit expressiveness limits chosen for implementability.

## Sources consulted
- http://ceur-ws.org/Vol-258/paper14.pdf
- `sources/sparql-dl.txt`
