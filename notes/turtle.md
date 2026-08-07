# Turtle

**What it is**
Turtle (Terse RDF Triple Language) is a syntax and `.ttl` file format for expressing RDF graphs. It is a W3C Recommendation whose syntax resembles SPARQL and is intended to be more readable and manually editable than RDF/XML.

**Key concepts**
RDF statements are subject–predicate–object triples; Turtle abbreviates their URI-heavy representation with prefixes and shared subjects or predicates. It is a subset of Notation3, a superset of N-Triples, uses the `text/turtle` media type, and is always UTF-8.

**How you'd use it**
Declare prefixes, write RDF triples in compact form, and parse or serialize them with an RDF toolkit such as RDFLib, Jena, RDF4J, Redland, or N3.js.

**LLM angle**
none stated

**Pitfalls & lessons**
Turtle can serialize only valid RDF graphs, not the broader expressiveness of full Notation3. It does not itself support named graphs; TriG extends Turtle for that purpose.

**Verdict**
A compact, readable choice for authoring and exchanging ordinary RDF graphs.

## Sources consulted
- https://en.wikipedia.org/wiki/Turtle_(syntax)
- `sources/turtle.txt`
