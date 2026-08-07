# SHACL (Shapes Constraint Language)

**What it is**
SHACL is a W3C Recommendation for describing RDF graphs through constraints on their content, structure, and meaning. It supports built-in constraints, extension through SPARQL or JavaScript, and SHACL Rules for inferring new statements.

**Key concepts**
Node shapes constrain nodes, property shapes constrain values reached through paths, constraints express requirements such as datatype, minimum count, length, ranges, patterns, and logical combinations, and targets select where shapes apply. Validation consumes a data graph and a shapes graph and emits an RDF validation-report graph with severities such as Violation, Warning, and Info.

**How you'd use it**
Create shapes for the resources or property paths you care about, assign targets, and run a SHACL engine against an RDF data graph. Use the report’s severity and messages to explain failures or suggest fixes.

**LLM angle**
none stated

**Pitfalls & lessons**
Targeting a class also targets members of its subclasses through `rdfs:subClassOf`. When a property shape is included by a node shape, the property shape’s own targets are ignored, so placement changes targeting behavior.

**Verdict**
A highly expressive, RDF-native validation language with clear targeting and machine-readable reports, plus extension and rule mechanisms when built-ins are insufficient.

## Sources consulted
- https://en.wikipedia.org/wiki/SHACL
- `sources/shacl-shapes-constraint-language.txt`
