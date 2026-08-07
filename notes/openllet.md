# Openllet

- **What it is** — Openllet is an open-source, Java-based OWL 2 DL reasoner. Its documented capabilities are ontology consistency checking, taxonomy/class-hierarchy classification, entailment checking, inference explanations, and SPARQL or SPARQL-DL query answering through Jena, OWL API, or its command-line interface.

- **Key concepts** —
  - Reasoning services include deciding whether an ontology is consistent, finding unsatisfiable concepts, computing a class hierarchy (optionally with instances), checking whether axioms are entailed, and explaining inferences.
  - Pellint distinguishes axiom-level modeling patterns from patterns established across a whole ontology. It teaches that general concept inclusions, large disjunctions, large cardinalities, interacting existential restrictions, and large `DifferentIndividuals` sets can create nondeterminism, generated individuals, or high memory use in tableau-based reasoning.
  - Some constructs can also produce unintended entailments: for example, defining a named class as equivalent to an `allValuesFrom` restriction may classify things with no value for that property under the named class.

- **How you'd use it** — Add the `openllet-owlapi` or `openllet-jena` Maven dependency and invoke the reasoner from Java, or run `openllet.sh help` to discover CLI operations for consistency, unsatisfiable concepts, hierarchy display, and SPARQL-DL queries. Pellint accepts an ontology file or URI, can limit analysis to the root ontology or to RDF/OWL checks, can check RDF/XML resource typing, and can write selected repairs to a new ontology with `-f`.

- **LLM angle** — none stated

- **Pitfalls & lessons** —
  - The README says the project needs “a lot more tests.”
  - Since 2.6.5, Java 11 is required; migration also renamed many `com.clarkparsia.*` / `com.mindswap.*` packages into `openllet.*` and changed typing substantially.
  - The documented Protégé plugin requires a Protégé version using OWL API 5.1.x and is not compatible with Protégé’s main branch.
  - Pellint explicitly warns that its repairs are not semantically equivalent to the constructs they replace; they are intended only to improve reasoning time.
  - The authors caution that GCIs, disjunctions, large cardinalities, existential expansion, and many different-individual assertions can make reasoning time or memory intractable; several Pellint findings are warnings only and require remodeling the ontology.

- **Verdict** — A practical Java OWL 2 DL reasoning toolkit for classification, consistency, entailment, explanations, querying, and ontology-performance linting, with documented compatibility and scalability cautions.

## Sources consulted

- `README.md`
- `misc/doc/index.html`
- `tools-cli/README.md`
- `tools-pellint/README.txt`
- `tools-pellint/PATTERNS.txt`
- `tools-profiler/README.md`
