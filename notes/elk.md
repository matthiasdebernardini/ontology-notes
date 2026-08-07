# ELK

- **What it is** — ELK is a Java-based ontology reasoner for the OWL 2 EL profile. It implements a polynomial-time, goal-directed consequence-based procedure for a fragment of OWL 2 EL and emphasizes concurrent, incremental reasoning and derivation explanations.
- **Key concepts** —
  - **Classification and class hierarchies:** ELK can classify an ontology and produce a taxonomy; class hierarchies are one of the reasoning results it can update.
  - **Incremental reasoning:** after ontology axioms change, ELK recomputes only results that depend on those axioms, which can make class-hierarchy updates nearly real time in many cases.
  - **Concurrent reasoning:** it can use multiple processor cores to accelerate reasoning-result computation.
  - **Explanations:** it can show, step by step, how a logical consequence follows from ontology axioms.
- **How you'd use it** — Run the standalone Java CLI to classify an ontology and save its taxonomy (`java -jar elk.jar -i pizza.owl -c -o pizza-taxonomy.owl`); use the `elk-owlapi` Maven dependency through the OWL API `OWLReasoner` interface for Java integration; or install the ELK reasoner plug-in in Protégé. The standalone parser accepts OWL 2 Functional-Style Syntax, and the packaged CLI documents `-h` for its available options.
- **LLM angle** — none stated
- **Pitfalls & lessons** — ELK's documented procedure covers a fragment of OWL 2 EL rather than unrestricted OWL. The standalone CLI cannot parse RDF/XML and accepts only OWL 2 Functional-Style Syntax, so other OWL formats must first be converted (the documentation suggests Protégé); larger classifications may also require increasing the Java heap.
- **Verdict** — A focused OWL 2 EL reasoner suited to fast classification, incremental updates, and explainable consequences through CLI, OWL API, or Protégé workflows.

## Sources consulted

- `README.md`
- `elk-distribution-parent/elk-distribution-cli/src/main/resources/README.txt`
- `elk-distribution-parent/elk-distribution-owlapi/src/main/resources/README.txt`
- `elk-distribution-parent/elk-distribution-protege/src/main/resources/README.txt`
- `elk-distribution-parent/elk-distribution-resources/src/main/resources/README.md`
