# HyLAR

- **What it is** — HyLAR is a hybrid, location-agnostic, rule-based incremental reasoner for the Web. It combines an rdfstore.js triplestore with an incremental reasoning engine and can run as an npm module, a browserified client, or a server.

- **Key concepts** —
  - Ontologies are loaded and classified before being queried with SPARQL; loading can replace the knowledge base or retain its existing values.
  - Entailment covers RDFS and a documented subset of OWL 2 RL.
  - Custom business logic is expressed as forward-chaining conjunctive rules: one or more cause triples imply a consequence triple. Rule terms can be variables, URIs, or literals, and predicates can also be comparison operators.
  - The Triple Storage Manager separates direct triplestore operations from inferencing: its `query()` delegates to rdfstore.js and does not infer at that level.

- **How you'd use it** — Install `hylar` through npm, instantiate `Hylar`, call `load(rawOntology, mimeType, keepOldValues)`, then issue SPARQL with `query()`. The main API documents Turtle, N3, and JSON-LD input; the storage-manager documentation also describes RDF/XML conversion to Turtle. Add or remove named custom rules with `parseAndAddRule()` and `removeRule()`. For deployment, generate a browser bundle with `npm run clientize`, or install the global server and use its classify, query, and rule endpoints; server options select RDFS versus OWL 2 RL entailment and incremental versus tag-based reasoning, with tag-based reasoning providing proofs.

- **LLM angle** — none stated

- **Pitfalls & lessons** — HyLAR supports only a subset of OWL 2 RL and RDFS. OWL 2 RL axiomatic triples are not yet supported, while RDFS axiomatic support excludes axioms related to `rdf:Seq` and `rdf:Bag`. Direct queries through the Triple Storage Manager bypass inferencing.

- **Verdict** — A practical JavaScript reasoner when you need incremental RDFS or partial OWL 2 RL entailment, SPARQL access, and custom forward rules across local, browser, or server deployments.

## Sources consulted

- `README.md`
- `github-pages/main.md`
- `github-pages/stor.md`
