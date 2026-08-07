# DBpedia Ontology (DBO)

- **What it is** — The DBpedia Ontology is described as the heart of DBpedia: a shallow, cross-domain ontology that began from commonly used Wikipedia infoboxes and evolved through community-maintained ontology schema and infobox mappings. The fetched page reports a class subsumption hierarchy, thousands of properties, and millions of instances.

- **Key concepts** — Classes and properties form the TBox, while RDF type statements, object relations, literal facts, and normalized properties form ABox data. Since DBpedia 3.7, the class hierarchy is a directed acyclic graph rather than a tree, allowing multiple superclasses; infobox mappings normalize differing infoboxes, property names, datatypes, and parsing rules.

- **How you'd use it** — Download development or release-aligned ontology versions, query the ontology through DBpedia's SPARQL endpoint, obtain TBox and ABox dump files, browse the hierarchy and instances, or contribute mappings and ontology extensions through the public mappings wiki.

- **LLM angle** — none stated

- **Pitfalls & lessons** — Development snapshots and monthly dataset releases are distinct, so consumers must choose a version deliberately. Multiple inheritance means the ontology is not intrinsically a tree; the page says a taxonomy can be produced only by ignoring all but the first, most important superclass. The mapping system exists partly because raw Wikipedia infoboxes use inconsistent classes, property names, and datatypes.

- **Verdict** — Worth deeper study as a large, community-maintained cross-domain ontology tightly coupled to a public knowledge graph and an explicit mapping/release workflow.

## Sources consulted

- [https://www.dbpedia.org/resources/ontology/](https://www.dbpedia.org/resources/ontology/)
- `sources/dbpedia-ontology-dbo.txt`
