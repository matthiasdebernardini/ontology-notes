# yamlpyowl

- **What it is** — yamlpyowl reads ontologies—including individuals and SWRL rules—written in YAML and represents them as Python objects through `owlready2`. Its goal is to make manually authored ontologies more approachable for contributors who may not know Protégé or OWL syntaxes such as Manchester, while still supporting reasoning and RDF/XML export.

- **Key concepts** —
  - YAML declarations cover OWL classes, object and data properties, individuals, property facts, and SWRL rules; documented property characteristics include functional and transitive roles.
  - `X_RelationConcept` is a yamlpyowl extension for modeling n-ary relations: subclasses represent the relation, the parser creates an associated role, and `relation_concept_facts` creates concrete relation instances.
  - “Proxy individuals” represent knowledge about a class when metaclasses/punning are unavailable; `__create_proxy_individual` can generate individuals named `i<ClassName>`.
  - The zebra-puzzle notebook distinguishes asserted knowledge from facts inferred after synchronizing a reasoner, then queries the inferred graph with SPARQL.

- **How you'd use it** — Install with `pip install yamlpyowl`, author an `.owl.yml` file, and load it with `yamlpyowl.OntologyManager(path)`. Use the manager’s name-mapping container and underlying `owlready2` ontology to access entities and relations, call `sync_reasoner(infer_property_values=True)` for inference, issue SPARQL via `make_query`, or use the installed `yamlpyowl` CLI to convert YAML to RDF/XML. Python 3.8+ and Java are required.

- **LLM angle** — none stated

- **Pitfalls & lessons** — Ordinary documentation does not yet exist, and the authors describe yamlpyowl as an early prototype likely to be expanded and changed. The README also says `owlready2` and most OWL reasoners do not support metaclasses/punning, motivating the optional proxy-individual workaround.

- **Verdict** — A documented prototype for human-readable YAML ontology authoring that bridges into `owlready2` reasoning, SPARQL inspection, and standard RDF/XML export.

## Sources consulted

- `README.md`
- `doc/demo_notebooks/zebra_puzzle.ipynb`
