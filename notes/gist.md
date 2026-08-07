# gist

**What it is**
gist is Semantic Arts’ minimalist, domain-independent upper ontology for enterprise use. It aims to cover common business concepts with roughly 100 classes and a similar number of attributes and relationships while minimizing primitives and ambiguity.

**Key concepts**
It uses familiar top-level concepts such as person, organization, and agreement; extensive high-level disjointness to expose inconsistent typing; sparing domain/range constraints; and no inverse properties. Specialized enterprise or application ontologies can build on this foundation.

**How you'd use it**
Download or clone the release package, or import `https://w3id.org/semanticarts/ontology/gistCore` into Protégé, then extend gist with domain concepts while retaining its namespace rules. Releases include Turtle, RDF/XML, and JSON-LD serializations plus documentation and migration material.

**LLM angle**
none stated

**Pitfalls & lessons**
Major release 14.0.0 broke compatibility with earlier versions, although migration scripts were supplied; 14.1.0 is backward-compatible with 14.0.0. CC BY 4.0 use requires attribution, gist concepts must remain in the gist namespace, and users must not define their own terms there.

**Verdict**
A deliberately small enterprise foundation with practical modeling safeguards and multiple distribution formats; adopters should manage major-version migrations and namespace discipline.

## Sources consulted
- https://semanticarts.com/gist/
- `sources/gist.txt`
