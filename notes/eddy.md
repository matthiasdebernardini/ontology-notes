# Eddy

- **What it is** — Eddy is a cross-platform graphical editor for specifying and visualizing Graphol ontologies. Its PyQt5/Qt5 design environment centers on a drawing viewport, with docked widgets for editing, navigation, and diagram inspection, plus design-time syntax validation that color-codes invalid expressions.

- **Key concepts** —
  - Graphol is a visual language for Description Logic ontologies intended to make ontologies understandable without requiring users to work in complex textual syntax.
  - Its graphical primitives are inspired by Entity–Relationship diagrams, so ontologies that can be rendered as ER diagrams retain a similar diagrammatic shape.
  - Eddy validates Graphol expressions while they are being designed. The README describes OWL 2 QL and RL profile support and marks OWL 2 EL support as “to appear”; these profiles are less-expressive OWL 2 fragments against whose syntax validation can run.

- **How you'd use it** — Draw and inspect a Graphol ontology in the desktop editor, choose an OWL 2 profile for profile-specific validation, and export the result as an OWL 2 ontology for third-party reasoners or editors such as Protégé; PDF export is also provided. The simplest installation is a bundled GitHub release, while PyPI/source installs require Python 3.9+ and Java 11+; launch those with `eddy` or `python3 -m eddy`.

- **LLM angle** — none stated

- **Pitfalls & lessons** — The documentation recommends a virtual environment because system Python packages can introduce dependency-version conflicts. A non-standard Java installation may require `JAVA_HOME`, and automatic JDK detection can fail. PyQt5 installation may hang when pip cannot find a wheel and starts a source build at a license prompt; source compilation can take a long time, particularly on platforms such as aarch64 Linux. Standalone Linux tarballs are deprecated in favor of AppImage or PyPI because AppImage builds are described as more reliable across distributions.

- **Verdict** — A focused visual Graphol authoring and validation tool whose documented interoperability path is OWL 2 export to the broader ontology-tool ecosystem.

## Sources consulted

- `README.md`
- `docs/install.md`
- `docs/dev.md`
- `docs/contributing.md`
