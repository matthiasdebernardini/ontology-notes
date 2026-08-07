# ShEx (Shape Expressions)

**What it is**
Shape Expressions (ShEx) is a data-modeling language for describing and validating RDF graphs. Shapes may be written in the compact ShExC syntax or in RDF serializations such as JSON-LD or Turtle, then used to check whether RDF nodes conform.

**Key concepts**
ShEx combines Turtle/SPARQL-like syntax with semantics inspired by regular-expression languages such as RelaxNG. Shapes constrain properties, value types, references to other shapes, and cardinality—for example, requiring one string name and allowing zero or more links to nodes conforming to a person shape.

**How you'd use it**
Write shapes for the RDF node patterns your dataset should satisfy, then run a compatible implementation such as PyShEx, shex.js, Ruby ShEx, ShEx.ex, or Shaclex to validate data.

**LLM angle**
none stated

**Pitfalls & lessons**
Implementation support is uneven in the fetched comparison table, with many feature cells unknown or unsupported. One listed online demo is explicitly marked as a possible link-rot case.

**Verdict**
A concise, human-oriented way to make RDF structural expectations executable, provided the chosen implementation supports the needed features.

## Sources consulted
- https://en.wikipedia.org/wiki/ShEx
- `sources/shex-shape-expressions.txt`
