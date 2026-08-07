# N-Triples

**What it is**

N-Triples is a line-based plain-text serialization for RDF graphs and a subset of Turtle. It is a W3C format with the `.nt` extension and `application/n-triples` media type.

**Key concepts**

Each statement line contains a subject, predicate, object, and terminating full stop; subjects may be URIs or blank nodes, predicates must be URIs, and objects may also be literals. Comments begin with `#`, and statement-ending line breaks cannot be wrapped arbitrarily.

**How you'd use it**

Use it to store or transmit RDF in a representation that is simple for software to parse and generate. Its low representational variation also makes it convenient for expected “model answers” in RDF test suites.

**LLM angle**

none stated

**Pitfalls & lessons**

It lacks shortcuts such as CURIEs and nested resources, so large files can be onerous to type and difficult to read. Do not confuse it with Notation3, which the source identifies as a superset of Turtle.

**Verdict**

A deliberately simple, predictable RDF interchange and testing format, trading human compactness for ease of machine processing.

## Sources consulted

- https://en.wikipedia.org/wiki/N-Triples
- `sources/n-triples.txt`
