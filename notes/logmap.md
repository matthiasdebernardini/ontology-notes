# LogMap

- **What it is** — LogMap is a highly scalable ontology matching system with built-in reasoning and inconsistency-repair capabilities. It extracts mappings between classes, properties, and instances, and is intended to handle semantically rich ontologies containing tens or even hundreds of thousands of classes.

- **Key concepts**
  - Ontology matching can cover classes, properties, and instances rather than classes alone.
  - Reasoning and mapping repair are integrated to minimize logical inconsistencies in produced alignments.
  - User intervention and LLM validation can participate in the matching process.
  - A large alignment task can be divided into manageable subtasks; the repository describes this as a dedicated LogMap module.
  - A separate LogMap variant targets violations of the conservativity principle.

- **How you'd use it**
  - Run the standalone distribution from the command line as either an ontology matcher or a mapping-debugging system, or integrate LogMap into a Java application.
  - Supply formats supported by OWL API, including RDF/XML, OWL/XML, OWL Functional Syntax, OBO, KRSS, and Turtle (N3).
  - Build the Maven/Eclipse project with `mvn package` or `mvn clean install`; deploy the generated JAR alongside the generated `java-dependencies` directory and `parameters.txt`.
  - For OAEI workflows, use LogMap's MELT-platform wrapper/interface; HOBBIT support is also documented through a separate package.

- **LLM angle** — The README states that LogMap supports LLM validation during matching and points to LogMapLLM work described as using large language models as oracles for ontology alignment. It also documents related work that augments alignment with semantic or knowledge-graph embeddings and distant supervision.

- **Pitfalls & lessons**
  - The old web interface is not functional; a replacement is being pursued.
  - The OWL API 3 branch is explicitly non-maintained; the main project relies on OWL API 4.
  - The Google Translate dependency is not downloaded automatically and must be added manually to the local Maven repository.
  - Newer Java versions require documented VM arguments, including a module-opening flag and increased entity-expansion limit; the suggested configuration also allows a heap up to 25 GB.
  - LogMap-ML is marked as under development.

- **Verdict** — A documented fit for large-scale, logic-aware ontology alignment and mapping repair, with command-line, Java, and evaluation-platform integration plus emerging LLM/embedding extensions.

## Sources consulted

- `README.md`
