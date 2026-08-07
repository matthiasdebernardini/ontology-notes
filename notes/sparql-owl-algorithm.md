# SPARQL-OWL algorithm

**What it is**
This paper presents a sound and complete query-answering algorithm for SPARQL’s OWL 2 Direct Semantics entailment regime. Its prototype combines ARQ, the OWL API, and HermiT and supports variables in complex class expressions and bindings to class or property names.

**Key concepts**
Basic graph patterns are mapped to OWL axiom templates, simplified, split into connected components, and evaluated in a planned sequence. The optimizations include query reordering, rewriting, dedicated reasoner tasks, and exploitation of class/property hierarchies.

**How you'd use it**
Use the algorithm to answer ontology-aware SPARQL queries whose results depend on OWL entailment rather than simple RDF subgraph matching. Put selective axiom templates early and add restrictive templates for variables to reduce intermediate mappings and reasoning work.

**LLM angle**
none stated

**Pitfalls & lessons**
Compatible mappings can grow exponentially with the number of query variables, and even optimized execution may remain expensive. The evaluation was preliminary—LUBM plus custom GALEN queries on one constrained machine—and some unoptimized queries exceeded the 30-minute limit.

**Verdict**
A technically strong bridge from expressive SPARQL patterns to complete OWL reasoning; its reported gains of up to three orders of magnitude make optimization central rather than optional.

## Sources consulted
- http://ceur-ws.org/Vol-796/owled2011_submission_4.pdf
- `sources/sparql-owl-algorithm.txt`
