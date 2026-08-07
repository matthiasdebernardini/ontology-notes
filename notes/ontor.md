# ontor

- **What it is** — ontor (ONTology editOR) is a Python library built on Owlready2 for creating, editing, extending, debugging, visualizing, and reasoning over OWL2 ontologies. Each `ontor` instance represents one ontology.

- **Key concepts** —
  - Ontologies contain taxonomies, classes, object and data properties, individuals/instances, relations, restrictions, and axioms.
  - General Class Axioms express statements more complex than ordinary class axioms; ontor implements them through equivalent helper classes as an Owlready2 workaround. The documented seafood-pizza example shows a reasoner inferring a price for matching classes and instances without requiring an explicitly defined class for that concept.
  - Ontologies can import other ontologies, and deletion can preserve structure by appropriately reassigning subclasses and instances.

- **How you'd use it** — Install with `pip install ontor`, then create or load an ontology, edit it through ontor's tuple-based syntax, and save it; JSON and CSV are supported. The documented scratch workflow is `add_taxo` first, then `add_ops`/`add_dps`, followed by `add_axioms`/`add_gcas`/`add_instances`. You can extract axioms and class restrictions, run reasoning, interactively debug by deleting problematic axioms, and visualize selected classes, instances, and properties around a focus node.

- **LLM angle** — none stated

- **Pitfalls & lessons** — Creation order matters: the taxonomy must exist before properties, and properties before axioms or instances, because later steps depend on already-defined classes and properties. General Class Axioms require an equivalent-helper-class workaround in Owlready2.

- **Verdict** — A focused Owlready2-based editor for programmatic OWL2 ontology construction and maintenance, with structured import formats plus reasoning, debugging, and visualization support.

## Sources consulted

- `README.md`
- `docs/source/index.rst`
