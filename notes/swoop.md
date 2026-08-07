# SWOOP

- **What it is** — SWOOP v2.3 beta 3 is an OWL ontology browser and editor built around a standard web-browser UI paradigm, including an address bar, history, bookmarks, and hypertext navigation. It can load multiple web-based ontologies and render ontologies, classes, properties, and individuals in an accessible form.

- **Key concepts** —
  - OWL ontologies are navigated through named entities—classes, properties, and individuals—and can include arbitrary class expressions and general concept inclusions (GCIs).
  - Integrated reasoners support subsumption and consistency checking; Pellet additionally provides explanations for unsatisfiable classes, inconsistent ontologies, and inferred assertions.
  - SWOOP supports sound-and-complete conjunctive ABox queries written in RDQL, cross-ontology search, and finding references to named OWL entities.
  - Experimental partitioning transforms an ontology into an E-connection, while Crop Circles visualizes a class hierarchy.
  - Changes are logged and can be rolled back or undone; Annotea annotations can carry and distribute ontology change sets.

- **How you'd use it** — Start the Java 1.4 application with `runme.bat` on Windows or `runme.sh` on Mac/Unix, using the high-memory launcher for large ontologies such as NCI. Load ontologies from the web, browse or edit entities, switch between the bundled simple RDFS-like reasoner and Pellet, query with RDQL, search across loaded ontologies, compare entities, generate HTML, or export to a remote WebDAV store. Source and editing formats include RDF/XML, OWL Abstract Syntax, and Turtle; workspaces and ontology changes can be saved in SWOOP files (`*.swo`, `*.swp`). Its plugin system supports extensions.

- **LLM angle** — none stated

- **Pitfalls & lessons** —
  - With Pellet enabled, switching ontologies can be considerably slow because classified trees are cached but reasoner results are not.
  - Nested class expressions lack a form-based editor; the documented workaround is inline RDF/XML editing.
  - Large change logs render slowly. The suggested workarounds are saving the workspace, pruning the log, disabling change logging, or turning off change rendering.
  - Datatype enumerations lack RDF/XML rendering support, so affected ontologies cannot be serialized.
  - “Show References” ignores information from imported ontologies.

- **Verdict** — A web-browser-style OWL editor with rich reasoning, explanation, change-management, query, and serialization features, but with explicitly documented performance and editing/serialization limitations.

## Sources consulted

- `readme.txt`
