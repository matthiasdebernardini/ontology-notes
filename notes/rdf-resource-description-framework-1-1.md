# RDF (Resource Description Framework) 1.1

**What it is**
RDF is a W3C method for describing and exchanging graph data, originally designed as a metadata data model. Its abstract model is a labeled directed multigraph made of subject–predicate–object statements, with RDF 1.1 published in 2014.

**Key concepts**
Subjects and predicates are identified by IRIs; objects may also be blank nodes or literals. The same graph can be serialized as Turtle, TriG, N-Triples, N-Quads, JSON-LD, RDF/XML, and other formats, stored in a triplestore, and queried with SPARQL.

**How you'd use it**
Represent resources and relationships as triples, choose a suitable serialization, store the graph in a triplestore, and query it with SPARQL. RDFS, OWL, and SHACL can add vocabulary, ontology, or validation layers over RDF.

**LLM angle**
none stated

**Pitfalls & lessons**
Do not confuse RDF’s abstract graph model with RDF/XML, one serialization of it. Producers and consumers must agree on identifier semantics because that agreement is not inherent in RDF; blank nodes are also anonymous and not directly identifiable from a statement.

**Verdict**
A simple, flexible graph foundation for interoperable knowledge representation, with deliberate separation between the abstract model and its concrete syntaxes.

## Sources consulted
- https://en.wikipedia.org/wiki/Resource_Description_Framework
- `sources/rdf-resource-description-framework-1-1.txt`
