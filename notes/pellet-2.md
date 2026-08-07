# Pellet 2

- **What it is** — Pellet is an open-source, pure-Java OWL 2 DL reasoner. Its documented scope includes ontology consistency checking, taxonomy classification, entailment checking, inference explanations, and SPARQL/SPARQL-DL query answering; the repository offers it under AGPL or a commercial license.

- **Key concepts** —
  - **Consistency and satisfiability:** check whether an ontology is consistent and find unsatisfiable concepts.
  - **Classification:** compute or display the class/taxonomy hierarchy, optionally including instances.
  - **Entailment and explanation:** test entailments and explain inferred results.
  - **Ontology querying:** answer SPARQL-DL queries over OWL ontologies.

- **How you'd use it** — Run the bundled command-line interface, beginning with `pellet.sh help`, to check consistency, find unsatisfiable concepts, display hierarchies, or issue SPARQL-DL queries. Java applications can integrate Pellet through either Jena or the OWL API; the guide says the two packages provide almost equivalent functionality. A prebuilt distribution includes required libraries, while repository builds use Ant; SWOOP is named as a GUI that uses Pellet for reasoning.

- **LLM angle** — none stated

- **Pitfalls & lessons** — The repository-local FAQ contains no answers and redirects readers to an online FAQ for the latest version. The bundled guide documents a Java 1.5-compatible JVM, Ant 1.5+, and a Subversion-oriented build workflow; the README also cautions that Pellet 3.0 is a separate closed-source next-generation version embedded in Stardog.

- **Verdict** — A focused Java reasoner for OWL 2 DL validation, classification, explanation, entailment, and semantic querying through CLI, Jena, or OWL API integrations.

## Sources consulted

- `README.md`
- `doc/index.html`
- `doc/FAQ.txt`
