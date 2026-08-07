# N-Quads

**What it is**

N-Quads is a W3C RDF serialization with the `.nq` extension and `application/n-quads` media type. It is a superset of N-Triples that adds an optional context value in the fourth position.

**Key concepts**

Each illustrated statement contains an RDF subject, predicate, and object plus a graph/context IRI before the terminating full stop. The format also permits comments beginning with `#`.

**How you'd use it**

Use it when line-oriented RDF data must retain the graph or context associated with individual triples, such as serializing an RDF dataset rather than only one RDF graph.

**LLM angle**

none stated

**Pitfalls & lessons**

none stated

**Verdict**

A small extension of N-Triples suited to RDF data that needs explicit per-statement graph context.

## Sources consulted

- https://en.wikipedia.org/wiki/N-Triples#N-Quads
- `sources/n-quads.txt`
