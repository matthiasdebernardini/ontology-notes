# FunOWL
- **What it is** — FunOWL is a pure-Python implementation of OWL 2 Functional-Style Syntax with a Pythonic API that stays close to the raw OWL functional model. It constructs and parses functional-syntax ontologies and can emit either OWL Functional Syntax or RDF through RDFLib. The project is no longer supported and directs users to migrate to `py-horned-owl`.
- **Key concepts** —
  - Ontologies are assembled from prefix declarations, ontology/version IRIs, imports, annotations, entity declarations, and axioms such as `SubClassOf`, `EquivalentClasses`, and `ClassAssertion`.
  - Class and data expressions shown in the documentation include intersections, unions, existential and universal restrictions (`ObjectSomeValuesFrom`, `DataSomeValuesFrom`, `DataAllValuesFrom`), and enumerated data values (`DataOneOf`).
  - One documented transformation turns selected classes expressed only through `SubClassOf` axioms into “fully defined entries” using `EquivalentClasses` and `ObjectIntersectionOf`.
  - Open-ended OWL productions are exposed with variadic Python constructors, avoiding the less natural requirement to wrap operands in a list.
- **How you'd use it** — Install the package and use `Ontology`, `OntologyDocument`, RDFLib `Namespace` objects, entity constructors, and axiom constructors to build an ontology, then call `str(...)` for Functional Syntax or `to_rdf(Graph())` for RDF serialization. `to_python` accepts Functional Syntax from a string, URL, file location, or open file; the `funowl` CLI converts a Functional Syntax file or URL to RDF and supports RDFLib output formats including Turtle, RDF/XML, JSON-LD, N-Triples, N-Quads, TriG, and TriX.
- **LLM angle** — none stated
- **Pitfalls & lessons** —
  - FunOWL is no longer actively maintained; the authors recommend migration to `py-horned-owl`, citing its active maintenance, faster Rust-backed parsing/serialization, broader format support, and OWL 2 conformance testing.
  - String CURIEs such as `ex:X` and `:Y` are stored as opaque strings rather than expanded; the migration guide recommends RDFLib `Namespace` values when using FunOWL so IRIs expand immediately.
  - FunOWL has no built-in method to retrieve all classes; its documented access path is the ontology's axiom collection.
  - The README says RDF-oriented Python OWL generation is time-consuming and error-prone, and notes that RDFLib's `infixowl` was close enough to the intended capability that the authors might have built on it instead of starting from scratch had they known about it.
- **Verdict** — A close-to-the-spec Python model and converter for OWL 2 Functional Syntax, useful for understanding or migrating existing FunOWL workflows but not a sound choice for new maintained work.

## Sources consulted
- `README.md`
- `docs/index.md`
- `UseCase.md`
- `ImplementationNotes.md`
- `MIGRATION_GUIDE.md`
