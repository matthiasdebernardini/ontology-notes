# Tawny-OWL

- **What it is** — Tawny-OWL is a Clojure domain-specific language for constructing OWL ontologies in an evaluative, functional, fully programmatic environment, implemented directly over the OWL API. Its Manchester-inspired textual syntax is intended to combine interactive ontology development with ordinary source control, extensible domain patterns, testing, packaging, dependency management, and continuous integration.

- **Key concepts**
  - The documentation defines an ontology as a computational representation of domain knowledge, normally expressed as concepts plus properties or relationships. OWL is a W3C language with description-logic semantics, enabling reasoners to infer conclusions and detect inconsistencies.
  - Ontology entities are built with frame-style forms: classes can have `:super`, `:sub`, `:equivalent`, and `:disjoint` frames, while OWL class expressions cover existential and universal restrictions, negation, union, intersection, cardinalities, values, and self restrictions. An equivalence definition gives necessary and sufficient membership conditions.
  - Asserted relationships and inferred relationships are deliberately separate: ordinary query functions inspect asserted axioms, while reasoner functions derive relationships. The reasoning docs distinguish satisfiability of classes, coherence of an ontology, and consistency when individuals are asserted.
  - Because the ontology is executable Clojure, repeated structures can become ontology-specific functions or patterns. Entities may also be built incrementally, which helps with mutual references and reusable modeling idioms.
  - Loading, importing, and reading are different operations: loading creates an OWL API object from a file; OWL importing makes another ontology's axioms participate in the current ontology and its reasoning; Tawny reading exposes imported entities as Clojure vars. Numeric IRI mappings and memorization files support stable, readable source names when upstream labels change.

- **How you'd use it**
  - Add the Clojars dependency to a Leiningen `project.clj`, import `tawny.owl`, declare an ontology with `defontology`, and define classes, object/data/annotation properties, individuals, axioms, and annotations in Clojure source.
  - Work interactively in a REPL to add, refine, inspect, or remove entities, then serialize with `save-ontology` in Manchester (`:omn`), OWL (`:owl`), or RDF (`:rdf`) form. Protege is documented as a useful read-only viewer for the generated ontology.
  - Select HermiT or ELK through `tawny.reasoner` for coherence, consistency, unsatisfiable-class, and inferred-hierarchy checks. Use `clojure.test` fixtures and probe entities to test expected inferences and disjointness, including ontologies authored outside Tawny.
  - Reuse existing OWL through OWL API loading, `owl-import`, or `tawny.read/defread`; filters and label-to-symbol transforms can make external ontologies usable as Tawny namespaces.

- **LLM angle** — none stated

- **Pitfalls & lessons**
  - Tawny is documented as an ontology-development interface first, not a conventional general-purpose Clojure API. Most operations mutate OWL API state and are not thread-safe; the implicit “current ontology” and dynamic scoping can make multiple ontologies awkward, so explicit ontology arguments are safer for API-style use.
  - Macro-based declarations require symbols to exist before use. String-based functional calls avoid that constraint but can silently create a new entity after a spelling mistake or let one IRI become both a class and a property, so the docs discourage casually mixing the two styles.
  - Lazy Clojure operations can appear to do nothing because ontology changes are side effects; the scripting guide recommends `doseq`, or forcing lazy sequences with `doall`.
  - Protege sees only generated OWL, not the abstractions that produced it, and edits in Protege do not update Tawny source. The docs also warn that Protege and Tawny may use different OWL API versions.
  - Reasoner availability is limited in the documented setup to mavenized HermiT and ELK. The default GUI progress monitor can be irritating in headless tests and can prevent the JVM from terminating unless replaced with the text or silent monitor.
  - The authors caution that ontologies are most worthwhile for sufficiently complex, categorical knowledge; probabilistic or heavily numerical domains are generally better served by statistical models.

- **Verdict** — Best suited to source-controlled, pattern-heavy OWL engineering that benefits from a REPL, automated reasoning, and tests; its own documentation positions general ontology manipulation as a secondary, less conventional use.

## Sources consulted

- `README.md`
- `docs/getting-started.md`
- `docs/what-is-owl.md`
- `docs/adding-restrictions.md`
- `docs/reasoning.md`
- `docs/querying.md`
- `docs/testing.md`
- `docs/importing.md`
- `docs/tawny-as-an-api.md`
- `docs/scripting.md`
- `docs/repl.md`
- `docs/protege.md`
- `docs/namespaces.md`
- `docs/nameclashes.md`
- `docs/obo.md`
- `docs/memorize.md`
- `docs/polyglot.md`
