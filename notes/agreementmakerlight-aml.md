# AgreementMakerLight (AML)
- **What it is** — AgreementMakerLight is an automated, efficient ontology-matching system with a flexible, extensible framework. Its documented approach emphasizes element-level matching techniques supported by background knowledge, and the project reports strong results across several OAEI tracks.
- **Key concepts** —
  - Ontology matching is performed between a mandatory source ontology and target ontology.
  - Element-level matching can be supported by background knowledge.
  - An alignment can be supplied as a reference during matching or as the required input to alignment repair.
  - AML distinguishes automatic match, configurable manual match, and alignment-repair modes.
- **How you'd use it** — Download and extract the ready-to-run release, then launch `AgreementMakerLight.jar` with Java for the graphical interface or pass command-line options for the source ontology, target ontology, optional or required input alignment, and output alignment. The CLI supports automatic matching, manual matching configured through `store/config.ini`, and repair; AML does not save results unless an output path is given.
- **LLM angle** — none stated
- **Pitfalls & lessons** — The documented release was tested with Oracle Java 1.7, 1.8, and 1.9, while OpenJDK compatibility is not guaranteed. The authors also report Maven compilation errors and advise downloading the release instead of building with Maven for the time being.
- **Verdict** — A focused ontology matcher for generating or repairing alignments between two ontology files, with both GUI and CLI workflows and a documented emphasis on element-level methods plus background knowledge.

## Sources consulted
- `README.md`
