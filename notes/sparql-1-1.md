# SPARQL 1.1

**What it is**

SPARQL 1.1 Query Language is a W3C Recommendation defining the syntax and semantics of queries over RDF graphs. It supports data stored directly as RDF or exposed as RDF through middleware, and can return either solution sets or RDF graphs.

**Key concepts**

- Triple patterns generalize RDF triples by allowing variables; basic graph patterns match when RDF terms can be substituted for those variables to produce an equivalent subgraph.
- Graph patterns can combine required, optional, alternative, and negative matches; property paths compactly express traversal, including arbitrary-length paths.
- Queries run against an RDF dataset with one default graph and zero or more IRI-named graphs; `GRAPH` changes the active graph for part of a query.
- `SELECT` returns variable bindings, `CONSTRUCT` builds an RDF graph from templates, `ASK` reports whether a match exists, and `DESCRIBE` returns a service-determined description graph.
- Assignment, inline `VALUES`, aggregation, grouping, subqueries, expressions, and sequence modifiers such as `ORDER BY`, `DISTINCT`, `OFFSET`, and `LIMIT` shape the solutions.

**How you'd use it**

Write a `WHERE` graph pattern against the relevant default or named graphs, then choose the result form suited to the task: bindings with `SELECT`, a derived graph with `CONSTRUCT`, an existence check with `ASK`, or a service-generated resource description with `DESCRIBE`. Add filters, expressions, grouping, and explicit sequence modifiers when results need constraints, calculated values, aggregation, ordering, deduplication, or slicing.

**LLM angle**

none stated

**Pitfalls & lessons**

Pattern matches initially produce solutions in no specific order, so deterministic presentation requires `ORDER BY`. `DESCRIBE` output is determined by the query service rather than prescribed by the query. Queries using `FROM`, `FROM NAMED`, or `GRAPH` may dereference IRIs, consuming network, disk, or CPU resources; the specification also warns about denial-of-service, local `file:` access, firewall-indirection attacks, extension-specific risks, and visually confusable Unicode IRIs.

**Verdict**

This is the authoritative query-language reference: it combines examples with normative syntax, formal algebra and evaluation semantics, grammar, and conformance requirements. Its boundaries are explicit—resource descriptions are service-defined, and federated-query behavior is defined in a separate SPARQL 1.1 Recommendation.

## Sources consulted

- https://www.w3.org/TR/sparql11-query/
- `sources/sparql-1-1.txt`
